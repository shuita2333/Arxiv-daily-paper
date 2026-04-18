# 📦 其他研究 | 2026年04月18日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-234](./part-05.md)

---

### 101. [Physically-Induced Atmospheric Adversarial Perturbations: Enhancing Transferability and Robustness in Remote Sensing Image Classification](https://arxiv.org/abs/2604.14643)

**<font color=#1a73e8>作者：</font>** Weiwei Zhuang, Wangze Xie, Qi Zhang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adversarial attacks pose a severe threat to the reliability of deep learning models in remote sensing (RS) image classification. Most existing methods rely on direct pixel-wise perturbations, failing to exploit the inherent atmospheric characteristics of RS imagery or survive real-world image degradations. In this paper, we propose FogFool, a physically plausible adversarial framework that generates fog-based perturbations by iteratively optimizing atmospheric patterns based on Perlin noise. By modeling fog formations with natural, irregular structures, FogFool generates adversarial examples that are not only visually consistent with authentic RS scenes but also deceptive. By leveraging the spatial coherence and mid-to-low-frequency nature of atmospheric phenomena, FogFool embeds adversarial information into structural features shared across diverse architectures. Extensive experiments on two benchmark RS datasets demonstrate that FogFool achieves superior performance: not only does it exceed in white-box settings, but also exhibits exceptional black-box transferability (reaching 83.74% TASR) and robustness against common preprocessing-based defenses such as JPEG compression and filtering. Detailed analyses, including confusion matrices and Class Activation Map (CAM) visualizations, reveal that our atmospheric-driven perturbations induce a universal shift in model attention. These results indicate that FogFool represents a practical, stealthy, and highly persistent threat to RS classification systems, providing a robust benchmark for evaluating model reliability in complex environments.

---


### 102. [Chaotic CNN for Limited Data Image Classification](https://arxiv.org/abs/2604.14645)

**<font color=#1a73e8>作者：</font>** Anusree M, Akhila Henry, Pramod P Nair  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNNs) often exhibit poor generalisation in limited training data scenarios due to overfitting and insufficient feature diversity. In this work, a simple and effective chaos-based feature transformation is proposed to enhance CNN performance without increasing model complexity. The method applies nonlinear transformations using logistic, skew tent, and sine maps to normalised feature vectors before the classification layer, thereby reshaping the feature space and improving class separability. The approach is evaluated on greyscale datasets (MNIST and Fashion-MNIST) and an RGB dataset (CIFAR-10) using CNN architectures of varying depth under limited data conditions. The results show consistent improvement over the standalone (SA) CNN across all datasets. Notably, a maximum performance gain of 5.43% is achieved on MNIST using the skew tent map with a 3-layer CNN at 40 samples per class. A higher gain of 9.11% is observed on Fashion-MNIST using the sine map with a 3-layer CNN at 50 samples per class. Additionally, a strong gain of 7.47% is obtained on CIFAR-10 using the skew tent map at 200 samples per class. The consistent improvements across different chaotic maps indicate that the performance gain is driven by the shared nonlinear and dynamical properties of chaotic systems. The proposed method is computationally efficient, requires no additional trainable parameters, and can be easily integrated into existing CNN architectures, making it a practical solution for data-scarce image classification tasks.

---


### 103. [Seen-to-Scene: Keep the Seen, Generate the Unseen for Video Outpainting](https://arxiv.org/abs/2604.14648)

**<font color=#1a73e8>作者：</font>** Inseok Jeon, Minhyeok Lee, Seunghoon Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video outpainting aims to expand the visible content of a video beyond the original frame boundaries while preserving spatial fidelity and temporal coherence across frames. Existing methods primarily rely on large-scale generative models, such as diffusion models. However, generationbased approaches suffer from implicit temporal modeling and limited spatial context. These limitations lead to intraframe and inter-frame inconsistencies, which become particularly pronounced in dynamic scenes and large outpainting scenarios. To overcome these challenges, we propose Seen-to-Scene, a novel framework that unifies propagationbased and generation-based paradigms for video outpainting. Specifically, Seen-to-Scene leverages flow-based propagation with a flow completion network pre-trained for video inpainting, which is fine-tuned in an end-to-end manner to bridge the domain gap and reconstruct coherent motion fields. To further improve the efficiency and reliability of propagation, we introduce a reference-guided latent propagation that effectively propagates source content across frames. Extensive experiments demonstrate that our method achieves superior temporal coherence and visual realism with efficient inference, surpassing even prior state-of-the-art methods that require input-specific adaptation.

---


### 104. [AgentGA: Evolving Code Solutions in Agent-Seed Space](https://arxiv.org/abs/2604.14655)

**<font color=#1a73e8>作者：</font>** David Y.Y. Tan, Kellie Chin, Jingxian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present AgentGA, a framework that evolves autonomous code-generation runs by optimizing the agent seed: the task prompt plus optional parent archives that initialize a fresh workspace. The outer loop searches over these reusable starting conditions rather than editing code directly. Each generation launches a fresh autonomous run from a reset workspace, while selected parent archives provide inherited artifacts that descendants can inspect and reuse. AgentGA couples a population-level genetic algorithm with long-horizon agents; selection uses deterministic 1:1 elite tournaments and operator allocation is adapted online with a modified Hedge controller. We instantiate the approach for tabular AutoML on the 16-competition Weco-Kaggle Lite benchmark. On the 10 benchmark runs reported here, AgentGA averages 74.52% Exceeds % of Human versus 54.15% for AIDE. Across 1135 parent-child comparisons, descendants given parent archives outperform runs started from scratch, indicating that inherited artifacts improve later autonomous runs. These findings support agent-seed optimization as a practical design point for autonomous code-search systems.

---


### 105. [EdgeDetect: Importance-Aware Gradient Compression with Homomorphic Aggregation for Federated Intrusion Detection](https://arxiv.org/abs/2604.14663)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) enables collaborative intrusion detection without raw data exchange, but conventional FL incurs high communication overhead from full-precision gradient transmission and remains vulnerable to gradient inference attacks. This paper presents EdgeDetect, a communication-efficient and privacy-aware federated IDS for bandwidth-constrained 6G-IoT environments. EdgeDetect introduces gradient smartification, a median-based statistical binarization that compresses local updates to $\{+1,-1\}$ representations, reducing uplink payload by $32\times$ while preserving convergence. We further integrate Paillier homomorphic encryption over binarized gradients, protecting against honest-but-curious servers without exposing individual updates. Experiments on CIC-IDS2017 (2.8M flows, 7 attack classes) demonstrate $98.0\%$ multi-class accuracy and $97.9\%$ macro F1-score, matching centralized baselines, while reducing per-round communication from $450$~MB to $14$~MB ($96.9\%$ reduction). Raspberry Pi-4 deployment confirms edge feasibility: $4.2$~MB memory, $0.8$~ms latency, and $12$~mJ per inference with $<0.5\%$ accuracy loss. Under $5\%$ poisoning attacks and severe imbalance, EdgeDetect maintains $87\%$ accuracy and $0.95$ minority class F1 ($p<0.001$), establishing a practical accuracy, communication, and privacy tradeoff for next-generation edge intrusion detection.

---


### 106. [Beyond Chat and Clicks: GUI Agents for In-Situ Assistance via Live Interface Transformation](https://arxiv.org/abs/2604.14668)

**<font color=#1a73e8>作者：</font>** Pan Hao, Rishi Selvakumaran, Jacob Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Complex visual interfaces are powerful yet have a steep learning curve, as users must navigate feature-rich visual interfaces while reasoning about domain-specific operations. Existing approaches either deliver assistance through a separate chat-based interaction, or require substantial application-specific engineering to build support natively into each interface. To address the gaps, we propose in-situ assistance: a mode of support delivered directly within any live web interface through lightweight, browser-level interventions on the Document Object Model (DOM), without rebuilding the application or modifying its underlying logic. We contribute a design space and a computational pipeline for DOM-mediated in-situ assistance, characterizing how GUI agents can insert, mutate, or recompose web elements to make the interface easier for users to understand, use, and navigate. We instantiate in-situ assistance in DOMSteer, a Chrome extension that interprets a user's help request and live interface context, grounds it to relevant UI elements, and executes reversible DOM manipulations directly on the live page to deliver assistance, including contextual tooltips, control highlighting, layout reorganization. Quantitative evaluations on two complex visual interfaces show that DOMSteer delivers reliable and efficient in-situ assistance. Use cases and a comparative user study with baseline ChatGPTAtlas demonstrate the usability and effectiveness of DOMSteer. Altogether, these findings point to a broader role for GUI agents: not just assisting from the sidelines, but actively reconfiguring live interfaces to support users in the moment.

