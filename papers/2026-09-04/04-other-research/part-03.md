# 📦 其他研究 | 2026年09月04日

> 本类共 **187** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-187](./part-04.md)

---

### 101. [Propose to Learn, Learn to Propose: Evaluability-Aware Assistance under Bounded Rationality](https://arxiv.org/abs/2609.02242)

**<font color=#1a73e8>作者：</font>** Yifan Zhu, Sammie Katt, Samuel Kaski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI assistants often collaborate by proposing candidate edits, plans, or designs that users evaluate before adoption. Existing assistance methods focus on proposal quality or user-goal inference, often assuming that the user can reliably evaluate any proposal, which can fail in practice because of bounded rationality. We study evaluability-aware proposal planning, where proposals serve both as task interventions and as probes for learning latent preferences and evaluation constraints, where the resulting belief updates then guide later proposals. We formalise this setting as ProSE, a hidden-parameter sequential assistance problem, and instantiate it with a KL-regularised bounded-rational binary response model in which acceptance trades off value gain against a distance-dependent evaluability penalty. Analysing the planning consequence of this likelihood reveals that likely accepted proposals and informative probes need not coincide, which explains why planners that only pursue acceptance systematically underperform. We operationalise ProSE with \textsc{ProSE-Plan}, a depth-2 Bayes-adaptive planner that scores proposals by possible responses and response-induced posterior beliefs. In controlled graph simulations, \textsc{ProSE-Plan} improves over evaluability-unaware and myopic baselines when evaluation cost is the bottleneck, and a probe-commit ablation confirms that our approach selects informative proposals that simpler methods miss. Our results thus identify user evaluability as a planning-relevant dimension of AI assistance, complementary to generation quality and preference inference.

---


### 102. [SAUF-Net: Structure--Appearance Representation Learning with Uncertainty Feedback for Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2609.02247)

**<font color=#1a73e8>作者：</font>** Qin Lu, Zheyang Jing, Yujie Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised learning has shown great potential for reducing annotation costs in medical image segmentation. However, most existing methods mainly exploit unlabeled data through prediction-level consistency, while the reliability of internal feature representations is often overlooked. In medical images, target-related structural cues are easily entangled with unstable appearance variations, which may lead to unreliable pseudo labels and error accumulation during training. To address these issues, we propose SAUF-Net, a Structure--Appearance Representation Learning with Uncertainty Feedback Network for semi-supervised medical image segmentation. SAUF-Net uses the Structure--Appearance Decomposition Module (SADM) to separate bottleneck features into structural and appearance representations. The Disentangled Guidance Module (DGM) injects these representations into the decoding process to enhance structure-aware segmentation. Meanwhile, the Auxiliary Decoder produces branch-specific predictions for reliability estimation and a fused prediction for appearance-swapped consistency. Furthermore, we introduce an Appearance-Swapped Consistency branch to encourage structural representations to remain stable under appearance variations. We also introduce a reliability-map-guided dual-head discriminator with a Validity Head and an Uncertainty Head to provide feature-level uncertainty feedback. Extensive experiments on ISIC-2016 and Kvasir-SEG demonstrate that SAUF-Net outperforms state-of-the-art semi-supervised methods, especially under low-label settings.

---


### 103. [Handwriting Trajectory Recovery via Autoregressive Ordered Stroke Instance Prediction](https://arxiv.org/abs/2609.02251)

**<font color=#1a73e8>作者：</font>** En-Guang Wang, Yan-Ming Zhang, Fei Yin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwriting trajectory recovery aims to infer the dynamic writing process hidden behind a static handwritten image. Since offline handwriting preserves only the final spatial ink pattern, temporal information such as stroke order, writing direction, and pen-tip motion is lost, making recovery inherently ambiguous. Existing learning-based methods often directly predict the complete character trajectory without explicitly exploiting the stroke-level organization of handwriting. We argue that recovering the writing process should follow the writing process itself. Accordingly, we propose a two-stage framework that first recovers ordered stroke instances and then reconstructs continuous within-stroke motion. The first stage integrates stroke extraction and stroke-order recovery through autoregressive ordered stroke prediction, while direction-related structural cues further support within-stroke trajectory generation. Experiments on Chinese handwriting show that the proposed ordered prediction is more effective than post-hoc stroke ordering. Even without trajectory simplification, our full-point model achieves numerically better results than those reported by all compared baselines, while a controlled analysis shows that trajectory sampling density substantially affects measured recovery performance. Additional experiments demonstrate generalization to unseen Chinese character categories and cross-language extensibility to English and Tamil handwriting.

---


### 104. [MAOL: Morphology-Aware Ordinal Learning for Fine-Grained Industrial Defect Severity Grading](https://arxiv.org/abs/2609.02266)

**<font color=#1a73e8>作者：</font>** Zhaoyang Wang, Haiyong Chen, Binyi Su 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained defect severity grading is essential for industrial inspection, yet remains challenging due to the ordinal nature of severity labels, the strong dependence on morphology-related cues, and the train-test discrepancy between clean annotated instances and noisy predicted instances in two-stage pipelines. We propose MAOL, a Morphology-Aware Ordinal Learning framework for fine-grained industrial defect severity grading. MAOL formulates severity grading as an instance-level ordinal learning task, incorporates explicit morphological features to enhance representation learning, introduces class-conditional adaptive ordinal thresholds to model defect-specific grading boundaries, and employs prediction-aware training via localization perturbation to improve robustness to imperfect predicted instances. Extensive experiments under both clean-ROI and predicted-instance settings demonstrate that MAOL consistently outperforms rule-based methods, nominal classification models, and existing ordinal baselines, especially in the predicted-instance setting. The proposed approach ranked third in the IDA 2026 Challenge on Fine-Grained Severity Grading for High-Precision Manufacturing.

---


### 105. [RouteGraph-Mona: Confusion-Aware Routing Fine-Tuning for Mineral Image Classification](https://arxiv.org/abs/2609.02282)

**<font color=#1a73e8>作者：</font>** Jierui Li, Zhiyuan Qi, Hao Zhu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mineral image classification is important for geological exploration and resource development, but it remains challenging due to substantial intra-class variations in appearance and high inter-class visual similarity. Multi-cognitive Visual Adapter (Mona) is a vision-oriented parameter-efficient adapter that adapts pre-trained visual models by tuning only a few parameters. However, Mona statically aggregates responses from multiple scales, limiting its ability to accommodate sample-specific scale preferences and model confusion among visually similar mineral categories. To address this issue, we propose \textbf{RouteGraph-Mona}, a lightweight route-space regularization method built on Mona. Specifically, we replace Mona's static multi-scale aggregation with sample-adaptive routing. The resulting branch-selection behavior defines a compact routing space that captures each image's scale preferences. We then regularize the resulting routing signatures with class-wise route anchors and confusion-weighted margins. The route anchors encourage class-consistent routing patterns, while the margins promote greater separation between visually similar categories in the routing space. Experiments on three public mineral image datasets with two visual backbones show that RouteGraph-Mona consistently outperforms Mona in mean accuracy and remains competitive with representative fine-tuning methods and mineral image classification baselines.

---


### 106. [Diffusion-Encoding Gaussian Field for Joint k-q dMRI Reconstruction](https://arxiv.org/abs/2609.02288)

**<font color=#1a73e8>作者：</font>** Zhibo Chen, Yajuan Huang, Yu Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion MRI requires repeated k-space acquisitions over multiple diffusion-encoding directions, making acquisition time dependent on both spatial and angular sampling. Existing joint k-q methods either associate directional parameters with fixed voxels or separate spatial reconstruction from angular completion. However, diffusion-weighted images acquired under different directions share the same anatomical organization, while their local signal intensities vary with diffusion encoding. Existing formulations do not fully exploit the complementarity between shared anatomy and direction-dependent signal variation. Consequently, residual spatial errors may be misinterpreted as genuine angular variation and propagated to unobserved directions.
We propose a subject-specific spatial-angular Gaussian field for self-supervised joint k-q dMRI reconstruction. Shared 3D Gaussian primitives provide local spatial support, with each primitive carrying a continuous q-conditioned tensor-residual response. The signal at each location is synthesized from multiple overlapping primitive responses, coupling neighboring spatial regions and diffusion directions. The field is progressively optimized from undersampled k-space measurements of observed directions, without fully sampled targets or held-out-direction supervision.
Experiments on three HCP diffusion shells under multiple acceleration settings demonstrated consistent improvements in missing-direction DWI reconstruction, tensor-derived metrics, and principal diffusion orientation estimation.

---


