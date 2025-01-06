from typing import Literal

ServerRoutes = Literal[
    "/admin/database/clear",
    "/admin/database/create",
    "/admin/database/drop",
    "/admin/settings",
    "/admin/version",
    "/artifacts/",
    "/artifacts/{id}",
    "/artifacts/{key}/latest",
    "/artifacts/count",
    "/artifacts/filter",
    "/artifacts/latest/count",
    "/artifacts/latest/filter",
    "/automations/",
    "/automations/{id}",
    "/automations/count",
    "/automations/filter",
    "/automations/owned-by/{resource_id}",
    "/automations/related-to/{resource_id}",
    "/block_capabilities/",
    "/block_documents/",
    "/block_documents/{id}",
    "/block_documents/count",
    "/block_documents/filter",
    "/block_schemas/",
    "/block_schemas/{id}",
    "/block_schemas/checksum/{checksum}",
    "/block_schemas/filter",
    "/block_types/",
    "/block_types/{id}",
    "/block_types/filter",
    "/block_types/install_system_block_types",
    "/block_types/slug/{slug}",
    "/block_types/slug/{slug}/block_documents",
    "/block_types/slug/{slug}/block_documents/name/{block_document_name}",
    "/collections/views/{view}",
    "/concurrency_limits/",
    "/concurrency_limits/{id}",
    "/concurrency_limits/decrement",
    "/concurrency_limits/filter",
    "/concurrency_limits/increment",
    "/concurrency_limits/tag/{tag}",
    "/concurrency_limits/tag/{tag}/reset",
    "/csrf-token",
    "/deployments/",
    "/deployments/{id}",
    "/deployments/{id}/create_flow_run",
    "/deployments/{id}/pause_deployment",
    "/deployments/{id}/resume_deployment",
    "/deployments/{id}/schedule",
    "/deployments/{id}/schedules",
    "/deployments/{id}/schedules/{schedule_id}",
    "/deployments/{id}/work_queue_check",
    "/deployments/count",
    "/deployments/filter",
    "/deployments/get_scheduled_flow_runs",
    "/deployments/name/{flow_name}/{deployment_name}",
    "/deployments/paginate",
    "/events",
    "/events/count-by/{countable}",
    "/events/filter",
    "/events/filter/next",
    "/flow_run_notification_policies/",
    "/flow_run_notification_policies/{id}",
    "/flow_run_notification_policies/filter",
    "/flow_run_states/",
    "/flow_run_states/{id}",
    "/flow_runs/",
    "/flow_runs/{id}",
    "/flow_runs/{id}/graph",
    "/flow_runs/{id}/graph-v2",
    "/flow_runs/{id}/input",
    "/flow_runs/{id}/input/{key}",
    "/flow_runs/{id}/input/filter",
    "/flow_runs/{id}/labels",
    "/flow_runs/{id}/logs/download",
    "/flow_runs/{id}/resume",
    "/flow_runs/{id}/set_state",
    "/flow_runs/count",
    "/flow_runs/filter",
    "/flow_runs/history",
    "/flow_runs/lateness",
    "/flow_runs/paginate",
    "/flows/",
    "/flows/{id}",
    "/flows/count",
    "/flows/filter",
    "/flows/name/{name}",
    "/flows/paginate",
    "/health",
    "/hello",
    "/logs/",
    "/logs/filter",
    "/ready",
    "/saved_searches/",
    "/saved_searches/{id}",
    "/saved_searches/filter",
    "/task_run_states/",
    "/task_run_states/{id}",
    "/task_runs/",
    "/task_runs/{id}",
    "/task_runs/{id}/set_state",
    "/task_runs/count",
    "/task_runs/filter",
    "/task_runs/history",
    "/task_workers/filter",
    "/templates/validate",
    "/ui/flow_runs/count-task-runs",
    "/ui/flow_runs/history",
    "/ui/flows/count-deployments",
    "/ui/flows/next-runs",
    "/ui/schemas/validate",
    "/ui/task_runs/count",
    "/ui/task_runs/dashboard/counts",
    "/v2/concurrency_limits/",
    "/v2/concurrency_limits/{id_or_name}",
    "/v2/concurrency_limits/decrement",
    "/v2/concurrency_limits/filter",
    "/v2/concurrency_limits/increment",
    "/variables/",
    "/variables/{id}",
    "/variables/count",
    "/variables/filter",
    "/variables/name/{name}",
    "/version",
    "/work_pools/",
    "/work_pools/{name}",
    "/work_pools/{name}/get_scheduled_flow_runs",
    "/work_pools/{work_pool_name}/queues",
    "/work_pools/{work_pool_name}/queues/{name}",
    "/work_pools/{work_pool_name}/queues/filter",
    "/work_pools/{work_pool_name}/workers/{name}",
    "/work_pools/{work_pool_name}/workers/filter",
    "/work_pools/{work_pool_name}/workers/heartbeat",
    "/work_pools/count",
    "/work_pools/filter",
    "/work_queues/",
    "/work_queues/{id}",
    "/work_queues/{id}/get_runs",
    "/work_queues/{id}/status",
    "/work_queues/filter",
    "/work_queues/name/{name}",
]