---


### 107. [Zeroth-Order Optimization at the Edge of Stability](https://arxiv.org/abs/2604.14669)

**<font color=#1a73e8>作者：</font>** Minhak Song, Liang Zhang, Bingcong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zeroth-order (ZO) methods are widely used when gradients are unavailable or prohibitively expensive, including black-box learning and memory-efficient fine-tuning of large models, yet their optimization dynamics in deep learning remain underexplored. In this work, we provide an explicit step size condition that exactly captures the (mean-square) linear stability of a family of ZO methods based on the standard two-point estimator. Our characterization reveals a sharp contrast with first-order (FO) methods: whereas FO stability is governed solely by the largest Hessian eigenvalue, mean-square stability of ZO methods depends on the entire Hessian spectrum. Since computing the full Hessian spectrum is infeasible in practical neural network training, we further derive tractable stability bounds that depend only on the largest eigenvalue and the Hessian trace. Empirically, we find that full-batch ZO methods operate at the edge of stability: ZO-GD, ZO-GDM, and ZO-Adam consistently stabilize near the predicted stability boundary across a range of deep learning training problems. Our results highlight an implicit regularization effect specific to ZO methods, where large step sizes primarily regularize the Hessian trace, whereas in FO methods they regularize the top eigenvalue.

---


### 108. [DETR-ViP: Detection Transformer with Robust Discriminative Visual Prompts](https://arxiv.org/abs/2604.14684)

**<font color=#1a73e8>作者：</font>** Bo Qian, Dahu Shi, Xing Wei  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual prompted object detection enables interactive and flexible definition of target categories, thereby facilitating open-vocabulary detection. Since visual prompts are derived directly from image features, they often outperform text prompts in recognizing rare categories. Nevertheless, research on visual prompted detection has been largely overlooked, and it is typically treated as a byproduct of training text prompted detectors, which hinders its development. To fully unlock the potential of visual-prompted detection, we investigate the reasons why its performance is suboptimal and reveal that the underlying issue lies in the absence of global discriminability in visual prompts. Motivated by these observations, we propose DETR-ViP, a robust object detection framework that yields class-distinguishable visual prompts. On top of basic image-text contrastive learning, DETR-ViP incorporates global prompt integration and visual-textual prompt relation distillation to learn more discriminative prompt representations. In addition, DETR-ViP employs a selective fusion strategy that ensures stable and robust detection. Extensive experiments on COCO, LVIS, ODinW, and Roboflow100 demonstrate that DETR-ViP achieves substantially higher performance in visual prompt detection compared to other state-of-the-art counterparts. A series of ablation studies and analyses further validate the effectiveness of the proposed improvements and shed light on the underlying reasons for the enhanced detection capability of visual prompts.

---


### 109. [Beyond Nodes vs. Edges: A Multi-View Fusion Framework for Provenance-Based Intrusion Detection](https://arxiv.org/abs/2604.14685)

**<font color=#1a73e8>作者：</font>** Fan Yang, Binyan Xu, Di Tang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Provenance-based intrusion detection has emerged as a promising approach for analyzing complex attack behaviors through system-level provenance graphs. However, existing defense methods face an inherent granularity limitation. Node-centric detectors, which evaluate anomalies using entities' attributes and local structural patterns, may misclassify benign behavioral changes or configuration modifications as suspicious. In contrast, edge-centric detectors, which focus more on interactions, may lack sufficient contextual awareness of the involved entities, leading to missed detections when compromised entities perform seemingly ordinary operations. These analytical biases highlight a persistent gap between node-centric and edge-centric analyses. To mitigate this gap, we present PROVFUSION, a multi-view detection framework that integrates anomaly signals from three distinct views (i.e., attribute, structure, and causality). The framework fuses heterogeneous anomaly signals through lightweight fusion schemes and determines the final anomaly decisions through a voting-based integration process, providing a more consistent and context-aware assessment of system behavior. This design enables PROVFUSION to capture both entity level deviations and interaction-level anomalies within a consistent analytic pipeline. Experiments on nine widely used benchmark datasets demonstrate that PROVFUSION achieves higher detection accuracy and lower false-positive rates than single node- and edge-centric baselines, maintaining stable performance across scenarios. Overall, the results suggest that our multi-view anomaly fusion together with voting-based decision aggregation offers a practical and effective direction for advancing provenance-based intrusion detection.

---


### 110. [Chain-of-Glimpse: Search-Guided Progressive Object-Grounded Reasoning for Video Understanding](https://arxiv.org/abs/2604.14692)

**<font color=#1a73e8>作者：</font>** Zhixuan Wu, Quanxing Zha, Teng Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding requires identifying and reasoning over semantically discriminative visual objects across frames, yet existing object-agnostic solutions struggle to effectively handle substantial object variations over time. To address this, we introduce Chain-of-Glimpse, a search-guided progressive object-grounded reasoning framework that explicitly anchors each reasoning step to specific visual evidence regions, enabling compositional and multi-step decision-making. Formally, Chain-of-Glimpse formulates video reasoning as a step-by-step process that incrementally builds spatially grounded traces around task-relevant visual objects, thereby mitigating over-reliance on saliency-driven cues. Specifically, Chain-of-Glimpse features a search-guided controller, optimized via reinforcement learning with a format reward that significantly incentivizes grounding capability, to iteratively ground visual evidence regions and form reliable reasoning trajectories, yielding accurate and interpretable multi-step decisions. Extensive evaluations on both in domain NExTQA and out-of-domain Video-Holmes, CG-Bench Reasoning, and VRBench benchmarks demonstrate consistent performance gains, robustness and generalization of Chain-of-Glimpse across diverse video reasoning tasks.

---


### 111. [Mean Flow Policy Optimization](https://arxiv.org/abs/2604.14698)

**<font color=#1a73e8>作者：</font>** Xiaoyi Dong, Xi Sheryl Zhang, Jian Cheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion models have recently emerged as expressive policy representations for online reinforcement learning (RL). However, their iterative generative processes introduce substantial training and inference overhead. To overcome this limitation, we propose to represent policies using MeanFlow models, a class of few-step flow-based generative models, to improve training and inference efficiency over diffusion-based RL approaches. To promote exploration, we optimize MeanFlow policies under the maximum entropy RL framework via soft policy iteration, and address two key challenges specific to MeanFlow policies: action likelihood evaluation and soft policy improvement. Experiments on MuJoCo and DeepMind Control Suite benchmarks demonstrate that our method, Mean Flow Policy Optimization (MFPO), achieves performance comparable to or exceeding current diffusion-based baselines while considerably reducing training and inference time. Our code is available at this https URL.

---


### 112. [Gating Enables Curvature: A Geometric Expressivity Gap in Attention](https://arxiv.org/abs/2604.14702)

**<font color=#1a73e8>作者：</font>** Satwik Bathula, Anand A. Joshi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multiplicative gating is widely used in neural architectures and has recently been applied to attention layers to improve performance and training stability in large language models. Despite the success of gated attention, the mathematical implications of gated attention mechanisms remain poorly understood. We study attention through the geometry of its representations by modeling outputs as mean parameters of Gaussian distributions and analyzing the induced Fisher--Rao geometry. We show that ungated attention operator is restricted to intrinsically flat statistical manifolds due to its affine structure, while multiplicative gating enables non-flat geometries, including positively curved manifolds that are unattainable in the ungated setting. These results establish a geometric expressivity gap between ungated and gated attention. Empirically, we show that gated models exhibit higher representation curvature and improved performance on tasks requiring nonlinear decision boundaries whereas they provide no consistent advantage on tasks with linear decision boundaries. Furthermore, we identify a structured regime in which curvature accumulates under composition, yielding a systematic depth amplification effect.

---


### 113. [The Courtroom Trial of Pixels: Robust Image Manipulation Localization via Adversarial Evidence and Reinforcement Learning Judgment](https://arxiv.org/abs/2604.14703)

