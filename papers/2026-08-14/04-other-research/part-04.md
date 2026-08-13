# 📦 其他研究 | 2026年08月14日

> 本类共 **202** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-202](./part-05.md)

---

### 151. [Slips: Behavioral Evidence Aggregation for Network Security](https://arxiv.org/abs/2608.11979)

**<font color=#1a73e8>作者：</font>** Sebastian Garcia, Veronica Valeros, Alya Gomaa 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Network intrusion detection systems often analyze individual packets or flows, although malicious behavior may develop across many connections and over time. This may limit their ability to combine isolated detections into a coherent assessment of host behavior. Packet-level features may also be too low-level for complex AI-based detection, requiring additional processing to improve accuracy while maintaining a low false-positive rate.
We present Slips, a network intrusion detection system that builds host-centered behavioral profiles and organizes activity into time windows. It uses a modular architecture in which independent modules report evidence rather than generating final alerts directly. Slips then accumulates this evidence into host-level decisions. We evaluate Slips against Suricata on an expert-labeled PCAP dataset. At the profile-time-window level, Slips achieved 83% higher recall and a 70% higher F1 score than Suricata, while neither system produced false positives. These results indicate that time-window-based evidence accumulation can produce context-aware decisions that better align with expert judgment.

---


### 152. [Auditing Frame-Level AUC in Weakly Supervised Video Anomaly Detection: Granularity, Resolution, and Scene Bias](https://arxiv.org/abs/2608.11985)

**<font color=#1a73e8>作者：</font>** Sara Abdulaziz, Egor Bondarev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Frame-level area under the ROC curve (AUC) is the dominant evaluation metric for weakly supervised video anomaly detection (WSVAD). Its standard form measures whether an anomalous frame outranks a normal frame drawn from anywhere in the test set. We refer to this comparison as pooled AUC, since it aggregates frame pairs across test videos regardless of source. Pooled AUC therefore credits both event localization and differences between video sources. We audit this protocol on UCF-Crime across recent state-of-the-art models spanning different backbone families. Holding each model's frame scores fixed, we read them under three pairing granularities: global, per anomaly category, and within each video, then repeat the same three-granularity readout on zero-shot scores computed from the models' internal representations. We assess ranking reliability with a paired video bootstrap. Three findings follow. First, pooled AUC does not reliably predict within-video anomaly localization: models with similar pooled scores exhibit large localization differences and rank reversals under stricter granularities. Second, at the benchmark's test-split size, pooled AUC lacks the resolution to support state-of-the-art margins reported in the field. Within each backbone family, it resolves no comparison at those margins, while within-video AUC resolves several over identical predictions. Learned representations further reveal that within-video anomaly structure and detector localization are decoupled. Third, on normal footage alone, every model we examine separates videos by recording properties, such as resolution and color encoding, indicating that scene sensitivity is shared across the setting rather than specific to any architecture. We publicly release a granularity-aware protocol computable from existing predictions and scene-factor annotations for UCF-Crime.

---


### 153. [A Remote Approach to Cashew Orchard Detection: Leveraging Active Learning with Satellite Imagery in Guinea-Bissau](https://arxiv.org/abs/2608.11996)

**<font color=#1a73e8>作者：</font>** Miguel, Sofia, Maria 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cashew production is a widespread economic activity in Guinea-Bissau, as well as other countries in West Africa. However, unregulated cashew production can be directly associated with increasing regionwide deforestation rates, biodiversity losses, and a fragile economic structure. There is no nationwide database for listing or georeferencing cashew orchards, so there is a clear need to remotely map their locations. In recent years, multiple methods for detecting orchards have been developed, though they have only been applied on a regional level. This work expands regional analyses to a nationwide scale. It develops a scalable and cost-effective remote approach, based on Sentinel-2 satellite imagery, using Machine Learning techniques to detect cashew orchards automatically. Margin-based Active Learning techniques were employed to develop an optimal training set in terms of the number of points and their informativeness, leading to a cashew map with 94.0% balanced accuracy obtained entirely off-site. We created two datasets and a 2021 cashew map with 10m spatial resolution that are openly accessible through GitHub. The results demonstrate the possibility of a broader cashew orchard mapping, creating a new stepping stone for this environmental application.

---


### 154. [Remote Sensing and Machine Learning-Based Analysis of Land Use and Vegetation Change in Dhaka District, Bangladesh](https://arxiv.org/abs/2608.12001)

**<font color=#1a73e8>作者：</font>** Muhammad Masud Tarek, Md. Alamgir Hossain, Md. Samiul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Rapid urbanization in Dhaka District, Bangladesh has triggered substantial alterations in land use and environmental conditions, necessitating systematic monitoring for informed urban planning and ecological sustainability. This study employs remote sensing data and machine learning techniques to analyze spatiotemporal changes in land cover and vegetation dynamics between 2019 and 2024. High-resolution satellite imagery from Sentinel-2 MSI and Landsat 8 was utilized to classify land cover types and compute spectral indices including the Normalized Difference Vegetation Index (NDVI), Normalized Difference Built-up Index (NDBI), and Normalized Difference Water Index (NDWI). A supervised machine learning approach incorporating Decision Tree, K-Nearest Neighbors (KNN), and Random Forest classifiers was applied using labeled geospatial training points within Google Earth Engine. Accuracy assessments were conducted using confusion matrices and kappa statistics. Results indicate a 59.5% increase in urban built-up areas and a significant decline in vegetation (-8.46%) and water bodies (-7.77%) over the five-year period. Land conversion from vegetated and aquatic areas to urban infrastructure was identified as a dominant trend. Among the models, Random Forest demonstrated the highest classification accuracy. These findings underscore the growing environmental pressures driven by unregulated urban expansion in Dhaka. The study highlights the potential of remote sensing and machine learning tools in providing timely, actionable data to support sustainable urban development, land-use regulation, and ecosystem conservation policies.

---


### 155. [CTBench: Evaluating Troubleshooting Capabilities of AI Agents in Realistic Telecom Network Operations](https://arxiv.org/abs/2608.12002)

**<font color=#1a73e8>作者：</font>** Xingyu Yan, Tingting Dai, Antonio De Domenico 等 19 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents are increasingly considered for automating network operations and maintenance, where engineers must diagnose network faults, optimize configurations to enhance services, and reduce operational costs while acting under strict constraints. However, existing evaluations fail to accurately model real network characteristics or assess agents under partially observable telecom environments with diverse vendors, devices, protocols, and interfaces. In this paper, we introduce CTBench, a public benchmark for assessing whether an agent behaves like a competent telecom troubleshooting engineer. CTBench focuses on root cause analysis and path restoration. Each task is constructed by experts and annotated with rich task metadata, including golden evidence steps. CTBench uses expert-grounded metrics that evaluate both final answers and the diagnostic evidence. Experiments with representative harness-model combinations show that state-of-the-art agents perform very well at identifying endpoints in path-restoration tasks but, more generally, underperform in root cause analysis. In particular, agents struggle with interface state, link-layer, service-management, and other operational faults. Most importantly, even when agents produce plausible or correct final answers, they often fail to provide the evidence-grounded diagnoses required in operational practice. Our results further show that path restoration is generally more resource expensive, yet larger resource usage does not necessarily translate into better diagnosis.

---


### 156. [Dual-Model Sentiment Analysis of Consumer Reviews in the Retail Coffee Sector Using Machine Learning and Deep Learning Approaches](https://arxiv.org/abs/2608.12007)

**<font color=#1a73e8>作者：</font>** Muntasir Hasan Kanchan, Md. Alamgir Hossain, Md. Samiul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Consumer reviews play an important role in shaping brand perception and business strategies, particularly in service-driven industries such as retail coffee. This study presents a comparative sentiment analysis framework for Starbucks customer reviews using classical machine learning and deep learning approaches. The dataset, collected from ConsumerAffairs, contains more than 700 reviews and was analyzed through preprocessing and exploratory data analysis to identify temporal and geographic patterns. Sentiment labels were generated by binarizing star ratings, with ratings of 4 and 5 classified as positive and ratings of 1 to 3 as negative. The resulting dataset was substantially imbalanced toward negative sentiment. Five machine learning classifiers, including Logistic Regression, Support Vector Machine (SVM), Decision Tree, Random Forest, and Naive Bayes, were evaluated alongside five deep learning models: LSTM, RNN, Bidirectional LSTM, GRU, and CNN. Model performance was assessed using accuracy, precision, recall, and F1-score. SVM achieved the highest accuracy among the machine learning models at 91.0 percent, while Bidirectional LSTM showed the strongest performance among the deep learning models and demonstrated good generalization on unseen data. The findings also show that class imbalance negatively affected positive sentiment recall across several models. Overall, this study provides a comparative evaluation of machine learning and deep learning approaches for real-world consumer sentiment analysis and highlights the importance of appropriate model selection and preprocessing for customer experience analytics in the retail coffee sector.

