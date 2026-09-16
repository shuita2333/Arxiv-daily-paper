# 📦 其他研究 | 2026年09月17日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-219](./part-05.md)

---

### 151. [Beyond In-Distribution Metrics: A Systematic Out-of-Distribution Evaluation of Congenital Heart Disease Segmentation](https://arxiv.org/abs/2609.17068)

**<font color=#1a73e8>作者：</font>** Aniketh Vijesh, Shrisharanyan Vasu, Abhijit Ramesh 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Congenital heart disease (CHD) diagnosis and surgical planning often require patient-specific 3D anatomical models, but manual segmentation is labor-intensive, particularly in complex anatomies. Although deep-learning methods can automate this process, they are typically evaluated in-distribution, despite clinically relevant shifts in scanner, protocol, institution, population, and imaging modality. We present, to our knowledge, the first systematic evaluation of out-of-distribution (OOD) generalization in CHD segmentation, using ImageCHD as a held-out target cohort. We compare representative segmentation architectures under combined CT and CMR training, CT-only training, self-supervised pretraining, and limited target-domain adaptation. In-distribution performance proves to be a poor indicator of cross-cohort robustness: nnU-Net achieves the highest validation Dice (0.77) but falls to 0.51 on ImageCHD, while SwinUNETR generalizes substantially better, reaching 0.67 Dice. MAE and JEPA pretraining provide only modest additional benefit, suggesting that architecture contributes more to robustness than the tested pretraining strategies in this setting. When limited target-domain supervision is introduced, all SwinUNETR variants exceed 0.76 Dice with only 11 labeled ImageCHD cases. These findings demonstrate that conventional in-distribution evaluation can obscure clinically important generalization failures and support explicit cross-dataset testing as a key component of CHD segmentation evaluation.

---


### 152. [Sample-Conditioned Representation Selection for Audio Few-Shot Learning](https://arxiv.org/abs/2609.17076)

**<font color=#1a73e8>作者：</font>** Fengrui Liu, Ningxin Shen, Yi Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Few-shot audio classifiers may rely on foreground-background co-occurrences and fail when those correlations shift. On SpurAudio, the resulting representation shift is concentrated and class dependent: for ResNet12, the top 10 percent of channels explain 82.80 percent of the null-corrected shift contribution. We propose SAMPLESELECT, which predicts a fixed-budget feature mask independently for each input while keeping the encoder and source classifier frozen. Training uses differentiable Gumbel Top-k selection with foreground classification and cross-background contrastive losses; inference uses deterministic Top-k masks and support-only linear adaptation. Across ResNet12 and Conv64 in 5-way 1-shot and 5-shot evaluation, SAMPLESELECT gives the best OOD accuracy among the compared methods and improves the matched full-representation control by 4.90-8.38 percentage points. Ablations and representation analyses further support the learned selection mechanism. Code is available at this https URL

---


### 153. [Scaling-Score Conformal Prediction for Multi-Target Regression](https://arxiv.org/abs/2609.17091)

**<font color=#1a73e8>作者：</font>** Sylvain Rousseau, Soundouss Messoudi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-target regression requires a model to simultaneously predict several related outputs. Conformal prediction provides distribution-free, finite-sample marginal coverage guarantees, but extending these to joint multi-dimensional regions in a model-agnostic, sample-efficient manner remains challenging: max-aggregation ignores scale differences, copula-based methods are only asymptotically valid, rectangular methods typically split the calibration set, and quantile or density-based methods require training a specialised model beyond a plain point predictor. We propose the scaling-score conformal method, which is model-agnostic (requires only component-wise absolute residuals), uses a single calibration set, and yields four nested output types: an outer rectangle (SCO) with valid joint coverage, the exact set R $\alpha$ , a staircase (SC 2 ) over approximation of R $\alpha$ , and an inner rectangle (SCI). A single hyperparameter $\gamma$ $\in$ (0, 1) controls the base-rectangle quantile level independently of $\alpha$. We prove downward-closedness and a rectangular sandwich bound and derive a closed-form outer rectangle. Experiments on 29 realworld datasets confirm valid joint coverage; SC 2 with $\gamma$ = 1-$\alpha$ consistently achieves competitive volume relative to baselines, with the advantage growing with output dimension d.

---


### 154. [Hub-Spectral Activation of Latent Multimodal Knowledge](https://arxiv.org/abs/2609.17094)

**<font color=#1a73e8>作者：</font>** Ying Guo, Haidong Chen, Linrui Xu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal representation learning seeks shared representations for cross-modal retrieval and knowledge transfer. Hub-based binding reduces pairwise supervision costs, but separate hub connections cannot guarantee reliable alignment between modalities without direct joint training. We introduce Hub-Spectral Activation (HSA), a closed-form method for recovering and activating the hub-readable component of latent multimodal knowledge in frozen representations. We formalize this knowledge as source-induced cross-modal dependence and characterize the component determined by the second-order statistics of two trained hub edges. Under a second-order source model, we establish conditions for exact recovery of the complete source-induced relation and bound the dimension of its hub-readable component by the hub covariance rank. HSA composes and standardizes hub-edge statistics, extracts paired spectral directions, and combines reliability-weighted matching evidence with source-gated candidate resolution for bidirectional retrieval and prototype classification. HSA requires no target-pair supervision, gradient optimization, or backbone updates. Across 19 retrieval and 11 prototype-classification relations on ImageBind and LanguageBind, HSA raises mean bidirectional Recall@10 from 18.27% to 31.15% and mean macro Top-1 accuracy from 29.01% to 52.43%, respectively. Controlled analyses further identify valid hub-edge correspondence and leading spectral directions as key sources of retrieval gains, demonstrating the utility of latent multimodal knowledge beyond native similarity scores. Code and models are publicly available at this https URL.

---


### 155. [GeoLAM: Learning Geometry-Grounded Latent Actions from Unlabeled Human Videos](https://arxiv.org/abs/2609.17099)

**<font color=#1a73e8>作者：</font>** Yifan Xie, Hekun Tian, Jinkun Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Human videos provide rich manipulation experience, but extracting action representations that preserve useful motion remains challenging. Visual reconstruction alone can entangle manipulation-related motion with appearance changes and camera movement. We present GeoLAM, a framework for learning geometry-grounded latent actions from action-free human videos. GeoLAM combines future-frame reconstruction through a frozen geometric feature hierarchy with motion supervision from a training-only 4D geometry teacher. The geometric representation provides a structural prior, while the teacher's predictions yield spatially pooled targets capturing 3D displacement, residual image-plane motion, and surface-orientation changes. Visibility and confidence weighting reduces the contribution of unreliable estimates, encouraging continuous latent actions to retain geometric motion without explicit hand-pose or hand-trajectory annotations. After video pretraining without action labels, the learned representation provides transition targets for a world-action model trained on action-labeled robot demonstrations. The model jointly denoises latent actions and executable action chunks, with future-video prediction used only as an auxiliary training task. Deployment therefore requires neither the geometry teacher nor future-video generation. Evaluations on a latent-action benchmark and robotic manipulation tasks demonstrate the strong performance of GeoLAM.

---


### 156. [Semi-Supervised Learning-Based Genetic Biomarkers Dataset for Multiple-Stage Hepatocellular Carcinoma Prediction](https://arxiv.org/abs/2609.17100)

**<font color=#1a73e8>作者：</font>** Ahmed Ammar Kubba, Manar Abu Talib, Jibran Sualeh Muhammad 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Liver cancer is a complex disease responsible for a high number of deaths across the globe each year, making automated solutions for liver cancer classification urgent. The most common form of liver cancer is hepatocellular carcinoma (HCC), accounting for over 90% of liver cancer cases. There is a distinct lack of publicly available HCC datasets utilizing genomic data, which is necessary for training artificial intelligence (AI) models for automated HCC classification. This study proposes constructing a multi-stage HCC dataset using XGBoost and Semi-Supervised learning on three separate datasets of genomic biomarkers, utilizing their existing labels in the Semi-Supervised learning process to label the proposed dataset. The proposed dataset consists of 770 patient samples in total, categorized into five classes that represent normal tissue alongside different stages of HCC. Each sample in the dataset consists of 11,150 different gene expression levels. The XGBoost model demonstrated a final classification accuracy of 96.5% during the Semi-Supervised learning process.

---


### 157. [High-Fidelity Digital Twin Data Models by Randomized Dynamic Mode Decomposition and Deep Learning with Applications in Fluid Dynamics](https://arxiv.org/abs/2609.17101)

