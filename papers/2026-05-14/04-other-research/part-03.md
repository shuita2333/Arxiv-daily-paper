# 📦 其他研究 | 2026年05月14日

> 本类共 **396** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

---

### 101. [HamBR: Active Decision Boundary Restoration Based on Hamiltonian Dynamics for Learning with Noisy Labels](https://arxiv.org/abs/2605.11383)

**<font color=#1a73e8>作者：</font>** Ningkang Peng, Jingyang Mao, Qianfeng Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In large-scale visual recognition and data mining tasks, the presence of noisy labels severely undermines the generalization capability of deep neural networks (DNNs). Prevalent sample selection methods rely primarily on training loss or prediction confidence for passive screening. However, within a feature space degraded by noise, decision boundaries undergo systematic boundary collapse. This phenomenon hinders the ability of the model to distinguish between hard clean samples and noisy samples at the decision margins, thereby creating a significant performance bottleneck. This study is the first to emphasize the pivotal importance of active boundary restoration for noise-robust learning. We propose HamBR, a novel paradigm based on Hamiltonian dynamics. The core approach leverages the Spherical Hamiltonian Monte Carlo (Spherical HMC) mechanism to actively probe inter-class ambiguous regions within the representation space and synthesize high-quality virtual outliers. By imposing explicit repulsion constraints via energy-based modeling, these synthesized samples establish robust energy barriers at the decision boundaries. This mechanism forces real samples to move from dispersed overlapping regions toward their respective class centers, thereby restoring the discriminative sharpness of the decision boundaries. HamBR demonstrates exceptional versatility and can be integrated as a plug-and-play defense module into existing semi-supervised noisy label learning frameworks. Empirical evaluations show that the proposed paradigm significantly enhances the discriminative accuracy of hard boundary samples, achieving state-of-the-art (SOTA) performance on CIFAR-10/100 and real-world noise benchmarks. Furthermore, it exhibits superior convergence efficiency and reliable robustness, while improving significantly the capability of the model for Out-of-Distribution (OOD) detection.

---


### 102. [Revisiting Privacy Preservation in Brain-Computer Interfaces: Conceptual Boundaries, Risk Pathways, and a Protection-Strength Grading Framework](https://arxiv.org/abs/2605.11386)

**<font color=#1a73e8>作者：</font>** Lei Sun, Xiuqing Mao, Shuai Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Brain-computer interfaces (BCIs) are moving rapidly from laboratory research into clinical, edge, and real-world settings. Under ISO/IEC 8663:2025, a BCI is a direct communication link between central nervous system activity and external software or hardware systems. This link expands privacy risk beyond raw neural-signal leakage: neural data, derived representations, model assets, and decoded outputs can be re-associated with individuals across collection, transmission, storage, training, inference, and feedback, or used to infer information beyond what a task requires. Starting from the general BCI paradigm, this review deffnes privacy-protection boundaries, protection objects, and the relationship between user data privacy and model privacy within a shared risk pathway. It then proposes a three-dimensional framework - protection object, lifecycle stage, and dominant protection-strength level - to classify existing work into four levels of protection strength. Finally, mental privacy and neuroethical risks are treated as open issues, emphasizing that BCI privacy protection should not only obscure data but also disentangle task-irrelevant sensitive information while preserving downstream utility. Keywords: Brain-computer interface, Neural data privacy, User data privacy, Model privacy, Disentanglement of task-irrelevant sensitive information, Protection-strength grading, Neuroethical risks

---


### 103. [Transformer Interpretability from Perspective of Attention and Gradient](https://arxiv.org/abs/2605.11392)

**<font color=#1a73e8>作者：</font>** Yongjin Cui, Xiaohui Fan, Huajun Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Although researchers' attention is more focused on the performance of Transformer models, the interpretation of Transformer can never be ignored. Gradient is widely utilized in Transformer interpretation. From the perspective of attention and gradient, we conduct an in-depth study of Transformer interpretation and propose a method to achieve it by guiding the gradient direction, or more precisely, the attention direction. The method enables more comprehensive interpretation of feature regions, offers detail interpretation, and helps to better understand Transformer mechanism. Leveraging the difference in how Vision Transformer (ViT) and humans perceive images, we alter the class of an image in a way that is almost imperceptible to the human eye. This class rewriting phenomenon may potentially pose security risks in certain scenarios.

---


### 104. [Modelling Expert Cognition Beyond Behaviour: towardss Interpretation, Tension, and Value Structures](https://arxiv.org/abs/2605.11393)

**<font color=#1a73e8>作者：</font>** Annie Yuan  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Existing computational models of expertise primarily focus on observable behaviour or decision outcomes, failing to capture the internal cognitive structures that generate expert reasoning. In this work, we introduce the Expert Identity Cognition Model (EICM), a three-layer framework for modelling expert cognition beyond behaviour. EICM conceptualises expert cognition as an identity-structured process operating within situational constraints, where constraints are interpreted through internal tensions arising from competing identity commitments and stabilised into value structures that guide action. Unlike behaviour-centric or constraint-driven approaches, EICM positions tension as the central cognitive mechanism connecting world structure and decision formation. We argue that expert cognition is not merely behavioural adaptation under constraints but an identity-structured negotiation process that produces stable judgement patterns across contexts. The framework provides a new perspective for modelling tacit knowledge, expert judgement, and cognitive consistency in domains including professional practice, cultural expertise, and design reasoning.

---


### 105. [More Than Meets the Eye: A Semantics-Aware Traffic Augmentation Framework for Generalizable Website Fingerprinting](https://arxiv.org/abs/2605.11402)

**<font color=#1a73e8>作者：</font>** Youquan Xian, Xueying Zeng, Lingjia Meng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning-based website fingerprinting has emerged as an effective technique for inferring the websites users visit. Although existing methods achieve strong performance on closed-world datasets, they often fail to generalize to real-world environments, especially under geographic and temporal shifts. This limitation fundamentally stems from the coupled effects of two key challenges: application-layer resource composition variability and observable feature instability induced by cross-layer encapsulation. Intertwined, these factors induce systematic shifts between underlying application semantics and observable traffic features. To address the above challenges, we propose SATA , a semantics-aware traffic augmentation framework. Specifically, SATA first performs application-layer semantic augmentation based on protocol rules, expanding the resource composition patterns within each flow and frame sequence patterns under protocol constraints. Based on these augmented frame sequences, we further introduce a cross-layer feature alignment mechanism via knowledge distillation. It aligns frame sequence with packet-length sequence features, enabling cross-layer feature alignment between enhanced semantics and observable sequences. Extensive experiments show that SATA successfully generates traffic patterns that are absent from the training set but genuinely exist in the test set, and significantly improves the performance of mainstream models across diverse and complex scenarios. In particular, in open-world settings, SATA improves ACC by 90.81% and AUROC by 48.37%. The source code of the prototype system is available at this https URL.

---


### 106. [Attributing Emergence in Million-Agent Systems](https://arxiv.org/abs/2605.11404)

**<font color=#1a73e8>作者：</font>** Ling Tang, Jilin Mei, Qian Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can simulate human-like reasoning and decision-making in individual agents. LLM-powered multi-agent systems (MAS) combine such agents to simulate population-scale social phenomena such as polarization, information cascades, and market panics. Such studies require attributing macro emergence to individual agents, but existing axiomatic methods scale combinatorially in $N$ and have been confined to $N \lesssim 10^3$, while the phenomena they explain occur at $N \geq 10^6$. We address this gap by adapting Aumann--Shapley path-integral attribution to LLM-powered MAS at million-agent scale; the resulting method satisfies all four axioms, runs four to five orders of magnitude faster than sampled Shapley on the same hardware. We use this method to test the scale gap empirically: across 14 days of public Bluesky data ($1{,}671{,}587$ active users), we compute the attribution at both full scale and the visibility-biased $N = 10^2$ convenience sample used by small-scale studies, and the two disagree structurally. At full scale the long tail and middle tier jointly carry the majority; the biased small panel attributes almost everything to a few high-follower accounts. We then prove that under any nonlinear macro indicator the disagreement cannot be reduced by post-hoc rescaling: an Attribution Scaling Bias theorem shows that no global rescaling factor can reconcile small-scale and full-scale attribution. Full-scale attribution is therefore not a methodological choice but a theoretical requirement for any nonlinear macro indicator.

---


### 107. [A Boundary-Aware Non-parametric Granular-Ball Classifier Based on Minimum Description Length](https://arxiv.org/abs/2605.11406)