**<font color=#1a73e8>作者：</font>** Songlin Li, Zhiqing Guo, Dan Ma 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Although some existing image manipulation localization (IML) methods incorporate authenticity-related supervision, this information is typically utilized merely as an auxiliary training signal to enhance the model's sensitivity to manipulation artifacts, rather than being explicitly modeled as localization evidence opposing the manipulated regions. Consequently, when manipulation traces are subtle or degraded by post-processing and noise, these methods struggle to explicitly compare manipulated and authentic evidence, resulting in unreliable predictions in ambiguous areas. To address these issues, we propose a courtroom-style adjudication framework that regards IML task as the confrontation of evidence followed by judgment. The framework comprises a prosecution stream, a defense stream, and a judge model. We first build a dual-hypothesis segmentation architecture on a shared multi-scale encoder, in which the prosecution stream asserts manipulation and the defense stream asserts authenticity. Guided by edge priors, it produces evidence for manipulated and authentic regions through cascaded multi-level fusion, bidirectional disagreement suppression, and dynamic debate refinement. We further develop a reinforcement learning judge model that performs strategic re-inference and refinement on uncertain regions, yielding a manipulated-region mask. The judge model is trained with advantage-based rewards and a soft-IoU objective, and reliability is calibrated via entropy and cross-hypothesis consistency. Experimental results show that our model achieves superior average performance compared with SOTA IML methods.

---


### 114. [SynHAT: A Two-stage Coarse-to-Fine Diffusion Framework for Synthesizing Human Activity Traces](https://arxiv.org/abs/2604.14705)

**<font color=#1a73e8>作者：</font>** Rongchao Xu, Lin Jiang, Dahai Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Human activity traces (HATs) are critical for many applications, including human mobility modeling and point-of-interest (POI) recommendation. However, growing privacy concerns have severely limited access to authentic large-scale HAT datasets. Recent advances in generative AI provide new opportunities to synthesize realistic and privacy-preserving HATs for such applications. Yet two major challenges remain: (i) HATs are highly irregular and dynamic, with long and varying time intervals, making it difficult to capture their complex spatio-temporal dependencies and underlying distributions; and (ii) generative models are often computationally expensive, making long-term, fine-grained HAT synthesis inefficient. To address these challenges, we propose SynHAT, a computationally efficient coarse-to-fine HAT synthesis framework built on a novel spatio-temporal denoising diffusion model. In Stage 1, we develop Coarse-HADiff, which models the overall spatio-temporal dependencies of coarse-grained latent spatio-temporal traces. It incorporates a novel Latent Spatio-Temporal U-Net with dual Drift-Jitter branches to jointly model smooth spatial transitions and temporal variations during denoising. In Stage 2, we introduce a three-step pipeline consisting of Behavior Pattern Extraction, Fine-HADiff, which shares the same architecture as Coarse-HADiff, and Semantic Alignment to generate fine-grained latent spatio-temporal traces from the Stage 1 outputs. We extensively evaluate SynHAT in terms of data fidelity, utility, privacy, robustness, and scalability. Experiments on real-world HAT datasets from four cities across three countries show that SynHAT substantially outperforms state-of-the-art baselines, achieving 52% and 33% improvements on spatial and temporal metrics, respectively.

---


### 115. [NG-GS: NeRF-Guided 3D Gaussian Splatting Segmentation](https://arxiv.org/abs/2604.14706)

**<font color=#1a73e8>作者：</font>** Yi He, Tao Wang, Yi Jin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in 3D Gaussian Splatting (3DGS) have enabled highly efficient and photorealistic novel view synthesis. However, segmenting objects accurately in 3DGS remains challenging due to the discrete nature of Gaussian representations, which often leads to aliasing and artifacts at object boundaries. In this paper, we introduce NG-GS, a novel framework for high-quality object segmentation in 3DGS that explicitly addresses boundary discretization. Our approach begins by automatically identifying ambiguous Gaussians at object boundaries using mask variance analysis. We then apply radial basis function (RBF) interpolation to construct a spatially continuous feature field, enhanced by multi-resolution hash encoding for efficient multi-scale representation. A joint optimization strategy aligns 3DGS with a lightweight NeRF module through alignment and spatial continuity losses, ensuring smooth and consistent segmentation boundaries. Extensive experiments on NVOS, LERF-OVS, and ScanNet benchmarks demonstrate that our method achieves state-of-the-art performance, with significant gains in boundary mIoU. Code is available at this https URL.

---


### 116. [MS-SSE-Net: A Multi-Scale Spatial Squeeze-and-Excitation Network for Structural Damage Detection in Civil and Geotechnical Engineering](https://arxiv.org/abs/2604.14711)

**<font color=#1a73e8>作者：</font>** Saif ur Rehman Khan, Imad Ahmed Waqar, Arooj Zaib 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Structural damage detection is essential for maintaining the safety and reliability of civil infrastructure. However, accurately identifying different types of structural damage from images remains challenging due to variations in damage patterns and environmental conditions. To address these challenges, this paper proposes MS-SSE-Net, a novel deep learning (DL) framework for structural damage classification. The proposed model is built upon the DenseNet201 backbone and integrates novel multi-scale feature extraction with channel and spatial attention mechanisms (MS-SSE-Net). Specifically, parallel depthwise convolutions capture both local and contextual features, while squeeze-and-excitation style channel attention and spatial attention emphasize informative regions and suppress irrelevant noise. The refined features are then processed through global average pooling and a fully connected classification layer to generate the final predictions. Experiments are conducted on the StructDamage dataset containing multiple structural damage categories. The proposed MS-SSE-Net demonstrates superior performance compared with the baseline DenseNet201 and other comparative approaches. Specifically, the proposed method achieves 99.31% precision, 99.25% recall, 99.27% F1-score, and 99.26% accuracy, outperforming the baseline model which achieved 98.62% precision, 98.53% recall, 98.58% F1-score, and 98.53% accuracy.

---


### 117. [Layered Mutability: Continuity and Governance in Persistent Self-Modifying Agents](https://arxiv.org/abs/2604.14717)

**<font color=#1a73e8>作者：</font>** Krti Tallam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent language-model agents increasingly combine tool use, tiered memory, reflective prompting, and runtime adaptation. In such systems, behavior is shaped not only by current prompts but by mutable internal conditions that influence future action. This paper introduces layered mutability, a framework for reasoning about that process across five layers: pretraining, post-training alignment, self-narrative, memory, and weight-level adaptation. The central claim is that governance difficulty rises when mutation is rapid, downstream coupling is strong, reversibility is weak, and observability is low, creating a systematic mismatch between the layers that most affect behavior and the layers humans can most easily inspect. I formalize this intuition with simple drift, governance-load, and hysteresis quantities, connect the framework to recent work on temporal identity in language-model agents, and report a preliminary ratchet experiment in which reverting an agent's visible self-description after memory accumulation fails to restore baseline behavior. In that experiment, the estimated identity hysteresis ratio is 0.68. The main implication is that the salient failure mode for persistent self-modifying agents is not abrupt misalignment but compositional drift: locally reasonable updates that accumulate into a behavioral trajectory that was never explicitly authorized.

---


### 118. [The Agentification of Scientific Research: A Physicist's Perspective](https://arxiv.org/abs/2604.14718)

**<font color=#1a73e8>作者：</font>** Xiao-Liang Qi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This article argues that the most important significance of the AI revolution, especially the rise of large language models, lies not simply in automation, but in a fundamental change in how complex information and human know-how are carried, replicated, and shared. From this perspective, AI for Science is especially important because it may transform not only the efficiency of research, but also the structure of scientific collaboration, discovery, publishing, and evaluation. The article outlines a gradual path from AI as a research tool to AI as a scientific collaborator, and discusses how AI is likely to fundamentally reshape scientific publication. It also argues that continuous learning and diversity of ideas are essential if AI is to play a meaningful role in original scientific discovery.

---


### 119. [Data Synthesis Improves 3D Myotube Instance Segmentation](https://arxiv.org/abs/2604.14720)

**<font color=#1a73e8>作者：</font>** David Exler, Nils Friederich, Martin Krüger 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Myotubes are multinucleated muscle fibers serving as key model systems for studying muscle physiology, disease mechanisms, and drug responses. Mechanistic studies and drug screening thereby rely on quantitative morphological readouts such as diameter, length, and branching degree, which in turn require precise three-dimensional instance segmentation. Yet established pretrained biomedical segmentation models fail to generalize to this domain due to the absence of large annotated myotube datasets. We introduce a geometry-driven synthesis pipeline that models individual myotubes via polynomial centerlines, locally varying radii, branching structures, and ellipsoidal end caps derived from real microscopy observations. Synthetic volumes are rendered with realistic noise, optical artifacts, and CycleGAN-based Domain Adaptation (DA). A compact 3D U-Net with self-supervised encoder pretraining, trained exclusively on synthetic data, achieves a mean IPQ of 0.22 on real data, significantly outperforming three established zero-shot segmentation models, demonstrating that biophysics-driven synthesis enables effective instance segmentation in annotation-scarce biomedical domains.