**<font color=#1a73e8>作者：</font>** Diana A. Bistrian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The purpose of this paper is the identification of high-fidelity digital twin data models from numerical code outputs by non-intrusive techniques (i.e., not requiring Galerkin projection of the governing equations onto the reduced modes basis). In this paper the author defines the concept of the digital twin data model (DTM) as a model of reduced complexity that has the main feature of mirroring the original process behavior. The significant advantage of a DTM is to reproduce the dynamics with high accuracy and reduced costs in CPU time and hardware for settings difficult to explore because of the complexity of the dynamics over time. This paper introduces a new framework for creating efficient digital twin data models by combining two state-of-the-art tools: randomized dynamic mode decomposition and deep learning artificial intelligence. It is shown that the outputs are consistent with the original source data with the advantage of reduced complexity. The DTMs are investigated in the numerical simulation of three shock wave phenomena with increasing complexity. The author performs a thorough assessment of the performance of the new digital twin data models in terms of numerical accuracy and computational efficiency.

---


### 158. [Not Another Text Benchmark: Putting the "Visual" Back in Visual Question Answering for Large Video Models](https://arxiv.org/abs/2609.17112)

**<font color=#1a73e8>作者：</font>** Rwiddhi Chakraborty, Yinong, Wang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large video models have exhibited impressive performance on a wide range of visual question answering tasks, owing to the rise of powerful, pretrained text and vision encoders. The usefulness of such models have also been demonstrated on a wide range of benchmarks, with an important caveat - the dominant approach in these benchmarks evaluates multiple choice reasoning via text options. This is a natural way to test text-based reasoning in these models, and has led to significant insights regarding model behavior in the community. In this work, we ask a different question - what happens when the evaluation modality is visual, rather than text? We introduce three new vision-centric evaluation benchmarks in temporal frame retrieval, video future prediction, and causal memory distortion, all designed around evaluating visual understanding capabilities in large video models. Our approach complements the existing approaches to evaluate video understanding in frontier models. We show that current frontier models exhibit significant weakness when attempting to reason through visual queries, rather than text. We conclude with an extended analysis section that provides pointers for future improvements in visual understanding for large video models.

---


### 159. [Predicting Human Disagreement for Calibrated Dynamic Facial Expression Recognition](https://arxiv.org/abs/2609.17130)

**<font color=#1a73e8>作者：</font>** Yiming Wang, Frederick W. B. Li, Jingyun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dynamic facial expression recognition (DFER) benchmarks such as DFEW provide multiple annotator votes per clip, yet most models collapse them to a majority label and cannot represent human disagreement at inference time. We propose a disagreement-aware DFER framework that trains directly on the raw annotator count vector using a Dirichlet-Multinomial likelihood. Unlike mean-only soft-label objectives, the proposed likelihood provides scale-sensitive supervision for the Dirichlet concentration while preserving the predictive mean. A separate ambiguity head predicts annotation entropy for unseen clips, and a monotone Chow-style reject rule combines predicted ambiguity, vacuity, temporal instability, and input quality for selective prediction. On DFEW, the method preserves recognition accuracy while reducing ECE by 30% and AURC by 15%, and predicted ambiguity reaches a Spearman correlation of 0.52 with the annotation entropy of test clips. The calibration and selective-prediction gains transfer to FERV39k and remain under identity- and movie-disjoint DFEW splits.

---


### 160. [Event-based Selective Attention for Multi-resolution Fast Region of Interest (ROI) Detection](https://arxiv.org/abs/2609.17134)

**<font color=#1a73e8>作者：</font>** Luca Peres, Giulia D'Angelo, Chiara Bartolozzi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neuromorphic vision systems operate under strict constraints on bandwidth, memory, and energy, particularly at the edge, motivating early mechanisms for data reduction and selective processing. In this work, we investigate a multi-scale training-free, saliency-based, bottom-up visual attention model that operates directly on low-resolution event-based input and selects Regions of Interest (ROI) from the visual scene. The model is evaluated across multiple downscaling factors applied to the incoming event stream, with input resolutions reduced by up to 256x relative to full resolution. Performance is assessed on the Prophesee Automotive dataset, the largest publicly available event-based dataset, demonstrating robust ROI selection across different scales on a real-world use-case. The proposed approach is capable of detecting ROIs belonging to multiple object classes, including various vehicle types, pedestrians, traffic lights, and traffic signs, with accuracy up to 70.8%, while operating at millisecond temporal resolution, 16x finer than the temporal resolution provided by the dataset ground truth. These results highlight the potential of combining early event downscaling with saliency-based attention as an effective front-end for efficient edge neuromorphic vision systems.

---


### 161. [From Foundation Embeddings to Cropland Maps: Label Efficiency, Temporal Transferability and Independent Human Validation](https://arxiv.org/abs/2609.17138)

**<font color=#1a73e8>作者：</font>** Mohammad Ammar Mughees, Giovanni Montefoschi, Zhongxin Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models provide reusable representations of satellite imagery that support downstream mapping with limited task-specific modelling. We evaluate whether annual AlphaEarth embeddings support binary cultivated-versus-non-cultivated mapping in Maine, USA, using 192 spatially separated patches and labels derived from the USDA Cropland Data Layer (CDL). Without fine-tuning the foundation model, a lightweight classifier reaches 93.7% overall accuracy and 90.8% balanced accuracy on held-out patches. Logistic regression is within 0.3 percentage points of a gradient-boosted ensemble, while a nearest-class-centroid rule, which uses class centroids but fits no parameters, reaches 90.2%. A balanced sample of 60,000 labelled pixels is within 1.3 percentage points of the full pool of 8.6 million pixels; because pixels are spatially autocorrelated, this result concerns pixel-sample efficiency rather than 60,000 independent annotation sites. In a same-region transfer experiment, classifiers trained in one year remain accurate across 2018 to 2023. Against a blind, two-interpreter consensus at 385 randomly sampled points in one contiguous 2023 block, the AlphaEarth-plus-random-forest map agrees at 95.3% ($\kappa=0.82$), compared with 91.7% for the CDL ($\kappa=0.72$; exact two-sided McNemar $p=0.0161$). This local result is consistent with partial smoothing of CDL label noise, but it does not establish statewide correction of the reference product. On the same points, the difference from a fine-tuned TerraMind segmentation model is not statistically significant (95.3% versus 93.5%; $p=0.14$), and the experiment is not a controlled comparison of computational cost. These results support frozen geospatial embeddings as a low-compute candidate for regional cropland mapping, subject to the limits of a single-state study, a 30 m-derived training reference, and a one-block human validation.

---


### 162. [Observational Indistinguishability and Integrity Blind Regions in Hybrid Quantum-Classical Workflows](https://arxiv.org/abs/2609.17150)

**<font color=#1a73e8>作者：</font>** Roberto Fernández-Barrios, Iker Pastor-López, Amaia Pikatza-Huerga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We present a claim-relative evidence/reference framework for hybrid quantum-classical workflow integrity. Observational indistinguishability yields structural blind regions, distinct from finite-batch statistical misses. Within the declared lattice, a trusted same-batch scalar $R_0$ suffices for conclusion integrity, aggregate $M_0$ for aggregate plus conclusion integrity, and item-aligned binding for item identity. In 3,600 label interventions, feature/prediction views realize exact label-path invariance; all 764 geometry-aligned aggregate-blind rows equal their paired-clean responses, giving zero attack-only increment. For statistical response, the geometry-aligned construction detects 343/2,700 conclusion-changing ($\tau \to 0^+$) label interventions with the conformal rule and 1,183/2,700 with the uncorrected union; the original frozen same-item geometry yields 11/2,617 and 43/2,617, respectively. The executed conformal clean false-action rates are 0.048--0.059 descriptively; its finite-sample guarantee requires exchangeability, which the overlapping-draw design violates. The cluster-preserving adaptive stress test (Gate A) reduces response versus matched controls in 25--40 of 40 environment/split cells while retaining conclusion changes. A bounded 165-design-cell ideal-statevector and finite-shot-emulation branch directly instantiates semantic, estimated and observed kernel transitions. The fixed equal-weight design estimates neither deployment prevalence nor QPU, provider or deployed-service assurance.

---


### 163. [Neural Field Ensembles for Aerodynamic Surface Prediction: Winning Solution to the ONERA CRM Wall Distribution 2025 Challenge](https://arxiv.org/abs/2609.17160)