### 107. [If It Moves, Radar Knows: A Physics-Aware Radar Transformer for Class-Agnostic Moving-Object Detection](https://arxiv.org/abs/2609.02289)

**<font color=#1a73e8>作者：</font>** Yinghao Sun, Shuguang Li, Jinliang Shao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detectors trained on closed-set annotations can miss rare moving objects outside the training taxonomy. Automotive radar provides category-independent Doppler motion cues and is less affected by adverse illumination and weather, but sparse, noisy returns hinder class-aware 3D box detection. Surface location and velocity remain useful for motion reasoning and collision avoidance when full box geometry is difficult to recover. We present the Physics-Aware Radar Transformer (PART), a fully sparse radar-only detector that predicts existence confidence, a representative surface point, and 2D ground-plane velocity for each moving-object hypothesis. Doppler-Aware Query Initialization (DAQI) replaces scene-independent learned queries with input-dependent proposals by clustering radar returns in position and velocity, easing query-object assignment in sparse scenes. Physics-Guided Cross-Attention (PGCA) incorporates radial-Doppler consistency and radar cross section (RCS) into query-point association. Uncertainty-aware supervision randomly masks ground-truth objects and assigns soft existence targets to ambiguous radar-supported queries, reducing reliance on exhaustive annotations. With only 1.1 million parameters, PART achieves a class-agnostic average precision (CA-AP) of 0.8827, a mean average surface translation error (mASTE) of 0.3188 m, and a mean average velocity error (mAVE) of 0.8084 m/s on nuScenes. It attains 0.9203 recall on rare and safety-relevant categories excluded from the standard evaluation and remains effective at night, in rain, and under severe occlusion. Inspection of apparent false positives shows that some predictions correspond to moving objects absent from the nuScenes annotations. Code and pretrained model weights will be publicly available at this https URL.

---


### 108. [VoRTeC: Taming Foundation Flow for One-step Real time Video Compression](https://arxiv.org/abs/2609.02291)

**<font color=#1a73e8>作者：</font>** Yichong Xia, Qinhong Wu, Qinhong Wu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ultra-low bitrate video compression still faces critical challenges: traditional neural video compression inevitably introduces blurring artifacts, while diffusion-based generative video compression suffers from excessive decoding latency and poor temporal consistency. To address these issues, we propose $\mathtt{VoRTeC}$, a Video Compression framework built upon a foundational flow model (Wan2.1). By compactly encoding latent video representations, predicting the positions of compressed representations along flow trajectories, and integrating multi-scale priors, $\mathtt{VoRTeC}$ enables the compressor to harness generative video flow priors effectively. Without accessing the parameters or gradients of flow matching networks, our framework achieves one-step decoding and reconstructions with high perceptual fidelity. Meanwhile, we maintain consistency across frame groups via tail-frame reuse and prior caching. Extensive experiments demonstrate that our method reduces bit consumption by 58\% compared to prior diffusion-based approaches, with decoding speed boosted by 3 to 197 times: $\mathtt{VoRTeC}$ achieves a decoding speed of 13 FPS at 720p and 32 FPS at 480p.

---


### 109. [Bayes-Optimal BER and AUC: Estimation and Evaluation of Estimators](https://arxiv.org/abs/2609.02304)

**<font color=#1a73e8>作者：</font>** Ryota Ushio, Takashi Ishida, Masashi Sugiyama  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A fundamental quantity in machine learning is the optimal performance achievable by any model on a given task. Estimating this quantity allows us to distinguish the irreducible part of the error from a deficiency of the model, telling us how much room for improvement remains. Recent work has shown that the Bayes error, or equivalently the optimal accuracy, can be estimated from soft labels in binary classification. However, accuracy is often a poor summary of performance in settings with severe class imbalance or noisy annotations, where metrics such as the balanced error rate (BER) and the area under the ROC curve (AUC) are more appropriate. We address this gap with two complementary contributions. (i) Estimation. We propose soft-label-based estimators for the optimal BER and AUC. We first consider the clean setting in which true soft labels and the class prior are known, and then extend the estimators to a more realistic setting in which the class prior is unknown and the observed soft labels are corrupted by an unknown order-preserving transformation, possibly followed by additive noise. In the latter setting, we approximately recover the clean soft labels via isotonic regression with auxiliary hard labels, estimate the class prior with a clipped mean of the hard labels, and derive finite-sample error bounds for the resulting plug-in estimators. (ii) Evaluation. Since the optimum is unobservable on real datasets, evaluating any such estimator is itself nontrivial. We extend the FeeBee framework, originally proposed for evaluating Bayes-error estimators, to the optimal BER and AUC. The resulting procedure provides practical evaluation scores without requiring knowledge of the optimum, and applies to any estimator of the optimal BER or AUC, not only our proposed ones. Experiments on synthetic and real-world datasets validate both the estimators and the evaluation procedure.

---


### 110. [Efficient GUI Agents: A Systems Survey of Observation, Memory, Action, and Runtime Optimization](https://arxiv.org/abs/2609.02309)

**<font color=#1a73e8>作者：</font>** Bizhe Bai, Jiakang Yuan, Hongming Wu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> GUI agents increasingly operate across websites, mobile apps, and desktop environments, yet the field still reports progress primarily through task success. We argue that practical deployment depends equally on efficiency: how much context, computation, action budget, and runtime overhead an agent consumes while succeeding. This survey studies efficient GUI agents through an end-to-end systems lens that preserves the current technical axes of observation efficiency, context and memory efficiency, action efficiency, and planner-side/system efficiency. For each subsection, we expand the seed literature through targeted search plus backward and forward citation chaining, then synthesize the dominant mechanisms, reported efficiency signals, and new overheads they introduce. Across the literature, recent progress converges on a small set of recurring ideas: selective reading instead of full-context ingestion, global-to-local visual allocation, recoverable memory rather than raw history replay, verification-aware control, and hybrid runtimes that can switch between GUI and non-GUI execution. We conclude by identifying the main open problems, including honest accounting of verifier cost, cross-benchmark comparability, and co-design of observation, memory, and execution layers under real latency and privacy constraints.

---


### 111. [DiffIE: Diffusion-based Open Information Extraction](https://arxiv.org/abs/2609.02315)

**<font color=#1a73e8>作者：</font>** Konstantin Fedorov, Valentin Malykh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A single sentence often expresses multiple valid relational triplets, which makes Open Information Extraction (OpenIE) fundamentally a multi-output task. Existing neural systems handle this by autoregressive generation, which is flexible but slow and prone to redundancy, or by fixed-slot prediction, which is efficient but couples the extraction budget to training. We introduce DIFFIE which instead treats the stochasticity of conditional discrete diffusion as the extraction mechanism itself: independent reverse-diffusion trajectories over per-token role tags produce a pool of candidate triplets, which are clustered under lenient matching and ranked to form the output. Both the pool size and the number of returned extractions are inference-time choices, decoupling the extraction budget from training and exposing test-time compute as a tunable axis. DIFFIE achieves the new state of the art in CaRB (1-1) both F1 and AUC, and outperforms the strongest rule-based system (ClausIE) in BenchIE; it also remains competitive in standard CaRB and WiRe57 evaluations, giving the best average score among systems that report all four benchmarks. Ablations show that uniform discrete diffusion outperforms absorbing state diffusion in our setting, and that a matched non-diffusion stochastic tagger does not reproduce its gains. Our results indicate that diffusion stochasticity is an effective mechanism for structured prediction tasks with multiple valid outputs.

---


### 112. [ORB-SVM : An Innovative Hybrid Framework for Efficient Brain Tumor Detection from MRI Scans](https://arxiv.org/abs/2609.02333)

**<font color=#1a73e8>作者：</font>** Amirhosein Azarpour  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain cancer remains one of the most significant challenges in modern medicine, where the accuracy of early stage diagnosis is a decisive factor in patient survival and treatment efficacy. Although Magnetic Resonance Imaging (MRI) is the established gold standard for visualizing neurological structures, the interpretation of these high dimensional scans is often complicated by subjective variability among practitioners and the inherent noise present in complex medical images. While contemporary approaches frequently rely on high parameter deep learning architectures, such models often involve significant computational costs and require extensive data for effective training. This study introduces a hybrid framework that utilizes the Oriented FAST and Rotated BRIEF (ORB) algorithm for precise feature extraction and a Support Vector Machine (SVM) for classification [1], [2]. The proposed approach achieves a sub- stantial data reduction of approximately 99.5%, which effectively minimizes the influence of non informative background data while preserving critical diagnostic patterns essential for tumor identification. By balancing feature sparsity with a robust kernel based classifier, this methodology addresses the limitations of over parameterized systems while maintaining high diagnostic integrity. Experimental evaluations conducted on the Br35H dataset demonstrate that the framework attains a classification accuracy of 97.5%. The findings suggest that the integration of localized feature representation and optimized classification provides a reliable and resource efficient alternative for medical image analysis, offering a structured solution that maintains per- formance without the need for extensive computational overhead.

