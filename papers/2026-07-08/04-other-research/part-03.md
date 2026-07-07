# 📦 其他研究 | 2026年07月08日

> 本类共 **571** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

---

### 101. [MambaLIE: Scene Light Intensity-Boosted Low-Light Image Enhancement with State Space Model](https://arxiv.org/abs/2607.03013)

**<font color=#1a73e8>作者：</font>** Wanshu Fan, Xiangyu Li, Cong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images captured by consumer electronic devices, such as mobile phones and digital cameras, often suffer from low-light degradation due to sensor limitations and imaging pipelines, which degrades visual quality and affects downstream vision tasks.
Existing methods based on Convolutional Neural Networks (CNNs) and Transformers have dominated current low-light image enhancement (LIE) due to their excellent ability to model hierarchical features.
However, CNNs operate in local receptive fields that cannot model long-range dependencies, while Transformers overcome this problem but incur substantial computational costs.
To address these challenges, we propose MambaLIE, a Scene Light Intensity-Boosted Low-Light Image Enhancement method based on a State Space Model (SSM).
We first introduce scene light intensity to improve the structural distribution of illumination, which is then gated with the low-light input to guide enhancement.
To better model the illumination while maintaining computational efficiency, we propose the Locally Enhanced State Space Model (LESSM) for efficient light enhancement.
Our LESSM contains two branches: an SSM branch and a Local Enhanced branch, where the former is used to model the long-range dependencies with linear time complexity, while the latter is used to enhance local feature representations.
Extensive experiments demonstrate that MambaLIE outperforms state-of-the-art CNN-based and Transformer-based LIE methods on four widely used synthetic benchmarks and five publicly available real-world benchmarks in terms of accuracy, speed, and model size, making it suitable for practical deployment on resource-constrained devices.

---


### 102. [Beyond Forecasting: The Belief-to-Trade Layer in Prediction-Market Agents](https://arxiv.org/abs/2607.03015)

**<font color=#1a73e8>作者：</font>** Yishu Wang, Yuxuan Wang, Jiaqi Deng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Forecasting future events has attracted growing attention as a testbed for general-purpose AI. A natural way to ground this evaluation is let the models trade in the prediction markets. Trading, however, requires more than forecasting. Moreover, recent benchmarks report a substantial gap between calibrated probability scores and the trading results. We propose Raven-Agent, to the best of our knowledge, the first autonomous trading agent for prediction markets. On a controlled replay over an archived decision set, our architecture achieves the only positive return and the only positive risk-adjusted return among all tested policies. We have released our code in this https URL .

---


### 103. [$C^3$ASD: Multi-Level Consistency-Driven Representation Learning](https://arxiv.org/abs/2607.03018)

**<font color=#1a73e8>作者：</font>** Jin Hong, Jisoo Park, Junseok Kwon  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Active Speaker Detection determines whether a visible person in a video is speaking at each moment. While recent audio-visual fusion methods perform well on clean data, they degrade under real-world corruptions such as background noise, occlusion, or simultaneous modality degradation. We attribute this limitation to the absence of explicit consistency constraints that promote robust, semantically aligned representations across modalities. Without such guidance, models tend to learn fragile modality-specific shortcuts that fail under corrupted conditions. We propose $C^3$ASD, a multi-level consistency-driven framework with three complementary constraints: embedding-level inter-modality consistency aligns audio-visual representations during speech; sequence-level intra-modality consistency separates speaking and non-speaking clusters via track-aware contrastive learning; and prediction-level consistency stabilizes fusion through knowledge distillation. Extensive experiments demonstrate significant improvements under diverse audio, visual and joint corruptions, while maintaining competitive performance on clean data.

---


### 104. [A Comparative Study of Static, Scrollytelling, and Chatbot Visualization Onboarding Techniques for UX Designers](https://arxiv.org/abs/2607.03023)

**<font color=#1a73e8>作者：</font>** Ester Chen, Aboli Shete, Aditya Anavekar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> User experience (UX) designers face barriers when creating data visualizations due to limited domain expertise in visualization or unfamiliarity with specialized tools. This highlights a clear need for effective methods to build visualization literacy. To address this, we evaluated three visualization onboarding techniques -- static, scrollytelling, and chatbot -- in an experimental study with 25 UX designers and students. We measured visualization comprehension and guideline adherence during a visualization creation task, followed by surveys and interviews to capture preferences and experiences. Compared to static onboarding, the pooled interactive condition (scrollytelling or chatbot) was associated with significantly higher guideline-adherence scores during visualization creation; both interactive techniques also received higher engagement ratings. Instruction clarity ratings were significantly higher when the two interactive conditions were pooled. Comprehension did not differ significantly across conditions. While participants generally preferred the interactive techniques, no significant differences emerged between scrollytelling and chatbot in performance or onboarding experience ratings. Drawing on the findings, we discuss three design dimensions of visualization onboarding (narrative structure, visual content layout, and navigational flexibility), their design implications, and potential opportunities for future research in this field.

---


### 105. [OmniDS: Dual-Stream Context Fusion for Omnidirectional Depth from Fisheye Cameras](https://arxiv.org/abs/2607.03038)

**<font color=#1a73e8>作者：</font>** Chaesong Park, Jihyeon Hwang, Muyeol Sung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Omnidirectional depth estimation from multi-fisheye camera rigs is complicated by visibility conflicts: wide baselines cause different cameras to observe different portions, or even different faces, of the same object, so aggregating their features into a unified equirectangular (ERP) representation under fixed projection produces ambiguous matching evidence near occlusion boundaries and thin structures. Although existing methods mitigate this by down-weighting unreliable views, they do not resolve the underlying discrepancy because context formation and cross-view fusion remain tied to rigid fisheye-to-ERP sampling. We present OmniDS, an iterative depth refinement framework that replaces rigid aggregation by combining dynamic context fusion with consensus-aware multi-view similarity. A dual-stream encoder pairs a lightweight CNN for geometric detail with a frozen DINOv3 for semantic priors; their features are reprojected into ERP space at each refinement step via learned view weighting and deformable cross-attention with geometric distortion bias. In parallel, a multi-view consensus volume captures global cross-camera agreement through group-wise correlation and feature variance, regularized by a 3D U-Net. For efficient deployment, we distill the dual-stream representation into a single MobileNet-based encoder. OmniDS achieves state-of-the-art performance on the OmniThings, OmniHouse, and Sunny benchmarks while maintaining competitive inference speed. Project page and codes are available at this https URL.

---


### 106. [Out-of-distribution Neural Inference in Dynamical Ising Models](https://arxiv.org/abs/2607.03039)

**<font color=#1a73e8>作者：</font>** Yuan-Bin Zhu, Shuang Qiao, Shi-Ju Ran  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural networks are increasingly used to infer hidden physical structure from dynamical observations, yet it remains unclear whether their out-of-distribution performance reflects transferable physical rule learning. We address this question in a controlled inverse problem: reconstructing interaction graphs of a kinetic Ising model from Glauber magnetization trajectories. Across convolutional, graph, Transformer, and hybrid architectures, we find that data-driven training produces distinct and reproducible statistical strategies under topology and temperature shifts. Edge-population diagnostics reveal that Transformer-based models tend to preserve the link density of the training ensemble, whereas convolutional models can collapse toward sparse- or no-link predictions that appear out-of-distribution stable by exploiting the majority no-link class. Thus, high in-distribution accuracy and apparent out-of-distribution robustness do not necessarily imply a learned dynamics-to-structure rule. Instead, neural reconstruction can be governed by architecture-dependent statistical priors. Our results identify a concrete failure mode of standard data-driven learning in physical inverse problems and motivate rule-guided principles for machine-learning-assisted scientific discovery.

---


### 107. [Natural Language Camera Movement Understanding](https://arxiv.org/abs/2607.03043)

**<font color=#1a73e8>作者：</font>** Yuwen Tan, Joey Huang, Jin Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding camera movement in natural language is critical for training and evaluating video generation models, among other applications. However, we demonstrate that existing vision-language models (VLMs) fail this task in surprising ways, frequently confusing translation with rotation, left with right, and object movement with camera movement. To address these limitations, we establish natural language camera movement understanding as a standalone research task. We introduce a two-level cinematographic taxonomy and an extensive, atomic benchmark featuring both real and synthetic videos. Furthermore, we curate a large-scale, multi-source training set enhanced by targeted camera movement augmentation. Our fine-tuned VLM-8B outperforms Gemini 3.1 Pro by 10% and 11% on our benchmark's real and synthetic videos, respectively. Despite these gains, a significant gap remains relative to human performance, underscoring the need to promote and facilitate future research on natural language camera movement understanding.

---


### 108. [CURE: Controllable Unified Image Restoration for Complex Degradations](https://arxiv.org/abs/2607.03044)