**<font color=#1a73e8>作者：</font>** Zeqiang Xian, Caihui Liu, Yong Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing granular-ball classification methods are often driven by handcrafted quality measures, neighborhood rules, or heuristic splitting and stopping criteria, which may reduce the transparency of local construction decisions and hinder explicit modeling of boundary-sensitive regions. To address this issue, this paper proposes a Minimum Description Length based Granular-Ball Classifier (MDL-GBC), a boundary-aware non-parametric and interpretable granular-ball classifier. MDL-GBC formulates class-conditional granular-ball construction as a local model selection problem under the Minimum Description Length principle. For each class, samples from the target class provide positive class evidence, while samples from the remaining classes provide negative boundary evidence. For each current granular ball, three candidate explanations are compared under a unified description-length criterion: a single-ball model, a two-ball model, and a core-boundary model. The selected model determines whether the ball is retained, geometrically split, or refined into core and boundary-sensitive child balls, thereby making local construction decisions consistent with the MDL-based classification mechanism. During prediction, a class-level mixture coding rule aggregates stable granular balls of the same class and assigns the test sample by comparing class-wise coding costs. Experiments on 18 benchmark datasets show that MDL-GBC achieves competitive classification performance against classical classifiers and representative granular-ball-based methods, obtaining the best average Accuracy, Macro-F1, and average rank. These results indicate that MDL-GBC provides an effective and interpretable alternative to conventional heuristic granular-ball classification strategies.

---


### 108. [MaskTab: Scalable Masked Tabular Pretraining with Scaling Laws and Distillation for Industrial Classification](https://arxiv.org/abs/2605.11408)

**<font color=#1a73e8>作者：</font>** Bo Zheng, Yudong Chen, Zihua Xiong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Tabular data forms the backbone of high-stakes decision systems in finance, healthcare, and beyond. Yet industrial tabular datasets are inherently difficult: high-dimensional, riddled with missing entries, and rarely labeled at scale. While foundation models have revolutionized vision and language, tabular learning still leans on handcrafted features and lacks a general self-supervised framework. We present MaskTab, a unified pre-training framework designed specifically for industrial-scale tabular data. MaskTab encodes missing values via dedicated learnable tokens, enabling the model to distinguish structural absence from random dropout. It jointly optimizes a hybrid supervised pre-training scheme--utilizing a twin-path architecture to reconcile masked reconstruction with task-specific supervision--and an MoE-augmented loss that adaptively routes features through specialized subnetworks. On industrial-scale benchmarks, it achieves +5.04% AUC and +8.28% KS over prior art under rigorous scaling. Moreover, its representations distill effectively into lightweight models, yielding +2.55% AUC and +4.85% KS under strict latency and interpretability constraints, while improving robustness to distribution shifts. Our work demonstrates that tabular data admits a foundation-model treatment--when its structural idiosyncrasies are respected.

---


### 109. [Generative Diffusion Prior Distillation for Long-Context Knowledge Transfer](https://arxiv.org/abs/2605.11414)

**<font color=#1a73e8>作者：</font>** Nilushika Udayangani, Kishor Nandakishor, Marimuthu Palaniswami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While traditional time-series classifiers assume full sequences at inference, practical constraints (latency and cost) often limit inputs to partial prefixes. The absence of class-discriminative patterns in partial data can significantly hinder a classifier's ability to generalize. This work uses knowledge distillation (KD) to equip partial time series classifiers with the generalization ability of their full-sequence counterparts. In KD, high-capacity teacher transfers supervision to aid student learning on the target task. Matching with teacher features has shown promise in closing the generalization gap due to limited parameter capacity. However, when the generalization gap arises from training-data differences (full versus partial), the teacher's full-context features can be an overwhelming target signal for the student's short-context features. To provide progressive, diverse, and collective teacher supervision, we propose Generative Diffusion Prior Distillation (GDPD), a novel KD framework that treats short-context student features as degraded observations of the target full-context features. Inspired by the iterative restoration capability of diffusion models, we learn a diffusion-based generative prior over teacher features. Leveraging this prior, we posterior-sample target teacher representations that could best explain the missing long-range information in the student features and optimize the student features to be minimally degraded relative to these targets. GDPD provides each student feature with a distribution of task-relevant long-context knowledge, which benefits learning on the partial classification task. Extensive experiments across earliness settings, datasets, and architectures demonstrate GDPD's effectiveness for full-to-partial distillation.

---


### 110. [Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry](https://arxiv.org/abs/2605.11418)

**<font color=#1a73e8>作者：</font>** Shoumik Saha, Kazem Faghih, Soheil Feizi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autonomous AI agents increasingly extend their capabilities through Agent Skills: modular filesystem packages whose this http URL files describe when and how agents should use them. While this design enables scalable, on-demand capability expansion, it also introduces a semantic supply-chain risk in which natural-language metadata and instructions can affect which skills are admitted, surfaced, selected, and loaded. We study this http URL - only attacks across three registry-facing stages of the Agent Skill lifecycle, using real ClawHub skills and realistic registry mechanisms. In Discovery, short textual triggers can manipulate embedding-based retrieval and improve adversarial skill visibility, achieving up to 86% pairwise win rate and 80% Top-10 placement. In Selection, description-only framing biases agents toward functionally equivalent adversarial variants, which are selected in 77.6% of paired trials on average. In Governance, semantic evasion strategies cause malicious skills to avoid a blocking verdict in 36.5%-100% of cases. Overall, our results show that this http URL is not passive documentation but operational text that shapes which third-party capabilities agents find, trust, and use.

---


### 111. [VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors](https://arxiv.org/abs/2605.11424)

**<font color=#1a73e8>作者：</font>** Jimin Tang, Wenyuan Zhang, Junsheng Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian Splatting has achieved remarkable progress in multi-view surface reconstruction, yet it exhibits notable degradation when only few views are available. Although recent efforts alleviate this issue by enhancing multi-view consistency to produce plausible surfaces, they struggle to infer unseen, occluded, or weakly constrained regions beyond the input coverage. To address this limitation, we present VidSplat, a training-free generative reconstruction framework that leverages powerful video diffusion priors to iteratively synthesize novel views that compensate for missing input coverage, and thereby recover complete 3D scenes from sparse inputs. Specifically, we tackle two key challenges that enable the effective integration of generation and reconstruction. First, for 3D consistent generation, we elaborate a training-free, stage-wise denoising strategy that adaptively guides the denoising direction toward the underlying geometry using the rendered RGB and mask images. Second, to enhance the reconstruction, we develop an iterative mechanism that samples camera trajectories, explores unobserved regions, synthesizes novel views, and supplements training through confidence weighted refinement. VidSplat performs robustly to sparse input and even a single image. Extensive experiments on widely used benchmarks demonstrate our superior performance in sparse-view scene reconstruction.

---


### 112. [PD-4DGS:Progressive Decomposition of 4D Gaussian Splatting for Bandwidth-Adaptive Dynamic Scene Streaming](https://arxiv.org/abs/2605.11427)

**<font color=#1a73e8>作者：</font>** Jiachen Li, Guangzhi Han, Jin Wan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 4D Gaussian Splatting (4DGS) enables high-quality dynamic novel view synthesis, yet current models remain monolithic bitstreams that clients must download in full before any frame can be rendered, causing black-screen waits of tens to hundreds of seconds on mobile bandwidth and leaving 4DGS incompatible with modern adaptive-bitrate delivery. Progressive 3DGS compression alleviates this for static scenes, but it acts only on spatial anchors and cannot partition the temporal deformation networks that dominate dynamic-scene size. We present PD-4DGS, the first framework for progressive compression and on-demand transmission of 4DGS. Hierarchical Deformation Decomposition (HDD) externalises the coarse-to-fine motion hierarchy already latent in 4DGS into three independently transmittable layers -- a static scaffold, a global deformation, and a local refinement -- so that any prefix of the bitstream is already renderable, turning a single training run into a scalable, DASH/HLS-compatible bitstream. A Gaussian-entropy attribute rate-distortion loss together with a temporal mask consistency regulariser shrink the base layer while suppressing low-bitrate flicker; a capacity-weighted rollout schedule, gated online by a learnt activation rate rho, then prevents deformation-network under-training without any per-scene hyperparameter. On the Dycheck iPhone benchmark, PD-4DGS cuts the streamed bitstream by >60% at matched rendering fidelity and reduces first-frame latency from 73--930 s to ~1.7 s on a 2 Mbps link, uniquely enabling true on-demand progressive streaming for 4DGS.