---


### 157. [Reducing Symmetry Increase in Equivariant Neural Networks](https://arxiv.org/abs/2608.12010)

**<font color=#1a73e8>作者：</font>** Ning Lin, Jiacheng Cen, Anyi Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Equivariant Neural Networks (ENNs) have empowered numerous applications in scientific fields. Despite their remarkable capacity for representing geometric structures, ENNs suffer from degraded expressivity when processing symmetric inputs: the output representations are invariant to transformations that extend beyond the input's symmetries. The mathematical essence of this phenomenon is that a symmetric input, after being processed by an equivariant map, experiences an increase in symmetry. While prior research has documented symmetry increase in specific cases, a rigorous understanding of its underlying causes and general reduction strategies remains lacking. In this paper, we provide a detailed and in-depth characterization of symmetry increase together with a principled framework for its reduction: (i) For any given feature space and input symmetry group, we prove that the increased symmetry admits an infimum determined by the structure of the feature space; (ii) Building on this foundation, we develop a computable algorithm to derive this infimum, and propose practical guidelines for feature design to prevent harmful symmetry increases. (iii) Under standard regularity assumptions, we demonstrate that for most equivariant maps, our guidelines effectively reduce symmetry increase. To complement our theoretical findings, we provide visualizations and experiments on both synthetic datasets and the real-world QM9 dataset. The results validate our theoretical predictions.

---


### 158. [Uncertainty-Aware Probabilistic Constrained Clustering from Entangled Pairwise Supervision](https://arxiv.org/abs/2608.12027)

**<font color=#1a73e8>作者：</font>** Shaojie Zhang, Ke Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pairwise constrained clustering typically relies on hard must-link/cannot-link labels, whereas realistic pairwise supervision may be real-valued and entangle intrinsic ambiguity, expert judgment, and stochastic corruption. Existing deep constrained clustering (DCC) methods mainly target hard, expert-agnostic constraints, treating soft labels mostly numerically rather than semantically. We formalize this setting as uncertainty-aware probabilistic constrained clustering (UPCC), defining a canonical aleatoric target through a heterogeneous observation process and analyzing its conditional identifiability. We introduce ProbPair, an angular pairwise objective for probabilistic relations, and build ECI-PP, an estimator--corrector--integrator framework that refines imperfect supervision via belief estimation, correction, and reliability-aware integration. Across challenging probabilistic supervision settings, experiments on diverse benchmarks show that ECI-PP outperforms state-of-the-art DCC methods and remains robust with a shared default configuration.

---


### 159. [LoSA: Near-Lossless Sparse Attention for Training-Free Video Diffusion Acceleration](https://arxiv.org/abs/2608.12032)

**<font color=#1a73e8>作者：</font>** Enhuai Liu, Yunke Wang, Yutong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video diffusion transformers are costly to sample: every denoising step applies self-attention over a long 3D token sequence, a quadratic cost that dominates as resolution and duration grow. Sparse attention reduces this cost without retraining, but existing methods pursue aggressive sparsity, where further speedup costs disproportionately more attention fidelity. We target the opposite end of this trade-off: fix near-lossless fidelity by construction, and remove as much computation as this constraint permits. Two observations make this regime practical: roughly 40% of block interactions can be removed while retaining 99% of the attention mass, and the high-mass support remains stable across denoising steps. We propose LoSA, a training-free sparse-attention method that fixes a retained-mass threshold of 99% rather than a sparsity ratio: it measures exact block attention masses at one early dense step, keeps, for each head and query block, the smallest key/value block set meeting the threshold, and reuses the frozen block indices for all remaining steps. On Wan2.1-1.3B, LoSA alone gives a $1.36\times$ speedup with a 0.06-point VBench Overall drop. The benefit is largest under composition: combined with feature caching, LoSA reaches a $3.2\times$ speedup on HunyuanVideo at a 0.02-point drop, versus 0.32 points for the strongest sparse baseline at comparable speed. Across three video diffusion transformers and speedups up to $3.2\times$, LoSA consistently achieves the best training-free speed-quality trade-off.

---


### 160. [How Far from Clinical Deployment? Evaluating the Complete Unsupervised Domain Adaptation Pipeline in Medical Imaging](https://arxiv.org/abs/2608.12035)

**<font color=#1a73e8>作者：</font>** Yiheng Xiong, Luisa Gallée, Daniel Santak Wolf 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deploying unsupervised domain adaptation (UDA) in clinical practice requires choosing which algorithm to use and which of its trained models to ship. However, the deployment (target) domain is unlabeled, so models cannot be evaluated directly on it, leaving it unclear which to select. We address this by evaluating the complete UDA pipeline, considering both adaptation and label-free selection together. Our study covers eleven clinically relevant cross-domain scenarios from nine medical imaging datasets, with ten UDA algorithms and 13 label-free selection methods (validators), evaluating over 80,000 trained models in total. By this, we find that a capable adapted model usually exists, but identifying it without target labels is difficult: the validator-selected models leave a large and structural target performance gap to the best available one, with no evaluated validator consistently reliable. Towards closing it, we explore two strategies, ensembling and a small target-labeling budget; both narrow this gap but do not close it entirely. Overall, deployable UDA depends on the complete pipeline; addressing the less explored selection step could bring much of current UDA closer to clinical use.

---


### 161. [Clustered Randomized Smoothing for Stochastic Prediction Functions](https://arxiv.org/abs/2608.12037)

**<font color=#1a73e8>作者：</font>** Eduardo Figueiredo, Frederik Mathiesen, Julian Schumann 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern stochastic predictors can model rich, multi-modal outcome distributions. However, this expressive power comes with challenges in ensuring robust predictions $-$ a critical requirement in safety-critical domains. Randomized smoothing is a leading technique for improving robustness, particularly against adversarial perturbations. Yet, in stochastic multi-modal regression settings, randomized smoothing often fails due to mode collapse, yielding averaged predictions that do not reflect the underlying distribution. To address this limitation, we propose clustered $\alpha$-smoothing, a framework that (1) partitions noisy samples using an arbitrary clustering algorithm, (2) applies $\alpha$-smoothing locally within each cluster, and (3) combines the resulting predictions into a mixture distribution. By interpreting the smoothing distribution as a mixture of $\alpha$-smoothers, we derive a lower bound on the probability that the smoothed prediction lies within a union of compact regions corresponding to distinct modes. We empirically evaluate our framework on two benchmarks, demonstrating substantial improvements over state-of-the-art methods. In stochastic trajectory prediction on a driving simulator dataset, our approach achieves, on average, a $27\%$ lower Wasserstein distance to the ground-truth distribution compared to $\alpha$-smoothing. In quadrotor control, where modes correspond to distinct feasible paths to a target, our method reduces the collision rate by $81\%$ relative to the state-of-the-art randomized smoothing.

---


### 162. [Localizing to Debias: A Patch-Level Benchmark and Baseline for Weakly Supervised Spatial Anomaly Detection](https://arxiv.org/abs/2608.12045)

**<font color=#1a73e8>作者：</font>** Sara Abdulaziz, Abdulrahman Al-Abri, Giacomo D'Amicantonio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite growing interest in weakly supervised video anomaly detection (WSVAD), current methods struggle to bridge the gap between coarse temporal supervision and fine-grained spatial reasoning. A key obstacle is the tendency of temporal detectors to latch onto background and scene-level cues rather than truly discriminative anomaly evidence. This background bias raises ethical concerns: models may inadvertently associate anomalies with societal or environmental context rather than authentic crime-related cues. Without spatial grounding, such biases remain hidden and unauditable. To address this, we propose SST-WSVADL, a sparse spatio-temporal framework that bridges temporal anomaly detection with fine-grained spatial localization. Rather than processing all spatial regions indiscriminately, SST-WSVADL progressively focuses on the most anomaly-relevant spatio-temporal regions through dynamic sparsification, naturally suppressing background dominant content while preserving discriminative evidence. The temporal and spatial branches are coupled end-to-end via motion-aware regularization that guides sparsification toward dynamically informative regions, without relying on external detectors or vision-language prompts. We publicly release frame-level spatial annotations and a method-agnostic evaluation protocol for three public datasets: UCF-Crime, XD-Violence, and MSAD. These resources enable the community to audit spatial biases in WSVAD predictions, supporting progress toward more ethical and accountable anomaly detection. Experiments demonstrate that SST-WSVADL is competitive with prior methods across benchmarks while enabling localization and patch-level auditability of scene bias, providing a reproducible foundation for interpretability-oriented evaluation of WSVAD models.

