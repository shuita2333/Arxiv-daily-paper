# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**401-450**（第 9/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 401. [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637)

**<font color=#1a73e8>作者：</font>** Pin Tang, Guoqing Wang, Xiangxuan Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios. Existing VLAs typically predict and optimize 3D trajectories from 2D images. While intuitive, this 2D-to-3D prediction is inherently entangled with camera parameters, leading to limited data scalability across heterogeneous driving datasets. Moreover, directly optimizing in 3D space induces severe convergence to trivial solutions, where VLAs rely on ego-status rather than visual scene understanding. To address these issues, we propose PixelPilot, a novel VLA featuring a decoupled planning and lifting paradigm. In the planning phase, PixelPilot reformulates scene understanding and trajectory prediction as sensor-agnostic 2D-to-2D tasks in the image plane, thereby facilitating scalable training across diverse datasets. The planned 2D trajectories are then deterministically lifted to 3D only during inference, ensuring the full exploitation of visual cues and generalization across different vehicles. To realize this paradigm, we propose a knowledge-instilled policy learning strategy that applies dense, intermediate rewards via Group Relative Policy Optimization (GRPO) to enforce a rigorous causal chain from visual perception to spatial planning. Extensive experiments demonstrate that PixelPilot achieves state-of-the-art performance in both open-loop and closed-loop settings, validating its superior scalability and visual reasoning capabilities.

---


### 402. [Learning Structured Visual Compositional Representations for Weakly Supervised Referring Expression Comprehension](https://arxiv.org/abs/2607.04638)

**<font color=#1a73e8>作者：</font>** Lian Xu, Mohammed Bennamoun, Farid Boussaid 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Referring expression comprehension (REC) aims to localize the object in an image described by natural language. In Weakly supervised REC (WREC), existing approaches primarily operate on anchor-level visual representations. Even when enriched with auxiliary cues, relational interactions remain implicitly encoded within individual anchor features. The resulting visual representation remains flat and unary-only, limiting its ability to align with the structured nature of language. In this work, we propose a Structured Visual Compositional Representation (SVCR) learning framework for WREC. Rather than implicitly encoding relations within unary anchors, the proposed SVCR explicitly models both unary object embeddings and pairwise relational embeddings, forming a structured visual representation space. We further introduce a compositional alignment mechanism that matches unary and pairwise visual representations with their corresponding textual embeddings in a unified manner, enabling compositional visual-textual matching under weak supervision. Extensive experiments on RefCOCO, RefCOCO+, and RefCOCOg show that the proposed SVCR achieves state-of-the-art performance. These results demonstrate the effectiveness of explicit structured visual representations and visual-textual alignment for WREC.

---


### 403. [Learning Flexible Generalization in Video Quality Assessment by Bringing Device and Viewing Condition Distributions](https://arxiv.org/abs/2607.04643)

**<font color=#1a73e8>作者：</font>** Nikolay Safonov, Dmitriy S. Vatolin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video quality assessment (VQA) plays a critical role in optimizing video delivery systems. While numerous objective metrics have been proposed to approximate human perception, the perceived quality strongly depends on viewing conditions and display characteristics. Factors such as ambient lighting, display brightness, and resolution significantly influence the visibility of distortions. In this work, we address the question of the multi-screen quality assessment on mobile devices, as this area still tends to be under-covered. We introduce a first large-scale subjective dataset collected across more than different 300 Android devices, accompanied by metadata on viewing conditions and display properties. We propose a strategy for aggregated score extraction and adaptation of VQA models to device-specific quality estimation. Our results demonstrate that incorporating device and context information enables more accurate and flexible quality prediction, offering new opportunities for fine-grained optimization in streaming services. Ultimately, this work advances the development of perceptual quality models that bridge the gap between laboratory evaluations and the diverse conditions of real-world media consumption. We made the dataset and the code available at this https URL.

---


### 404. [Machine Learning for Depression Screening and Intervention: an Original Circadian Rhythm Score-based Methodology](https://arxiv.org/abs/2607.04648)

**<font color=#1a73e8>作者：</font>** Bin Wang, Shuo Lian, Yuanyuan Hou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Depression screening from large-scale behavioral data is challenged by fragmented circadian indicators, limited interpretability, and the lack of intervention-oriented analysis. Existing approaches typically analyze sleep, activity, and social behaviors in isolation, failing to capture their joint circadian structure. To address this limitation, we first propose the Circadian Rhythm Score (CRS), a composite index that compresses multi-domain daily behaviors into a unified representation of circadian rhythm. CRS is constructed to maximize discriminative power for depression screening while preserving behavioral semantics through non-negativity constraints. Empirical results demonstrate near-lossless compression, where a single CRS retains almost the full predictive capability compared with multiple raw behavioral indicators. Building upon CRS, we develop an interpretable depression screening framework based on gradient-boosted trees and SHAP analysis, revealing nonlinear and saturation-like associations between circadian rhythm and depression risk. Beyond risk prediction, we further integrate interaction modeling and counterfactual regression to estimate heterogeneous and dose-dependent behavioral effects, enabling intervention-oriented reasoning under different circadian contexts. Experiments on the China Health and Retirement Longitudinal Study (CHARLS, n=15,233), demonstrate robust screening performance (ROC-AUC=0.825) and identify actionable behavioral thresholds, including a minimum effective exercise dose of approximately 300 MET-min/week and an optimal restorative nap duration of approximately 65 minutes for sleep-deprived individuals. By bridging supervised representation learning and interpretable modeling, this work provides a scalable framework for depression screening and intervention-aware healthcare data mining.

---


### 405. [Enhancing Video Physical Consistency via Role-aware Joint Training and Modality-decoupled Denoising](https://arxiv.org/abs/2607.04653)

**<font color=#1a73e8>作者：</font>** Guangting Zheng, Haojing Chen, Hao Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While modern video diffusion models excel in visual fidelity, maintaining long-range physical consistency remains a formidable challenge. Conventional pixel-reconstruction objectives mainly focus on appearance details and often fail to capture the underlying dynamics of a scene. To mitigate this, recent efforts have integrated auxiliary modalities (e.g., optical flow) to introduce physics priors via joint training with video appearance. However, these methods have three main limitations: (1) they do not distinguish the different motion patterns of different entity types; (2) joint modeling of visual and auxiliary modalities can cause capacity conflicts and weaken the pretrained visual prior; and (3) auxiliary modalities may accumulate errors during inference. To address these issues, we propose \textbf{VPT}, a fine-tuning framework for improving physical consistency in video diffusion models. VPT introduces a role-aware signal that groups entities into agents, controlled objects, passive objects, and background, so that different physical roles can be modeled more clearly. We further propose a modality-decoupled denoising strategy, where the visual and auxiliary channels are assigned independent noise levels. Together with a loss-weight decay strategy, this design makes auxiliary modalities serve as soft constraints rather than strong dependencies, mitigating recursive prediction errors during inference. We also introduce cross-step auto-guidance to further strengthen physical dynamics. Experiments show that VPT improves physical consistency while preserving visual quality, achieving relative gains of 39.4\% in SA and 17.9\% in PC on VideoPhy benchmark over Wan2.1-T2V-1.3B, and consistent improvements on VideoPhy-2 benchmark. The project page is available at this https URL.

---


### 406. [FormalRx: Rectify and eXamine Semantic Failures in Autoformalization](https://arxiv.org/abs/2607.04655)

**<font color=#1a73e8>作者：</font>** Haocheng Wang, Baiyu Huang, Yingjia Wan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The veracious semantic alignment in autoformalization is significant for formal mathematical reasoning. However, existing evaluations provide only opaque binary verdicts or scalar scores, offering no interpretable insight into where or why translations fail. This opacity severely limits both human understanding and automated system improvement. To bridge this gap, we introduce FormalRx, a comprehensive diagnostic evaluation framework that transforms autoformalization assessment from black-box judgments into actionable feedback. At its core is SCI Error Taxonomy, a hierarchical classification scheme decomposing autoformalization errors into 28 distinct categories with strict priority ordering. Building on this taxonomy, FormalRx provides four critical diagnostic capabilities: alignment verdicts, error categorization, error localization, and correction. We instantiate the framework with a diagnostic model FormalRx-8B, trained on 56,287 NL-FL pairs with fine-grained diagnostic annotations, and release FormalRx-Test as the first fine-grained diagnostic benchmark. FormalRx-8B achieves F1-scores of 0.88 (verdict) and 0.71 (categorization), along with accuracies of 0.75 (localization) and 0.73 (correction), substantially outperforming both general-purpose LLMs and specialized baselines. By connecting evaluation with actionable insights, FormalRx enables systematic diagnosis and improvement of autoformalization systems.