---


### 113. [FastUMAP: Scalable Dimensionality Reduction via Bipartite Landmark Sampling](https://arxiv.org/abs/2605.11428)

**<font color=#1a73e8>作者：</font>** Hongmin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Exploratory analysis of high-dimensional data rarely stops at a single embedding. In practice, analysts rerun dimensionality reduction after changing preprocessing, subsets, or hyperparameters, and standard nonlinear methods can quickly become the bottleneck. We introduce FastUMAP (Bipartite Manifold Approximation and Projection), a landmark-based method designed for this repeated-use setting. FastUMAP builds a sparse point-landmark fuzzy graph, computes a Nystrom spectral warm start from the induced landmark affinity, and then refines all sample coordinates with a UMAP-style objective on the bipartite graph. The landmark ratio r = m/n provides a direct way to trade runtime against fidelity. On 9 benchmark datasets spanning 178 to 70,000 samples, FastUMAP has the lowest runtime on 7 datasets in our reported default-implementation comparison on one workstation. On MNIST and Fashion-MNIST (n=70000), it runs in about 4.6 seconds, compared with about 73--75 seconds for Barnes--Hut t-SNE, while reaching 91.4% mean kNN accuracy versus 94.6% for the strongest accuracy baseline. FastUMAP is therefore best viewed as a fast option for repeated exploratory embedding, rather than as a replacement for accuracy-first methods.

---


### 114. [Diabetic Retinopathy Classification using Downscaling Algorithms and Deep Learning](https://arxiv.org/abs/2605.11430)

**<font color=#1a73e8>作者：</font>** Nishi Doshi, Urvi Oza, Pankaj Kumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetic Retinopathy (DR) is an art and science of recording and classifying the retinal images of a diabetic patient. DR classification deals with classifying retinal fundus image into five stages on the basis of severity of diabetes. One of the major issue faced while dealing with DR classification problem is the large and varying size of images. In this paper we propose and explore the use of several downscaling algorithms before feeding the image data to a Deep Learning Network for classification. For improving training and testing; we amalgamate two datasets: Kaggle and Indian Diabetic Retinopathy Image Dataset. Our experiments have been performed on a novel Multi Channel Inception V3 architecture with a unique self crafted preprocessing phase. We report results of proposed approach using accuracy, specificity and sensitivity, which outperform the previous state of the art methods. Index Terms: Diabetic Retinopathy, Downscaling Algorithms, Multichannel CNN Architecture, Deep Learning

---


### 115. [ZeroIDIR: Zero-Reference Illumination Degradation Image Restoration with Perturbed Consistency Diffusion Models](https://arxiv.org/abs/2605.11435)

**<font color=#1a73e8>作者：</font>** Hai Jiang, Zhen Liu, Yinjie Lei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this paper, we propose a zero-reference diffusion-based framework, named ZeroIDIR, for illumination degradation image restoration, which decouples the restoration process into adaptive illumination correction and diffusion-based reconstruction while being trained solely on low-quality degraded images. Specifically, we design an adaptive gamma correction module that performs spatially varying exposure correction to generate illumination-corrected only representations to mitigate exposure bias and serve as reliable inputs for subsequent diffusion processes, where a histogram-guided illumination correction loss is introduced to regularize the corrected illumination distribution toward that of natural scenes. Subsequently, the illumination-corrected image is treated as an intermediate noisy state for the proposed perturbed consistency diffusion model to reconstruct details and suppress noise. Moreover, a perturbed diffusion consistency loss is proposed to constrain the forward diffusion trajectory of the final restored image to remain consistent with the perturbed state, thus improving restoration fidelity and stability in the absence of supervision. Extensive experiments on publicly available benchmarks show that the proposed method outperforms state-of-the-art unsupervised competitors and is comparable to supervised methods while being more generalizable to various scenes. Code is available at this https URL.

---


### 116. [Beyond Masks: The Case for Medical Image Parsing](https://arxiv.org/abs/2605.11438)

**<font color=#1a73e8>作者：</font>** Siddharth Gupta, Alan L. Yuille, Zongwei Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical imaging research has spent a decade getting very good at one thing: producing per-voxel masks. Masks tell us size, volume, and location, and a decade of clinical infrastructure rests on those outputs. Yet the report a radiologist writes contains almost nothing a mask can express. We argue that medical imaging research should adopt medical image parsing as its central output: a structured representation in which entities, attributes, and relationships are emitted together and mutually consistent. Entities are the named structures and findings, present or absent. Attributes describe those entities, capturing things like margin regularity, enhancement pattern, or severity grade. Relationships connect them, naming where one structure sits relative to another, what abuts what, and what has changed since the prior scan. A good parse satisfies three properties, in order: (1) decision (the parse names the right things in the current image), (2) reconstruction (its content is rich enough to regenerate that image), and (3) prediction (its content is rich enough to forecast how the patient state will evolve). Quantitative measurements are derived from this content; they are not predicted alongside it. To test how close the field is to producing such an output, we audit eleven representative systems against the three parsing primitives plus closure. None emits a well-formed parse. Entities are largely solved. Attributes, relationships, and closure remain near-empty. The path forward is not a new architecture. It is a commitment to a richer output, and to training signals that reward it. Segmentation taught models to measure. Parsing asks them to explain.

---


### 117. [Deep Minds and Shallow Probes](https://arxiv.org/abs/2605.11448)

**<font color=#1a73e8>作者：</font>** Su Hyeong Lee, Risi Kondor  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural representations are not unique objects. Even when two systems realize the same downstream computation, their hidden coordinates may differ by reparameterization. A probe family intended to reveal structure already present in a representation should therefore be stable under the relevant representation symmetries rather than be tied to a particular basis. We study this group action in the tractable exact setting of the final readout layer, where equivalent realizations induce affine changes of hidden coordinates. The resulting symmetry principle singles out a unique hierarchy of shallow coordinate-stable probes, with linear probes as its degree-1 member. We also show that a natural object for cross-model probe transfer is a shared probe-visible quotient--the representation modulo directions invisible to the probe family--rather than the full hidden state. Experiments on synthetic and real-world tasks support both predictions, showing where degree-2 probes help beyond linear ones and how quotient-based transfer enables coverage-aware monitor portability across model families. These results point toward a broader geometric representation theory of neural probing, with coverage-aware monitor transfer as a concrete operational consequence.

---


### 118. [Beyond Prediction: Interval Neural Networks for Uncertainty-Aware System Identification](https://arxiv.org/abs/2605.11460)

**<font color=#1a73e8>作者：</font>** Mehmet Ali Ferah, Tufan Kumbasar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> System identification (SysID) is critical for modeling dynamical systems from experimental data, yet traditional approaches often fail to capture nonlinear behaviors. While deep learning offers powerful tools for modeling such dynamics, incorporating uncertainty quantification is essential to ensure reliable predictions. This paper presents a systematic framework for constructing and training interval Neural Networks (INNs) for uncertainty-aware SysID. By extending crisp neural networks into interval counterparts, we develop Interval LSTM and NODE models that propagate uncertainty through interval arithmetic without probabilistic assumptions. This design allows them to represent uncertainty and produce prediction intervals. For training, we propose two strategies: Cascade INN (C-INN), a two-stage approach converting a trained crisp NN into an INN, and Joint INN (J-INN), a one-stage framework jointly optimizing prediction accuracy and interval precision. Both strategies employ uncertainty-aware loss functions and parameterization tricks to ensure reliable learning. Comprehensive experiments on multiple SysID datasets demonstrate the effectiveness of both approaches and benchmark their performance against well-established uncertainty-aware baselines: C-INN achieves superior point prediction accuracy, whereas J-INN yields more accurate and better-calibrated prediction intervals. Furthermore, to reveal how uncertainty is represented across model parameters, the concept of channel-wise elasticity is introduced, which is used to identify distinct patterns across the two training strategies. The results of this study demonstrate that the proposed framework effectively integrates deep learning with uncertainty-aware modeling.

---


### 119. [SpatialForge: Bootstrapping 3D-Aware Spatial Reasoning from Open-World 2D Images](https://arxiv.org/abs/2605.11462)