---


### 163. [Predicting Functions, Not Features: KANs with Function-Space Joint-Embedding Predictive Learning for Medical Image Segmentation](https://arxiv.org/abs/2608.12050)

**<font color=#1a73e8>作者：</font>** Yungeng Liu, Xuanzi Fang, Yuge Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Kolmogorov--Arnold Networks (KANs) introduce explicit functional representations by parameterizing each network edge as a learnable univariate function. However, existing KAN-based segmentation models optimize edge functions only through objectives defined after edge aggregation, leaving individual functions without an explicit pre-aggregation learning target. To address this limitation, we propose Function-Space Joint-Embedding Predictive Learning (FS-JEPA) for medical image segmentation. Our FS-JEPA framework moves predictive learning into the pre-aggregation function space of KANs. A masked online branch predicts structured signatures of sampled KAN edge functions generated by a full-context exponential moving average target branch, while shared edge indices preserve correspondence between predictions and targets. Rather than predicting an isolated edge response, we represent each sampled edge function using a multi-radius signature composed of function evaluations around its input anchor. This structured representation captures local functional variations that cannot be characterized by a single response and provides a more informative predictive target. The function-space objective is jointly optimized with the segmentation loss during training, while the predictive branch is removed at inference. Experiments on five medical image segmentation benchmarks show that our FS-JEPA achieves the best average Dice and outperforms the strongest competing KAN-based method by +2.25 percentage points.

---


### 164. [Towards Truly Unsupervised Evaluation of Feature Selection](https://arxiv.org/abs/2608.12057)

**<font color=#1a73e8>作者：</font>** Hafiz Saud Arshad, Muhammad Rajabinasab, Arthur Zimek  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Feature selection is one of the most important and fundamental tasks in data mining, tackled by a family of methods with an established set of evaluation techniques to measure the quality of a specific method. Most of the methods commonly used for the unsupervised evaluation of feature selection algorithms suffer from critical design flaws which question their unsupervised nature. In this paper, we provide a critical discussion on the established allegedly unsupervised evaluation techniques, and shed light on the reasons why they are not truly unsupervised but, at best, supervised evaluation under an unsupervised downstream task. We also propose a novel, truly unsupervised evaluation framework to measure the quality of the feature selection algorithms without any form of information about the labels. The proposed framework utilizes unsupervised Principal Component Analysis, and optimal transport to measure the quality of the feature selection methods in a truly unsupervised manner.

---


### 165. [Preference Tree Optimization: Enhancing Goal-Oriented Dialogue with Look-Ahead Simulations](https://arxiv.org/abs/2608.12062)

**<font color=#1a73e8>作者：</font>** Lior Baruch, Moshe Butman, Kfir Bar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Developing dialogue systems capable of engaging in multi-turn, goal-oriented conversations remains a significant challenge, especially in specialized domains with limited data. This research proposes a novel framework called Preference Tree Optimization (PTO), designed to iteratively improve agent models in such dialogue systems, by generating preference data using a method called Preference Tree with Look-Ahead. Focusing on Motivational Interviewing (MI) -- a counseling technique aimed at facilitating behavioral change -- we leverage virtual patients and an oracle evaluator to simulate conversations and generate rich preference datasets. By combining this method with Direct Preference Optimization (DPO), we aim to enhance the agent's decision-making capabilities over iterative training cycles. The proposed framework addresses data scarcity and advances the development of more nuanced and effective dialogue systems in goal-oriented domains. Experimental evaluations demonstrate that the PTO framework enhances dialogue agents' performance in goal-oriented conversations within the domain of Motivational Interviewing (MI). Models trained with PTO consistently outperformed the baseline in key metrics such as session satisfaction and working alliance. Additionally, incorporating look-ahead simulations led to improved long-term planning and more effective conversational strategies, with deeper look-ahead configurations yielding the most stable and high-scoring results.

---


### 166. [Draw This First](https://arxiv.org/abs/2608.12064)

**<font color=#1a73e8>作者：</font>** Dazhi Zhong, Rowan Bradbury, Grant Davis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We invert the typical formulation of sketch generation: instead of drawing strokes in order, we predict a 2D field that defines the order in which strokes are drawn. We use a pretrained latent flow-matching transformer to supply the image prior to predict an intermediate representation, while training the VAE's decoder to predict the order field, stroke mask, and stroke segmentation. We vectorize the predicted segmentation into polylines and sort them by the field, producing an ordered vector sketch. Our model can predict an ordered vector sketch from a text description or derender an image into ordered vectors; for either, it follows text instructions specifying the order of drawing.

---


### 167. [A Comparison of Malware Image Transformations Using Grad-CAM and Hybrid Learning Models](https://arxiv.org/abs/2608.12077)

**<font color=#1a73e8>作者：</font>** Vibha Bhavikatti, Mark Stamp  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that binary-to-image representations can enable effective machine learning-based results for malware detection and classification. However, performance can vary significantly, depending on the technique used to convert binaries to images. Furthermore, the explainability and interpretability of image-based models is largely unexplored within the malware domain. In this research, we employ Gradient-weighted Class Activation Maps (Grad-CAM) as an eXplainable AI (XAI) tool, which we use to analyze eight distinct image types derived from malware samples. We provide quantitative faithfulness and stability metrics for Grad-CAM heatmaps and we compare these heatmaps to High-Resolution Class Activation Mappings (HiResCAM). We also show that Grad-CAM heatmaps can provide useful information for malware classification. Specifically, we show that a Random Forest model trained on features extracted from Grad-CAM images via a MobileNetV2 Convolutional Neural Network (CNN) model achieves a test accuracy of 0.777 across 17 malware families, exceeding a previous benchmark of 0.750 for this same dataset. A key finding of this research is that for the malware image transformations considered, accuracy and explanation faithfulness do not coincide, e.g., image transformation techniques that produce the most faithful explanations yield only mid-tier accuracy.

---


### 168. [Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric World Models](https://arxiv.org/abs/2608.12078)

**<font color=#1a73e8>作者：</font>** Shukrullo Nazirjonov, Sai Prasanna, Anna Manasyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning world models from offline trajectories enables agents to accomplish different tasks through planning. Object-centric (OC) representations, which decompose a scene into a set of slots that bind to its objects, have been proposed as an inductive bias for world models that are more sample-efficient and generalize better. Yet prior object-centric world models (OCWMs) take the slot encoder as given and evaluate only in-distribution, leaving open whether the object-centric bias actually delivers for planning and what within the OCWM drives it. We conduct a controlled study of OCWMs for visual model-predictive control along two axes: object-centric representation quality and generalization under distribution shift relative to scene-centric models. We find that (i) planning success correlates positively with unsupervised slot-quality metrics (FG-ARI, mBO), though the gains saturate at high slot quality; (ii) with well-bound slots, the auxiliary proprioception inputs and masking inductive bias that prior methods relied on become unnecessary; and (iii) under unseen distribution shifts, the OCWM with well-bound slots is more robust overall than the end-to-end trained scene-centric LeWM, while DINO-WM, built on similar frozen pretrained features, remains competitive -- pointing to pretrained features as a key contributor to robustness.

---


### 169. [Faithful, Sufficient and Understandable: Rethinking Graph Counterfactual Explanations via Discrete Diffusion Inversion](https://arxiv.org/abs/2608.12083)

**<font color=#1a73e8>作者：</font>** David Bechtoldt, Sidney Bender  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) achieve strong predictive performance on graph-structured data across domains such as chemistry, biology, and network analysis, yet they provide no intrinsic explanation of their predictions. This limits their adoption in high-stakes and safety-critical settings. Counterfactual explanations address this by revealing the minimal structural modifications that would change a model's prediction. On graphs, however, such a modification is hard to produce. The search space is discrete and combinatorial, and a valid answer must respect categorical node and edge types together with domain rules such as chemical valency in the case of molecular graphs. Existing explainers give up one of two things. Either edits are not held on the data manifold, or the search does not span the full edit space. We propose Graph Diffusion Counterfactual Explanation via Inversion (GDCE-I), which gives up neither. A discrete denoising diffusion model with a novel discrete inversion scheme enables distribution-aware edits leveraging the whole domain edit space. We further address the incomplete and inconsistent evaluation of graph counterfactuals by deriving a framework of explanation desiderata and applying it to every method under one shared protocol. Across four benchmarks, GDCE-I outperforms related work by a large margin on the defined framework. For the molecular domain, we further qualitatively show that GDCE-I attains interpretable in-distribution solutions.

---


