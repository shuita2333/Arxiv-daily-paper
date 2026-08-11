# 📦 其他研究 | 2026年08月12日

> 本类共 **445** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-445](./part-09.md)

---

### 101. [APEX-VW: A Document-Level English-Spanish Post-Editing Dataset in the Healthcare Domain](https://arxiv.org/abs/2608.08059)

**<font color=#1a73e8>作者：</font>** Marie Escribe, Tharindu Ranasinghe, Amal Haddad Haddad 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-Editing (PE) of Machine Translation (MT) output often involves repeating the same lexical and terminological corrections across many segments, especially in specialised and highly repetitive documents. Despite substantial work on Automatic Post-Editing (APE), most available corpora operate at the sentence level, others are synthetic, and overall not designed to study how corrections propagate in realistic Computer-Assisted Translation (CAT) workflows. This paper presents the APEX-VW (Automatic Post-Editing eXperiments on Virtual Wards) Corpus, a new open English-Spanish (EN-ES) dataset built from recent NHS virtual-ward documents and professional PE in Trados Studio, with controlled MT, terminology, and quality assurance settings. The corpus contains seven document-coherent source texts totalling 42k words, translated with four MT systems representing different paradigms and then post-edited by professional translators. Unlike prior resources such as WMT APE corpora, eSCAPE, MLQE-PE, or LangMark, the dataset preserves document order and CAT-tool context, making it suitable for research on terminology normalisation, correction propagation, and human-in-the-loop translation support. The paper describes the corpus design, data preparation, PE setup, and initial corpus statistics, and positions the resource as a benchmark for document-level APE and propagation-aware assistive tools.

---


### 102. [CLAM: Causal Spatial Disaggregation to Infer Local Effects From Coarse Data](https://arxiv.org/abs/2608.08064)

**<font color=#1a73e8>作者：</font>** Gerrit Großmann, Sumantrak Mukherjee, Sebastian J. Vollmer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning fine-grained spatial patterns from coarse-resolution data is challenging, especially in causal settings where high-resolution effects must be inferred from aggregated interventions and outcomes. We introduce CLAM, a method for estimating localized causal effects from coarse observations by exploiting high-resolution contextual covariates that modulate these effects. By jointly learning the causal mechanism and a disaggregation mapping, CLAM captures interactions that are missed when addressing these problems independently. The method supports localized effect estimation, counterfactual reasoning, and principled outcome disaggregation, and reliably captures spatially varying causal effects across diverse settings. This is particularly relevant for applications such as public health and environmental policy, where decisions are made at broad scales despite substantial local heterogeneity. Code is available at this https URL

---


### 103. [EvBS: Event-guided Blur Synthesis for Domain-adaptive Motion Deblurring](https://arxiv.org/abs/2608.08066)

**<font color=#1a73e8>作者：</font>** Junsik Jung, Seokryun Choi, Yoonki Cho 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Motion deblurring has achieved remarkable progress with deep learning, yet pre-trained deblurring models often suffer from performance degradation in real-world scenarios due to the domain shift between training and testing distributions. To remedy this, we propose EvBS, an event-guided blur synthesis framework that generates diverse training pairs for calibrating pre-trained models to the target domain. While existing methods are constrained by the inherent entanglement between motion and visual content, our method leverages the high temporal resolution of event cameras to effectively decouple them. This enables us to utilize not only the intrinsic motion that is inherent to the given content but also extrinsic motion transferred from different sources within the target domain, thereby facilitating effective adaptation via fine-tuning. Specifically, EvBS comprises two complementary strategies: Intrinsic-Blur Synthesis, which blurs sharp contents with their own motion patterns, and Extrinsic-Blur Synthesis, which transfers motion from blurry patches to distinct sharp content. This approach generates a diverse set of training pairs that break the inherent constraints of naturally coupled motion and content, resulting in enhanced domain-adaptive deblurring performance. Extensive experiments on multiple benchmarks demonstrate that EvBS effectively enhances the robustness of existing deblurring models on unseen testing datasets.

---


### 104. [DialectS2S: End-to-End Speech Dialogue Modeling for Low-Resource Chinese Dialects](https://arxiv.org/abs/2608.08067)

**<font color=#1a73e8>作者：</font>** Yi Shu, Tianyu Peng, Yingzhuo Deng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current end-to-end speech dialogue models are primarily optimized for mainstream languages and remain limited in low-resource dialect scenarios due to the scarcity of dialect speech data. Moreover, during dialect adaptation, the semantic representation space of speech dialogue models continuously evolves, while conventional speech supervision remains unchanged, leading to semantic inconsistency between hidden representations and speech targets and degrading speech stability and naturalness. To address these issues, we propose DialectS2S, an end-to-end speech dialogue model for Chinese dialects. We first develop a scalable dialect speech dialogue synthesis pipeline for efficient data construction. We further introduce a two-stage post-training strategy with self-aligned speech supervision, which aligns the semantic content of speech supervision with the evolved semantic representations of the model to improve dialect speech generation quality. Experimental results show that DialectS2S consistently outperforms existing baselines across multiple Chinese dialects in speech dialogue, achieving substantial improvements in dialect consistency, response quality, and speech intelligibility. Our work provides an efficient and scalable solution for end-to-end speech dialogue modeling in low-resource dialect scenarios. To facilitate future research and practical applications, we fully open-source the DialectS2S framework, including model checkpoints, training datasets, and fine-tuning code.

---


### 105. [NeuroGuard: Neural Gradient Update Aware of Representation Damage](https://arxiv.org/abs/2608.08068)

**<font color=#1a73e8>作者：</font>** Taigo Sakai, Kazuhito Hotta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-tailed class-incremental learning (LT-CIL) must learn new classes from imbalanced streams while retaining old classes. Existing methods mainly change replay, classifiers, or losses. We study a different factor, namely how strongly the feature representation should be updated at each task boundary. We propose NeuroGuard, an update-control method added to DGR, a replay-based LT-CIL baseline, without adding learnable parameters. NeuroGuard preserves DGR's replay memory, classifier, and set of loss terms. Adaptive Gradient Scaling (AGS) converts teacher uncertainty into one task-wise gradient scale. Confidence-Ranked Knowledge Distillation Reweighting (CRK) gives larger knowledge-distillation weights to replay samples that the teacher predicts less decisively. Fragility-Blended Entropy Gate (FBE) adds old-memory leakage to the scale decision. Across five LT-CIL settings, NeuroGuard improves over DGR in every setting. In the four main benchmark comparisons, it achieves the best task-agnostic accuracy among the compared methods. The gains extend to both old- and new-class accuracy, while medium-frequency accuracy improves consistently across all five settings. Controlled comparisons show that the gain does not come from generic gradient suppression: AGS outperforms a matched fixed-scale control in all five settings, demonstrating that boundary-specific scaling is more effective than applying the same average scale throughout learning.

---


### 106. [PATH: Next-Interval Prediction via Autoregressive Tree Hierarchy on Tabular Data](https://arxiv.org/abs/2608.08078)

**<font color=#1a73e8>作者：</font>** Pengxiang Cai, Wanchen Lian, Chenyang Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interval prediction aims to achieve a target coverage level while producing intervals that are as short as possible. Many conformal regression pipelines first predict an uncertainty surrogate and then convert it into an interval through calibration or selection. This separation supports coverage calibration, but post hoc rules largely determine the final interval and do not fully use the learned output distribution. We observe that the resulting intervals have inherently hierarchical geometry: an interval can be recursively refined into nested subintervals, and binary trees naturally represent this structure. We formulate this hierarchy as next-interval prediction and propose PATH, which learns how probability mass flows from each interval to its next nested subintervals. PATH predicts a base leaf distribution and uses an autoregressive decoder to refine branch probabilities. Matching the distribution to the interval hierarchy aligns learning with extraction: PATH accumulates probability over adjacent output intervals and returns the shortest contiguous range reaching a selected mass. We compare PATH with 24 baselines for interval prediction on PATHBench, comprising 56 OpenML regression datasets. PATH substantially shortens the resulting intervals, achieving the lowest mean normalized length, 0.1473, while maintaining mean coverage of 0.9144. These results establish hierarchical output modeling as an effective approach for compact interval prediction on tabular data. Code is publicly available at this https URL.

---


### 107. [Adaptive Symmetry Discovery for Dynamical System Identification](https://arxiv.org/abs/2608.08091)