**<font color=#1a73e8>作者：</font>** Boseong Kim, Donghyeon Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The presence of composite degradations poses a significant challenge, since the underlying corruption factors exhibit complex and interdependent interactions. Even when the degradation types are known, accurately restoring the image remains difficult due to the intertwined nature of their effects and the need for selective control during the recovery process. To address this, we introduce CURE, a unified framework that enables controllable restoration in complex degradation settings by learning disentangled and adjustable representations. CURE is driven by four complementary objectives. First, an identity embedding is incorporated, along with a reconstruction constraint, to ensure that the model can reproduce the input image when restoration is unnecessary. Second, the ratio control mechanism blends the identity embedding with degradation-specific embeddings using user-regulated mixing ratios, allowing continuous control over restoration intensity. Third, an intermediate loss is applied to supervise stepwise outputs, each encouraged to tackle the removal of only a single degradation factor within a composite mixture. Finally, a permutation-invariant loss ensures that the model achieves consistent restoration quality regardless of the order in which multiple degradations are addressed. Since CURE modifies only the training strategy and not the underlying network architecture, it can be seamlessly integrated into existing controllable restoration models. Experiments demonstrate that CURE delivers state-of-the-art performance on composite degradation benchmarks, while enabling both selective and jointly fused restoration through flexible modulation of embedding ratios. The code and dataset are available at this https URL.

---


### 109. [Text-to-Image Generation for Projector-Camera System Registration](https://arxiv.org/abs/2607.03046)

**<font color=#1a73e8>作者：</font>** Xinyu Chen, Yuqi Li, Jiabao Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Establishing correspondence between projector and camera images in a procam (projector + camera) system is essential for achieving high-resolution pixel matching, referred to as procam registration. The highest accuracy is typically obtained using structured light patterns (e.g., stripes or blobs). However, these methods are often inefficient and lack meaningful information for human viewers. Although some have explored the use of natural images, these often fail to provide a sufficient distribution of features to achieve comparable accuracy. Additionally, existing methods struggle to cope with environmental factors such as surface textures and variations in brightness due to ambient light or changes in camera exposure. To address these limitations, we propose a method based on deep neural networks. Our approach aims to generate a single natural image from text-based prompts that not only appears realistic but also possesses rich spatial features to enhance registration accuracy in procam applications. We have developed a deep neural network trained on a synthesized dataset that simulates potential geometric and photometric distortions encountered in a procam system illuminating a relatively smooth object (see Figure 1). Our trained network predicts the correspondence between projector and camera images, significantly improving registration accuracy across various procam configurations. By jointly considering the naturalness and feature richness of the projector images, our method minimizes visual disruptions in projected content without sacrificing precision. A user study confirms that our technique enhances perceived naturalness and usability compared to existing methods, validating its practical utility in real-world applications.

---


### 110. [SHiPPO: Recurrent Memory with Transported Polynomial Projections](https://arxiv.org/abs/2607.03055)

**<font color=#1a73e8>作者：</font>** Tomoya Mizuguchi, Bum Jun Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> HiPPO gives recurrent states memory semantics as coefficients of online polynomial projections, but in fixed channel coordinates. Modern selective SSMs, by contrast, rely on token-dependent control and channel interaction. We introduce SHiPPO (Sylvester HiPPO), a transported projection-memory prior that lifts HiPPO coefficient memories into a moving channel frame. For any fixed or realized right-transport path, SHiPPO transports the approximation family and channel metric together; conditional on that path, the state is ordinary HiPPO in a tied moving frame and follows Sylvester coefficient dynamics, preserving the left online-memory operator while adding right-action transport. For selective-SSM execution, we derive a restricted group-local realization with controller-compatible right actions, exponential-adjusted updates, exact block-affine scan, and recurrent decoding. We also give a simultaneous-reducibility criterion identifying when right transports collapse to static mixing plus independent scalar or blockwise banks. Controlled diagnostics show that larger current-token write rank improves ordinary prediction error but cannot recover order-sensitive changes to already-written memory; transported-memory variants recover this signal, which disappears when the transport pathway is removed. A finite-field associative-recall diagnostic with interleaved bindings, operations, and queries provides complementary autoregressive evidence while leaving the preferred right-action realization open. Taken together, these results support SHiPPO as a mechanistically grounded transported-memory prior, with evidence focused on memory mechanisms rather than broad sequence-modeling dominance.

---


### 111. [RIGS-Refiner: Risk-Guided Recursive Refinement in Prediction Space for Colonoscopy Polyp Segmentation](https://arxiv.org/abs/2607.03058)

**<font color=#1a73e8>作者：</font>** Jiachi Zhang, Zhuoyu Wu, Wenqi Fang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-refinement can improve colonoscopy segmentation after host inference, but many designs still rely on extra correction heads or multi-stage pipelines with non-negligible parameter or computational cost. For polyp segmentation, host predictions are often already reasonable globally, with remaining errors clustered around ambiguous boundaries and difficult local structures. These residual errors matter in colonoscopy images because useful masks need correct lesion coverage and clean contour delineation across subtle mucosal transitions. This setting favors selective local repair in prediction space over reprocessing the entire mask. We therefore propose RIGS-Refiner, a lightweight post-refinement plugin for risk-guided recursive refinement in prediction space. Starting from a frozen host anchor prediction, RIGS-Refiner extracts lightweight image priors and prediction cues, applies risk-guided update, and writes back residual corrections through a shared recursive cell. The module adds only +519 parameters and +0.631 GFLOPs, keeping the refinement path compact for deployment. Experiments use Kvasir-SEG for training and Kvasir, ClinicDB, ColonDB, and ETIS for evaluation under two frozen hosts, namely PraNet and SegFormer-B0. Results show consistent gains on both hosts and a favorable efficiency-accuracy trade-off against representative post-refinement methods. Code is available at this https URL.

---


### 112. [Lightweight Polyp Segmentation via a Gain-Aware Prediction-Space Recursive Controller](https://arxiv.org/abs/2607.03062)

**<font color=#1a73e8>作者：</font>** Jiachi Zhang, Zhuoyu Wu, Quanjun Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While lightweight polyp segmentation is highly desirable for low-cost deployment, reported performance gains often stem from upgraded backbone encoders, complex decoders, or heavy refinement branches. Consequently, it remains difficult to isolate whether a lightweight correction mechanism is inherently effective on its own. We address this limitation by formulating refinement as a prediction-space recursive correction task, introducing a recursive controller that operates directly on backbone logits. Under a fixed recursion budget, this controller aggregates discrepancy and uncertainty evidence, updates a compact state tracking recent correction utility, and applies additive residual logit corrections. By design, this correction path remains small, host-portable, and deployment-explicit. Utilizing a unified Kvasir-trained protocol, we evaluate our approach across seven lightweight backbones on Kvasir-SEG and three transfer datasets, measuring segmentation accuracy (Dice/IoU) alongside deployment efficiency (parameters, GMACs, and peak memory). The controller yields consistent improvements in the source domain, achieves competitive performance against both training-side baselines and heavier structural refiners on representative hosts, and delivers selective transfer gains with minimal static overhead. Code is available at this https URL.

---


### 113. [PixCon: Clean-Positive Contrastive Learning for Foundation-Model Semi-Supervised Segmentation](https://arxiv.org/abs/2607.03068)

**<font color=#1a73e8>作者：</font>** Ebenezer Tarubinga  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Semi-supervised semantic segmentation (SSSS) has long turned on one question, which pseudo-labels to trust, and answered it with ever more careful confidence filtering. Foundation backbones change the regime: with a DINOv2 teacher a strict threshold already retains a measured 98%-clean pseudo-label set, so the accuracy that remains lives not in the filter but in how the embedding space is structured by class. We propose PixCon, a clean-positive pixel-contrastive framework. PixCon maintains a per-class memory bank that admits only labeled pixels the student already classifies correctly, guaranteeing a contamination-free positive set ($\rho_F=0$) by construction, unlike prior contrastive SSSS banks (ReCo, U$^2$PL) built from confidence-filtered pseudo-labels. It is a single branch over a consistency backbone, adds no inference-time parameters, and needs no bank-specific threshold. A first-order analysis of the supervised-InfoNCE gradient explains why contamination hurts: its false-positive term scales as $\rho_F/(1-\rho_F)$, which we measure (0.018 on Pascal, 0.106 on ADE20K) rather than assume. Across Pascal VOC, Cityscapes, and ADE20K, PixCon matches or improves a strong DINOv2-based UniMatch V2 baseline in a compute-matched one-switch protocol: it improves every Pascal-1/8 seed (a per-seed gain of about +0.2 mIoU) and its three-seed mean reaches 87.90, the published UniMatch V2-B figure. Because contamination is already rare under foundation-model teachers, our analysis indicates the $\rho_F=0$ guarantee acts chiefly as robustness as teachers weaken, while the accuracy gain comes from cleaner positive supervision, making clean-positive contrast a robust, low-cost default for foundation-model SSSS.