### 170. [NAE: Normalizing AutoEncoder](https://arxiv.org/abs/2608.12084)

**<font color=#1a73e8>作者：</font>** Muhammad Abdur Rafae, Niels Landwehr  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider the setting of Normalizing flows with approximate inverses, an established paradigm spanning both full-dimensional ($d=D$) and bottleneck ($d<D$) settings, and group these models under the term flow autoencoders. We present a theoretical investigation into their training dynamics and prove that the proposed loss used by existing approaches is suboptimal; specifically, both encoder and decoder surrogates must be optimized in alignment with reconstruction loss. Guided by these insights, we propose Normalizing Autoencoder (NAE), which employs a novel conditional loss that aligns the surrogate loss gradient with that of reconstruction loss, directly improving upon the current standard. Extensive experiments across molecule generation, tabular data, and image benchmarks demonstrate that NAE achieves state of the art performance. Our work highlights the importance of loss alignment in flow autoencoders and establishes NAE as a powerful generative framework.

---


### 171. [RA-ClipScore: Making Generative Model Evaluation More Interpretable](https://arxiv.org/abs/2608.12088)

**<font color=#1a73e8>作者：</font>** Yifan Lu, Taras Kucherenko, Hedvig Kjellström 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models can produce images nearly indistinguishable from real data, yet rigorous and interpretable evaluation remains challenging. Conventional metrics such as FID provide only scalar scores with limited diagnostic insight. Widely adopted CLIP-based metrics enable semantic evaluation beyond simple training class labels, but inherit limitations from CLIP's training paradigm that restrict attribute-wise analysis. We propose RA-CLIPScore, a novel metric that mitigates these issues and extends CLIP-based evaluation to spatial distribution alignment, measuring whether generated objects adhere to the positional priors found in the training data. RA-CLIPScore introduces dual prompts to decouple competing attributes and leverages local patch tokens to capture fine-grained regional semantics. We evaluate image generative models on their ability to match both attribute and spatial distributions of the training data. Extensive experiments show that RA-CLIPScore provides more robust and interpretable evaluations than prior methods, particularly under distribution misalignment or partially irrelevant textual attributes. We further demonstrate how it reveals spatial biases in generative models. User evaluations confirm that Regional Single Attribute Divergence based on our RA-CLIPScore aligns more closely with human perception of visual diversity than existing semantic metrics.

---


### 172. [Confidence Calibration of Deep Learning Systems](https://arxiv.org/abs/2608.12100)

**<font color=#1a73e8>作者：</font>** Coby Penso  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In high-stakes applications, reliable confidence estimates are as important as the predictions themselves. Confidence calibration ensures that predicted probabilities reflect the likelihood of correctness, making it essential for safe deployment of deep learning models. However, existing methods typically assume access to clean validation data, which is often unrealistic due to label noise and domain shifts. This thesis develops methods for improving calibration under these conditions.
First, we address calibration under label noise. Standard methods can produce misleading confidence estimates when labels are unreliable. We propose a framework that uses an estimated noise model to reconstruct noise-free confidence estimates by modeling the relationship between noisy and clean label distributions. We extend this approach to Conformal Prediction (CP), which provides set-valued predictions with guaranteed coverage. Our noise-aware CP method estimates clean conformity scores despite label noise, enabling reliable uncertainty quantification. Next, we study calibration in unsupervised domain adaptation, where a model trained on a labeled source domain is adapted to an unlabeled target domain. Since labeled target data are unavailable, we estimate target-domain accuracy from source performance and domain discrepancies, enabling calibration without target labels. We also consider privacy-preserving settings in which user labels and model outputs must remain protected. We propose a locally differentially private conformal prediction framework that provides valid uncertainty quantification while maintaining privacy guarantees and balancing privacy, computational feasibility, and prediction reliability.
Our results bridge calibration theory and practical deployment in safety-critical applications, contributing to reliable, privacy-preserving, and noise-resilient neural network predictions.

---


### 173. [Avatar-Forever: Decoupled Parallel Training for High-Quality Real-Time Infinite Avatars](https://arxiv.org/abs/2608.12107)

**<font color=#1a73e8>作者：</font>** Ruibin Li, Tao Yang, Zhiyuan Ma 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing streaming video systems often rely on sequential, distillation-centered training pipelines to enable few-step long-video generation. However, this paradigm suffers from two limitations. First, failures or distribution shifts introduced in earlier stages affect later optimization, complicating the training process to converge. Second, the distillation-centric objective favours short-term generation but is prone to quality degradation when autoregressive errors accumulate over long rollouts. We propose Avatar-Forever, a decoupled parallel training framework for high-quality real-time infinite interactive avatars. Instead of coupling generation efficiency and long-horizon robustness under a sequential distillation pipeline, we treat them as two independent capabilities that can be trained in parallel. One branch performs full-parameter distillation to train an efficient generator with high visual quality, while another trains a lightweight long-horizon adapter via Recovery-oriented Rollout Training (RRT), which improves generation robustness under long-horizon inference conditions. Our decoupled parallel training design simplifies the overall training process and avoids unnecessary objective conflicts between few-step generation and long-horizon adaptation. We further introduce ForeverCache, a chunk-wise feature caching mechanism to substantially reduce redundant history computation during streaming inference. Built upon a 22B video foundation model, Avatar-Forever supports unbounded audio-driven avatar generation while maintaining identity consistency, motion coherence, and visual fidelity, enabling an end-to-end throughput of high-resolution 768x512 videos at 27.2 FPS on a single H100 GPU and providing a practical path toward stable digital humans.

---


### 174. [Beyond Parameter Space: NTK-Guided Personalized Aggregation for Robust Federated Learning](https://arxiv.org/abs/2608.12108)

**<font color=#1a73e8>作者：</font>** Mirko Konstantin, Stefan Zachow, Anirban Mukhopadhyay  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative model training across distributed clients while keeping data local. A central challenge is determining which client updates are beneficial for aggregation with respect to each client's target domain. Existing methods typically address this problem in parameter space by comparing model parameters or gradients. However, parameter-space similarity can be a poor proxy for predictive behavior, especially under heterogeneous, non-IID data. Consequently, updates that are misaligned with a client's target domain, including those caused by heterogeneous data or malfunctioning clients, may degrade local model performance.
We propose Local Inference Guided Aggregation for Heterogeneous Training Environments to Yield Enhancement Through Agreement and Regularization (LIGHTYEAR), a federated learning framework that performs update selection in function space. LIGHTYEAR uses an NTK-based agreement score to characterize predictive behavior and determine a personalized aggregation set for each client. By relating model parameters to local predictive responses, the Neural Tangent Kernel (NTK) provides a more expressive criterion for update selection than parameter-space similarity alone.
Because function-space information is not available before aggregation in conventional centralized FL, LIGHTYEAR uses a peer-to-peer (P2P) topology in which clients exchange updates directly and evaluate incoming models on private validation data. Each client selects only updates that are beneficial for its own target domain and aggregates them using a regularized rule that improves stability under heterogeneity.
Across five datasets and nine baseline methods, LIGHTYEAR consistently outperforms centralized FL baselines and existing P2P approaches.

---


### 175. [Structuring the Space of Perspectives](https://arxiv.org/abs/2608.12113)

**<font color=#1a73e8>作者：</font>** Agnese Daffara, Sebastian Padó, Tanise Ceron  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The same event can be reported from different perspectives depending on the experiences, background, and beliefs of the writer or speaker. A variety of NLP areas engage with perspectives, spanning from text analysis to algorithm optimization. A wide range of operative concepts (such as stances, sentiment, frames, and arguments) has been used to capture perspectives in texts, however the precise relationships among those concepts remain unclear. Arguably, a deeper theoretical understanding of these concepts would empower more effective research on perspectives. In this paper, we address this gap by reviewing the space of perspectives in NLP and defining a set of properties that help distinguishing perspective-related concepts. Our analysis leads us to posit a hierarchy which organizes these concepts linearly along a single axis. Finally, we show how this principled conceptual hierarchy can help researchers navigate the field and select operationalizations of perspective that align with their specific research objectives.

---


### 176. [Attractor Image-Based Deep Learning of Arterial Pulse Waves for Age Classification](https://arxiv.org/abs/2608.12117)