---


### 407. [Targeted Structure Completion for Sparse-View 3D Reconstruction in Autonomous Driving](https://arxiv.org/abs/2607.04661)

**<font color=#1a73e8>作者：</font>** Guoqing Wang, Pin Tang, Xiangxuan Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstructing 3D scene structures from sparse, low-overlap observations remains a fundamental challenge in autonomous driving. Recent state-of-the-art frameworks achieve promising results by incorporating voxel-based Gaussians, but incur substantial computational redundancy due to a uniform volumetric processing strategy. To bridge the gap between the efficiency of pixel-based Gaussian methods and the structural completeness of voxel-based Gaussian approaches, we propose FocusGS, a simple yet effective framework that shifts the paradigm from global densification to targeted structural completion. Our central insight is that structural completion should be decoupled from deterministic regions, with computation concentrated exclusively on areas exhibiting geometric ambiguity. Specifically, FocusGS addresses the localization challenge by deriving a 3D Geometric Ambiguity Manifold to accurately isolate localized areas prone to occlusion and high geometric uncertainty. To overcome the subsequent manifold completion challenge, we design a lightweight targeted structure completion module that selectively instantiates and optimizes continuous Gaussian queries strictly within this unstructured, sparse topological subspace. Extensive experiments demonstrate that FocusGS achieves a superior efficiency-quality trade-off, advancing state-of-the-art performance on driving-centric benchmarks while naturally reducing the total number of Gaussians by ~74% and decreasing rendering time by ~34%.

---


### 408. [Who Responds When the Driver Is Gone? A Framework for Human Intent Understanding](https://arxiv.org/abs/2607.04670)

**<font color=#1a73e8>作者：</font>** Xuewen Luo, Ding Fan, Ruiqi Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As autonomous vehicles progress toward fully driverless mobility, a critical question emerges: who understands and responds to passengers when the human driver is absent? Existing autonomous driving systems primarily optimize predefined navigation and control objectives from external scene observations, but they remain limited in perceiving and reasoning about in-cabin human intent. In this paper, we propose Intent2Drive, a unified framework for holistic human intent understanding and human-aligned planning. Instead of treating passenger intent as explicit commands alone, Intent2Drive models intent as a latent cognitive state shaped by language, personal attributes, emotional and physical conditions, behavioral signals, and situational context. To support this formulation, we construct a Holistic Intent Dataset (HID) that provides structured supervision over both explicit and implicit intent cues. Built upon HID, our Theory-of-Mind-inspired Human Intent Reasoner (HIR) infers a Latent Human State (LHS) and further translates it into a planner-compatible Human Intent Objective (HIO). We then introduce a Hierarchical Intent-Conditioned Planner (HICP) that incorporates HIO into route-level and trajectory-level planning, enabling driving behaviors to remain aligned with passenger needs across different planning horizons. Extensive experiments show that Intent2Drive improves structured human intent inference and HIO construction while preserving competitive closed-loop planning performance. These results demonstrate a promising step toward passenger-responsive autonomous driving systems that can reason about, interpret, and act upon human intent in driverless mobility.

---


### 409. [GlaKG: A Biomarker-Centric Fundus Knowledge Graph for Explainable Glaucoma Diagnosis and Risk Assessment](https://arxiv.org/abs/2607.04673)

**<font color=#1a73e8>作者：</font>** Cheng Huang, Jia Zhang, Yi Jiang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Glaucoma is a leading cause of irreversible blindness worldwide, yet most automated diagnosis systems rely on opaque deep-learning models that offer little clinical interpretability. We present GlaKG, a biomarker-centric fundus knowledge graph that integrates structural biomarkers, clinically grounded rules, and image features to produce traceable reasoning for glaucoma diagnosis and risk stratification. GlaKG encodes six entity types (Fundus Image, Optic Disc, Neural Rim, Pathology, Diagnosis, Risk Level), eight relation types, and 11 clinically validated rules into a unified graph, so that every prediction is accompanied by an explicit reasoning chain linking biomarker evidence to activated clinical rules. To keep knowledge-based reasoning strictly separate from label information, we adopt a post-processing fusion framework that combines ResNet50 image embeddings with a normalized KG reasoning-chain score via a tunable weight alpha, with all fitting confined to the training split. On a publicly available, AI-annotated fundus dataset, GlaKG reaches F1 = 0.9953 for binary glaucoma classification and 0.930 accuracy with 0.922 weighted F1 for four-class risk stratification; we report openly that the dataset's biomarker annotations are highly label-correlated, and therefore frame these figures as an upper bound attainable with clean structured biomarkers rather than as leakage-free image-only performance. Feature-importance analysis shows KG-derived and biomarker features contributing near-equally (51.1% vs. 48.9%), and the reasoning chain flags borderline cases by exposing low chain scores rather than failing silently. GlaKG's central contribution is therefore a clinically auditable reasoning framework that complements raw predictive performance by explicitly exposing the biomarker evidence and rule activations behind each decision.

---


### 410. [Video Generation Models Are Inherent Lighting Estimators](https://arxiv.org/abs/2607.04674)

**<font color=#1a73e8>作者：</font>** Ziqi Cai, Shuchen Weng, Kaiqi Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering dynamic environment maps from a single in-the-wild video is crucial for photorealistic rendering, yet remains a challenge. Recent video generation models can produce photorealistic scenes with complex lighting, possessing an inherent understanding of lighting. In this paper, we introduce V-LITE (Video generation models are inherent lighting estimators), a framework that unlocks this internal knowledge by reframing lighting estimation as a guided video inpainting task. Inspired by VFX industry practices, we insert a synthetic chrome ball into the scene to compel the model to generate physically plausible reflections from the surrounding spatio-temporal context. To bridge the gap from LDR-native models to the HDR domain, we design an HDR-aware VAE and employ an efficient LoRA-based fine-tuning strategy. We then construct a mixed dataset comprising high-fidelity HDR images to provide realistic HDR priors, and in-the-wild HDR videos to provide dynamic spatio-temporal context. Extensive experiments demonstrate that V-LITE produces temporally coherent HDR environment maps, revealing that modern video diffusion models are not merely synthesizers but also powerful, inherently capable estimators of physical scene lighting.

---


### 411. [ICME 2026 Grand Challenge on Cross-Scenario Defect Detection and Fine-Grained Severity Grading for High-Precision Manufacturing](https://arxiv.org/abs/2607.04675)

**<font color=#1a73e8>作者：</font>** Wei Sun, Weixia Zhang, Linhan Cao 等 33 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents the IEEE International Conference on Multimedia and Expo (ICME) 2026 Grand Challenge on Cross-Scenario Defect Detection and Fine-Grained Severity Grading for High-Precision Manufacturing. The challenge is motivated by two key limitations of existing industrial defect inspection systems: (1) current deep learning-based methods often suffer significant performance degradation when deployed in unseen production scenarios, and (2) most benchmarks neglect severity-aware assessment, which is critical for risk control and yield optimization. To address these limitations, we design two complementary tracks: Track 1 (Cross-Scenario Defect Detection) targets accurate defect detection, localization, and classification across diverse unseen production environments; Track 2 (Fine-Grained Severity Grading) requires assigning each detected defect an industry-standard severity level, including Acceptable, Marginal NG, NG, and Gross NG. We construct a large-scale industrial dataset of high-resolution microscopic images spanning seven representative defect categories, comprising over 3,800 images with pixel-level instance annotations for Track 1 and over 2,600 images with severity-grade labels for Track 2. The challenge attracted 86 registered participants with 130 submissions; during the final testing phase, 21 teams submitted results and 12 teams provided models with technical reports. The resulting benchmark, together with the diverse and effective solutions contributed by participating teams, sets a new standard for industrial defect analysis research.

---


### 412. [AnyStyle: A Single LoRA is Sufficient for Image-Guided Style Transfer](https://arxiv.org/abs/2607.04677)