**<font color=#1a73e8>作者：</font>** Lionel Salesses, Caroline Sainvitu, Tariq Benamara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learning surrogate models offer a promising alternative to high-fidelity Computational Fluid Dynamics (CFD) simulations for aerodynamic analysis and design. However, constructing accurate surrogates for realistic aircraft configurations remain challenging due to complex geometries, multiple flow regimes, and limited training data. This work presents the methodology that achieved first place in the ONERA CRM Wall Distribution Regression Challenge, which focuses on predicting pressure and skin-friction coefficient distributions over the NASA Common Research Model wing-body-pylon-nacelle configuration under different operating conditions. The proposed approach formulates the problem as a conditional neural field mapping spatial coordinates, surface normals, and operating conditions to aerodynamic wall quantities. Fourier feature encoding, a relative squared error objective aligned with the challenge metric, ensemble learning, and $k$-fold cross-validation are progressively introduced to improve prediction accuracy and exploit the limited training data. Beyond presenting the final methodology, the paper documents the successive model design choices that led to the winning solution through a comprehensive ablation study and discusses several alternative approaches that were investigated but ultimately discarded. On the hidden competition test set, the proposed methodology achieves an overall score of 8.81, outperforming the strongest organizer-provided baseline, which achieved a score of 8.64, while requiring approximately three orders of magnitude fewer trainable parameters. These results illustrate that carefully designed coordinate-based neural fields constitute an efficient and robust framework for aerodynamic surrogate modeling on complex geometries under limited-data conditions.

---


### 164. [MUMINS: Metadata-conditioned Uncertainty-aware Medical Image Next-state Synthesis](https://arxiv.org/abs/2609.17169)

**<font color=#1a73e8>作者：</font>** Anna Oliveras, Roger Marí, Rafael Redondo 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Forecasting anatomical changes such as tumor growth and neurodegeneration is a challenging generative vision task. Morphological evolution is subtle relative to static anatomy, highly patient-specific, and inherently stochastic. Existing methods struggle with several issues: deterministic networks ignore biological stochasticity, while standard diffusion models require computationally prohibitive multi-pass sampling to quantify uncertainty. We propose MUMINS (Metadata-conditioned Uncertainty-aware Medical Image Next-state Synthesis), an efficient diffusion framework that jointly diffuses a baseline scan and its follow-up residual, summed to synthesize the follow-up scan, while concurrently predicting a spatial uncertainty map, in a single reverse diffusion process. Conditioned on the time interval and relevant metadata, it preserves fine-grained anatomy by dynamically re-injecting the baseline as a soft anchor at every denoising step, and a negative-log-likelihood head learns the uncertainty map to explicitly flag error-prone regions. Designed without organ-specific heuristics, the same architecture is reused across anatomies via separate, dataset-specific retraining. Extensive evaluations demonstrate that dataset-specific retraining of MUMINS matches or outperforms dedicated, domain-specific state-of-the-art methods on lung CT (PNG) and brain MRI (OASIS-3). Project page: this https URL.

---


### 165. [A unified framework for global and local interpretability using adaptive derivative-ordered random explanation](https://arxiv.org/abs/2609.17171)

**<font color=#1a73e8>作者：</font>** Lemen Chao, Ming Lei, Anran Fanga  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The interpretability of complex machine learning models is of paramount importance, especially in real-world high-stakes domains such as healthcare and finance. However, existing post-hoc interpretability methods suffer from inherent limitations: fragmented analytical processes, inadequate capacity to model nonlinear feature interactions, computational inefficiencies, and over-reliance on specific model architectures. To address these challenges, this paper provides a novel method - Adaptive Derivative-Ordered Random Explanation (ADORE) - that leverages first- and second-order derivatives to accommodate nonlinear model complexities, while enabling effective capture of feature-sample interactions within a unified analytical framework. ADORE integrates global feature importance with local sample contributions, precisely quantifying feature impact by capturing both magnitude and direction, and identifying critical samples influencing model decisions. Furthermore, it achieves computational efficiency through randomized singular value decomposition (SVD) and dynamic sparsity detection, making it scalable to large, high-dimensional datasets. Experiments across three data modalities - tabular, text, and image - demonstrate that ADORE outperforms existing methods such as LIME and SHAP in handling complex interactions and computational efficiency, while providing detailed and reliable explanations. To facilitate adoption and reproducibility, ADORE has been released as an open-source Python package, hosted on GitHub, enabling researchers and practitioners to readily adapt and apply our approach to their specific tasks, models, and datasets.

---


### 166. [IRENE: A Convolutional GRU Ensemble Model for Radar Precipitation Nowcasting over Italy](https://arxiv.org/abs/2609.17175)

**<font color=#1a73e8>作者：</font>** Alessandro Camilletti, Gabriele Franch, Elena Tomasi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present IRENE (Italian Radar Ensemble Nowcasting Experiment), a deep learning model for probabilistic short-range precipitation nowcasting over the Italian domain at \SI{1}{km} spatial and 5 min temporal resolution. IRENE adopts an encoder--forecaster architecture built on multi-scale Convolutional Gated Recurrent Units (ConvGRUs), trained on the national radar composite produced by the Italian Civil Protection Department (DPC). An importance-sampling scheme focuses training on precipitation-relevant events, while the almost-fair Continuous Ranked Probability Score (afCRPS) is adopted as the primary probabilistic loss function. Two additional training configurations are proposed: an adversarial (GAN) variant, IRENE-GAN, designed to improve the spatial sharpness of the generated forecasts, and a spectrally constrained variant, IRENE-GAN-RAPSD, in which the adversarial objective is complemented by an explicit penalty on the radially averaged power spectral density. The three configurations are evaluated against the stochastic extrapolation method STEPS and the pre-trained deep learning model DGMR. All IRENE configurations attain a lower Continuous Ranked Probability Score than both benchmarks at every lead time and rank histograms closer to uniformity, indicating better probabilistic skill and ensemble calibration. In terms of ensemble-mean mean absolute error the advantage is confined to the first 90 min, beyond which the strongly damped DGMR fields and, to a lesser extent, STEPS become competitive. Spectral analysis shows that the adversarial training removes the progressive loss of small-scale variance exhibited by IRENE, at the cost of an excess of fine-scale power at long lead times that the spectral penalty only partially controls.

---


### 167. [MOCC-R1: Reinforcing Reasoning-Response Consistency for Multimodal Counselor Response Generation](https://arxiv.org/abs/2609.17180)

**<font color=#1a73e8>作者：</font>** Wenjie Zheng, Qiming Xie, Jianfei Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal counselor response generation (MCRG) aims to generate an appropriate counselor response from multimodal dialogue histories. Progress is limited by two gaps: first, existing datasets rarely capture sustained, human-recorded counseling interactions conducted by qualified counselors; Second, existing methods do not explicitly optimize consistency between counseling reasoning and the generated response, potentially undermining the reliability of MCRG systems. Thus, we introduce MOCC, a multimodal counseling conversation corpus containing over 200 hours of interactions involving 154 credential-verified counselors. Based on MOCC, we propose MOCC-R1, a two-stage framework for optimizing reasoning-response consistency. Cold-start supervised fine-tuning trains the model to generate a structured trajectory consisting of client-state understanding, a response intent that links a counseling principle to a planned action, and the final response. Reinforcement learning (RL) then rewards grounded plan coherence and plan execution, encouraging the inferred state and plan to be supported by the dialogue context and the response to realize that plan. Experiments demonstrate the effectiveness of the proposed MOCC-R1.

---


### 168. [Multimodal Cultural Heritage Architectural Style Classification for Residential Buildings in the UAE Based on CLIP Embeddings and SVM](https://arxiv.org/abs/2609.17181)

**<font color=#1a73e8>作者：</font>** Ahmed Ammar Kubba, Manar Abu Talib, Iman Ibrahim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The analysis and classification of cultural heritage architectural styles remain challenging due to the complexity of visual images of buildings, which are highly relied on in traditional CNN-based classification approaches in comparison to textual descriptions, and the relative lack of non-western region-specific datasets. This paper addresses this gap by proposing a multimodal machine learning framework to analyze and classify Emirati residential architecture using OpenAI's CLIP model. We integrate visual features from images and textual features from expert descriptions into a unified 512-dimensional embedding, followed by dimensionality reduction with UMAP for visualization and unsupervised clustering using K-Means. Cluster labels, which are derived from manual analysis of the K-Means clusters, are used to train an SVM classifier for automated architectural style classification. Our approach achieves a classification accuracy of 98% across eight identified style clusters, higher than every other study in the literature, demonstrating the effectiveness of combining visual and textual modalities. Overall, this paper highlights the potential of using multimodal AI to support architectural heritage analysis, offering scalable and interpretable tools for exploring regional architectural identities.

---


### 169. [LoopSpec: Pipelined Self-Speculative Decoding for Looped Transformers](https://arxiv.org/abs/2609.17184)

