with source as (
    select * from {{ source('first_sensor_data', 'sensor_data1') }}
    ),

    sensor_data as (
    select
        flow1,
        occupancy1,
        flow2,
        occupancy2
        flow3,
        occupancy3
    from davis2.sensor_data
    )
    select
    *
    from sensor_data