**<font color=#1a73e8>作者：</font>** Yongwen Lai, Chaoqun Wang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-guided style transfer aims to apply the artistic characteristics of a style image to a content image while preserving its semantic structure and layout. Despite advances in diffusion-based methods, existing approaches often face challenges in disentangling content and style, particularly when independently optimized adapters are naively combined, causing conflicts between adapters and limiting controllability over the content-style balance in inference. We further demonstrate that training-free structural guidance directly derived from the content image through the internal attention of pre-trained model outperforms a dedicated content LoRA adapter in terms of structural fidelity and computational efficiency. Building on these observations, we propose AnyStyle, a streamlined framework for image-guided style transfer. The framework adopts a unified single-adapter paradigm for coherent style capture from the style image and incorporates training-free structural guidance from the content image, thus avoiding complex entanglement between multiple adapters and improving controllability and stability. Extensive experiments show that our method delivers competitive quantitative performance and significantly improved perceptual quality. Code is available at this https URL.

---


### 413. [A Physics-Regulated Neural Framework for Learning 3D Grain Growth Dynamics](https://arxiv.org/abs/2607.04680)

**<font color=#1a73e8>作者：</font>** Zhihui Tian, Kang Yang, Michael Tonks 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Grain growth is governed by the reduction in grain boundary energy and exhibits well-established statistical scaling laws. Developing data-driven surrogates that preserve these physical invariants while remaining computationally scalable remains challenging, especially in 3D. We present 3D-PRIMME (Physics-Regulated Interpretable Machine Learning for Microstructure Evolution) for learning three-dimensional grain growth dynamics. The model is trained using only two consecutive time steps yet accurately reproduces the linear coarsening law and preserves topological statistics over extended time scales. Despite being trained on a $100^3$ grid points with 512 grains, the learned evolution operator is applied to domains up to $1024^3$ grid points with 550000 grains without retraining, maintaining consistent kinetics and grain topology across orders-of-magnitude increases in system size. These results demonstrate that 3D-PRIMME learns a scale-independent and temporally stable local evolution rule, enabling efficient and robust large-scale surrogate prediction of 3D microstructure evolution.

---


### 414. [TubeLite: Lightweight Multi-Actor Spatio-Temporal Action Detection](https://arxiv.org/abs/2607.04684)

**<font color=#1a73e8>作者：</font>** Ali Soltaninezhad, Melissa Cote, Alejandro Rico Espinosa 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatio-temporal action detection in videos requires jointly localizing actors in space and identifying action boundaries over time. A common challenge is constructing temporally stable action tubes, as frame-level detectors often suffer from jitter, fragmentation, and imprecise temporal localization. Many recent approaches address this by introducing heavy spatio-temporal transformers or optical-flow-based pipelines, leading to high computational cost and limited scalability. We propose TubeLite, a lightweight framework for spatio-temporal action detection that focuses on stable tube construction and boundary-aware temporal modeling. TubeLite represents each actor as a tube, defined as a sequence of bounding boxes associated with a single actor over time, and explicitly enforces temporal consistency at both the spatial and semantic levels. The method combines low-jitter actor detection, Gaussian-weighted actor feature extraction, efficient short-term temporal propagation, and a boundary-focused temporal prediction head, while avoiding optical flow and large-scale temporal attention. Despite its compact design, TubeLite achieves strong video-level localization performance. It improves Video-mAP@0.5 by 4.5 and 7.1 percentage points over the best compared method on the MultiSports and UCF101-24 datasets, respectively, with substantially fewer parameters and floating-point operations than transformer-based alternatives, demonstrating that effective spatio-temporal action detection can be obtained through principled, lightweight temporal modeling.

---


### 415. [URSA: Chemistry-Aware Benchmark for Utilitarian Retrosynthesis Assessment](https://arxiv.org/abs/2607.04688)

**<font color=#1a73e8>作者：</font>** Bogdan Zagribelnyy, Ivan Ilin, Nikita Bondarev 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Synthesis planning aiming to find pathways of reactions for a target molecule is one of the most important and challenging tasks in drug discovery. Recent progress has produced both specialized deep-learning retrosynthesis systems and general-purpose large language models, but objective comparison remains difficult due to the lack of flexible, chemically interpretable benchmarking protocols. In the current study, we are introducing the URSA (Utilitarian RetroSynthesis Assessment) evaluation framework that provides the opportunity to benchmark the synthetic routes not only from a formal perspective, such as convergence to commercially available starting materials, but also from a chemical plausibility perspective, mimicking the way expert chemists evaluate the reactions and routes. The study covers a comprehensive evaluation of both conventional end-to-end retrosynthesis solutions and LLMs for the synthesis planning task on a set of novel, diverse target molecules with undisclosed synthetic routes, which represent realistic tasks in the daily drug design routine. We find that while LLMs can support high-level strategic planning, they currently underperform specialized retrosynthesis models in reliably solving synthesis planning tasks.

---


### 416. [PAST-TIDE: Prototype-Anchored Statement Tuning with Topic-Invariant Normalization for Stance Detection](https://arxiv.org/abs/2607.04690)

**<font color=#1a73e8>作者：</font>** Md. Shakhoyat Rahman Shujon, MD Jahid Hasan Jim, Md. Milon Islam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce PAST-TIDE, our stance detection system addressing both subtasks of the StanceNakba Shared Task at NakbaNLP@LREC-COLING 2026. The main idea is statement tuning. We redefine stance as cloze-style masked language modeling (MLM), letting a verbalizer map label words to stance categories through the pre-trained MLM head rather than appending a randomly initialized classification head. We complement this with prototypical contrastive learning, which uses learnable class prototypes for batch-size independent contrastive training, and topic-conditional layer normalization for cross-topic Arabic stance detection. PAST-TIDE achieves macro-F1 scores of 0.75 for Subtask A and 0.74 for Subtask B on the official leaderboard, indicating that minimal architectural additions to a pre-trained model can remain competitive in low-resource settings.

---


### 417. [From Open Loop to Closed Loop: A Test-Time Iterative Optimization Framework for Reference-Consistent Image Generation](https://arxiv.org/abs/2607.04691)

**<font color=#1a73e8>作者：</font>** Baixuan Zhao, Xinyu Zhang, Huayu Zheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While controllable image generation has made significant strides by incorporating visual reference conditions, existing methods predominantly operate as open-loop systems. They inject control signals in a strictly feed-forward manner, failing to guarantee strict fidelity to the reference due to the absence of active feedback and error correction mechanisms. To address this fundamental limitation, we propose a novel test-time iterative optimization framework that reformulates reference-consistent generation as a closed-loop dynamic tracking problem. By treating the pre-trained generative model as a control plant, our framework employs a sensor-controller architecture driven by a modified Proportional-Integral-Derivative (PID) algorithm. This mechanism iteratively optimizes the latent control signals at test time based on the sensed discrepancy between the generated output and the reference target. Notably, this approach is entirely training-free, model-agnostic, and integrates seamlessly around existing diffusion pipelines. Extensive evaluations across ID-preserving, pose-controlled, and depth-controlled generation tasks validate the universality of our method. Empirical results demonstrate improvements over computation-matched open-loop baselines, achieving relative performance gains of up to 25.36\% for facial similarity, alongside spatial error reductions of up to 27.71\% for pose alignment and 28.50\% for depth consistency. More broadly, this work offers a new conceptual perspective: it demonstrates that controllable generation can be effectively managed as a dynamic feedback system, bringing the rigorous principles of classical control theory into the optimization of generative models. Code is available at this https URL.

---


### 418. [Probe-EM: Targeted Neuron Tracing via Training-Free Semantic Verification](https://arxiv.org/abs/2607.04696)

**<font color=#1a73e8>作者：</font>** Liuyun Jiang, Yanchao Zhang, Jinyue Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Establishing large-scale, high-resolution neural connectivity maps is fundamental to elucidating the structural basis of brain function. However, when processing terabyte- or petabyte-scale electron microscopy data, over-segmentation inherent in automated reconstruction algorithms remains a critical bottleneck, requiring extensive manual proofreading spanning person-years. To alleviate the heavy reliance on annotated data and the limited flexibility of conventional tracing methods, we propose a training-free, targeted neuron tracing framework. Specifically, we introduce a skeleton-guided Heuristic Spatial Search paradigm that leverages geometric priors to iteratively reconstruct neuronal morphologies through a probing-verification cycle. To achieve robust zero-shot semantic verification, we further develop a Dimension-Aware Semantic Verification strategy built upon the foundation model NeuroSAM 2. This strategy resolves intra-slice splits via Planar Ensemble Consensus and inter-slice splits via Axial Spatio-Temporal Propagation. Notably, we integrate the proposed workflow into the Neuroglancer visualization platform, enabling an interactive human-in-the-loop proofreading system. Experimental results demonstrate that the proposed method outperforms supervised baselines and reduces manual proofreading time by 33.4%. The source code is publicly available at this https URL.