**<font color=#1a73e8>作者：</font>** Zishan Liu, Ruoxi Zang, Yanglin Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Large Vision-Language Models (VLMs) have demonstrated exceptional semantic understanding, yet these models consistently struggle with spatial reasoning, often failing at fundamental geometric tasks such as depth ordering and precise coordinate grounding. Recent efforts introduce spatial supervision from scene-centric datasets (e.g., multi-view scans or indoor video), but are constrained by the limited number of underlying scenes. As a result, the scale and diversity of such data remain significantly smaller than those of web-scale 2D image collections. To address this limitation, we propose SpatialForge, a scalable data synthesis pipeline that transforms in-the-wild 2D images into spatial reasoning supervision. Our approach decomposes spatial reasoning into perception and relation, and constructs structured supervision signals covering depth, layout, and viewpoint-dependent reasoning, with automatic verification to ensure data quality. Based on this pipeline, we build SpatialForge-10M, a large-scale dataset containing 10 million spatial QA pairs. Extensive experiments across multiple spatial reasoning benchmarks demonstrate that training on SpatialForge-10M significantly improves the spatial reasoning ability of standard VLMs, highlighting the effectiveness of scaling 2D data for 3D-aware spatial reasoning.

---


### 120. [Encore: Conditioning Trajectory Forecasting via Biased Ego Rehearsals](https://arxiv.org/abs/2605.11463)

**<font color=#1a73e8>作者：</font>** Conghao Wong, Ziqian Zou, Xinge You  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning and representing the subjectivities of agents has become a challenging but crucial problem in the trajectory prediction task. Such subjectivities not only present specific spatial or temporal structures, but also are anisotropic for all interaction participants. Despite great efforts, it remains difficult to explicitly learn and forecast these subjectivities, let alone further modulate models' predictions through a specific ego's subjectivity. Inspired by prefactual thoughts in psychology and relevant theatrical concepts, we interpret such subjectivities in future trajectories as the continuous process from rehearsal to encore. In the rehearsal phase, the proposed ego predictor focuses on how each ego agent learns to derive and direct a set of explicitly biased rehearsal trajectories for all participants in the scene from the short-term observations. Then, these rehearsal trajectories serve as immediate controls to condition final predictions, providing direct yet distinct ego biases for the prediction network to simulate agents' various subjectivities. Experiments across datasets not only demonstrate a consistent improvement in the performance of the proposed \emph{Encore} trajectory prediction model but also provide clear interpretability regarding subjectivities as biased ego rehearsals.

---


### 121. [Robust Multi-Agent Path Finding under Observation Attacks: A Principled Adversarial-Plus-Smoothing Training Recipe](https://arxiv.org/abs/2605.11469)

**<font color=#1a73e8>作者：</font>** Riad Ahmed  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized multi-agent path finding (MAPF) routes a team of agents on a shared grid, each acting from its own local view. The standard solution trains one shared neural policy with Proximal Policy Optimization (PPO), a popular on-policy reinforcement learning algorithm. Such a policy works well on clean observations, but a small input perturbation on one agent often changes its action, which then blocks a neighbour, and the team jams. In this paper we present two training recipes that keep the same network and the same deployment loop, yet make the policy hold up under perturbed observations. The first recipe, Adv-PPO, trains the shared policy against worst-case perturbations of its own input and selects the checkpoint by performance under adversarial perturbation. The second recipe, Adv-PPO+MACER, fine-tunes that checkpoint with a small on-policy smoothness term whose gradient follows the certified radius of randomized smoothing. On POGEMA with 8x8 maps and four agents, the unprotected PPO policy reaches 95.8% clean success but only 2.5% under the strongest attack. Adv-PPO recovers worst-case success to 59.2% at one percentage point of clean cost. Adv-PPO+MACER recovers it to 77.5% +/- 6.0% across three independent seeds at less than one percentage point of clean cost. We support these numbers with per-attack curves, a certified action-stability sanity check (which measures the smoothed-policy wrapper, not the deployed argmax policy), and side-by-side rollout storyboards that show the failure mode and the fix inside one environment instance.

---


### 122. [On the Approximation Complexity of Matrix Product Operator Born Machines](https://arxiv.org/abs/2605.11471)

**<font color=#1a73e8>作者：</font>** Chao Li, Zerui Tao, Yuchen Cong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Matrix product operator Born machines (MPO-BMs) are tractable tensor-network models for probabilistic modeling, but their efficient approximation capability remains unclear. We characterize this boundary from both negative and positive perspectives. First, we prove that KL approximation is NP-hard for MPO-BMs in the continuous setting, ruling out universal efficient approximation in the worst case. Second, for score-based variational inference, we show that, under a locality and spectral-gap conditions on the loss-induced Hamiltonian, structured targets (e.g., path-graph Markov random fields) admit MPO-BM approximations with polynomial bond dimension and provable KL guarantees. Third, under the same locality structure, we prove that polynomially many score queries suffice to estimate the induced Hamiltonian and obtain such guarantees. Our results provide a theoretical characterization of when MPO-BMs are fundamentally hard to approximate and when they become efficiently learnable.

---


### 123. [TOPPO: Rethinking PPO for Multi-Task Reinforcement Learning with Critic Balancing](https://arxiv.org/abs/2605.11473)

**<font color=#1a73e8>作者：</font>** Yuanpeng Li, Gefei Lin, Annie Qu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Soft Actor-Critic (SAC) and its variants dominate Multi-Task Reinforcement Learning (MTRL) due to their off-policy sample efficiency, while on-policy methods such as Proximal Policy Optimization (PPO) remain underexplored. We diagnose that PPO in MTRL suffers from a previously overlooked issue: critic-side gradient ill-conditioning, which may cause tail tasks to stall while easy tasks dominate the value function's updates. To address this, we propose TOPPO (Tail-Optimized PPO), a reformulation of PPO via Critic Balancing -- a set of modules that improve gradient conditioning and balance learning dynamics across tasks. Unlike prior approaches that rely on modular architectures or large models, TOPPO targets the optimization bottleneck within PPO itself. Empirically, TOPPO achieves stronger mean and tail-task performance than published SAC-family and ARS-family baselines while using substantially fewer parameters and environment steps on Meta-World+ benchmark. Notably, TOPPO matches or surpasses strong SAC baselines early in training and maintains superior performance at full budget. Ablations confirm the effectiveness of each module in TOPPO and provide insights into their interactions. Our results demonstrate that, with proper optimization, on-policy methods can rival or exceed off-policy approaches in MTRL, challenging the prevailing reliance on SAC and highlighting critic-side gradient conditioning as the central bottleneck.

---


### 124. [Deep Probabilistic Unfolding for Quantized Compressive Sensing](https://arxiv.org/abs/2605.11475)

**<font color=#1a73e8>作者：</font>** Gang Qu, Ping Wang, Siming Zheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a deep probabilistic unfolding model to address the classical quantized compressive sensing problem that leverages an unfolding framework to enhance the reconstruction accuracy and efficiency. Unlike previous unfolding methods that apply L2 projection to measurements, we derive a closed-form, numerically stable likelihood gradient projection, which allows the model to respect the true quantization physics, turning the hard quantization constraint into a soft probabilistic guidance. Furthermore, an efficient, dual-domain Mamba module is specifically designed to dynamically capture and fuse the multi-scale local and global features, ensuring the interactions between the distant but correlated regions. Extensive experiments demonstrate the state-of-the-art performance of the proposed method over previous works, which is capable of promoting the application of quantized compressive sensing in real life.

---


### 125. [FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression](https://arxiv.org/abs/2605.11478)

**<font color=#1a73e8>作者：</font>** Namyoon Lee, Yongjune Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context inference is increasingly a memory-traffic problem. The culprit is the key--value (KV) cache: it grows with context length, batch size, layers, and heads, and it is read at every decoding step. Rotation-based scalar codecs meet this systems constraint by storing a norm, applying a shared random rotation, and quantizing one coordinate at a time. They are universal and random-access, but they discard the geometry created by the normalization step. After a Haar rotation, a block of $k$ consecutive coordinates is not a product source; it is a spherical-Beta source on the unit ball. We introduce \textsc{FibQuant}, a universal fixed-rate vector quantizer that keeps the same normalize--rotate--store interface while replacing scalar tables by a shared radial--angular codebook matched to this canonical source. The codebook combines Beta-quantile radii, Fibonacci\,/\,Roberts--Kronecker quasi-uniform directions, and multi-restart Lloyd--Max refinement. We prove that the resulting vector code strictly improves on its scalar product specialization at matched rate, with a high-rate gain that separates into a cell-shaping factor and a density-matching factor. The same construction gives a dense rate axis, including fractional-bit and sub-one-bit operating points, without calibration or variable-length addresses. On GPT-2 small KV caches, \textsc{FibQuant} traces a memory--fidelity frontier from $5\times$ compression at $0.99$ attention cosine similarity to $34\times$ at $0.95$. End-to-end on TinyLlama-1.1B, it is within $0.10$ perplexity of fp16 at $4\times$ compression and has $3.6\times$ lower perplexity than scalar \textsc{TurboQuant} at $b = 2$ ($8\times$ compression), where scalar random-access quantization begins to fail.

