# 📦 其他研究 | 2026年06月24日

> 本类共 **219** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-219](./part-05.md)

---

### 101. [Decoherence as Defence and the Magnitude of Noise Regularisation: A Rigorous N -Qubit Theory of Stochastic Quantum Neural Networks for Adversarially Robust Network Intrusion Detection](https://arxiv.org/abs/2606.24219)

**<font color=#1a73e8>作者：</font>** Gautier-Edouard Edouard Filardo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stochastic quantum neural networks (SQNNs) encode neuronal activations as qubits, synaptic topology as entanglement, and neural noise through a Lindblad master equation. A recent conference study applied a ring-entangled SQNN to collaborative intrusion detection and reached three conclusions: ring entanglement is \emph{essential} for non-local anomaly detection; an adversarial-resilience bound holds but is \emph{conservative}; and the depolarising channel \emph{fails} to act as a dropout-style regulariser, behaving instead as output noise. It left open whether a per-gate stochastic deactivation (``true quantum dropout'') could regularise where the depolarising channel could not, and whether the loose robustness bound could be replaced by a predictive theory. This paper resolves both and extends the framework to real data and to neutral-atom hardware. We give an $N$-qubit formulation through the stochastic master equation and its vectorised Liouvillian, and prove a \emph{decoherence-contraction theorem}: a depolarising channel of strength $\gamma$ over $L$ entangling layers contracts every weight-$w$ Pauli read-out by a factor $(1-4\gamma/3)^{wL}$ (for the weight-$1$ read-out used here, $(1-4\gamma/3)^{L}$); building on the general noise-as-defence result of Du et al., we make this quantitative and operational for intrusion detection. On the real NSL-KDD dataset under white-box FGSM and PGD attacks, a depolarising SQNN trained with the channel is, over seven seeds under strong $\ell_\infty$/$\ell_2$ attacks, significantly more robust than the noiseless circuit ($\ell_\infty$ PGD-$20$, $p=0.04$, large effect) and, critically, never suffers the catastrophic robustness collapse that the noiseless model and gradient-trained classical detectors (which fall from $95\%$ to $47\%$) do, cutting robustness variance roughly twofold; we show this robustness arises from a noise-reshaped training boundary rather than from attack-time gradient contraction. For generalisation, we derive an adaptive-penalty formula showing that per-gate dropout implements a curvature-weighted $L_2$ penalty $\tfrac{p(1-p)}{2}\sum\theta^2\partial^2_\theta L$ in weight space, maximised at $p=1/2$, whereas depolarising noise implements an output-space penalty. A $30$-seed study confirms the formula's quantitative prediction: both mechanisms reduce the train-test gap by a small but statistically significant margin ($\approx\!0.01$; $p<10^{-4}$ and $p=0.004$), are statistically indistinguishable from each other, and the effect is concentrated where overfitting is largest; increasing the dropout rate past $1/2$ does not help, as the formula predicts. The single-seed dichotomy of prior work does not survive replication. We close with a neutral-atom realisation and a feasibility-by-$N$ analysis.

---


### 102. [Exploring the relationship between human-centric AI and firm idiosyncratic risks](https://arxiv.org/abs/2606.24224)

**<font color=#1a73e8>作者：</font>** Zhen-Yuan Ralph Liu, Yu-Ting Wang, Jia-Jia Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite the extensive discussions of human-centric AI (HCAI) in Industry 5.0, its effects on firms' idiosyncratic risks (IR) remains underexplored. This is an imperative issue for firms navigate financial risks during the current technological revolution, as IR reflects investor reactions to corporate heterogeneous AI strategies and implementations by isolating firm-level stock volatility from systematic factors. Integrating situated AI theory with social-technical systems theory, we conceptualise HCAI as a situated AI strategy that reduces AI-related ethical risks and fosters AI-Human synergies in firms' business operations, ultimately reducing IR by aligning with stakeholders' diverse expectations. Moreover, socio-technical factors, namely digitalisation, operational efficiency, executive shareholding, and CEOs with IT background, may moderate the HCAI-IR relationship. Using a multi-source panel dataset of Chinese listed firms from 2015 to 2023, we find that HCAI is associated with lower firm IR. Furthermore, digitalisation and executive shareholding strengthen this risk-reducing effect, whereas operational efficiency and CEOs with IT background surprisingly attenuate it. Our findings offer theoretical contributions and practical insights for both ethical AI governance and firm financial risk management in the AI era.

---


### 103. [Geometry-Instructed Video Editing](https://arxiv.org/abs/2606.24225)

**<font color=#1a73e8>作者：</font>** Chirui Chang, Xiaoyang Lyu, Yi-Hua Huang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-level geometric edits, including translating, rotating, scaling, duplicating, or removing an object, are routine operations in digital content creation (DCC) workflows, yet they remain unreliable in generative video editing. The key challenge lies in specifying the target object's 3D state change unambiguously across viewpoint and time, while consistently updating geometry-dependent secondary effects such as shadows and reflections. We introduce GIVE, a geometry-instructed video editing framework that represents edits through a unified object-state formulation. Two video-aligned geometry streams describe the target object before and after editing: a depth-box encoding coarse 3D placement and extent, and an orientation-box providing an appearance-agnostic orientation cue. Together, these streams provide a compact pre/post geometric specification for object-state transitions. To provide paired supervision for learning these edits, we build a scalable graphics-engine pipeline that executes object-level edit programs and renders controlled before/after pairs, isolating the intended geometric edit while keeping secondary effects consistent with the transformation. Experimental results demonstrate that GIVE produces faithful geometric edits with temporal coherence and consistent secondary effects across operators in a unified framework, and shows promising transfer to in-the-wild videos. Project page: this https URL

---


### 104. [FiCA: Feed-forward instant Gaussian Codec Avatars from a Single Portrait Image](https://arxiv.org/abs/2606.24232)

**<font color=#1a73e8>作者：</font>** Kim Youwang, Zhengyu Yang, Liuhao Ge 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce FiCA, a Feed-forward, instant Gaussian Codec Avatar generation pipeline that creates lifelike avatars from a single portrait image. Generating a photorealistic and drivable avatar from just a single image is significantly challenging due to the limited visual information available to accurately infer the 3D appearance and geometry of human heads. To address this, we develop a novel system that combines human-centric vision foundation models with a diffusion model. This system is designed to fully exploit partial visual observations to generate lifelike human avatars. Our proposed diffusion model learns a generative mapping from these partial observations to complete and authentic 3D mesh reconstruction. Additionally, we introduce a feed-forward mesh refinement network that enhances the fidelity and identity preservation of the generated avatars, eliminating the need for person-specific test-time optimization. By leveraging a universal prior model that decodes a generated mesh into a set of 3D Gaussians, we generate a photorealistic 3D Gaussian avatar, capable of being driven with novel expressions in real-time. Our experiments demonstrate that the avatars generated by our feed-forward approach faithfully represent diverse identities and surpass the visual quality of avatars produced by recent competing methods.

---


### 105. [From Open Waters to Enclosed Cabins: ProteusVPR for Cross-Scene Visual Place Recognition in Maritime Perception and Cabin Inspection](https://arxiv.org/abs/2606.24234)

**<font color=#1a73e8>作者：</font>** Zexi Chena, Zitai Huang, Qiwen Gu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous robotic inspection in maritime environments presents unique challenges for Visual Place Recognition (VPR) due to cross-scene perceptual shifts. Robots navigating ship-borne environments must transition between visually distinct domains: open decks with sparse textures and severe illumination changes, and enclosed cabins with repetitive structures and high visual ambiguity. Existing VPR methods, designed primarily for urban or indoor scenes, fail to generalize reliably across these starkly different scenarios. To address this, we propose ProteusVPR, a two-stage retrieval-refinement framework. The first stage employs any standard VPR model for initial image retrieval. The second stage introduces a geometric-visual estimation network that fuses the retrieved image with two temporally preceding frames, incorporating geometric descriptors, a local affine coordinate system, and camera azimuth encoding to achieve precise localization. To support this task, we introduce the XHZ dataset, an 8K-panoramic ship-borne dataset collected from an operational vessel, featuring multi-floor cabin structures, deck transition zones, and strict query-database separation for rigorous evaluation. Extensive experiments on the XHZ dataset demonstrate that ProteusVPR consistently improves the localization accuracy across multiple VPR backbones, reducing mean localization error by over 60\% on average and that ProteusVPR offers an effective and robust solution for precise visual localization in challenging, cross-scene maritime environments.

---


### 106. [SP-Mind: An Autonomous Reasoning Agent for Spatial Proteomics Analysis](https://arxiv.org/abs/2606.24235)