---


### 419. [F-ACVAE: A Federated Adaptive Conditional Variational Auto-Encoder for Privacy-Preserving Intrusion Detection in IoT Networks](https://arxiv.org/abs/2607.04698)

**<font color=#1a73e8>作者：</font>** Mohammad Ansarimehr, Somayeh Changiz, Ehsan Baghishani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of Internet of things (IoT) devices has significantly expanded the cyber-attack surface, necessitating robust and privacy-preserving intrusion detection systems (IDS). However, centralized learning approaches often suffer from severe performance degradation due to high-dimensional traffic data, extreme class imbalance, and highly non-independent and identically distributed (non-IID) data across heterogeneous edge devices. To address these challenges, this paper proposes F-ACVAE, a federated adaptive conditional variational autoencoder framework that enables collaborative model training across distributed IoT devices without sharing raw data. F-ACVAE incorporates selective parameter aggregation, where local encoders remain private while globally shared components are synchronized to preserve discriminative latent structures. To further enhance stability under extreme non-IID settings and feature distribution shifts, we introduce a novel constrained momentum Gaussian aggregation (CMGA) strategy that combines update clamping with momentum-based smoothing to mitigate client drift. Extensive experiments on the N-BaIoT dataset demonstrate that F-ACVAE achieves an average accuracy and macro F1-score of 99\%, outperforming state-of-the-art baselines. Moreover, the selective aggregation mechanism reduces communication overhead by approximately 62\%, making the framework particularly suitable for resource-constrained IoT environments. These results highlight the effectiveness of F-ACVAE in achieving high detection performance while ensuring privacy preservation and communication efficiency.

---


### 420. [Hierarchical Scaffolding Enables Human-Like Cognitive Selectivity under Data Scarcity](https://arxiv.org/abs/2607.04709)

**<font color=#1a73e8>作者：</font>** Juhyoung Park, Jaehyuk Bae, Hyeonbo Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern machine learning systems demand extensive datasets for visual recognition. Conversely, humans learn with high efficiency despite severe data limitations, often by acquiring broad categorical structures before refining finer distinctions. Inspired by this contrast, we introduce SCALA (Scaffolded Cognitive Architecture for Learning under limited dAta), a hierarchical learning framework grounded in cognitive psychology that guides models from coarse conceptual structures to fine-grained recognition. Our model exhibits human-like cognitive selectivity by effectively prioritizing task-relevant features while suppressing background distractors, a mechanism that induces a fundamental shift in representation learning. This shift is characterized by accelerated cluster formation, reduced intra-class dispersion, and enhanced semantic separability. Empirically, SCALA achieves significant accuracy improvements under severe data scarcity. Furthermore, this hierarchical scaffolding promotes robust generalization to unseen classes and accelerates the acquisition of novel categories. Collectively, our results establish SCALA as a powerful framework for achieving human-level sample efficiency and resilient category generalization in data-constrained environments.

---


### 421. [Integrated Altruistic and Fairness Preference Induces Advanced Mutual Cooperation in Sequential Social Dilemmas](https://arxiv.org/abs/2607.04710)

**<font color=#1a73e8>作者：</font>** Yu Wei, Yukiko Ogura, Yoshiyuki Ohmura 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inducing cooperation among distributed agents is still a difficult problem in the field of multi-agent reinforcement learning (MARL), particularly in social dilemma situations. There, individual interests are misaligned with the common good and individual rationality leads to suboptimal group outcomes. In contrast, humans are able to achieve cooperation with one another in such situations. A common explanation for such cooperative behavior is that individuals have social preferences. In order to achieve cooperation in MARL, we design a new utility function integrating altruistic preferences (incentive for other's reward) and fairness preferences (incentive for equality) from social psychology and behavioral economics, namely, Altruistic and Fairness Preference (AFP), a reward-sharing mechanism which converts one's own and other's rewards to incentives for cooperative behavior. We performed comparative experiments with standard RL and inequity aversion agents in two challenging sequential social dilemma games, and showed that AFP agents successfully achieved mutual cooperation with more collective rewards and higher equity than the baselines. To further understand the progression of AFP during training, we subsequently explore the effects of altruistic preferences and fairness preferences on agents' behavior. The results suggest that altruistic preferences encourage agents to contribute to the public goods, and fairness preferences induce mutual behavior between agents.

---


### 422. [Learning Probabilistic Prompt for Continual Learning](https://arxiv.org/abs/2607.04711)

**<font color=#1a73e8>作者：</font>** Hyekang Park, Sanghoon Lee, Geon Lee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Continual learning aims to progressively learn from a sequence of tasks, each containing a disjoint subset of classes, while preserving previously learned knowledge. Prompt-based continual learning methods propose to learn a small set of parameters, i.e., prompts, by associating them with a query feature of an input image. These methods optimize the prompts, attempting to represent diverse patterns of images. However, we have observed that existing prompt-based methods suffer from a prompt collapse problem, that is, the prompts tend to be highly similar to each other, thereby failing to capture the diverse data distributions in continual learning scenarios. To address this issue, we propose in this paper a novel prompt-based continual learning framework that captures diverse patterns of images across a sequence of tasks. To this end, we model each prompt as a probabilistic distribution and construct a mixture of these distributions, from which we sample diverse prompts. This enables our model to effectively capture highly diverse image distributions in the continual learning process. We also present a distribution regularization loss to prevent abrupt changes in the prompt distributions throughout the training process. We show extensive experimental results for continual learning on standard benchmarks, including ImageNet-R, CIFAR-100, and CUB-200, demonstrating the effectiveness of our framework.

---


### 423. [FORGE: Research-Trajectory Hijacking Attacks on Deep Research Agents](https://arxiv.org/abs/2607.04718)

**<font color=#1a73e8>作者：</font>** Yue Pan, Ziheng Zhang, Junxiang Lei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep research agents decompose open-ended queries into subtasks, retrieve web evidence over multiple rounds, and synthesize long-form reports. This workflow creates a planning-layer poisoning surface: adversarial documents that enter the retrieval pool can steer follow-up questions and turn a local injection into report-level contamination. We present FORGE (Fabricated Orchestrated Reasoning chain for aGent Exploitation), a two-level attack that combines intra-document reasoning fabrication with inter-document chain coordination to hijack subtask planning. We further introduce the PRISM metric, which weights infected report claims by cognitive type, and Root Query Anchoring, a lightweight defense that ties recursive follow-up generation to the root query. Across 25 queries, Network FORGE reaches 26.4% PRISM with five injected documents and exhibits depth migration, in which recursive synthesis shifts poisoned content from overt framing into factual premises. On the 10-query defense subset, RQA (Root Query Anchoring) reduces PRISM from 38.5% to 18.3%.

---


### 424. [Reference-Induced Consensus for Selective Posed-Reference Visual Localization](https://arxiv.org/abs/2607.04722)

**<font color=#1a73e8>作者：</font>** Wonseok Kang, Jaehyun Kim, Jeongmin Lee 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present RIC-Loc (Reference-Induced Consensus localization), a scene-training-free posed-reference localizer that is SfM-point-map-free in its main estimator: it uses known reference poses, but not precomputed SfM 3D map points, query-to-map 2D-3D matches, or query-to-map PnP. A frozen VGGT pass predicts local camera poses, depth, and query-reference tracks for a query and selected references. Each reference induces one map-frame SE(3) query-pose hypothesis, robust consensus estimates the pose, and the preserved hypothesis structure yields two reliability scores: spatial dispersion and a track-conditioned covariance score. On the covariance-eligible set, the two scores are complementary for held-out, ground-truth-free failure detection across indoor, outdoor, and large-scale low-texture benchmarks: the joint policy is strongest in textured scenes and the covariance score in the low-texture regime, and the hypothesis-derived scores consistently outperform the standard retrieval-score gap and random rankings. Without per-scene training the consensus estimator remains accurate -- competitive with structure-based localization indoors and improving over a comparable feed-forward baseline -- giving an effective selective operating regime for posed-reference localization. Code is available at this https URL.

---


### 425. [What You See Is What You Get: Observation-Aligned Supervision for Chart-to-Code Generation](https://arxiv.org/abs/2607.04726)