---


### 113. [AGI Maze Prediction Datasets: A Compact Benchmark for Learning World Dynamics with Transformers](https://arxiv.org/abs/2609.02339)

**<font color=#1a73e8>作者：</font>** Alexey Potapov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> World modeling requires a predictive model to maintain and update an internal state adequate for reasoning about the consequences of actions. We introduce the AGI Maze Prediction Datasets and Benchmark, a lightweight controlled testbed for studying this capability in Transformers and other predictive models. Derived from procedurally generated, stateful grid worlds, the benchmark comprises per-step transition prediction, fixed-horizon state prediction, and sequential textual-observation prediction. Source-maze-disjoint training and validation splits, together with greedy exact-match evaluation, distinguish learning transferable action-conditioned dynamics from memorizing transitions in familiar layouts. We establish from-scratch byte-level Transformer baselines and compare them with two working-memory-augmented architectures. A generic auxiliary latent-memory Transformer can fit some training sets perfectly but does not consistently improve held-out performance. In contrast, a pseudo-video spatial-memory Transformer initializes a two-dimensional latent workspace from the input map and updates it from action history without receiving intermediate maps, positions, or state labels. Under the same data, objectives, and evaluation protocol, this model reaches perfect validation accuracy on selected fixed-horizon tasks where the byte and unstructured-memory baselines do not, and substantially improves sequential text-trace prediction. These results suggest that structured, task-aligned working memory can be more useful than additional latent capacity alone. More broadly, we argue that language grounding is mediated by persistent data structures and computations over them; the benchmark offers a compact setting for testing architectures that couple textual interfaces to learned structured state.

---


### 114. [Structured-Prior-Guided Diffusion Inpainting with Physical Consistency for Traffic Sign Augmentation](https://arxiv.org/abs/2609.02348)

**<font color=#1a73e8>作者：</font>** Luo Li, Chongchong Huang, Jun Jia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Traffic sign detection faces a long-tailed data distribution. Many rare signs matter as much as common ones from a regulatory standpoint, yet they have very few samples. Generative data augmentation is one way out. General-purpose inpainting models, however, distort digits, deform geometry and perspective, and shift colours when applied directly to sign regions. We trace this to a single gap: the conditioning signal is too abstract for the physical composition of a sign. We propose a structured-prior-guided diffusion inpainting framework with physical consistency. It injects the semantic, appearance and geometric priors of a sign through three orthogonal pathways: a JSON-formatted text prompt, a front-view vector template rendered with measured dominant colours (via IP-Adapter), and an affine-aligned vector template (via ControlNet). Two physical consistency losses constrain colour with a CIELAB chromaticity $L_1$ term and edge structure with a Sobel gradient term. We train by self-supervised reconstruction on a large set of images collected in-house at AMAP, then evaluate zero-shot on the public TT100K-2021 dataset, a different source. Our method uses a Stable Diffusion 1.5 backbone of about 1.4B parameters. It beats seven representative competitors on every metric of reconstruction fidelity, physical consistency and semantic controllability. Its OCR exact-match rate reaches 91.1\%, against 44.2\% for the 12B industrial model FLUX.1 Fill [dev], and it needs only $1/14$ of that model's inference time. Leave-one-out ablations confirm that each of the three prior pathways and both loss terms contribute on their own. In downstream detection, the synthetic data raises the group-pooled AP50 of rare classes by $1.23\times$ to $7.40\times$ over a real-data-only baseline. Code and pre-trained models are available at this https URL.

---


### 115. [GlyphAnchor: Enhancing Visual Text Rendering via Position-Anchored Glyph Priors](https://arxiv.org/abs/2609.02349)

**<font color=#1a73e8>作者：</font>** Qiang Xiang, Shuang Sun, Binglei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rendering accurate text remains difficult for image generation and editing models, especially when the target contains long, complex, and densely arranged text or rare characters. Existing approaches either improve native text rendering through stronger backbones and data-centric training without explicit glyph priors, or incorporate glyph priors through specialized designs that remain insufficiently accurate and robust under challenging scenarios. We introduce GlyphAnchor, a novel text-rendering enhancement method for both text-to-image and image-editing diffusion transformer models. GlyphAnchor enhances the backbone with lightweight glyph patch conditions whose positions are anchored to the target image through the model's native positional encoding. We train this capability with staged supervised finetuning and further refine it with text-aware post-training to improve robustness. We also introduce InfoTextBench, a benchmark for evaluating text-rich visual text rendering in both generation and editing settings. Experiments across multiple backbones and benchmarks, including long, complex, and densely arranged text and rare character scenarios, show that GlyphAnchor consistently improves text fidelity while preserving overall image quality.

---


### 116. [Towards a Foundational Ontology for Identifying and Resolving Contradictions in Dialogue-based Human-Robot Interactions](https://arxiv.org/abs/2609.02364)

**<font color=#1a73e8>作者：</font>** Maitreyee Tewari, Michele Persiani  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Existing Human-Robot Interaction (HRI) literature has focused on identifying and structuring errors, failures, conflicts, and knowledge issues (called in this work as contradictions) in domain-specific dialogue-based interactions. However, there is still lack of a formal computational framework to represent and define these contradictions, interoperable and usable across HRI and human-agent interaction (HAI) domains. Thus, this research project aims to capture, represent, and evaluate the notion of (1) dialogue-based collaborative interaction and (2) related contradictions in a foundational ontology. METHONTOLOGY, a systematic approach to build domain-independent ontologies was applied. In the conceptualisation stage of the presented ontology, concepts and models from Activity Theory were used. Preliminary results presented in this short article are: (i) Natural language definitions of dialogues and related contradictions in HRI, (ii) Set Theoretic definitions of dialogues and contradictions, and (iii) First Order Logic (FoL) formulation of the contradiction concepts and three novel principles guiding dialogue-based interactions between humans and robots. In summary, we report on ongoing work to develop a foundational ontology based on Activity Theory called Activity Theory-based foundational ontology (ATFOt) to capture and represent the notion of contradictions in HRI.

---


### 117. [Information Density Imbalance in Visual Object Detection](https://arxiv.org/abs/2609.02369)

**<font color=#1a73e8>作者：</font>** Ziwei Zhao, Yanxi Lu, Yuwei Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In object detection, the number of instances is typically used to determine whether a dataset exhibits a long-tailed distribution, implicitly assuming that the model will perform poorly on categories with fewer instances. This assumption has led to extensive research on category bias in datasets with imbalanced instance numbers. However, even in datasets where instance numbers are relatively balanced, models still exhibit category bias, indicating that instance count alone cannot explain this phenomenon. In this work, we first introduce the concept and measurement of information density. We then observe a significant negative correlation between a category's information density and its accuracy, and we investigate how the training process impacts this relationship. Empirical studies suggest that information density imbalance may be a potential source of category bias. To preliminarily validate the potential of information density, we made simple improvements to three advanced object detection loss functions using this concept. Experiments on the Pascal VOC, COCO-LT, and LVIS datasets demonstrate that information density can significantly reduce model bias while effectively enhancing the overall performance of existing loss functions. This study provides a new perspective for understanding the generalized bias phenomenon in object detection models and offers new tools for designing fairer loss functions and training strategies.

---


### 118. [Percolation Dynamics in Optimization : Variance Cascades and Discrete Scale Invariance](https://arxiv.org/abs/2609.02373)

**<font color=#1a73e8>作者：</font>** Sai Niranjan Ramachandran, Suvrit Sra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the dynamics of Stochastic Gradient Descent (SGD), which is known to steer deep neural networks toward invariant sets that correspond to simpler subnetworks. How this steering unfolds over time remains poorly understood. We answer this by modeling the stochastic gradient flow (SGF) as a percolation process, in which architectural symmetries force subnetworks to merge in discrete simultaneous blocks rather than one at a time. These structural transitions register as variance spikes in a macroscopic order parameter, echoing physical phase transitions. We further show this trapping mechanism and its associated scaling cascade extend to Adam and AdamW under an explicit heavy-tailed noise model.

---


### 119. [ProSR: Semantic-Prototype-Guided Discrete Modeling for Physically Consistent SAR Super-Resolution](https://arxiv.org/abs/2609.02377)

