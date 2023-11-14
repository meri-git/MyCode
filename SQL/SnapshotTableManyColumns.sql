CREATE TABLE SnapshotMain (
    SnapshotID INT PRIMARY KEY,
    Timestamp DATETIME
    -- Add other common columns
);

CREATE TABLE SnapshotDetails (
    SnapshotID INT PRIMARY KEY,
    ColumnName VARCHAR(50),
    ColumnValue DATATYPE,
    FOREIGN KEY (SnapshotID) REFERENCES SnapshotMain(SnapshotID)
);