**<font color=#1a73e8>作者：</font>** Tianhao Niu, Qingfu Zhu, Wanxiang Che  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chart-to-code generation is commonly trained with supervised fine-tuning on reference plotting scripts, implicitly treating the gold code as a fully observable target. We argue that this assumption is often invalid: many chart programs contain latent raw variables that cannot be uniquely recovered from the rendered image. For example, a boxplot exposes summary statistics rather than original samples, a pie chart reveals proportions rather than arbitrary raw values, and a histogram shows bin-level mass rather than individual observations. Supervising models to reproduce such non-identifiable quantities encourages hallucination and over-specified code generation. We introduce Observation-Aligned supervision, a rewriting framework that replaces latent raw-data targets with quantities constrained by the visual observation: box statistics for boxplots, wedge percentages for pie charts, and bin weights for histograms. Applying this framework to chart-to-code training data from two sources, we obtain the Observation-Aligned supervision target data. Experiments across multiple VLMs on ChartMimic and ChartX demonstrate consistent improvements in observable value recovery, including under both-executable evaluation. Our results suggest that improving chart-to-code models requires not only more data or advanced learning objectives or algorithms, but also supervision targets that respect what is identifiable from the chart image.

---


### 426. [RustMizan: A Compilable, Contamination-Aware Benchmarking Framework for Rust Vulnerabilities](https://arxiv.org/abs/2607.04729)

**<font color=#1a73e8>作者：</font>** Tarek Elsayed, Shiping Yang, Eunsong Koh 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly applied to vulnerability analysis, but existing benchmarks have not kept pace. They typically rely on small non-compilable snippets, focus on binary classification (vulnerable or not), and do not account for the risk that publicly-released datasets are part of model training corpora. We introduce RustMizan, a benchmarking framework for Rust vulnerability analysis that addresses these gaps. RustMizan contains compilable code variants at the crate, file, and function levels, with annotations for binary vulnerability detection, CWE classification, and function- and line-level localization. A paired mutation framework produces semantics-preserving code mutants for contamination testing and robustness probing. Across four frontier models in an agentic setup with command-line access, binary classification sits in the 56-65% range, but line localization F1 stays near 20%, and adversarial cues drop line F1 by about 27%.

---


### 427. [When Does High-CFG Diffusion Inversion Fail? A Controlled Study of Prompt--Latent Interactions](https://arxiv.org/abs/2607.04731)

**<font color=#1a73e8>作者：</font>** Yan Zeng, Yusuke Hosoya, Huyen T. T. Tran 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-guided diffusion inversion is central to image editing, where an image is mapped to an initial latent and then edited by replaying the denoising process under a modified prompt. In practice, however, inversion is often performed with a lower classifier-free guidance(CFG) scale than the one used for generation or editing. This mismatch is empirically useful but leaves a basic question unresolved: when a target image is generated by a high-CFG trajectory, when can that trajectory actually be inverted? We study this question in a controlled generation--inversion--reconstruction setting, where the true initial latent and denoising trajectory are known. Using prompts taken from an existing diffusion-editing benchmark, we generate images under high CFG and reconstruct them with fixed-point inversion using the same prompt and guidance setting. The results reveal three types of prompt-level reconstruction behavior: easy prompts that reconstruct for most initial latents, hard prompts that fail for most initial latents, and intermediate prompts whose success depends on the prompt--latent pairing. To analyze the generation side, we define prompt pressure, a step-wise measure of how strongly CFG moves the denoising update away from the unconditional trajectory. Total pressure correlates with reconstruction quality and separates easy from hard prompts, but it does not explain the success or failure of intermediate prompt--latent pairs. Text-side analyses further show that the main visual subject and wording can change inversion difficulty. Finally, we evaluate a compact trajectory-consistency intervention that relaxes guidance only at locally unstable inverse steps. This diagnostic check improves reconstruction and Prompt-to-Prompt editing in our controlled setting, supporting the view that high-CFG inversion failure requires local, trajectory-aware analysis.

---


### 428. [SparseOcc++: Geometry-Aware Sparse Latent Representation for Semantic Occupancy Prediction](https://arxiv.org/abs/2607.04732)

**<font color=#1a73e8>作者：</font>** Pin Tang, Zhongdao Wang, Guoqing Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-based 3D semantic occupancy prediction is essential for autonomous driving, yet dense voxel representations waste computation on largely empty space, while BEV and TPV projections compromise fine-grained 3D structure. Fully sparse representations offer an attractive alternative, but existing methods, including SparseOcc, entangle scene completion with semantic prediction by indiscriminately propagating high-dimensional features into empty regions and applying voxel-wise classification. This creates excessive activations, computational overhead, and geometric ambiguity. We present SparseOcc++, a geometry-aware sparse framework that explicitly decouples scene completion from semantic segmentation. SparseOcc++ reformulates completion as signed-distance regression on sparse anchor voxels through a scene completion field (SCF). To model complex outdoor geometry robustly, it combines orthogonal decomposition with discretized distance learning. A geometry-guided propagation module then converts the SCF into a complete volumetric scene and restricts semantic segmentation to geometrically verified regions. Experiments establish new state of the art: SparseOcc++ improves IoU by 2.3 points and is 3.9x faster than SparseOcc on nuScenes, while achieving a 5.9x speedup over OccFormer on SemanticKITTI.

---


### 429. [DriftST: One-Step Generative Inference of Spatial Transcriptomics from H\&E Histology](https://arxiv.org/abs/2607.04740)

**<font color=#1a73e8>作者：</font>** Yuhang Yang, Yonggan Bu, Shengyuan Zhou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spatial Transcriptomics (ST) measures gene expression while preserving spatial context, but its high cost and low throughput leave public datasets small. Inferring expression directly from widely available Hematoxylin and Eosin (H&E) stained histology offers a cost-effective alternative. However, existing approaches face several limitations: regression methods over-smooth toward the conditional mean, while generative methods are faithful but require slow multi-step inference; most methods treat genes as independent and equally important, ignoring inter-gene dependencies and heterogeneous gene informativeness; and most are tailored to a single resolution, either spot-level or cell-level. To address these issues, we propose DriftST, a unified framework for inferring spatially resolved gene expression from H&E images. DriftST builds on a Cellular Drifting generative model that learns a direct drift from a histology-conditioned source to the expression distribution, retaining generative expressiveness while enabling efficient one-step generation. To capture gene structure, we introduce the STransformer, which combines a co-expression attention module for inter-gene dependencies with a gene residual gate for differential gene importance. Operating on a generic gene-panel representation, DriftST applies directly to both spot-level and cell-level data in one framework, and extensive experiments across diverse tissues and platforms show that it achieves state-of-the-art performance at both resolutions.

---


### 430. [MergeSurv: Merging-Based Continual Learning for Survival Analysis on Whole-Slide Images](https://arxiv.org/abs/2607.04747)

**<font color=#1a73e8>作者：</font>** Vu Minh Tran, Doanh C. Bui, Maï K. Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Survival analysis on Whole Slide Images (WSIs) is important in computational pathology for prognosis estimation and treatment planning. However, existing survival models are typically trained independently for each cancer cohort, making continual adaptation computationally expensive for gigapixel-scale WSIs. In this study, we propose MergeSurv, a merging-based continual learning framework for WSI survival analysis. A pathology vision-language foundation model is independently fine-tuned on each task, and the learned parameters are sequentially merged into a unified model without storing previous training data. We further investigate two inference strategies: One-for-All (OFA) and Voting-Expert Aggregation (VEA). Experiments on four TCGA cohorts demonstrate that MergeSurv outperforms naive fine-tuning as well as representative regularization-based and rehearsal-based continual learning methods, while effectively reducing catastrophic forgetting. The results suggest that model merging is a promising direction for scalable and privacy-preserving continual learning in computational pathology.

---


### 431. [FM-ChangeNet: Learning Change through Pathwise Feature Transport](https://arxiv.org/abs/2607.04750)

**<font color=#1a73e8>作者：</font>** Roie Kazoom, George Leifman, Genady Beryozkin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present FM-ChangeNet, a pathwise-supervised framework for change detection that reformulates bi-temporal reasoning as continuous transport in feature space rather than static endpoint comparison. Given encoded pre and post-temporal representations, we construct intermediate latent states and learn a time-conditioned velocity field $\hat{v}_\theta(z_t,t)$ along the transformation trajectory. This pathwise formulation constrains the predictor over a continuum of intermediate states, providing a denser and less ambiguous supervision signal than conventional endpoint-only segmentation and enabling the model to capture temporal evolution explicitly. The learned velocity field is not only a transport mechanism but also an interpretable representation of change: its magnitude serves as a spatially localized change cue that helps distinguish true structural variation from nuisance effects such as illumination shifts and spatial misalignment. We develop a hierarchical multi-scale architecture with cross-temporal alignment, time-conditioned coarse-to-fine flow decoding, and a unified objective that couples flow supervision, trajectory consistency, spatial regularization, and segmentation loss. Experiments on remote sensing benchmarks show that the proposed framework produces more structured and robust change representations while achieving state-of-the-art performance.