**<font color=#1a73e8>作者：</font>** SangLyul Cho, Langqing Cui, Sehoon Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers achieve strong performance with compact parameter sizes by repeatedly applying a shared stack of Transformer blocks across recurrent depths. However, they incur higher decoding latency than standard Transformer models of comparable parameter size because shared weights are accessed at every recurrent depth. To improve decoding efficiency, self-speculative decoding is particularly well suited to Looped Transformers, as their intermediate recurrent states can directly provide draft predictions without an auxiliary draft model. We therefore propose LoopSpec, a training-free self-speculative decoding framework tailored for Looped Transformers. LoopSpec extracts draft tokens from early recurrent states and operates in a pipelined manner, overlapping draft generation of future tokens with target verification of the current token. To improve draft accuracy without excessive compute overhead, we introduce a selective second proposal from deeper recurrent depth while ensuring lossless decoding under both greedy and sampling regimes. Furthermore, we derive the optimal proposal depths in closed form and show the prediction matches measurement. Across reasoning and coding benchmarks, LoopSpec achieves up to 6.83$\times$ inference speedup across diverse Looped Transformers.

---


### 170. [EventEgoHands++: Event-based Egocentric 3D Hand Mesh Reconstruction with Real Dataset](https://arxiv.org/abs/2609.17189)

**<font color=#1a73e8>作者：</font>** Ryosei Hara, Wataru Ikeda, Masashi Hatano 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D hand mesh reconstruction is a challenging yet essential task for downstream applications, including human-robot interaction and AR/VR. Although conventional cameras have been widely adopted for this task, methods that rely on them struggle in low-light environments and under severe motion blur. To address these limitations, event-based cameras have recently attracted attention for their high dynamic range and high temporal resolution. However, applying event cameras to egocentric hand reconstruction remains challenging because camera wearer's motion produces dense background events that obscure hand-specific signals. Although the first egocentric event-based approach mitigates this issue using hand segmentation, its binary hand mask does not distinguish between left and right hands. As a result, the model lacks instance-level hand information and predicts both hands even when only one or neither hand is present. This limitation leads to incorrect inter-hand relationships and degraded reconstruction accuracy. In this paper, we propose EventEgoHands++, a framework for event-based 3D hand mesh reconstruction from an egocentric viewpoint. The proposed method incorporates a Hand Detector that estimates instance-level bounding boxes and masks for both the left and right hands. Moreover, we introduce Adaptive Attention, which dynamically gates the attention based on these detection results to accurately learn the spatial relationship and mutual interactions between the hands. To train and evaluate our framework, we extend the synthetic N-HOT3D dataset and newly construct EEH-R, the largest real-world event-based egocentric hand dataset to date, comprising approximately 1M annotated frames captured in environments including low-light conditions. Extensive experiments on both synthetic and real datasets demonstrate that our method consistently outperforms the baselines.

---


### 171. [MyoFlow: Anchor-Tied Rectified Flow for HD-sEMG Gesture Recognition Across Sessions and Subjects](https://arxiv.org/abs/2609.17194)

**<font color=#1a73e8>作者：</font>** Chenhao Wu, Dingjie Peng, Satoshi Funabashi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> High-density surface electromyography (HD-sEMG) gesture recognition supports prosthetic control, assistive robotics, and rehabilitation, but electrode re-donning and physiological variability cause distribution shifts that degrade accuracy across sessions and subjects. Generative HD-sEMG models primarily synthesize signals for augmentation; although diffusion models enhance representation learning, prediction still relies on a separate classifier. To tie learned dynamics to the decision rule, we propose MyoFlow, the first discriminative flow-matching framework for HD-sEMG recognition across sessions and subjects. It recasts classification as anchor-tied transport: a domain-conditioned rectified flow moves encoded windows toward gesture anchors that serve as transport targets and define the nearest-anchor decision geometry, enabling zero-shot prediction without an independent head. On the Hyser dataset, MyoFlow improves mean cross-session and cross-subject accuracy over the strongest diffusion-based baseline by 4.24\% and 6.37\%, respectively, and achieves 91.71\% mean zero-shot accuracy and 97.39\% mean few-shot accuracy across multiple days on the CEMHSEY dataset.

---


### 172. [Cross-Domain Inference for Human Localization: Applying Wi-Fi RSSI Data to CSI-Trained Models](https://arxiv.org/abs/2609.17204)

**<font color=#1a73e8>作者：</font>** Ariel Duschanek-Myers, Thomas Welsh, Helmut Neukirchen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Wi-Fi signal data can be used to compromise the privacy of individuals. While many existing approaches rely on Channel State Information (CSI), collecting this data on typical IoT devices often requires elevated operating system permissions and specialized drivers. Consequently, this paper investigates the feasibility of utilizing Received Signal Strength Indicator (RSSI) data to predict human locations. RSSI was selected because it is accessible even on devices with limited user permissions, and therefore is more applicable to a wider array of IoT devices. To bypass the tedious process of obtaining training data needed to train an RSSI-based model, an existing Wi-Fi pose prediction project was used in this research. However, that project assumed CSI data as input. Therefore, we investigate the feasibility of cross-domain inference, i.e., feeding RSSI data into that existing CSI-based model. We collected an RSSI dataset, synchronized with video ground-truth of a person moving within a room, to evaluate the model's performance. This evaluation confirmed that RSSI data can predict locations with approximately 80% confidence when human movement is present. This demonstrates that a model trained on CSI data can be used to evaluate low-granularity RSSI data consisting of decibel-milliwatt (dBm) values to roughly locate people in the collection space. These results imply that a wide range of IoT devices can be used for privacy invasion in Wi-Fi-dense environments.

---


### 173. [[MM/AI] Mental Models in Human-AI Interaction: Methods and Challenges in the Generative and Agentic AI Era (Workshop)](https://arxiv.org/abs/2609.17206)

**<font color=#1a73e8>作者：</font>** Téo Sanchez, Bhada Yun, Prerna Ravi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The mental model construct is widely used in HCI to refer to the knowledge structure people hold in order to reason about and interact with computing systems. Yet it is often operationalized intuitively: the construct is often used interchangeably with related concepts (e.g., folk theories, sensemaking) and methods of studying it (e.g., through elicitation) are many and diverse, with each method resting on distinct assumptions about what counts as a mental model. Generative and agentic AI systems may further complicate mental model formation and elicitation as such systems are opaque by design and increasingly act on users' behalf across files, applications, and on the web. Together, these challenges may hinder the commensurability of research on people's mental models of AI systems. The MM/AI workshop calls for a critical reassessment of how we understand and study mental models in human-AI interaction research. It aims to foster theoretical and methodological exchange on mental models in human-AI interaction, identify open challenges, and develop directions for future research. We invite short papers on users' or stakeholders' mental models of AI systems, particularly contributions that reflect on the conceptual and methodological foundations of the construct. The half-day workshop combines lightning talks, hands-on elicitation exercises, and structured discussions on key questions concerning the future of the mental model for human-AI interaction research.

---


### 174. [InfoTaxa: Information-Calibrated Label-Free Clustering for Fine-Grained Visual Taxonomy](https://arxiv.org/abs/2609.17218)

**<font color=#1a73e8>作者：</font>** David Ahmedt-Aristizabal, Mohammad Ali Armin, Lars Petersson  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Label-free clustering of frozen pretrained visual embeddings offers a scalable route to biodiversity monitoring, but image-only fine-grained taxonomy exhibits a consistent coarse-to-fine failure mode: clusters recover broad taxonomic structure yet plateau at species level. We study this behaviour on BIOSCAN-5M through an information-calibrated clustering analysis. BioCLIP~2 features with UMAP and HDBSCAN reach $0.79$ AMI at family and $0.67$ at genus, substantially improving over the prior image baseline and remaining competitive with oracle-$K$, graph-based, and learned clustering heads on the same frozen features. To diagnose whether the remaining plateau is method-limited or information-limited, we introduce InfoTaxa, which combines clustering efficiency---the fraction of probe-estimated image information recovered by an unsupervised partition---with paired DNA as an audit signal only, not an inference input. The density pipeline recovers approximately $0.90$ and $0.81$ of the image-available information at order and family, respectively. Held-out late-fusion probes show that adding DNA to the image embedding reduces species-level prediction error by approximately two bits. Robustness analyses cover multiple image encoders, described-species and rare-class subsets, probe diagnostics, and held-out-species coarse-rank generalisation and same-species retrieval. Thus, in the tested setting, species-level label-free clustering is both clustering-limited and representation-limited: improved clustering may recover additional image-exposed structure, but cannot close the DNA-audited information gap alone.

---


### 175. [Memorisation bias in medical AI](https://arxiv.org/abs/2609.17223)