**<font color=#1a73e8>作者：</font>** Sara Vardanega, Patrick Segers, Philip Aston 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Arterial pulse waveform morphology evolves with age, reflecting structural and functional changes in the cardiovascular system. Thus, vascular age is a valuable surrogate marker of cardiovascular health, and premature vascular ageing can indicate increased disease risk. Pulse wave analysis could support risk stratification in otherwise asymptomatic adults. We transformed pulse wave time-series data from photoplethysmography (PPG) and arterial tonometry into images, using the Symmetric Projection Attractor Reconstruction (SPAR) method. These SPAR images were used to train a convolutional neural network to classify healthy subjects into two closely spaced age groups (35-40 and 50-55 years). The model demonstrated consistent classification performance across internal and external test sets, achieving F1 scores above 70% for both PPG and tonometry signals. These results suggest that SPAR-derived pulse wave images contain discriminative morphological features even among healthy adults close in age. This proof-of-concept lays the groundwork for future research into the use of SPAR for early risk detection using smart wearables.

---


### 177. [Adversarial Resilience of Poisson-Process Submodular Maximization over Matroids: From Robust Offline Optimization to Full-Bandit Learning](https://arxiv.org/abs/2608.12134)

**<font color=#1a73e8>作者：</font>** Vaneet Aggarwal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study nonnegative submodular maximization subject to a general matroid when the offline algorithm is given an arbitrary controlled value oracle. Our main result is an adversarial resilience theorem for the Spiteful Greedy Swap Poisson Process (SGS-Poisson): without modifying its Poisson intensity, single-element exchange rule, or spiteful drop step, the algorithm retains limiting approximation factors $1/e$ for non-monotone objectives and $1-1/e$ for monotone objectives. More precisely, under every controlled oracle $\widehat f$ satisfying $|\widehat f(S)-f(S)|\le \xi$ for every set $S$, our implementation returns a feasible set with expected value at least $(1/e-\varepsilon)\OPT-O(k\xi)$ and $(1-1/e-\varepsilon)\OPT-O(k\xi)$, respectively, using $\widetilde O(nk^2\varepsilon^{-2})$ oracle calls. As a consequence, the offline-to-online reduction yields full-bandit CMAB algorithms for general matroid-constrained submodular rewards with exact limiting approximation-regret factors $1/e$ and $1-1/e$ and $\widetilde O(n^{1/5}k^{4/5}T^{4/5})$ regret.

---


### 178. [Autonomous Telerehabilitation via Skeletal Motion Prediction and Joint-Level Performance Assessment](https://arxiv.org/abs/2608.12145)

**<font color=#1a73e8>作者：</font>** Lara Pereira, João Ruivo Paulo, Pedro Santos 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous rehabilitation systems must not only recognize human motion but also provide structured feedback to support users without continuous therapist supervision. This paper presents a telerehabilitation pipeline that integrates skeleton-based exercise quality assessment and short-term motion prediction into a two-module system operating on marker-free RGB video. A self-attentive Bidirectional LSTM performs exercise quality classification using MMD-NCA metric learning, while a graph-based motion prediction module computes per-joint position errors between predicted and observed poses, generating spatially localized deviation signals. Each module is evaluated independently on established benchmarks: the classifier achieves 96.45% mean-class accuracy on squat sequences from the PROZIS dataset, and the adopted STARS predictor achieves a mean MPJPE of 75.8 mm at 560 ms on Human3.6M, outperforming graph and recurrent baselines across all prediction horizons. The framework is designed for eventual deployment in assistive robotics and home-based rehabilitation contexts; end-to-end integration and clinical validation are important directions for future work. By combining motion recognition and prediction in a single system, this work contributes a step toward autonomous, feedback-driven telerehabilitation, for more accessible and scalable rehabilitation solutions.

---


### 179. [TGRHuman: Text-Guided Realistic 3D Human Generation via Diffusion Renderer](https://arxiv.org/abs/2608.12175)

**<font color=#1a73e8>作者：</font>** Muxin Zhang, Chaohui Yu, Yuanwang Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Realistic 3D human generation plays a crucial role in many graphics applications. However, current methods still struggle to generate high-quality human geometry and texture while maintaining 3D consistency and inference efficiency. In this work, we address these limitations by introducing TGRHuman, a novel approach for generating realistic 3D humans from text. Our method decouples geometry and texture generation to alleviate the issues commonly encountered in NeRF-based methods. Instead of relying on slow, implicit score-distillation-based optimization, we directly use explicit multi-view observation generation and optimization for efficient 3D synthesis. For geometry generation, we propose a high-resolution generative module for multi-view normals together with a geometry-carving strategy that preserves view consistency and supports loose clothing. For texture generation, we produce spatially consistent RGB observations from densely sampled surrounding views using a carefully designed texture-prior acquisition strategy and a diffusion renderer, enabling detailed human texture synthesis. Experiments show that our method can generate high-quality and consistent 3D human geometry and texture efficiently. TGRHuman outperforms existing text-to-3D human methods in both geometry and texture quality.

---


### 180. [Map-Det3D: Metric Feed-Forward 3D Reconstruction Prior for Multi-view 3D Object Detection from Streaming Inputs](https://arxiv.org/abs/2608.12179)

**<font color=#1a73e8>作者：</font>** Yung-Hsu Yang, Luigi Piccinelli, Samuel Rota Bulò 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Metric 3D object detection is a core capability for embodied agents, yet most reliable systems lean on depth sensors, trading away cost, power, and integration simplicity. This motivates monocular 3D detection, which avoids additional constraints, yet it faces a major obstacle: from a single image, depth, and especially absolute scale, are underconstrained. As a result, the prevailing pattern of detecting in 2D and then predicting 3D attributes is often brittle, since modest range errors can dominate 3D localization, and the learned scale prior can fail when cameras, motion, or environments undergo domain shifts. To address this, we propose Map-Det3D, an online multi-view 3D object detection model that brings detection directly into a 3D space reconstructed from RGB. We map a short temporal window into multiple views and repurpose a feed-forward metric 3D reconstruction model as our geometric backbone while tuning its object-aware capabilities. Building on this representation, Map-Det3D directly predicts boxes in metric 3D space, without the widely used 2D-to-3D lifting. Experiments across different benchmarks show that this design supports strong online performance and robust transfer without adaptation, suggesting that training reconstruction priors for detection is a practical route to stable metric 3D detection from monocular video. Code and models are available at this https URL.

---


### 181. [GenFAR: A generalized representation of brain structure, derived from 49,246 multi-cohort MRIs via deep learning](https://arxiv.org/abs/2608.12185)

**<font color=#1a73e8>作者：</font>** Vishnu M. Bashyam, Guray Erus, Junhao Wen 等 32 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models for neuroimaging have largely been developed for individual tasks, limiting knowledge transfer across applications. Here we introduce GenFAR, a modular deep learning framework that learns general, clinically informed features from brain MRIs. We trained this modular architecture on 49,246 individuals across 11 cohorts, using 17 diverse classification and regression tasks spanning cognition, clinical, diagnosis, demographics, and biomarkers. This yields aggregated, focused feature sets that capture rich, clinically- and biologically-relevant brain representations. We developed a sequential learning approach where tasks progressively build on previously learned representations. Through an analysis of 5,000 task sequences, we identified an optimal sequence length of six tasks and introduced a Donor Score metric to quantify each task's contribution to downstream performance. This analysis revealed five consistently strong donor tasks (Age, AD/MCI, MMSE, Hypertension, Hyperlipidemia) that formed the base of our sequential model. We demonstrated the utility of our learned representation, in various tasks beyond those included in the training set, to serve as the foundation for specialized secondary predictors. We further showed that using the learned feature representation can substantially increase the sample efficiency of secondary deep learning training tasks and models, as well as improve their accuracy.

---


### 182. [HSTGFormer: Hyper Spatial-Temporal Graph Transformer for 3D Human Pose Estimation](https://arxiv.org/abs/2608.12187)

**<font color=#1a73e8>作者：</font>** Ruochen Li, Shuang Chen, Wenke E 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Transformer-based methods have achieved strong performance in monocular 3D human pose estimation, but most existing approaches organise spatial and temporal reasoning as separate stages, which may weaken unified spatial-temporal interdependencies inherent in human motion and compress frame-level structural information before temporal modelling. In this paper, we propose HSTGFormer, a graph-enhanced Transformer framework that reformulates spatial-temporal reasoning as localised coupled graph aggregation over joint-time nodes. Specifically, HSTGFormer introduces a Hyper Spatial-Temporal Graph (HSTG), which decomposes global spatial-temporal reasoning into local spatial-temporal receptive fields around individual joint-time nodes by extending per-frame skeleton graphs into temporal neighbourhoods, thereby enabling structure-aware coupled reasoning while preserving local structural motion information. It further incorporates an Adaptive Dual-Scale Temporal Graph (ADSTG) to capture joint-specific temporal dependencies over complementary short- and long-range windows. A lightweight node-wise fusion module further adaptively integrates the two graph representations for each joint-time node. Experiments on Human3.6M and MPI-INF-3DHP show that HSTGFormer achieves strong accuracy with high computational efficiency.