---


### 120. [HAMSA: Scanning-Free Vision State Space Models via SpectralPulseNet](https://arxiv.org/abs/2604.14724)

**<font color=#1a73e8>作者：</font>** Badri N. Patro, Vijay S. Agneeswaran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision State Space Models (SSMs) like Vim, VMamba, and SiMBA rely on complex scanning strategies to adapt sequential SSMs to process 2D images, introducing computational overhead and architectural complexity. We propose HAMSA, a scanning-free SSM operating directly in the spectral domain. HAMSA introduces three key innovations: (1) simplified kernel parameterization-a single Gaussian-initialized complex kernel replacing traditional (A, B, C) matrices, eliminating discretization instabilities; (2) SpectralPulseNet (SPN)-an input-dependent frequency gating mechanism enabling adaptive spectral modulation; and (3) Spectral Adaptive Gating Unit (SAGU)-magnitude-based gating for stable gradient flow in the frequency domain. By leveraging FFT-based convolution, HAMSA eliminates sequential scanning while achieving O(L log L) complexity with superior simplicity and efficiency. On ImageNet-1K, HAMSA reaches 85.7% top-1 accuracy (state-of-the-art among SSMs), with 2.2 X faster inference than transformers (4.2ms vs 9.2ms for DeiT-S) and 1.4-1.9X speedup over scanning-based SSMs, while using less memory (2.1GB vs 3.2-4.5GB) and energy (12.5J vs 18-25J). HAMSA demonstrates strong generalization across transfer learning and dense prediction tasks.

---


### 121. [Catching Every Ripple: Enhanced Anomaly Awareness via Dynamic Concept Adaptation](https://arxiv.org/abs/2604.14726)

**<font color=#1a73e8>作者：</font>** Jiaqi Zhu, Shaofeng Cai, Jie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Online anomaly detection (OAD) plays a pivotal role in real-time analytics and decision-making for evolving data streams. However, existing methods often rely on costly retraining and rigid decision boundaries, limiting their ability to adapt both effectively and efficiently to concept drift in dynamic environments. To address these challenges, we propose DyMETER, a dynamic concept adaptation framework for OAD that unifies on-the-fly parameter shifting and dynamic thresholding within a single online paradigm. DyMETER first learns a static detector on historical data to capture recurring central concepts, and then transitions to a dynamic mode to adapt to new concepts as drift occurs. Specifically, DyMETER employs a novel dynamic concept adaptation mechanism that leverages a hypernetwork to generate instance-aware parameter shifts for the static detector, thereby enabling efficient and effective adaptation without retraining or fine-tuning. To achieve robust and interpretable adaptation, DyMETER introduces a lightweight evolution controller to estimate instance-level concept uncertainty for adaptive updates. Further, DyMETER employs a dynamic threshold optimization module to adaptively recalibrates the decision boundary by maintaining a candidate window of uncertain samples, which ensures continuous alignment with evolving concepts. Extensive experiments demonstrate that DyMETER significantly outperforms existing OAD approaches across a wide spectrum of application scenarios.

---


### 122. [Expressivity of Transformers: A Tropical Geometry Perspective](https://arxiv.org/abs/2604.14727)

**<font color=#1a73e8>作者：</font>** Ye Su, Yong Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To quantify the geometric expressivity of transformers, we introduce a tropical geometry framework to characterize their exact spatial partitioning capabilities. By modeling self-attention as a vector-valued tropical rational map, we prove it evaluates exactly to a Power Voronoi Diagram in the zero-temperature limit. Building on this equivalence, we establish a combinatorial rationale for Multi-Head Self-Attention (MHSA): via the Minkowski sum of Newton polytopes, multi-head aggregation expands the polyhedral complexity to $\mathcal{O}(N^H)$, overcoming the $\mathcal{O}(N)$ bottleneck of single heads. Extending this to deep architectures, we derive the first tight asymptotic bounds on the number of linear regions in transformers ($\Theta(N^{d_{\text{model}}L})$), demonstrating a combinatorial explosion driven intrinsically by sequence length $N$, ambient embedding dimension $d_{\text{model}}$, and network depth $L$. Importantly, we guarantee that this idealized polyhedral skeleton is geometrically stable: finite-temperature soft attention preserves these topological partitions via exponentially tight differential approximation bounds.

---


### 123. [Find the Differences: Differential Morphing Attack Detection vs Face Recognition](https://arxiv.org/abs/2604.14734)

**<font color=#1a73e8>作者：</font>** Una M. Kelly, Luuk J. Spreeuwers, Raymond N.J. Veldhuis  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Morphing is a challenge to face recognition (FR) for which several morphing attack detection solutions have been proposed. We argue that face recognition and differential morphing attack detection (D-MAD) in principle perform very similar tasks, which we support by comparing an FR system with two existing D-MAD approaches. We also show that currently used decision thresholds inherently lead to FR systems being vulnerable to morphing attacks and that this explains the tradeoff between performance on normal images and vulnerability to morphing attacks. We propose using FR systems that are already in place for morphing detection and introduce a new evaluation threshold that guarantees an upper limit to the vulnerability to morphing attacks - even of unknown types.

---


### 124. [Personalized and Context-Aware Transformer Models for Predicting Post-Intervention Physiological Responses from Wearable Sensor Data](https://arxiv.org/abs/2604.14738)

**<font color=#1a73e8>作者：</font>** Esther Brown, Victoria Dean, Finale Doshi-Velez  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Consumer wearables enable continuous measurement of physiological data related to stress and recovery, but turning these streams into actionable, personalized stress-management recommendations remains a challenge. In practice, users often do not know how a given intervention, defined as an activity intended to reduce stress, will affect heart rate (HR), heart rate variability (HRV), or inter-beat intervals (BBI) over the next 15 to 120 minutes. We present a framework that predicts post-intervention trajectories and the direction of change for these physiological indicators across time windows. Our methodology combines a Transformer model for multi-horizon trajectories of percent change relative to a pre-intervention baseline, direction-of-change calls (positive, negative, or neutral) at each horizon, and an empirical study using wearable sensor data overlaid with user-tagged events and interventions. This proof of concept shows that personalized post-intervention prediction is feasible. We encourage future integration into stress-management tools for personalized intervention recommendations tailored to each person's day following further validation in larger studies and, where applicable, appropriate regulatory review.

---


### 125. [Efficient closed-form approaches for pose estimation using Sylvester forms](https://arxiv.org/abs/2604.14747)

**<font color=#1a73e8>作者：</font>** Jana Vráblíková, Ezio Malis, Laurent Busé  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Solving non-linear least-squares problem for pose estimation (rotation and translation) is often a time consuming yet fundamental problem in several real-time computer vision applications. With an adequate rotation parametrization, the optimization problem can be reduced to the solution of a~system of polynomial equations and solved in closed form. Recent advances in efficient closed form solvers utilizing resultant matrices have shown a promising research direction to decrease the computation time while preserving the estimation accuracy. In this paper, we propose a new class of resultant-based solvers that exploit Sylvester forms to further reduce the complexity of the resolution. We demonstrate that our proposed methods are numerically as accurate as the state-of-the-art solvers, and outperform them in terms of computational time. We show that this approach can be applied for pose estimation in two different types of problems: estimating a pose from 3D to 3D correspondences, and estimating a pose from 3D points to 2D points correspondences.

---


### 126. [Which bird does not have wings: Negative-constrained KGQA with Schema-guided Semantic Matching and Self-directed Refinement](https://arxiv.org/abs/2604.14749)