---


### 432. [Trust Region Policy Distillation](https://arxiv.org/abs/2607.04751)

**<font color=#1a73e8>作者：</font>** Zhengpeng Xie, Li Lyna Zhang, Zeke Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Big goals are hard to achieve all at once; breaking them into small steps is wiser. We present Trust Region Policy Distillation (TOP-D), which transforms the notoriously unstable, high-variance On-Policy Distillation (OPD) into a stable training paradigm by dynamically constructing a proximal teacher. Theoretically, we establish a rigorous framework demonstrating that TOP-D inherently controls gradient variance. By providing a formal global convergence analysis alongside a monotonic improvement bound, we mathematically formalize the reliability and stability of the overall training dynamics. Empirically, TOP-D dramatically enhances training stability, sample efficiency, and final performance on mathematical reasoning tasks. More importantly, TOP-D introduces zero additional computational overhead, positioning itself as a promising alternative to the well-established OPD paradigm.

---


### 433. [Continual Model Merging with Test-Time Adaptation for Whole-Slide Image Analysis](https://arxiv.org/abs/2607.04755)

**<font color=#1a73e8>作者：</font>** Duc-Thanh Le, Doanh C. Bui, Maï K. Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model merging offers a practical alternative to conventional continual learning by integrating independently fine-tuned models without retaining previous training data. Recent state-of-the-art model merging methods employ test-time adaptation (TTA-guided merging) to address distribution shifts by adjusting merging-related variables using unlabeled target data. However, these methods have primarily been studied in multi-task or single-target settings, and their behavior under sequential continual learning remains insufficiently understood. We present a benchmark study that maps this family of methods to rehearsal-free continual Whole Slide Image classification and evaluates them against traditional continual-learning approaches. Experiments on six TCGA cancer-subtyping cohorts cover CLASS-IL and TASK-IL scenarios, in-domain and out-of-domain evaluation, and different task orders. The results show that adapting model merging at test time can provide strong task-specific performance and improve retention of previously acquired knowledge without storing historical WSIs. Nevertheless, performance remains sensitive to task order and to the interaction between adaptation on the current distribution and accumulated knowledge. This benchmark identifies model merging with test-time adaptation as a promising direction for continual computational pathology and motivates future methods that balance adaptation to domain shift with explicit preservation of historical knowledge.

---


### 434. [DeGenseGS: Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting](https://arxiv.org/abs/2607.04761)

**<font color=#1a73e8>作者：</font>** Yimo Wang, Bin Kang, Shuojue Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time, text-promptable 4D reconstruction is indispensable for autonomous surgical interaction. Severe misalignment between semantic meaning and physical anatomy still persists, largely because existing solutions integrate Vision-Language Models into deformable fields via a rigid coupling scheme that tightly binds semantic features to geometric warping. In this paper, we propose DeGenseGS, Geometrically and Semantically Decoupled Surgical Scene Understanding in 4D Gaussian Splatting, a novel framework that independently models semantic evolution and geometric deformation. Specifically, we propose a HexPlane-based spatiotemporal entanglement module that uses shared kinematic latents to synchronize semantic mutations with scene dynamics, while explicitly disentangling semantic updates from geometric deformation. To further ensure robustness against reconstruction artifacts, we devise a Rasterization-Native Semantic Extraction mechanism that infers semantics from topologically continuous feature maps. Additionally, we incorporate an angular-aligned optimization strategy that conforms to the native hyperspherical latent space, thereby preventing semantic distortion. Extensive evaluations on the CholecSeg8k and EndoVis18 datasets demonstrate that DeGenseGS achieves state-of-the-art performance. Our framework yields enhanced geometric completeness and robust semantic-anatomic alignment, enabling spatially continuous segmentation despite drastic tissue deformation and topological transitions.

---


### 435. [Multi-Turn On-Policy Distillation with Prefix Replay](https://arxiv.org/abs/2607.04763)

**<font color=#1a73e8>作者：</font>** Baohao Liao, Hanze Dong, Christof Monz 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study on-policy distillation (OPD) for agentic tasks, where an LLM agent interacts with an environment over multiple turns and a student imitates a teacher over these multi-turn interaction histories. Fully online OPD is costly because each update requires fresh student rollouts through the environment and teacher queries at visited histories. We propose Replayed-Prefix On-Policy Distillation (ReOPD), an off-environment alternative that reuses pre-collected teacher trajectories as replayed prefixes: the student acts at selected steps, while the teacher provides dense per-step supervision without executing new environment interactions. We show that multi-turn OPD introduces a prefix trap: making histories more student-on-policy improves relevance to the student, but can query the teacher on histories where its target is unreliable. This creates a two-sided distribution shift between student occupancy and teacher reliability. ReOPD addresses this by treating multi-turn OPD as a reliability-aware prefix distribution design and implements it with a simple step-decaying sampling schedule that emphasizes early, lower-shift prefixes. Across mathematical reasoning with Python and search environments over multiple teacher and student model scales, ReOPD preserves or improves OPD-level accuracy, uses zero tool calls during student training, and is at least 4$\times$ faster per training step than OPD. ReOPD therefore turns expensive agent-environment interaction into a reusable offline resource, enabling scalable distillation across tools, tasks, and environments.

---


### 436. [HilEnT: Hilbert, Entropy Transformed Image Based Malware Detection](https://arxiv.org/abs/2607.04772)

**<font color=#1a73e8>作者：</font>** Rahul Kale, Thesath Wijayasiri, Kar Wai Fok 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the increasing threat of malware across various software related domains, malware detection and classification is critical to determine the response actions. Different strategies have been adopted to address the challenge of malware detection. With the advent of deep learning techniques, malware detection using image processing has garnered research attention. In this work, we proposed a novel malware binary to image transformation technique HilEnT based on a combination of Hilbert curve-based transformation of malware binary and the entropy feature comparison of malware file with benign and malware classes. Three grayscale images produced during this process are combined to form a three-channel colored image which is then used for malware detection using machine learning techniques. We performed supervised binary and multiclass classification to evaluate the effectiveness of our proposed HilEnT. We also evaluated a few-shot learning technique to assess the robustness of our proposed HilEnT in a practical setting where the number of available class samples is limited. Furthermore, we investigated the benefits of combination of Histogram of Oriented Gradients and Principal Component Analysis for time performance improvements through feature reduction techniques. We evaluated our proposed methodology on four datasets: Dike, Michael Lester Dataset, Microsoft BIG 2015 and a self-collected dataset, and achieved the state-of-the-art results.

---


### 437. [MARLIN: De Novo Molecular Structure Elucidation from Tandem Mass Spectra without a Ground-Truth Formula](https://arxiv.org/abs/2607.04774)

**<font color=#1a73e8>作者：</font>** Xujun Che, Xiuxia Du, Depeng Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Untargeted tandem mass spectrometry (MS/MS) detects thousands of small molecules per biological sample, yet most go unidentified because they are absent from spectral libraries. These uncharacterized metabolites and natural products are precisely the compounds that matter for drug discovery, biomarker research, and exposomics. Computational de novo structure elucidation could close this gap, but almost all state-of-the-art methods assume the ground-truth molecular formula is known, an oracle that does not exist for genuinely novel compounds and is itself predicted with substantial error. We present MARLIN, a de novo method that elucidates structures directly from a spectrum with no molecular formula at any stage. A self-supervised encoder predicts a molecular fingerprint from the raw peaks, and a block-diffusion language model generates candidate structures conditioned only on the fingerprint and the instrument-measured precursor mass. A provably safe mass-shell constraint keeps every candidate consistent with the measured mass without fixing the atom inventory, and candidates are accepted by exact parts-per-million mass agreement. A symmetric noise objective absorbs encoder error, and a candidate-diversity mechanism keeps the candidates from collapsing to a single structure. On the NPLIB1 benchmark, MARLIN is the strongest method evaluated without a ground-truth formula across exact-match accuracy, structural distance, and fingerprint similarity, and it recovers the correct molecular formula as a byproduct about as often as a dedicated predictor without ever using one. MARLIN enables reliable de novo structure elucidation in the realistic discovery regime where the molecular formula is unavailable.