**<font color=#1a73e8>作者：</font>** Byoungwoo Kim, Munchurl Kim  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution Synthetic Aperture Radar (SAR) imagery is critical for precision analysis such as automatic target recognition, yet its acquisition is costly. Although generative image super-resolution (ISR) models offer a promising alternative, current smooth-approximation based diffusion frameworks often struggle to preserve the coherent scattering statistics, causing stochastic structural distortions that are less consistent with real SAR physics. To address this, we propose Semantic Prototype-Guided Super-Resolution (ProSR), reformulating SAR ISR as a semantically-guided discrete token prediction task within a quantized latent space. By mapping signal features to discrete scattering primitives, ProSR preserves the impulsive nature of SAR without over-smoothing. Furthermore, we integrate a Self-Supervised Learning backbone into SAR ISR to extract label-free semantic priors, overcoming label scarcity. Guided by these priors, we introduce Semantic-Aligned Detail Encoding to decouple high-frequency signals into discrete scattering primitives. In parallel, the Semantic Prototype Map Generator explicitly constructs semantic prototype maps, allowing Prototype-Map-Guided Attention to route the information flows within identical categories and mitigate inter-class interference. To validate our approach, we present a large-scale 0.25m resolution benchmark from the Umbra Open Dataset. Experimental results show ProSR achieves superior visual quality while preserving essential scattering characteristics required for practical SAR applications.

---


### 120. [Contrastive Explanations in Quantitative Bipolar Argumentation Frameworks](https://arxiv.org/abs/2609.02399)

**<font color=#1a73e8>作者：</font>** Xiang Yin, Nico Potyka, Antonio Rago 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Argumentation frameworks are useful tools for representing and reasoning with information in a variety of settings, e.g. in supplementing AI models as they perform classification tasks, with a notable benefit of providing additional explainability. In this paper, we introduce contrastive explanations for Quantitative Bipolar Argumentation Frameworks (QBAFs), one such formalism. Unlike most existing explanations for QBAFs, which explain the reasoning outcome of a single argument of interest (i.e. a topic argument), contrastive explanations explain the difference between two topic arguments. We introduce a general form of contrastive attribution functions (CAFs) and establish a set of general properties they should satisfy. We introduce CAFs based on removal, gradients and Shapley-values, and study their properties. Finally, to illustrate contrastive explanations, we demonstrate their usefulness in healthcare and bias identification settings.

---


### 121. [Coverage, Not Targeting: A Structural Regime in Multi-Turn Agent Credit Assignment](https://arxiv.org/abs/2609.02417)

**<font color=#1a73e8>作者：</font>** Chenyu Zhou, Qiliang Jiang, Shuning Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-turn agentic RL increasingly treats credit assignment as a targeting problem: given a terminal verifiable reward, per-turn methods localize credit onto the turns that mattered. We identify the structural quantity that predicts when this is the right move, the verifier information density V_d = k/C (the fraction of an agent's C-step causal chain whose per-turn correctness the verifier exposes), and show that terminal-state verifiers sit deep in a low-V_d regime where targeting is the wrong axis. In controlled shared-rollout comparisons on tau^2-bench that separate reward density from credit geometry, a continuous dense reward spread uniformly beats the sparse binary outcome reward (net-harmful on 4/5 seeds), while concentrating the same advantage on progress turns or on random turns is equally harmful: targeting is second-order. The mechanism is coverage: terminal-state verification collapses the observable signal to a single final-write turn (k=1 in 98% of rollouts) while success requires a 5-8 step chain of prerequisite tool calls. A synthetic phase boundary places the crossover at V_d* ~ 0.8, whereas measured V_d is ~0.15 on tau^2-bench and ~0.4 on BFCL V3; uniform also wins on BFCL, where a matched-concentration shuffled control is negative on 8/8 seeds. The effect reproduces across model families on ToolACE-2-8B (Delta = -0.048 over 32 pre-registered seeds; an independent 20-seed replication is itself significant), and a pre-registered matched-budget breadth sweep traces a monotone dose-response whose deficit vanishes only at full chain coverage, with a reward-to-go arm reaching full-coverage parity. Uniform redistribution is the zero-information coverage default that per-turn schemes must beat; we contribute the matched-concentration shuffled control that any targeting claim should clear.

---


### 122. [IFW-BLS: Dual-Robust Broad Learning System with Intuitionistic Fuzzy Wave Loss](https://arxiv.org/abs/2609.02422)

**<font color=#1a73e8>作者：</font>** Mushir Akhtar, M. Tanveer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Broad Learning System is an efficient randomized learning model that expands network width through feature and enhancement nodes and estimates the output weights without deep backpropagation. Its standard least-squares training, however, is vulnerable in two different ways: (i) large residuals caused by noise, outliers, or corrupted labels can dominate the objective, and (ii) all samples are treated as equally reliable even when some lie in ambiguous or locally conflicting regions. This paper proposes IFW-BLS, an Intuitionistic Fuzzy Wave Broad Learning System that addresses these two sources of fragility within one optimization model. The first robustness mechanism is residual-level protection, obtained by replacing the squared loss with the bounded, smooth, and asymmetric wave loss. Boundedness prevents extreme residuals from receiving unbounded influence, while asymmetry allows positive and negative deviations to be penalized differently when the dominant error direction varies. The second mechanism is sample-level credibility control, obtained through intuitionistic fuzzy scores that combine global class-center consistency with local neighborhood conflict. The resulting model evaluates the wave loss on credibility-weighted residuals, so unreliable samples are down-weighted before the bounded loss further limits the effect of extreme errors. A Nesterov accelerated gradient based optimizer is used to solve the proposed objective, avoiding the explicit matrix inversion used in conventional BLS. Experiments on UCI benchmark datasets validate the superiority of the proposed IFW-BLS model over the baseline models; additional corruption experiments also show more stable performance than BLS under noise and outlier contamination.

---


### 123. [Uncertainty-Guided Adverse Weather Restoration via Gated Transformer Network](https://arxiv.org/abs/2609.02434)

**<font color=#1a73e8>作者：</font>** Zheke Jin, Yuning Cui, Tianle Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Restoring images degraded by adverse weather remains challenging due to spatially heterogeneous degradations. Many existing weather-specific restoration models rely on weather-agnostic global aggregation, naive cross-scale fusion, and deterministic objectives, which struggle to handle heterogeneous degradations in all-in-one adverse-weather settings. To address these limitations, we propose an Uncertainty-guided Adverse-weather Restoration Network (UAR-Net), a weather-specific AiO framework that integrates a gated transformer with balanced multi-scale skip connections. Specifically, we employ Gated Dual-scale Transformer Blocks (GDTB) to jointly model selective global interactions and multi-scale local structures, a progressive Balanced Multi-scale Skip Connection (BMSC) for balanced multi-scale feature integration, and an Uncertainty-Aware Refinement Head (URH) that performs artifact removal, detail enhancement, and predictive uncertainty estimation. The model is supervised by a Brightness-Aware Energy Loss (BAE-Loss) to encourage accurate reconstruction with well-calibrated uncertainty. Extensive experiments demonstrate that our method achieves state-of-the-art performance across multiple adverse-weather benchmarks. The codes will open source upon acceptance.

---


### 124. [Decoding Decision Correctness from EEG Under High Cognitive Workload in Virtual Reality: Implications for Collaborative Brain-Computer Interface Teams](https://arxiv.org/abs/2609.02436)

**<font color=#1a73e8>作者：</font>** Christopher Baker, Stephen Hinton, Tom Reed 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Collaborative Brain-Computer Interfaces (cBCIs) offer a promising mechanism to augment team decision-making, but existing approaches rely exclusively on evidence available only after a decision has been made and reported, such as reaction time or stated confidence. This limits their use to explaining or discounting a decision after the fact, rather than informing a team's response before it is finalised. We tested whether spatial-covariance EEG features could instead provide a genuinely pre-emptive signal of an operator's decision correctness, available within the response window itself, and whether such a signal depends on cognitive workload. Using a continuous virtual reality target-detection task, participants (N = 23) completed a within-subject workload manipulation (High vs. Low). At the team level, weighting votes by this pre-emptive neural signal, available before a response is committed, produced substantial accuracy gains on contested (evenly-split) trials under High Workload (57% to 88% as team size increased from 2 to 16), but was actively detrimental under Low Workload. Critically, this advantage held even against post-hoc behavioural signals: confidence was the strongest single team-level signal overall, but by definition cannot inform a decision still in progress, whereas the neural signal can. These findings indicate that EEG-based decision-reliability signals are not a general-purpose team augmentation tool, but a workload-conditional one, with clear implications for when and how cBCI systems should be deployed in operational teams.

