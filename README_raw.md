# iNaturalist Competition 
Please open an issue if you have questions or problems with the dataset.

# 2017 Competition
The 2017 competition is part of the [FGVC^4 workshop](fgvc.org) at [CVPR](http://cvpr2017.thecvf.com/). 

## Details

There are a total of 5,089 categories in the dataset, with 579,184 training images and 95,986 validation images. For the training set, the distribution of images per category follows the observation frequecy of that category by the iNaturalist community. Therefore, there is a non-uniform distribution of images per category. 


| Super Category |	Species Count	| Train Images |	Val Images |
|------|---------------|-------------|---------------|
Plantae|2,101|158,407|38,206|
Insecta|1,021|100,479|18,076|
Aves|964|214,295|21,226|
Reptilia|289|35,201|5,680|
Mammalia|186|29,333|3,490|
Fungi|121|5,826|1,780|
Amphibia|115|15,318|2,385|
Mollusca|93|7,536|1,841|
Animalia|77|5,228|1,362|
Arachnida|56|4,873|1,086|
Actinopterygii|53|1,982|637|
Chromista|9|398|144|
Protozoa|4|308|73|
|||||
|Total|13|579,184|95,986|


## Evalutation
We follow a similar metric to the classification tasks of the [ILSVRC](http://image-net.org/challenges/LSVRC/2016/index#scene). For each image $i$, an algorithm will produce 5 labels $l_{ij}$, $j=1,\ldots,5$. We allow 5 labels because some categories are distinguished with additional data provided by the observer, such as latitude, longitude and date. It might also be the case that multiple categories occur in an image (e.g. a photo of a bee on a flower). For this competition each image has one ground truth label $g_i$, and the error for that image is:
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

## Annotation Format
We closely follow the annotation format of the [COCO dataset](http://mscoco.org/dataset/#download). The annotations are stored in the [JSON format](http://www.json.org/) and are organized as follows:
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
  "rights_holder" : str
}

category{
  "id" : int,
  "name" : str,
  "supercategory" : str,
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

## Submission Format
Depends on if we use Kaggle or not...
```
[{
  "image_id" : int,
  "category_id" : int,
  "score" : float
}]
```


# Terms of Use

By downloading this dataset you agree to the following terms:

1. You will abide by the [iNaturalist Terms of Service](https://www.inaturalist.org/pages/terms)
2. You will use the data only for non-commercial research and educational purposes.
3. You will NOT distribute the above images.
4. The Califonia Insitute of Technology makes no representations or warranties regarding the data, including but not limited to warranties of non-infringement or fitness for a particular purpose.
5. You accept full responsibility for your use of the data and shall defend and indemnify the Califonia Insitute of Technology, including its employees, officers and agents, against any and all claims arising from your use of the data, including but not limited to your use of any copies of copyrighted images that you may create from the data.

