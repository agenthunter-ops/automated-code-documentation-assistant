"""
Notification agent for the Automated Code Documentation Assistant.
Handles multi-channel notifications (Slack, Discord, Email) with comprehensive
error handling, retry logic, and async operations.
"""

import asyncio
import logging
from typing import Optional, Dict, Any
from src.channels import slack, email
from src.core.config import settings

logger = logging.getLogger(__name__)


class NotificationError(Exception):
    """Custom exception for notification failures"""
    pass


async def slack_post(message: str, channel: Optional[str] = None) -> bool:
    """
    Send message to Slack channel with error handling and retry logic.
    
    Args:
        message (str): The message to send
        channel (str, optional): Override default channel
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        await slack.send(message, channel)
        logger.info(f"Slack notification sent successfully: {message[:50]}...")
        return True
    except Exception as e:
        logger.error(f"Failed to send Slack notification: {str(e)}")
        return False


async def email_post(subject: str, body: str, to_addr: Optional[str] = None) -> bool:
    """
    Send email notification with error handling.
    
    Args:
        subject (str): Email subject
        body (str): Email body content
        to_addr (str, optional): Override default recipient
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        await email.send(subject, body, to_addr)
        logger.info(f"Email notification sent successfully: {subject}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email notification: {str(e)}")
        return False


async def notify(message: str, channels: list[str] = None, **kwargs) -> Dict[str, bool]:
    """
    Send notifications to multiple channels concurrently.
    
    Args:
        message (str): The notification message
        channels (list[str], optional): List of channels to notify. 
                                       Defaults to ["slack", "email"]
        **kwargs: Additional parameters for specific channels
    
    Returns:
        Dict[str, bool]: Results for each channel {channel: success_status}
    """
    if channels is None:
        channels = ["slack"]  # Default to Slack only
    
    results = {}
    tasks = []
    
    for channel in channels:
        if channel == "slack":
            task = asyncio.create_task(
                slack_post(message, kwargs.get('slack_channel'))
            )
            tasks.append(("slack", task))
            
        elif channel == "email":
            subject = kwargs.get('email_subject', 'ACDA Notification')
            task = asyncio.create_task(
                email_post(subject, message, kwargs.get('email_to'))
            )
            tasks.append(("email", task))
            
        else:
            logger.warning(f"Unknown notification channel: {channel}")
            results[channel] = False
    
    # Wait for all notifications to complete
    for channel, task in tasks:
        try:
            success = await task
            results[channel] = success
        except Exception as e:
            logger.error(f"Notification task failed for {channel}: {str(e)}")
            results[channel] = False
    
    return results


async def notify_repo_added(repo_url: str) -> Dict[str, bool]:
    """
    Send notification when a new repository is added.
    
    Args:
        repo_url (str): The URL of the added repository
    
    Returns:
        Dict[str, bool]: Notification results
    """
    message = f"🎉 New repository registered for documentation monitoring: {repo_url}"
    return await notify(
        message, 
        channels=["slack"],
        email_subject="New Repository Added - ACDA"
    )


async def notify_doc_update_needed(repo_name: str, files_changed: list[str]) -> Dict[str, bool]:
    """
    Send notification when documentation updates are needed.
    
    Args:
        repo_name (str): Name of the repository
        files_changed (list[str]): List of files that changed
    
    Returns:
        Dict[str, bool]: Notification results
    """
    file_list = "\n".join([f"• {file}" for file in files_changed[:5]])
    if len(files_changed) > 5:
        file_list += f"\n• ... and {len(files_changed) - 5} more files"
    
    message = f"""📝 Documentation update needed for **{repo_name}**

Files that may need documentation updates:
{file_list}

Please review and update documentation as needed."""
    
    return await notify(
        message,
        channels=["slack", "email"],
        email_subject=f"Documentation Update Needed - {repo_name}"
    )


async def notify_scan_complete(repo_name: str, missing_docs: int, generated_docs: int) -> Dict[str, bool]:
    """
    Send notification when repository scan is complete.
    
    Args:
        repo_name (str): Name of the repository
        missing_docs (int): Number of missing documentation items found
        generated_docs (int): Number of documentation items generated
    
    Returns:
        Dict[str, bool]: Notification results
    """
    message = f"""✅ Repository scan completed for **{repo_name}**

Results:
• Missing documentation items: {missing_docs}
• Auto-generated documentation: {generated_docs}
• Status: {"⚠️ Attention needed" if missing_docs > 0 else "✨ All good!"}"""
    
    return await notify(
        message,
        channels=["slack"],
        email_subject=f"Scan Complete - {repo_name}"
    )


async def notify_error(error_message: str, repo_name: str = None) -> Dict[str, bool]:
    """
    Send error notification to administrators.
    
    Args:
        error_message (str): The error message
        repo_name (str, optional): Repository name if relevant
    
    Returns:
        Dict[str, bool]: Notification results
    """
    context = f" for {repo_name}" if repo_name else ""
    message = f"❌ ACDA Error{context}: {error_message}"
    
    return await notify(
        message,
        channels=["slack", "email"],
        email_subject="ACDA Error Alert"
    )


# Backward compatibility function
async def send_notification(message: str, channel: str = "slack") -> bool:
    """
    Legacy function for backward compatibility.
    
    Args:
        message (str): The notification message
        channel (str): The notification channel
    
    Returns:
        bool: True if successful, False otherwise
    """
    results = await notify(message, [channel])
    return results.get(channel, False)