---


### 125. [Towards One-for-All Robustness Across a Continuum of Threat Levels](https://arxiv.org/abs/2609.02440)

**<font color=#1a73e8>作者：</font>** Zhichao Hou, Xiaorui Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adversarially robust models often overfit to a specific attack budget, necessitating multiple specialized models for diverse and dynamic adversarial environments, a strategy that becomes fundamentally intractable as the threat space grows. This raises an open challenge: can we achieve strong robustness across a continuum of threat levels within a single model? We propose the Threat Conditional Network (TCN), grounded in a representation factorization framework that decomposes representation learning into a threat-invariant shared backbone and a lightweight threat-conditional adaptor. TCN conditions a single model on the perturbation level via Fourier-based embeddings and channel-wise affine modulation, and is trained against a distribution over perturbation budgets, enabling flexible and seamless adaptation across an infinite continuum of threat levels during inference. Extensive experiments on CIFAR-10, CIFAR-100, and Tiny-ImageNet show that TCN matches or surpasses a full ensemble of budget-specialized models with a single set of parameters, generalizes to unseen perturbation budgets, and transfers robustly under mismatched threat conditions, with only 4.6\% parameter overhead. These contributions chart a promising path toward adaptive and generalizable robustness in dynamic and diverse threat environments.

---


### 126. [CACTUS: Mask-Guided Semantic Clean-Label Backdoors in Decentralized Federated Learning](https://arxiv.org/abs/2609.02450)

**<font color=#1a73e8>作者：</font>** Chao Feng, Burkhard Stiller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Semantic triggers in federated learning (FL) can be less conspicuous than synthetic patches, but sample-dependent placement may weaken backdoor implantation across aggregation rounds. This challenge is compounded in decentralized FL (DFL), where topology-dependent peer aggregation repeatedly mixes local models. CACTUS converts label-consistent semantic pairs into target-directed representation shifts. Mask-guided, modality-specific operators isolate trigger effects, couple them across samples, and apply the shifts counterfactually to clean non-target embeddings before peer aggregation. Experiments cover speech, text, tabular, and image tasks under nine aggregation rules. With 30\% malicious nodes, CACTUS reaches a nine-rule mean attack success rate (ASR) of 51.2\% on Speech Commands and the highest nine-rule mean ASR among evaluated attacks on three of four modalities. Sensitivity analyses show that ASR varies with network topology and increases with the malicious-node ratio. These results indicate that CACTUS can propagate backdoors through repeated DFL aggregation.

---


### 127. [WiFlow: Estimating Optical Flow using WiFi Channel State Information](https://arxiv.org/abs/2609.02452)

**<font color=#1a73e8>作者：</font>** Thomas Weigel, Simon Kiefhaber, Fabian Portner 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Knowing where and how fast objects are moving within a scene is important across various domains. Usually, cameras are used to capture the data necessary for this task, but adding cameras often raises privacy concerns, and the quality of captured frames is heavily influenced by lighting conditions. In this work, we explore using WiFi channel state information (CSI) instead of camera frames for optical flow estimation. We propose WiFlow, a CSI based flow estimator, a preprocessor evaluation for CSI, and three model architectures that offer different trade-offs between accuracy and complexity. Further, we create the first dataset for training and evaluating CSI-based optical flow estimators, and our experiments provide insights into key design elements for this task. Code and data are available at this https URL.

---


### 128. [VIPS: Vehicle-Infrastructure Cooperative Planning Benchmark via Pseudo-Simulation](https://arxiv.org/abs/2609.02462)

**<font color=#1a73e8>作者：</font>** Hoonhee Cho, Jae-Young Kang, Giwon Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> End-to-end autonomous driving in urban environments requires robust decision-making under partial observability and complex multi-agent interactions. Severe occlusions and dense traffic at intersections limit the perception capability of single-agent systems, motivating recent efforts on Vehicle-to-Infrastructure (V2I) cooperation for perception and planning. However, existing evaluation protocols face a fundamental trade-off: open-loop evaluation fails to capture error accumulation and recovery from deviations, while closed-loop evaluation is costly, difficult to scale, and often relies on simulated environments that may suffer from domain gaps. To bridge this gap, we propose VIPS, a benchmark for cooperative autonomous driving in V2I settings based on pseudo-simulation. VIPS extends pseudo-simulation by integrating vehicle and infrastructure observations. This enables scalable yet realistic evaluation of robustness and error propagation without full simulation. We further present CoS-V2X, a cooperative planning framework based on sparse representations. CoS-V2X models vehicle-infrastructure interactions using compact features for efficient communication and robust decision-making under heterogeneous observations. Code and dataset are available at this https URL.

---


### 129. [Evaluating ML-based Intrusion Detection Systems: The Illusion of Model Efficacy](https://arxiv.org/abs/2609.02469)

**<font color=#1a73e8>作者：</font>** Achilleas Spanos, Ioanna Kantzavelou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Intrusion Detection has been revolutionized due to the integration of Machine Learning. Improved detection rates, reduced false alarms, and optimized algorithms contribute to the perception of improved systems with optimal accuracy and near-perfect performance, the illusion of model efficacy. However, the value of this effectiveness diminishes when confronted with unseen attacks. In this paper, we go beyond solely algorithmic enhancements and metric adjustments in ML-based Network Intrusion Detection Systems. We design an experiment to test the generalization capabilities of certain classifiers on unseen attacks. Our approach examines the dimensionality parameter's impact through two experimental methodologies, which are applied in two distinct settings. The experimental findings reveal how effectively the models could identify even a fraction of unseen attacks and underscore structural weaknesses in ML-based IDS research and evaluation techniques. Finally, seven evaluation criteria are outlined to address these challenges.

---


### 130. [Learning to Track from Privileged Target Appearances](https://arxiv.org/abs/2609.02471)

**<font color=#1a73e8>作者：</font>** Xin Chen, Jiao Xu, Dong Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Target templates define what a visual tracker searches for, yet the templates available at inference trade off localization certainty with appearance freshness: the initial ground-truth template is exact but becomes stale, whereas recent templates better reflect the current appearance but are cropped from uncertain predictions. We quantify this bottleneck with a non-deployable oracle that supplies an exact current-frame target crop, improving AUC on LaSOT by 15.2 percentage points. This gap reveals a training-only opportunity: frame-level ground truths provide exact current- and future-frame target crops, although such crops are unavailable at deployment. We introduce Privileged Appearance Transfer for Tracking (PATT), a teacher-student training framework that transfers these privileged appearances to a deployable tracker through multi-level representation prediction. The privileged teacher observes exact target crops from past, current, and future frames, whereas the student receives only past-frame templates and learns to predict the teacher's search representations. To avoid transferring unreliable teacher signals, PATT weights this transfer by the teacher's relative localization advantage over the student and its absolute localization accuracy. After training, the teacher, latent predictor, reliability weights, and privileged crops are removed, leaving standard student-only inference. Across seven benchmarks at two model scales, PATT achieves consistent gains under both long- and short-term tracking protocols.

---


### 131. [UnCapsTSR: An Unsupervised Transformer-based Image Super-Resolution Approach for Capsule Endoscopy Images](https://arxiv.org/abs/2609.02476)

**<font color=#1a73e8>作者：</font>** Anjali Sarvaiya, Shubh Kawa, Lalit Agrawal 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Wireless Capsule Endoscopy (WCE) captures and streams video while passing through a patient's Gastrointestinal (GI) tract and is used to examine its irregularities. Although advantageous over conventional endoscopy, WCE suffers from limitations related to capsule size and wireless transmission, resulting in images with coarser resolution. This work presents UnCapsTSR, an unsupervised transformer-based Generative Adversarial Network (GAN) framework for improving the spatial resolution of Low-Resolution (LR) WCE images. The proposed method accomplishes SR without explicit degradation estimation of real-world LR data and eliminates the need for true LR-HR pairs. UnCapsTSR employs a Bilateral Total Variation (BTV) loss to ensure spatial continuity in SR images. A newly curated dataset from the Kvasir Capsule dataset is also presented for training WCE SR models. Generalizability is validated on KID and GIANA datasets that are not used during training. A new non-reference metric, Endoscopy Quality Metric (EndoQM), is introduced for quantitative evaluation of domain-specific WCE data. Experiments demonstrate consistent improvement over state-of-the-art unsupervised SR approaches using NIQE, BRISQUE, PIQE, and EndoQM. Statistical evaluation shows 40 to 80 percent improvement in EndoQM from LR to SR across the evaluated datasets.

---