**<font color=#1a73e8>作者：</font>** Midan Shim, Seokju Hwang, Kaehyun Um 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models still struggle with faithfulness and hallucinations despite their remarkable reasoning abilities. In Knowledge Graph Question Answering (KGQA), semantic parsing-based approaches address the limitations by understanding constraints in a user's question and converting them into a logical form to execute on a knowledge graph. However, existing KGQA benchmarks and methods are biased toward positive and calculation constraints. Negative constraints are neglected, although they frequently appear in real-world questions. In this paper, we introduce a new task, NEgative-conSTrained (NEST) KGQA, where each question contains at least one negative constraint, and a corresponding dataset, NestKGQA. We also design PyLF, a Python-formatted logical form, since existing logical forms are hardly suitable to express negation clearly while maintaining readability. Furthermore, NEST questions naturally contain multiple constraints. To mitigate their semantic complexity, we present a novel framework named CUCKOO, specialized to multiple-constrained questions and ensuring semantic executability. CUCKOO first generates a constraint-aware logical form draft and performs schema-guided semantic matching. It then selectively applies self-directed refinement only when executing improper logical forms yields an empty result, reducing cost while improving robustness. Experimental results demonstrate that CUCKOO consistently outperforms baselines on both conventional KGQA and NEST-KGQA benchmarks under few-shot settings.

---


### 127. [ASGNet: Adaptive Spectrum Guidance Network for Automatic Polyp Segmentation](https://arxiv.org/abs/2604.14755)

**<font color=#1a73e8>作者：</font>** Yanguang Sun, Hengmin Zhang, Jianjun Qian 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Early identification and removal of polyps can reduce the risk of developing colorectal cancer. However, the diverse morphologies, complex backgrounds and often concealed nature of polyps make polyp segmentation in colonoscopy images highly challenging. Despite the promising performance of existing deep learning-based polyp segmentation methods, their perceptual capabilities remain biased toward local regions, mainly because of the strong spatial correlations between neighboring pixels in the spatial domain. This limitation makes it difficult to capture the complete polyp structures, ultimately leading to sub-optimal segmentation results. In this paper, we propose a novel adaptive spectrum guidance network, called ASGNet, which addresses the limitations of spatial perception by integrating spectral features with global attributes. Specifically, we first design a spectrum-guided non-local perception module that jointly aggregates local and global information, therefore enhancing the discriminability of polyp structures, and refining their boundaries. Moreover, we introduce a multi-source semantic extractor that integrates rich high-level semantic information to assist in the preliminary localization of polyps. Furthermore, we construct a dense cross-layer interaction decoder that effectively integrates diverse information from different layers and strengthens it to generate high-quality representations for accurate polyp segmentation. Extensive quantitative and qualitative results demonstrate the superiority of our ASGNet approach over 21 state-of-the-art methods across five widely-used polyp segmentation benchmarks. The code will be publicly available at: this https URL.

---


### 128. [OmniGCD: Abstracting Generalized Category Discovery for Modality Agnosticism](https://arxiv.org/abs/2604.14762)

**<font color=#1a73e8>作者：</font>** Jordan Shipard, Arnold Wiliem, Kien Nguyen Thanh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generalized Category Discovery (GCD) challenges methods to identify known and novel classes using partially labeled data, mirroring human category learning. Unlike prior GCD methods, which operate within a single modality and require dataset-specific fine-tuning, we propose a modality-agnostic GCD approach inspired by the human brain's abstract category formation. Our $\textbf{OmniGCD}$ leverages modality-specific encoders (e.g., vision, audio, text, remote sensing) to process inputs, followed by dimension reduction to construct a $\textbf{GCD latent space}$, which is transformed at test-time into a representation better suited for clustering using a novel synthetically trained Transformer-based model. To evaluate OmniGCD, we introduce a $\textbf{zero-shot GCD setting}$ where no dataset-specific fine-tuning is allowed, enabling modality-agnostic category discovery. $\textbf{Trained once on synthetic data}$, OmniGCD performs zero-shot GCD across 16 datasets spanning four modalities, improving classification accuracy for known and novel classes over baselines (average percentage point improvement of $\textbf{+6.2}$, $\textbf{+17.9}$, $\textbf{+1.5}$ and $\textbf{+12.7}$ for vision, text, audio and remote sensing). This highlights the importance of strong encoders while decoupling representation learning from category discovery. Improving modality-agnostic methods will propagate across modalities, enabling encoder development independent of GCD. Our work serves as a benchmark for future modality-agnostic GCD works, paving the way for scalable, human-inspired category discovery. All code is available $\href{this https URL}{here}$

---


### 129. [Wasserstein Formulation of Reinforcement Learning. An Optimal Transport Perspective on Policy Optimization](https://arxiv.org/abs/2604.14765)

**<font color=#1a73e8>作者：</font>** Mathias Dus  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a geometric framework for Reinforcement Learning (RL) that views policies as maps into the Wasserstein space of action probabilities. First, we define a Riemannian structure induced by stationary distributions, proving its existence in a general context. We then define the tangent space of policies and characterize the geodesics, specifically addressing the measurability of vector fields mapped from the state space to the tangent space of probability measures over the action space. Next, we formulate a general RL optimization problem and construct a gradient flow using Otto's calculus. We compute the gradient and the Hessian of the energy, providing a formal second-order analysis. Finally, we illustrate the method with numerical examples for low-dimensional problems, computing the gradient directly from our theoretical formalism. For high-dimensional problems, we parameterize the policy using a neural network and optimize it based on an ergodic approximation of the cost.

---


### 130. [CoPA: Benchmarking Personalized Question Answering with Data-Informed Cognitive Factors](https://arxiv.org/abs/2604.14773)

**<font color=#1a73e8>作者：</font>** Hang Su, Zequn Liu, Chen Hu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While LLMs have demonstrated remarkable potential in Question Answering (QA), evaluating personalization remains a critical bottleneck. Existing paradigms predominantly rely on lexical-level similarity or manual heuristics, often lacking sufficient data-driven validation. We address this by mining Community-Individual Preference Divergence (CIPD), where individual choices override consensus, to distill six key personalization factors as evaluative dimensions. Accordingly, we introduce CoPA, a benchmark with 1,985 user profiles for fine-grained, factor-level assessment. By quantifying the alignment between model outputs and user-specific cognitive preferences inferred from interaction patterns, CoPA provides a more comprehensive and discriminative standard for evaluating personalized QA than generic metrics. The code is available at this https URL.

---


### 131. [AIM: Asymmetric Information Masking for Visual Question Answering Continual Learning](https://arxiv.org/abs/2604.14779)

**<font color=#1a73e8>作者：</font>** Peifeng Zhang, Zice Qiu, Donghua Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In continual visual question answering (VQA), existing Continual Learning (CL) methods are mostly built for symmetric, unimodal architectures. However, modern Vision-Language Models (VLMs) violate this assumption, as their trainable components are inherently asymmetric. This structural mismatch renders VLMs highly prone to catastrophic forgetting when learning from continuous data streams. Specifically, the asymmetry causes standard global regularization to favor the massive language decoder during optimization, leaving the smaller but critical visual projection layers highly vulnerable to interference. Consequently, this localized degradation leads to a severe loss of compositional reasoning capabilities. To address this, we propose Asymmetric Information Masking (AIM), which balances stability and plasticity by applying targeted masks based on modality-specific sensitivity. Experiments on VQA v2 and GQA under continual VQA settings show that AIM achieves state-of-the-art performance in both Average Performance (AP) and Average Forgetting (AF), while better preserving generalization to novel skill-concept compositions.

---


### 132. [Integrating Object Detection, LiDAR-Enhanced Depth Estimation, and Segmentation Models for Railway Environments](https://arxiv.org/abs/2604.14781)

**<font color=#1a73e8>作者：</font>** Enrico Francesco Giannico, Federico Nesti, Gianluca D'Amico 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Obstacle detection in railway environments is crucial for ensuring safety. However, very few studies address the problem using a complete, modular, and flexible system that can both detect objects in the scene and estimate their distance from the vehicle. Most works focus solely on detection, others attempt to identify the track, and only a few estimate obstacle distances. Additionally, evaluating these systems is challenging due to the lack of ground truth data. In this paper, we propose a modular and flexible framework that identifies the rail track, detects potential obstacles, and estimates their distance by integrating three neural networks for object detection, track segmentation, and monocular depth estimation with LiDAR point clouds. To enable a reliable and quantitative evaluation, the proposed framework is assessed using a synthetic dataset (SynDRA), which provides accurate ground truth annotations, allowing for direct performance comparison with existing methods. The proposed system achieves a mean absolute error (MAE) as low as 0.63 meters by integrating monocular depth maps with LiDAR, enabling not only accurate distance estimates but also spatial perception of the scene.

---