---


### 183. [Machine Learning-Based Cyber Defense for Cloud Infrastructure: An Adaptive Deep Q-Network Architecture for Intelligent Intrusion Detection and Automated Threat Mitigation](https://arxiv.org/abs/2608.12190)

**<font color=#1a73e8>作者：</font>** Md Yassir Mottalib, Md Yousuf, Eklachur Rahman Bhuiyan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the increasing complexity of cyber assaults in cloud environments, adaptable security solutions are needed that can support real-time detection and autonomous response. In this paper, we propose a reinforcement learning-based dynamic cyber defense framework. We deploy a Deep Q-Network (DQN) to train effective defensive strategies to counteract the evolving cyberattacks. We leverage the CICIDS2017 dataset for model creation and the UNSW-NB15 dataset for external validation, involving preprocessing of data, feature engineering, and adaptive policy learning. We compare the proposed DQN with decision tree, support vector machine, random forest, XGBoost, and multilayer perceptron models. The proposed DQN achieves an accuracy of 99.72%, a precision of 99.68%, a recall of 99.65%, an F1-score of 99.66%, and an ROC-AUC of 0.999, while the false positive rate is 0.31%, the false negative rate is 0.35%, and the detection latency is 15 ms. The framework achieved 99.54% attack mitigation rate, demonstrating strong adaptive and real-time defensive capabilities. These results demonstrate the potential of reinforcement learning as a powerful and scalable approach for autonomous cybersecurity in modern cloud environments.

---


### 184. [How to Spend Your Oracle Budget: Practical Guidance for Protein Structure Prediction Models](https://arxiv.org/abs/2608.12192)

**<font color=#1a73e8>作者：</font>** Aleksandra Kalisz, Jack Simons, Krisztina Sinkovics 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Foundation models for protein structure prediction remain unreliable on certain targets. External oracles can flag and correct these failures, but biological oracles are expensive, making oracle budget a critical constraint. Existing guidance methods, such as FK-steering, DPO, and Best K-of-N sampling, differ in how they spend this budget, yet no systematic comparison exists to guide method selection. To bridge this gap, we benchmark these methods alongside the recently proposed Optimisation Over Outputs (O3), which applies off-the-shelf optimisers within a generative model's latent subspace. We extend the usage of O3 to protein structure prediction models. Overall, our work provides the first practical reference for oracle budget-aware guidance. Our evaluation on two protein targets, calmodulin (1CLL) and E. coli aspartate transcarbamoylase (9EEH), reveals that no single method consistently dominates across all budgets and oracles. Specifically, O3 proves most effective at low oracle budgets, while FK-steering and DPO demonstrate improved performance as the budget increases. We distil these findings into actionable recommendations for practitioners operating under real-world oracle-budget constraints.

---


### 185. [HYDRA: Hyperbolic Dynamic Representation Architecture for Kolmogorov-Arnold Networks](https://arxiv.org/abs/2608.12194)

**<font color=#1a73e8>作者：</font>** Zhao Su, Yuxin Xia, Haoran Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) enhance nonlinear function approximation by replacing scalar weights with learnable univariate functions. However, assigning an independent function to every connection results in substantial parameter redundancy, limiting their scalability and efficiency. To reduce this redundancy, we introduce \textbf{HY}perbolic \textbf{D}ynamic \textbf{R}epresentation \textbf{A}rchitecture (HYDRA), a parameter-efficient hyperbolic extension of KAN that combines spline-based functional learning with representations in the Poincaré ball. HYDRA maps vector-valued inputs into a bounded hyperbolic latent space, performs KAN-style updates in tangent space, and employs a low-rank prototype block to share functional transformations across hidden dimensions. The resulting hyperbolic representations provide a structured radial coordinate for interpretation, while radius control improves training stability by preventing boundary saturation. Extensive experiments across eight benchmark datasets demonstrate that HYDRA consistently achieves competitive or superior predictive performance while improving parameter efficiency and representation interpretability.

---


### 186. [M-Net: Integrating Spectral Features and Physical Field Operators into Deep Learning for Medical Image Segmentation](https://arxiv.org/abs/2608.12196)

**<font color=#1a73e8>作者：</font>** Jing Zhu, Ye Wang, Fumin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Deep learning-based medical image segmentation has achieved remarkable success, yet purely data-driven approaches often fail to exploit the rich mathematical structure inherent in medical images. We investigate whether explicit mathematical inductive biases, specifically matrix spectral analysis and vector calculus operators, can enhance segmentation beyond data-driven learning alone. Methods: We propose M-Net (Math-Augmented Network), which integrates three complementary mathematical priors into U-Net: (1) continuous spectral features derived from the condition number of centered local pixel matrices, providing a differentiable measure of texture ill-conditioning; (2) physical field operators (divergence and a discrete curl-like boundary irregularity operator) computed from image gradient fields, capturing focal intensity extrema and edge non-smoothness; and (3) a Math-Attention Gate (MAG) that adaptively fuses mathematical features with CNN-extracted deep features at skip connections. Results: Experiments on three benchmarks (LiTS, KiTS, and BraTS) show that M-Net achieves Dice scores of 78.42%, 76.15%, and 83.67%, outperforming baseline U-Net by 12.37%, 3.52%, and 5.55% on liver, kidney, and brain tumor segmentation, respectively. Ablations reveal that the condition-number feature contributes a 2.14% gain over binary invertibility features, while MAG adds 1.45% over simple concatenation. Conclusion: M-Net establishes that mathematical inductive biases provide effective complementary information for medical image segmentation. The continuous condition-number feature offers superior gradient information over discrete alternatives, and MAG preserves these priors throughout the network. This work opens avenues for integrating linear algebra and vector calculus into deep architectures for medical imaging.

---


### 187. [GeoFlow: Efficient Driving Video Generation via Geometry-Aligned Priors](https://arxiv.org/abs/2608.12203)

**<font color=#1a73e8>作者：</font>** Jiazheng Liu, Hang Li, Jiawei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generative models like Diffusion Models and Flow Matching have demonstrated remarkable capabilities in synthesizing high-fidelity driving videos, but are severely constrained by high inference latency due to the requirement of extensive sampling steps. We argue that this inefficiency stems from the prevailing reliance on a standard Gaussian source distribution, where consecutive frames are initialized as independent Gaussian noise. This paradigm disregards the rich spatiotemporal correlations inherent in driving videos, compelling the model to regenerate deterministic scene structures existing in previous frames from noise, which is both computationally redundant and prone to geometric inconsistency. To address this problem, we propose GeoFlow, a novel framework designed to achieve efficient driving video generation by harnessing explicit geometric priors. Instead of sampling from standard Gaussian noise, we leverage multi-view geometry and spatially-adaptive noise injection to construct a Geometry-Aligned Prior (GAP) distribution as starting point. This initialization bridges the gap between source distribution and data distribution, yielding a significantly straighter and shorter sampling trajectory. Extensive experiments demonstrate that GeoFlow can achieve remarkable efficiency of both training and inference: merely several hours of fine-tuning on baseline models can significantly boost few-step generation quality, while fully converged training drastically reduces number of inference steps required for state-of-the-art video generation.

---


### 188. [Few-Shot Ordinal Learning for Day-Wise Freshness Estimation with Hyperspectral Fish Images](https://arxiv.org/abs/2608.12230)

**<font color=#1a73e8>作者：</font>** Kazi Nabiul Alam, Pooneh Bagheri Zadeh, Akbar Sheikh-Akbari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-destructive food quality assessment has increasingly benefited from hyperspectral imaging (HSI), which captures spectral signatures linked to biochemical changes during storage. Estimating day-wise freshness, however, remains challenging owing to strong inter-fillet variability and scarce labelled data per product. All existing deep learning approaches for HSI-based freshness prediction operate under full supervision, requiring densely annotated training sets that are costly to obtain at the individual-product level. We introduce, to the best of our knowledge, the first few-shot learning framework for HSI-based food quality estimation. Each fillet defines a distinct episodic task, and a CORAL-style ordinal prediction head captures the ranked nature of freshness progression through cumulative threshold modelling. Biologically grounded monotonicity and embedding smoothness constraints further guide predictions toward plausible trajectories. On a 16-day salmon HSI dataset under a strict unseen-fillet protocol, our method achieves a mean absolute error of 1.58 days and 2-day accuracy of 72.3% with only three labelled days per fillet, substantially outperforming scalar regression and label-distribution baselines under an identical unseen-fillet protocol.

---


### 189. [An Efficient Near-Optimal Algorithm for Adversarial $m$-Set Bandits](https://arxiv.org/abs/2608.12231)