**<font color=#1a73e8>作者：</font>** Behrooz Tahmasebi, Melanie Weber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Dynamical systems model trajectory data generated by fixed underlying dynamics, with applications ranging from biology to physics. Especially in scientific settings, dynamical systems are not generic but often exhibit symmetries imposed by physical laws, formalized through equivariance with respect to group actions. The identification problem concerns recovering the parameters of a system from observed trajectories. In this work, we study adaptive symmetry discovery for dynamical system identification and address how a system can be identified from a single trajectory when it is equivariant with respect to an unknown symmetry group. To this end, we first show that for known symmetries, the system can be identified from a significantly shorter single trajectory than in the generic setting, and we precisely characterize this improvement. We then consider the automatic symmetry discovery setting, proposing a method to learn the symmetry group directly from a single trajectory and incorporate it into the identification procedure, achieving the same optimal trajectory length as in the known-symmetry case. Our analysis relies on tools from group representation theory and the expander properties of Cayley graphs, and may be of independent interest for the study of symmetries in dynamical systems.

---


### 108. [Support Selection Beyond Smooth DAG Exactness: Completion Geometry,Score Margins, and Selective Certificates](https://arxiv.org/abs/2608.08103)

**<font color=#1a73e8>作者：</font>** Rui Wu, Zongyuan Chen, Hong Xie  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Smooth acyclicity constraints answer whether a weighted support is a DAG, whereas structure learning asks which support change should be made. Existing analyses establish degeneracy for particular constraint formulas but do not isolate what follows from smooth exactness itself. At a DAG boundary, we show that minimal cycle completions generate a squarefree monomial ideal containing every restricted Taylor jet of an exact representation. If the smallest completion has $q$ edges, the first possible response has order $q$ for a vector residual and $2q$ for a nonnegative scalar. Exponentially many constant-scale cyclic manifolds exhibit the same lack of ranking away from the boundary for NOTEARS and DAGMA. We derive the exact selection time for an isolated cycle. When $\Psi'(h)\asymp h^\nu$, the feasibility-only time is $T_0(\varepsilon)=\Theta(\varepsilon^{-(2\nu+1)})$; a score margin changes the leading dynamics at scale $T_0^{-1}$ for $\nu>0$, while $\nu=0$ has a logarithmic boundary layer requiring $\gamma T_0\log(1/\varepsilon)\to0$. Experiments verify this law, and a truth-free separation statistic predicts selection time on 320 official NOTEARS/DAGMA trajectories (Spearman $-0.52$ and $-0.66$, permutation $p<10^{-4}$). For finite samples, a parent-set confidence family and forced-opposite queries certify skeleton and unshielded-collider labels shared by every population optimum of a frozen score. Across 320 runs, every regret bound covers an independent oracle-score audit. None of 3,042 certified skeleton or 2,396 collider labels disagrees with the oracle-score optimum, although 4.4% and 5.5%, respectively, disagree with the generating graph. These results separate DAG feasibility, score-based support selection, and causal identification.

---


### 109. [SCTD 3.0: Sonar Common Target Detection in the Wild - A Large-Scale, Multi-Scene Dataset from Real Marine Surveys](https://arxiv.org/abs/2608.08106)

**<font color=#1a73e8>作者：</font>** Peng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic Aperture Sonar (SAS) is core for wide-area detection of small underwater targets. However, large-scale, high-quality SAS datasets are scarce, hindering data-driven recognition. Existing benchmarks are small and limited to single scenarios, failing to reproduce complex acoustic scattering, diverse seabeds, and multi-pose imaging in real detection. To fill this gap, we introduce SCTD 3.0 - a large-scale real-measured dataset for Sonar Common Target Detection in the Wild in natural waters. It contains over 10,000 high-quality real SAS image snippets from multi-frequency systems (240 kHz, 450 kHz, and others), covering ten typical target categories across varied seabed geomorphologies, with multiple observation angles, detection ranges, and frequency bands. We establish a rigorous hierarchical annotation protocol that decouples labeling of intrinsic physical properties, deployment characteristics, and scattering phenomena - covering material, geometry, internal structure, burial state, shadow integrity, specular highlights, edge diffraction, and resonance effects. This enables fine-grained target characterization. We also construct a multi-task benchmark for object detection, fine-grained classification, and attribute prediction, evaluating mainstream deep learning models under cross-domain, cross-scene, cross-frequency, and cross-view generalization. SCTD 3.0 is expected to provide a critical data cornerstone for robust underwater target perception in open-water environments. SCTD 3.0 is available at this https URL.

---


### 110. [SUMI: Scalable Unified Model for 3D Point Cloud Inference](https://arxiv.org/abs/2608.08115)

**<font color=#1a73e8>作者：</font>** Yanlong LI, Kanchana Thilakarathna  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Point cloud completion commonly follows a coarse-to-fine paradigm, where a low-density coarse shape is first predicted and then upsampled to the target resolution. Although recent methods have improved global structure recovery, the fine stage often remains limited by simple upsampling and insufficient interaction with coarse structural features, making local detail reconstruction challenging. We propose SUMI, a diffusion-enhanced refinement module for coarse-to-fine point cloud completion. Unlike prior diffusion-based completion methods that use diffusion as a standalone point generator, SUMI injects noisy geometric features into cross-attention with coarse structural features, enabling reverse denoising to refine local geometry while preserving global consistency. SUMI can also be integrated into existing coarse-to-fine models as a flexible refinement module. Experiments on PCN, ShapeNet-55/34, and MVP demonstrate consistent improvements over strong baselines. SUMI achieves the best overall CD and F1-score on PCN, reduces CD by up to 16.1% on ShapeNet-55, and obtains the best CD across all output densities on MVP.

---


### 111. [TSDS-Toolbox: A Toolbox for Measuring Time-Series Dataset Similarity](https://arxiv.org/abs/2608.08119)

**<font color=#1a73e8>作者：</font>** Yen-Ku Liu, Hongjie Chen, Ryan A. Rossi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of artificial intelligence (AI) has significantly accelerated research in time-series analysis, particularly in forecasting, classification, and generation tasks. Recent models, especially foundation models, benefit from time-series dataset similarity due to its significant role in source dataset selection for fine-tuning. However, many existing implementations for benchmarking time-series dataset similarity methods are fragmented and difficult to extend. To address this, we present a unified framework, the Time-Series Dataset Similarity Toolbox (TSDS-Toolbox). Our work enables (1) systematic and reproducible comparisons of time-series dataset similarity methods; (2) flexible extensibility for users to add customized datasets, similarity methods, and downstream time-series tasks; and (3) consistent evaluation of both dataset-level and series-level similarity methods through integrated time-series dataset reducers. The effectiveness of TSDS-Toolbox is validated through comprehensive experiments under diverse experimental settings. Our toolbox is publicly available.

---


### 112. [Constraining ontology mappings using metaphysical choices](https://arxiv.org/abs/2608.08122)

**<font color=#1a73e8>作者：</font>** Giacomo De Colle, Helena Blackmore, Chris Partridge  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper we discuss the foundations behind a novel methodology for the validation of semantic mappings between different data sources based upon different foundation ontologies, where the methodology builds a framework based upon the metaphysical commitments of the ontologies. We provide as example the test case of mappings between IES and BFO, and we especially focused on providing cardinality constraints on the mappings between the two ontologies. In order to demonstrate the applicability of our method, we showcased how these principles can be operationalized through SPARQL queries validating the results of a mapping pipeline.

---


### 113. [Staying True to the Origin: Continuous Image Stylization with Smooth Transitions](https://arxiv.org/abs/2608.08125)

**<font color=#1a73e8>作者：</font>** Rui Xu, Hanmo Zhang, Songhua Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative models have achieved remarkable performance in text- and image-conditioned editing. However, preserving the content of a given image while referencing style patterns from another remains challenging, often leading to uncontrollable stylization results. In this paper, we approach image stylization from the perspective of continuous control, aiming to enable modern Diffusion Transformer (DiT)-based multi-reference editing models to (1) faithfully preserve the semantic structure of the content image, (2) render strong stylization effects, and (3) smoothly transition between the two. To this end, we propose a simple yet effective two-stage training strategy along with a style-strength-aware spline formulation. Specifically, in the first stage, the model is trained to produce strongly stylized outputs while preserving the content semantics as much as possible. In the second stage, with the base model frozen, we learn a set of anchor projectors that map various stylization strengths into the model parameter space. During inference, by performing style-strength-aware spline interpolation in a low-rank space, our method enables continuous control over stylization strength, even though the model is trained with only a few discrete strength levels. Extensive experiments demonstrate that our method supports precise and continuous manipulation of stylization strength while generating high-fidelity results with modern DiT models. Project page: this https URL.

---


### 114. [Understanding Security and Privacy Perceptions of Content Creators Regarding AI Labels of AI-Generated Content](https://arxiv.org/abs/2608.08129)