**<font color=#1a73e8>作者：</font>** Moritz A. Knolle, Martin J. Menten, Laurin Lux 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Medical AI models hold immense potential to improve patient outcomes, but they are also known to unintentionally memorise individual records from their training datasets. While such memorisation has been linked to targeted privacy attacks, its consequences for clinical deployment, where patients may be assessed by a model that saw their historical data during training, remain poorly understood. Here we show that predictions on a patient's unseen future data can change significantly if a model observed that same patient's anonymised historical data during training, a phenomenon we term "memorisation bias". We demonstrate that this bias exists across diverse data modalities and model architectures, and over prolonged time spans: in some cases, memorisation bias persists on future records acquired decades after the historical records used for training. Moreover, in simulated prospective deployment, memorisation bias has asymmetric effects on the diagnostic accuracy of returning data contributors. When a patient returned with a de novo condition absent from their historical records in the training dataset, diagnostic sensitivity decreased significantly compared to an otherwise identical model not trained on their historical data. Conversely, when their health state was unchanged, both sensitivity and specificity were significantly inflated. Our findings reveal a previously uncharacterised risk in medical AI that arises when a model is deployed on patients who contributed to its training data. This exposes a shortcoming of current model development practice: the de-identification measures designed to protect patients' privacy make it difficult to identify returning contributors and exclude them from the AI-assisted interpretation of their own future data. Mitigating memorisation risks may thus require changes to current model training and deployment protocols.

---


### 176. [Psychological Effects of Cultural Upheavals from Millions of Song Lyrics Over 100 Years](https://arxiv.org/abs/2609.17225)

**<font color=#1a73e8>作者：</font>** David M. Markowitz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cultural upheavals impact many aspects of social life, and many studies have investigated their impact on language patterns. However, few investigations have isolated the impact of upheavals on individuals at scale in popular media. The current work evaluated millions of song lyrics spanning more than a century in search of within-artist and between-artist signals of distress from the Vietnam War, the terrorist attacks of 9/11, and COVID-19. Compared to a five-year baseline, rates of self-references - a marker of psychological distancing - were significantly reduced after the Vietnam War and September 11th. Cognitive processing terms were elevated post-upheaval vs. pre-upheaval, which indicated artists' increased attempts to make meaning from such massive disruptions. Content patterns corroborated these findings as artists wrote more about "life and freedom" (societal conditions) and less about "courtship and nightlife" (interpersonal connection) following the upheavals. Cultural upheavals modify individual and collective verbal behavior, demonstrating their far-reaching impact on society.

---


### 177. [FROD: Feature Matching Residual Denoising Oracle Bone Decipher](https://arxiv.org/abs/2609.17227)

**<font color=#1a73e8>作者：</font>** Yanbin Hou, Biao Xiong, Guojun Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Oracle bone script (OBS), one of the earliest Chinese writing systems, plays an important role in the study of Chinese etymology. Traditional decipherment relies heavily on domain experts who analyze characters through semantic context and structural evolution. To assist this labor-intensive process, we formulate OBS decipherment assistance as a cross-era image translation task and propose FROD (Feature Matching Residual Denoising Oracle Bone Decipher). Although many OBS characters differ substantially from their modern counterparts, they often preserve local topological invariants at the radical level. During training, FROD leverages fast feature matching to provide gated segmentation supervision: paired samples with sufficient matches are processed patch-wise to align fine-grained radicals, whereas low-similarity pairs are trained holistically to avoid mismatched artifacts. In addition, a Residual Denoising Diffusion Model (RDDM) jointly estimates noise and residual signals, thereby reducing the positional drift and stroke disorder commonly observed in standard diffusion models. Finally, a multi-stage font stylization refinement network refines the generated images by eliminating edge noise and stabilizing stroke structures. On our augmented character-disjoint dataset, FROD achieves higher Top-1 recognition accuracy than the evaluated baselines, with a 3.8% absolute gain over OBSD.

---


### 178. [DecoGS: Adaptive Static-Dynamic Decoupling of 3D Gaussians for Free-Viewpoint Video Streaming](https://arxiv.org/abs/2609.17230)

**<font color=#1a73e8>作者：</font>** Idil Sulo, Alexey Supikov, Ilke Demir 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming 3D reconstruction demands both speed and temporal fidelity, goals that existing methods undermine by updating every Gaussian every frame, even in static regions. We present DecoGS, a method for efficient online training of 3D Gaussians from streaming videos. Unlike prior methods that update the entire scene indiscriminately, DecoGS introduces an adaptive mechanism that selectively focuses optimization on spatiotemporal regions exhibiting motion or photometric changes. This targeted training strategy eliminates redundant updates that cause flickering and drift in nominally static regions, while enabling fast, high-fidelity scene updates. The pipeline further integrates region-aware Gaussian management through gradient gating and efficient visibility filtering to maintain temporal coherence and a compact memory footprint. On N3DV and MeetRoom, DecoGS achieves 34.55 and 31.60 dB PSNR respectively, outperforming all streaming and offline baselines, while rendering at 261 FPS with $70\times$ lower temporal flicker than the best prior method, requiring no large-scale pretraining.

---


### 179. [AraMIP: Extending MIPVU Towards Metaphor Identification in Arabic](https://arxiv.org/abs/2609.17235)

**<font color=#1a73e8>作者：</font>** Mandar Marathe, Manar Ali, Sara Nabhani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Metaphor research has gained increasing attention due to its relevance to linguistic creativity, language use, cognitive processes, and related areas. While many efforts have been devoted to metaphor identification and annotation in English and other languages, Arabic remains under-resourced in this area. In this work, we propose the Arabic Metaphor Identification Procedure (AraMIP), a novel guideline for Arabic metaphor annotation. AraMIP builds on the widely used Metaphor Identification Procedure Vrije Universiteit (MIPVU) framework, incorporating adaptations that accounts for the language-specific properties of Arabic. We distinguish three major types of Arabic figurative language: Isti'ara (metaphor), kinaya (metonymy/indirect expression), and tashbih (simile), and annotate a pilot dataset of 300 sentences (5277 words). Our analysis reveals key challenges specific to Arabic, including morphological complexity, inconsistencies in dictionary sense ordering, and the absence of standardized contextual materials for annotators. This work contributes a first step toward standardized Arabic figurative instances and facilitates the development of larger annotated resources, thereby supporting future research on figurative language in Arabic.

---


### 180. [SEMA-GUARD: Semantic and Graph-Based Vulnerability Detection in Assembly Code](https://arxiv.org/abs/2609.17254)

**<font color=#1a73e8>作者：</font>** Halil Dursunoglu, Kaan Sulkalar  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In cases where source code is not available, such as malware analysis, firmware analysis, and embedded systems analysis, vulnerability detection in compiled programs has gained importance. Current methods are heavily reliant on syntactical regularities or higher level representations that are vulnerable to changes in the compiler and may not be readily applicable to assembly this http URL this article, we present SEMA-GUARD, a framework that uses semantic analysis and graph neural networks to identify flaws in assembly code. The approach improves the representation of control flow graphs by adding information about the program's execution at a lower level of abstraction, including stack manipulations, memory accesses, and data flow. A set based on the Juliet Test Suite was used to evaluate the effectiveness of SEMA-GUARD. In this set, each piece of source code is initially translated into assembly language and then broken down into function-level chunks. The suggested method, which relies only on statistical or structural data, achieves an accuracy of 85.1\% and an F1 score of 0.801, according to the results. Such results imply that including semantic information in graph-based models may be a successful method for identifying vulnerabilities in compiled code.

---


### 181. [Exploring 2D backbone effects for indoor semantic occupancy prediction](https://arxiv.org/abs/2609.17257)

**<font color=#1a73e8>作者：</font>** Shizhang Fanga, Wanling Yea, Qi Zheng  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semantic occupancy prediction gives an embodied agent a voxel-level account of where space is free, occupied, and semantically meaningful. In RGB-D pipelines such as EmbodiedScan, the image encoder is often left as a default module, even though its features are the visual evidence later sampled into the 3D grid. We study this design choice directly. A central finding is that changing the 2D backbone improves occupancy accuracy more than several carefully designed occupancy architectures or modules. We keep the main RGB-D projection, depth branch, and occupancy head fixed, and replace only the image backbone. The compared encoders are CLIP-ResNet, CLIP-ViT, BLIP2, and DINOv2. Under the controlled setting, the measured mIoU changes substantially: DINOv2 obtains 30.55\%, BLIP2 obtains 29.49\%, CLIP-ViT obtains 24.33\%, and CLIP-ResNet obtains 17.41\%. The stronger encoders also exceed the original EmbodiedScan ResNet-50 baseline without modifying the downstream 3D fusion pipeline. Class-level results give a more detailed picture: DINOv2 is stronger on many layout and structural categories, whereas BLIP2 remains close on several object-centered classes. CLIP-ViT improves clearly over CLIP-ResNet, showing that the way CLIP features are exposed as dense tokens matters for voxel lifting. These results indicate that the image backbone is not a secondary engineering detail in embodied semantic occupancy, but a major source of variation in the final 3D prediction.