**<font color=#1a73e8>作者：</font>** Francesco Bacchiocchi, Tommaso Cesari, Roberto Colomboni  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study adversarial combinatorial bandits with $m$-set actions, where at each round the learner selects $m$ out of $d$ items and observes only the aggregate loss of the selected items. The resulting action set contains $K=\binom{d}{m}$ elements and can therefore be exponentially large. Nevertheless, the loss of every action is determined by the same $d$-dimensional vector of item losses. We propose a computationally efficient algorithm that exploits this structure without explicitly enumerating the action set. Against adaptive non-anticipating adversaries, it guarantees, with probability at least $1-\delta$, regret against the best fixed action of \[
R_T =
O\left(\sqrt{dT\log(K/\delta)}\right). \] This matches the high-probability regret bound of the finite-action EXP3-KW algorithm of Zimmert and Lattimore, whose direct implementation may require exponential space. Our algorithm instead represents each sampling distribution with $d$ parameters and runs in polynomial time without enumerating the action set. Thus, it resolves the open problem posed by Maiti et al.

---


### 190. [ScaleVid: Geometry-Aware Video Object Scaling with Mesh-Free Inference](https://arxiv.org/abs/2608.12232)

**<font color=#1a73e8>作者：</font>** Youze Huang, Penghui Ruan, Bojia Zi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geometry-aware video object scaling aims to anisotropically resize the object along object-centric axes while preserving geometric plausibility, temporal coherence, and background consistency. Existing text-guided methods mainly operate in the 2D image plane, while depth-guided approaches provide coarse control and mesh-based methods require costly 3D reconstruction. We present a progressive two-stage training framework that decouples geometry-aware foreground transformation from background preservation and realistic video composition, without mesh-pixel alignment and explicit 3D reconstruction at inference. In both stages, geometrically perturbed pseudo-sources are constructed from real videos, while the original complete videos are retained as reconstruction targets. The first stage uses planar transformations to learn robust foreground-background composition, whereas the second introduces object-centric 3D deformation guidance for geometry-aware scaling. This pseudo-source reconstruction formulation enables real-video synthesis without paired real-world scaling targets. We construct complementary paired-geometry and real-background benchmarks and further evaluate on in-the-wild videos. Extensive experiments demonstrate superior geometric consistency, foreground fidelity, and background preservation, together with faster and more practical inference than methods requiring explicit 3D reconstruction.

---


### 191. [HAMP-LIC: Hessian-Aware Mixed-Precision Post-Training Quantization for Learned Image Compression](https://arxiv.org/abs/2608.12239)

**<font color=#1a73e8>作者：</font>** Yuefeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Use this plain-text version for the arXiv abstract field: Learned image compression (LIC) models achieve strong rate-distortion performance but are hindered by high computational complexity and encoding-decoding mismatches across heterogeneous hardware platforms. Uniform fixed-precision quantization alleviates these issues but suffers severe quality degradation at low bit widths because it ignores differences in the quantization sensitivities of individual layers. To enable efficient and accurate low-bit deployment of pretrained LIC models, we propose HAMP-LIC, a Hessian-aware mixed-precision post-training quantization (PTQ) framework with a four-stage optimization strategy. First, block-wise sensitivity is estimated from the Hessian trace to capture second-order importance. Second, a task-aware refinement module adjusts these sensitivities by jointly considering quantization distortion and rate-distortion performance. Third, guided by the refined sensitivity profile, bit widths are allocated under a global model-size constraint to balance efficiency and reconstruction quality. Finally, block-wise reconstruction using a small calibration set further suppresses quantization error. Experiments on representative LIC models, including Minnen2018 and Cheng2020, demonstrate that HAMP-LIC achieves up to 4.85x model compression with as little as 0.59% BD-rate loss. It consistently outperforms existing fixed- and mixed-precision PTQ methods across multiple datasets while completely eliminating cross-platform encoding-decoding errors.

---


### 192. [Automated Borehole Core Analysis with Report-Derived Weak Labels and Supervised Crack Segmentation](https://arxiv.org/abs/2608.12252)

**<font color=#1a73e8>作者：</font>** Usama Imdad, Ali Khan, Luke Lu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Borehole archives commonly contain core tray photographs and corresponding digital log reports, but no native pixel-level crack annotations. We investigate two complementary approaches for extracting defect-spacing information from these archives. First, structured spacing categories recovered from the report text layer provide weak interval-level labels for classification. A DINO encoder trained on unlabeled core crops supplies domain-specific representations, and a manually verified subset is used to identify label inconsistencies. Second, we manually annotate 5,087 extracted core-row images and evaluate fully supervised crack-segmentation models. Our gated U-Net combines PiDiNet edge maps with Mask R-CNN masks through a learned spatial gating mechanism. This configuration achieves an F1 score of 0.860 and a crack-class IoU of 0.754, the highest result among the evaluated segmentation configurations. Deterministic post-processing converts predicted crack locations into defect-spacing categories. Separate rule-based branches estimate core-relative bedding angles and lithological color descriptors; their predictions agree with log-report references on 75.4% and 84.7% of 1,200 evaluated images, respectively. Because these references are extracted from existing reports, the reported values measure agreement with recorded geological observations rather than independent physical accuracy. The resulting framework combines report-derived weak supervision for spacing classification with fully supervised segmentation for image-based crack localization.

---


### 193. [Calibration Bets on the Past: Post-Training Quantization for Financial Time-Series Forecasting](https://arxiv.org/abs/2608.12259)

**<font color=#1a73e8>作者：</font>** Junyi Ye, Ivy Gateri Wanjiku  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Financial forecasting models are typically developed in full precision, yet production deployment often requires low-precision inference to reduce memory and computational cost. Post-training quantization (PTQ) enables such deployment without retraining. However, reliable activation quantization requires calibration: activation ranges are estimated from historical data before deployment and then remain fixed during future inference. The importance of this deployment choice for financial forecasting remains poorly understood. We present a systematic study of activation calibration for PTQ in cross-sectional volatility forecasting on the S&P 500. Our evaluation covers seven representative neural architectures, eight walk-forward test years (2018-2025), and 560 trained models. We find that activation calibration has little effect at 8 bits but becomes the primary determinant of predictive performance at 4 bits. Under default absolute-maximum (abs-max) calibration, static 4-bit quantization of both weights and activations removes 11-62% of the full-precision mean information coefficient in affected architectures. Replacing abs-max with percentile calibration recovers 53-94% of this degradation in the four most affected architectures. The preferred activation range also varies across market periods. Narrow ranges improve resolution under typical market conditions but lose part of their advantage when test-period market dispersion exceeds the calibration history. These findings show that activation calibration is a first-class deployment decision for reliable 4-bit PTQ in financial forecasting. When substantial degradation remains, 8-bit activations or weight-only 4-bit quantization provide more robust deployment choices.

---


### 194. [Earth observation embeddings are effective sub-grid descriptors for probabilistic weather downscaling](https://arxiv.org/abs/2608.12271)

**<font color=#1a73e8>作者：</font>** Pedro Sousa, Will Tebbutt, Sadiq Jaffer 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Global weather reanalyses and forecasts resolve the evolving atmospheric state on coarse grids, but site-specific applications require predictions at arbitrary locations where near-surface conditions also depend on unresolved terrain and land-surface properties. Existing probabilistic downscalers address this gap using hand-crafted topographic descriptors. We ask instead whether Earth observation foundation models can provide transferable sub-grid surface representations for probabilistic weather downscaling.
We augment a convolutional conditional neural process that downscales coarse ERA5 reanalysis fields at ~25 km resolution with a learned local surface descriptor, obtained by compressing a patch of TESSERA embeddings at 10 m resolution. Although these embeddings summarise surface conditions over annual timescales, they improve downscaling of instantaneous 2 m temperature and 10 m wind speed by encoding persistent surface properties that capture a location's departure from the coarse-grid atmospheric state. Across five climatically diverse regions, the embedding improves point and probabilistic skill at stations held out in both space and time, overall improving CRPS skill by 11.5% for 2 m temperature and 6.2% for 10 m wind speed. We further analyse how its contribution differs by variable, finding that topography explains more of temperature's sub-grid structure, while TESSERA provides additional surface information for wind speed.
These improvements persist when the coarse input is changed from ERA5 to forecasts from the Aurora AI forecasting model, and when predicting at newly deployed stations with no regional history. To our knowledge, this is the first evidence that long-timescale Earth-observation embeddings can support short-timescale weather downscaling where sub-grid departures are systematically structured by persistent surface properties.

---


### 195. [A Neighborhood Attention Transformer Network for Enhanced 3D Segmentation of the Left Anterior Descending Artery](https://arxiv.org/abs/2608.12274)