**<font color=#1a73e8>作者：</font>** Shuning Zhang, Hui Wang, Rongjun Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> AI labels, typically implemented via underlying tracing mechanisms such as watermarks and metadata, are crucial for protecting Artificial Intelligence-Generated Content (AIGC) against security threats like disinformation and evasion. However, the perceived devaluation of AI-assisted work discourages creators from disclosing AI use, incentivizing efforts to bypass labeling and compromising downstream traceability. Yet, how AIGC creators perceive the security and privacy (S\&P) implications of these labels, and how their behaviors impact technical resilience remain underexplored. To this end, we conducted semi-structured interviews with 21 AIGC creators and measured images across 6 image generation platforms against 16 self-reported manipulation settings. Our findings reveal that creators conflate binary AI labels with granular traceability, and express strong fears of de-anonymization via platform identifiers. Driven by fears of algorithmic traffic suppression and reputational risks, they defensively removed digital traces. Through empirical tests, we show that targeted modifications like coarse quantization significantly degrade detection. AI detection capabilities are also inconsistent across platforms, and suffer from false positives even for human-authored images. Based on these insights, we advocate for workflow-resilient implicit AI labels that align technical guarantees with creators' incentives.

---


### 115. [When Does An Extra View Help? Adapting Single-View 3D Reconstruction with Extra Imagery](https://arxiv.org/abs/2608.08132)

**<font color=#1a73e8>作者：</font>** Y Huynh, Duc Thanh Nguyen, Thao Minh Le 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reconstruction of 3D objects from a single image is a challenging research problem in computer vision. The key challenge is the lack of critical information from viewpoints to complete 3D structures. Using an additional view may help to resolve the issue. However, there is no mechanism that can integrate the extra view into the single-view 3D reconstruction principle. We address this challenge by proposing ASV3D, a framework for adapting single-view 3D object reconstruction to test-time data with support from one additional image. We introduce two adaptation strategies: (i) a zero-shot adaptation scheme that leverages the auxiliary image to improve the reconstruction quality of an object without retraining, and (ii) an optimised adaptation scheme that further enhances visual fidelity and cross-view consistency via contrastive learning. We apply our ASV3D to improve two state-of-the-art single-view 3D reconstruction pipelines on both benchmark and real-world datasets. Results demonstrate that our approach consistently improves reconstruction accuracy and robustness under unconstrained multi-view inputs, outperforming the baselines in both quantitative metrics and human preference. We publish our code and the real-world object dataset in our project page at this https URL.

---


### 116. [Compositional Cross-Modality Translation via Whole-Volume Multitask Latent Flow Matching](https://arxiv.org/abs/2608.08135)

**<font color=#1a73e8>作者：</font>** Daniele Molino, Alessio Zoboli, Camillo Maria Caruso 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-modality medical image translation can reduce the burden of multi-modal acquisitions, yet the field remains constrained by two coupled limitations: methods operate on 2D slices or 3D patches rather than whole volumes, and train a separate model for each translation task. Both stem from a single cause, the absence of a sufficiently strong volumetric prior, which forces generative models to learn anatomical appearance and cross-modality mapping simultaneously, an ill-posed problem at the scale of available paired datasets. We propose to decouple these objectives. A large-scale pretrained 3D variational autoencoder provides a compact latent representation of volumetric appearance, reducing translation to a conditional flow-matching problem. This compression makes whole-volume processing tractable, while a resolution-aware sampling strategy preserves native anatomical scale. We train a single model jointly across inter-modality (MRI$\to$CT, CBCT$\to$CT) and intra-modality (MRI$\to$MRI) tasks over three multi-center datasets. Across all tasks, whole-volume processing outperforms its patch-based counterpart, and the multi-task model matches task-specific baselines while replacing $N$ networks with one. Crucially, joint training unlocks capabilities inaccessible to task-specific approaches: zero-shot generalization to anatomical regions unseen during training, within 0.15 SSIM of the fully supervised model, and compositional cross-dataset translation along paths never directly supervised. These results suggest that combining a strong volumetric prior with multitask training is a scalable route toward synthesis systems that generalize beyond their training distribution. Code is available at this https URL.

---


### 117. [Learning Structural Illumination for Unsupervised Low-light Enhancement](https://arxiv.org/abs/2608.08153)

**<font color=#1a73e8>作者：</font>** Tianle Du, Peiyuan He, Hainuo Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing unsupervised low-light image enhancement (LLIE) methods often estimate illumination directly from the entire low-light input, without separating its spatially varying illumination pattern, termed relative illumination structure, from the absolute exposure level or preventing unreliable low signal-to-noise ratio regions from biasing the estimate. Moreover, fixed exposure targets impose a scene-agnostic enhancement criterion, limiting adaptation across diverse lighting conditions. Inspired by the spatial propagation of light, we propose a Relative Illumination Structure Estimation (RISE) framework that decouples relative illumination structure from absolute exposure and infers it from reliable bright regions, enabling interpretable and robust enhancement. For scene-adaptive exposure adjustment, we further propose a Dual-Metering Exposure Reference derived from each input, allowing RISE to adapt the enhancement strength to individual scenes and generalize across diverse lighting conditions. Extensive benchmark and real-world generalization experiments show that RISE achieves state-of-the-art performance among unsupervised LLIE methods while producing visually natural results.

---


### 118. [A Unified Framework for Dynamic Reward Shaping in Reinforcement Learning](https://arxiv.org/abs/2608.08158)

**<font color=#1a73e8>作者：</font>** Fouad Bahrpeyma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse, delayed, and weakly informative rewards remain central obstacles to efficient reinforcement learning. Reward shaping addresses these limitations by supplementing the task reward with an auxiliary signal that can accelerate learning while, in the classical setting, the original objective remains the evaluation criterion. Established theory guarantees safety for fixed shaping signals: potential-based reward shaping preserves optimal policies when the auxiliary term is the discounted difference of a time-invariant potential. In contemporary reinforcement learning systems, however, both the learner and the information available for guidance evolve during training: value estimates improve, novelty diminishes, feedback shifts, and predictive models are refined. Adaptive reward mechanisms occur across exploration, Bayesian inference, human-in-the-loop learning, automated reward design, and foundation-model-based approaches. This study introduces a unified analytical framework for comparing dynamic reward shaping and neighbouring adaptive reward mechanisms. The proposed framework distinguishes parametric revision from state-dependent variation, separates additive shaping from reward replacement and reward-adjacent guidance, and organises existing methods along temporal, informational, and theoretical dimensions. Using this framework, twelve method families are comparatively analysed. The framework further highlights the conditions under which optimality guarantees survive contemporary deep reinforcement learning pipelines, replay buffers, bootstrapped critics, and reward normalisation, while exposing the unresolved relationship between adaptation rate and learner stability.

---


### 119. [Predicting blood clot growth from sparse post-onset measurements with latent neural differential equations](https://arxiv.org/abs/2608.08165)

**<font color=#1a73e8>作者：</font>** Lennon J. Shikhman, Ying Qian, He Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Computational models of blood clotting improve understanding of thrombus formation, but their clinical application remains limited because many model inputs are difficult to measure and patient-specific data are often sparse. We present a computational framework based on latent neural differential equations that infers unknown model parameters from sparse measurements and forecasts thrombosis progression. We demonstrate the framework using data generated from a multiphysics blood-clotting model in which clot growth is governed by the coagulation cascade and diffusion. Four known biochemical inputs (fibrinogen and factors IX, VIII, and V), together with sparse early clot-size observations, are used to infer the tissue-factor parameter and predict subsequent clot growth. We compare seven probabilistic methods: stochastic neural ordinary differential equations (SNODE), stochastic neural functional differential equations (SNFDE), a latent neural-process baseline, a monotone probabilistic deep ensemble, empirical trajectory retrieval, PCA-ridge Gaussian posterior, and Gompertz-curve retrieval. SNODE achieved the best performance in inferring the unknown input and forecasting future clot-growth trajectories. SNFDE performed similarly and consistently outperformed the other non-differential models. Prediction accuracy improved as more observations became available, whereas longer forecasting horizons increased uncertainty and decreased accuracy. Latent neural differential equations thus effectively combine parameter inference and clot-growth forecasting from sparse measurements, providing a promising foundation for personalized thrombosis modeling.

---


### 120. [AOC-CBS: Anytime-Optimal Continuous-time Conflict-Based Search for Generalised Multi-Agent Path Finding](https://arxiv.org/abs/2608.08175)

