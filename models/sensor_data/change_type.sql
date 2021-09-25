with sensor_data_change as {
    ALTER TABLE `davis2`.`sensor_data2` 
    CHANGE COLUMN `occupancy1` `occupancy1` INT NULL DEFAULT NULL ,
    CHANGE COLUMN `flow2` `flow2` INT NULL DEFAULT NULL ,
    CHANGE COLUMN `occupancy2` `occupancy2` INT NULL DEFAULT NULL ,
    CHANGE COLUMN `flow3` `flow3` INT NULL DEFAULT NULL ,
    CHANGE COLUMN `occupancy3` `occupancy3` INT NULL DEFAULT NULL ,
    CHANGE COLUMN `occupancy4` `occupancy4` INT NULL DEFAULT NULL ,
    CHANGE COLUMN `occupancy5` `occupancy5` INT NULL DEFAULT NULL ;
}