---


### 182. [Towards Illusions Awareness in Cyber-Physical System's Design](https://arxiv.org/abs/2609.17260)

**<font color=#1a73e8>作者：</font>** Anna Di Placido, Nicolas Ferry, Julien Deantoni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cyber-Physical Systems (CPS) operate through a continuous sense-compute-act loop within an open context environment, making it impossible to anticipate all the situations the system will face. To cope with this openness, stakeholders rely on assumptions, formalized into design models. However, these assumptions may no longer hold once the system is confronted with runtime reality, resulting in a discrepancy between expected and observed behaviour known in literature as the reality gap. Existing approaches mainly focus on reducing or overcoming it by making simulations more faithful to reality, with no unified methodology to structure and exploit invalidated assumptions that give rise to this gap as reusable design knowledge. We refer to the persistent reliance on invalidated assumptions -and the resulting false confidence in the design model's operational validity -as design illusions, and argue that they need to be made explicit, structured, and exploited as knowledge to support better design decisions. We propose a conceptual pipeline for illusions-awareness that identifies, classifies, characterizes, and leverages illusions to transform them into actionable design knowledge.

---


### 183. [Calibrate Once, Fly Any Team: Residual-Grounded Low-Fidelity Training for Cooperative Drone Swarms](https://arxiv.org/abs/2609.17265)

**<font color=#1a73e8>作者：</font>** Maxim Mednikov, Oren Gal  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Training multi-agent drone-swarm policies directly in high-fidelity (HF) rigid-body physics is accurate but computationally expensive. This cost scales poorly with team size, as each additional agent multiplies contact-resolution complexity and sharply raises the in-simulation crash rate. To address this, we propose a mixed-fidelity training scheme that eliminates HF reinforcement learning entirely.
A single shared, decentralized policy is optimized inside a fully-differentiable, JAX-native low-fidelity (LF) point-mass simulator. The simulator is corrected by a small, per-agent bagged residual ensemble fit once, offline, using short calibration flights in the HF simulator. Because calibration requires only one isolated drone, the data collection budget does not compound with team size. Reference trajectories are generated by rolling out an existing LF-only policy and tracked in the HF simulator by a zero-training PD controller.
Evaluated across four cooperative drone tasks and team sizes from 3 to 18, the residual-corrected policy outperforms an uncorrected LF baseline in all combinations, and a from-scratch HF policy in 22 of 24 combinations tested. It trails an HF-finetuned policy by a margin that narrows steadily with team size. Ultimately, the proposed method achieves near-equivalent performance at the largest team sizes at a fraction of the computational cost, completely avoiding the high crash rates typical of HF training.

---


### 184. ["Piecing Data Connections Together Like a Puzzle": Effects of Increasing Task Complexity on the Effectiveness of Data Storytelling Enhanced Visualisations](https://arxiv.org/abs/2609.17278)

**<font color=#1a73e8>作者：</font>** Mikaela Elizabeth Milesi, Paola Mejia-Domenzain, Laura Brandl 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The emerging concept of data storytelling (DS) suggests that enhancing visualisations with annotations and narratives can make complex data more insightful than conventional visualisations. Previous works found that DS-enhanced visualisations are more effective than conventional visualisations for simple tasks like identifying key data points or the main message. However, no previous work has explored the extent to which DS enhancements influence task completion across different levels of cognitive complexity. We address this gap by presenting the results of a study where 128 participants completed tasks based on four visualisations (two line charts and two choropleth maps, either with or without DS elements) spanning a range of complexity based on Bloom's taxonomy, which has been applied in data visualisation to categorise tasks hierarchically from lower to higher-order thinking. Results suggest that while DS-enhanced visualisations effectively support lower-order tasks (finding data points and understanding insights), they don't necessarily aid the correct completion of higher-order tasks (application, analysis, evaluation and creation). However, DS enhancements improve how efficiently participants complete complex tasks.

---


### 185. [GAUGE: A Formal Framework for Measuring Cryptographic Security under Heterogeneous Adversary Cost Models](https://arxiv.org/abs/2609.17281)

**<font color=#1a73e8>作者：</font>** Bhanwar Gupta, Sanjeev Rana  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Standards bodies report cryptographic security as a single number of bits, but this value depends on the adversary cost model used to price time, memory, and quantum resources. Different conventions can therefore produce different rankings of cryptographic schemes. GAUGE represents security as a function over admissible cost models, called a security profile. Comparisons then become comparisons between profiles, and ranking reversals become an explicit structural property rather than a measurement error.
We formalize price functionals over a cone of adversary cost models, show that security profiles are piecewise-linear and concave, and prove a rating trilemma: when two profiles cross, no rating can simultaneously be faithful to underlying costs, total over comparable pairs, and independent of the chosen cost model. We provide a polynomial-time linear-programming procedure that certifies whether the ranking of two schemes is robust, reverses under admissible models, or is genuinely incomparable.
We extend GAUGE with a two-layer risk measure combining stochastic cryptanalytic decay with uncertainty over the appropriate cost model. We evaluate the framework on NIST post-quantum standards, classical anchors, and a 25-year chronology of cryptanalytic breaks. The analysis certifies a ranking reversal for ML-KEM-512 versus AES-128 from a 4-5% shift in memory pricing, and measures a lattice-sieving cost drift of 9.79 bits per year over eight years. A hybrid X25519 + ML-KEM-768 handshake reduces combined-break probability twenty-fold at a 2.3 kilobyte cost. The artifact reproduces all tables and figures in under seven seconds. GAUGE provides an explicit and auditable framework for reporting cryptographic security under competing cost models.

---


### 186. [Personalized Federated Learning through Global Knowledge Distillation and Local Head Adaptation](https://arxiv.org/abs/2609.17284)

**<font color=#1a73e8>作者：</font>** Polycarpo Souza Neto, José Mairton Barros da Silva Júnior, Charles Casimiro Cavalcante  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Statistical heterogeneity limits federated learning when a single global classifier cannot represent client-specific label distributions. In this work, we propose Personalized Federated Knowledge Distillation with Head Adaptation (pFedKDH), which aggregates only the shared backbone, keeps persistent client-specific heads, and uses a recalibrated global head as a teacher during local training. Across MNIST, Fashion-MNIST, CIFAR10, and CIFAR100 under class-wise Dirichlet partitions, pFedKDH obtains the best accuracy in most settings, with accuracy gaps up to 37.67\% over the weakest baseline and consistently low standard deviation across repetitions. Component-wise diagnostics and convergence results support the role of persistent heads and distillation-guided local optimization under label-skewed data.

---


### 187. [Same Flow, Different Paths: Variance Reduction in Flow Matching](https://arxiv.org/abs/2609.17287)

**<font color=#1a73e8>作者：</font>** Alexander Tyurin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In flow matching (FM), a velocity model $v_{\theta}$ is trained using a predefined path $g_t$ that connects data and noise samples (e.g., $g_t(x_0, x_1) = (1 - t) x_0 + t x_1$). In this work, we study the choice of this path from an optimization perspective by analyzing the variance of stochastic gradients. We consider the class $G(p_t,v^\star_t)$ of paths that induce the same marginal distributions $p_t$ and marginal velocity field $v^\star_t$, and therefore the same FM objective. Our main finding is that the choice of path $g_t$ can fundamentally change the convergence rate of SGD, even when the FM objective remains exactly the same. (i) For a linear velocity model and one-dimensional Gaussian data, we derive a tight bound on the SGD iteration complexity up to logarithmic factors and find an analytically optimal path that minimizes this bound among linear paths inducing the same FM problem. (ii) We then extend the variance analysis to general FM problems and formulate path selection at a fixed $\theta$ as the variance-minimization problem PathOpt$_\theta$, constrained to $g_t\in G(p_t,v^\star_t)$. We show that this constraint is essential: reducing variance without it can lead to slower convergence. (iii) Since the constraint $g_t \in G(p_t,v^\star_t)$ cannot generally be verified directly, we derive an equivalent formulation with constraints that can be estimated from samples, allowing paths to be found numerically. Our theoretical results are supported by experiments with Gaussian data, Gaussian mixture models, and real datasets.

---


### 188. [Optical-Flow Wingbeat Counting in MuJoCo: A Comparison of Convolutional, Spiking, and Attention-Based Temporal Models](https://arxiv.org/abs/2609.17308)

