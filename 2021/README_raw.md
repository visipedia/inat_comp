![Banner](assets/inat_2021_banner.jpg)

# iNaturalist 2021 Competition
The 2021 competition is part of the [FGVC^8 workshop](https://sites.google.com/view/fgvc8/home) at [CVPR](http://cvpr2021.thecvf.com/).

Please open an issue if you have questions or problems with the dataset.

## Updates
February 24, 2021:
  * Including dataset description and figures.

February 13, 2021:
  * Mocking up 2021 page. Preparing dataset files. 


## Dates
Competition launch and data release coming soon!

## Details
There is a total of 10,000 species in the dataset. The full training dataset contains nearly 2.7M images. To make the dataset more accessible we have also created a "mini" training dataset with 50 examples per species for a total of 500K images. Each species has 10 validation images. There are a total of 500,000 test images. 

| Super Category | Species Count | Train Images | Train Mini Images | Val Images | Test Images |
| ---- | ---- | ---- | ---- | ---- | ---- |
Plants|4,271|1,148,702|213,550|42,710|x|
Insects|2,526|663,682|126,300|25,260|x|
Birds|1,486|414,847|74,300|14,860|x|
Fungi|341|90,048|17,050|3,410|x|
Reptiles|313|86,830|15,650|3,130|x|
Mammals|246|68,917|12,300|2,460|x|
Ray-finned Fishes|183|45,166|9,150|1,830|x|
Amphibians|170|46,252|8,500|1,700|x|
Mollusks|169|44,670|8,450|1,690|x|
Arachnids|153|40,687|7,650|1,530|x|
Animalia|142|37,042|7,100|1,420|x|
||||||
Total|10,000|2,686,843|500,000|100,000|500,000|

![Train Val Distribution](assets/train_val_distribution.png)

![Location Distribution](assets/location_distribution.png)

## Evaluation
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image $i$, an algorithm will produce 3 labels $l_{ij}$, $j=1,\ldots,3$. We allow 3 labels because some categories are disambiguated with additional data provided by the observer, such as latitude, longitude and date. For a small percentage of images, it might also be the case that multiple categories occur in an image (e.g. a photo of a bee on a flower). For this competition each image has one ground truth label $g_i$, and the error for that image is:
$$
e_i = \min_{j}d(l_{ij}, g_i)
$$
Where
$$
d(x, y) =
\begin{cases}
    0       & \quad \text{if } x = y \\
    1  & \quad \text{otherwise}\\
\end{cases}
$$

The overall error score for an algorithm is the average error over all $N$ test images:
$$
\text{score} = \frac{1}{N} \sum_{i} e_{i}
$$

## Differences from Previous Competitions
We made a few modifications to the competition this year. Similar to the [2017](../2017) competition, we are releasing the species names immediately, instead of obfuscating them. Our reason for obsfucating them in [2018](../2018) and [2019](../2019) was to make it difficult for competitors to scrape the web (or iNaturalist itself) for additional images. Because we are releasing 2.7M training images and the dataset doesn't necessarily focus on the long tail problem we feel that we can release the species names without worry. This does not mean that scraping is allowed. Please do not scrape for additional data, especially from iNaturalist. Having the species names also makes interpretting validation results easier when examining confusion matrices and accuracy statistics. 

We are also releasing location information for each image in the form of `latitude`, `longitude`, and `location_uncertainty` values. We have retroactively added this information to the [2017](../2017) and [2018](../2018) datasets, but this year competitors are able to utilize this information when building models. We hope this motivates competitors to devise interesting solutions to this large scale problem. 

## Guidelines
Participants are welcome to use previous iNaturalist competition datasets ([2017](../2017/), [2018](../2018), [2019](../2019)) as an additional data source. However we do not provide a category or image mappings between the datasets and there is certainly overlap between the species and images included in the various datasets. Besides using previous iNaturalist competition datasets, participants are forbidden from collecting additional natural world data for the 2021 competition. Weights from models trained on ImageNet, COCO, and previous iNaturalist competition datasets may be used to initialize models. Models pretrained on other datasets are not allowed. Please specify any and all external data used for training when uploading results.

The general rule is that participants should only use the provided training and validation images (with the exception of the allowed pretrained models) to train a model to classify the test images. We do not want participants crawling the web in search of additional data for the target categories. Participants should be in the mindset that this is the only data available for these categories.

Participants are allowed to collect additional annotations (e.g. bounding boxes, keypoints) on the provided training and validation sets, however they should not annotate the test images. Teams should specify that they collected additional annotations when submitting results.

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

### Annotation Format Notes:
  * It is possible for the `latitude`, `longitude`, and `location_uncertainty` fields to be `nan` when the values were missing from the respective iNaturalist observation. 
  * The `test.json` file does not have the `annotations` field. You can only evaluate on the test set by uploading your submission to the Kaggle competition. 

## Submission Format

The submission format for the Kaggle competition is a csv file with the following format:
```
Id,Predicted
12345,0 78 23
67890,83 13 42
```
The `Id` column corresponds to the test image id. The `Predicted` column corresponds to 3 category ids, separated by spaces. You should have one row for each test image. Please sort your predictions from most confident to least, from left to right, this will allow us to study top-1, top-2, and top-3 accuracy.

## Terms of Use
By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms).
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the dataset images.
4. Cornell University makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify Cornell University, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

## Data
Links coming soon!

## Previous Competitions
* [2019 Competition](../2019)
* [2018 Competition](../2018)
* [2017 Competition](../2017)