**<font color=#1a73e8>作者：</font>** Yucheng Yuan, Yuanfeng Ji, Zhongxiao Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spatial proteomics enables single-cell-resolution characterization of protein expression within tissue architecture, playing a critical role in understanding tumor microenvironments and guiding precision medicine. However, current analysis workflows remain fragmented, requiring expert manual orchestration of heterogeneous tools and limiting research scalability and reproducibility. We present SP-Mind, the first autonomous AI agent designed to unify the spatial proteomics analysis pipeline, from raw multiplexed tissue imaging to downstream phenotype discovery. Equipped with expert-curated biological analysis skills and specialized computational tools, SP-Mind converts natural-language queries into end-to-end analytical workflows without task-specific fine-tuning. To rigorously evaluate its capabilities, we introduce SP-Bench, a comprehensive benchmark spanning diverse tissue types, comprising 102 tasks across 18 distinct categories. Through extensive evaluation on SP-Bench and established downstream tasks, SP-Mind achieves state-of-the-art performance compared to existing open-source biomedical agent baselines.

---


### 107. [Towards Federated Long-Tailed Graph Learning: An Energy-Guided Dual Decoupling Approach](https://arxiv.org/abs/2606.24237)

**<font color=#1a73e8>作者：</font>** Lianshuai Guo, Zhongzheng Yuan, Xunkai Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Federated Graph Learning facilitates collaborative graph modeling across distributed clients while preserving data privacy. However, real-world data categories frequently exhibit long-tailed distributions. Such statistical scarcity severely degrades performance in two ways: it biases the global model toward majority classes, and it structurally isolates minority nodes by submerging them in heterophilic, head-dominated neighborhoods. While existing methods attempt topology-agnostic statistical compensations, they often fail under data scarcity. Instead of recovering tail nodes, they overfit the structural noise from adjacent dominant classes, leading to representation degradation. To address these limitations, we propose FedEPD, a framework built on a dual decoupling paradigm that separates topological purification from semantic recalibration. Specifically, FedEPD utilizes distribution-aware Dirichlet energy pruning to filter spatial heterophilic edges. It then overcomes Non-IID distribution shifts by extracting robust global prototypes from topologically central nodes, which are incorporated into local representations via a spatial low-pass prototype injection. Furthermore, a two stage alternating optimization strategy strictly protects majority decision boundaries while improving minority accuracy. Extensive experiments demonstrate that FedEPD achieves state-of-the-art performance across diverse long-tailed benchmarks, yielding absolute improvements of up to 4.97% in Accuracy and 5.48% in Macro-F1.

---


### 108. [M^2C-EvDet: Multi-Domain Multi-Order Cross-Modal Knowledge Distillation for Event-based Object Detection](https://arxiv.org/abs/2606.24248)

**<font color=#1a73e8>作者：</font>** Wei Bao, Siqi Li, Shouan Pan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Event-based object Detection (EvDet), as a biologically inspired visual perception paradigm, demonstrates superior performance in scenarios demanding high temporal resolution and a wide dynamic range. Nevertheless, the inherent sparse representations and inadequate visual semantics of event data result in a considerable performance disparity between EvDet and frame-based object detection. Previous works attempt to alleviate this cross-modal discrepancy through knowledge distillation, yet they only focus on spatial visual semantics or pair-wise relational information, thus limiting performance in more complex scenarios. To address this challenge, this paper proposes M^2C-EvDet, a Multi-domain and Multi-order Cross-modal knowledge distillation framework for EvDet. Built upon frequency learning and hypergraph computation, M^2C-EvDet integrates two specialized modules: Adaptive Frequency-Decoupled Feature Distillation (AF^2D^2) and Multi-Order Relational Distillation (MORD).

---


### 109. [TuringViT: Making SOTA Vision Transformers Accessible to All](https://arxiv.org/abs/2606.24253)

**<font color=#1a73e8>作者：</font>** Qiman Wu, Hanlin Chen, Lyujie Chen 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern VLMs and VLA systems commonly adopt off-the-shelf ViTs such as SigLIP2 as visual encoders, but diverse downstream requirements in latency, temporal modeling, and VLM integration often call for customized SOTA-level ViTs. Training such encoders remains beyond the reach of much of the community, as it requires massive image-text data, while standard softmax attention makes high-resolution or dynamic-resolution pretraining prohibitively costly and often forces low-resolution pretraining followed by post-hoc adaptation. TuringViT addresses these challenges with three key designs: Turing Linear Attention (TLA) for efficient sequence modeling, VISTA-Curation to construct supervision-rich image-video training data, and native dynamic-resolution pretraining that supports flexible inputs from the start and transfers seamlessly to downstream VLMs. As a result, TuringViT outperforms leading open-source ViT baselines with only 10% of the data, achieves stronger downstream VLM performance, and delivers substantially better latency scaling on high-resolution inputs. Our scaling-law analysis further shows that TuringViT continues to improve predictably with curated data scale, far from saturation. Its fast adaptation, hardware-friendly design, and efficient deployment have made it a unified visual foundation across XPeng's AI systems. More broadly, TuringViT provides a reproducible pipeline that dramatically lowers the cost for the community to train, customize, and deploy SOTA-level ViTs, moving toward making such Vision Transformers accessible to all.

---


### 110. [3DCarGen: Scalable 3D Car Generation via 3D-consistent Multi-view Synthesis](https://arxiv.org/abs/2606.24257)

**<font color=#1a73e8>作者：</font>** Hongli Xiao, Youjian Zhang, Yaohui Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-quality 3D vehicle assets are essential for autonomous driving simulation. Although multi-view diffusion-based paradigms enable controllable single-image reconstruction, they typically produce limited viewpoints and exhibit cross-view geometric inconsistencies, thereby reducing reconstruction fidelity in real-world scenarios. In this work, we introduce 3DCarGen, a scalable single-view 3D car generation framework designed for real-world images by synthesizing an arbitrary number of 3D-consistent multi-view images. Specifically, given a single image as input, we first synthesize a set of images from fixed viewpoints. These images are then fed into a feed-forward reconstruction model, resulting in a coarse 3D representation based on 3D Gaussian Splatting. Conditioned on this explicit 3D prior, our multi-view diffusion model generates 3D-consistent images from arbitrary camera viewpoints. We further extend a fast mesh reconstruction algorithm by incorporating color-normal joint optimization to recover detailed and coherent 3D vehicle models from the synthesized dense views. Extensive experiments on synthetic and real-world datasets demonstrate that our approach achieves robust geometric consistency and reconstruction fidelity compared to existing methods. Code and models will be released.

---


### 111. [MotifGen: Spatiotemporal interpolation of misaligned satellite images via multi-source generative modeling, in an application to tropical cyclones](https://arxiv.org/abs/2606.24263)

**<font color=#1a73e8>作者：</font>** Clément Dauvilliers, Claire Monteleoni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Microwave satellite imagery plays a crucial role in monitoring tropical cyclone precipitation and intensity worldwide, but suffers from long revisit times, potentially missing rapid storm evolution phases. While this raises the need for an interpolation method, it is made challenging by the high level of heterogeneity of microwave data coming from different instruments. In this work, we introduce the first generative model that can be applied to multiple geospatial sources that change across samples, occur at irregular time intervals, are misaligned geographically, and come from instruments with varying characteristics. We apply this model to the case of spatio-temporal interpolation of tropical cyclone microwave images from other microwave and infrared instruments. We train using a self-supervised task in which a random source is masked and reconstructed, and show that it leads to a significant decrease in Continuous Ranked Probability Score over supervised training. We show a further improvement by combining infrared and microwave data compared to microwave only. Using these improvements, the generative model produces an ensemble mean on par with that of a deterministic model, while generating a power spectrum significantly closer to that of true observations. To the best of our knowledge, this is the first generative model that interpolates microwave images of cyclones by combining multiple microwave instruments and infrared observations at irregular time intervals.

---


### 112. [Tractable Reasoning and Conjunctive Query Answering for Defeasible DL-Lite under Rational Closure](https://arxiv.org/abs/2606.24279)

**<font color=#1a73e8>作者：</font>** Giovanni Casini, Umberto Straccia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Description Logics (DLs), reasoning under Rational Closure (RC) is a well-known and widely accepted non-monotonic formalism to handle defeasible knowledge. In this paper, we study the application of RC to the core and horn variants of the DL-Lite family of lightweight description logics. We analyze both entitlement (instance checking) and Conjunctive Query (CQ) answering under RC. Our main contribution is providing a plug-in architecture that builds upon existing standard classical reasoners, establishing that reasoning and CQ answering under RC for DL-Lite can be done efficiently with minimal computational overhead.

---


### 113. [UniRED: Unified RGB-D Video Frame Interpolation with Event Guidance](https://arxiv.org/abs/2606.24282)