**<font color=#1a73e8>作者：</font>** Alvin Combrink, Sabino Francesco Roselli, Martin Fabian  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Many research fields share a common structure: a set of agents, each pursuing its own goal, whose actions must be coordinated so that no two of them conflict. Multi-Agent Path Finding (MAPF) is a concrete instance of this structure, with applications from warehouses to road traffic and airports. Much of MAPF research assumes discrete time, circular agents sharing one spatial graph, a single goal per agent, and that an agent must remain at its goal once reached, precluding heterogeneous fleets, non-geometric conflicts, task sequences, and agents that move on after completing them. We generalise the MAPF formulation to lift these assumptions, and present Anytime-Optimal Continuous-time Conflict-Based Search (AOC-CBS), an exact and solution-complete solver for it. AOC-CBS guarantees the eventual return of an optimal solution, while reporting an incumbent with a known optimality gap upper bound throughout its runtime; it is configurable with a portfolio of repair functions, one of which we introduce (Tier-Prioritized Safe Interval Path Planning), and can exploit multiple processor cores. We demonstrate AOC-CBS on a mixed fleet of non-convex agents moving along smooth, kinodynamically feasible trajectories. Preliminary experiments against the exact solver OC-CBS, on well-known benchmarks and roadmaps we sample from them, show AOC-CBS is comparable at finding optimal solutions while extending scalability from the tens to the hundreds of agents when a bounded optimality gap is accepted.

---


### 121. [A Grounded and Decomposed Framework for Relation-Level Hallucination Evaluation in Abstractive Summarization](https://arxiv.org/abs/2608.08180)

**<font color=#1a73e8>作者：</font>** Praveen Kumar Katwe, Rakesh Chandra Balabantaray, Kali Prasad Vittala 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Abstractive text summarization systems frequently generate fluent yet unfaithful summaries by fabricating or distorting relationships between entities and
events. Such relation-level hallucinations undermine the reliability of generated summaries, particularly in high-stakes domains. In this work, we present a
refined and grounded framework for evaluating relation hallucination in abstractive summarization. We present the empirical Relation Hallucination Index (RHI) by
introducing a dependency-aware relation extraction algorithm that incorporates lemmatization-based normalization, named entity grounded subject resolution,
passive agent recovery, negation-aware verb modeling, reporting verb filtering, nominal relation fallback, clausal propagation, and systematic deduplication.
These enhancements improve the structural fidelity of extracted relation triples and reduce spurious matches during evaluation. In addition, we introduce a
normalized formulation of RHI to ensure scale-invariant comparison between datasets and models. The revised metric decomposes hallucination into interpretable
components, aggregates relation hallucination metric into a normalized relation faithfulness score. Extensive evaluation across multiple state-of-the-art
summarization models demonstrates that the grounded extraction process yields more stable and discriminative hallucination measurements. The proposed framework
advances automated relation-level faithfulness evaluation and supports coherence-aware, hallucination-sensitive model analysis.

---


### 122. [Biologically Informed Representation Learning for Robust Cross-Center Generalization of MALDI-TOF Mass Spectrometry](https://arxiv.org/abs/2608.08182)

**<font color=#1a73e8>作者：</font>** Alejandro L. García-Navarro, Carlos Sevilla-Salcedo, Belén Rodríguez-Sánchez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models for MALDI-TOF mass spectrometry have shown considerable promise for clinical microbiology tasks such as microbial identification and antimicrobial resistance prediction. However, their deployment across institutions remains limited by domain shift, as acquisition-specific variability often leads models to capture technical artifacts rather than transferable biological information. Existing representation learning approaches primarily address this problem through statistical domain alignment while largely overlooking the biological supervision naturally available in microbiology datasets. We introduce DALMA, a probabilistic representation learning framework that jointly models acquisition-specific variability and biological supervision to learn biologically structured latent representations. By combining domain-specific reconstruction with biologically guided representation learning, DALMA learns transferable representations that generalize across heterogeneous clinical centers without requiring institution-specific components at inference, enabling zero-shot deployment on previously unseen sites. We evaluate DALMA on a multi-center benchmark comprising seven datasets from three countries. DALMA consistently achieves state-of-the-art zero-shot microbial identification across two held-out clinical centers, while the learned representations also transfer effectively to antimicrobial resistance prediction. Furthermore, latent-space novelty estimation enables reliable selective prediction under previously unseen domain shifts. These results demonstrate that biologically informed representation learning provides an effective strategy for robust and transferable ML in clinical microbiology.

---


### 123. [Large Multimodal Agents for Intelligent Transportation Systems: Architectures, Evidence, and Deployment Challenges](https://arxiv.org/abs/2608.08184)

**<font color=#1a73e8>作者：</font>** Muhammad Ayub Sabir, Shaohong Zheng, Zhiyu Qu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large multimodal agents (LMAs) are increasingly proposed for intelligent transportation systems (ITS), but existing studies often conflate multimodality, agency, empirical performance, and deployment readiness. This review provides an auditable evidence map of 42 primary study families released between January 2023 and 3 August 2026 within a corpus of 91 mapped sources. It distinguishes model-level, system-level, and hybrid multimodality and classifies each family by system architecture and action authority. Evidence is assessed independently through functional capability (C0-C3), validation setting (E0-E4), three evidence propositions (P1-P3), and eight methodological-concern domains (Q1-Q8). Transportation semantics (P1) are directly evaluated in 23 families and multidimensional integration (P3) in 24; 19 families directly evaluate both. Evidence reconciliation (P2) remains unresolved because no family demonstrates the complete provenance-challenge-handling-comparison-outcome chain. Fourteen families reach C3, but 13 remain at E2; only one reaches E3 and none reaches E4. Across ITS domains, LMAs are best supported for semantic interpretation, intent translation, evidence organisation, scenario authoring, explanation, and specialist-tool coordination. Numerical forecasting, optimisation, simulation fidelity, hard constraints, low-level control, safety fallback, and final authority should remain with independently verifiable specialist systems or accountable humans. The review therefore supports bounded orchestration rather than replacement and provides a matched comparative evaluation protocol and staged roadmap for accountable deployment. The living evidence repository is available at this https URL.

---


### 124. [BAP-MOS: Bandit-Based Adaptive Prompting for Boundary-Sensitive Multi-Organ Segmentation](https://arxiv.org/abs/2608.08191)

**<font color=#1a73e8>作者：</font>** Satvik Praveen, Shengji Jin, Ahmed Lamidi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-organ ultrasound segmentation remains challenging when anatomically adjacent structures must be delineated jointly, as localized boundary errors can persist even when Dice scores are high. To address these challenges, we propose Boundary-Adaptive Prompting for Multi-Organ Segmentation (BAP-MOS), a closed-loop adaptive prompting framework. BAP-MOS formulates prompt selection as an organ-specific multi-armed bandit problem over box, point, and combined prompts. An outer Tree-structured Parzen Estimator (TPE) loop selects the prompt-selection parameter vector, while an inner UCB-Tuned loop adapts per-organ prompt preferences during fine-tuning using a bounded Dice--MSD--HD95 validation-probe reward. The framework further introduces an organ-scaled negative prompt ring to adapt sparse prompt geometry across anatomical scales, while keeping the image and prompt encoders frozen and updating only the mask decoder. We evaluate BAP-MOS on pooled prostate-region TRUS cohorts against U-Net, nnU-Net, MedSAM, fixed-prompt SAM/MedSAM, and adaptive policy variants. On this benchmark, BAP-MOS achieves Dice 0.982, HD95 0.482, and MSD 0.204, reducing HD95 by approximately 48% and MSD by 45% relative to the strongest conventional baseline. To verify the generalization ability of the framework, we tested it on the external PFUS1 pelvic-floor ultrasound corpus using MedSAM and its adaptive strategy variants, and the results were good. These results support adaptive prompt allocation as an effective mechanism for improving boundary-sensitive multi-organ ultrasound segmentation without modifying the foundation-model backbone. Source Code is available at: this https URL

---


### 125. [A Minimal $κ$--$τ$ Logic for Risk-Sensitive Abduction](https://arxiv.org/abs/2608.08192)

**<font color=#1a73e8>作者：</font>** Remo Pareschi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Standard approaches to abductive reasoning can retain multiple candidate explanations, but they do not generally combine explicit compositional cross-hypothesis interaction with an internal, rival-sensitive commitment judgment. This paper argues that in risk-sensitive domains -- where premature commitment carries asymmetric downside costs -- the timing of commitment is itself a governed decision that the inferential apparatus should formally represent. We present a minimal $\kappa$--$\tau$ logical framework built on two primitives: epistemic interaction among hypotheses ($\kappa$) and a normative commitment threshold ($\tau$). Hypotheses may coexist, reinforce or inhibit one another, and form emergent composite explanations, while collapse into committed conclusions is regulated by governance constraints rather than forced by inference alone. The logic is developed in two complementary modes sharing the interaction relation and the governance apparatus: a synthetic mode, in which atomic hypotheses are composed upward into emergent explanations, and an analytic mode, in which complex observed states of affairs are decomposed into causal clusters of latent factors, with commitment governed at both the cluster and the factor level. The framework provides formal machinery for domains in which the distinction between highly likely and commit-worthy is operationally consequential. The $\kappa$--$\tau$ logic is positioned as the symbolic governance layer of a neurosymbolic architecture: its epistemic parameters are naturally estimated by neural components -- semantic embeddings and generative models, as demonstrated in existing computational realizations -- while its normative parameters remain under explicit human governance, yielding transparent and auditable abductive reasoning for deployment in high-stakes settings.