---


### 126. [Engagement Process: Rethinking the Temporal Interface of Action and Observation](https://arxiv.org/abs/2605.11484)

**<font color=#1a73e8>作者：</font>** Jialian Li, Yuchen Cao, Junhong Liu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Task completion in digital and physical environments increasingly involves complex temporal interaction, where actions and observations unfold over different time scales rather than align with fixed observation--action steps. To model such interactions, we propose \emph{Engagement Process} (EP), an interaction formalism that inherits the decision-theoretic structure of POMDPs while making time explicit in the action--observation interface. EP represents actions and observations as decoupled event streams along time, rather than updates paired at fixed decision steps. This interface captures single-agent timing issues such as deliberation latency, delayed feedback, and persistent actions, while supporting richer agent-side organization, multi-rate coordination, and compositional interaction among subsystems. Across toy, LLM-agent, and learning experiments, EP exposes temporal behaviors hidden by step-based interfaces and enables policies to adapt under explicit time costs.

---


### 127. [Adaptive Calibration in Non-Stationary Environments](https://arxiv.org/abs/2605.11490)

**<font color=#1a73e8>作者：</font>** Junyan Liu, Haipeng Luo, Lillian J. Ratliff  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Making calibrated online predictions is a central challenge in modern AI systems. Much of the existing literature focuses on fully adversarial environments where outcomes may be arbitrary, leading to conservative algorithms that can perform suboptimally in more benign settings, such as when outcomes are nearly stationary. This gap raises a natural question: can we design online prediction algorithms whose calibration error automatically adapts to the degree of non-stationarity in the environment, smoothly interpolating between i.i.d. and adversarial regimes? We answer this question in the affirmative and develop a suite of algorithms that achieve adaptive calibration guarantees under multiple calibration measures. Specifically, with $T$ being the number of rounds and $C\in[0,T]$ being an unknown non-stationary measure defined as the minimal $\ell_1$ deviation of the mean outcomes, our algorithms attain $\widetilde{O}(\sqrt{T}+(TC)^{\frac{1}{3}})$ for $\ell_1$ calibration error and $\widetilde{O}((1+C)^{\frac{1}{3}})$ for both $\ell_2$ and pseudo KL calibration error. These bounds match the optimal rates in the stationary case ($C=0$) and recover known guarantees in the fully adversarial regime ($C=T$). Our approach builds on and extends prior work [Hu et al., 2026, Luo et al., 2025], introducing an epoch-based scheduling together with a novel non-uniform partition of the prediction space that allocates finer resolution near the underlying ground truth.

---


### 128. [Understanding and Preventing Entropy Collapse in RLVR with On-Policy Entropy Flow Optimization](https://arxiv.org/abs/2605.11491)

**<font color=#1a73e8>作者：</font>** Huimin Xu, Shuai Zhao, Xiaobao Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has become an effective paradigm for improving the reasoning ability of large language models. However, widely used RLVR algorithms, such as GRPO, often suffer from entropy collapse, leading to premature determinism and unstable optimization. Existing remedies, including entropy regularization and ratio-based clipping heuristics, either control entropy in a coarse-grained manner or rely on approximate on-policy training. In this paper, we revisit entropy collapse from a token-level entropy flow perspective. Our analysis reveals that entropy-decreasing tokens consistently outweigh entropy-increasing ones, resulting in a severely imbalanced entropy flow. This perspective provides a unified explanation of entropy collapse in existing RLVR algorithms and highlights the importance of balancing entropy dynamics. Motivated by this analysis, we propose On-Policy Entropy Flow Optimization (OPEFO), an adaptive entropy flow balancing mechanism that rescales entropy-increasing and entropy-decreasing updates according to their contributions to entropy change, while remaining strict on-policy. Experiments on six mathematical reasoning benchmarks demonstrate that OPEFO improves training stability and final performance. We will release the code and models upon publication.

---


### 129. [A Mimetic Detector for Adversarial Image Perturbations](https://arxiv.org/abs/2605.11492)

**<font color=#1a73e8>作者：</font>** Johnny Corbino  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks fool deep image classifiers by adding tiny, almost invisible noise patterns to a clean image. The standard $\ell^\infty$-bounded attacks (FGSM, PGD, and the $\ell^\infty$ variant of Carlini--Wagner) produce high-frequency, near-random sign patterns at the pixel level: nearly invisible in $\ell^2$, but carrying disproportionate gradient energy. We exploit this with a single-shot, training-free detector using the high-order Corbino--Castillo mimetic operators from the open-source MOLE library. No retraining, no surrogate classifier, no access to the network under attack: the verdict is a property of the input alone, computed in $O(HW)$ time. We validate the detector on the standard \texttt{peppers} test image at the canonical $\ell^\infty$ budget $\varepsilon = 16/255$ and observe a clean-vs-adversarial separation that grows monotonically from $3.55\times$ at order $k=2$ to $4.19\times$ at $k=6$.

---


### 130. [STRIDE: Training-Free Diversity Guidance via PCA-Directed Feature Perturbation in Single-Step Diffusion Models](https://arxiv.org/abs/2605.11494)

**<font color=#1a73e8>作者：</font>** Ankit Yadav, Arpit Garg, Ta Duc Huy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Distilled one-step (T=1) or few-step (T$\leq$4) diffusion models enable real-time image generation but often exhibit reduced sample diversity compared to their multi-step counterparts. In multi-step diffusion, diversity can be introduced through schedules, trajectories, or iterative optimization; however, these mechanisms are unavailable in the few-step or single-step setting, limiting the effectiveness of existing diversity-enhancing methods. A natural alternative is to perturb intermediate features, but naive feature perturbation is often ineffective, either yielding limited diversity gains or degrading generation quality. We argue that effective diversity injection in few-step models requires perturbations that respect the model's learned feature geometry. Based on this insight, we propose STRIDE, a training-free and optimization-free method that operates in a single forward pass. STRIDE injects spatially coherent (pink) noise into intermediate transformer features, projected onto the principal components of the model's own activations, ensuring that perturbations lie on the learned feature manifold. This design enables controlled variation along meaningful directions in the representation space. Extensive experiments on FLUX.1-schnell and SD3.5 Turbo across COCO, DrawBench, PartiPrompts, and GenEval show that STRIDE consistently improves diversity while maintaining strong text alignment. In particular, STRIDE reduces intra-batch similarity with minimal impact on CLIP score, and Pareto-dominates existing training-free baselines on the diversity-fidelity frontier. These results highlight that, in the absence of iterative refinement, improving diversity in few-step and one-step diffusion depends not on increasing perturbation strength, but on aligning perturbations with the model's internal representation structure.

---


### 131. [Hedwig: Dynamic Autonomy for Coding Agents Under Local Oversight](https://arxiv.org/abs/2605.11495)

**<font color=#1a73e8>作者：</font>** Tanjal Shukla, K. J. Kevin Feng, Leijie Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Despite coding agents' advances in handling increasingly complex tasks, their continued tendency to introduce unintended edits, subtle bugs, and scope drift that slip past code review means developers must still decide how much autonomy to grant them. However, existing approaches for setting an agent's level of autonomy, such as static permission settings or instruction files, cannot account for how developers' preferences for agent autonomy can shift across tasks and over time. We conducted a formative survey with 21 software engineers who use coding agents and found that they experience frustration with calibrating autonomy and have evolving preferences for level of oversight. Building on these insights, we present Hedwig, a CLI coding agent that dynamically adjusts its autonomy level based on developer-agent interactions across sessions. Rather than operating on a global, fixed autonomy configuration, Hedwig learns an evolving set of behavioral guidelines from developer decisions and feedback, reducing friction on work for which the agent has earned trust, while tightening oversight when the agent operates outside familiar territory. Hedwig demonstrates the potential of a new paradigm where agents intelligently adapt their level of autonomy based on user trust through active, longitudinal collaboration.

---


### 132. [The Evaluation Differential: When Frontier AI Models Recognise They Are Being Tested](https://arxiv.org/abs/2605.11496)