**<font color=#1a73e8>作者：</font>** Yinuo Zhang, Guangshun Wei, Yuanfeng Zhou 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High frame-rate RGB-D videos are crucial for a variety of downstream tasks, including motion analysis, dynamic scene understanding, and 3D reconstruction. However, due to hardware and sensing constraints, practical RGB-D cameras are typically limited to low frame rates, making it difficult to capture rapid scene dynamics. Existing video interpolation methods have achieved strong performance on RGB data, but they are not readily applicable to RGB-D scenarios, where they often yield blurry boundaries, visible artifacts, and degraded geometric consistency. Furthermore, motion estimation from only two boundary frames is inherently under-constrained in complex dynamic scenes. Event cameras, by contrast, provide asynchronous measurements with ultra-high temporal resolution, offering dense motion cues. In this paper, we propose a unified multimodal framework for RGB-D video interpolation that jointly exploits RGB appearance, depth geometry, and event-based temporal cues. Specifically, it first extracts and fuses RGB, depth and event cues, then estimates bidirectional flow with motion basis refinement for RGB and Z-axial refinement for depth, and finally synthesizes the target RGB-D frame via bidirectional warping and soft blending. In addition, we construct a new RGB-D-Event dataset to alleviate the scarcity of tri-modal training data. Extensive experiments on a public benchmark and the proposed dataset demonstrate that our method achieves superior photometric fidelity for RGB interpolation and stronger geometric accuracy for depth interpolation than existing approaches.

---


### 114. [Hierarchical Spatial and Channel Aggregation for Cross-domain Few-shot Segmentation](https://arxiv.org/abs/2606.24296)

**<font color=#1a73e8>作者：</font>** Sujun Sun, Mingwu Ren, Haofeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-domain Few-shot Segmentation (CD-FSS) aims to learn generalizable segmentation capability from abundant annotated samples in the source domain, enabling accurate segmentation of novel classes in the target domain with only a few annotated samples. Existing CD-FSS methods mainly focus on mitigating feature distribution shifts caused by style gaps while ignoring significant differences in class semantic granularity and discriminative attributes across domains, leading to two key degradations in support-query matching: semantic over-alignment and attribute over-alignment. To this end, we propose the Dual Hierarchical Aggregation Network (DHANet), which comprises three key modules. First, the Hierarchical Spatial Aggregation (HSA) module performs multi-scale region aggregation of pixel features along the spatial dimension, generating hierarchical semantic-enhanced features to alleviate semantic over-alignment. Additionally, the HCA module conducts multi-scale attribute aggregation along the channel dimension, generating hierarchical attribute-enhanced features to mitigate attribute over-alignment. Finally, we propose the Online Probabilistic Semantic Bank (OPSB), which progressively constructs and updates class probability distributions from query predictions during inference, and samples multiple pseudo-prototypes as additional support information to mitigate insufficient support. Extensive experiments on four target-domain datasets demonstrate that our method achieves state-of-the-art performance.

---


### 115. [Training-free Cross-domain Few-shot Segmentation via Robust Semantic Representation and Matching](https://arxiv.org/abs/2606.24297)

**<font color=#1a73e8>作者：</font>** Sujun Sun, Mingwu Ren, Haofeng Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cross-domain Few-shot Segmentation (CD-FSS) aims to transfer knowledge learned from source domain to distinct target domains, segmenting unseen target classes with only a few annotated samples. Although existing methods have made significant progress, they still rely on training or fine-tuning processes, which incur high computational costs and risk overfitting. We observe that when powerful and general-purpose vision foundation models are incorporated into these methods, their performance shows only marginal improvement or even degrades due to overfitting. To address this, we eliminate trainable parameters and propose a training-free framework to avoid both training overhead and overfitting. Built upon the self-supervised vision encoder DINOv3, our framework addresses cross-domain challenges through three core modules. First, the Semantic-aware Feature Re-fusion (SAFR) module identifies and re-fuses features that emphasize semantic patterns, generating representations with enhanced semantic discriminability. Additionally, the Adaptive Support Enhancement (ASE) module narrows semantic gaps between support and query through robust query information aggregation. Finally, the Hybrid Prototype Matching (HPM) module integrates matching results from diverse prototypes to adapt to varying semantic complexity across domains. Extensive experiments on four target domain datasets demonstrate that our method achieves state-of-the-art performance in CD-FSS without any training.

---


### 116. [MM-TRELLIS: Point-Cloud Guided Multi-Modal 3D Vehicle Generation in Autonomous Driving](https://arxiv.org/abs/2606.24301)

**<font color=#1a73e8>作者：</font>** Hongli Xiao, Youjian Zhang, Yucai Bai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering realistic 3D vehicle models from autonomous driving scenes is crucial for synthesizing training data and building simulation environment. However, most existing vehicle generation methods fail to fully exploit multimodal sensors i.e. multi-view images and LiDAR point clouds) and rely on neural rendering based reconstruction, leading to low-quality mesh. Recently, native 3D generative models have made significant progress, yet they are not built for arbitrary multi-view inputs and often struggle with in-the-wild driving images. In this work, we present MM-TRELLIS, a multi-modal version of TRELLIS for in-the-wild 3D vehicle generation that integrates LiDAR and image sensors from autonomous driving datasets into native 3D generative models. Specifically, multi-view images are cycled as conditioning inputs, while LiDAR point clouds provide test-time guidance to ensure geometric accuracy and cross-view consistency. During denoising, we first align the guidance point cloud with the model priors, then enforce consistency between the generated geometry and the guidance point cloud. Finally, we introduce a voxel filtering strategy based on the opacity of 3D Gaussian Splatting to suppress floaters and produce clean meshes. Comprehensive experiments on Waymo dataset demonstrate our method outperforms existing methods in high-fidelity 3D vehicle generation. Code is available at this https URL.

---


### 117. [TrOCR for Medieval HTR: A Systematic Ablation Study with Cross-Dataset Validation](https://arxiv.org/abs/2606.24302)

**<font color=#1a73e8>作者：</font>** Sachin Sharma, Michele Flammini, Federico Simonetta  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-tuning transformer-based handwritten text recognition (HTR) models on medieval manuscripts is challenging because these models are pre-trained on modern text and must adapt to a very different visual domain. This paper studies how three controllable fine-tuning choices (contrast normalization, data augmentation, and layer freezing) affect recognition accuracy when adapting TrOCR to small historical datasets. We run controlled experiments on a 13th-century Italian manuscript (I-CT 91 "Cortonese") and replicate the same experimental grid on the public READ-16 benchmark as robustness evidence. On Cortonese, our best configuration achieves 8.03% character error rate (CER). Statistical comparisons across 13 configurations show that freezing up to three encoder layers or six decoder layers does not significantly harm accuracy, while deeper freezing becomes progressively detrimental. Removing contrast normalization (CLAHE) yields 7.84% CER, comparable to a domain-specialized baseline, suggesting strong optimization can reduce reliance on image preprocessing. Cross-dataset validation on READ-16 shows that decoder freezing thresholds transfer more robustly than encoder thresholds, and combined freezing strategies require dataset-specific re-validation. Finally, we use Grad-CAM gradient attributions and decoder cross-attention maps to diagnose error patterns and failure modes revealed by the ablations. Source code is available at this https URL

---


### 118. [Prob-BBDM: a Probabilistic Brownian Bridge Diffusion Model for MRI sequence image-to-image translation](https://arxiv.org/abs/2606.24313)

**<font color=#1a73e8>作者：</font>** Martin Valls, Pascal Bourdon, Christine Fernandez-Maloigne 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI-driven image-to-image synthesis is rapidly advancing, with growing applications in medical imaging. Multi-modal image analysis plays a crucial role in optimizing examination quality, yet acquiring multiple imaging modalities in clinical settings remains resource-intensive and time-consuming, especially for 3D imaging. To address this challenge, we propose a novel image-to-image translation model based on Brownian Bridge Diffusion Models (BBDM), which synthesizes magnetic resonance imaging (MRI) sequences from 2D axial slices. Our approach integrates a variational encoder-guided diffusion mechanism, leveraging probabilistic image distributions to enhance synthesis quality. Evaluated on the BraTS 2021 dataset, our Probabilistic-BBDM (Prob-BBDM) achieves superior performance across multiple translation tasks, reaching up to 88.46% SSIM and 26.09 dB PSNR, with consistent improvements over baselines. Notably, our diffusion process requires only 4 steps, making it computationally efficient while maintaining high-quality synthesis. To further validate generalizability, we test Prob-BBDM on an external third-party dataset, demonstrating consistent performance across domains. Additionally, we assess the clinical utility of the synthesized slices by using them as input to a pre-trained segmentation model. Tumor segmentation yields a Dice score of 88.71% and an HD95 of 3.49 mm, confirming that the synthesized slices preserve critical diagnostic information. These results highlight the potential of Prob-BBDM for high-quality, efficient, and generalizable MRI synthesis, offering a promising step toward improved medical image translation.

---


### 119. [REDI-Match: Rotation-Equivariant Distillation for Efficient and Robust Dense Matching](https://arxiv.org/abs/2606.24330)

