with source as (
    select * from {{ source('second_sensor_data', 'sensor_data2') }}
    ),
    sensor_data as (
    select
        flow1,
        occupancy1,
        flow2,
        occupancy2
        flow3,
        occupancy3
    from davis2.sensor_data2
    )
    select
    *
    from sensor_data