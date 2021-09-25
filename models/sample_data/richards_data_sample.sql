with source_richards_data as (
    select * from {{ source('richards_sample_data', 'sensor_data') }}
),

final as (
    select * from source_richards_data
)

select * from final