**<font color=#1a73e8>作者：</font>** Yinji Ge, Guixu Zheng, Wulong Guo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision Foundation Models (VFMs) have significantly advanced dense feature matching, yet severe in-plane rotation remains a critical challenge. Existing solutions face a fundamental dilemma: data-driven methods require inefficient parameter scaling to implicitly learn rotations, whereas strictly equivariant networks lack the semantic capacity of modern VFMs. Consequently, current frameworks typically freeze VFMs and shift the entire burden of rotation generalization to the downstream decoder. To break this architectural bottleneck, we propose REDI-Match, an efficient framework driven by a novel Rotation-Equivariant Distillation (REDI) paradigm. Instead of relying on rotation data augmentation to establish rotational correspondences, REDI distills the non-equivariant semantic representations of a VFM into a lightweight, strictly rotation-equivariant encoder, leveraging an equivariant geometric architecture to constrain robust high-dimensional semantics. To fully exploit these features, we equip the decoder with an entropy-driven spatial alignment module. By evaluating discrete rotation hypotheses, this mechanism explicitly locks onto the canonical coordinate system, eliminating global ambiguity before continuous refinement. Extensive experiments demonstrate that REDI-Match establishes a new state-of-the-art (SOTA) across multiple benchmarks. Notably, it achieves a 13.89% absolute pose accuracy improvement on the highly challenging SatAst dataset while operating 1.9x faster than the current SOTA (RoMa v2), enabling real-time inference (~41 FPS) on a single RTX 4090 GPU. Code: this https URL.

---


### 120. [UniTranslator: A Unified Multi-modal Framework for End-to-end In-Image Machine Translation](https://arxiv.org/abs/2606.24333)

**<font color=#1a73e8>作者：</font>** Jiahao Lyu, Pei Fu, Zhenhang Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In-Image Machine Translation (IIMT) aims to translate scene text in an image and render the translated text back into the original regions while preserving the overall visual appearance. Recent unified multimodal models provide a promising solution by combining visual-text understanding and image generation within a single framework. However, directly adapting such models to IIMT remains challenging. In particular, they often suffer from understanding-generation conflicts, where the translation inferred during understanding is inconsistent with the text supervision used in generation, and spatial position misalignment, where the rendered text does not accurately match the target text regions. To address these issues, we present UniTranslator, a unified multimodal framework for IIMT that tightly couples translation understanding and text editing. Specifically, we introduce an Understand-Generation Alignment Module (UGAM) to bridge the representation gap between understanding and generation, encouraging semantic consistency between translated content prediction and text rendering. We further propose a Spatial Mask Decoder (SMD) with pixel-level supervision over text regions to improve spatial grounding, geometric alignment, and layout controllability during generation. Extensive experiments on multiple benchmarks demonstrate that UniTranslator achieves state-of-the-art performance across diverse language directions and complex real-world layouts. Moreover, our results reveal a strong mutual reinforcement effect between translation understanding and image generation, highlighting the advantage of unified translation multimodal learning. Code is available at this https URL.

---


### 121. [TIGER: Taming Identity, Geometry, and Generative Priors for High-Quality Face Video Restoration](https://arxiv.org/abs/2606.24336)

**<font color=#1a73e8>作者：</font>** Yang Zhou, Wenxue Li, Peng Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Face Video Restoration (FVR) aims to recover high-fidelity facial videos from degraded input while preserving identity and semantic consistency across frames. Existing methods often struggle to simultaneously address three key challenges: identity shift, viewpoint-entangled guidance, and perceptual realism. To tackle these issues, we propose TIGER, a structured tri-prior fusion framework that Tames Identity, Geometry, and gEnerative pRiors for high-quality FVR. Specifically, an Identity Prior is first established by injecting subject-discriminative embeddings into the latent space, effectively anchoring the subject's identity against severe degradations. Then, to provide temporally consistent structural guidance for dynamic videos, TIGER constructs a Geometry Prior by lifting 2D reference cues into a disentangled 3D parameter space, creating a geometric anchor through cross-source parameter fusion. Moreover, to achieve maximum efficiency without compromising realism, we harness the video generation model's Generative Prior through a one-step rectified flow. We further design a progressive three-stage training optimization strategy that refines structural fidelity, textural reconstruction, and distribution-level realism to ensure robust optimization. We also construct a large-scale FVR dataset to facilitate robust training and standardized evaluation. Extensive experiments demonstrate that TIGER achieves state-of-the-art performance in both identity fidelity and temporal stability, delivering a high-quality, efficient and identity-consistent FVR. Project page: this https URL.

---


### 122. [Meet UD_Czech-PDTC: A Large and Genre-Rich Treebank in Universal Dependencies](https://arxiv.org/abs/2606.24337)

**<font color=#1a73e8>作者：</font>** Marie Mikulová, Barbora Štěpánková, Daniel Zeman 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Czech has been part of Universal Dependencies since its first release in 2015. It has also been one of the best represented languages, with the Prague Dependency Treebank being order of magnitude larger than most other UD treebanks. More recently, three other datasets from the Prague family were added and the annotations thoroughly revisited, forming the "Prague Dependency Treebank-Consolidated" (PDT-C). In comparison to the original PDT, PDT-C is more than twice as large, but it is also much more diverse in terms of genres and domains. In this paper, we describe the conversion of the new resource to Universal Dependencies. While the two annotation schemes are relatively similar at the first sight, there are numerous small differences in topology of the dependency structures and in granularity of the POS and relation type inventories. We demonstrate a selection of such differences on examples, discuss the diverging motivations, as well as ways to overcome the differences during conversion. We argue that while PDT is less "universal" and more tightly bound to one language, its multi-layer annotation is rich and provides all information needed for basic UD trees, and much more.

---


### 123. [Managing Task Execution for Unknown Workloads in Batteryless IoT: A Hardware-Agnostic Evaluation](https://arxiv.org/abs/2606.24340)

**<font color=#1a73e8>作者：</font>** Samer Nasser, Henrique Duarte Moura, Ritesh Kumar Singh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In recent years, the Internet of Things (IoT) paradigm has been shifting toward batteryless, energy-harvesting architectures. Sustaining reliable operation in these systems requires intelligent management of highly volatile stored energy. As edge applications grow in complexity, traditional energy-aware schedulers struggle with unpredictable workloads due to their reliance on static execution thresholds or pre-measured, hardware-specific task profiles. To overcome this, we propose two novel, hardware-agnostic dynamic scheduling strategies treating applications as a "black box," requiring no prior energy information: a model-free Reinforcement Learning (RL) agent and an on-the-fly Approximated Prediction (AP) method. We evaluate these methods against an adaptive task rate approach (AsTAR) and optimized static thresholds using a custom-built, physically accurate simulation framework driven by real-world solar data and dynamic LoRa transmission profiles. Rather than claiming universal superiority, our analysis exposes the distinct operational trade-offs of each method: the AP approach delivers lightweight, near-oracle task throughput; the RL agent provides tunable survival-execution balancing; and AsTAR excels at execution pacing across long energy gaps. Finally, we demonstrate that while these advanced strategies provide critical resilience for severely constrained systems with small capacitors, devices with larger energy buffers can efficiently rely on simpler, less computationally expensive static policies.

---


### 124. [MVG-KAN: Multi-View Geo-Wind Guided KAN for PM$_{2.5}$ Forecasting](https://arxiv.org/abs/2606.24347)

**<font color=#1a73e8>作者：</font>** Cheng Huang, Muyao Guan, Jairus Yougui Railey 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Accurate short-term PM$_{2.5}$ forecasting is important for public health protection, air-quality early warning, and urban environmental management. However, PM$_{2.5}$ variation is driven by multiple coupled factors, including stable periodic changes induced by human activities and meteorological regularity, station-specific short-term concentration evolution, and meteorology-driven pollutant dispersion among monitoring stations. Existing spatio-temporal forecasting methods may capture station relationships to some extent, but distance-only, correlation-based, or purely adaptive graphs are often insufficient to comprehensively represent these heterogeneous factors, especially wind-direction-dependent pollutant transport. To address this problem, we propose a Multi-View Geo-Wind Guided KAN model for PM$_{2.5}$ forecasting, named \textbf{MVG-KAN}, which models station-level PM$_{2.5}$ evolution from three complementary views: local periodic regularity, station-wise residual temporal dynamics, and meteorological-environment-guided spatial dispersion. Specifically, the periodic-residual forecasting backbone first separates stable daily and weekly patterns from non-periodic residual variations. A Geo-Wind Graph is constructed by combining geographic distance decay with wind-direction- and wind-speed-aware transport, providing a lightweight physically motivated directed spatial prior for residual propagation among stations. In addition, a temporal Kolmogorov-Arnold network (TKAN) residual head is then introduced to learn station-wise nonlinear autoregressive correction from de-periodized PM$_{2.5}$ residuals and historical multi-pollutant sequences, thereby enhancing the modeling of local residual inertia and pollutant co-variation.