---


### 114. [SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)

**<font color=#1a73e8>作者：</font>** Wenlin Wu, Sheng Zhou, Peipei Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As video generation paradigms evolve from localized manipulation to full-scene synthesis, AI-generated video detection becomes increasingly challenging, as forgeries exhibit coherent global structure and high perceptual realism. However, existing benchmarks are biased toward perceptual fidelity and primarily evaluate detectors based on perceptual artifacts, providing limited coverage of scenarios that require reasoning about violations of physical laws, structural coherence, or social logic. This dataset bias shapes current approaches and results in a Perception-Reasoning Gap: artifact-centric models capture low-level statistical irregularities yet lack semantic inference, whereas vision-language models perform semantic reasoning but remain insensitive to fine-grained forensic cues. To bridge this gap, we propose SafeGuard, a multi-agent framework that enables collaborative specialization between forensic perception and semantic reasoning. A hierarchical perceptual solver extracts fine-grained forensic evidence, while a self-reflective verifier enforces consistency between semantic inference and physical plausibility, forming an interpretable evidence chain. To support evaluation, we introduce SafeVid, a novel AI-generated video detection benchmark comprising 20K videos spanning 10 social risk categories, designed to evaluate physical plausibility, structural consistency, and the rationality of social behaviors. Extensive experiments demonstrate the generalization of SafeGuard, improving accuracy on SafeVid by +18.7% and consistently outperforming prior methods across four public benchmarks.

---


### 115. [LOTUSim: Multi-Domain Simulator for Marine Robotics](https://arxiv.org/abs/2607.03072)

**<font color=#1a73e8>作者：</font>** Cédric Buche, Juliette Grosset, Hélène Lechêne 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Simulation is essential for maritime robotics, supporting operator training, mission rehearsal, and human-vehicle interaction in environments where real-world testing is costly or hazardous. Existing simulators focus primarily on autonomy systems and often lack human-in-the-loop interaction and realistic environmental physics. This paper introduces LOTUSim, an open-source, real-time maritime simulator supporting multi-user interaction across aerial, surface, and underwater robotic systems for coordinated naval-style operations. The first contribution of this work is enabling real-time interactive performance for users while ensuring scalability to large fleets operating within a shared interactive simulation environment. Validation demonstrates robust human-in-the-loop performance, maintaining strict real-time execution and high visual fidelity while scaling to large heterogeneous maritime drone swarms. The second contribution is a computationally efficient, Ekman-inspired layered, underwater current model that captures wind-driven, depth-dependent flow dynamics with sufficient physical fidelity for large-scale simulations. Validation against ocean reanalysis data demonstrates substantially improved accuracy compared to commonly used stochastic Gauss-Markov current models. These results confirm LOTUSim's suitability as a simulation platform for operatorin-the-loop maritime robotics research.

---


### 116. [Attention-Guided Efficientnet Architecture For Precise Criminal Identification in Surveillance Images](https://arxiv.org/abs/2607.03073)

**<font color=#1a73e8>作者：</font>** Savitha N J, Lata B T  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Criminal identification from surveillance imagery has become a critical research area in intelligent forensic surveillance systems due to the increasing deployment of CCTV cameras in public and private environments. However, surveillance-based face recognition remains highly challenging because of low image resolution, illumination variation, motion blur, pose changes, facial occlusion, and background clutter. To address these limitations, this paper proposes an Attention-Guided EfficientNet (AG-EfficientNet) framework for precise criminal identification in surveillance images. The proposed framework integrates EfficientNet-B0 with Convolutional Block Attention Modules (CBAM) to enhance discriminative facial feature learning under degraded surveillance conditions. In addition, a multi-scale surveillance feature fusion strategy is introduced to preserve both local texture information and high-level semantic identity representations. A hybrid Softmax-Triplet optimization mechanism is further employed to improve inter-class separability and intra-class compactness for robust criminal identity discrimination. The proposed framework was experimentally evaluated using the Labeled Faces in the Wild (LFW) and SCFace datasets. Experimental results demonstrate that the proposed AG-EfficientNet framework achieved superior surveillance recognition performance with an identification accuracy of 98.2%, Precision of 97.9%, Recall of 97.6%, F1-Score of 97.7%, and ROC-AUC of 0.99, outperforming conventional deep learning architectures including AlexNet, VGG16, ResNet50, MobileNetV2, and standard EfficientNet-B0. Furthermore, Grad-CAM visualization and ablation analysis confirm the effectiveness of the proposed attention-guided feature learning strategy.

---


### 117. [Robustness Meets Uncertainty: Evidential Adversarial Training for Robust Selective Classification](https://arxiv.org/abs/2607.03075)

**<font color=#1a73e8>作者：</font>** Nicolas Sournac, Ahmed Baha Ben Jmaa, Bertrand Braeckeveldt  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Safety-critical applications require classifiers that are both robust and reliable. Adversarial training is a widely adopted defense for improving robustness in deep neural networks; however, its effect on the reliability of predictive uncertainty remains underexplored. We investigate this gap through the lens of selective classification, which has rarely been systematically analyzed alongside adversarial robustness. We introduce a unified benchmark for the robustness-uncertainty trade-off. It standardizes architectures, augmentations, threat models, and evaluation metrics across clean, adversarial, and common-corruption settings. Across a wide range of state-of-the-art adversarial training methods, we uncover a recurring failure mode: several approaches improve robust accuracy while degrading uncertainty ranking, leading to poorer selective behavior. To address this, we propose Evidential Adversarial Training (EV-AT), which models uncertainty through a Dirichlet distribution and combines (i) an evidence-based loss promoting clean accuracy and reliable uncertainty with (ii) a robust evidence-alignment loss matching clean and adversarial predictions in log Dirichlet-parameter space. Extensive experiments show that EV-AT shifts the Pareto frontier of robustness-uncertainty trade-offs beyond prior state-of-the-art adversarial training methods. Our source code is publicly available at this https URL.

---


### 118. [Don't Wait to Reply: Towards Responsive yet Thoughtful Dialogue through Proactive Thinking](https://arxiv.org/abs/2607.03093)

**<font color=#1a73e8>作者：</font>** Ante Wang, Jiaqi Fu, Xuanyi Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Thinking has emerged as a critical capability for Large Language Models (LLMs) tackling complex tasks. However, its reactive nature, where reasoning is passively triggered only upon receiving a user response, inevitably introduces latency that compromises conversational fluidity. This stands in sharp contrast to human dialogue, where speakers proactively anticipate and plan future content during natural pauses to ensure seamless interaction. To bridge this gap, we propose Proactive Thinking, a framework that empowers models to pre-compute potential response elements during conversational downtime instead of waiting idly for the next input. We then introduce a training-free baseline that can think ahead by anticipating future states, balancing efficiency and quality through speculative continual thinking. To evaluate this approach in practice, we adapt three benchmarks of varying complexity into time-aware environments that simulate real-time conversational flow. We demonstrate that proactive thinking effectively improves interaction efficiency without compromising performance. Ultimately, this work advocates for a fundamental shift toward more intelligent, anticipatory, and real-time conversational AI.

---


### 119. [Heterogeneous Graph Condensation via Role-Aware Clustering](https://arxiv.org/abs/2607.03097)

**<font color=#1a73e8>作者：</font>** Fuyan Ou, Yulin Hu, Ye Yuan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous Graph Neural Networks (HGNNs) have exhibited remarkable efficacy in modeling complex systems with multiple types of nodes and relations, yet their training on large-scale heterogeneous graphs remains computationally prohibitive. Although graph condensation methods can effectively improve learning efficiency on large-scale graphs, existing condensation processes are mainly designed for homogeneous graphs and typically rely on computationally expensive gradient matching or bilevel optimization paradigms, rendering them impractical for heterogeneous settings. To address these limitations, we propose HGC-RC, a simple yet effective role-aware heterogeneous graph condensation framework. Specifically, HGC-RC first extracts semantically enhanced node embeddings via lightweight propagation. It then introduces a role-aware hybrid clustering strategy consisting of class-partitioned clustering for labeled target nodes to preserve class distributions and unsupervised type-wise clustering for non-target nodes to retain critical cross-type connectivity. Finally, a compact heterogeneous graph is efficiently reconstructed based on the resulting cluster assignments. Extensive experiments demonstrate that HGC-RC outperforms state-of-the-art baselines, offering a practical pathway to accelerate HGNN training on large-scale heterogeneous graphs without sacrificing task performance

---


### 120. [SNR-Adaptive Unified Diffusion for Multi-Task Medical Image Segmentation](https://arxiv.org/abs/2607.03103)