---


### 126. [Beyond Aggregate Calibration: Decomposing Income-Conditional Recall Disparities in Automated Credit Default Prediction](https://arxiv.org/abs/2608.08202)

**<font color=#1a73e8>作者：</font>** Sai Srikar Boddupalli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-centric curation pipelines frequently rely on model confidence scores to flag and filter noisy or mislabeled training instances. Evaluating this filtering convention on a large-scale consumer lending sample (LendingClub, N = 1,344,936) uncovers an underlying demographic asymmetry: high-income defaulters are disproportionately classified as label noise relative to low-income defaulters (Cramer's V approximately 0.03-0.07). Re-examining this behavior through the lens of equal opportunity [Hardt et al., 2016] reveals a far more severe discrepancy: a 16.86 percentage point gap in true positive rate (recall) between high- and low-income borrowers who ultimately defaulted. Implementing a sequential feature-blinding methodology allows us to isolate the drivers of this disparity across three distinct mechanisms: (1) direct reliance on self-reported applicant income; (2) algorithmic absorption of upstream institutional bias encoded within origination interest rates; and (3) a residual disparity (3.55 percentage points in cross-validation; 2.56 percentage points on a held-out test partition, Z = -4.04, p < 0.0001) that remains even after purging both income and interest rates from the model. Out-of-sample signed SHAP valuations demonstrate that this residual gap is maintained by structural proxies, most notably loan amount and home ownership status. These empirical findings show that simply blinding an algorithm to sensitive attributes fails to ensure fairness when institutional pricing decisions and behavioral proxy variables collectively reconstruct the omitted signals. We outline the practical implications of these findings for auditing data-centric AI workflows within regulated financial institutions.

---


### 127. [FreSH: Frequency-Segmented Hierarchical Multi-Expert Framework for Multivariate Time Series Classification](https://arxiv.org/abs/2608.08207)

**<font color=#1a73e8>作者：</font>** Pingping Liu, Muyao Wang, Zijian Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate Time Series Classification (MTSC) demands models that can effectively capture complex temporal patterns across multiple scales while remaining computationally efficient. However, existing approaches generally struggle to reconcile fine-grained representation learning, especially under class imbalance and real-world constraints. In this paper, we present FreSH, a Frequency-Segmented Hierarchical Multi-Expert Framework designed to address these challenges. FreSH introduces a new perspective for MTSC by enabling adaptive, multi-scale analysis of temporal signals, allowing different aspects of the data to be modeled in a complementary and coordinated manner. By combining localized specialization with holistic context modeling, FreSH achieves strong representational capacity without incurring excessive computational overhead. An adaptive fusion strategy further enhances flexibility, enabling the model to dynamically emphasize the most informative components of the input. In addition, we incorporate a more robust optimization objective that improves learning stability across varying sample difficulties and class distributions. Extensive evaluations on 30 UEA benchmark datasets and real-world vibration data demonstrate that FreSH consistently outperforms state-of-the-art methods in classification accuracy, while substantially reducing model size and efficiency.

---


### 128. [VTO: Visual Tool Orchestration for Video Anomaly Detection](https://arxiv.org/abs/2608.08219)

**<font color=#1a73e8>作者：</font>** Rui Wang, Yeteng Wu, Xianling Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video anomaly detection (VAD) is a critical yet challenging task due to the complex and diverse nature of real-world scenarios. Traditional deep learning approaches are fundamentally limited by poor generalization across diverse scenarios. While multimodal agents offer a promising tool-learning paradigm for VAD, current systems relying on supervised fine-tuning struggle with complex orchestration, and standard reinforcement learning often causes premature termination due to coarse-grained outcome rewards. To address these challenges, we propose VTO, a process-supervised reinforcement learning framework. Moving beyond static tool usage, VTO enables the agent to dynamically explore and interact with the environment. Specifically, we introduce a foundation model-driven cognitive evaluator to provide context-aware semantic feedback, which is seamlessly integrated into a Process-Supervised Cognitive Alignment that delivers fine-grained, step-wise supervision. By explicitly penalizing logical truncation and rewarding complete causal chains, the agent optimizes its multi-step reasoning policy for interrelated tool orchestration. To support our proposed framework, we meticulously crafted VAD-Tool, a hierarchical visual tool set comprising 12 specialized vision tools spanning from entity tracking to high-stakes hazard detection, and established the corresponding benchmark for rigorous multi-step reasoning evaluation. Extensive experiments on VAD-Tool demonstrate that VTO significantly outperforms baselines, achieving up to a 10.2\% absolute accuracy improvement in tool scheduling. Code and data are available at this https URL.

---


### 129. [Metanormative Theory for RL-Based Moral Agents](https://arxiv.org/abs/2608.08220)

**<font color=#1a73e8>作者：</font>** Aleks Knoks, Marija Slavkovik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The overlapping disciplines of machine ethics and value alignment are concerned with designing artificial agents that are aligned with human values and that act in ethically acceptable ways. A recent trend in these disciplines is the use of reinforcement learning (RL) to design such agents, sidelining the philosophical literature that used to play a more central role. Against this backdrop, this paper pursues two goals. The first is to draw out ideas from recent work in metanormative theory that can be useful for designing artificial moral and value-aligned agents. The second is to examine the RL architecture through the lens of these ideas. This will give us clearer criteria for when an RL agent's behavior can be classified as moral, as well as a basis for evaluating and comparing different RL-based approaches to machine ethics and value alignment.

---


### 130. [A Fair Objective for Human-Empowerment-Preserving AI: Desiderata, Design, and Likely Behavioral Consequences](https://arxiv.org/abs/2608.08240)

**<font color=#1a73e8>作者：</font>** Jobst Heitzig, Ram Potham  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper explores the idea of promoting well-being and safety in human-AI interactions by forcing AI agents explicitly to empower humans and to manage the power balance between humans and AI agents in a desirable way. Using a principled, partially axiomatic approach based on desirable properties, we design a parametrizable and decomposable objective function for AI systems that represents an inequality- and risk-averse long-term aggregate of human power. It can take into account models of human bounded rationality and social norms, and crucially, considers a wide variety of possible human goals. We prove how certain desiderata enforce particular functional forms and restrict parameter ranges. We exemplify the consequences of softly maximizing this metric in several paradigmatic situations and describe what instrumental sub-goals it will likely imply.

---


### 131. [Underwater MMG-Based Muscle State Monitoring with Integrated Emergency Buoyancy Assistance](https://arxiv.org/abs/2608.08263)

**<font color=#1a73e8>作者：</font>** Xiao Jin, Yixian Fan, Zefeng Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> This paper presents an underwater MMG-driven wearable emergency assistance system for lower-leg muscle-state monitoring and automatic buoyancy deployment. A compact microphone-based MMG sensor was waterproofed using a flexible 5 mil PE membrane, preserving identifiable muscle-vibration responses under immersion, depth variation, and stirring disturbances. Two lower-leg sensors captured stroke-dependent MMG patterns across four swimming styles, and a MiniRocket classifier achieved 91.91% window-level and 97.56% file-level accuracy. For cramp-related monitoring, a pattern-based risk score was used to identify representative pre-cramp abnormal muscle-state transitions during rhythmic motion. A controlled underwater test demonstrated the closed sensing--decision--actuation chain, triggering CO_2 release, airbag inflation, and flotation in less than 5~s. These results support underwater MMG as a sensing basis for wearable robotic emergency assistance in aquatic environments.

---


### 132. [Design Knowledge in Data Visualization: Mapping the Epistemic Landscape](https://arxiv.org/abs/2608.08270)