---


### 125. [Open-Vocabulary BEV Segmentation with 3D-Aware Geometric Constraints](https://arxiv.org/abs/2606.24353)

**<font color=#1a73e8>作者：</font>** Hojun Choi, Seulbin Hwang, Dae Jung Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bird's-eye view (BEV) perception fuses multi-camera images into a unified top-down representation for autonomous driving. Despite recent progress, state-of-the-art methods remain confined to closed-set scenarios, making them vulnerable to unpredictable real-world environments. In this work, we introduce open-vocabulary BEV segmentation (OVBS), which leverages vision-language models (VLMs) to recognize categories beyond the training set while maintaining precise BEV perception and real-time efficiency. A key challenge in OVBS lies in the 3D geometric inconsistency inherent in the ill-posed lifting of 2D VLM semantics into BEV. To address this, we propose OVBEVSeg, a geometry-aware OVBS framework that enhances efficient Gaussian splatting (GS)-based unprojection by leveraging robust 3D geometric constraints across three progressive stages: (1) 2D-to-BEV pseudo-labeling via reliable 3D projection for OV generalization; (2) joint 2D-BEV per-scene optimization with BEV structural constraints for 3D geometric consistency; and (3) 3D geometric distillation for online efficiency. On the nuScenes dataset, OVBEVSeg achieves state-of-the-art performance, outperforming closed-set methods by 15.3 mIoU on unseen categories. Remarkably, even with no novel-class ground-truth labels, it remains competitive with self- and semi-supervised baselines trained with up to 40% of ground-truth annotations. Furthermore, it achieves 2.5x faster inference with only 0.22x the memory consumption of projection-based methods. Project page: this https URL.

---


### 126. [Automatic Part-of-Speech Tagging of Arabic-English Dictionary Senses through WordNet](https://arxiv.org/abs/2606.24359)

**<font color=#1a73e8>作者：</font>** Diaa M. Fayed, Aly A. Fahmy, Mohsen A. Rashwan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper proposed an algorithm for part-of-speech (POS) tagging senses of a bilingual dictionary. The algorithm is applied on the Al-Mawrid Arabic-English dictionary. The tagging task is accomplished by transferring the POS tags of the English translation equivalences (TEs) to the dictionary senses after dis-ambiguities process. The English POS tags of senses are acquired from the Princeton WordNet. POS tagging of bilingual dictionary senses is prerequisite to link a bilingual dictionary to WordNet and/or standardizing that dictionary into WordNet-LMF format where the synset (set of synonyms), not word, is the basic brick. The registered accuracy is high though the cost is little. Building NLP/HLT tools needs linguistic experts, large investments, and long time. For statistical approach, we need large annotated corpora and for rule-based approach, we need large lexicon that contains rich linguistic and world knowledge. That motivates the appearance of what are called resource-light approaches to develop natural language processing (NLP) tools for poor-resource languages.

---


### 127. [SignNet-1M: Large-Scale Multilingual Sign Language Video Dataset with Downstream Benchmarks](https://arxiv.org/abs/2606.24361)

**<font color=#1a73e8>作者：</font>** Zhewen He, Junyi Hu, Haomian Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sign language models are typically trained on datasets captured under constrained conditions, with limited viewpoint, background, and signer-identity diversity, leading to poor robustness under real-world distribution shifts. We introduce SignNet-1M, a large-scale augmented dataset spanning ASL, CSL, and German Sign Language (DGS). SignNet-1M synthesizes realistic variations along three axes: (i) novel-view rendering (rotation and zoom) via 3D Gaussian Splatting (3DGS), (ii) scene/identity editing via diffusion models for background replacement and signer substitution while preserving sign motion and linguistic content, and (iii) post-rendering augmentations that emulate capture and compression artifacts (e.g., pose/temporal perturbations and video-level corruptions) to better match in-the-wild recordings. Beyond data release, we provide a unified benchmark suite across downstream tasks (e.g., translation and recognition) and ablations that isolate each augmentation component. Experiments across backbones show that training with SignNet-1M consistently improves generalization under cross-view, cross-background, cross-identity, and post-rendering shifts, while maintaining strong in-distribution performance. The dataset, full augmentation pipeline, and benchmark are available at this https URL.

---


### 128. [MorfFlex: Handling Rich Morphology](https://arxiv.org/abs/2606.24366)

**<font color=#1a73e8>作者：</font>** Jaroslava Hlaváčová, Marie Mikulová, Barbora Štěpánková 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present MorfFlex, a morphological dictionary architecture suitable for languages with extensive regularity in both inflection and derivation. As the primary example of MorfFlex in use we introduce MorfFlex CZ, a morphological dictionary of Czech. It is distributed as a simple, unstructured list of <wordform, lemma, tag> triplets, however, its manually maintained, unpublished source files and conversion scripts encode a sophisticated system of inflectional and derivational patterns. These patterns dramatically reduce the otherwise enormous size of the dictionary, which currently contains over 100 million wordforms and more than 1 million lemmas. The MorfFlex CZ dictionary serves as an essential resource for ensuring the consistency of manual morphological annotation in the Prague Dependency Treebanks and underpins state-of-the-art automatic tools such as MorphoDiTa. In this paper, we focus on: (i) presenting an effective method for managing the rich morphological system within the dictionary, and (ii) demonstrating the utility of such a language resource for maintaining annotation consistency in corpora and supporting the development of advanced NLP applications.

---


### 129. [Structural Kolmogorov-Arnold Convolutions: Learnable Function on the Values or the Filter Shape as Parameter-Efficient Alternative to Per-Edge Convolutional KANs](https://arxiv.org/abs/2606.24371)

**<font color=#1a73e8>作者：</font>** Stefano Mereu, Oleksandr Kuznetsov, Gabriele Marchello 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional Kolmogorov--Arnold Networks (KANs) replace the fixed weights of a convolutional kernel with learnable univariate functions. The dominant formulation attaches one such function to every kernel entry and lets it act on pixel values, expressive but parameter-heavy and prone to overfitting. We argue that the learnable functions are better placed in the \emph{structure} of the convolution than on each edge, and we organise the design space along a single axis: whether the function acts on the pixel \emph{values} or on the filter \emph{shape}. We study three realisations. SV-KAN applies one shared univariate function to the values and leaves the spatial filter free and static, aa classical convolution with a single learnable shared activation. AG-KAN keeps the shared value function but supplies the spatial structure through a content-adaptive Gaussian gate. RF-KAN instead moves the learnable functions onto the filter shape, building each filter from oriented ridge profiles expanded in a localised oscillatory (Morlet) wavelet basis with content-adaptive amplitudes. Under a matched four-layer protocol with in-run references and three seeds, RF-KAN and SV-KAN reach $88.47\pm0.10\%$ and $88.20\pm0.31\%$ on CIFAR-10 and $64.40\pm0.19\%$ and $64.57\pm0.30\%$ on CIFAR-100, at about $0.4$M parameters. At this matched scale the shape model and the simplest value model meet at the top, both above a plain convolution and every per-edge KAN we tested, including the official Gram variant, at roughly a fifth of the parameters. A controlled study attributes the RF-KAN gain to an intrinsically localised oscillatory basis and to content adaptivity, and an ablation that removes the learned shape entirely, leaving only the shared value function, collapses accuracy by over forty points, identifying the learned shape as the load-bearing ingredient at this scale.

---


### 130. [MATCH: Flow Matching for Multi-View Anomaly Detection](https://arxiv.org/abs/2606.24375)

**<font color=#1a73e8>作者：</font>** Mathis Kruse, Melissa Schween, Bodo Rosenhahn  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting anomalies in industrial objects is an important topic for increasing production efficiency. More complex objects often require the analysis of several view points, which has led to the field of multi-view anomaly detection. We present MATCH, the first multi-view anomaly detection method based on Flow Matching (FM). With the ODE formulation of Flow Matching, we can estimate likelihoods and thereby derive an anomaly score to detect anomalies in multi-view image data at object, image, and pixel-level. The architectural flexibility of FM models allows us to efficiently transform features of different spatial sizes to the normal distribution. We evaluate thoroughly on the already established Real-IAD data set and are also the first to provide a comprehensive evaluation of popular anomaly detection methods for the MANTA-Tiny data set. MATCH achieves state-of-the-art performance in both anomaly detection and segmentation, all while running on consumer-level hardware. By omitting the costly divergence term needed for likelihood estimation, we ensure that MATCH is usable in real-time production scenarios. Lastly, several ablation studies are conducted to validate the methodological choices.

---


### 131. [ComputeFHE: A Privacy-Preserving General-Purpose Computation Library](https://arxiv.org/abs/2606.24379)