**<font color=#1a73e8>作者：</font>** Jiahao Liu, Hang Wei, Shuai Wu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Clinical cardiac imaging pipelines currently deploy separate models for each dataset and modality, incurring redundant training costs and precluding knowledge sharing across anatomically related tasks. Consolidating semi-supervised learning, unsupervised domain adaptation, and domain generalisation into one model is therefore a practical necessity, yet naive joint training exposes a fundamental barrier: conflicting label semantics between datasets collapse LA Dice from 90.31\% to 83.38\%, while gradient imbalance across tasks of unequal complexity suppresses the weaker tasks throughout training. We present UniT-Diff, a unified diffusion segmentation framework that resolves these conflicts through three targeted mechanisms. An 11-channel task-specific output space physically partitions label categories, eliminating cross-task gradient sign reversal by construction. SNR-Adaptive Task Conditioning (SATC) scales the task token by the log signal-to-noise ratio of the current diffusion timestep, suppressing domain-specific bias during coarse denoising and restoring full task guidance as the signal clears. Task-Type-Aware Conditional Dropout (TTACD) permanently removes the task token for domain-generalisation inputs, routing them through a shared neutral pathway that draws on cross-dataset cardiac anatomy rather than source-vendor statistics. Under a single parameter set, UniT-Diff surpasses independently trained task-specific baselines on all three benchmarks simultaneously: +0.87\% on LA, +1.77\% on MMWHS, and +0.88\% on MNMS.

---


### 121. [Observable- and Positional-Encoding-Dependent Symmetry Readout from Neural Network Weights](https://arxiv.org/abs/2607.03108)

**<font color=#1a73e8>作者：</font>** Naoya Chiba, Satoshi Sugiyama, Yuki Uranishi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-hoc analysis of trained neural network weights often seeks to recover geometric structure directly from the parameters. We show that, for positional-encoding-equipped neural fields, the symmetry visible from weights is not the true symmetry group itself, but an observable symmetry set determined by the trained parameters, the positional encoding (PE), and readout observable. We formulate this dependence through an exact observability hierarchy, $G_{\mathrm{obs}}^{\mathrm{exact}} \subseteq G_{\mathrm{lift}}^{\mathrm{exact}}(\phi) \cap G_{\mathrm{true}}$, where $G_{\mathrm{lift}}^{\mathrm{exact}}(\phi)$ is the set of input transformations that the PE can exactly lift to the feature space. The hierarchy implies that even when a target function has a geometric symmetry, that symmetry may be structurally invisible to weight-level observables if the PE does not represent the corresponding transformation. We test this prediction using MLPs trained on two-dimensional signed distance functions with multiple shape symmetry groups, positional encodings, and Gram-based observables. The results show a consistent PE-dependent pattern: DyadicAxisPE supports $D_4$-sensitive readout but structurally suppresses $D_3$ rotations, TriAxisPE yields lower $D_3$ / $D_6$ readout scores under the tested Gram observables by replacing coordinate axes with three 120-degree-separated axes, and random Fourier features mainly exhibit a $\pi$-rotation response under these readouts. These findings show that PE design affects not only approximation behavior but also which structures are accessible to post-hoc weight-level readouts. This provides a basis for a principled observable-dependent symmetry readout.

---


### 122. [ExpoMotion: A Large-Scale Benchmark and A Householder Projection Network for Multi-Exposure Fusion](https://arxiv.org/abs/2607.03110)

**<font color=#1a73e8>作者：</font>** Yao Liu, Lishen Qu, Shihao Zhou 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-Exposure Fusion (MEF) effectively extends dynamic range, but practical deployment is hindered by motion-induced ghosting and the scarcity of high-quality dynamic benchmarks. Current benchmarks largely neglect dynamic scenes and lack reliable ground truth, making it difficult to handle the complexity of real-world motions. In response, we introduce ExpoMotion, a large-scale benchmark designed to evaluate deghosting capabilities. Comprising 1,738 sequences and 10,909 images across diverse environments, it covers a wide range of motions and provides high-fidelity GTs constructed through an expert-guided acquisition pipeline. To tackle the complex dynamics and extreme conditions captured in this benchmark, we propose the Householder Orthogonal Projection network (HOP), which revisits MEF deghosting from a mathematical perspective via Householder transformation, decoupling multi-frame alignment into exposure pre-alignment and ghost filtering. Specifically, the Global Priors Illumination Alignment (GPIA) module first rectifies drastic dynamic range discrepancies by utilizing global statistics for exposure harmonization. Regarding ghost removal, our Householder Orthogonal Attention (HOA) models artifacts as orthogonal perturbations. By employing a dynamic Householder reflector, HOA effectively projects ghosts out of the feature manifold while preserving high-frequency details. Experiments demonstrate that our ExpoMotion dataset enables superior generalization and artifact-free detail restoration, while also validating the effectiveness and efficiency of the HOP method. The dataset and code are available at this https URL.

---


### 123. [Vidu S1: A Real-Time Interactive Video Generation Model](https://arxiv.org/abs/2607.03118)

**<font color=#1a73e8>作者：</font>** Jintao Zhang, Kai Jiang, Jintao Chen 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Vidu S1, a real-time interactive video generation model supporting voice control of digital characters. Users can control video generation content at any moment through voice instructions. Vidu S1 supports infinite-length real-time video generation without blurring, drift, or visual distortion. Built with TurboDiffusion and TurboServe, Vidu S1 outputs 540p real-time videos at up to 42 FPS on regular consumer GPUs. Users can upload custom images of real people, anime, and pets, and choose different voice tones for personalized experiences. Experiments show that Vidu S1 achieves the best performance across all test metrics while fully meeting real-time inference requirements. A playable online demo is available at this https URL.

---


### 124. [Integrating Physics-Informed Neural Networks for Safe Reinforcement Learning in a 1-DoF Helicopter System](https://arxiv.org/abs/2607.03125)

**<font color=#1a73e8>作者：</font>** Georg Schäfer, Jakob Rehrl, Stefan Huber  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) offers powerful control for industrial cyber-physical systems (ICPSs), but its "black-box" exploration risks violating strict hardware safety limits. Typically, these constraints are managed through complex reward shaping. In this work-in-progress paper, we embed a differentiable physics model directly into the proximal policy optimization (PPO) actor loss function. By simulating short-horizon future trajectories during training, the policy is penalized for anticipated safety violations independent of the task-reward signal. Evaluated on a simulated 1-degree-of-freedom helicopter testbed with strict pitch constraints, our physics-informed soft regularizations substantially reduce constraint violations while maintaining reliable target tracking.

---


### 125. [A Multi-Task Deep Learning Framework for Real-Time Intelligent Video Surveillance with Temporal Event Validation](https://arxiv.org/abs/2607.03131)

**<font color=#1a73e8>作者：</font>** Estera Dumitru, Stelian Spînu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern video surveillance systems generate far more video streams than human operators can effectively monitor, making automated analysis essential for timely detection of security events. This paper presents a unified multi-task deep learning framework that simultaneously performs face recognition with zone-based authorization, automatic license plate recognition, weapon detection, fire and smoke detection, and human action recognition on a shared GPU platform. Among the integrated modules, two task-specific deep-learning models are proposed in this work to address scenarios that are insufficiently represented in publicly available datasets: a single-class weapon detector fine-tuned on a merged and relabeled dataset, achieving a mean average precision (mAP@0.5) of 0.947, and a SlowFast-R50 action recognition model trained on a purpose-built vandalism dataset comprising 614 video clips, achieving 94.33% classification accuracy. To improve robustness in continuous video, all detection modules are integrated into a temporal event-validation architecture based on multi-frame confirmation, confidence-weighted voting, and cascaded filtering, transforming frame-level predictions into reliable security events. Each module is evaluated independently on established public datasets (LFW, D-Fire, FIRESENSE, and UCF-Crime), followed by integrated end-to-end system evaluation. The proposed temporal validation strategy reduces the fire and smoke false-alarm rate from 52% to 4% and improves video license plate exact-match accuracy from 66.7% to 81.8%, while the complete framework maintains real-time operation with a per-frame latency below 100 ms on commodity hardware. These results demonstrate that combining specialized deep-learning models with temporal event validation provides an effective and practical solution for reliable real-time intelligent video surveillance.

---


### 126. [Anticipatory Reinforcement Learning for Trajectory Tracking](https://arxiv.org/abs/2607.03132)