**<font color=#1a73e8>作者：</font>** Paul C. Parsons, Colin M. Gray, Ali Baigelenov  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data visualization research has developed many influential forms of design knowledge, including perceptual principles, design guidelines, process models, and formalized representations of design constraints. These contributions have been effective at articulating explicit, portable, and codified forms of knowledge. Yet the broader landscape on which visualization design depends remains less clearly articulated, especially with respect to intermediate-level knowledge, precedents, tacit repertoires, and situated forms of knowing. In this paper, we draw on design theory to map this broader landscape of design knowledge in data visualization. Through this lens, we show how visualization research has built substantial strengths in some regions while leaving others comparatively underarticulated. We further argue that visualization design depends not only on knowledge artifacts such as theories, guidelines, and patterns, but also on knowledge-in-use---the situated interpretation, adaptation, and coordination of multiple forms of knowing in concrete design situations. This broader account has implications for how the field conceptualizes design expertise, evaluates and develops scholarly contributions, and approaches AI-assisted design. Rather than treating visualization design as either fully formalizable or wholly resistant to computational support, we argue for a differentiated view in which computational systems can support some forms of design knowing, while others remain inseparable from human judgment, contextual interpretation, and the ongoing reorganization of design work in practice.

---


### 133. [Situatedness in Visualization Design: Making Unresolved Work Actionable](https://arxiv.org/abs/2608.08274)

**<font color=#1a73e8>作者：</font>** Paul C. Parsons, Prakash Shukla, Phuong Bui 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Visualization design often proceeds under unresolved conditions---goals shift, data remain provisional, stakeholder needs evolve, and several plausible directions may remain available at once. Existing visualization frameworks help organize design work and articulate major decisions, yet offer limited explanation of how practitioners proceed before a path forward has become clear. Drawing on an episode-level analysis of a previously collected three-phase qualitative corpus involving eleven expert visualization practitioners, we examine situations in which the problem, representational target, or viable direction remained unsettled. We find that practitioners make such situations actionable through provisional local moves. These moves reveal patterns, distinctions, and interpretive possibilities; clarify what is tractable, viable, or worth pursuing; and sometimes reorient the work itself. The analysis shows that situated action, professional judgment, and explicit design reasoning are intertwined in expert practice. It also identifies a practical limit on how fully design activity can be specified in advance. When the meaning of the next move depends on what a situation reveals in response to action, prescriptive decision structures cannot fully determine the course of design. The paper contributes an empirical account of situatedness in visualization practice and explains how local action makes unresolved work interpretable enough for consequential design decisions.

---


### 134. [Ego-OSCAR: Egocentric Open source Stereo CAptuRe System](https://arxiv.org/abs/2608.08285)

**<font color=#1a73e8>作者：</font>** Gunjan Paul, Senthil Palanisamy, Satpal Singh Rathore 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Ego-OSCAR, an open-hardware, low-cost, head-mounted stereo-inertial capture device for egocentric data collection in the wild. EgoOSCAR pairs a hardware-synchronized global-shutter stereo camera with a 6- axis IMU, an embedded Linux SBC for on-device video encoding, and a realtime microcontroller for user feedback and watchdog functions. The complete bill of materials is under USD 200 per unit, using only commercially available components and 3D-printed parts. Alongside the device, we release a complete software stack (hardware-accelerated recording pipeline, IMU sampling daemon, time-synchronization tooling, and watchdog firmware) and roughly 550 hours of egocentric stereo video per camera with synchronized IMU, collected by a distributed contributor network across everyday indoor environments. The release is annotated rather than raw: free-form action captions cover essentially the entire recorded timeline with an open vocabulary, and per-frame 3D hand reconstructions ship alongside per-session stereo calibration. Ego-OSCAR does not aim to match the per-unit fidelity of research-grade systems such as Project Aria; it aims to be the cheapest defensible substrate for crowdsourced egocentric capture, and to lower the activation energy for any team that wants to collect egocentric data at scale. All hardware designs, software, and the dataset are open-sourced

---


### 135. [What Irregularity Costs: CUDA C++, Rust, and Triton on a Hash-Blocked GPU Workload](https://arxiv.org/abs/2608.08287)

**<font color=#1a73e8>作者：</font>** Petr Korolev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> GPU language comparisons are almost always run on tiled dense linear algebra, where every toolchain is good and the differences are small. We implement the same hash-blocked TSDF fusion kernel in CUDA C++, in Rust through NVIDIA's cuda-oxide, and in Triton, and measure it on a workload with the opposite character: an open-addressed hash table with compare-exchange insertion, data-dependent per-lane probe depth, and contended scatter.
The result is a split. On the regular stage, which walks a truncation band and accumulates, all three languages land within a small factor of each other. On the irregular stage, which probes and inserts, Rust stays close to hand-written CUDA C++ while Triton is more than an order of magnitude slower. Language choice is nearly free on the work that is usually benchmarked and expensive on the work that is not.
We attribute both gaps to specific things the languages cannot express, not to ratios. Triton's cost follows from a probe loop that must run to a compile-time bound and from tl.atomic_cas taking no mask, which forces a scratch structure with no counterpart in CUDA. Rust's cost was invisible in every instruction count: its kernel issues fewer instructions, fewer compare-exchanges and fewer registers at identical occupancy, yet was slower. Hardware counters located it in L1 residency. A GPU-scope atomic load must be coherent across SMs, no NVIDIA L1 is, so the type-correct way to read a shared location bypasses the cache on every access.
Triton's bounded probe is also a correctness problem for fusion: at load factors an ordinary depth trajectory reaches, it silently discards blocks and the reconstruction loses patches of surface with nothing reported. We also report a defect found and fixed in cuda-oxide itself, now merged upstream: its scoped atomic load and store could not be called at all in the build mode that produces real kernels.

---


### 136. [Causal State-Space Model for Causal Inference: Estimating Longitudinal Individual Treatment Effects](https://arxiv.org/abs/2608.08288)

**<font color=#1a73e8>作者：</font>** Abisoye Abidakun, Mingjun Zhong, Georgios Leontidis  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Estimating counterfactual outcomes over time from longitudinal observational data is central to clinical decision support. Existing methods rely on domain confusion -- adversarial training that renders representations invariant to treatment assignment -- yet this invariance creates a mutual information conflict: it suppresses treatment-correlated covariate signals necessary for accurate outcome prediction. We formalise this tension via a Jensen-Shannon divergence bound on counterfactual prediction error and develop two complementary models. CSSD (Causal State-Space model with Direct decoder) adapts selective State Space Models with a parallel multi-step decoder that eliminates accumulated rollout error by producing all prediction horizons simultaneously in a single forward pass. CSSPD (Causal State-Space model with Predictive regularisation and Direct decoder) augments CSSD with Contrastive Predictive Coding and Local Information Maximisation to reinforce temporal predictability in the balancing representation and recover local covariate information destroyed by domain confusion. On MIMIC-III, CSSPD achieves lower counterfactual RMSE than the Causal Transformer at every horizon tau >= 2 at O(T) encoder cost, with gains from 0.02 (2-step) to 0.07 (6-step). On Cancer Simulation across confounding strengths gamma in {0,1,2,3,4}, CSSPD outperforms CT at gamma <= 3 (margins 25.9%--37.0%), and CSSD achieves the lowest overall average RMSE (12.7% reduction over CT), confirming the MI conflict analysis. To our knowledge, this is the first work to formalise the balancing-prediction MI conflict and propose a structured resolution through complementary predictive and information-theoretic training objectives.

---


### 137. [Test-Time Prototype Adaptation for Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2608.08290)

**<font color=#1a73e8>作者：</font>** Haozhe Wang, Jintao Cheng, Weibin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation (OVSS) repurposes a pretrained CLIP encoder for dense prediction without additional labeled supervision. Existing methods improve CLIP's spatial behavior either by redesigning its internal attention or by injecting features from auxiliary vision foundation models; both require access to the host's internal computation and are tailored to its specific forward pass. In this work, we propose Test-time Prototype Adaptation (TPA), a training-free plug-in that operates at the output level, leaving the host's forward pass and weights unmodified. By leveraging a lightweight transductive adaptation phase, TPA identifies confident anchor patches from the host's own output predictions on a small pool of unlabeled deployment-domain images, and aggregates their frozen DINO features into per-class prototypes; at inference, a single cosine similarity lookup against this frozen bank provides an auxiliary score fused linearly with the host's logits. TPA composes with five representative OVSS hosts spanning attention-redesign and VFM-injection designs, across three CLIP backbones, eight benchmarks, and multiple internal VFM choices. Under a single set of hyper-parameters and without per-host tuning or parameter updates, TPA consistently improves segmentation accuracy, with as few as approximately 10% of unlabeled deployment-domain images sufficing for effective bank construction on most benchmarks.

---


### 138. [A Controlled Study of Feature-Based Knowledge Distillation Across Student Designs](https://arxiv.org/abs/2608.08294)

