![Banner](assets/inat_2021_banner.jpg)

# iNaturalist 2021 Competition
The 2021 competition is part of the [FGVC^8 workshop](https://sites.google.com/view/fgvc8/home) at [CVPR](http://cvpr2021.thecvf.com/).

Please open an issue if you have questions or problems with the dataset.

## Updates
February 13, 2021:
  * Mocking up 2021 page. Preparing dataset files. 


## Dates


## Details



## Evaluation


## Differences from Previous Competitions


## Guidelines


## Annotation Format
We follow the annotation format of the [COCO dataset](http://mscoco.org/dataset/#download) and add additional fields. The annotations are stored in the [JSON format](http://www.json.org/) and are organized as follows:
```
{
  "info" : info,
  "images" : [image],
  "categories" : [category],
  "annotations" : [annotation],
  "licenses" : [license]
}

info{
  "year" : int,
  "version" : str,
  "description" : str,
  "contributor" : str,
  "url" : str,
  "date_created" : datetime,
}

image{
  "id" : int,
  "width" : int,
  "height" : int,
  "file_name" : str,
  "license" : int,
  "rights_holder" : str,
  "date": str,
  "latitude": float,
  "longitude": float,
  "location_uncertainty": int,
}

category{
  "id" : int,
  "name" : str,
  "common_name" : str,
  "supercategory" : str,
  "kingdom" : str,
  "phylum" : str,
  "class" : str,
  "order" : str,
  "family" : str,
  "genus" : str,
  "specific_epithet" : str,
  "image_dir_name" : str,
}

annotation{
  "id" : int,
  "image_id" : int,
  "category_id" : int
}

license{
  "id" : int,
  "name" : str,
  "url" : str
}
```

Note that the test json file does not have the `annotations` field. 

## Submission Format


## Terms of Use


## Data


## Previous Competitions
* [2019 Competition](../2019)
* [2018 Competition](../2018)
* [2017 Competition](../2017)