**<font color=#1a73e8>作者：</font>** Georg Schäfer, Jakob Rehrl, Stefan Huber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep reinforcement learning (DRL) in industrial control often suffers from lag and overshoot due to purely reactive control based on the current tracking error. To achieve anticipatory control without high computational overhead, we introduce a predictive formulation that augments the DRL state space with target velocities and future reference horizons. Evaluating eight configurations using proximal policy optimization (PPO) on a 1-degree-of-freedom (1-DoF) helicopter testbed, simulation results showed a 9-fold error reduction, lowering the mean absolute deviation from 2.73° to 0.31°. However, zero-shot transfer to physical hardware revealed a sim-to-real gap. Interestingly, a simpler configuration using a single, further look-ahead horizon matched the real-world top performance of the most complex model (1.11°). Overall, evaluating various combinations of prediction horizons and target velocities demonstrated that highly granular predictive data is not necessarily required for physical transfer.

---


### 127. [Sample-Efficient Pareto Front Modeling for Energy-Aware Reinforcement Learning Using Bayesian Optimization](https://arxiv.org/abs/2607.03140)

**<font color=#1a73e8>作者：</font>** Georg Schäfer, Jakob Rehrl, Stefan Huber 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Industrial automation increasingly demands control strategies that balance operational performance with strict energy efficiency requirements. A common approach to solving this multi-objective problem, particularly within the framework of reinforcement learning (RL), is to formulate a single, scalar reward function that linearly combines the competing objectives. However, the manual weighting of these different objectives is heavily reliant on domain intuition, incredibly time-consuming, prone to human bias, and frequently fails to uncover optimal trade-off solutions. This work addresses the critical challenge of automating the weight selection process to systematically and efficiently discover the Pareto front of optimal trade-off policies. We formulate the weight selection process as a multi-objective Bayesian optimization (MOBO) problem and evaluate its sample efficiency against a standard uniform grid search baseline. Using a physical Quanser Aero 2 testbed configured for 1-DoF pitch control, our results demonstrate that the MOBO approach, utilizing the expected hypervolume improvement (qEHVI) acquisition function, consistently outperforms uniform grid sampling. MOBO achieves superior hypervolume and maximum spread, successfully identifying high-quality, diverse trade-off policies with a reduced evaluation budget, thereby enabling highly efficient energy-aware control in complex mechatronic systems.

---


### 128. [CuBAS: Information Geometric Curvature-Based Adaptive Sampling for Supervised Classification](https://arxiv.org/abs/2607.03145)

**<font color=#1a73e8>作者：</font>** Alexandre L. M. Levada  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The informativeness of a training set is as consequential as its size, yet most sampling strategies remain agnostic to the intrinsic geometry of the data distribution. We introduce CuBAS (Curvature-Based Adaptive Sampling), an information-geometric framework for adaptive data selection in supervised classification, grounded in the q-state Potts Markov random field (MRF) model. The central insight is that a labeled dataset can be viewed as a statistical manifold, on which local curvature, estimated via the ratio of second to first-order observed Fisher information, faithfully encodes the geometric complexity of the data distribution. We construct a k-nearest-neighbor graph over the labeled data and derive a closed-form curvature score at each vertex from the Potts sufficient statistics. This curvature signal partitions the graph into two complementary regimes: low-curvature regions, corresponding to smooth, homogeneous clusters, and high-curvature regions, concentrated around decision boundaries that are disproportionately informative for classification. By selecting nodes from both regimes, CuBAS constructs compact yet maximally informative training subsets. Empirical evaluation across more than 60 benchmark datasets demonstrates consistent and statistically significant improvements over random sampling and uncertainty-based baselines, across a wide range of labeling budgets and classifier architectures. CuBAS is computationally efficient (linear in the number of k-NN graph edges), theoretically grounded in the differential geometry of statistical manifolds, and interpretable in terms of the local shape operator of the data manifold.

---


### 129. [Rethinking Neural Nonlinearity as Gating](https://arxiv.org/abs/2607.03148)

**<font color=#1a73e8>作者：</font>** Muhammad Sabih, Frank Hannig, Jürgen Teich  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation functions are considered an essential primitive for neural nonlinearity, i.e., they enable neural networks to serve as universal approximators. In this paper, we show that this nonlinearity can also be achieved by input-conditioned threshold gating through branches as a universal primitive. We demonstrate that standard activations -- whether piecewise-linear (ReLU, PReLU, Hardtanh) or smooth (SiLU, Sigmoid, Tanh, GELU) -- are in fact instances of a single Threshold Gating (TG) primitive. For softmax, we show that it admits an exact TG conversion via its equivalent per-element Sigmoid form. We then validate these equivalences by converting pretrained networks across CNNs, transformer-based models, and recurrent architectures, preserving model performance without requiring retraining. Threshold Gating also enables training from scratch that goes beyond replacing existing activations, enabling gains in model compression, performance, and shorter training. We also propose a 'Minimal Branch Theorem' which relates the minimum number of required branches in our primitive to the trainability of general deep neural networks. In terms of hardware implementation, TG maps to a unified implementation in the case of analog in-memory systems, addressing the bottleneck of analog-to-digital and digital-to-analog converters (ADC/DAC) that is known to significantly impact power consumption and on-chip area.

---


### 130. [Conditional Diffusion Guided Knowledge Transfer for Multi-Domain Knowledge Graph Completion](https://arxiv.org/abs/2607.03154)

**<font color=#1a73e8>作者：</font>** Jiawei Sheng, Taoyu Su, Xixun Lin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-domain knowledge graph completion (MKGC) aims to improve missing triple prediction in a target KG by transferring knowledge from other support KGs. Existing methods typically enforce consistency constraints on equivalent entities across KGs to transfer knowledge, which risks suppressing domain-specific contextual information of entities. This design can also compromise entity representation information from all KG domains, impeding performance improvements, especially in low-resource data scenarios. To address this, we pioneer a generation-based paradigm for MKGC and propose DMKGC, a conditional diffusion-guided knowledge transfer framework. Our key insight is to treat each KG as a partial view of the entity entire information, and generate informative domain-general entity embeddings through diffusion models conditioned on support KGs. Particularly, we first initialize domain-agnostic entity embeddings as prior entity embeddings, and then encode them within individual KGs. Afterward, we fuse equivalent entities from support KGs as the conditional diffusion generation guidance. We leverage the prior entity embeddings as the proxy generation objective, which ensures this conditional generation to be unbiased towards any conditioned KGs. Simultaneously, we also train the generated embeddings to be predictive across KGs, thus preserving domain-specific information. Extensive experiments on 14 KGs in 3 benchmarks demonstrate a 4.3\% average MRR improvement in tail entity prediction over state-of-the-art methods, with sustained gains in low-resource data settings.

---


### 131. [DistillH-Mamba: A Hypergraph-Mamba-Based Knowledge Distillation Model for Efficient Impact Fall Detection](https://arxiv.org/abs/2607.03156)

**<font color=#1a73e8>作者：</font>** Tresor Y. Koffi, Youssef Mourchid, Mohammed Hindawi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Falls among the elderly represent a significant public health concern due to their prevalence, consequences, and societal burden. While deep learning has improved fall detection, accurately identifying impact moments (when an individual hits the ground) remains challenging. Additionally, current algorithms often rely on complex models with high computational demands, limiting real-time deployment feasibility. In this work, we propose DistillH-Mamba, a novel architecture for impact fall detection that addresses these challenges through three key innovations: First, we introduce a hypergraph-based approach that captures higher-order relationships between multiple joints simultaneously, enabling more accurate modeling of complex interactions during impact falls. Second, we integrate the Mamba architecture with hypergraphs for impact detection, significantly accelerating processing speed while efficiently capturing both long-term dependencies and sudden skeletal motion changes. Third, we employ relational knowledge distillation that preserves crucial spatial-temporal relationships while reducing computational demands for real-time impact fall detection. Evaluated on the 3D Skeletons UP-Fall and UMAFall datasets, our DistillH-Mamba model achieves 97.38% accuracy in detecting impact within fall events and 73.8% reduction in inference time compared to its teacher model, outperforming state-of-the-art methods in both precision and efficiency.

---


### 132. [Rethinking Brain Decoding with CLIP: The Role of Adversarial Robustness](https://arxiv.org/abs/2607.03165)

**<font color=#1a73e8>作者：</font>** Byeongseo Bok, Futa Waseda, Jun Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Brain decoding aims to uncover neural mechanisms by inferring stimulus-related representations from brain signals. In fMRI studies, this is typically achieved by mapping fMRI responses to the latent representations of computational models. Recently, CLIP has become a popular choice for brain decoding due to its rich vision--language embedding space. However, aligning fMRI signals with CLIP representations remains challenging. As CLIP is not explicitly optimized for neural alignment, its representations may capture statistically predictive cues that are only partially reflected in brain activity, limiting decoding performance. In this paper, we investigate whether adversarially robust representations improve neural decoding with CLIP. Adversarial training suppresses non-robust features and promotes more stable, perceptually structured representations, which may better align with brain activity. We evaluate this by fixing the fMRI decoder and varying only the target representation (standard CLIP vs. robust variants) on fMRI-image retrieval and zero-shot classification tasks across NSD and GOD datasets. Empirical results show that this simple change consistently improves task performance and yields stronger alignment across multiple metrics. Attribution analysis further reveals consistently low agreement between standard CLIP and its robust variants, suggesting that adversarial robustness reorganizes feature importance in the visual representation. These findings suggest that the choice of target representation influences neural decoding performance and that adversarial robustness may serve as a useful criterion for brain decoding.