---


### 438. [Towards Personalized Differentially Private Learning for Decentralized Local Graphs](https://arxiv.org/abs/2607.04777)

**<font color=#1a73e8>作者：</font>** Longzhu He, Peng Tang, Chaozhuo Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph-structured data is increasingly generated and stored in decentralized environments, such as social platforms, mobile applications, and edge networks, where users maintain control over their local graph data. However, collecting and analyzing such decentralized graph data for downstream learning tasks raises significant privacy concerns, as nodes and their attributes often contain sensitive personal information. Local Differential Privacy (LDP) has emerged as a promising solution for privacy-preserving data collection without relying on trusted servers. Nevertheless, existing LDP-based graph learning methods typically assume uniform privacy requirements across users, ignoring the heterogeneous and personalized privacy preferences commonly observed in real-world systems. This uniform treatment leads to inflexible noise injection at the data collection stage, resulting in substantial distortion of graph data and degraded utility in subsequent analysis. To address this limitation, we propose PPGNN, a personalized differentially private framework for decentralized graph data. PPGNN enables user-specific privacy budgets during local perturbation while preserving analytical utility. To handle heterogeneous privacy levels and noise distortion, we design a two-stage solution consisting of a Personalized Perturbation Mechanism (PPM) and a weighted calibration strategy, FlexProp. Extensive experiments on six real-world graph datasets demonstrate that PPGNN effectively balances personalized privacy protection and data utility in decentralized graph learning scenarios.

---


### 439. [Predicting Drafted Deck Strength for "Magic: the Gathering"](https://arxiv.org/abs/2607.04782)

**<font color=#1a73e8>作者：</font>** Tomas Rigaux, Hisashi Kashima  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many real-world games do not admit a fixed, compact rule set: instead, their dynamics are defined by interactions among a large and often evolving collection of game pieces, making general-purpose policy learning impractical. Magic: the Gathering (MTG) exemplifies this setting, where the cards themselves define and alter gameplay rules, strategic constraints, and long-term outcomes, while the pool of available cards is ever-changing. We study Draft, a constrained deck-building format of MTG in which eight players make 39-45 sequential selections from semi-random packs to construct a 40-card deck under partial information. By isolating the card selection process from gameplay, Draft provides a tractable yet non-trivial setting for studying decision-making driven by combinatorial card synergies. We propose an encoder-based model that produces set-contextualized card embeddings to encode the draft decision sequence, with a consistent improvement over linear baselines on large-scale real-world data, establishing a first learned benchmark for outcome prediction in MTG Draft. Our code is available at this http URL.

---


### 440. [Ghost Traffic: ICMP Tunneling-Based Billing Bypass in LTE Networks](https://arxiv.org/abs/2607.04783)

**<font color=#1a73e8>作者：</font>** Jung Jin Kim, Sungyup Nam, Seungho Jeon  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cellular data billing is a core operational mechanism for mobile Internet service providers (ISPs), and a policy gap that excludes a specific protocol from usage accounting can lead to a practical security threat. Some cellular ISPs treat ICMP echo traffic as control traffic rather than user data and exclude it from billing. At the same time, Android allows ordinary applications to create ICMP echo sockets without root privileges because of an unsafe default configuration, and the combination of these two conditions forms a vulnerability that can bypass data billing. Existing billing-bypass attacks either require root privileges to create raw sockets and modify routing tables, or do not provide an end-to-end implementation that works in a non-rooted environment, which limits the threat to a small group of experts. This paper proposes Ghost Traffic, an end-to-end system that uses Android's VpnService to encapsulate all application traffic into ICMP echo payloads without root privileges and route it through an external proxy server. The proposed system targets both public IPv4 environments and IPv6-only LTE environments through two variants: IPv4 ICMP tunneling and IPv4-over-IPv6 ICMP tunneling. We evaluated its applicability in seven ISP environments in South Korea, Japan, and the United States, and observed end-to-end tunneling in six of them. We observed that billing bypass occurred in multiple environments and quantitatively showed this effect by measuring that Quality of Service (QoS) throttling was not applied even after the data cap was exhausted. Finally, we propose layered countermeasures across the device, platform, and network levels, performed responsible disclosure, and show that the operational practice of not billing ICMP traffic can lead to practical billing bypass.

---


### 441. [Compressed Computation under $L^4$ Loss is likely Computation in Superposition](https://arxiv.org/abs/2607.04800)

**<font color=#1a73e8>作者：</font>** Francisco Ferreira da Silva, Stefan Heimersheim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks are thought to represent concepts as directions in their activation space, and superposition lets them encode more concepts than they have dimensions. It is natural to ask whether they can also compute more functions than they have neurons, i.e., perform computation in superposition. In this regime many functions of sparse inputs are evaluated by a layer with fewer neurons than there are functions to compute. Representation in superposition is by now fairly well understood, but computation in superposition is not, and there are few toy models of it arising through training rather than being hand designed. As a toy model of computation in superposition we study the compressed-computation setup: a single-hidden-layer ReLU network with 50 neurons that must compute the ReLU of each of 100 sparse input features. We show that training it under an $L^4$ loss (the mean fourth power of the error), rather than the usual $L^2$, elicits a solution that appears to compute all features in superposition. We then reverse-engineer this solution. We find that the network assigns each feature a sparse binary codeword over neurons and decodes it with a pseudoinverse of the encoder. Given these codewords, a description with only three scalars recovers most of the network's performance, and we validate it by building equivalent networks from hand-designed codes.

---


### 442. [LILAC: Layer-Wise Independent LoRAs and Cascaded Conditioning for Multi-Concept Customization of Diffusion Models](https://arxiv.org/abs/2607.04801)

**<font color=#1a73e8>作者：</font>** Marian Lupascu, Sebastian Ripa, Mihai Trascau 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Personalizing text-to-image diffusion models to render several specific subjects in a coherent image remains challenging: the model must preserve each subject's identity while keeping the scene spatially and visually coherent. Methods that fuse independently trained concept adapters in a shared weight space (via federated averaging, gradient fusion, or orthogonality constraints) suffer from identity confusion and style bleeding and require joint retraining. In this work, we show that composing concepts as separate image layers, instead of merging their adapters in a shared weight space, avoids parameter-level interference. We introduce LILAC, a framework that composes independently trained low-rank adapters at inference time: each subject is conditioned on the frozen composite of previously placed subjects, with exactly one adapter active at a time, therefore identities never interfere at the parameter level. LILAC composes the adapters without any joint training, scales linearly with the number of concepts, and is backbone-agnostic. Under the Orthogonal Adaptation protocol, LILAC applied on Qwen-Image-Edit reaches an ArcFace detection rate of 0.861, while Orthogonal Adaptation reports 0.745 in its original setting. Adaptation reports 0.745 in its original setting. Code is available at this https URL.

---


### 443. [Hybrid Deep Learning for Traceability and Classification of Industrial Slate Tiles](https://arxiv.org/abs/2607.04811)

**<font color=#1a73e8>作者：</font>** Soren Antebi, Stefan Eickeler, Sandra Halscheidt 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Applying deep learning to instance-aware reidentification of slate tiles and extraction site classification can improve production efficiency and quality control in the slate tile industry. These tasks are particularly important for handling natural materials where visual variability can make manual inspection costly and error-prone. We present a lightweight, hybrid deep learning approach that combines image matching and classification within a single framework. The system integrates a feature-matching branch based on XFeat with a MobileNetV3- based classification branch. The XFeat branch, combined with a LightGlue matching head, improves instance matching performance by +15.4% AUC. For classification, features from both backbones are shared and fused, resulting in a +10.9% accuracy improvement over a standard MobileNetV3 model. Our approach is evaluated on a newly created industrial dataset consisting of 2,610 slate tile images from six extraction sites. The results demonstrate the effectiveness of the proposed approach for object re-identification and classification in an industrial setting.

---


### 444. [TGRIP: A Text-Guided Approach to Vehicle Instance Prediction in Autonomous Driving](https://arxiv.org/abs/2607.04812)

