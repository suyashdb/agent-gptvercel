from typing import Any, Dict, List

from pydantic import BaseModel

from reworkd_platform.schemas.workflow.base import Node


class WorkflowTaskEvent(BaseModel):
    workflow_id: str
    user_id: str

    queue: List[Node]
    outputs: Dict[str, Any]

    @classmethod
    def from_workflow(
        cls, workflow_id: str, user_id: str, work_queue: List[Node]
    ) -> "WorkflowTaskEvent":
        return cls(
            workflow_id=workflow_id,
            user_id=user_id,
            queue=work_queue,
            outputs={},
        )