---


### 133. [Decentralised Federated Learning over Temporal Networks: The Role of Heterogeneities](https://arxiv.org/abs/2607.03171)

**<font color=#1a73e8>作者：</font>** Arash Badie-Modiri, Chiara Boldrini, Lorenzo Valerio 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralised federated learning, based on peer-to-peer communication, is increasingly proposed for on-device training of machine learning models, promising a privacy-preserving, communication-efficient training process with no risk of single-point failure. However, the role of structural and temporal inhomogeneities in such fully decentralised settings remains poorly understood. Here, we investigate their effects when model parameters are locally averaged during aggregation. We show that the decentralised federated learning process is governed, both in the early phase and the late, stationary limit, by the same dynamics as a lazy random-walk diffusion process on temporal networks. Based on this mapping, we demonstrate that the typical experimental scenario used in decentralised federated learning leads to unrealistically rapid convergence because of ignoring the temporal and structural inhomogeneities inherent in the communication network. We analyse real-world temporal networks and find that inhomogeneities most often dramatically slow down diffusion, hence the convergence process.

---


### 134. [Understanding electricity consumption behaviour through Inverse Reinforcement Learning](https://arxiv.org/abs/2607.03176)

**<font color=#1a73e8>作者：</font>** Enrico Cofler, Carlos Rodriguez-Pardo, Matteo Giuliani 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how households consume electricity in response to socioeconomic and climatic drivers is important for decision-makers designing energy policies in a changing climate and under geopolitical tensions. Consumers respond differently to thermal stress depending on income, consumption habits and the surrounding built environment, a nonlinear behaviour that most approaches oversimplify. In this study, households are treated as agents interacting with complex environments, and Inverse Reinforcement Learning is used to represent their consumption behaviour as model implied reward functions. Specifically, we observe how these reward functions change when households undergo socioeconomic and climatic shocks. The framework is tested on different clusters of electricity consumption profiles in Italy. Clusters' reward functions are retrieved and used to understand how cooling behaviour changes from summer 2021 to summer 2022 and 2023, before, during and after the energy crisis and a heatwave. We find that these shocks reshaped cooling behaviour heterogeneously across consumer groups, in directions conditioned by their prior habits and built environment. Across the 2021 to 2023 summers, we identify a spectrum of responses: transient adjustments that receded as the shocks eased, durable shifts persisting into 2023, and consumers exhibiting negligible change. At the intradaily scale, groups comparable in socioeconomic and environmental context but differing in their daily timing of consumption responded distinctly, identifying time of use as a separate dimension of behavioural heterogeneity. Energy policies and demand-response schemes should therefore account not only for who consumers are and where they live, but for when they consume and whether their response to a shock persists.

---


### 135. [FairFlow: Demystifying and Mitigating Stereotype Bias in Text-to-Image Diffusion Transformers](https://arxiv.org/abs/2607.03180)

**<font color=#1a73e8>作者：</font>** Chen Chen, Yuanmin Huang, Zhenfei Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal diffusion transformers (MM-DiTs) have emerged as the prevalent backbone for modern text-to-image generation systems. However, they exhibit critical alignment vulnerabilities, systematically manifesting severe stereotype biases even under benign prompts. This poses a significant risk of algorithmic discrimination in deployed systems. Since most existing mitigation strategies were tailored for legacy U-Net architectures, the precise remediation of these vulnerabilities in MM-DiTs remains a critical open challenge. In this work, we first investigate the root cause of this vulnerability via mechanistic analysis. We reveal that bias representations in MM-DiTs are not uniformly distributed across depth, but are mediated by a sparse set of layers functioning as internal semantic binding hubs. These hubs exhibit a stage-wise propagation driving bias manifestation: early hubs establish the structural templates susceptible to bias, middle hubs actively extract core stereotypical concepts from textual conditioning, and late hubs globally solidify these biases through visual self-attention. Leveraging these architectural insights, we propose FairFlow, an intrinsic, mechanism-guided mitigation framework. FairFlow acts as an internal regulator by employing sparse steering: it learns attribute-specific fair directions and injects them exclusively at the identified semantic hubs within a constrained inference window. Evaluations on FLUX.1-dev and Stable Diffusion~3 demonstrate that FairFlow effectively neutralizes these stereotypical vulnerabilities across gender, race, and intersectional settings, achieving an optimal fairness-fidelity balance. With near-zero inference overhead and robustness to complex prompts, FairFlow provides a lightweight and practical bias mitigation for large-scale deployed MM-DiT systems. Code and datasets will be publicly released upon acceptance.

---


### 136. [A Bayesian Framework for Evaluating Scenario Compatibility in Generative Population Synthesis](https://arxiv.org/abs/2607.03190)

**<font color=#1a73e8>作者：</font>** Zhenlin Qin, Leizhen Wang, Yancheng Ling 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scenario-based transportation analysis specifies future assumptions through aggregate population targets, whereas generative population synthesis models produce detailed individual-level realizations. When scenario targets are imposed on generative models, current practice relies on deterministic marginal calibration, implicitly assuming that the targets are compatible with the model's learned structural support. However, whether scenario-level constraints lie within the generative support--and how strongly they distort structural uncertainty--remains largely unexamined. We propose an ensemble-based Bayesian updating framework to quantify scenario compatibility in conditional population synthesis. A population-aware conditional variational autoencoder is developed to learn a distribution over plausible population structures while preserving aggregate fidelity. An ensemble of realizations sampled from the learned prior provides an empirical approximation of structural uncertainty. Scenario targets are treated as probabilistic evidence over aggregate statistics, and posterior weights are obtained through Bayesian updating across the ensemble. Scenario compatibility is quantified using effective sample size (ESS), which measures posterior concentration and the compression of structural uncertainty induced by conditioning. Experiments demonstrate that scenario impact depends not only on target magnitude but also on alignment with the learned joint structure, and reveal structural failure modes when targets fall outside prior ensemble support. The proposed framework provides a probabilistic diagnostic model for evaluating scenario feasibility and structural consistency before downstream projection and transportation planning.

---


### 137. [Seeing Through WiFi: Lightweight Human Pose Estimation with Dynamic Kernel Attention](https://arxiv.org/abs/2607.03196)

**<font color=#1a73e8>作者：</font>** Toan D. Gian, Van-Dinh Nguyen, Vo Phi Son 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> WiFi-based human pose estimation (HPE) enables the detection and interpretation of human body positions and movements without the need for wearable devices while preserving individual privacy concerns. Implementing this solution requires enhancing model performance and maintaining efficiency, especially on resource-constrained devices. This paper introduces a novel framework, WiLHPE, for lightweight and efficient human pose estimation using WiFi CSI signals. Empowered by a camera-based model during training, WiLHPE processes raw WiFi signals directly to estimate human poses in the testing phase. It employs a novel neural network architecture to dynamically learn convolutional kernels and apply attention mechanisms across channel and frequency spaces. This innovative method diversifies the kernels to improve the recognition capabilities of WiFi signals without adding complexity, ensuring efficiency. Additionally, the Tree-Structured Parzen Estimator algorithm is employed to optimize the critical hyperparameters of the neural network efficiently, minimizing the time required for optimal hyperparameter search compared to heuristic methods. Results from experiments on both the MM-Fi and WiPose datasets highlight the superiority of WiLHPE over state-of-the-art approaches, achieving 85.96% and 94.27% at PCK50, respectively, with minimal computational overhead. Notably, WiLHPE performs impressively even under challenging conditions, maintaining around 80% at PCK50 under AWGN noise with an error variance of 0.5.

---


### 138. [OpFlow: Learning Opportunity-Conditioned Choice Potentials for Robust OD Flow Prediction](https://arxiv.org/abs/2607.03200)

**<font color=#1a73e8>作者：</font>** Changjian Liu, Yong Gao, Yuqing Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Origin-destination (OD) flow prediction is central to urban analytics, yet deep models trained on raw counts remain vulnerable to distribution shift. The core problem is that raw count supervision cannot distinguish transferable choice mechanisms from environment-specific shortcuts. Raw OD count mixes two objects: how much demand an origin produces and how that demand is allocated across destinations. We argue that the transferable object is the exposure-to-choice law that maps spatial conditions to relative destination preferences. We propose OpFlow, a mechanism-constrained framework that learns row-centered choice potentials and reconstructs flows by combining the induced allocation with a separately calibrated origin scale. Under distribution shift, spatial exposures and the induced allocations are allowed to vary; what transfers is the conditional map from exposure states to relative choice potentials. Theoretically, we characterize the identifiable row-centered potential and show that classical spatial interaction laws are restricted log-potential cases. Controlled synthetic shifts and a real-world experiment show OpFlow improves robustness under environment shifts.