**<font color=#1a73e8>作者：</font>** Rafi Ibn Sultan, Chengyin Li, Yiannos Demetriou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Background: Accurate segmentation of the Left Anterior Descending (LAD) artery in 3D free-breathing, non-contrast CT is critical for cardiac dose sparing in thoracic radiotherapy. The LAD is extremely small, has poor soft-tissue contrast, and varies substantially across patients; even manual contours show limited inter-observer agreement, underscoring the ambiguity of the vessel boundaries. Purpose: To develop a transformer-based framework that improves LAD delineation in low-contrast, imbalanced CT through local-global context modeling and uncertainty-guided optimization. Methods: We propose NA-UNETR, a 3D transformer-based segmentation model whose Neighborhood Attention (NA) and Dilated NA (DiNA) blocks jointly capture fine structural detail and long-range context. Given the scarcity of annotated LAD data, the model is pretrained on 1,000 CTA volumes of general coronary anatomy and fine-tuned with LoRA-based parameter-efficient adaptation on 20 free-breathing institutional CT scans. A composite Dice-Focal and Hausdorff loss, dynamically balanced via homoscedastic uncertainty, improves overlap and boundary accuracy. Results: NA-UNETR reached 45.64% Dice, 38.16 mm HD95, and 10.01 mm ASD, improving Dice by 3.10 percentage points over nnU-Net and reducing HD95 by 2.96 mm relative to Swin UNETR, with the strongest boundary accuracy among all models and improved centerline stability. On ImageCAS it achieved 79.49% Dice, 8.89 mm HD95, and 1.02 mm ASD. Ablations confirmed that residual blocks, variable kernels, and uncertainty-weighted loss each contributed. Conclusions: NA-UNETR balances local precision and global context for thin, low-contrast LAD structures, offering a computationally efficient framework for substructure-level cardiac segmentation in radiotherapy planning.

---


### 196. [XYZFlow:Scaling Multi dimensional Shortcut Flows for Efficient Generative Modeling](https://arxiv.org/abs/2608.12276)

**<font color=#1a73e8>作者：</font>** Jinxiu Liu, Xuanming Liu, Kangfu Mei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-fidelity image generation faces a trade-off between speed and quality. Diffusion models produce strong visuals but require costly iterative sampling. Existing efficient methods mainly distill pretrained models into few-step samplers, a challenging process that depends heavily on teacher-model quality. In this paper, we introduce XYZFlow, a framework that rethinks efficient generation through multidimensional scaling of flow matching. Unlike single-step mappings, XYZFlow enhances expressivity by making probability paths more identifiable and learnable through structured multidimensional conditioning. We view autoregressive modeling as implicit flow straightening, where richer context reduces trajectory ambiguity. XYZFlow realizes this idea through two orthogonal dimensions: temporal scaling, which uses non-Markovian conditioning on the full denoising history; and spatial scaling, enabled by Next Shortcut Prediction, which sequentially generates patches using preceding patches' denoising trajectories as priors. Experiments show that XYZFlow achieves state-of-the-art performance, with 7.2-8.5X teacher speedups and competitive FID, while Next Shortcut Prediction delivers superior quality-latency trade-offs over model scaling or step reduction.

---


### 197. [Structural Silence: When AI Infrastructure Fails Speakers of Underrepresented Languages](https://arxiv.org/abs/2608.12278)

**<font color=#1a73e8>作者：</font>** Avijit Roy, Proma Roy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence tools for education and language support are increasingly framed as scalable responses to access gaps in under-resourced communities. Yet the infrastructure underlying these tools, including training corpora, tokenization schemes, evaluation benchmarks, and deployment architectures, can systematically disadvantage speakers of underrepresented languages before a model is trained.
This paper examines these structural barriers through Bengali, one of the world's most widely spoken languages, focusing on AI-assisted education in low-connectivity environments. We identify four interlocking failures: a severe web presence gap, with Bengali accounting for less than 0.5% of global web content despite representing nearly 4% of the global population; a 67:1 training-token deficit between English and Bengali in major multilingual corpora; a tokenization penalty associated with Bengali's alphasyllabary script that compounds the data deficit through higher token fertility; and connectivity exclusion, with individual internet penetration at 36.5% in rural areas compared with 71.4% in urban areas.
These failures reflect longstanding resource-allocation decisions, institutional priorities, and design defaults that did not center underrepresented languages in mainstream AI development. We argue that dataset scarcity should be understood as a structural barrier rather than an isolated technical limitation, and that offline-first design should be treated as an equity-oriented infrastructure strategy. We conclude with directions for linguistics and AI research aimed at reducing these structural inequalities.

---


### 198. [Curvature-Aware Zeroth-Order Optimization for Memory-Efficient Test-Time Adaptation](https://arxiv.org/abs/2608.12279)

**<font color=#1a73e8>作者：</font>** Junming Zhang, Shuyu Yin, Peilin Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) aims to enhance the cross-domain performance of pre-trained models by adapting to unlabeled test data. While most existing TTA methods rely on backpropagation (BP) for finetuning, BP-free methods such as zeroth-order (ZO) methods are more desired in practical on-device scenarios. ZO methods rely only on forward computation, which can largely reduce the complexity and memory overhead of on-device deployment. However, ZO methods suffer from much higher variance compared with first-order methods in estimating the gradient. To address this, we propose an improved ZO method to substantially boost the performance of ZO optimization based TTA. First, we provide an observation to reveal the persistent low-rank Hessian structure of the loss during the adaptation process. Based on this insight, we then propose a loss-landscape curvature-aware zeroth-order (CAZO) method, which leverages a sliding-average estimation of the diagonal Hessian to construct a covariance matrix for anisotropic perturbation sampling. CAZO operates by freezing pretrained weights and optimizing minimal adapter parameters via forward-only passes based gradient estimation, which can substantially reduce the memory overhead compared to BP-based methods. Extensive experiments demonstrate that CAZO significantly outperforms existing TTA methods, achieving state-of-the-art performance while maintaining an excellent balance between accuracy and memory efficiency. Code is available at this https URL.

---


### 199. [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies](https://arxiv.org/abs/2608.12282)

**<font color=#1a73e8>作者：</font>** Ankita Rajaram Naik, Anupama Murthi, Benjamin Elder 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents deployed in enterprise settings must reason across structured APIs and document collections, yet existing benchmarks evaluate these capabilities in isolation. We introduce VAKRA (e\textbf{V}aluating \textbf{A}PI and \textbf{K}nowledge \textbf{R}etrieval \textbf{A}gents), a benchmark of over $8{,}000$ executable APIs across $62$ domains with tasks spanning three settings of increasing difficulty: diverse API interaction styles, multi-hop reasoning over structured APIs, and multi-source reasoning with natural-language tool-use policy constraints. Correctness is verified by re-executing predicted tool calls against live APIs, accommodating multiple valid paths. Using a fixed ReAct harness to isolate model capabilities from agent architecture, we evaluate frontier and open-weight models and find that even the best model achieves only 70.4\% on single-hop endpoint-style tasks and drops to 50--51\% on compositional APIs; performance degrades by over 50\% as reasoning depth increases, and policy-constrained questions expose severe failures (as low as 2.4\% on unanswerable queries). Trace analysis shows failures concentrate at language-mediated reasoning - entity disambiguation, cross-source grounding, rather than tool invocation mechanics. Code is available this https URL. Dataset is available this https URL

---


### 200. [A Framework for Designing Reward Functions: From Objectives to Features to Human-Aligned Reward Functions](https://arxiv.org/abs/2608.12302)

**<font color=#1a73e8>作者：</font>** Di Yang Shi, W. Bradley Knox  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a formal process to enable non-experts to instantiate and iterate on human-aligned reward functions, i.e. reward functions that adhere to a given preference ordering over trajectories. Given a task described in natural language, our process produces a linear reward function in three steps: distill the task's objectives into a set of fundamental objectives and derive measurable outcome variables that capture those fundamental objectives, select a causally representative subset of outcome variables as the reward terms, and fit weights to those reward terms via preference elicitation. Our contributions describe the first step and formalize the latter two steps. The first is a guided workflow for deriving outcome variables. The second is a reduction of reward term selection to minimum-cost partial cover on a causal DAG, solved in polynomial time via max-flow. The third is a geometric framing of weight fitting as a convex feasibility problem iteratively narrowed by preference queries, solved by existing separation oracle methods. To the best of our knowledge, this is the first reward-design method that maintains a deterministically conflict-free feasible weight region, narrowed to a desired tolerance via a separation oracle with O(n log \kappa) preference queries.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-202](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