**<font color=#1a73e8>作者：</font>** Varad Vishwarupe, Nigel Shadbolt, Marina Jirotka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent published evidence from frontier laboratories shows that contemporary AI models can recognise evaluation contexts, latently represent them, and behave differently under those contexts than under deployment-continuous conditions. Anthropic's BrowseComp incident, the Natural Language Autoencoder findings on SWE-bench Verified and destructive-coding evaluations, and the OpenAI / Apollo anti-scheming work all document instances of this phenomenon. We argue that these findings create a claim-validity problem for safety conclusions drawn from frontier evaluations. We introduce the Evaluation Differential (ED), a conditional divergence in a target behavioural property between recognised-evaluation and deployment-continuous contexts, define a normalised effect-size form (nED) for cross-property comparison, and prove that marginal evaluation scores cannot identify ED. We develop a typology of safety claims (ED-stable, ED-degraded, ED-inverted, ED-undetermined) by their warrant-status under documented divergence, and specify TRACE (Test-Recognition Audit for Claim Evaluation), an audit protocol that wraps existing evaluation infrastructure and produces restricted claims rather than capability scores. We apply the framework retrospectively to three publicly documented evaluation incidents and discuss governance implications for system cards, conformity assessment, and the international network of AI safety and security institutes. TRACE does not eliminate adversarial adaptation; it disciplines the claims drawn from evaluation evidence by making explicit the conditions under which that evidence was produced.

---


### 133. [PoseBridge: Bridging the Skeletonization Gap for Zero-Shot Skeleton-Based Action Recognition](https://arxiv.org/abs/2605.11497)

**<font color=#1a73e8>作者：</font>** Sanghyeon Lee, Jinwoo Kim, Jong Taek Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Zero-shot skeleton-based action recognition (ZSSAR) is typically treated as a skeleton-text alignment problem: encode joint-coordinate sequences, align them with language, and classify unseen actions. We argue that this alignment is often too late. Skeletons are not complete action observations, but compressed outputs of human pose estimation (HPE); by the time alignment begins, human-object interactions and pose-relative visual cues may no longer be explicit. We call this upstream semantic loss. To address it, we propose PoseBridge, an HPE-aware ZSSAR framework that bridges intermediate HPE representations to skeleton-text alignment. Rather than adding an RGB action branch or object detector, PoseBridge extracts pose-anchored semantic cues from the same HPE process that produces skeletons, then transfers them through skeleton-conditioned bridging and semantic prototype adaptation. Across NTU-RGB+D 60/120, PKU-MMD, and Kinetics-200/400, PoseBridge improves ZSSAR performance under the evaluated protocols. On the Kinetics-200/400 PURLS benchmark, which contains in-the-wild videos with diverse scenes and action contexts, PoseBridge shows the clearest separation, improving the strongest compared baseline by 13.3-17.4 points across all eight splits. Our code will be publicly released.

---


### 134. [Robust Biomedical Publication Type and Study Design Classification with Knowledge-Guided Perturbations](https://arxiv.org/abs/2605.11502)

**<font color=#1a73e8>作者：</font>** Shufan Ming, Joe D. Menke, Neil R. Smalheiser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Accurately and consistently indexing biomedical literature by publication type and study design is essential for supporting evidence synthesis and knowledge discovery. Prior work on automated publication type and study design indexing has primarily focused on expanding label coverage, enriching feature representations, and improving in-domain accuracy, with evaluation typically conducted on data drawn from the same distribution as training. Although pretrained biomedical language models achieve strong performance under these settings, models optimized for in-domain accuracy may rely on superficial lexical or dataset-specific cues, resulting in reduced robustness under distributional shift. In this study, we introduce an evaluation framework based on controlled semantic perturbations to assess the robustness of a publication type classifier and investigate robustness-oriented training strategies that combine entity masking and domain-adversarial training to mitigate reliance on spurious topical correlations. Our results show that the commonly observed trade-off between robustness and in-domain accuracy can be mitigated when robustness objectives are designed to selectively suppress non-task-defining features while preserving salient methodological signals. We find that these improvements arise from two complementary mechanisms: (1) increased reliance on explicit methodological cues when such cues are present in the input, and (2) reduced reliance on spurious domain-specific topical features. These findings highlight the importance of feature-level robustness analysis for publication type and study design classification and suggest that refining masking and adversarial objectives to more selectively suppress topical information may further improve robustness. Data, code, and models are available at: this https URL

---


### 135. [Distance-Constrained Unlabeled Multi-Agent Pathfinding](https://arxiv.org/abs/2605.11503)

**<font color=#1a73e8>作者：</font>** Takahiro Suzuki, Yuma Tamura, Keisuke Okumura  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> We study a graph pathfinding problem Distance-$r$ Independent Unlabeled Multi-Agent Pathfinding, finding a set of collision-free paths between two sets where agents must stay at pairwise distance at least $r+1$ at all times. This additional constraint, generalizing collision modeling for classical MAPF, targets aspects of real-world multi-agent coordination. This additional distance constraint makes feasibility (i.e., whether a solution exists) PSPACE-complete, in contrast to standard (unlabeled) MAPF, where it can be decided in polynomial time. We address the challenge via two complementary approaches: (i) reduction-based optimal algorithms with a feasibility-preserving compression procedure, and (ii) a configuration generator-based search. Despite the hardness, empirical results show that our algorithm can handle hundreds of agents in a practical timeframe.

---


### 136. [Selective Off-Policy Reference Tuning with Plan Guidance](https://arxiv.org/abs/2605.11505)

**<font color=#1a73e8>作者：</font>** Duc Anh Le, Tien-Phat Nguyen, Thien Huu Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards helps reasoning, but GRPO-style methods stall on hard prompts where all sampled rollouts fail. SORT adds a repair update for those failures without changing rollout generation: it derives a plan from the reference solution, compares token probabilities with and without that plan, and gives higher weight to tokens that become more predictable under plan conditioning. This turns all-wrong prompts into selective, structure-aware learning signals instead of uniform imitation. Across three backbones and eight reasoning benchmarks, SORT improves over GRPO and guidance baselines, with largest gains on weaker models.

---


### 137. [Principled Design of Diffusion-based Optimizers for Inverse Problems](https://arxiv.org/abs/2605.11506)

**<font color=#1a73e8>作者：</font>** Julio Oscanoa, Irmak Sivgin, Cagan Alkan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Score-based diffusion models achieve state-of-the-art performance for inverse problems, but their practical deployment is hindered by long inference times and cumbersome hyperparameter tuning. While pretrained diffusion models can be reused across tasks without retraining, inference-time hyperparameters such as the noise schedule and posterior sampling weights typically require ad-hoc adjustment for each problem setup. We propose principled reparameterizations that induce invariances, allowing the same hyperparameters to be reused across multiple problems without re-tuning. In addition, building on the RED-diff framework, which reformulates posterior sampling as an optimization problem, we further develop the OptDiff pipeline. OptDiff provides a simplified tuning framework that facilitates the integration of convex optimization tools to accelerate inference. Experiments on image reconstruction, deblurring, and super-resolution show substantial speedups and improved image quality.

---


### 138. [LiBrA-Net: Lie-Algebraic Bilateral Affine Fields for Real-Time 4K Video Dehazing](https://arxiv.org/abs/2605.11508)

**<font color=#1a73e8>作者：</font>** Yongcong Wang, Chengchao Shen, Guangwei Gao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Currently, there is a gap in the field of ultra-high-definition (UHD) video dehazing due to the lack of a benchmark for evaluation. Furthermore, existing video dehazing methods cannot run on consumer-grade GPUs when processing continuous UHD sequences of 3--5 frames at a time. In this paper, we address both issues with a new benchmark and an efficient method. Our key observation is that atmospheric dehazing reduces to a per-pixel affine transform governed by the low-frequency depth field, which can be compactly encoded in bilateral grids whose prediction cost is decoupled from the output resolution. Building on this, we propose LiBrA-Net, which factorizes the spatiotemporal affine field into a spatial--color and a temporal bilateral sub-grid predicted at a fixed low resolution, fuses their coefficients in the $\mathfrak{gl}(3)$ Lie algebra under group-theoretic regularization, maps the result to invertible GL(3) transforms via a Cayley parameterization, and restores high-frequency detail through a lightweight input-guided branch. We further release UHV-4K, the first paired 4K video dehazing benchmark with depth, transmission, and optical-flow annotations on every frame. Across UHV-4K, REVIDE, and HazeWorld, LiBrA-Net sets a new state of the art among compared video dehazing methods while running native 4K at 25 FPS on a single GPU with only 6.12 M parameters. Code and data are available at this https URL.