### 133. [One-shot Compositional 3D Head Avatars with Deformable Hair](https://arxiv.org/abs/2604.14782)

**<font color=#1a73e8>作者：</font>** Yuan Sun, Xuan Wang, WeiLi Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose a compositional method for constructing a complete 3D head avatar from a single image. Prior one-shot holistic approaches frequently fail to produce realistic hair dynamics during animation, largely due to inadequate decoupling of hair from the facial region, resulting in entangled geometry and unnatural deformations. Our method explicitly decouples hair from the face, modeling these components using distinct deformation paradigms while integrating them into a unified rendering pipeline. Furthermore, by leveraging image-to-3D lifting techniques, we preserve fine-grained textures from the input image to the greatest extent possible, effectively mitigating the common issue of high-frequency information loss in generalized models. Specifically, given a frontal portrait image, we first perform hair removal to obtain a bald image. Both the original image and the bald image are then lifted to dense, detail-rich 3D Gaussian Splatting (3DGS) representations. For the bald 3DGS, we rig it to a FLAME mesh via non-rigid registration with a prior model, enabling natural deformation that follows the mesh triangles during animation. For the hair component, we employ semantic label supervision combined with a boundary-aware reassignment strategy to extract a clean and isolated set of hair Gaussians. To control hair deformation, we introduce a cage structure that supports Position-Based Dynamics (PBD) simulation, allowing realistic and physically plausible transformations of the hair Gaussian primitives under head motion, gravity, and inertial effects. Striking qualitative results, including dynamic animations under diverse head motions, gravity effects, and expressions, showcase substantially more realistic hair behavior alongside faithfully preserved facial details, outperforming state-of-the-art one-shot methods in perceptual realism.

---


### 134. [CogEvolution: A Human-like Generative Educational Agent to Simulate Student's Cognitive Evolution](https://arxiv.org/abs/2604.14786)

**<font color=#1a73e8>作者：</font>** Wei Zhang, Yihang Cheng, Zhirong Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative Agents, owing to their precise modeling and simulation capabilities of human behavior, have become a pivotal tool in the field of Artificial Intelligence in Education (AIEd) for uncovering complex cognitive processes of learners. However, existing educational agents predominantly rely on static personas to simulate student learning behaviors, neglecting the decisive role of deep cognitive capabilities in learning outcomes during practice interactions. Furthermore, they struggle to characterize the dynamic fluidity of knowledge internalization, transfer, and cognitive state transitions. To overcome this bottleneck, this paper proposes a human-like educational agent capable of simulating student cognitive evolution: CogEvolution. Specifically, we first construct a cognitive depth perceptron based on the Interactive, Constructive, Active, Passive (ICAP) taxonomy from cognitive psychology, achieving precise quantification of learner cognitive engagement. Subsequently, we propose a memory retrieval method based on Item Response Theory (IRT) to simulate the connection and assimilation of new and prior knowledge. Finally, we design a dynamic cognitive update mechanism based on evolutionary algorithms to simulate the real-time integration of student learning behaviors and cognitive evolution processes. Comprehensive evaluations demonstrate that CogEvolution not only significantly outperforms baseline models in behavioral fidelity and learning curve fitting but also uniquely reproduces plausible and robust cognitive evolutionary paths consistent with educational psychology expectations, providing a novel paradigm for constructing highly interpretable educational agents.

---


### 135. [Sequence Search: Automated Sequence Design using Neural Architecture Search](https://arxiv.org/abs/2604.14788)

**<font color=#1a73e8>作者：</font>** Rokgi Hong, Hongjun An, Sooyeon Ji 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Developing an MR sequence is challenging and remains largely constrained by human intuition. Recently, AI-driven approaches have been proposed; however, most require an initial sequence for parameter optimization or extensive training datasets, limiting their general applicability. In this study, we propose "Sequence Search," an automated sequence design framework based on neural architecture search. The method takes tissue properties, imaging parameters, and design objectives as inputs and generates pulse sequences satisfying the design objectives, without requiring prior knowledge of conventional sequence structures. Sequence Search iteratively generates candidate sequences through neural architecture search and optimizes them via a differentiable Bloch simulator and objective-specific loss functions using gradient-based learning. The framework successfully replicated conventional spin-echo, T2-weighted spin-echo, and inversion recovery sequences. Less intuitive solutions were also discovered, such as three-RF spin-echo-like sequences with reduced RF energy and refocusing phases deviating from the conventional Hahn-echo. This work establishes a generalizable framework for automated MR sequence design, highlighting the potential to explore configurations beyond conventional designs based on human intuition.

---


### 136. [A Comparative Study of CNN Optimization Methods for Edge AI: Exploring the Role of Early Exits](https://arxiv.org/abs/2604.14789)

**<font color=#1a73e8>作者：</font>** Nekane Fernandez, Ivan Valdes, Steven Van Vaerenbergh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deploying deep neural networks on edge devices requires balancing accuracy, latency, and resource constraints under realistic execution conditions. To fit models within these constraints, two broad strategies have emerged: static compression techniques such as pruning and quantization, which permanently reduce model size, and dynamic approaches such as early-exit mechanisms, which adapt computational cost at runtime. While both families are widely studied in isolation, they are rarely compared under identical conditions on physical hardware. This paper presents a unified deployment-oriented comparison of static compression and dynamic early-exit mechanisms, evaluated on real edge devices using ONNX based inference pipelines. Our results show that static and dynamic techniques offer fundamentally different trade-offs for edge deployment. While pruning and quantization deliver consistent memory footprint reduction, early-exit mechanisms enable input-adaptive computation savings that static methods cannot match. Their combination proves highly effective, simultaneously reducing inference latency and memory usage with minimal accuracy loss, expanding what is achievable at the edge.

---


### 137. [Diffusion Crossover: Defining Evolutionary Recombination in Diffusion Models via Noise Sequence Interpolation](https://arxiv.org/abs/2604.14790)

**<font color=#1a73e8>作者：</font>** Chisatao Kumada, Satoru Hiwa, Tomoyuki Hiroyasu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Interactive Evolutionary Computation (IEC) provides a powerful framework for optimizing subjective criteria such as human preferences and aesthetics, yet it suffers from a fundamental limitation: in high-dimensional generative representations, defining crossover in a semantically consistent manner is difficult, often leading to a mutation-dominated search. In this work, we explicitly define crossover in diffusion models. We propose Diffusion crossover, which formulates evolutionary recombination as step-wise interpolation of noise sequences in the reverse process of Denoising Diffusion Probabilistic Models (DDPMs). By applying spherical linear interpolation (Slerp) to the noise sequences associated with selected parent images, the proposed method generates offspring that inherit characteristics from both parents while preserving the geometric structure of the diffusion process. Furthermore, controlling the time-step range of interpolation enables a principled trade-off between diversity (exploration) and convergence (exploitation). Experimental results using PCA analysis and perceptual similarity metrics (LPIPS) demonstrate that Diffusion crossover produces perceptually smooth and semantically consistent transitions between parent images. Qualitative interactive evolution experiments further confirm that the proposed method effectively supports human-in-the-loop image exploration. These findings suggest a new perspective: diffusion models are not only powerful generators, but also structured evolutionary search spaces in which recombination can be explicitly defined and controlled.

---


### 138. [Evaluating Encodings for Bivariate Edges in Adjacency Matrices](https://arxiv.org/abs/2604.14791)

**<font color=#1a73e8>作者：</font>** Jorge Acosta-Hernández, Alexander Lex, Tingying He  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present the first empirical evaluation of techniques for encoding distributions of quantitative edge values within adjacency matrices. In many real-world networks, edges represent not a single value but a set of measurements. While adjacency matrices preserve structural clarity, their compact cells limit the simultaneous display of multiple values. To address this, we explore edge encodings that represent distributions by two values: a measure of central tendency (mean, median, mode) and a measure of dispersion (standard deviation, variance, IQR). We select four possible encodings for evaluation that prior work has suggested are suitable for the limited space available in matrices: a bivariate color palette, embedded bar charts, and two overlaid-mark designs mapping the primary attribute to color and the secondary attribute to area or angle. In a preregistered crowdsourced study with 156 participants, we assessed performance of these encodings across eight analytical tasks and collected readability and aesthetic ratings. Results reveal clear performance regimes: area-based overlaid marks and bar charts achieved the highest overall performance; angle-based marks show moderate but less stable performance,and bivariate color consistently underperforms these alternatives. These findings clarify how visual channels behave under strict constraints and delineate the strengths and limitations of key design choices for multivariate edge visualization.