---


### 139. [S-DiverSe: Spanish Diverse Speech](https://arxiv.org/abs/2607.03207)

**<font color=#1a73e8>作者：</font>** Fernando López, Fernando Ibañez, Ana Martínez 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatic speech recognition (ASR) has advanced remarkably for standard speech, yet speech affected by neurological conditions remains a challenge. We present S-DiverSe (Spanish Diverse Speech), a corpus of 3.2 hours of in-the-wild Spanish speech from 22 speakers with amyotrophic lateral sclerosis, Parkinson's disease, and stroke. The dataset contains 444 manually transcribed audio segments with metadata on speaker sex, disease type, and intelligibility. S-DiverSe is designed to support ASR evaluation and development for neurologically affected Spanish speech. We describe the dataset, analyze its composition, and report baseline ASR results alongside initial adaptation experiments. Our findings reveal that heuristic text post-processing is more robust than fine-tuning for out-of-domain neurological Spanish speech. This underscores the need for dedicated in-the-wild Spanish benchmarks.

---


### 140. [Transition Information Density: Morphological Trajectories, Synesthetic Perception, and Structured Interpolation in Neural Training (or: The Synesthetic AI)](https://arxiv.org/abs/2607.03210)

**<font color=#1a73e8>作者：</font>** Sam Mao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard machine learning training presents data as discrete endpoint pairs, omitting the structure of the space between them. This paper introduces Transition Information Density (TID) -- the information content recoverable from structured intermediate states between categorically distinct training endpoints -- and Positional Identity, the defined location of an intermediate state on the A-to-B continuum. Both constructs are grounded in three empirical contexts: grapheme-color synesthesia, the Synesthesia Grid (a boundary-contour morphing algorithm instantiating TID in visual morphological space), and a four-condition training experiment across four representational mediums. Probes trained on structured interpolation at defined Positional Identities (C3) exhibit substantially lower intrinsic dimensionality than volume-matched controls (C2) in Phonetic/Linguistic (C3: 3.33 vs. C2: 10.81) and Semantic Description (C3: 4.59 vs. C2: 8.67) mediums. Visual and cross-modal mediums do not show this effect, establishing a modality boundary condition. A fixed-N=50 comparison confirms that Positional Identity structure, not sample count, drives the effect. Resolution N scales monotonically with representational richness. Pooled TwoNN analysis reveals globally collapsed representations in visual space (0.075) and globally consistent representations in phonetic space (0.977). The paper contributes a formal definition of TID and Positional Identity, a nine-metric shape characterization framework, and a four-condition experimental design isolating trajectory structure, data volume, and Positional Identity as distinct factors.

---


### 141. [Builder, Defender, Breaker: The Case Against Removing the Human from the AI-Driven Security Lifecycle](https://arxiv.org/abs/2607.03215)

**<font color=#1a73e8>作者：</font>** Mohamed Chahine Ghanem  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence has spread across the whole of the security lifecycle. The same family of models now writes application code, hardens it, and probes it for weaknesses, so that a single generative substrate increasingly performs all three roles at once. Enthusiasm for this convergence tends to treat full autonomy as the natural end point of partial assistance. This article argues that it is not. When the system that builds an artifact is drawn from the same distribution as the systems that defend and test it, the three roles inherit a common set of blind spots, and the independence that makes verification meaningful is quietly lost. Removing the human does more than raise the automation level: it collapses the external oracle against which machine output is judged, outruns the point at which a person could intervene, hands adversaries a predictable and poisonable target, and dissolves the locus of accountability when something fails. Drawing on evidence from autonomous code generation, adversarial machine learning, software fault tolerance, and the first all-machine hacking tournaments, we argue that the human belongs in the loop not as a temporary scaffold but as a permanent structural requirement, and set out what a defensible division of labour between people and machines should preserve.

---


### 142. [Joint distribution of upstream runoff governs downstream river-discharge prediction uncertainty in distributed ML models](https://arxiv.org/abs/2607.03217)

**<font color=#1a73e8>作者：</font>** Karan Ruparell, Tristan Hascoet, Takemasa Miyoshi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Uncertainty quantification of hydrological predictions is necessary to inform operational decisions. Recent generative machine-learning methods have advanced probabilistic streamflow prediction, but have remained confined to lumped models that predict a basin outlet directly. At the same time, deterministic LSTM runoff models are increasingly applied at grid or catchment scale and routed through river networks to produce spatially continuous, physically consistent discharge fields. This technical note argues that moving probabilistic prediction from lumped to distributed models introduces a specific new requirement: the joint distribution of upstream runoff generation must be sampled jointly. In lumped inference, the model predicts the outlet distribution directly and can modulate spread from basin attributes. In distributed inference, downstream discharge is obtained by routing many upstream runoff predictions, so independent local sampling averages uncertainty away. Using Japan as a case study, we train two probabilistic basin-scale runoff LSTMs and route their runoff through a Hayami routing scheme. Randomly matching upstream ensemble members produces severely under-dispersed downstream ensembles, whereas a simple quantile matching strategy restores much of the spread of the direct basin-scale reference. The shift from lumped to distributed probabilistic hydrology therefore requires explicit attention to the spatial joint structure of runoff uncertainty.

---


### 143. [CONTRA: Red-Teaming Configurations of Personalizable Agents](https://arxiv.org/abs/2607.03220)

**<font color=#1a73e8>作者：</font>** Jonathan Nöther, Adish Singla, Goran Radanovic  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Recent tools such as OpenClaw have extended the capabilities of LLM-based agents from simple dialog-based systems to fully autonomous agents. These systems allow personalization of the agent through modifiable internal files and the installation of skills. While this enables deployment in a wide range of settings and the automation of diverse tasks, greater capability and autonomy increases the risk of malicious actions being executed unintentionally. In this work, we explore the interplay between agent configuration and the risk of executing dangerous actions without explicit instruction. To this end, we propose CONfiguration Tree-search for Red-teaming Agents (CONTRA), an LLM-assisted tree-search algorithm that discovers agent configurations resulting in the execution of malicious actions. CONTRA works by reasoning about benign yet dangerous configurations and evaluating them in a simulated environment. We construct a dataset of the 473 most popular skills from a public repository, along with 2-5 corresponding malicious target actions per skill. In a large-scale analysis, we find that 75.1% of skills have at least one configuration resulting in the execution of a malicious action, most of which have not been detected as containing malicious content by existing scans. Overall, CONTRA successfully identifies a configuration leading to the execution of the target action in 39.2% of all tested cases. Our findings demonstrate that current agents provide insufficient safety with respect to personalization.

---


### 144. [Learning to Suppress SPAD-based LiDAR Flare](https://arxiv.org/abs/2607.03247)

**<font color=#1a73e8>作者：</font>** Xuanya Zhu, Linghao Shen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-Photon Avalanche Diode (SPAD)-based Light Detection and Ranging (LiDAR) is emerging for autonomous vehicles due to its high sensitivity and precise depth sensing capabilities. However, flare caused by excessive photon returns or pile-up effects can lead to incorrect depth estimation and exaggerated boundaries in point clouds, resulting in severe distortions of geometric measurements, making flare suppression essential for safety-critical applications. Existing flare mitigation methods primarily operate at the hardware or signal-processing levels. While effective under specific configurations, they are largely rule-based and configuration-dependent, lacking learnable representations that generalize across diverse sensing scenarios. In this work, we reformulate flare suppression as a semantic segmentation problem, enabling data-driven learning of geometric and photometric cues directly from SPAD measurements. We first benchmark representative segmentation models on the newly introduced SPAD flare dataset and observe that they struggle to exploit the intrinsic multi-echo characteristics of SPAD signals. Motivated by this observation, we propose Physically-Informed segmentation for LiDAR Flare (PILF), a learning-based approach that treats the first and second echoes, together with ambient illumination, as distinct modalities, aggregating cross-echo information while jointly encoding geometric and photometric features. Experiments across multiple real-world scenes demonstrate that PILF significantly outperforms compared segmentation models, achieving up to 79.32% mIoU, and providing an effective solution for SPAD-based LiDAR flare suppression.

---


### 145. [Semantic Segmentation-Driven Image-Level Diagnosis of Liver Cancers in Hematoxylin and Eosin Histopathology Images](https://arxiv.org/abs/2607.03253)