**<font color=#1a73e8>作者：</font>** Abhinand Balachandran, Praveen Prashant  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Knowledge distillation trains a smaller student to match the outputs of a larger teacher. Feature-based methods also align intermediate representations, but this extra constraint may affect students differently. We study this question on CIFAR-100 using a ResNet-50 teacher, a width-controlled CustomResNet family and MobileNetV2 as a cross-design comparison. For each student, we evaluate each feature method against a matched logit-KD run using the same teacher, optimizer settings, training schedule and seed. We repeat the main comparisons across multiple seeds.
Logit KD improved every tested student over its scratch baseline. Attention Transfer showed no clear relationship with size inside the CustomResNet family, but its average effect was negative for that family and positive for MobileNetV2. FitNets was below logit KD in all 15 paired runs. Within the constant-depth width sweep, its gap increased for wider students, although the different-depth w=48 student did not follow this trend. Finally, the same auxiliary coefficient produced different gradient scales across students, showing that a fixed coefficient does not create a uniform training condition.

---


### 139. [Machine-Learning-Based Diagnostic Framework for Passive Ultrasonic Detection of Railway Wheel Defects](https://arxiv.org/abs/2608.08301)

**<font color=#1a73e8>作者：</font>** Aashish Shaju, Steve Southward, Mehdi Ahmadian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable identification of railway wheel defects is important for safety and maintenance. This study develops a machine-learning-based diagnostic framework for multi-class defect identification using passive air-coupled ultrasonic acoustic emission signals. Data were collected from eleven full-scale railway wheelsets representing nine health states. Time- and frequency-domain features were evaluated using Kruskal-Wallis statistical testing and mutual-information analysis to identify the most discriminative indicators. A Random Forest classifier was then trained using the selected features with stratified 5-fold cross-validation. The model achieved a balanced accuracy of approximately 0.66 and a Macro-F1 score of 0.65 across the nine classes. Decay rate, kurtosis, skewness, and envelope low-frequency power emerged as the most influential features, while a compact subset of features retained most of the classification performance. The results demonstrate the feasibility of combining passive ultrasonic sensing, statistical feature selection, and supervised machine learning for non-contact railway wheel defect classification and provide a foundation for future field-deployable inspection systems.

---


### 140. [Frequency-Domain Dual-Branch Fusion for Medical Visual Question Answering](https://arxiv.org/abs/2608.08307)

**<font color=#1a73e8>作者：</font>** Yusra Tariq, Rakesh Chandra Joshi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Visual Question Answering (VQA) requires aligning subtle visual evidence, including lesion texture, boundary sharpness, and diffuse density changes, with clinical language. Existing multimodal fusion approaches operating in the spatial domain may not fully exploit complementary frequency information present in visual and textual representations. We introduce a dual-branch frequency-domain fusion module that conditions spectral filtering on the input question, enabling adaptive selection of global low-frequency structure and fine-grained high-frequency detail before reconstructing the spatial representation for answer generation. To provide a richer spectrum for filtering, we extract complementary features from early texture-sensitive and final semantic layers of a frozen BiomedCLIP encoder and align both with the question representation using a symmetric InfoNCE objective prior to staged joint training with a BioBART decoder. We pretrain the proposed model on PMC-VQA and fine-tune it on the VQA-RAD and SLAKE benchmarks, demonstrating that frequency-aware multimodal fusion improves medical VQA performance while maintaining a lightweight and efficient architecture.

---


### 141. [Open-World Semantic Segmentation with Sensitivity Modeling](https://arxiv.org/abs/2608.08308)

**<font color=#1a73e8>作者：</font>** Anastasios Romanos Varvarigos, Nikos Giakoumoglou, Tania Stathaki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern vision systems must operate in "open-world" settings, where models must recognize known categories and detect unseen or anomalous content. Conventional semantic segmentation models operate under a "closed-world" assumption, often producing overconfident misclassifications on novel content. We address open-world semantic segmentation, the joint task of segmenting known classes while detecting and grouping novel or anomalous content without additional supervision, by extending a dual-decoder baseline with a third, complementary decoder within a unified encoder-decoder design. The first decoder performs closed-set segmentation using Gaussian prototypes for known categories. The second uses contrastive feature learning to isolate unknown regions in embedding space. The third, our key contribution, is a sensitivity decoder that captures fine-grained texture irregularities and activation instabilities indicative of semantic uncertainty, which neither semantic prototypes nor contrastive norms can reliably detect. The three decoders provide genuinely complementary signals: class-level OOD distance in logit space, global feature energy in embedding space, and local activation instability across encoder scales. Experiments on Cityscapes and BDD-Anomaly show that our method improves anomaly segmentation and novel-class discovery while maintaining competitive closed-set accuracy, with gains of +2.4% AUROC and a 2.5 pp. reduction in FPR@95TPR on BDD-Anomaly over the baseline.

---


### 142. [Three Necessary Principles for Self-Supervised Visual Representation Learning](https://arxiv.org/abs/2608.08309)

**<font color=#1a73e8>作者：</font>** Nikos Giakoumoglou, Paschalis Giakoumoglou, Tania Stathaki  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We argue that learning visual representations without labels requires a training signal jointly complete across three non-overlapping objectives: semantic invariance across augmented views, patch-level spatial prediction, and representational non-degeneracy. We formalize these as the observation, prediction, and regularization principles and prove (i) that combining observation and prediction without regularization admits the constant encoder as a global minimizer under negative-free alignment; (ii) that the two objectives are gradient-complementary and structurally non-conflicting at the encoder output; and (iii) that the momentum encoder converges to the same fixed point as the online encoder and provides no collapse guarantee at convergence. Contrastive alignment provides only self-limiting collapse resistance, formalized via an explicit gradient-decay argument. Dropping prediction withholds the spatial training signal by construction; dropping observation forfeits cross-view semantic invariance by construction; at the scale we study, no pair substitutes for the third. Every major self-supervised method is a special case of a single unified energy decomposition. We pair every theoretical claim with a controlled experiment, including a patch-retrieval evaluation for the spatial consequence of prediction.

---


### 143. [The Neural Division of Labor: Biologically-Inspired Modular Architectures for Robust Neuromorphic Computing](https://arxiv.org/abs/2608.08317)

**<font color=#1a73e8>作者：</font>** Maksim Bazhenov, Serafim Grubas, Vakhtang Putkaradze  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Biological neural systems achieve high efficiency and robustness through compartmentalized architectures. In contrast, modern artificial neural networks rely on globally entangled structures, which obscure decision logic and suffer from catastrophic forgetting. Here, we report a Decomposable Spiking Neural Network (D-SNN) that eliminates global synaptic entanglement by structurally isolating classification pathways into independent experts. Optimized via a bio-inspired push-pull loss function, the D-SNN achieves competitive accuracies on MNIST, Fashion-MNIST, and CIFAR-10/100 benchmarks. This modular approach matches the performance of fully dense networks while utilizing an order of magnitude fewer parameters. In addition, our networks operate with up to several orders of magnitude lower firing rates and fewer synaptic operations. Furthermore, physically severing connections between experts provides inherent protection against catastrophic forgetting during sequential learning. Crucially, these isolated pathways generate auditable neural signals, increasing decision transparency. This biomimetic, verifiable architecture establishes an efficient foundation for deploying deterministic neuromorphic intelligence in resource-constrained edge environments.

---


### 144. [Spatial Heterogeneity-Aware Multi-Hazard Susceptibility and Risk Mapping at Regional Scale](https://arxiv.org/abs/2608.08321)

**<font color=#1a73e8>作者：</font>** Aswathi Mundayatt, Siddharth Anil, Hitanshu Seth 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Floods and landslides often co-occur, but their relationships with environmental controls vary spatially. This study develops a spatial heterogeneity-aware framework for flood-landslide susceptibility and relative-risk mapping in Kerala, India, and Nepal. It combines 15 km x 15 km grid cells with region-specific contextual zones and compares proximity-gated cross-zone training (S1) and ecology-gated zone-constrained training (S2). S1 permits geographically nearby models to be assigned across contextual boundaries, whereas S2 restricts model development and assignment to the same zone. Random Forest models for each hazard use strategy-specific predictor sets and are evaluated on spatially held-out test samples. Susceptibility surfaces are integrated with CRITIC-weighted exposure and vulnerability indices to produce hazard-specific and nine-class bivariate relative-risk maps. S1 achieved higher mean accuracy, precision, recall, F1-score, AUC-ROC, and PR-AUC for both hazards and regions. The largest difference occurred for Nepal flood susceptibility, where AUC-ROC increased from 0.728 under S2 to 0.886 under S1 and PR-AUC from 0.512 to 0.823. S2 produced lower Brier scores for both Nepal hazards and retained zone-specific differences in predictor selection, SHAP rankings, and response patterns, particularly in Kerala. Both strategies reproduced flood-prone lowland and landslide-prone upland patterns but differed in susceptibility and risk classes. Bivariate risk-map agreement was 0.521 in Kerala and 0.711 in Nepal, with allocation disagreement exceeding quantity disagreement in all S1-S2 comparisons. Susceptibility-to-risk correspondence remained below 0.350, showing that exposure and vulnerability changed priority locations. Overall, cross-zone learning strengthens regional discrimination, while zone-constrained learning preserves environmental differences, supporting their integration.