### 132. [RINSE: Robust Target-Time Normality Estimation for Zero-Shot Graph Anomaly Detection](https://arxiv.org/abs/2609.02497)

**<font color=#1a73e8>作者：</font>** Taufikur Rahman Fuad, Md Abrar Jahin, Amir Hussain  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-shot graph anomaly detection seeks to deploy a detector trained on source graphs to unseen, unlabeled targets, yet domain shift can make source-derived notions of normality unreliable. We introduce RINSE (Robust Iterative Normality Self-Estimation), a gradient-free target-time framework that keeps the source-trained detector fixed while sequentially estimating target normality, representation calibration, and evidence reliability from the target graph. Its core idea is to identify a reliable subset of low-residual target nodes, use them to construct a trimmed target-aware normality model, and combine complementary anomaly evidence through reliability-gated rank fusion and encoder ensembling. Across eight unseen target graphs, RINSE achieves the highest average AUPRC among the evaluated methods under two separate preprocessing protocols, while block ablations and sensitivity analyses support the combined design. These results support robust target-time estimation as a practical approach to generalist graph anomaly detection without target labels, gradients, or per-target tuning.

---


### 133. [SR-Edit: Region-Aware Image Editing via Self-Refinement](https://arxiv.org/abs/2609.02504)

**<font color=#1a73e8>作者：</font>** Andong Wang, Zehua Chen, Yuxuan Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> With the recent rapid progress in generative models, image editing has made remarkable advances, yet achieving faithful edits that precisely modify only the target regions while strictly preserving all other regions remains challenging. Since externally provided region annotations are often difficult to obtain in practice, a growing body of work seeks to improve preservation by automatically inferring edit and non-edit regions, and then enforcing consistency on the latter. However, these approaches still suffer from inaccurate region estimation and heuristic correction strategies that distort the native inference process, making methods designed for fidelity themselves a new source of artifacts. We propose SR-Edit, an image editing framework that overcomes these issues via iterative self-refinement. Specifically, at each iteration, SR-Edit first (i) extracts progressively precise and self-consistent region separation from the model's own predictions by lightweight post-processing, and then (ii) enforces preservation in non-edit areas through correction updates that remain aligned with the original sampling dynamics. Extensive experiments demonstrate that SR-Edit achieves superior preservation and overall image quality compared to existing editing techniques.

---


### 134. [Rethinking the Teacher-Student Framework for Test-Time Adaptation](https://arxiv.org/abs/2609.02507)

**<font color=#1a73e8>作者：</font>** Damian Sójka, Marc Masana, Bartłomiej Twardowski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-Time Adaptation (TTA) has recently emerged as a promising strategy that allows the adaptation of pre-trained models to changing data distributions at deployment time, without access to any labels. To mitigate error accumulation, researchers have widely adopted the teacher-student framework, though its long-term stability is often taken for granted. In this work, we challenge the common strategy of setting the teacher weights to an exponential moving average of the student by showing that error accumulation still occurs, although it is mostly apparent on longer sequences compared to those commonly utilized. We analyze the stability-plasticity trade-off within the teacher-student framework and propose to use an intransigent teacher that does not update its weights. Surprisingly, we show that this simple change allows TTA methods to significantly improve their performance on multiple datasets with longer scenarios and result in increased robustness to changes in hyperparameters. Finally, we show that those changes can be seamlessly and effectively applied to various architectures and experimental setups, including semantic segmentation. The code is available at this https URL.

---


### 135. [Orthogonal Ensembles and Tested Explanations for Performer-Independent Body-Motion Emotion Recognition](https://arxiv.org/abs/2609.02510)

**<font color=#1a73e8>作者：</font>** Naoto Nishida, Yoshio Ishiguro  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study body-only, 12-class acted-emotion classification from skeleton motion under leave-performer-out (LPO) evaluation, a hard, underdetermined setting: chance is 8.3%, and a protocol-matched reproduced STGCN++ baseline reaches only 25.73 +/- 4.03% Macro-F1. We show that reliable gains come not from a new architecture but from combining eleven models with orthogonal error modes: under 10-fold LPO cross-validation on the labeled training performers, an equal-weight logit-mean ensemble reaches 36.80 +/- 4.00% per-fold Macro-F1, a protocol-matched +11.07 pp (+43% relative) over the same-split reproduced baseline. Our central contribution is a tested explanation suite: for a strong ensemble member, part-masking and counterfactual edits show (rather than assert) that its decisions depend on motion-grounded body-region evidence, and this region saliency aligns with rule-based Laban Movement Analysis (LMA) attributes far more than with classical kinematics: region-level saliency-LMA Spearman rho = +0.500 versus +0.033, roughly 15x, and the alignment holds for the submitted 11-way ensemble itself at rho = +0.517; the audit is post hoc and needs no retraining. The same suite faithfully reports a negative: within-window temporal saliency is diffuse rather than localized.

---


### 136. [Spectral Initialization and Scheduled Graph Smoothness for Uncertain Knowledge Graph Completion](https://arxiv.org/abs/2609.02519)

**<font color=#1a73e8>作者：</font>** Md Abrar Jahin, Taufikur Rahman Fuad, Jay Pujara 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertain knowledge graphs (UKGs) extend knowledge graphs by assigning each triple a continuous confidence score. Since most possible triples lack observed confidences, recent methods rely on semi-supervised learning to generate pseudo-labels. These methods initialize entity embeddings without using the confidence-weighted graph, discarding its global community and hub structure. We introduce QUEST, which adds no trainable parameters to the standard confidence-distribution learning pipeline. First, QUEST initializes entity embeddings using the smallest non-trivial eigenvectors of the confidence-weighted graph Laplacian, incorporating community and hub structure before training. Second, QUEST applies an unbiased mini-batch Dirichlet energy regularizer to enforce early-stage structural consistency. On two UKG datasets, QUEST improves confidence prediction and link prediction on six of eight metric-dataset pairs over prior methods and matches the previous best on the remaining two, while removing the instability spike observed on dense graphs. These results indicate that spectral structural priors combined with a graph Dirichlet energy regularizer improve accuracy, training stability, and checkpoint reliability in UKG completion.

---


### 137. [Doppio: A Dataset for Contactless Weight Estimation of Falling Particles](https://arxiv.org/abs/2609.02528)

**<font color=#1a73e8>作者：</font>** Simon Kiefhaber, Jan-Martin O. Steitz, Julia Grabinski 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Measuring the mass of powder, including falling particles, is a common task in industrial applications. While scales are effective for static measurements, many applications require contactless sensing, where existing solutions are often costly, application-specific, and technically complex. In this work, we investigate computer vision as a practical alternative for contactless mass estimation. As an accessible real-world case study, we focus on coffee grinding and introduce \emph{Doppio}, a novel video dataset capturing videos of falling ground coffee, paired with precise, per-frame ground-truth weight measurements. To demonstrate contactless measuring, we evaluate deep learning-based approaches ranging from purely spatial feed-forward networks to recurrent spatio-temporal models. These models are analyzed with respect to their predictive accuracy and computational trade-offs. We demonstrate that deep learning-based computer vision models accurately estimate the cumulative weight of falling particles, establishing a solid foundation for future vision-based contactless measurement solutions.

---


### 138. [Fine-Grained Anomaly Perception in Wild UGC-Enhanced Images: A Comprehensive Dataset and Difference-Fusion Framework](https://arxiv.org/abs/2609.02529)

**<font color=#1a73e8>作者：</font>** Yan Zhong, Gefei Chen, Qiufang Ma 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image enhancement and restoration have become standard back-end operations on short-video and social media platforms to boost UGC visual experience. Yet these processes inevitably introduce visual anomalies--especially in faces, texts, and textures--that directly undermine perceptual fidelity and viewer trust. While existing IQA methods perform well on classic distortions, they target holistic quality assessment and fail to capture the specific, localized anomalies caused by enhancement algorithms in real-world UGC. To bridge this gap, we formally define a new task-quality Anomaly Perception for UGC image Enhancement (UEAP), and contribute the first UEAP benchmark dataset, named UEAP-4k, curated from the real business scenarios. It provides fine-grained annotations for anomaly categories, localization and severity levels. Furthermore, we propose a Difference-Fusion Anomaly Perception Method (DFAP-UGC) for wild UGC-enhanced images, which leverages explicit problem-reference difference fusion with dense spatial querying, regional verification, and quality-aware ranking, enabling robust anomaly identification in challenging scenarios. To handle the inherent coupling of subtasks in this new task, we propose a Locality-Aware Dynamic Task Prioritization (LADTP) training strategy that enables effective end-to-end learning and eliminates multi-stage overhead. Extensive experiments show that our method outperforms baselines adapted from classical approaches for this task, validating the value of this dataset and the superior of DFAP-UGC for robust UGC-enhanced image anomaly perception. Code and data will be public.