**<font color=#1a73e8>作者：</font>** Ivica Kopriva, Dario Sitnik, Arijana Pacic 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As hematoxylin & eosin (H&E) staining constitutes the primary entry point in routine diagnostic workflows, computer-aided diagnosis from whole-slide H&E images is of particular clinical relevance. However, substantial variability in specimen preparation, staining protocols, and scanning conditions, together with inherent uncertainty in expert pixel-level annotations, makes automated analysis of H&E-stained images challenging. In this study, we propose a semantic segmentation-based framework for image-level diagnosis, grounded in the clinically motivated assumption that each histopathological image corresponds to a single cancer type. Image-level predictions are obtained by assigning the class of the dominant pixel-level label in the segmentation output. To ensure clinical relevance, we adopt the nnU-Net architecture and train it on a publicly available dataset collected in our study with pixel-level annotations for three liver cancer types: hepatocellular cacrcinoma (HCC; 55 images from 30 patients), cholangiocellular carcinoma (CCA; 55 images from 29 patients), and colorectal metastatic adenocarcinoma (CMA; 60 images from 30 patients). Annotations were independently provided by four pathologist. We hypothesize that the combination of stain normalization and semantic segmentation mitigates domain shift and reduces sensitivity to annotation noise. Five-fold cross-validation yielded balanced accuracy of 0.975 (HCC), 0.950 (CCA), and 1.000 (CMA), comparable to results obtained with immunohosthochemical staining and superior to several deep learning models trained on patch-level annotations. The proposed framework has the potential to support pathologists in prioritizing immunohistochemical marker selection, thereby reducing diagnostic costs and turnaround time. Integration with immunohistochemical findings improve overall diagnostic reliability.

---


### 146. [A Decomposable Probe for Few-Step Diffusion Models: Prompt, Latent, and Score Selectivity across Backbone Families and Distillation Paradigms](https://arxiv.org/abs/2607.03256)

**<font color=#1a73e8>作者：</font>** Patrick Mu Haojie  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-step distilled diffusion students cut text-to-image inference from ~50 to 1-8 network evaluations, but the quality gap is usually summarised by a single FID/CLIP scalar that cannot say which axis of the conditioning response changed, nor whether a behaviour comes from the architecture, the distillation objective, or simply from being a diffusion model. We replace the scalar with a decomposable probe that injects controlled perturbations along three layers (prompt encoder, denoiser input, denoiser output) under three modes (mean, variance, scale) and six strengths, reporting a bootstrap-median Bures W2^2 selectivity ratio on Inception features. Under a single matched estimator across 23 models -- five teachers and 18 distilled students spanning five backbone families (SDXL, SD1.5, SD3.5, PixArt-alpha, FLUX), three architecture classes (UNet, DiT, MMDiT), and five distillation paradigms -- the three layers read three empirically separable factors: the prompt layer is a universal prompt-mean response (a sanity channel, not a discriminator), the latent layer reads the prediction type, and the score layer reads the distillation objective. Our main result: within this sweep, the latent layer is a near-binary detector of rectified-flow backbones. Its ratio exceeds 1 across a sustained low-to-mid band only for rectified-flow models (SD3.5, FLUX); no epsilon-prediction model qualifies. A matched epsilon-prediction control (PixArt-alpha) rules out wide-T5 conditioning, and the fingerprint survives adversarial (ADD) distillation as both teacher and student. Two secondary score-layer findings hold under narrower scopes: a canonical 4-step ADD-vs-rest contrast on the UNet families with a non-ADD baseline, and a CI-separated trajectory-rollout early-strength score spike on both UNet and DiT. All ratios are CI-citable under one estimator; we release the per-cell tables and the estimator.

---


### 147. [Defending from GeoLocalization through Adversarial Road Trips](https://arxiv.org/abs/2607.03277)

**<font color=#1a73e8>作者：</font>** Niccolò Niccoli, Federico Becattini, Lorenzo Seidenari  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Retrieval-based image geolocalization has emerged as a powerful technique for determining the location of a query image by matching it against a large, geotagged database. The success of deep learning based approaches has raised concerns regarding privacy and safety. A way to protect users from geolocalization is to design adversarial attacks for such methods. In this paper, we introduce RoadTrip Attack (RTA), a novel and highly effective targeted adversarial attack for geolocalization. RTA conceptualizes the adversarial process as finding an optimal distractor journey to a specific, attacker-chosen location. It employs a beam search algorithm to iteratively construct a sequence of incorrect geographic locations that form a path to the target. At each step, the attack generates subtle perturbations to the query image, guiding the geolocalization model toward the next location in this deceptive path. We show that our method is also strong in black-box settings, obtaining highly transferable attacks with less perceptible image artifacts.

---


### 148. [Embodied Operators and Benchmarking: Toward Reusable and Deployable Embodied Intelligence Systems](https://arxiv.org/abs/2607.03283)

**<font color=#1a73e8>作者：</font>** Junwu Xiong, Jiaxuan Gao, Wei Chai 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied intelligence systems require not only end-to-end policy models, but also reusable functional modules that transform multimodal observations, robot states, human demonstrations, and task contexts into structured representations, decisions, trajectories, control references, and system services. This work defines these modules as embodied operators and studies them as independent yet composable units in embodied intelligence pipelines. We clarify their definition boundary, emphasizing task semantics, standardized input-output contracts, deployability, reusability, and multi-layer optimizability. We further construct a taxonomy covering five categories: detection and segmentation, spatial localization and 3D understanding, hand motion recovery, embodied foundation models and task-decision operators, and planning, control, and system support operators. For each category, we summarize representative functions, technical paradigms, application roles, and practical limitations. Beyond taxonomy, we propose a multi-dimensional benchmark framework that evaluates embodied operators in terms of correctness, end-to-end efficiency, resource usage, temporal stability, portability, interface compatibility, deployment reliability, and downstream task utility. We also discuss workflow-level operator acceleration and open challenges in operator composition, data standardization, world models, VLA safety, edge deployment, and real-world application value. Overall, this work argues that embodied operators should be optimized and evaluated as holistic deployable components, providing a foundation for reusable, scalable, and verifiable embodied intelligence systems.

---


### 149. [Security Analysis for SCONE Logic Locking](https://arxiv.org/abs/2607.03288)

**<font color=#1a73e8>作者：</font>** Akashdeep Saha, Mohammed Nabeel, Johann Knechtel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> SCONE [DAC'25] expands a logic locking interface with additional encoded inputs derived from the original primary inputs, and admits two realizations: a \textit{with-ES} variant, where the critical encoding stage is implemented in hardware, and a \textit{without-ES} variant, where the locked design directly exposes an encoded interface of width $n+m$. We show that both realizations are vulnerable, but for different reasons. For the without-ES variant, we prove that, when the added encoded inputs are deterministic linear functions of the original inputs, the valid encoded-input space remains $n$-dimensional despite the nominal expansion to $n+m$ inputs. Hence, the widened interface does not yield $m$ additional or independent brute-force dimensions. For the with-ES variant, we present a polynomial-time white-box attack that exactly recovers the added-input count and the implemented linear encoding relation from the locked netlist, achieving 100\% recovery over all evaluated instances. We also develop a black-box procedure that certifies the same dimensionality collapse from valid encoded-input samples without reconstructing the hidden encoder. Experiments on ISCAS-85 and ITC-99 benchmarks validate both results, and we further demonstrate exact white-box recovery on an ARM Cortex-M0 RTL benchmark. Finally, we propose a lightweight non-linear mitigation and show that it does not exhibit the vulnerabilities identified in this paper under all representative attack sets considered in SCONE.

---


### 150. [Regulating AI: Where U.S. State Policy and HCI (Mis)align](https://arxiv.org/abs/2607.03292)

**<font color=#1a73e8>作者：</font>** Nino Migineishvili, Alice Gao, Adinawa Adjagbodjou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence (AI) technologies are increasingly adopted into everyday life, with most investment and development concentrated in the U.S. In response to rapid AI integration and scant federal guidelines, U.S. states have formed AI committees charged with studying AI-related societal trade-offs. We analyzed the 18 existing state-level AI committee reports to understand how policymakers discuss AI-related benefits and risks. We then compared the risks surfaced by policymakers to an established taxonomy of AI risks aggregated from literature and examined how policymakers' concerns align, or misalign, from those of HCI scholars. These insights provide important mileposts for shaping currently ongoing policy initiatives and future research. Our findings reveal important gaps: while committees invoke responsible AI, their framings often omit broader socio-technical concerns emphasized in HCI. We discuss opportunities for HCI to support socio-technical perspectives, employ participatory design, and close the gap between research and policy.

---


> [!TIP]
> 当前位于：**101-150**（第 3/12 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-550](./part-11.md) | [551-571](./part-12.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