---


### 139. [Controllable User Simulation](https://arxiv.org/abs/2605.11519)

**<font color=#1a73e8>作者：</font>** Guy Tennenholtz, Ofer Meshi, Amir Globerson 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Using offline datasets to evaluate conversational agents often fails to cover rare scenarios or to support testing new policies. This has motivated the use of controllable user simulators for targeted, counterfactual evaluation, typically implemented by prompting or fine-tuning large language models. In this work, we formalize controllable simulation as a causal inference problem. By bridging natural language evaluation with off-policy evaluation methodology, we show that the standard practice of training simulators via supervised fine-tuning on post-hoc trajectory labels yields a structurally biased model. Specifically, these labels are inextricably coupled to the data-generating behavior policy, injecting a look-ahead bias that breaks causal consistency. Furthermore, we prove that under policy shift this failure causes the variance of evaluation metrics to explode geometrically, a phenomenon we term controllability collapse. To restore causal consistency, we establish theoretical conditions for accurate simulation and propose practical training mitigations: a priori controls, step-wise dynamic controls, and direct policy-conditioned learning. Empirical evaluation confirms that while standard global controls distort conversational distributions and collapse behavioral diversity, our causally grounded simulators eliminate look-ahead bias, preserve natural variance, and exhibit robust zero-shot generalization to unseen agent behaviors.

---


### 140. [PointGS: Semantic-Consistent Unsupervised 3D Point Cloud Segmentation with 3D Gaussian Splatting](https://arxiv.org/abs/2605.11520)

**<font color=#1a73e8>作者：</font>** Yixiao Song, Qingyong Li, Wen Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unsupervised point cloud segmentation is critical for embodied artificial intelligence and autonomous driving, as it mitigates the prohibitive cost of dense point-level annotations required by fully supervised methods. While integrating 2D pre-trained models such as the Segment Anything Model (SAM) to supplement semantic information is a natural choice, this approach faces a fundamental mismatch between discrete 3D points and continuous 2D images. This mismatch leads to inevitable projection overlap and complex modality alignment, resulting in compromised semantic consistency across 2D-3D transfer. To address these limitations, this paper proposes PointGS, a simple yet effective pipeline for unsupervised 3D point cloud segmentation. PointGS leverages 3D Gaussian Splatting as a unified intermediate representation to bridge the discrete-continuous domain gap. Input sparse point clouds are first reconstructed into dense 3D Gaussian spaces via multi-view observations, filling spatial gaps and encoding occlusion relationships to eliminate projection-induced semantic conflation. Multi-view dense images are rendered from the Gaussian space, with 2D semantic masks extracted via SAM, and semantics are distilled to 3D Gaussian primitives through contrastive learning to ensure consistent semantic assignments across different views. The Gaussian space is aligned with the original point cloud via two-step registration, and point semantics are assigned through nearest-neighbor search on labeled Gaussians. Experiments demonstrate that PointGS outperforms state-of-the-art unsupervised methods, achieving +0.9% mIoU on ScanNet-V2 and +2.8% mIoU on S3DIS.

---


### 141. [XWOD: A Real-World Benchmark for Object Detection under Extreme Weather Conditions](https://arxiv.org/abs/2605.11521)

**<font color=#1a73e8>作者：</font>** Chih-Hsin Chen, Yu-Tung Liu, Amar Fadillah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous driving and intelligent transportation systems remain vulnerable under extreme weather. The U.S. Federal Highway Administration reports that roughly 745,000 crashes and 3,800 fatalities per year are weather-related, and recent regulatory investigations have examined failures of Level-2/3 driving systems under reduced-visibility conditions. However, datasets commonly used to evaluate weather robustness remain limited in scale, diversity, and realism. In this paper, we introduce XWOD (Extreme Weather Object Detection), a large-scale real-world traffic-object detection benchmark containing 10,010 images and 42,924 bounding boxes across seven extreme weather conditions: rain, snow, fog, haze/sand/dust, flooding, tornado, and wildfire. The dataset covers six traffic-object categories, including car, person, truck, motorcycle, bicycle, and bus. XWOD extends the weather taxonomy from one to seven conditions, and is the first to cover the emerging class of climate-amplified hazards, such as flooding, tornado, and wildfire. To evaluate the quality of our data, we train standard YOLO-family detectors on XWOD and test them zero-shot on external weather benchmarks, achieving mAP$_{50}$ scores of 63.00% on RTTS, 59.94% on DAWN, and 61.12% on WEDGE, compared with the corresponding published YOLO-based baselines of 40.37%, 32.75%, and 45.41%, respectively, representing relative improvements of 56%, 83%, and 35%. These cross-dataset results show that XWOD provides a strong source domain for learning weather-robust traffic perception. We release the dataset, splits, baseline weights, and reproducible evaluation code under a research-use license.

---


### 142. [EqOD: Symmetry-Informed Stability Selection for PDE Identification](https://arxiv.org/abs/2605.11524)

**<font color=#1a73e8>作者：</font>** Gnankan Landry Regis N'guessan, Bum Jun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data-driven identification of partial differential equations (PDEs) relies on sparse regression over a candidate library of differential operators, where larger libraries inflate false positives under observation noise and smaller libraries risk missing true terms. We introduce Equivariant Operator Discovery (EqOD), a fully automatic method combining two library reduction mechanisms. When Galilean invariance is detected from trajectory data via a weak-form structural test, EqOD uses the symmetry-reduced library, eliminating terms that our Galilean exclusion result proves to be absent from the governing equation. Otherwise, it applies randomized LASSO stability selection guided by classical false-positive bounds. A residual-based fallback prevents degradation below the full-library baseline. On 8 PDEs at 4 noise levels, EqOD attains $F_1 = 1.000 \pm 0.000$ on Heat at $20\%$ noise, where WF-LASSO obtains $0.475 \pm 0.181$, official PySINDy 2.0 obtains $0.000$, and the WSINDy reimplementation obtains $0.789$. Under the strict criterion that the mean F1 difference exceeds the larger of the two standard deviations, EqOD wins 7 of 32 cells. WF-LASSO wins none, and the remaining 25 cells are ties. Across all 32 cells, EqOD outperforms PySINDy 2.0.0 in 23 of 32 cells, and all 5 PySINDy wins occur on reaction PDEs. External validation on WeakIdent and PINN-SR datasets gives $F_1 = 1.000$ on all 5 clean benchmarks. NLS, 2D, coupled-system, and cylinder-wake extensions are reported. The Galilean library reduction is proved under explicit autonomy and library assumptions. The stability-selection step is motivated by classical false-positive bounds, while formal guarantees for correlated PDE design matrices remain open.

---


### 143. [OverNaN: NaN-Aware Oversampling for Imbalanced Learning with Meaningful Missingness](https://arxiv.org/abs/2605.11525)

**<font color=#1a73e8>作者：</font>** Amanda S Barnard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Missing values are routinely treated as defects to be eliminated through deletion or imputation prior to machine learning. In many applied domains, however, missingness itself carries information, reflecting experimental constraints, measurement choices, or systematic mechanisms tied to the data-generating process. Eliminating or masking this structure can distort class boundaries, introduce bias, and reduce generalisability; particularly in imbalanced datasets where minority classes are already under-represented. OverNaN is a lightweight, NaN-aware oversampling framework designed to address class imbalance without erasing missingness structure. It extends common synthetic oversampling methods to operate directly on incomplete feature vectors, allowing missing values to be preserved, propagated, or selectively interpolated according to explicitly defined strategies. Rather than repairing missing data, OverNaN treats missingness as part of the feature space over which synthetic samples are generated. This paper situates OverNaN within the broader landscape of imbalanced learning, missing-data handling, and NaN-tolerant algorithms. Using representative examples included with the software, we demonstrate that meaningful missingness can be retained during oversampling without introducing artificial certainty. OverNaN is intended for practitioners working with small, incomplete, and imbalanced datasets in scientific and engineering domains where missingness is unavoidable and often informative.

---


### 144. [FERMI: Exploiting Relations for Membership Inference Against Tabular Diffusion Models](https://arxiv.org/abs/2605.11527)