**<font color=#1a73e8>作者：</font>** Faris Serdar Tasel, Efe Ciftci  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully Homomorphic Encryption (FHE) enables computations to be performed directly on encrypted data while preserving data confidentiality. However, its practical applications remain limited by high computational costs and development complexity. This paper presents ComputeFHE, an open-source C++ library that facilitates the development of privacy-preserving applications based on the TFHE cryptosystem. The library provides encrypted integer and fixed-point data types together with arithmetic, logical, comparison, conditional, and oblivious array-access operations which allow developers to implement algorithms using a familiar imperative programming paradigm. ComputeFHE supports both conventional TFHE arithmetic based on standard two-input logic gates and an optimized Arithmetic Logic Unit (ALU) architecture utilizing FHE-friendly logic primitives. Experimental results demonstrate significant reductions in the number of required bootstrapping operations, achieving performance improvements of up to 3.9x for selected operations. In addition, the library includes a simulation mode that enables testing, debugging, and complexity analysis without performing actual cryptographic computations while providing circuit complexity and bootstrapping costs. Built on top of OpenFHE, ComputeFHE offers a practical and accessible framework for developing and evaluating privacy-preserving algorithms and applications.

---


### 132. [AutoSpecNER: A Fine-Grained Named Entity Recognition Dataset for Vehicle Specification Extraction](https://arxiv.org/abs/2606.24387)

**<font color=#1a73e8>作者：</font>** Jordan Lee, Filippos Ventirozos, Abdirahman Abdullahm 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Vehicle advertisements contain rich specification information, but automotive NER resources remain limited. We introduce AutoSpecNER, an expert-annotated dataset for fine-grained entity recognition in vehicle listings. The dataset includes 659 advertisements from a popular car-selling website, with over 10,000 entities annotated across 15 categories, including MODEL, ENGINE_SPEC, and BATTERY_CAPACITY. Annotation quality was validated through inter-annotator agreement, achieving an average score of 91.5%. We benchmark rule-based extraction, fine-tuned transformer encoders, and large language models. DeBERTa achieves the best performance with a 90% micro-F1 score, outperforming the rule-based baseline (43%) and the strongest large language model (77.8%).

---


### 133. [ATRIA: Adaptive Traceable ECG Reporting with Iterative Agents](https://arxiv.org/abs/2606.24392)

**<font color=#1a73e8>作者：</font>** Donggyun Hong, Kyuhwan Lee, Junmyung Kwon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing ECG report generation is tightly coupled -- interpretation and reporting fused end-to-end, so errors propagate without stage-level recourse -- while agent-based systems decouple tasks but remain single-pass, never revisiting earlier outputs. Clinical ECG reporting instead unfolds iteratively, requiring progressive context integration and bidirectional editing. We present \textsc{ATRIA}, a multi-agent ECG reporting system that mirrors the clinician's iterative workflow: it binds every report claim to its supporting evidence, flags statements unsupported by that evidence, incorporates additional context mid-session, and lets clinicians verify and revise individual findings rather than accept one opaque output. Because its agents use ECG analysis models already in clinical use, the underlying findings are clinically trustworthy; and as a cloud-based web service, \textsc{ATRIA} is ready for immediate deployment. We demonstrate \textsc{ATRIA} through four interaction cases, with a live demo and video available.

---


### 134. [Parallel Manifold Steering: Efficient Adaptation of Large Associative Memories via Residual Energy Shaping](https://arxiv.org/abs/2606.24396)

**<font color=#1a73e8>作者：</font>** Kanishk Awadhiya  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Transformer models function as Dense Associative Memories (DAMs), retrieving knowledge via high-dimensional attractor dynamics driven by the self-attention mechanism \citep{ramsauer2020hopfield, wu2024attention}. However, adapting these frozen memory systems to new tasks presents a fundamental ``Plasticity-Stability'' dilemma. Current methods either risk catastrophic interference by modifying synaptic weights directly (e.g., LoRA) \citep{hu2021lora} or degrade associative capacity by clogging the retrieval buffer with static prompt tokens (e.g., VPT) \citep{jia2022vpt}. In this work, we propose \textbf{H-Res} (Hierarchical Residual Steering), a mechanism that modulates the effective energy landscape of the Transformer without altering its global equilibrium or expanding its sequence length. By formulating adaptation as a control problem on the activation manifold \citep{chen2018neuralode}, H-Res learns a state-dependent vector field that steers token trajectories into task-specific basins of attraction. We formally prove that H-Res preserves the attention entropy of the foundation model and facilitates Neural Collapse \citep{papyan2020prevalence}. Empirically, Manifold Steering outperforms global weight modification by 26\% on associative retrieval tasks and eliminates the computational overhead of prompt-based methods, scaling effectively to structured domains \citep{zha2023vtab}.

---


### 135. [Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents](https://arxiv.org/abs/2606.24402)

**<font color=#1a73e8>作者：</font>** Juho Park, Hyunmin Choi, Kevin Nam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI security agents increasingly rely on Retrieval-Augmented Generation (RAG) to use external security knowledge for vulnerability analysis and exploit reasoning. This creates a new risk: poisoned write-ups can be operationalized into incorrect exploit behavior. Yet, prior work on RAG poisoning has mostly studied answer corruption in QA settings, much less is known about action-taking security agents. This paper aims to reveal such characteristics with crafted poisons about real-world challenges and AI agents. First, we demonstrate how a crafted single poisoned write-up injected into public-style security knowledge sources which we denote as Poisoned Playbooks, alters the behavior of RAG-based AI security agents. Across 11 CTF challenges, 3 frontier LLM families, 2 model generations, and 11 real-world CVEs, we find that poison adoption is systematic rather than random. To explain this pattern, we introduce the Verification Boundary (VB), a 3-level empirical classification based on what evidence the agent can use to refute a retrieved claim. Finally, we evaluate verification prompting and multi-source retrieval, showing that both help when stronger evidence exists, but weaken under sparse-evidence and zero-day conditions.

---


### 136. [Modality-Aware Out-of-Distribution Detection for Multi-Modal Action Recognition](https://arxiv.org/abs/2606.24404)

**<font color=#1a73e8>作者：</font>** Lars Doorenbos, Duc Manh Vu, Serdar Ozsoy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The incorporation of additional modalities into action recognition models increases their performance across a wide range of settings. However, how this additional information can contribute to making the models more robust remains underexplored, particularly for the case of multi-modal out-of-distribution (OOD) detection. While methods exist that regularize the multi-modal training process with OOD detection in mind, they still apply off-the-shelf OOD detectors designed for the uni-modal case during inference, discarding important information. Based on an interesting relationship we find between the multi-modal and uni-modal predictions, we propose to use this signal to build a post-hoc detector explicitly designed for the multi-modal scenario. We combine this new source of information with a feature-space score, which detects off-manifold samples in the multi-modal space, and normalize them by the multi-modal logits. In doing so, the proposed hybrid detector is compatible with existing training-time approaches and consistently improves performance. Experiments on a wide range of established datasets from the MultiOOD benchmark show that, on average, our approach outperforms the state of the art. Our results show the importance of explicitly considering the different modalities at inference time for multi-modal OOD detection.

---


### 137. [Cycle-Consistent Neural Explanation of Formal Verification Certificates](https://arxiv.org/abs/2606.24414)

**<font color=#1a73e8>作者：</font>** Andoni Rodriguez, Alberto Pozanco, Daniel Borrajo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Formal verification produces machine-checkable certificates that attest to the satisfaction or violation of temporal properties, yet these certificates remain opaque to non-specialist stakeholders. We propose a cycle-consistent neural architecture that generates faithful natural language explanations of verification certificates. A forward network NN1 maps certificates to explanations, and an inverse network NN2 reconstructs certificates from explanations; a symbolic verifier closes the loop, providing a differentiable faithfulness proxy. A pointer-generator mechanism ensures lexical grounding by copying state names directly from the certificate. We evaluate on 420 test certificates spanning six verification methods (bounded proof, k-induction, inductive invariant, lasso, reachability, witness pair) in both YES and NO verdict variants, drawn from a financial compliance domain with 207 named states. Our trained architecture, combined with a hybrid inference-time routing strategy, achieves 90.0% cycle-verified soundness, surpassing a multi- LLM few-shot baseline (76.1% for the best of 16 LLM combinations across four frontier models) by 13.9 percentage points. The neural model wins on 10 of 12 verdict/kind categories, with three categories reaching 100% soundness. The architecture offers 860x faster inference (185 ms vs. 160 s per certificate for the full multi-LLM baseline), offline operation, deterministic outputs, and zero per-inference cost. These results demonstrate that trained specialization outperforms general-purpose LLM prompting for structured certificate explanation, while eliminating the deployment constraints of cloud-based inference.

---


### 138. [Data Augmentation: A Fourier Analysis Perspective](https://arxiv.org/abs/2606.24418)