---


### 145. [A Decision Framework for Selecting Technology Acceptance and Use Models: TAM, TAM2, TAM3, UTAUT, and UTAUT2](https://arxiv.org/abs/2608.08333)

**<font color=#1a73e8>作者：</font>** Nathalino Pachêco Britto  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Introduction: Models such as TAM, TAM2, TAM3, UTAUT, and UTAUT2 underpin a substantial share of research on technology acceptance and use in HCI and related fields. Although they differ in terms of constructs and conditions of application, their selection is often not conceptually justified, frequently driven by pragmatic considerations, with implications for theoretical consistency and cross-study comparability. Objective: To propose a decision framework that guides the selection among the five models of the TAM/UTAUT lineage based on conceptual criteria derived from their structural differences. Methods: A conceptual, artifact-oriented approach was adopted, comprising comparative analysis of the models and critical review studies, derivation of conceptual dimensions, and formulation of operational decision criteria. Applicability was demonstrated through two contrasting research scenarios. Results: The framework articulates five analytical dimensions, 16 guiding questions, and descriptive suitability profiles for the models. The demonstration illustrated, in the two scenarios examined, its ability to identify misalignments between the declared model and the actual operationalization, as well as to confirm theoretical choices consistent with the conditions of the study.

---


### 146. [Differential Privacy for Markov Chain State Trajectories](https://arxiv.org/abs/2608.08341)

**<font color=#1a73e8>作者：</font>** Alexander Benvenuti, Matthew Hale  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Data-driven systems may require state trajectories of Markov chains to function because these trajectories contain information that is useful to the system, e.g., a product's credit risk, a user's physical location, or a user's internet browsing behavior. However, sharing such state trajectories can reveal sensitive information about users, which presents a privacy threat. Therefore, we develop a new framework for privatizing the state trajectories in a Markov chain using differential privacy. Our framework privatizes state trajectories online, in the sense that a private state trajectory is generated at the same time as the sensitive one it approximates. We treat Markov chains as weighted directed graphs whose edge weights are the negative logarithms of the transition probabilities. Then, each state in a private state trajectory is chosen by minimizing its distance to the corresponding state in the sensitive state trajectory, where the notion of distance is equal to the total edge weight along a shortest path. We prove that with high probability the private state trajectory remains close to the sensitive one, which maintains high utility for downstream uses of private data. Additionally, we prove that private state trajectories are consistently in the typical set of state trajectories generated by the underlying Markov chain, which means that private state trajectories have similar statistical properties to actual state trajectories produced by the underlying Markov chain. Numerical simulations show that under $3$-differential privacy, the mechanism we introduce exhibits up to an $80\%$ decrease in entropy compared to the state of the art, which illustrates that private state trajectories generated by our framework more closely resemble their corresponding sensitive state trajectory while maintaining the same level of privacy.

---


### 147. [Dramarrator: Object-Based Audio Editing for Audio Drama Production from Books](https://arxiv.org/abs/2608.08349)

**<font color=#1a73e8>作者：</font>** Karim Benharrak, Oriol Nieto, Bryan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Audio dramas weave dialogue, sound effects, and music into immersive stories. Creators often adapt books into audio dramas, but this process remains labor-intensive, requiring them to interpret source material, author scripts, generate audio assets, and assemble them on a timeline. Because story elements like characters and scenes manifest across many interdependent assets, a single change can ripple into manual updates across the entire project. We present Dramarrator, an audio drama authoring tool built around object-based audio editing, where these story elements are represented as editable objects. Dramarrator extracts these objects from a book, generates linked audio assets (speech, sound effects, and music), and composes a multi-track audio drama. Edits to any object (e.g., a character's voice) automatically propagate to all dependent assets. In a user study with professionals (N=8), Dramarrator significantly lowered task load when creating audio dramas. A listener study (N=300) shows that creator-refined output from Dramarrator approaches the quality of productions made with existing professional tools, and an exploratory study (N=3) suggests object-based editing lowers entry barriers and generalizes beyond audio dramas.

---


### 148. [Correlation flow governs learning at criticality](https://arxiv.org/abs/2608.08350)

**<font color=#1a73e8>作者：</font>** Andrea Combette, Nelly Pustelnik, Antoine Venaille  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The initialisation of deep neural networks determines whether information and gradients can propagate across depth, yet a unified theory connecting these properties to learning dynamics remains elusive. Combining mean-field theory and random matrix theory, we establish a direct link between correlation propagation and the Neural Tangent Kernel (NTK) that governs learning in the sequential limit of infinitely wide, infinitely deep networks. Correlation propagation to infinite depth is possible only at a single critical point in the weight-bias variance plane. At this point, we show that the end-to-end Jacobian vanishes algebraically with depth, and use this to prove that the NTK becomes exactly proportional to the output correlation at infinite depth. This equivalence between information propagation and learning dynamics had not yet been noticed. We further show that orthogonal initialisation suppresses the leading finite-size corrections present under Gaussian initialisation, clarifying the respective roles of the two initialisation ensembles in this limit. These theoretical predictions are validated quantitatively on finite-width, finite-depth networks. Together, these results demonstrate that orthogonal initialisation at criticality plays a central role in controlling the asymptotic dynamics of deep learning.

---


### 149. [Tropical Cyclone Forecasting via Latent Rectified Flow using Satellite Imagery and Atmospheric Fields](https://arxiv.org/abs/2608.08354)

**<font color=#1a73e8>作者：</font>** Meheru Zannat, Sk. Md. Masudul Ahsan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Tropical cyclones are growing more destructive in a changing climate, and efficient forecasting of their structure and track has become a necessity. Deep generative models promise an alternative to computationally expensive numerical weather prediction (NWP), yet current systems produce either satellite imagery or atmospheric fields, never both; they need many sampling steps, putting them out of reach of modest hardware; and their storm tracks come from regression heads with no physical link to the generated atmosphere. This work presents a single-pass model that jointly forecasts GRIDSAT-B1 infrared imagery and four ERA5 atmospheric fields (U-wind, V-wind, air temperature, and surface pressure) out to nine hours. A five-channel variational autoencoder compresses each 5 x 256 x 256 frame to a 4 x 64 x 64 latent, and a conditional rectified-flow UNet with a factorized temporal-attention module predicts the next three frames from three past frames, their best-track coordinates, and timestamps. The model is then reward-fine-tuned (DRaFT) against a differentiable track error derived from the predicted winds through a steering-flow calculation. On held-out 2022 storms the model reaches 16.35 dB PSNR and 0.759 SSIM, ahead of a reproduced cascaded-diffusion baseline at every lead time (+0.84 dB at +9 h) while sampling ~30x faster (56 ms vs. 1673 ms). Track error at +9 h is 62.4 km, 15% below the baseline, and a reward fine-tuning study demonstrates a further 8-11% track-error reduction across sampler budgets.

---


### 150. [Unimodality-Promoting Regularized Learning for Ordinal Regression](https://arxiv.org/abs/2608.08359)

**<font color=#1a73e8>作者：</font>** Ryoya Yamasaki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ordinal regression, also called ordinal classification, is classification of ordinal data, in which the underlying target variable is categorical and considered to have a natural ordinal relation. Previous works have indicated that, in many real-world ordinal data, the conditional probability distribution (CPD) of the target variable given a value of the explanatory variable would be unimodal in a large domain of the explanatory variable and close to be unimodal even in a remaining domain. Therefore, unimodality-promoting regularized learning (UPRL), which promotes a predicted CPD closer to be unimodal with the aim of decreasing a prediction variance without inducing much bias for ordinal data of the unimodality, is promising to improve the prediction performance especially with small-size training data. In this study, we show that previous UPRL methods promote a predicted CPD to not only become closer to be unimodal but also have a larger scale (in other words, be smoother or less-confident). Therefore, we develop a novel method that more strictly reflects the idea of UPRL and evades a scale-related bias, and verify through experimental comparison that the unimodality-promotion indeed contributes to improve the prediction performance. Additionally, while our proposed UPRL method could perform better for smaller-scale data or with larger-size training data compared to a previous UPRL method, our analysis explains this experimental observation in terms of the presence or absence of an unexpected scale-related bias.

---


> [!TIP]
> 当前位于：**101-150**（第 3/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-445](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