---


### 139. [Spatially Aware World Action Model via Geometric Latent Diffusion](https://arxiv.org/abs/2609.02531)

**<font color=#1a73e8>作者：</font>** Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> World Action Models (WAMs) leverage the capabilities of large-scale pretrained video diffusion models to jointly predict future observations and actions, inheriting rich visual and physical priors from internet-scale video. This has made them a promising paradigm for robot policy learning, yet the prevailing models operate exclusively on RGB observations and do not leverage 3D information. To bridge this gap, we introduce a Spatially Aware World Action Model (SA-WAM), which repurposes a pretrained video model for joint action, RGB, and depth prediction, enabling 3D-aware world modeling and action prediction within a single diffusion backbone. We use a nonlinear encoding that maps the unbounded depth signal into the bounded input domain expected by the frozen VAE tokenizer. This allows us to reuse the tokenizer without 3D-specific fine-tuning, incorporating geometric information without sacrificing the pretrained priors. SA-WAM achieves state-of-the-art results on the RoboCasa and LIBERO-Plus benchmarks, while simultaneously improving future-state predictions. Furthermore, SA-WAM outperforms strong baselines in real-world evaluation using a UR5 robotic arm, with strong gains in randomized environments. We analyze the correlation between world model prediction quality and rollout success, providing insights into WAM performance and avenues for its improvement.

---


### 140. [A Comparative Study of Graph Representations for GNN-Based Power Grid Control in L2RPN](https://arxiv.org/abs/2609.02538)

**<font color=#1a73e8>作者：</font>** Adrian Degenkolb, Qiong Huang, Benjamin Schäfer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph construction is a critical but underexamined design choice in deep reinforcement learning for power grid control. We present a controlled experimental comparison of different graph representations, including physical topology, electrical-sensitivity, and hybrid variants for topology control in the Learning to Run a Power Network (L2RPN) environment. Our findings indicate that matching graph complexity to task granularity is more important than maximizing representational richness, and highlight the importance of controlled representation studies at scale.

---


### 141. [TrajMind: Chaining Role-Specialized LoRAs for Fast-and-Slow Collective Trajectory Anomaly Diagnosis](https://arxiv.org/abs/2609.02540)

**<font color=#1a73e8>作者：</font>** Jiahao Wu, Zhenqun Yang, Chen Jason Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diagnosing collective anomalies from urban trajectories is increasingly important for traffic governance, as it reveals what happened, who was involved, and where and when the event occurred. Existing detectors efficiently produce scores or labels, whereas vision--language pipelines provide richer semantics; neither couples verifiable diagnosis with low-latency monitoring. The central challenge is to recognize collective patterns and recover exact event details from the source trajectories without running the full diagnostic pipeline for every monitored window. We therefore separate always-on screening from on-demand diagnosis: screening raises alerts, while diagnosis releases only source-verified what--who--where--when records. We present TrajMind, a fast-and-slow framework that switches three role-specialized LoRA adapters over one frozen vision--language backbone. Its slow path, \textit{TrajMind$_{\text{slow}}$}, chains canvas-based typing, type-conditioned localization over serialized trajectories, and executable verification, yielding structured, evidence-backed diagnoses. Additionally, the fast path, \textit{TrajMind$_{\text{fast}}$}, screens each window in a single text-only pass, delivering efficient structured alerts. Extensive experiments show that, TrajMind$_{\mathrm{slow}}$ outperforms the strongest baselines by at least $15.3$ percentage points in anomaly typing and $13.8$ percentage points in localization. These gains persist under cross-city transfer, and TrajMind$_{\mathrm{fast}}$ reduces latency by $41.1\%$ and maintains binary balanced accuracy of at least $93.5\%$. Together, TrajMind delivers accurate, evidence-backed diagnoses across cities and efficient front-line monitoring.

---


### 142. [ProbeMatchDTI: Probe-Driven Multi-Scale Biochemical Pattern Matching for Drug-Target Interaction Prediction](https://arxiv.org/abs/2609.02549)

**<font color=#1a73e8>作者：</font>** Quan Hao, Mengyue Fan, Zifan Dong 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Drug-target interaction (DTI) prediction is an important task in AI-driven drug discovery. Although recent biochemical representation learning methods have improved DTI prediction, their passive feature aggregation tends to favor dominant molecular patterns while suppressing weak yet binding-relevant signals, such as functional groups and residue-context patterns, limiting the modeling of multi-scale biochemical correspondences. To address this issue, we propose ProbeMatchDTI, a pattern-probe-driven framework comprising IterProbe and BindingProbe. IterProbe explicitly retains contextual states across refinement depths and uses learnable probes to select them at each position before cross-entity matching, thereby preserving weak biochemical patterns and strengthening associations among functional groups, local motifs, and molecular scaffolds. BindingProbe then characterizes cross-entity drug-protein complementarity at local biochemical-unit and whole-pair levels, jointly modeling fine-grained interactions and multi-scale correspondences while preserving weaker binding-relevant associations. Extensive experiments demonstrate the superiority of ProbeMatchDTI, achieving 2.0% and 0.5% higher AUC-ROC on BindingDB and DrugBank, respectively. Feature-level pattern analyses further characterize its probe-driven behavior in cross-scale biochemical pattern matching. We further connect ProbeMatchDTI predictions with an evidence-guided downstream drug-discovery workflow, demonstrating their utility for candidate refinement and validation planning. Our code is available at this https URL

---


### 143. [RGB-to-IR image translation for infrared vehicle detection in unseen UAV domains](https://arxiv.org/abs/2609.02556)

**<font color=#1a73e8>作者：</font>** Thijs A. Eker, Ella P. Fokkinga, Jan Erik van Woerden 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Synthetic training data is crucial for developing vision AI when real-world data is scarce, as in thermal infrared (IR) aerial vehicle detection. While abundant UAV RGB imagery motivates RGB-to-IR translation for data augmentation, unobservable thermal traits (e.g., engine heat) make learning transferable mappings challenging. This work investigates whether modern generative translators can overcome this cross-modal gap to improve infrared vehicle detection on unseen UAV target domains. Translators are trained on paired RGB-IR source datasets and applied to RGB training images from held-out target datasets to generate synthetic IR data. Evaluated methods include supervised GANs, ControlNet-based diffusion models, and foundation-model editing via LoRA. The resulting synthetic IR imagery is used to train RF-DETR vehicle detectors, which are evaluated on unseen IR target test splits across five aerial datasets, with Kust4K and VTUAV serving as target domains. Synthetic IR consistently outperforms RGB and grayscale baselines. Stable Diffusion 3.5 with ControlNet yields the best results, improving mAP from 50.8 to 60.1 on Kust4K and from 25.6 to 38.4 on VTUAV compared to models trained only on source-domain IR data. Increasing output diversity via multiple seeds (+1.1 mAP) and prompt variations (+3.3 mAP) provides additional gains on VTUAV. Although a performance gap to real target IR data remains, generative RGB-to-IR translation effectively mitigates IR data scarcity and improves cross-domain aerial vehicle detection.

---


### 144. [Stereo 4D Radar for 3D Object Detection: Integrating Geometric Alignment and Absolute Velocity Estimation](https://arxiv.org/abs/2609.02560)

**<font color=#1a73e8>作者：</font>** Seung-Hyun Song, Dong-Hee Paek, Woong-Chan Byun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Four-dimensional (4D) Radar is a powerful sensing modality capable of detecting surrounding three-dimensional (3D) objects under diverse weather conditions and providing Doppler-based motion information. However, raw 4D Radar signals contain significant clutter from road surfaces, guardrails, and surrounding vehicles, along with multipath-induced ghost reflections and the receiver's inherent noise floor. Consequently, preprocessing algorithms designed to remove such invalid measurements often make the Radar data excessively sparse. Moreover, the Doppler measurements provided by 4D Radar describe only the radial component of an object's velocity, limiting their ability to recover the full motion state. In this paper, we introduce a stereo 4D Radar-based 3D object detection framework that exploits the geometric disparity between left and right Radars to estimate the absolute velocity of objects and achieve more robust perception through the fusion of their complementary features. The effectiveness of the proposed framework is validated on our in-house stereo 4D Radar dataset, demonstrating performance gains of 8.82 points in AP 3D and 9.0 points in AP BEV over state-of-the-art mono 4D Radar baselines. These results demonstrate that absolute velocity estimation combined with stereo geometry-aware feature fusion leads to substantial improvements in 3D object detection.