**<font color=#1a73e8>作者：</font>** Miguel Antunes-García, Santiago Montiel-Marín, Fabio Sánchez-García 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bird's-Eye View (BEV) end-to-end instance prediction has emerged as a robust paradigm for autonomous driving perception, effectively mitigating the error propagation inherent in traditional modular pipelines. However, current state-of-the-art approaches rely predominantly on geometric supervision, such as occupancy regression and optical flow, effectively treating scene agents as generic moving obstacles. This absence of explicit semantic awareness imposes limitations on the capacity of the model to solve ambiguities in complex scenarios, particularly those where object-specific behavior is essential for accurate forecasting (e.g. overtaking, intersections). In this paper, we introduce Text-Guided Representation for Instance Prediction (TGRIP), a novel framework that bridges this gap by injecting rich semantic priors into the instance prediction loop. The proposed teacher-student pipeline employs Vision-Language Foundation Models to generate dense, semantic-enhanced BEV maps from multi-camera images. These maps serve as auxiliary supervision during training, guiding the network to learn spatio-temporal representations that are not only geometrically consistent but also semantically discriminative. To the best of our knowledge, this represents the first attempt to unify semantic guidance with the temporal task of future instance prediction. The experimental results demonstrate that TGRIP surpasses existing state-of-the-art models in nuScenes, validating the hypothesis that semantic enrichment is a fundamental element for robust, end-to-end motion prediction. Code is available on this https URL.

---


### 445. [Evaluating the Effect of Linguistic Relatedness on Cross-Lingual Transfer in Large Multilingual Automatic Speech Recognition](https://arxiv.org/abs/2607.04814)

**<font color=#1a73e8>作者：</font>** Andrei Florian, Cynthia Jayne Amol, Hope Kerubo Ombaba 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Extending automatic speech recognition (ASR) to low-resource African languages is constrained by the prohibitive demands of data collection at scale. A promising direction is to leverage linguistic relatedness to enhance cross-lingual transfer from a related auxiliary language to the low-resource target by sequentially adapting on both. Although this strategy has shown meaningful improvements in small ASR models, its effectiveness in large ASR remains unclear. We extend this framework to large multilingual ASR through a systematic controlled experimental design spanning six factors, two Africa-centric corpora, and four large ASR models, isolating whether linguistic relatedness reliably predicts cross-lingual transfer gains in this setting. Across all conditions, pre-adaptation on related auxiliary languages yields no practically meaningful transfer improvements given minimal target-language data, suggesting that linguistic relatedness alone may not reliably predict cross-lingual transfer gains in large multilingual ASR, or constitute an effective strategy for extending such models to low-resource languages.

---


### 446. [Layer-Parallel Inference Reduces Encrypted Nonlinear Depth in Transformers](https://arxiv.org/abs/2607.04819)

**<font color=#1a73e8>作者：</font>** Ligong Han, Kai Xu, Hao Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) enables computation on encrypted data, but practical encrypted Transformer inference is bottlenecked by the sequential composition of many nonlinear blocks. We study whether Structured Newton Layer Parallelism (SNLP) can make this inter-layer composition more FHE-friendly: each Transformer block still requires polynomial approximations for operations such as softmax and RMSNorm, but SNLP reduces the layerwise sequential nonlinear depth from L stages to a small number of solver iterations plus linear structured corrections. Using a simulation framework based on Chebyshev polynomial approximations, we measure error accumulation under sequential versus SNLP inference across 8 models and 4 architecture families. On a 0.5B IDN-trained model, SNLP reduces symbolic bootstraps from 53 to 20 (2.65x) with only +1.2% perplexity degradation, while lowering error amplification (1.36x vs. 1.42x). Across all tested models, SNLP has lower amplification than sequential inference. Ablations show that softmax approximation dominates the error budget and CKKS arithmetic noise is negligible in our setting, suggesting that SNLP is complementary to block-level FHE-friendly operator design rather than a replacement for it.

---


### 447. [KinEMbed: Decoding Kinematics from Electromyography via Cross-Modal Contrastive Learning](https://arxiv.org/abs/2607.04820)

**<font color=#1a73e8>作者：</font>** Sofia Gilardini, Chenfei Ma, Kianoush Nazarpour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decoding hand kinematics from surface electromyography (EMG) is a core challenge in wearable biosignal processing with clinical relevance for prosthetic control and motor rehabilitation. Most representation learning approaches for EMG focus on discrete gesture classification, and few focus on continuous regression. We present KinEMbed, a cross-modal contrastive learning framework for hand kinematics regression that jointly trains dual encoders -- one for windowed EMG features and one for kinematic (joint angle) targets. The resulting embeddings inherit the geometric structure of the kinematic space without requiring kinematic signals at inference time. Evaluating on the NinaPro DB8 dataset that includes both able-bodied users and subjects with limb difference (N=11), KinEMbed outperforms PCA, PLS, autoencoder and contrastive (CEBRA) baselines on held-out sessions, with largest gains on the most challenging thumb degrees of articulation. We position this work as a first step toward contrastive representation learning for regression of hand kinematics from structured wearable biosignals.

---


### 448. [Probably Correct Optimal Stable Matching under Two-Sided Uncertainty](https://arxiv.org/abs/2607.04824)

**<font color=#1a73e8>作者：</font>** Andreas Athanasopoulos, Anne-Marie George, Christos Dimitrakakis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a sequential learning problem for stable matchings in two-sided markets where preferences on both sides are initially unknown. We focus on a centralized setting where an algorithm matches agents at each time step and receives noisy rewards that reflect the preferences of the matched agents, following a semi-bandit feedback structure. We adopt a pure exploration perspective, aiming to efficiently identify the optimal stable matching with high probability. Our work extends prior results by handling \emph{two-sided uncertainty} and by exploiting \emph{partial preference} information. A central ingredient is the notion of \textbf{pervasive stable matching}, which enables the identification of optimal stable matchings under partial preferences. We propose elimination-based algorithms whose stopping criteria exploit the structure of the learned partial preferences, and provide a refined sample-complexity analysis. Beyond pure exploration, we extend our approach to regret minimization and establish regret bounds with respect to the \emph{optimal} stable matching that avoid dependence on the minimum reward gap $\Delta_{\min}$.

---


### 449. [Dynamic Airspace Management for UAVs in Evolving Urban Environments: Collaborative Coordination and Human Safety](https://arxiv.org/abs/2607.04825)

**<font color=#1a73e8>作者：</font>** Lin Sun, Yuhang Wang, Fan Meng Hong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> The low-altitude economy is an emerging industry with significant development potential, in which the safety of unmanned aerial vehicle (UAV) operations is a critical challenge. Particularly within complex urban topographies and human-populated environments, UAV airspace management must prioritize collision avoidance and human safety. We propose Pharos, a collaborative multi-UAV airspace management system. Pharos lies between the distributed local perception paradigm and the centralized fine-grained control paradigm. Pharos coordinates the safe parallel execution of UAVs in shared airspace while innovatively accounting for the impact of human fear. Pharos is implemented using the MAPPO algorithm due to its faster convergence and higher rewards than other typical MARL algorithms (HAPPO and HATRPO). To evaluate Pharos, we developed a 3D simulation system using real urban data. Visualization results demonstrate its effective airspace coordination capability. Regarding performance verification, Pharos reduced human fear by 52.72% compared to the benchmark Ipopt. Moreover, we designed spatial entropy as a system evaluation metric to quantify space utilization, which improved performance by 70.82% and 2.03% compared to the benchmarks Ipopt and A-star, respectively. The source code is available at an anonymized repository: this https URL.

---


### 450. [Semantic Homogenization in Italian Popular Music: A Diachronic Analysis](https://arxiv.org/abs/2607.04832)

**<font color=#1a73e8>作者：</font>** Lorenzo Canale, Stefano Scotta, Alberto Messina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, studies have revealed a decline in semantic variety across popular music lyrics, particularly in English-language songs on streaming platforms like Spotify. This research examines whether a similar trend can be observed in a different linguistic and cultural context: the lyrics of all finalist songs from the 75 editions of the Sanremo Music Festival, Italy's most renowned music competition. What sets this work apart is the development of a flexible and efficient methodology for tracking changes in semantic similarity over time, which can be applied to different datasets to study similar phenomena. Drawing on a combination of full-text, segment-based, topic-based, and word-level analyses, the approach leverages both embedding techniques and large language models. When applied to the Sanremo corpus, this framework reveals a gradual move toward increasing semantic uniformity, echoing the global patterns identified in previous studies. These findings underscore the value of natural language processing tools in uncovering long-term shifts in musical language and cultural expression.

---


> [!TIP]
> 当前位于：**401-450**（第 9/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | **401-450** | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