**<font color=#1a73e8>作者：</font>** Behrooz Tahmasebi, Melanie Weber, Stefanie Jegelka  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data augmentation is a simple and model-agnostic approach for exploiting known invariances in learning problems. Given a group acting on the input space, one augments the training set with transformed copies of each sample. Because it exploits symmetries without modifying the underlying learning algorithm, data augmentation can be applied broadly across learning methods. However, this universality comes at a computational cost: when the group is large, full group-sized augmentation quickly becomes computationally infeasible. This raises a fundamental question: Can partial data augmentation achieve the same statistical benefits as full augmentation in terms of generalization and sample complexity? We develop a general framework for investigating this question using Fourier analysis and the representation theory of finite groups. We show that, for a broad class of classical learning problems, partial data augmentation based on a randomly sampled subset of group elements achieves the same minimax rates as full augmentation, up to an approximation error that vanishes as the subset size increases. Our results provide a theoretical explanation for why partial augmentation can retain the statistical benefits of full augmentation despite enforcing symmetry only approximately, and shed light on a recently raised question in learning with symmetries: whether statistically optimal learning under general group invariances can be achieved using computationally scalable methods. Moreover, we prove a complementary impossibility result: enforcing exact invariance via data augmentation requires averaging over the entire group, and cannot be achieved by any strict subset when the hypothesis space is sufficiently expressive. Together, these results provide a unified perspective on full and partial data augmentation, as well as exact and approximate symmetry enforcement.

---


### 139. [Can Aggregate Invariants Accelerate Continuous Subgraph Matching? Limits, Laws, and a Dynamic Spectral Index](https://arxiv.org/abs/2606.24421)

**<font color=#1a73e8>作者：</font>** Minghao Chen, Jiale Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spectral filtering recently delivered substantial pruning for \emph{static} subgraph matching: Laplacian interlacing rejects candidates whose neighborhoods cannot host the query. We study whether such aggregate structural tests can accelerate \emph{continuous} subgraph matching (CSM) over dynamic graphs, and answer in three parts. First, lazily maintained spectral bounds are infeasible exactly where spectral pruning has value: we characterize the tightest safe rule over a formalized perturbation relaxation and show that even it loses essentially all pruning power within four touching updates. Second, exact maintenance is affordable when selective: pruning utility and recomputation cost are anti-correlated across vertices -- hubs provably never prune -- so recomputing small-neighborhood spectra on touch sustains exact local spectra at microseconds per update, complete by construction. Third, integrated into a decoupled CSM benchmark against an identical-minus-spectra control, the tests remove up to $51\%$ of candidates or safely skip up to $47\%$ of update enumerations, yet enumeration intermediates remain unchanged -- beyond the gates' skipped first-level bindings, typically zero -- across two engines, four real graphs, two stream types, and $77$ solved queries; a constructed radius-stratified workload confirms the instrument detects the exception when one exists ($-99.9\%$ intermediates, $748\times$ faster). Aggregate tests accelerate what scales with candidate sets -- construction, list scans -- never adjacency-guided exploration. We distill an intermediate-invariance methodology for evaluating CSM filters and release a reusable dynamic local-spectra index.

---


### 140. [EgoSAT: A Comprehensive Benchmark of Egocentric Streaming Interaction Understanding](https://arxiv.org/abs/2606.24422)

**<font color=#1a73e8>作者：</font>** Yijia Lei, Jinzhao Li, Yichi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce EgoSAT, the first comprehensive benchmark for egocentric video reasoning in streaming settings, designed to evaluate the capabilities of modern vision-language models (VLMs). The benchmark targets streaming interaction understanding, where video frames arrive sequentially and models must continuously interpret evolving visual context. EgoSAT unifies several previously distinct tasks within a single streaming framework. In this formulation, queries about completed events correspond to retrospective reasoning, queries about ongoing activities require online understanding, and queries about future actions involve prospective anticipation. This unified setting requires models to reason about the past, present, and future while operating under the constraint that only previously observed frames are available. EgoSAT contains 1,997 unique videos spanning 165 hours of egocentric footage and around 4,800 high-quality question-answer pairs, carefully designed to probe reasoning across varying temporal contexts. Using this benchmark, we evaluate a diverse set of both open-weight and closed-weight VLMs, providing a systematic assessment of their ability for streaming interaction understanding. By distinguishing answerability and conducting diagnostics on confidence of models, we find existing models not only struggle with prospective and retrospective modeling, but also exhibit severe mis-calibration: confidence often fails to track inherent answerability, leading to dangerous "confidently wrong" behaviors. Project page: this https URL

---


### 141. [Transformation Behavior of Images in Latent Space](https://arxiv.org/abs/2606.24430)

**<font color=#1a73e8>作者：</font>** Christian Zöllner, Mozzam Motiwala, Aysel Ahadova 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training of neural networks for histopathology classification tasks typically relies on data encoding into latent space, which reduces complexity and improves performance. There are several encoder networks available, either pretrained on general image datasets such as ImageNET, or specifically on histopathological images. Training of encoder networks should be adapted to downstream tasks, allowing encoding of biologic/diagnostic content while rendering networks invariant to label-irrelevant transformations.
This paper investigates the effect of classical image transformation on the latent space, using networks provided by Lunit Inc. and Bioptimus, both focusing on pathological images, and by Meta Research Team. We assess variance of embeddings resulting from standard data transformations by comparing original and transformed image embeddings and by contrasting them with random, unrelated embeddings, using image tiles from hematoxylin/eosin-stained sections available in a colorectal tissue dataset and the publicly accessible TCGA dataset.
Our findings show that embeddings of original and transformed images are closer to each other than to random embeddings, indicating robustness to transformations. However, they are not fully invariant, revealing that the encoder networks do not completely neutralize transformation effects in latent space, explaining why transformation-mediated augmentation of datasets can improve performance. Significant differences were observed between general and histopathology-specific encoder networks.

---


### 142. [MedPCFM: Improving Medical Point Cloud Completion by Integrating Point Transformers and Flow Matching](https://arxiv.org/abs/2606.24433)

**<font color=#1a73e8>作者：</font>** Kamil Kwarciak, Marek Wodzinski  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical point cloud completion is important for anatomical reconstruction and downstream clinical workflows, yet generative modeling in this setting remains insufficiently studied. We investigate completion through continuous-time generative modeling and introduce PCFM, a PTv3-backed flow matching approach for medical point cloud completion. We evaluate on SkullFix and SkullBreak, and additionally on the more recent Mandibular Defect dataset. We build strong baselines by adapting PTv3 to a deterministic encoder-decoder completion model and by instantiating diffusion completion (PCDiff) with both PVCNN and PTv3 denoisers. PCFM with PTv3 is competitive with the deterministic PTv3 baseline and achieves state-of-the-art generative performance across datasets, while requiring substantially fewer sampling steps than diffusion. At the best operating points, PTv3 also yields clear throughput gains, providing up to a 7$\times$ speed-up for PCFM compared to a PVCNN backbone. Finally, we study empirical scaling trends by varying model size and point cardinality, showing consistent gains with higher point resolution and informative trade-offs across model scales.

---


### 143. [ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling](https://arxiv.org/abs/2606.24437)

**<font color=#1a73e8>作者：</font>** Heng Ping, Arijit Bhattacharjee, Peiyu Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Agents (MoA) architectures improve inference-time scaling by organizing multiple LLM agents into layered reasoning pipelines. However, existing MoA variants fail to sustain gains as depth increases, exhibiting degradation, early plateauing, or saturation. We propose ReM-MoA, a memory-augmented MoA framework that sustains scaling through two mechanisms: (1) a Ranked Reasoning Memory that persistently stores and ranks reasoning traces from all layers using a comparative Reviewer Agent, and (2) a Curated Diversified Memory Routing scheme that exposes different agents to distinct combinations of successful and failed traces, preserving exploration diversity while propagating high-quality reasoning. We further introduce an optional multi-domain Reviewer distillation pipeline that improves ranking quality through frontier-model supervision. Across five reasoning benchmarks spanning math, formal logic, code, knowledge, and commonsense, ReM-MoA consistently outperforms prior MoA variants across both depth and width scaling, and its advantage widens with depth, establishing structured cross-layer reasoning memory as a key missing mechanism for scalable multi-agent inference.

---


### 144. [A Comparison of Kubernetes Compliance Standards and Configuration Scanners](https://arxiv.org/abs/2606.24438)