**<font color=#1a73e8>作者：</font>** Zhang Nengbo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual monitoring of flapping-wing vehicles requires distinguishing individual wingbeats from motion strength and average frequency. This paper presents a controlled MuJoCo evaluation of wingbeat counting from signed optical flow observed by virtual cameras mounted on Crazyflie vehicles. Three flapping-wing models were recorded at optical distances of 1.5 and 3.0 m, producing 1,440 clips from 240 paired scene configurations with a scene-level 3:1 training-test split. A common spatial convolutional encoder was combined with a causal temporal convolutional network, a recurrent leaky integrate-and-fire spiking network, or causal self-attention. Each model predicted phase and activity, followed by the same directed-crossing event counter. The six existing convolutional models were retained, and all twelve new models were frozen before their test predictions were generated. Exact-count accuracies at 1.5 m were 96.67%, 95.00%, and 96.67%, respectively; at 3.0 m they were 94.44%, 92.22%, and 95.00%. All paired scene-bootstrap intervals for differences in exact-count accuracy included zero. Seven far-distance spiking-model clips had correct totals despite event-timing mismatches, demonstrating why total-count and event-level measurements must be reported together. The results support the feasibility of causal optical-flow counting in the tested setting and identify boundary-sensitive errors. They do not establish an architecture ranking across repeated training, real-flight robustness, or hardware efficiency.

---


### 189. [Can We Stop The Ads? Taxonomy and Characterization of Smartphone Splash Ads and Existing Countermeasures](https://arxiv.org/abs/2609.17316)

**<font color=#1a73e8>作者：</font>** Shuhao Zhang, Xinyu Liu, Ziyu Shao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Splash ads are full-screen advertisements that pop up and appear as the first interaction page when users start an app, often tricking users into unknowingly activating certain trigger mechanisms, such as moving the phone to redirect users to other profit-driven third parties. So far, splash ads have already caused significant real-world impacts, ranging from significantly delaying emergency response to distracting drivers, as well as degrading accessibility of apps to vision-impaired users. We analyze 108 documented implementations of advertising defenses to examine their applicability to splash ads and the requirements users face when deploying them.
Our analysis identifies substantial deployment barriers, including device rooting or jailbreaking, runtime code injection, and application modification. Options without these requirements can still involve additional permissions, rule maintenance, source compilation, or payment. In our evaluation of 13 configurations of 11 tools across 10 popular apps, only one tool prevented the target ad-triggered navigation across all ten apps. It required Accessibility permission, and ads remained visible for approximately one second before dismissal. Other tested configurations failed to prevent navigation or, in some cases, left host apps unable to launch or stuck on the ad page. We further analyze the outstanding challenges and pos- sible future directions, highlighting the urgent need to incentivize smartphone manufacturers to provide more friendly and regulated platforms.

---


### 190. [Intrinsic Motivation in Reinforcement Learning: A Research Agenda for Adaptive Self-Organisation](https://arxiv.org/abs/2609.17325)

**<font color=#1a73e8>作者：</font>** Anatoly Belikov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biological cells can be viewed as individual, interacting agents whose collective dynamics give rise to adaptive behaviour at multiple levels of organisation, from individual cells through tissues to whole multicellular organisms. In this perspective and tutorial article we discuss whether intrinsic rewards in artificial neural systems can support adaptation, functional specialisation and higher-level self-organisation without a shared external objective. We review empowerment, curiosity, learning progress, information gain, unsupervised skill discovery, mutual information estimation and the use of world models for intrinsic reward computation. Particular attention is given to failure modes showing when such objectives do not produce sustained exploration or increasingly complex behaviour. We argue that more capable systems may require complementary objectives, communication, memory, learning at multiple temporal scales and environmental constraints. Based on this perspective, we outline three experimental directions. These include a resource-constrained environment in which otherwise stable behavioural attractors become unsustainable, allowing us to test whether environmental constraints can mitigate characteristic failure modes of intrinsic objectives. The network of recurrent agents with per-agent intrinsic rewards, and a hierarchical world-model agent in which exploratory motor competence develops before goal-directed behaviour. These experiments are intended to test whether intrinsic learning can lead to adaptive organisation at progressively higher levels.

---


### 191. [RobResilience: Implementing and Evaluating a Resilience Framework for Cyber-Physical Embodied Systems](https://arxiv.org/abs/2609.17349)

**<font color=#1a73e8>作者：</font>** Gysella Imrell, Emanuele Miotto, Mahya Mohammadi Kashani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In embodied cyber-physical systems, active cyberattacks pose an immediate threat not just to data, but to physical integrity and human safety. While existing security approaches excel at detection, they lack the runtime mechanisms to determine whether a disruption is tolerable or if performance degradation remains within safe operational bounds. This gap leaves autonomous systems vulnerable to graceful failure paralysis, where they cannot distinguish between a safe, degraded state and a catastrophic hazard during an ongoing attack. This paper presents RobResilience, an implementation of a formal resilience framework for embodied cyber-physical systems in a Webots simulation environment, using a PR2 robot and ROS2. The framework evaluates three predicates at runtime: tolerable disruption ($\delta$), tolerable degradation ($\gamma$), and mitigation feasibility ($\mu$), over a compromised device set derived from IDS confidence scores. When resilience is lost, the framework triggers available mitigation strategies. We evaluate our implementation through eight attack scenarios that systematically cover all possible combinations of the predicate state space, varying attack targets, degradation rates, and mitigation availability. Results confirm that the runtime behaviour of the implementation is consistent with the theoretical definitions.

---


### 192. [Hybrid Variational Quantum Circuits for Multivariate Regression and High-Dimensional Data Reconstruction](https://arxiv.org/abs/2609.17358)

**<font color=#1a73e8>作者：</font>** Koffi Ognandon Ayena, Frédéric Holweck, Serge Iovleff 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational quantum circuits (VQCs) are parameterized quantum circuits optimized classically. We propose a hybrid variational quantum circuit (HVQC) extending VQCs with a classical affine post-measurement layer, enabling vector-valued regression without the linear overhead of independent scalar circuits. Theoretically, we show that elementary one-and two-qubit circuits can approximate quadratic functions and products via data re-uploading and entanglement, providing the foundations of the full architecture. Experimentally, on two synthetic image reconstruction datasets and the Friedman1 benchmark (40,568 test samples), our HVQC matches Gaussian Process Regression and outperforms XGBoost and Random Forest. An ablation study confirms that both quantum and classical components are essential, and results highlight the central role of the feature map in hybrid quantum-classical models.

---


### 193. [ECHO: A Matched-Contrast Benchmark for Context-Sensitive Turn-Taking in Full-Duplex Dialogue](https://arxiv.org/abs/2609.17360)

**<font color=#1a73e8>作者：</font>** Shuofeng Zhao, Hongwei Cai, Wenke Fan 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Full-duplex spoken dialogue systems must distinguish interruptions that require yielding the floor from backchannels that permit continued speaking. Existing benchmarks typically evaluate events independently and may therefore reward fixed action preferences rather than context-sensitive decisions. We introduce ECHO, a paired diagnostic benchmark for Chinese full-duplex turn-taking. ECHO pairs examples with the same overlap transcript but contrasting preceding multi-turn dialogue contexts, with one requiring Yield and the other Keep. It additionally includes off-talk examples for diagnosing unnecessary yielding. We introduce pair accuracy, which requires correct decisions on both members of a pair and assigns no credit to constant-action policies. Experiments on multiple full-duplex systems show that most exhibit a pronounced bias toward \textsc{Yield}, performing substantially better on interruptions than on backchannels, while another system remains comparatively balanced. These findings demonstrate that interruption-only evaluation can overestimate practical turn-taking reliability. ECHO and its metadata will be publicly released.

---


### 194. [Lexplorer: Navigating the Complexity of Legal Document Landscapes](https://arxiv.org/abs/2609.17366)

**<font color=#1a73e8>作者：</font>** Daniel Fürst, Titus Pünder, Maximilian T. Fischer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As technological and social innovations create novel regulatory challenges, legal systems grow in complexity - increasing the need for interfaces that enable effective interactions with legal document collections. Through interviews with legal scholars (n=15), we find that supporting legal work requires going beyond retrieval-centered legal-information-system paradigms. Hence, we propose Lexplorer, a flexible interface for exploring, navigating, and analyzing legal documents, based on a taxonomy capturing user intents. Distinguishing text and data views for one, few, and many documents, Lexplorer enables context-sensitive interactions with evolving collections of interconnected legal texts, facilitating Adaptive Meaning Construction in law. We evaluate Lexplorer with legal scholars (n=20) in the context of European Union law, validating our elicited requirements, intent taxonomy, and prototype design. Resulting from a close collaboration between visual-analytics researchers and legal scholars, our work also provides nuanced insights into the process required to design interactive systems for expert domains driven by implicit methodological knowledge.

---


### 195. [Bridging the Confidence Gap: Temperature Scaling for Calibrating Test-Time Prompt Tuning](https://arxiv.org/abs/2609.17386)

