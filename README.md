# Coordinate Conversion Utility

This tool provides a simple and efficient way to convert coordinates between
different geographic reference systems.

## Introduction

Geospatial data often comes in various coordinate systems, and it is crucial
for analysts and developers working with location data to convert between these
systems accurately. This Coordinate Conversion Utility is designed to handle
transformations between popular systems such as WGS84, OSGB36, and others,
ensuring that your geospatial data aligns correctly on maps and other
geographic applications.

## Features

- Convert between WGS84, OSGB36, and other common coordinate systems
- Batch conversion capabilities for handling multiple coordinates at once

## Prerequisites

Will need a csv file with the following table format: 

| Name | East    | North   |
|------|---------|---------|
| name of the project | X coordinate | Y coordinate |



## Installation

To install the Coordinate Conversion Utility, follow these steps:

```bash
git clone https://github.com/ardms/coordinate-transformation
cd coordinate-conversion-utility
pip install -r requirements.txt 
```