**<font color=#1a73e8>作者：</font>** Abtin Mahyar, Masoumeh Shafieinejad, Yuhan Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models are the leading approach for tabular data synthesis and are increasingly used to share sensitive records. Whether they actually protect privacy has become a pressing question. Membership inference attacks are the standard tool for this purpose, yet existing attacks assume a single-table setting and ignore the multi-relational structure of real sensitive data. A core challenge in assessing privacy risks from membership inference attacks in multi-table settings is how to leverage auxiliary information from relations associated with the target table, such as its parent tables. Particularly, we study a practical setting in which such auxiliary information is available only when training the attack model. At inference time, the attacker observes only the attribute values of the target record from the target table. We propose FERMI (FEature-mapping for Relational Membership Inference), which resolves this gap by enriching single-table features with relational membership signal. Across three tabular diffusion architectures and three real-world relational datasets, FERMI consistently improves attack performance over single-table baselines, with TPR@$0.1$FPR rising by up to 53% over the single-table baseline in the white-box setting and 22% in the black-box setting.

---


### 145. [Multi-Narrow Transformation as a Single-Model Ensemble: Boundary Conditions, Mechanisms, and Failure Modes](https://arxiv.org/abs/2605.11530)

**<font color=#1a73e8>作者：</font>** Tatsuhito Hasegawa, Taisei Tanaka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Single-model ensembles (SMEs) have attracted attention as a way to approximate some of the benefits of deep ensembles within a single network. However, under an approximately matched parameter budget, it remains unclear whether model capacity should be concentrated in a single wide pathway or redistributed into many narrow and independent members. We investigate this question through the Multi-Narrow (MN) transformation, which converts a baseline CNN into an SME of narrow, path-wise independent branches while approximately preserving the dominant parameter budget. We systematically compare Single-Wide and Multi-Narrow configurations across different training-data regimes, architectures, and datasets. The results show that the effectiveness of MN is strongly data-dependent: weakly partitioned or baseline-wide models are preferable in data-rich settings, whereas highly partitioned MN models consistently outperform the baseline in low-data settings. This tendency is reproduced across multiple CNN architectures and image-classification datasets, suggesting that it is not specific to a single benchmark or model family. Analysis of internal representations shows that high-MN models learn more diverse and less redundant path-wise features. In low-data regimes, this diversity is broadly utilized and improves generalization, whereas in data-rich regimes, training becomes imbalanced and prediction is dominated by a small subset of paths. These findings clarify when and why Multi-Narrow transformation is effective, and provide practical guidance for allocating model capacity between width and member multiplicity under a limited budget.

---


### 146. [Primal-Dual Policy Optimization for Linear CMDPs with Adversarial Losses](https://arxiv.org/abs/2605.11535)

**<font color=#1a73e8>作者：</font>** Kihyun Yu, Seoungbin Bae, Dabeen Lee  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing work on linear constrained Markov decision processes (CMDPs) has primarily focused on stochastic settings, where the losses and costs are either fixed or drawn from fixed distributions. However, such formulations are inherently vulnerable to adversarially changing environments. To overcome this limitation, we propose a primal-dual policy optimization algorithm for online finite-horizon {adversarial} linear CMDPs, where the losses are adversarially chosen under full-information feedback and the costs are stochastic under bandit feedback. Our algorithm is the \emph{first} to achieve sublinear regret and constraint violation bounds in this setting, both bounded by $\widetilde{\mathcal{O}}(K^{3/4})$, where $K$ denotes the number of episodes. The algorithm introduces and runs with a new class of policies, which we call weighted LogSumExp softmax policies, designed to adapt to adversarially chosen loss functions. Our main result stems from the following key contributions: (i) a new covering number argument for the weighted LogSumExp softmax policies, and (ii) two novel algorithmic components -- periodic policy mixing and a regularized dual update -- which allow us to effectively control both the covering number and the dual variable. We also report numerical results that validate our theoretical findings on the performance of the algorithm.

---


### 147. [Taming Extreme Tokens: Covariance-Aware GRPO with Gaussian-Kernel Advantage Reweighting](https://arxiv.org/abs/2605.11538)

**<font color=#1a73e8>作者：</font>** Cheng Wang, Qin Liu, Wenxuan Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Group Relative Policy Optimization (GRPO) has emerged as a promising approach for improving the reasoning capabilities of large language models. However, it struggles to effectively balance the tradeoff between exploration and exploitation during training, often resulting in suboptimal performance. Motivated by the theoretical insight that changes in entropy are governed by the covariance between token probabilities and their corresponding advantages, we propose a hyperparameter-free, covariance-weighted optimization method that dynamically down-weights extreme token-level updates via a Gaussian kernel. This approach automatically reduces the instability caused by exploration-exploitation trade-off while preserving informative learning signals. Extensive empirical evaluations show that our approach improves downstream performance across reasoning benchmarks compared with GRPO, and effectively stablizes entropy as training progresses.

---


### 148. [GeoR-Bench: Evaluating Geoscience Visual Reasoning](https://arxiv.org/abs/2605.11541)

**<font color=#1a73e8>作者：</font>** Yushuo Zheng, Zicheng Zhang, Huiyu Duan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geoscience intelligence is expected to understand, reason about, and predict earth system changes to support human decision-making in critical domains such as disaster response, climate adaptation and environmental protection. Although current research has shown promising progress on specific geoscience tasks, such as remote sensing interpretation, geographic question-answering, existing benchmarks remain largely task-specific which failing to capture the open-ended real world geoscience problems. As a result, it remains unclear how far current AI systems are from achieving genuine geoscience intelligence. To address this gap, we present \textbf{GeoR-Bench}, a \underline{Bench}mark for evaluating \underline{Geo}science visual \underline{R}easoning through reasoning informed visual editing tasks. GeoR-Bench contains 440 curated samples spanning 6 geoscience categories and 24 task types, covering earth observation imagery and structured scientific representations such as maps and diagrams. We evaluate outputs along three dimensions, including reasoning, consistency, and quality. Benchmark results of 21 closed- and open-source multimodal models reveal that geoscience reasoning remains a critical bottleneck. The highest-performing model achieves 42.7\% overall strict accuracy, while the best open-source models only get 10.3\%. Notably, the visual consistency and image quality of the outputs frequently surpass their scientific accuracy. Ultimately, these findings indicate that current models generate superficially plausible results but fail to capture underlying earth science processes.

---


### 149. [Optimal LTLf Synthesis](https://arxiv.org/abs/2605.11544)

**<font color=#1a73e8>作者：</font>** Yujian Cao, Sven Schewe, Qiyi Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Strategy synthesis typically follows an all-or-nothing paradigm, returning unrealisable whenever a specification cannot be guaranteed in an uncertain environment. In this paper, we introduce optimal LTLf synthesis, where the goal is to realise as many objectives as possible from a given specification consisting of multiple objectives, especially for the case that they are not all jointly realisable. We first consider max-guarantee synthesis, which commits to a maximal set of objectives that we can a priori guarantee to realise. We then introduce max-observation synthesis, which maximises a posteriori realised objectives that may be incomparable on different executions. Finally, we present incremental max-observation synthesis, which further improves strategies by exploiting opportunities for stronger guarantees when they arise during an execution. Experimental results show that different variations of optimal synthesis scale broadly equally well, solving a large fraction of the benchmark instances within the given timeout, demonstrating the practical feasibility of the approach.

---


### 150. [Sharpen Your Flow: Sharpness-Aware Sampling for Flow Matching](https://arxiv.org/abs/2605.11547)

**<font color=#1a73e8>作者：</font>** Aditi Gupta, Soon Hoe Lim, Annan Yu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Flow matching models generate samples by numerically integrating a learned velocity field, with each integration step requiring a neural network evaluation. Fast generation therefore requires using a small fixed evaluation budget effectively: the key question is not only how to integrate the flow, but where the sampler should spend its steps. We propose SharpEuler, a training-free sampler that profiles a pretrained model offline by estimating where the learned velocity field changes most rapidly along calibration trajectories. This finite-difference estimate defines a solver-aware sharpness profile, which is smoothed and converted by a quantile transform into a timestep grid for any desired inference budget. At test time, sampling remains ordinary Euler integration with the same number of model evaluations as a uniform schedule. We justify SharpEuler using three principles: a numerical principle identifying trajectory acceleration as the leading source of Euler discretization error, a variational principle deriving sharpness-based power-law timestep densities, and a statistical guarantee showing that the finite-sample calibrated sampler is stable at the terminal distribution level. Our experiments show that SharpEuler improves sample quality at fixed budgets, reducing inter-mode leakage and increasing mode coverage.

---


> [!TIP]
> 当前位于：**101-150**（第 3/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-396](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
