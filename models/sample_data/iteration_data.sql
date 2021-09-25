create table as new_sensor_data (
    with source_richards_data as (
        select `flow1`, `flow2`, `occupancy1`, `occupancy2`
        from {{ source('richards_sample_data', 'sensor_data')}}
    )
),

final as (
    select flow1, flow2, occupancy1, occupancy2 from source_richards_data
)

select * from final