**<font color=#1a73e8>作者：</font>** Michael Krieger, Markus Gierlinger, Farooq Shaikh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Kubernetes has become the industry standard for orchestrating containers in microservice-based software architectures. While several hardening guidelines and scanning tools for securing Kubernetes clusters and deployments have emerged in recent years, their differing guidance and outputs often lead to inconsistent configuration and prioritization decisions. This work presents a systematic comparison of eight commonly used Kubernetes hardening guidelines. Through this comparison and the inclusion of best practices, we established a benchmark of 79 Kubernetes configuration recommendations and conducted the a structured empirical evaluation of ten popular static configuration scanning tools and their scoring outputs. Our findings reveal substantial disparities in the coverage of configuration issues across hardening guidelines and scanners, as well as inconsistencies in how configuration issues are scored and ranked by different scanners. These results highlight the need for more standardized, transparent, and consistent approaches to risk and severity assessment of Kubernetes configuration issues.

---


### 145. [S1-Omni-Image: A Unified Model for Scientific Image Understanding, Generation, and Editing](https://arxiv.org/abs/2606.24441)

**<font color=#1a73e8>作者：</font>** Qingxiao Li, Zikai Wang, Qingli Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present S1-Omni-Image, an open-weight unified multimodal model for scientific image understanding, generation, and editing. Unlike general-purpose image generation models, scientific image tasks require not only high-fidelity synthesis, but also robust understanding of scientific semantics, structural relations, domain knowledge, and task intent. To this end, S1-Omni-Image builds on the scientific multimodal reasoning backbone S1-VL-32B and couples its understanding capability with an image generation module under a unified think-before-generate paradigm. Given a user instruction, the model first produces a task-oriented reasoning trace, a textual answer, and a task special token; their hidden states are then injected into the generation module to condition image generation or editing. S1-Omni-Image supports scientific image understanding, generation, and editing in a unified framework. For generation, it focuses on scientific illustrations and text rendering, including logical diagrams, relational comparisons, data charts, and realistic scientific visualizations. For editing, it casts segmentation and other domain-specific vision tasks as native image editing problems, enabling multi-turn illustration editing, medical and geographic image segmentation, medical image translation, and scientific image super-resolution. We construct SciGenEdit, a 314K-sample training dataset, and release the model weights, inference code, and SciGenEdit-10K. Experiments show that S1-Omni-Image substantially improves scientific image generation and editing while preserving the scientific image understanding capability inherited from S1-VL-32B. It outperforms open-source models on GenExam and TechImage-Bench, achieves state-of-the-art results on four editing benchmarks including MSD, cigRockSEM, SynthRAD2025, and IXI, and maintains stable performance on scientific image understanding evaluations.

---


### 146. [P-MTP: Efficient Document Parsing via Multi-Token Prediction with Progressive Depth Scaling](https://arxiv.org/abs/2606.24447)

**<font color=#1a73e8>作者：</font>** Le Xiang, Chenxi Zhai, Shu Wei 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) have revolutionized document parsing by enabling end-to-end mapping from images to structured text, imposing a significant latency bottleneck, particularly for token-dense documents. While Multi-Token Prediction (MTP) has emerged as a promising approach for accelerating inference, its potential is constrained by optimization instability when scaling to deeper look-ahead depth. In this paper, we propose \textbf{P-MTP}, a framework that leverages \textbf{Progressive Multi-Token Prediction} with a lightweight MTP module to scale the look-ahead depth for high-throughput document parsing. Specifically, we introduce Progressive Curriculum Loss that adaptively re-weights different look-ahead depths using cumulative path reliability and retrospective target consistency. By effectively suppressing gradient noise in long-range predictions, P-MTP, facilitates an automated easy-to-hard optimization transition, enabling the model to master increasingly distant look-ahead depths. Furthermore, we propose Confidence-Gated Dynamic Drafting to maximize the effective look-ahead depth and acceptance rate by adaptively calibrating speculative length during inference, thereby minimizing computational waste and further pushing the boundaries of inference speedup. Experimental results across multiple benchmarks and architectures demonstrate that P-MTP, achieves up to a $5\times$ speedup with negligible loss in accuracy, providing the first successful validation of extensive look-ahead MTP in the document parsing domain.

---


### 147. [SENTRY: SAM2-Enhanced Neighbor-Aware and Temporally Reasoned Memory for Visual Tracking](https://arxiv.org/abs/2606.24449)

**<font color=#1a73e8>作者：</font>** Mohamad Alansari, Yonathan Michael, Hasan AlMarzouqi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We revisit the memory update mechanism in SAM2-based visual object tracking and identify confidence-only mask selection as the dominant cause of drift under occlusion, rapid motion, and distractors. We introduce SENTRY, a training-free, plug-and-play, refine-before-write module that validates each memory update for short-horizon temporal consistency before committing it. SENTRY aggregates diverse segmentation hypotheses per frame, backtracks them into short tracklets, and uses neighbor-aware cycle-consistent matching against recent trajectories to favor temporally and geometrically consistent masks. It leaves the base architecture untouched, replacing confidence-driven writes with consistency-validated ones. For fair evaluation, we re-evaluate major open-source SAM2-based trackers across all available scales and datasets, filling gaps in prior reports. Integrated into five strong baselines, SENTRY delivers consistent gains across nine benchmarks, achieving new zero-shot SOTA on LaSOT, LaSOT_ext, GOT-10k, VOT20, VOT22, and DiDi. Despite these checks, the SAM2-L version runs at 32.8 FPS on an A100, and across compatible hosts adds only about 0.4--0.6 GB VRAM. Our results provide the first unified all-scale evaluation of SAM2-based trackers and show that enforcing temporal validity at write time stabilizes memory-augmented tracking without retraining.

---


### 148. [Bayesian control for coding agents](https://arxiv.org/abs/2606.24453)

**<font color=#1a73e8>作者：</font>** Theodore Papamarkou, Vladislav Smirnov, Viktor Mazanov 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern coding agents pair LLM generators with various tools, including cheap diagnostics and expensive verifiers. The tool-use decisions are typically governed by orchestrators that often use fixed rules and ignore uncertainty. We formulate orchestration as cost-sensitive sequential hypothesis testing: a Bayesian controller maintains a belief over candidate correctness and dynamically decides whether to gather more evidence, refine the candidate, verify it, or stop. Across six generators and nine coding benchmarks, Bayesian control proves to be most valuable when verification is costly and critics are informative but imperfect. Beyond control, the belief state yields an interpretable correctness score that outperforms token-probability and raw tool-success baselines for uncertainty quantification.

---


### 149. [Optimizing Visual Analytics Workflows: From Theory to Practice](https://arxiv.org/abs/2606.24454)

**<font color=#1a73e8>作者：</font>** Philip Beaucamp, Alfie Abdul-Rahman, Rita Borgo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The principle of visual analytics (VA) is to provide integrated workflows where human-centric processes (e.g., visualization and interaction) and machine-centric processes (e.g., statistics and algorithms) complement each other. To implement this principle in practice, it is necessary to reason about the trade-offs among different processes and make optimal use of them in a workflow. Building on an existing ontology of the methodology for analyzing such trade-offs information-theoretically and for optimizing VA workflows systematically, we investigate ways to transform this methodology from theory to practice. In particular, we adopted the action research method. Through case studies in different application domains, VA researchers with different background knowledge and experiences offered their answers to several hypotheses about using the methodology in practice and proposed ways forward. In this paper, we present our collective analysis, the strengths and feasibility of this theory-based methodology, as well as the obstacles to its broad deployment in practice. To address these challenges, we outline a roadmap to remove such obstacles.

---


### 150. [Lite Any Stereo V2: Faster and Stronger Efficient Zero-Shot Stereo Matching](https://arxiv.org/abs/2606.24457)

**<font color=#1a73e8>作者：</font>** Junpeng Jing, Ronglai Zuo, Zhelun Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in stereo matching have achieved remarkable accuracy, but often rely on large models, heavy computation, or additional foundation-model priors, making them difficult to deploy on resource-constrained platforms. In contrast, efficient stereo models offer faster inference but are commonly considered less capable of strong zero-shot generalization. In this paper, we challenge this assumption by introducing Lite Any Stereo V2 (LAS2), an ultra-fast model series designed for efficient zero-shot stereo matching. LAS2 is developed from both architecture and training perspectives. Architecturally, we revisit efficient stereo design under practical deployment settings and propose a 2D-only cost aggregation framework, optimized for real inference latency rather than theoretical MACs alone. For training, we develop a three-stage strategy that combines synthetic supervision, self-distillation, and real-world knowledge distillation. To improve the reliability of real-world pseudo supervision, we further introduce pseudo-label filtering and an error-clamping operation, enabling smoother synthetic-to-real transfer. We instantiate LAS2 as a family of models, including feed-forward variants for different efficiency budgets and an iterative variant for higher accuracy. Extensive experiments show that LAS2 achieves state-of-the-art accuracy among efficient stereo methods while maintaining significantly lower latency. Specifically, LAS2-H achieves stronger overall zero-shot performance than the iterative method Fast-FoundationStereo, with 1.8x and 2.7x faster inference on H200 and Orin, respectively. The project page, demos, and code are available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-219](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