---


### 145. [Online Reinforcement Learning in the Met Office Unified Model through Distributed Model-Agent Coupling](https://arxiv.org/abs/2609.02566)

**<font color=#1a73e8>作者：</font>** Pritthijit Nath, Sebastian Schemm, Peter Haynes 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine-learnt corrections can complement numerical weather prediction only if they adapt to the evolving model state while preserving dynamical consistency and numerical stability. To test this within a global forecasting model, we couple the Met Office (UKMO) Unified Model (UM) with distributed RL agents through rank-local tensors. A DDPG actor shares weights across the 70 vertical model levels of each atmospheric column and applies bounded potential-temperature corrections to the model tendencies. Across ten nudged training forecasts, nudging calculations towards the UKMO operational analysis provides an immediate counterfactual target. The frozen policy is then evaluated in a non-nudged forecast for inference. The coupled workflow successfully completes training and remains numerically stable in the evaluated case. Relative to a matched native UM forecast at +6 h, the learnt policy reduces Z$_{500}$ MAE in four of six latitude bands, including reductions of 45.8% and 40.8% in the northern and southern tropics. MSLP error too decreases in three bands, with a maximum reduction of 27.3% at 0-30°N. This single-case experiment demonstrates significant promise and feasibility of distributed online learning followed by non-nudged inference, laying the groundwork for RL-based bias correction and parametrisations within operational systems.

---


### 146. [Learning-Based Reconstruction Attacks on Coordinate-Obfuscated Point Clouds](https://arxiv.org/abs/2609.02568)

**<font color=#1a73e8>作者：</font>** Mohammad Waquas Usmani, Susmit Shannigrahi, Michael Zink  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Volumetric video based on point cloud representations enables immersive virtual and augmented reality applications but introduces significant challenges for efficient and secure content delivery. Prior work proposed a selective coordinate encryption framework for point clouds that encrypts only a subset of coordinates, reducing computational costs while visually degrading unauthorized content. However, it remains unclear whether the remaining unencrypted information is sufficient to enable content reconstruction.
In this paper, we evaluate the robustness of selective coordinate encryption against machine learning-based reconstruction attacks. We consider an attacker with access to selectively encrypted point clouds attempting to recover encrypted coordinates without decryption by exploiting spatial and geometric correlations in the unencrypted data. We evaluate PointNet and Random Forest models under two encryption granularities: \texttt{X}, where all $X$ coordinates are encrypted, and \texttt{2X}, where every second $X$ coordinate is encrypted.
Our results show that reconstructing fully encrypted $X$ coordinates remains challenging, whereas the \texttt{2X} scheme leaks sufficient information through neighboring coordinates to enable accurate reconstruction. These findings demonstrate that the security of selective coordinate encryption depends strongly on encryption granularity.

---


### 147. [EEG-based Visual Retrieval and Reconstruction: From Neurally Visible Optimal Layer to Hierarchical Diffusion Generation](https://arxiv.org/abs/2609.02582)

**<font color=#1a73e8>作者：</font>** Minyi Wang, Zhenqin Wu, Rihui Li  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Decoding visual perception from electroencephalography (EEG) is important for non-invasive brain-computer interfaces (BCIs). However, most existing visual decoding pipelines directly align EEG features with semantic features from pretrained vision models. Those EEG signals carry information at more than one level and this practice disregards the varying neural visibility of different visual components in EEG signals, leading to cross modal mismatches and incomplete information use. In this work, we address this limitation through layer-wise contrastive learning. For each subject, the intermediate CLIP layer that maximizes retrieval performance is selected as the Neural Visibility Optimal Layer (NVOL). Built on NVOL, a hierarchical framework couples retrieval and generation through a shared intermediate representation. The retrieval branch fuses multi-NVOL features, aligns them to image embeddings via contrastive learning, and applies cross-domain similarity local scaling (CSLS) at test time to mitigate hubness. The generation branch reconstructs subject-specific NVOL features from EEG using a conditional diffusion prior, maps them to CLIP space through a lightweight adapter, and drives a pretrained Stable Diffusion XL model. Experimental validation on THINGS-EEG showed that, NVOL-based retrieval achieves 78.1\% mean Top-1 accuracy in 200-way retrieval, rising to 86.4\% with CSLS. Two-stage NVOL-to-semantic reconstruction also outperforms single-stage final-layer diffusion on semantic and structural metrics. By aligning EEG with layer-wise neural visibility rather than fixed high-level semantics, the proposed framework improves both retrieval accuracy and image reconstruction in EEG-based visual decoding.

---


### 148. [Generalizable Brain Tumor Segmentation with Self-Training and Tumor-Aware Deformations](https://arxiv.org/abs/2609.02600)

**<font color=#1a73e8>作者：</font>** Henrique Zan Grande, Jeovane Honorio Alves, Rayson Laroca 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This work presents an approach to the Generalizability Across Tumors (BraTS-GoAT) task of the BraTS 2026 Challenge, which focuses on robust segmentation of brain tumor sub-regions across a heterogeneous patient population. The proposed method employs the nnU-Net framework with a large residual encoder architecture, integrating a semi-supervised learning technique with pseudo-labels generated from the unlabeled training data and a tumor-aware deformable augmentation that locally deforms the lesion while preserving the surrounding anatomy. We evaluate the individual contributions of each component, as well as their combination, using varying proportions of the most confident pseudo-labeled cases. The submitted configuration for the generalization task achieves Dice and NSD scores of 0.881 and 0.473 for Whole Tumor, 0.817 and 0.490 for Tumor Core, and 0.775 and 0.533 for Enhancing Tumor on the BraTS-GoAT validation set, improving over the labeled-only baselines across all tumor regions and confirming that self-training and the proposed augmentation are complementary. Our source code is publicly available at this https URL.

---


### 149. [Predictors of Loneliness in Older Adults Using Multimodal Analysis of Speech and Language](https://arxiv.org/abs/2609.02606)

**<font color=#1a73e8>作者：</font>** Vinmay Khandode, Sai Karthik Kosuri, Neil K. R. Sehgal 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Loneliness is a critical public health issue among older adults, linked to higher risks of depression, cognitive decline, and mortality. Scalable, objective methods for its detection remain limited, particularly in natural conversational contexts. We analyzed speech and language markers of loneliness in 310 older adults using semi-structured telephone interviews to help understand how they process feeling lonely and how their language differs at different levels of feeling loneliness. Our multimodal framework combined linguistic features (psycholinguistic dictionaries, n-grams, and topic models) with acoustic features (pitch, tone, loudness) to examine associations with self-reported loneliness scores. Both predefined and data-driven methods captured patterns in verbal content and vocal delivery. Higher loneliness was associated with negations(r = 0.11), negative tone(r = 0.12), and conflict-related language. Lower loneliness was linked to social references(r = -0.18), motivational drives(r = -0.11), and emotional richness in speech(r = -0.12). We also found that the multimodal model (r = 0.298) outperforms the text-only and audio-only models. Findings suggest that loneliness manifests through both linguistic and acoustic cues, supporting the potential of speech-based analysis in psychological assessments and as an early indicator of emotional loneliness when used alongside existing assessments, rather than as standalone diagnostic tools.

---


### 150. [AffectDelta: Beyond Emotion Labels for Image Editing](https://arxiv.org/abs/2609.02616)

**<font color=#1a73e8>作者：</font>** Xingzu Zhan, Lin Gu, Ruogu Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Emotion-driven image editing aims to evoke a specified target emotion by modifying emotion-relevant visual cues in a source image, while preserving the overall composition and semantic-structural coherence of the original scene. Existing scene-level editors typically specify the target with a single emotion category and often learn visual transformations from operation-level text instructions. A category collapses a mixed affective endpoint into one dominant label, while language cannot precisely quantify how coexisting emotions should increase, decrease, or remain stable. We introduce AffectDelta, a source-aware editor that treats editing as a transition between eight-dimensional emotion distributions. A frozen Emotion Distribution Predictor estimates the source state, and the signed source-to-target difference encodes the direction and magnitude of the requested transition. Within AffectDelta, an internal transition encoder and a source-aware diffusion backbone jointly translate this signal into context-dependent semantic and appearance changes. To train this formulation, we construct AffectPair-249K, comprising 248,841 source-target pairs with predicted eight-dimensional distributions and spanning both cross-category and within-category transitions. Experiments against six baselines, combining quantitative evaluation with qualitative comparisons, demonstrate improved affective alignment and content preservation, while ablations validate our design choices. Code and dataset will be made publicly available upon acceptance.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-187](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