---


### 139. [From Boundaries to Semantics: Prompt-Guided Multi-Task Learning for Petrographic Thin-section Segmentation](https://arxiv.org/abs/2604.14805)

**<font color=#1a73e8>作者：</font>** Yili Ren, Shiqi Wen, Li Hou 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grain-edge segmentation (GES) and lithology semantic segmentation (LSS) are two pivotal tasks for quantifying rock fabric and composition. However, these two tasks are often treated separately, and the segmentation quality is implausible albeit expensive, time-consuming, and expert-annotated datasets have been used. Recently, foundation models, especially the Segment Anything Model (SAM), have demonstrated impressive robustness for boundary alignment. However, directly adapting SAM to joint GES and LSS is nontrivial due to 1) severe domain gap induced by extinction-dependent color variations and ultra-fine grain boundaries, and 2) lacking novel modules for joint learning on multi-angle petrographic image stacks. In this paper, we propose Petro-SAM, a novel two-stage, multi-task framework that can achieve high-quality joint GES and LSS on petrographic images. Specifically, based on SAM, we introduce a Merge Block to integrate seven polarized views, effectively solving the extinction issue. Moreover, we introduce multi-scale feature fusion and color-entropy priors to refine the detection.

---


### 140. [NTIRE 2026 Challenge on Video Saliency Prediction: Methods and Results](https://arxiv.org/abs/2604.14816)

**<font color=#1a73e8>作者：</font>** Andrey Moskalenko, Alexey Bryncev, Ivan Kosmynin 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This paper presents an overview of the NTIRE 2026 Challenge on Video Saliency Prediction. The goal of the challenge participants was to develop automatic saliency map prediction methods for the provided video sequences. The novel dataset of 2,000 diverse videos with an open license was prepared for this challenge. The fixations and corresponding saliency maps were collected using crowdsourced mouse tracking and contain viewing data from over 5,000 assessors. Evaluation was performed on a subset of 800 test videos using generally accepted quality metrics. The challenge attracted over 20 teams making submissions, and 7 teams passed the final phase with code review. All data used in this challenge is made publicly available - this https URL.

---


### 141. [Pangu-ACE: Adaptive Cascaded Experts for Educational Response Generation on EduBench](https://arxiv.org/abs/2604.14828)

**<font color=#1a73e8>作者：</font>** Dinghao Li, Wenlong Zhou, Zhimin Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Educational assistants should spend more computation only when the task needs it. This paper rewrites our earlier draft around the system that was actually implemented and archived in the repository: a sample-level 1B to 7B cascade for the shared-8 EduBench benchmark. The final system, Pangu-ACE, uses a 1B tutor-router to produce a draft answer plus routing signals, then either accepts the draft or escalates the sample to a 7B specialist prompt. We also correct a major offline evaluation bug: earlier summaries over-credited some open-form outputs that only satisfied superficial format checks. After CPU-side rescoring from saved prediction JSONL, the full Chinese test archive (7013 samples) shows that cascade_final improves deterministic quality from 0.457 to 0.538 and format validity from 0.707 to 0.866 over the legacy rule_v2 system while accepting 19.7% of requests directly at 1B. Routing is strongly task dependent: IP is accepted by 1B 78.0% of the time, while QG and EC still escalate almost always. The current archived deployment does not yet show latency gains, so the defensible efficiency story is routing selectivity rather than wall-clock speedup. We also package a reproducible artifact-first paper workflow and clarify the remaining external-baseline gap: GPT-5.4 re-judging is implemented locally, but the configured provider endpoint and key are invalid, so final sampled-baseline alignment with GPT-5.4 remains pending infrastructure repair.

---


### 142. [Beyond Literal Summarization: Redefining Hallucination for Medical SOAP Note Evaluation](https://arxiv.org/abs/2604.14829)

**<font color=#1a73e8>作者：</font>** Bhavik Vachhani, Kush Shrisvastava, Pranshu Nema 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating large language models (LLMs) for clinical documentation tasks such as SOAP note generation remains challenging. Unlike standard summarization, these tasks require clinical abstraction, normalization of colloquial language, and medically grounded inference. However, prevailing evaluation methods including automated metrics and LLM as judge frameworks rely on lexical faithfulness, often labeling any information not explicitly present in the transcript as hallucination.
We show that such approaches systematically misclassify clinically valid outputs as errors, inflating hallucination rates and distorting model assessment. Our analysis reveals that many flagged hallucinations correspond to legitimate clinical transformations, including synonym mapping, abstraction of examination findings, diagnostic inference, and guideline consistent care planning.
By aligning evaluation criteria with clinical reasoning through calibrated prompting and retrieval grounded in medical ontologies we observe a significant shift in outcomes. Under a lexical evaluation regime, the mean hallucination rate is 35%, heavily penalizing valid reasoning. With inference aware evaluation, this drops to 9%, with remaining cases reflecting genuine safety concerns. These findings suggest that current evaluation practices over penalize valid clinical reasoning and may measure artifacts of evaluation design rather than true errors, underscoring the need for clinically informed evaluation in high context domains like medicine.

---


### 143. [Improved Multiscale Structural Mapping with Supervertex Vision Transformer for the Detection of Alzheimer's Disease Neurodegeneration](https://arxiv.org/abs/2604.14837)

**<font color=#1a73e8>作者：</font>** Geonwoo Baek, David H. Salat, Ikbeom Jang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Alzheimer's disease (AD) confirmation often relies on positron emission tomography (PET) or cerebrospinal fluid (CSF) analysis, which are costly and invasive. Consequently, structural MRI biomarkers such as cortical thickness (CT) are widely used for non-invasive AD screening. Multiscale structural mapping (MSSM) was recently proposed to integrate gray-white matter contrasts (GWCs) with CT from a single T1-weighted MRI (T1w) scan. Building on this framework, we propose MSSM+, together with surface supervertex mapping (SSVM) and a Supervertex Vision Transformer (SV-ViT). 3D T1w images from individuals with AD and cognitively normal (CN) controls were analyzed. MSSM+ extends MSSM by incorporating sulcal depth and cortical curvature at the vertex level. SSVM partitions the cortical surface into supervertices (surface patches) that effectively represent inter- and intra-regional spatial relationships. SV-ViT is a Vision Transformer architecture operating on these supervertices, enabling anatomically informed learning from surface mesh representations. Compared with MSSM, MSSM+ identified more spatially extensive and statistically significant group differences between AD and CN. In AD vs. CN classification, MSSM+ achieved a 3%p higher area under the precision-recall curve than MSSM. Vendor-specific analyses further demonstrated reduced signal variability and consistently improved classification performance across MR manufacturers relative to CT, GWCs, and MSSM. These findings suggest that MSSM+ combined with SV-ViT is a promising MRI-based imaging marker for AD detection prior to CSF/PET confirmation.

---


### 144. [Efficient Search of Implantable Adaptive Cells for Medical Image Segmentation](https://arxiv.org/abs/2604.14849)

**<font color=#1a73e8>作者：</font>** Emil Benedykciuk, Marcin Denkowski, Grzegorz M. Wójcik  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: Adaptive skip modules can improve medical image segmentation, but searching for them is computationally costly. Implantable Adaptive Cells (IACs) are compact NAS modules inserted into U-Net skip connections, reducing the search space compared with full-network NAS. However, the original IAC framework still requires a 200-epoch differentiable search for each backbone and dataset. Methods: We analyzed the temporal behavior of operations and edges within IAC cells during differentiable search on public medical image segmentation benchmarks. We found that operations selected in the final discrete cell typically emerge among the strongest candidates early in training, and their architecture parameters stabilize well before the final epoch. Based on this, we propose a Jensen--Shannon-divergence-based stability criterion that tracks per-edge operation-importance distributions and progressively prunes low-importance operations during search. The accelerated framework is called IAC-LTH. Results: Across four public benchmarks (ACDC, BraTS, KiTS, AMOS), several 2-D U-Net backbones, and a 2-D nnU-Net pipeline, IAC-LTH discovers IAC cells whose patient-level segmentation performance matches and sometimes slightly exceeds that of cells found by the original full-length search, while reducing wall-clock NAS cost by 3.7x to 16x across datasets and backbones. These results are consistent across architectures, benchmarks, and both non-augmented and augmented training settings, while preserving the gains of IAC-equipped U-Nets over strong attention-based and dense-skip baselines. Conclusion: Competitive IAC architectures can be identified from early-stabilizing operations without running the full search, making adaptive skip-module design more practical for medical image segmentation under realistic computational constraints.