**<font color=#1a73e8>作者：</font>** Yuwei Liang, Jian Liang, Dapeng Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time prompt tuning (TPT) enables adaptation on a single test instance, achieving improved accuracy but often sacrificing calibration performance. Most existing calibration methods introduce additional regularization terms to promote dispersion across text embeddings and reduce calibration error, yet these methods often suffer from a drop in accuracy. Motivated by the well-calibrated nature of zero-shot predictions, we propose CoTS, a simple yet effective post-hoc calibration method that preserves accuracy. Specifically, CoTS applies temperature scaling to minimize the confidence gap between adapted and zero-shot predictions. To fully exploit the potential of multiple augmentations during adaptation, we introduce a weak-strong ensemble strategy that further boosts accuracy. We then apply CoTS to this ensemble, termed E-CoTS, to maintain its well-calibrated property. Extensive experiments on diverse datasets and backbones show that our approaches effectively mitigate miscalibration without compromising primary accuracy. For instance, E-CoTS reduces the average expected calibration error of TPT from 11.90% to 5.38% on ImageNet variants, while even increasing accuracy from 60.74% to 62.95%. Moreover, when integrated with existing calibration methods, E-CoTS usually enhances both accuracy and calibration simultaneously.

---


### 196. [PanoGS-SLAM: Panoramic 3D Gaussian Splatting SLAM](https://arxiv.org/abs/2609.17387)

**<font color=#1a73e8>作者：</font>** Yongqi Mao, Hao Shi, Yufan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time dense SLAM is a core capability for robotics applications that require robust localization and high- quality mapping in dynamic or fast-changing environments. Recent 3D Gaussian Splatting (3DGS)-based SLAM methods have shown promising performance, but most are designed for narrow-FoV pinhole cameras, where limited angular coverage weakens pose observability and often leads to unstable photo- metric optimization under rapid motion and large viewpoint changes. We present PanoGS-SLAM, the first panoramic dense SLAM system built on 3D Gaussian Splatting. Our method per- forms differentiable rendering and pose optimization directly in the spherical domain, enabling omnidirectional photometric constraints for more stable tracking. To improve geometric consistency and robustness, we introduce (1) a sphere-consistent photometric loss that compensates for the area distortion of equirectangular projection, and (2) a depth-guided Gaussian initialization strategy that stabilizes incremental mapping in newly observed regions. Extensive experiments on both real and synthetic panoramic benchmarks (PALVIO and SynPano) show that PanoGS-SLAM consistently outperforms geometric and GS-based baselines in tracking accuracy and rendering quality, while achieving fast front-end convergence and real-time perfor- mance. In addition, controlled field-of-view experiments reveal a clear monotonic improvement in optimization conditioning and convergence stability as angular coverage increases, high- lighting the fundamental role of sensing geometry in shaping the optimization landscape of differentiable Gaussian-based SLAM. The source code will be made publicly available.

---


### 197. [FlashVector: Agent for Hierarchical Model Serving Stack Optimization](https://arxiv.org/abs/2609.17391)

**<font color=#1a73e8>作者：</font>** Qi Wu, Lohan Lemire, Kai Meng 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model serving is one of the largest cost drivers in production recommender systems. Maximizing its throughput requires navigating a deeply layered hierarchy: GPU kernels, the ML framework computation graph, the model server, and on-demand feature processing -- each demanding specialized domain expertise. Such cross-layer expertise is inherently difficult to acquire, and does not scale with a workload that continuously grows and evolves, leaving significant cost efficiency gains unrealized. While recent AI agents have demonstrated human expert level efficiency in standalone GPU kernel optimization, automated tuning and optimization for the rest of the serving stack remain largely unexplored. We present FlashVector, an agentic system that optimizes performance across all layers of the model serving stack. The key contribution is an extensible framework to generalize the single kernel optimization agent paradigm to heterogeneous technical stacks, and to deliver performance improvements holistically. After deployment in Unity's Vector advertising platform, FlashVector achieved up to 2x throughput increase and up to 1.98x latency speedup on model server, and up to 1.6x throughput increase on feature store. These optimizations were discovered not only at the GPU kernel and computation graph levels, but also across the other components of the model serving stack, such as the model server (NVIDIA Triton's C++ codebase) and the on-demand feature transformation service (Python codebase), demonstrating the extensibility of the framework to more complex system architectures.

---


### 198. [Closing the Loop: Bidirectional Fully Encrypted Protocols](https://arxiv.org/abs/2609.17397)

**<font color=#1a73e8>作者：</font>** Baigang Chen, Nicholas Hopper  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully encrypted protocols (FEPs) provide encrypted channels that make all protocol-generated bytes computationally indistinguishable from uniform random strings. Several previous works have explored security definitions and constructions of unidirectional FEPs: protocols in which one party acts only as a sender, and the other acts only as a receiver. However, most applications require two-way information exchange, and a network adversary can observe communication in both directions and their shared lifetime. Because the semantics of bidirectional channels involve more complex shared state, it is possible that the ``naïve'' composition of two unidirectional channels can result in a two-way protocol that can be detected based on dependencies between the two directions, such as traffic imbalance, channel closure, failures, or connection tear-down.
To address this issue, we introduce new formal security definitions for bidirectional FEPs that capture exact shaping, delivery, protocol-state integrity, private half-close, and cross-direction isolation, while revealing a public ``sending schedule'' and ``closing epoch'' that may be randomized. We show that the trivial composition fails to meet these definitions, leading to practical detection attacks. We then construct provably secure bidirectional FEPs (BiFEPs) for both the datastream and datagram settings. For datastream, we combine two direction-separated FEPs with a ``wrapper'' layer that prevents detection based on the mismatch between uni- and bi-directional connection states. For datagram, we add encrypted DATA/FIN/ACK with replay protection and loss-tolerant close. We validate the design through a Rust implementation and show that none of the surveyed deployed protocols provides the full set of BiFEP security properties.

---


### 199. [SCHERI: Provably Secure Speculation Under the Constant-Time Policy for CHERI (Extended Version)](https://arxiv.org/abs/2609.17399)

**<font color=#1a73e8>作者：</font>** Shixin Song, Davide Davoli, Elias Storme 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Capability-based architectures such as CHERI provide strong support for the architectural isolation of software components. To additionally protect against microarchitectural leakage, software can be written in a constant-time fashion. Modern processors, however, rely heavily on speculative execution, which can invalidate the constant-time guarantees and leak isolated secrets transiently.
In this work, we show that providing secure speculation for CHERI is non-trivial, and that existing proposals fail to preserve the confidentiality guarantees. We develop a formal framework for reasoning jointly about capability safety, speculative execution, and information-flow security, and use it to demonstrate potential leaks. We then present SCHERI, a new processor design within this framework, and formally prove that it provides end-to-end secure speculation guarantees for the constant-time policy.
Our results provide formal foundations and practical guidance for building future capability-based processors, which are resilient to Spectre attacks for constant-time programs.

---


### 200. [SSC-Priors: Exploring Semantic and Visibility Priors to Boost Lidar Semantic Scene Completion](https://arxiv.org/abs/2609.17413)

**<font color=#1a73e8>作者：</font>** Tetiana Martyniuk, Jonathan Seele, Alexandre Boulch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper investigates easy strategies to boost the performance of existing networks for lidar semantic scene completion (SSC) without requiring complex architectural redesigns. The fact is that, over the last years, SSC methods have mostly pursued architectural innovations, making the models heavier and more complex, e.g., by jointly training a point cloud semantic segmentation branch. In this work, we take a step back and explore two priors used as simple ingredients (possibly noisy) to improve existing approaches: semantic pseudo-labels and sensor visibility information. Concretely, we provide both kinds of information directly as additional inputs to a given SSC network, requiring only a minimal adaptation of the original architecture. We first demonstrate that endowing input point clouds with semantic pseudo-labels from off-the-shelf segmenters significantly improves the performance of existing SSC models. In fact, by evaluating these models against an oracle, we establish that high-quality semantic priors are a primary driver of semantic gains (mIoU), and that the SSC model can be trained just once with ground-truth semantics and then exploited without retraining using any segmenter. Furthermore, we equip the input lidar point cloud with visibility information that distinguishes between empty spaces (between the lidar and a scanned point) and unknown spaces (outside of lines of sight), providing a secondary performance boost across the tested architectures. We study the design space of data for representing visibility information and bound the remaining headroom with a ground-truth oracle on the free-space labels. On SemanticKITTI, these enhancements make older models competitive with state-of-the-art systems across four architectures, in one case even outperforming them. On the SSCBench-nuScenes benchmark, both priors also transfer with the sparser 32-beam sensor.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-219](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