---


### 145. [ClimateCause: Complex and Implicit Causal Structures in Climate Reports](https://arxiv.org/abs/2604.14856)

**<font color=#1a73e8>作者：</font>** Liesbeth Allein, Nataly Pineda-Castañeda, Andrea Rocci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding climate change requires reasoning over complex causal networks. Yet, existing causal discovery datasets predominantly capture explicit, direct causal relations. We introduce ClimateCause, a manually expert-annotated dataset of higher-order causal structures from science-for-policy climate reports, including implicit and nested causality. Cause-effect expressions are normalized and disentangled into individual causal relations to facilitate graph construction, with unique annotations for cause-effect correlation, relation type, and spatiotemporal context. We further demonstrate ClimateCause's value for quantifying readability based on the semantic complexity of causal graphs underlying a statement. Finally, large language model benchmarking on correlation inference and causal chain reasoning highlights the latter as a key challenge.

---


### 146. [Benchmarks for Trajectory Safety Evaluation and Diagnosis in OpenClaw and Codex: ATBench-Claw and ATBench-CodeX](https://arxiv.org/abs/2604.14858)

**<font color=#1a73e8>作者：</font>** Zhonghao Yang, Yu Li, Yanxu Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agent systems move into increasingly diverse execution settings, trajectory-level safety evaluation and diagnosis require benchmarks that evolve with them. ATBench is a diverse and realistic agent trajectory benchmark for safety evaluation and diagnosis. This report presents ATBench-Claw and ATBench-CodeX, two domain-customized extensions that carry ATBench into the OpenClaw and OpenAI Codex / Codex-runtime settings. The key adaptation mechanism is to analyze each new setting, customize the three-dimensional Safety Taxonomy over risk source, failure mode, and real-world harm, and then use that customized taxonomy to define the benchmark specification consumed by the shared ATBench construction pipeline. This extensibility matters because agent frameworks remain relatively stable at the architectural level even as their concrete execution settings, tool ecosystems, and product capabilities evolve quickly. Concretely, ATBench-Claw targets OpenClaw-sensitive execution chains over tools, skills, sessions, and external actions, while ATBench-CodeX targets trajectories in the OpenAI Codex / Codex-runtime setting over repositories, shells, patches, dependencies, approvals, and runtime policy boundaries. Our emphasis therefore falls on taxonomy customization, domain-specific risk coverage, and benchmark design under a shared ATBench generation framework.

---


### 147. [Curvature-Aligned Probing for Local Loss-Landscape Stabilization](https://arxiv.org/abs/2604.14870)

**<font color=#1a73e8>作者：</font>** Nikita Kiselev, Andrey Grabovoy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Local loss-landscape stabilization under sample growth is typically measured either pointwise or through isotropic averaging in the full parameter space. Despite practical value, both choices probe directions that contribute little to the dominant local deformation of strongly anisotropic neural landscapes. We recast stabilization as an observational problem and introduce a unified family of criteria parameterized by an aggregation order and a probing distribution; within this family we propose a curvature-aligned criterion $\Delta_2^{(D)}$ that probes the loss increment field in the top-$D$ eigenspace of the empirical Hessian near a trained solution. Solely from a local quadratic model, we prove that $\Delta_2^{(D)}$ preserves the $O(k^{-2})$ mean-squared rate of the full-space criterion while replacing ambient-dimension curvature dependence with dependence on the subspace dimension $D$; a corollary gives a closed-form spectral expression and a proposition identifies the top-$D$ eigenspace as extremal within the eigenspace-aligned family. We also derive scalable estimators based on Hessian-vector products, subspace Monte Carlo, and a closed-form Gaussian-moment proxy. On a decoder-only transformer, a curvature-aligned probe occupying a tiny fraction of parameter space already reproduces the full-space mean-squared signal to within numerical noise throughout the validated local regime, and the closed-form estimator is orders of magnitude faster than direct Monte Carlo after subspace construction.

---


### 148. [SkillDroid: Compile Once, Reuse Forever](https://arxiv.org/abs/2604.14872)

**<font color=#1a73e8>作者：</font>** Qijia Chen, Andrea Bellucci, Zhida Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> LLM-based mobile GUI agents treat every task invocation as an independent reasoning episode, requiring a full LLM inference call at each action step. This per-step dependence makes them stateless: a task completed successfully yesterday is re-derived from scratch today, with no improvement in reliability or speed. We present SkillDroid, a three-layer skill agent that compiles successful LLM-guided GUI trajectories into parameterized skill templates (sequences of UI actions with weighted element locators and typed parameter slots) and replays them on future invocations without any LLM calls. A matching cascade (regex patterns, embedding similarity, and app filtering) routes incoming instructions to stored skills, while a failure-learning layer triggers recompilation when skill reliability degrades. Over a 150-round longitudinal evaluation with systematic instruction variation and controlled perturbations, SkillDroid achieves an 85.3% success rate (23 percentage points above a stateless LLM baseline) while using 49% fewer LLM calls. The skill replay mechanism achieves a perfect 1000% success rate across 79 replay rounds at 2.4 times the speed of full LLM execution. Most critically, the system improves with use: its success rate converges upward from 87% to 91%, while the baseline degrades from 80% to 44%.

---


### 149. [Open-Set Vein Biometric Recognition with Deep Metric Learning](https://arxiv.org/abs/2604.14874)

**<font color=#1a73e8>作者：</font>** Paweł Pilarek, Marcel Musiałek, Anna Górska  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Most state-of-the-art vein recognition methods rely on closed-set classification, which inherently limits their scalability and prevents the adaptive enrollment of new users without complete model retraining. We rigorously evaluate the computational boundaries of Deep Metric Learning (DML) under strict open-set constraints. Unlike standard closed-set approaches, we analyze the impact of data scarcity and domain shift on recognition performance. Our approach learns discriminative L2-normalised embeddings and employs prototype-based matching with a calibrated similarity threshold to effectively distinguish between enrolled users and unseen impostors. We evaluate the framework under a strict subject-disjoint protocol across four diverse datasets covering finger, wrist, and dorsal hand veins (MMCBNU 6000, UTFVP, FYO, and a dorsal hand-vein dataset). On the large-scale MMCBNU 6000 benchmark, our best model (ResNet50-CBAM) achieves an OSCR of 0.9945, AUROC of 0.9974, and EER of 1.57%, maintaining high identification accuracy (99.6% Rank-1) while robustly rejecting unknown subjects. Cross-dataset experiments evaluate the framework's generalisation across different acquisition setups, confirming that while the model handles large-scale data robustly, performance remains sensitive to domain shifts in low-data regimes. Ablation studies demonstrate that triplet-based objectives combined with a simple 1-NN classifier offer an optimal trade-off between accuracy and efficiency, enabling real-time deployment on commodity hardware.

---


### 150. [SOLIS: Physics-Informed Learning of Interpretable Neural Surrogates for Nonlinear Systems](https://arxiv.org/abs/2604.14879)

**<font color=#1a73e8>作者：</font>** Murat Furkan Mansur, Tufan Kumbasar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear system identification must balance physical interpretability with model flexibility. Classical methods yield structured, control-relevant models but rely on rigid parametric forms that often miss complex nonlinearities, whereas Neural ODEs are expressive yet largely black-box. Physics-Informed Neural Networks (PINNs) sit between these extremes, but inverse PINNs typically assume a known governing equation with fixed coefficients, leading to identifiability failures when the true dynamics are unknown or state-dependent. We propose \textbf{SOLIS}, which models unknown dynamics via a \emph{state-conditioned second-order surrogate model} and recasts identification as learning a Quasi-Linear Parameter-Varying (Quasi-LPV) representation, recovering interpretable natural frequency, damping, and gain without presupposing a global equation. SOLIS decouples trajectory reconstruction from parameter estimation and stabilizes training with a cyclic curriculum and \textbf{Local Physics Hints} windowed ridge-regression anchors that mitigate optimization collapse. Experiments on benchmarks show accurate parameter-manifold recovery and coherent physical rollouts from sparse data, including regimes where standard inverse methods fail.

---


> [!TIP]
> 当前位于：**101-150**（第 3/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
