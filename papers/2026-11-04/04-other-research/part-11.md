# 📦 其他研究 | 2026年11月04日

> 本类共 **633** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**501-550**（第 11/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-633](./part-13.md)

---

### 501. [Kolmogorov-Arnold Networks vs. Multi-Layer Perceptrons: A Rigorous Statistical Benchmark on Clinical Tabular Data](https://arxiv.org/abs/2611.02856)

**<font color=#1a73e8>作者：</font>** Rafał Wodziński, Paweł Szczerbiak  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) have recently been proposed as a promising alternative to Multi-Layer Perceptrons (MLPs). However, empirical evaluations on structured medical datasets remain scarce, and commonly reported metrics like AUROC can yield overly optimistic performance estimates on imbalanced clinical cohorts. In this study, we present a standardized benchmark comparing eleven architectures - nine KAN variants (FastKAN, WavKAN, ReLUKAN, ChebyKAN, TaylorKAN, GramKAN, JacobiKAN, LegendreKAN, and TabKAN), a tuned StandardMLP, and a Random Forest baseline - across seven heterogeneous medical tabular datasets spanning oncology, cardiology, nephrology, neurology, endocrinology, and obstetrics. Our experimental protocol employs a 3x5 Repeated Stratified K-Fold cross-validation scheme with nested Bayesian hyperparameter optimization and evaluates discrimination via Area Under the Precision-Recall Curve (AUPRC), calibration through the Brier Score, and computational efficiency. Formal equivalence testing is conducted using the Bayesian Correlated t-Test with a Region of Practical Equivalence (ROPE) at +/- 0.01. The results indicate that on datasets with severe class imbalance, dedicated KAN architectures (particularly TabKAN and ReLUKAN) can improve minority-class detection and achieve higher AUPRC than standard MLPs. Nevertheless, across pooled datasets, KAN variants demonstrate comparable overall predictive discrimination rather than a systematic advantage, while requiring 1.20x to 1.48x longer inference latency per sample and up to 12.5x more trainable parameters. Consequently, StandardMLP remains a strong baseline on the efficiency Pareto frontier, while KAN variants provide a viable alternative when precision on rare positive cases is the primary clinical objective. The code for reproducing the results is available at this https URL.

---


### 502. [Solv3R: 3D Looped Transformer as a Multi-view Solver](https://arxiv.org/abs/2611.02857)

**<font color=#1a73e8>作者：</font>** Jeong-gi Kwak, Andrea Tagliasacchi, Sho Kagami 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Classical structure-from-motion reconstruction proceeds iteratively, refining camera poses and scene geometry from a current estimate. This allows maps to easily expand without recomputing already computed views, or geometry estimates to improve as more observations are provided. Most geometric foundation models, however, predict entire geometry in a single forward pass or update a recurrent state as frames arrive sequentially, making this expansion and refinement non-trivial. We introduce Solv3R, a looped transformer that learns to continue solving multi-view geometry from its current state. Importantly, its update operator is independent of the iteration count, allowing previously refined and newly introduced views to be jointly updated regardless of how ``solved'' they are. We train the operator to preserve accurate reconstructions under continued iteration and correct inaccurate states, enabling refinement of fixed image collections and integration of new observations. Representations of solved views can also be cached once and reused as geometric context across iterations, enabling compact and efficient key-value caching. We analyze the solver dynamics and compare it with the state-of-the-art, demonstrating that a single learned solver supports offline reconstruction, incremental reconstruction, relocalization, and streaming without task-specific training or modules. The code and models will be made publicly available at this https URL.

---


### 503. [Evaluating autonomous self-healing against persistent cyber-attacks](https://arxiv.org/abs/2611.02858)

**<font color=#1a73e8>作者：</font>** Bart Gijsen, Stefano Nieuwenhuizen, Lucien Yap 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The need for autonomous cyber resilience (ACR) is strongly accelerating. The boost in cyber capabilities of advanced AI is speeding up the attacker-defender rat race to an unprecedented pace. As a result, the field of ACR must progress from early design and experimentation to hands-on evaluation and deployment. To illustrate what is needed for this transition, we put TNO's autonomous immune system-inspired Self-Healing for Cyber Security (SH4CS) software to the test. Our analytic and experimental evaluation results demonstrate that effective cyber resilience is achieved with SH4CS for (repeated) web application vulnerability exploits. Remaining challenges of SH4CS revolve around finding the right balance between predictable resilient behaviour, and adaptiveness to the large variety of cyber threats and applications-to-be-protected.

---


### 504. [Performance evaluation of super-resolution techniques for characterization and phenotyping of commodity crops using multispectral imagery](https://arxiv.org/abs/2611.02862)

**<font color=#1a73e8>作者：</font>** Abhiram Karukayil, João F. C. Mota, Mateo Vásquez-Guevara 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multispectral imagery provides spectral information beyond the visible range for vegetation monitoring, but it typically suffers from limited spatial resolution, which can obscure fine crop structures and affect vegetation-index (VI) estimates.} This study evaluates whether single-image super-resolution (SISR) methods developed for red, green, and blue (RGB) imagery can enhance the spatial resolution of red, green, and near-infrared (RGN) crop images while preserving spectral fidelity. Eight pretrained methods are applied directly to RGN images without fine-tuning: bicubic and nearest-neighbor interpolation, Real-ESRGAN, HAT, HiT-SR, SRFormer, ResShift, and StableSR. Reconstruction at $4\times$ and $16\times$ is evaluated for whole images and manually segmented leaf regions. Reconstruction quality is assessed using mean absolute error (MAE), peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), spectral angle mapper (SAM), and erreur relative globale adimensionnelle de synthèse (ERGAS). Eight VIs, computed from reference and super-resolved images, are evaluated using MAE, PSNR, and SSIM. Transformer-based methods \modification{significantly} outperform GAN- and diffusion-based approaches in both evaluation settings \modification{($p < 0.001$)}, with \modification{HAT, HiT-SR, and SRFormer forming the highest-performing statistical tier}. These findings indicate that RGB-trained SISR can enhance spatial detail in RGN crop imagery while maintaining spectral consistency and VI reliability for high-resolution crop phenotyping.

---


### 505. [TensorLOB: Structure-Preserving Tensor Learning for Limit Order Book Forecasting](https://arxiv.org/abs/2611.02866)

**<font color=#1a73e8>作者：</font>** Yuxuan Gu, Danilo Mandic  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The limit order book (LOB) records outstanding buy and sell orders across multiple price levels. Its state evolves over time across market side, price level, and order attribute, naturally forming a multiway structure. However, existing LOB models typically flatten these dimensions into a matrix model, thus obscuring the existing structural relationships. Starting from first principles and the market-microstructure intuition of the LOB, we design TensorLOB to operate entirely in the tensor domain. TensorLOB uses mode-wise tensor contractions for feature extraction and directly contracts the learned representation with low-rank class-weight tensors for prediction, retaining the distinct roles of time, side, level, and attribute modes. Experiments on the FI-2010 benchmark show that TensorLOB achieves the highest accuracy, recall, and F1 score across all four evaluated horizons. This proof of concept highlights the potential of high-dimensional modelling of multi-way latent information intrinsic to financial markets, which has so far been largely overlooked.

---


### 506. [AGiR: Mitigating Gift Over-Reliance in Mixed-Motive Games](https://arxiv.org/abs/2611.02875)

**<font color=#1a73e8>作者：</font>** Woohyeon Byeon, Seongmin Kim, Jiwon Jeon 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In this paper, we consider mixed-motive games (MMGs) which model various real-world multi-agent scenarios where self-interested agents must both cooperate and compete. We identify an issue with existing gifting methods, where agents become overly dependent on incoming gifts and fail to learn reward-yielding behaviors, a phenomenon we call gift over-reliance. To address this, we propose a refusal-augmented gifting framework that balances cooperation and competition in MMGs. Our approach introduces an adaptive refusal mechanism that allows agents to selectively reject a portion of received gifts from their policy-update signals, thereby mitigating gift over-reliance and preventing the agents from being exploited by other agents. This mechanism is gifting-method-agnostic, serving as a plug-in for existing schemes while enabling decentralized learning. We demonstrate that across diverse MMG environments and gifting schemes, our mechanism consistently reduces gift over-reliance and prevents lock-in to sacrificing policies, improving $\alpha$-fairness as a result, without necessitating major changes to existing training pipelines.

---


### 507. [Identifiable Signed Causal Learning via Latent Stochastic Differential Equations for Inferring Brain Dynamic Effective Connectivity](https://arxiv.org/abs/2611.02876)

**<font color=#1a73e8>作者：</font>** Yiding Wang, Chen Qiao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Understanding how brain regions interact to support cognitive tasks requires characterizing directed causal influences among them, known as effective connectivity (EC). As inter-regional coupling changes over time, a dynamic EC (dEC) estimate is required to track this temporal variation. Existing dEC learning methods typically lack a causal rationality guarantee or an identifiability analysis, and output unsigned connectivity that cannot distinguish excitatory from inhibitory influences, which limits further study of brain mechanisms. We propose ISCL, a latent stochastic differential equation framework that derives dEC from latent dynamics through a causal influence operator defined in observation space. As established by a rationality theorem, the operator captures a directed interventional response at each brain state, and under invariance assumptions the operator is identifiable from data, with its signed output separating excitatory from inhibitory influences. On synthetic benchmarks, \model recovers the causal structure on Lorenz96 and achieves the lowest mean structural Hamming distance among compared methods on NetSim, while preserving signed influence structures that distinguish excitatory from inhibitory interactions. Applied to HCP Social Cognition task-fMRI, ISCL reveals a signed architecture whose stability across seeds supports the identifiability guarantee, identifies dominant source and target networks consistent with social-cognition systems, and shows that condition-specific training strengthens causal outflow from the default-mode and frontoparietal networks during theory-of-mind processing. In this task, the recovered signed structure reveals network-level excitatory and inhibitory organization, with the dorsal-attention network as the only consistently positive out-strength source.

---


### 508. [ProtoFusion: Protocol-Guided Prompt Refinement for Generative Infrared and Visible Image Fusion](https://arxiv.org/abs/2611.02877)

**<font color=#1a73e8>作者：</font>** Pengwei Liang, Junjun Jiang, Junhui Hou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Infrared and visible image fusion integrates complementary information from both modalities to provide a more comprehensive representation of the scene. We propose ProtoFusion, a protocol-guided generative framework for infrared and visible image fusion. Instead of relying on fixed fusion operators, hand-crafted objectives, or manually specified one-shot prompts, ProtoFusion formulates fusion as protocol-constrained generation. It represents fusion intent with a structured protocol, consisting of environment state cards, grounding principles, and a style profile, which explicitly specifies which evidence should be preserved or suppressed and which properties the fused result should satisfy. To optimize this protocol, we introduce protocol-guided prompt refinement, a closed-loop learning framework that iteratively performs generation, evaluation, and revision under multimodal evidence. Once learned, the optimized protocol is fixed at inference time and directly guides fusion generation. To address residual source inconsistencies, we further incorporate structured belief construction, which organizes modality reliability, scene evidence, and cross-modal conflicts into a structured representation for conservative correction after generation. Extensive experiments on standard benchmarks show that ProtoFusion improves quantitative performance, achieves favorable results in aesthetic evaluation, and produces visually coherent fusion outputs. Project Page: {this https URL}.

---


### 509. [Extending Aircraft Coverage of the Poll Schumann Model Using Public Data](https://arxiv.org/abs/2611.02880)

**<font color=#1a73e8>作者：</font>** Gabriel Jarry, Ramon Dalmau, Philippe Very  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Poll Schumann model requires airframe and engine parameters, but published tables cover only part of the fleet. Applications must obtain missing parameters, substitute another aircraft type or exclude unrepresented types. We reconstruct parameters using geometry from certification documents and manufacturer manuals, together with ICAO engine records. Published equations supply the physical parameters, regression estimates the propulsion efficiency scale. The inventory covers 90 type designators, including 22 absent from the direct pycontrails table and 18 without a listed substitute. Across 68 types, mean absolute percentage error (MAPE) against pycontrails was 7.38% for drag and 3.14% for design Mach. Across 66 types in 21 families, efficiency regression achieved 3.91% MAPE with the evaluated family excluded from input selection and fitting. On 100 recorded A320 flights, a type already represented in the published tables, cruise fuel flow MAPE for reconstructed and published parameter sets was 4.50% versus 4.68%, while mean absolute percentage error in integrated fuel over covered airborne intervals was 7.19% versus 6.82%. Public technical records can therefore extend Poll Schumann parameter coverage, with quantified agreement against published coefficients and comparable fuel prediction errors on the evaluated A320 flights.

---


### 510. [A Universal Policy Wrapper With Guarantees](https://arxiv.org/abs/2611.02888)

**<font color=#1a73e8>作者：</font>** Georgiy Malaniya, Anton Bolychev, Pavel Osinenko  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many control tasks require driving the system into a prescribed goal set and subsequently keeping it there. The considered setting assumes that a working controller is available that provably reaches and maintains the goal, albeit with suboptimal performance. This controller is referred to as the fallback policy. Conversely, although state-of-the-art reinforcement-learning (RL) algorithms can discover policies with impressive empirical performance, the neural networks at their core act as opaque black boxes learned through data-driven exploration and, as such, provide no theoretical mechanism to guarantee that the system will ever reach---and stay within---the prescribed goal set. This article presents CALF-Wrapper, a method that combines the fallback policy with a pretrained RL base policy and uses the critic estimate associated with the base policy to select between them during deployment. The theoretical analysis establishes that CALF-Wrapper inherits the goal-reaching property of the fallback policy under the stated assumptions and provides probability bounds for the settling time and the maximum distance from the goal set over a prescribed time interval. The experimental study evaluates CALF-Wrapper in four simulated control environments of different complexity. Comparisons include the base policy, fallback policy, and constrained reinforcement-learning methods formulated for the same objective. Sensitivity and ablation studies provide direct hyperparameter recommendations. The experiments show how CALF-Wrapper can provide effective task performance while attaining the maximum possible observed goal-reaching rate. CALF-Wrapper requires no additional dynamics model, online learning, or constrained optimization during execution.

---


### 511. [Gibbs Variational Last Layers for Long-Horizon Dynamics Learning](https://arxiv.org/abs/2611.02891)

**<font color=#1a73e8>作者：</font>** Paul Brunzema, Henrik Hose, Sebastian Trimpe  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate long-horizon probabilistic predictions of dynamical systems are a prerequisite for model-based decision-making. Variational Bayesian last layers (VBLLs) are an attractive model class for this setting, offering tractable uncertainty at near-deterministic cost, yet they are trained exclusively with single-step likelihood objectives that may be insufficient for reliable multi-step rollouts. We revisit VBLLs through the lens of Gibbs variational inference, which decouples posterior inference from the choice of training loss. Building on this perspective, we introduce a family of multi-step training losses that progressively incorporate long-horizon structure, robustness via continuous ranked probability scores (CRPS), and training on full autoregressive rollouts. Our approach retains the simplicity of VBLLs while directly optimizing for multi-step predictive quality. Across illustrative synthetic environments, a diverse suite of chaotic dynamical systems, and real-world data, we show that multi-step, CRPS-based objectives substantially improve long-horizon accuracy and distributional fit, consistently outperforming single-step likelihood training.

---


### 512. [JABER: Sequential Quality Control for Human-AI Data Annotation under Shared Bias](https://arxiv.org/abs/2611.02892)

**<font color=#1a73e8>作者：</font>** Fengxu Yang, Minghui Liwang, Yang Lu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-quality annotations are essential for training and evaluating artificial intelligence (AI) systems. Quality control (QC) often acquires additional human or AI judgments before accepting a label. Nevertheless, shared biases can cause correlated judgments, leading conventional methods to mistake repeated agreement for independent evidence of correctness. To address this challenge, we propose JABER (Joint Alias-Preserving Belief for Evidence Routing), a bias-aware sequential QC framework that maintains a joint Bayesian posterior over label correctness and shared biases to guide evidence acquisition and termination decisions. Building on this posterior, we develop a finite-horizon algorithm that selects evidence-acquisition and termination actions to minimize expected QC loss under resource constraints. Our theoretical analysis shows that conditional-independence updating can become arbitrarily confident in an incorrect label under persistent shared bias. We further identify when repeated inspections cannot distinguish a correct label from an incorrect label supported by shared bias, when obtaining a new label can resolve this ambiguity, and why modeling the dependence between label correctness and shared bias can be necessary for QC decisions. Our experiments show that JABER reduces expected QC loss by an average of 4.65% compared with a method maintaining separate label correctness and bias probabilities when shared bias makes repeated inspections unreliable. Further, JABER's finite-horizon planning, which evaluates outcomes of successive QC actions, reduces expected QC loss by an average of 10.05% compared with a one-step lookahead method. In real-API experiments on FEVER, JABER achieves zero labeling errors while reducing QC costs by 2.67% and 16.99% compared with marginal-based belief modeling and one-step lookahead methods, respectively.

---


### 513. [TailorRig: Controllable and Structured Auxiliary Skeleton Generation for Garment-Aware Rigging](https://arxiv.org/abs/2611.02902)

**<font color=#1a73e8>作者：</font>** Yajing Chen, Xin Chen, Saidan Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Humanoid rigging for modern characters with complex garments remains challenging due to the need for dense auxiliary skeletons and precise skinning control. Existing automatic methods primarily recover rigs from geometry, providing limited artist control over auxiliary articulation and often lacking explicit semantic or kinematic-chain structure for dense garment bones, leading to instability and weight bleeding. We present TailorRig, a framework that reformulates garment-aware humanoid rigging as a structured, controllable full-rig generation problem. This formulation shifts the goal from automatic rig recovery to artist-driven rig authoring, where both body-template compatibility and auxiliary articulation are explicit design choices. TailorRig exposes two explicit axes of artist control within a unified framework: a user-specified body skeleton template that preserves body-rig compatibility, and artist-provided semantic labels that drive an autoregressive generator to synthesize requested category-specific auxiliary bone chains. To robustly assign skinning weights under dense skeletal configurations, we further introduce a hierarchical chain-to-bone formulation: vertices are first associated to a kinematic chain, and bone weights are then refined within that chain, reducing weight bleeding between spatially adjacent but semantically unrelated structures. We evaluate TailorRig on a diverse set of characters and introduce Human-Mix, a large-scale dataset of over 38,000 humanoid models curated for garment-aware rigging. Experiments show that TailorRig improves skeleton accuracy, deformation stability, controllability, and practical usability over existing methods.

---


### 514. [Maswao: An automatically collected, prepared, and benchmarked dataset for the South African Sign language](https://arxiv.org/abs/2611.02903)

**<font color=#1a73e8>作者：</font>** Thapelo Sindane, Unarine Netshifhefhe, Vukosi Marivate 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advancements in sign language processing can be attributed to developments in both large-scale dataset collection and algorithmic complexity in areas such as pose estimation techniques, signal processing through Transformer models, and model optimization. However, only a handful of sign languages, such as the American, British, and German, from over 200 globally recognized sign languages, reap the benefits of such advancements, while the rest lag behind. In this study, we aim to address this technological disparity by proposing a framework for the automatic collection and preparation of sign language datasets, with very minimal human-labour intervention, using the South African Sign Language (SASL) as a testbed. Specifically, we automatically collect SASL video content using public resources such as news broadcasts. Additionally, we convert their accompanying audio streams into text using available Automatic Speech Recognition (ASR) tools. Furthermore, we crop the sign language area in the videos and use gradient descent to locate valleys of non-motion to determine end-of-sentence points within long videos to create our weakly sentence-aligned parallel corpora -- the Maswao (Signs) dataset. Finally, we benchmark the weakly aligned dataset on the task of Sign-to-text Translation using Recurrent Neural Networks and Transformer models to compare their individual intricacies. Our results show that Transformer models proposed in the literature outperform recurrent baselines, with the best-performing Transformer achieving BLEU-1 to BLEU-4 scores of 13.78, 5.21, 2.52, and 1.54, respectively, as well as ChrF = 18.09 and ROUGE-L = 10.51. These results indicate that the task remains promising and warrants further investigations.

---


### 515. [Unimodal Augmentation-based SSL Objectives Induce Cross-Modal Alignment](https://arxiv.org/abs/2611.02917)

**<font color=#1a73e8>作者：</font>** Zohar Mashiah, Nir Ben-Ari, Ronen Talmon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent works have observed implicit cross-modal alignment between independently trained unimodal models. However, the mechanisms underlying the emergence of this phenomenon remain unresolved. In this paper, we demonstrate that unimodal augmentation-based self-supervised objectives implicitly induce cross-modal alignment. We show that low unimodal losses force high cross-modal alignment, whereas a high unimodal loss prevents such alignment. We theoretically connect the widely used InfoNCE loss to local CKA, the popular measure of cross-modal alignment. We further provide extensive empirical evidence supporting this claim, both in controlled settings and across 53 unconstrained frozen text, vision, and audio unimodal encoders. In both cases, unimodal augmentation-based objectives control cross-modal alignment. Overall, our results provide a theoretical and empirical foundation for understanding the emergence of implicit cross-modal alignment by establishing a direct connection between unimodal training objectives and cross-modal structure.

---


### 516. [Unlocking the Potential of Contrastive Regularization for Diffusion Transformer Training](https://arxiv.org/abs/2611.02921)

**<font color=#1a73e8>作者：</font>** Yi Tan, Beier Zhu, Sirui Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation regularization has emerged as an effective way to improve diffusion transformer training. Yet one of the most canonical regularizers--InfoNCE-style contrastive learning--remains largely underexplored in this setting. We naturally ask a question: can standard contrastive learning serve as an effective regularizer for diffusion transformers? Surprisingly, we find that naive InfoNCE regularization brings only marginal gains. Our analysis reveals that the objective is easily dominated by a shortcut: near-orthogonal noise components in diffusion inputs provide a bypass for enlarging negative-pair distances while weakening positive-pair alignment, especially at high noise levels. To unlock the benefit of contrastive regularization, we propose Clean Representation-ANchored Contrastive (CRAN) regularization. Specifically, CRAN anchors contrastive dispersion with clean-sample representation distances, transferring clean relational semantic structure to noisy diffusion representations to suppress the noise shortcut. Extensive experiments on ImageNet show that CRAN consistently improves diffusion transformer training across model scales and training budgets, outperforming internal feature-alignment and dispersive regularization baselines while matching external DINO-guided REPA. These results re-establish InfoNCE-based contrastive learning as an effective regularizer for diffusion training, once its noise-driven over-dispersion is properly constrained.

---


### 517. [Comprehensive Evaluation of Monocular and Multi-view 3D Human Pose Estimation Models for Fitness Exercise Analysis](https://arxiv.org/abs/2611.02929)

**<font color=#1a73e8>作者：</font>** Néstor Ortega, Agustín Salgado, Javier Sánchez  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Three-dimensional human pose estimation has become a fundamental component of computer vision systems for sports analytics, rehabilitation, and motion understanding. Although recent deep learning approaches have achieved remarkable accuracy on standard benchmarks, their performance under realistic sports scenarios remains insufficiently studied. Furthermore, the trade-offs between recent monocular and multi-view approaches, as well as the benefits of post-processing techniques for improving temporal consistency, have not been systematically evaluated on fitness-oriented datasets. This paper evaluates recent state-of-the-art 3D human pose estimation methods on Fit3D, a dataset of synchronized multi-view recordings of a wide variety of fitness exercises with accurate ground-truth annotations. We study two recent monocular lifting approaches, TCPFormer and PoseMamba-L, and a multi-view model, MVGFormer, under a unified evaluation protocol. To investigate the influence of the input data, monocular methods are evaluated using ground-truth keypoints and detections generated by recent 2D pose estimators, RTMPose and YOLO-Pose. Additionally, we analyze the effectiveness of three temporal filters for reducing prediction jitter while preserving motion dynamics. Experimental results provide a detailed comparison of accuracy, temporal consistency, and robustness to imperfect 2D detections across the evaluated methods. Our analysis highlights the impact of detector quality on lifting-based approaches, compares transformer- and state-space-based temporal architectures, and discusses the practical trade-offs between monocular and multi-view systems for fitness motion analysis. Our results show that 2D detection quality, temporal modeling, and post-processing must be considered jointly in pose estimation pipelines for exercise analysis.

---


### 518. [Training-Time Domain Transfer for Generator-Free Diagnostics on Novel Modalities in Computational Pathology](https://arxiv.org/abs/2611.02931)

**<font color=#1a73e8>作者：</font>** Julia A. Mielcarz, Andrea Camilloni, Nita Mulliqi 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Novel imaging modalities promise improved diagnostics, but AI development is constrained by scarce training data. Inference-time domain transfer can address this by mapping novel modalities to established ones, enabling reuse of existing diagnostic models. However, this introduces hallucination risks, computational overhead, and regulatory complexity. Inspired by sim-to-real transfer, we propose training-time domain transfer, generating synthetic target-domain training data from archived routine samples to enable direct diagnosis on real inputs without inference-time generation. Using unstained prostate histopathology as a proof-of-concept, we compare this approach with inference-time virtual staining and conventional H&E-based cancer detection. Training-time transfer achieved higher concordance with the conventional benchmark than virtual staining for both raw (Cohen's $\kappa$=0.59 vs. 0.37; Gwet's AC1=0.73 vs. 0.29) and deparaffinized tissue ($\kappa$=0.66 vs. 0.61; AC1=0.73 vs. 0.64), supporting its potential for emerging diagnostic modalities.

---


### 519. [ILR-SMO: Iterative Latent Refinement for Robust Spatial Multi-Omics Integration](https://arxiv.org/abs/2611.02932)

**<font color=#1a73e8>作者：</font>** Anqi Yu, Xudong Xu, Jianzhi Lu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spatial multi-omics technologies jointly profile diverse molecular modalities with spatial context, providing a comprehensive view of cellular heterogeneity and tissue organization. To integrate spatial multi-omics data and identify spatial domains, a wide range of unsupervised methods has been proposed. However, recent approaches rely on single-step fusion, directly aggregating heterogeneous modalities into a shared representation, making embeddings sensitive to modality imbalance and measurement noise that are inherent to spatial multi-omics data, as well as unstable optimization under weak supervision. Here, we propose ILR-SMO (Iterative Latent Refinement for Spatial Multi-Omics), a unified self-supervised framework that reformulates multimodal integration as a stability-aware refinement process over a shared latent representation. Instead of single-step plain fusion, ILR-SMO progressively integrates modality-specific information through sequential updates, allowing information to be injected in a controlled manner. This incremental refinement enables later updates to correct or compensate for earlier deviations, resulting in more stable and robust representation learning under heterogeneous and noisy modalities. ILR-SMO further incorporates reliability-aware modality gating for adaptive modulation of modality contributions, and employs a joint objective to enforce spatial coherence while preventing representation collapse. Extensive experiments on five spatial multi-omics benchmarks demonstrate that ILR-SMO consistently outperforms seven state-of-the-art methods and exhibits strong robustness across diverse settings.

---


### 520. [Leakage-Aware Encrypted Semantic Communication with Key-Conditioned Signal Perturbation](https://arxiv.org/abs/2611.02938)

**<font color=#1a73e8>作者：</font>** Omar Kaaki, Maria Slim, Mariette Awad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Encrypted semantic communication systems protect transmitted messages by inserting key-conditioned modules into a deep-learning semantic communication pipeline, but existing designs rely on a fixed adversarial weight and operate mainly at the semantic-feature level. We propose two changes to the encrypted semantic communication system (ESCS): a key-conditioned signal-domain perturbation layer, called learned adversarial perturbation injection (LAPI), and an information noise-contrastive estimation (InfoNCE)-guided adaptive training rule that {adds an adaptive leakage penalty alongside the fixed adversarial objective} using an InfoNCE-based proxy for mutual information leakage. Experiments on the Europarl corpus over additive white Gaussian noise (AWGN) and Rayleigh fading channels show that InfoNCE-guided training is the primary source of eavesdropper suppression, reducing the eavesdropper's bilingual evaluation understudy (BLEU) score to approximately 0.07 at high signal-to-noise ratio (SNR). Adding LAPI to the InfoNCE-guided objective further lowers the InfoNCE-estimated leakage by 5-9% with low measured inference overhead, while its impact on legitimate-receiver BLEU depends on channel conditions. The two mechanisms operate on different parts of the pipeline and can be jointly applied.

---


### 521. [RouteREPA: Routed Representation Alignment for Just Image Transformers](https://arxiv.org/abs/2611.02941)

**<font color=#1a73e8>作者：</font>** Yi Tan, Beier Zhu, Sirui Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Representation alignment (REPA) is widely used to accelerate the training of latent-space diffusion transformers (DiTs). However, applying it to pixel-space models such as Just Image Transformers (JiT) is challenging. Our analysis reveals a pronounced representation conflict between discriminative alignment and pixel-space generation. Compared with its latent counterpart, JiT learns representations that are substantially less aligned with DINOv2. Applying REPA to JiT consistently reduces the reconstructability of its intermediate representations, whereas this effect is not observed in Latent JiT. We attribute this conflict to JiT directly reconstructing pixels, which requires its representations to hierarchically encode discriminative semantics and reconstruction-relevant visual information across network depths. To address these challenges, we propose Routed Representation Alignment (RouteREPA), which uses lightweight, representation-dependent routers to adaptively route task-oriented representations for alignment and generation. We further apply routing across multiple network depths to accommodate their depth-dependent representation requirements. Extensive experiments on ImageNet-1K at 256x256 resolution show that RouteREPA consistently improves JiT across model scales and training budgets, outperforming standard REPA. On JiT-H/16, RouteREPA further surpasses PixelREPA using only one-third of its training epochs without classifier-free guidance.

---


### 522. [Exact Fusion of Softmax Attention Heads Can Require Exponentially Many Atoms](https://arxiv.org/abs/2611.02943)

**<font color=#1a73e8>作者：</font>** Hiroyasu Usami, Keisuke Hara, Ayato Tsuboi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fusing independently normalized attention heads can increase the number of explicit key-value entries, or atoms, needed to preserve their output. We prove a sharp separation for $W_d(q)=\sum_{j=1}^d\sigma(q_j)$: its $d$ two-atom heads use $2d$ head-atom terms, whereas its minimum single-head representation has exactly $2^d$ atoms, even with arbitrary fixed replacement keys, scalar values, and positive masses. The same lower bound holds for every fixed uniform error below $1/2$ on $\mathbb R^d$, and the threshold is sharp. The proof uses exposed-key normal cones; exact equality on any nonempty open query domain inherits the bound. The resulting atom bound for a fixed head count is tight when that count divides $d$. A normalized family retains its exponential exact minimum while approaching a constant on fixed-radius query balls. For pretrained-model caches, a classical affine-rank bound and a certified instance exclude exact vector preservation at a specified atom count. Learned-cache comparisons on two disjoint banks of 64 contexts show budget-dependent reversals and calibration effects.

---


### 523. [Balancing Representations by Identifying and Generating Under-represented Data](https://arxiv.org/abs/2611.02952)

**<font color=#1a73e8>作者：</font>** Filipe Laitenberger, Hirokatsu Kataoka, Yuki Asano 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Self-supervised learning inherits the coverage of its source data. When an unlabeled corpus is long-tailed, the representation becomes dense around frequent modes and thin where coverage is weak. Objectives for long-tailed SSL reweight the images already in the corpus and add no new ones. We introduce BRIDGE (Balancing Representations by Identifying and Generating Under-represented Data), a label-free feedback loop around the source set. The current encoder scores every source image by its mean kNN distance, and a budgeted acquisition rule selects images from a band of that score distribution where support is thin and the generator still produces faithful variants. A frozen image-to-image diffusion model then adds local variants of the selected anchors, and pretraining continues on the enlarged source set. We formulate acquisition as recoverability-weighted allocation of local support and derive when a finite budget should favor a sparse band that excludes the extreme tail and when reallocation after each repair is optimal under a fixed objective. Across five long-tailed, web-scraped and synthetic source regimes, BRIDGE has the highest seven-task linear-probe and kNN average of the compared methods, and paired experiments extend the gain to ViT-S under contrastive and self-distillation objectives, to low-label fine-tuning and to semantic segmentation. The linear-probe gain is smaller under masked reconstruction. Generated repair matches an oracle that restores the withheld real images, and under a frozen encoder the inserted images shrink the neighborhoods of the selected anchors about twice as much as those of matched unselected images. BRIDGE needs no labels and leaves the pretraining objective unchanged, so it can be added to pretraining on uncurated web data, where the encoder decides which images to generate.

---


### 524. [One Image Is Enough: Self-Generated Supervision for Personalizing Human Video Diffusion at Test Time](https://arxiv.org/abs/2611.02964)

**<font color=#1a73e8>作者：</font>** Sadman Rakib Pinon, Adamo Orsini, Yanis Falaki 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pose-driven human video diffusion animates a person from a single reference image and a target pose sequence, yet it struggles to preserve identity, rendering the face and garments unfaithfully as the pose departs from it. Personalization is the standard remedy, but its supervision is missing: one image fixes identity at a single pose, while a multi-pose subject video cannot be assumed in practice. Instead, we synthesize the missing supervision. A domain-tuned, pose-conditioned generator produces pseudo-ground-truth frames at selected key poses. An inference-time reference-only sampler steers these candidates toward the subject and keeps the most identity-consistent. A per-subject low-rank adapter then trains on static clips of them, configured from the reference alone, with no subject video, ground truth, or labels. Although lower in fidelity, these synthetic frames supervise more effectively than real ones. Real frames as captured carry motion that erodes the temporal prior, while a static clip conveys appearance alone. On TikTok and UBC Fashion, the adapted model improves the base on every metric, inverts the identity-versus-motion trade-off, and matches or surpasses adaptation on five real frames despite using none. Code and weights are available at this https URL.

---


### 525. [Utility-Aware Generative Recommendation: Utility-Enriched Semantic Codes and Utility-Guided Decoding](https://arxiv.org/abs/2611.02981)

**<font color=#1a73e8>作者：</font>** Yang Hu, Duo Wang, Ning Li 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative recommendation has been widely adopted in large-scale industrial recommendation systems, where multimodal item embeddings are quantized into offline semantic identifiers (SIDs) and items are retrieved by autoregressively generating their SIDs. However, conventional SID construction often underrepresents item utility reflected in post-exposure behaviors such as shares, long views, and video completion, making semantically similar items with different utility insufficiently distinguishable while struggling to accommodate rapidly changing utility signals. Moreover, generation likelihood may be misaligned with downstream utility, causing high-utility candidates to be prematurely pruned during beam search before post-generation reranking or training-time reward alignment can effectively compensate. To address these limitations, we propose UAGR, which aligns both SID construction and decoding with downstream multi-objective utility. Our Utility-Enriched Semantic Codes preserve the original semantic information while incorporating item-level utility without increasing SID length or vocabulary size, supporting incremental utility updates with no additional tokenization or sequence-decoding cost. Meanwhile, our Utility-Guided Decoding estimates candidate utility by combining predictions of multiple post-exposure outcomes and incorporates these estimates into beam scoring, reducing the risk of prematurely pruning high-utility paths while enabling flexible utility control without interfering with generative backbone training. Extensive offline experiments and online A/B tests under real-world traffic demonstrate the effectiveness and deployability of UAGR, which has been fully deployed on Kuaishou and increases video watch time by 0.206\% online.

---


### 526. [Supporting Habit Formation in Pre-Meal Photo Capture: A Longitudinal Study of Behavior Change Techniques](https://arxiv.org/abs/2611.02983)

**<font color=#1a73e8>作者：</font>** Jun Fang, Yueying Suo, Yuntao Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Pre-meal photo capture is lightweight only with a smartphone, yet habit formation requires repeatedly initiating and completing the action within the narrow window before the first bite. We examine how supports based on behavior change techniques can shape capture adherence, perceived habit, and support needs over time. Using a participant-informed selection process, we implemented three smartphone supports targeting Prompts/cues, Focus on past success, and Social support. We evaluated them in a five-week field study with 54 participants, spanning support, withdrawal, and reinstatement, followed by interviews and a three-week follow-up. Across 4,945 main meals, 63.9\% were confirmed pre-meal captures, and adherence was broadly maintained across phases. Perceived automaticity and spontaneous remembering improved mainly during initial support. As capture became more familiar, participants combined spontaneous remembering with deliberate strategies, reduced active feature use while continuing to value support availability, and carried the practice forward through accumulated records, familiar tools, and chosen relationships. These findings frame BCT support for pre-meal photo capture as a configurable arrangement. Systems should preserve a predictable capture pathway while adapting when, how, and through whom support remains available.

---


### 527. [ILLRAW: Illumination-Aware RAW Object Detection](https://arxiv.org/abs/2611.02995)

**<font color=#1a73e8>作者：</font>** Xinzhe Wang, Xiao Liang, Xiaoli Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing RAW-based detectors typically introduce learnable ISP modules to convert RAW inputs into sRGB-like formats to fit off-the-shelf detectors. However, this RAW-to-sRGB paradigm decouples representation learning from the downstream detection task. Crucially, it forces the network to inherit human-centric visual priors while discarding intrinsic RAW advantages, such as linear sensor responses and high-bit-depth, minimally processed scene cues. In this paper, we propose \textbf{ILLRAW}, an \textbf{ILL}umination-aware end-to-end \textbf{RAW} object detection framework. Instead of reconstructing visually plausible sRGB images, ILLRAW directly learns detection-oriented RAW features through a lightweight feature adapter inserted at the input stage of existing detectors. ILLRAW estimates an illumination mask and introduces channel-sensitive embeddings to model Bayer-channel responses. These features are fused by an illumination attention fusion module. Experiments show clear improvements on the diverse AODRaw benchmark and competitive performance on LOD and PascalRAW, with particularly strong results under dark exposure.

---


### 528. [Systematic Derivation of Leakage in Massey Secret Sharing Schemes](https://arxiv.org/abs/2611.03009)

**<font color=#1a73e8>作者：</font>** Nadja Aoutouf, Daniel Augot  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Leakage attacks on secret sharing schemes can be based on the exploitation of partial information about individual shares to recover the underlying secret. In coding theory, linear exact repair schemes (LERSs) allow the recovery of a codeword symbol from limited information obtained from the remaining symbols. When applied to code-based secret sharing schemes, such repair schemes can be interpreted as recovering the secret from partial information about the shares, expressed in terms of subfield symbols. Guruswami and Wootters introduced the first explicit constructions of LERSs for low-rate Reed--Solomon codes that is optimal in terms of bandwidth. In this work, we first investigate the construction and algebraic properties of LERSs, building on the Guruswami-Wootters construction. We derive new explicit repair schemes from their construction and establish structural properties of the resulting schemes. Second, we further develop a systematic computational approach based on a Gr{ö}bner bases approach to identify leakage functions associated with LERSs for arbitrary linear codes. This approach enables us to investigate the existence and structural properties of LERSs across different code families and parameter ranges. We first applied our method to Reed-Solomon codes, which gave as further insights into the algebraic structure of LERSs. Moreover, by applying our method to generalized Reed-Muller and Tamo-Barg codes, we identify several LERSs that, to the best of our knowledge, have not previously been described in the literature.

---


### 529. [Comparative study of global pooling for pre-departure ship fuel consumption prediction: Advantages over per-ship and adaptation-based approaches](https://arxiv.org/abs/2611.03015)

**<font color=#1a73e8>作者：</font>** Heungjun Im, Bongmin Cha, Agung Nugraha 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most fuel oil consumption (FOC) models for voyage planning are per-ship models and thus generalize poorly beyond each vessel's records. Transfer and federated learning have been reported to perform better, but under different protocols that often use inputs unavailable before departure or random data splits. It therefore remains unclear which approach performs best. In this study, we compare 11 per-ship, adaptation-based, and global methods on 21 vessels. To prevent leakage, all methods receive identical inputs known or forecast before departure, excluding engine RPM and shaft power, and are tested on intact voyage legs after all training records of each vessel. Global pooling, in which one model describes each vessel by its ship identity and seven ship specifications, performs best overall in every setting examined. For in-fleet vessels, Global LightGBM reaches an overall MAPE of 8.92%, against 11.14% for Per-Ship LightGBM, and outperforms every per-ship and adaptation-based model. Global models of five architectures, including a Transformer, all outperform the per-ship and federated models. Fine-tuning a global model for each vessel, even by low-rank adaptation of the Transformer, adds no accuracy. Without any records of a vessel, the global model reaches a median MAPE of 11.20% and outperforms a per-ship model trained on that vessel's records for 14 of 21 vessels. Adding its first records to the pooled data is as accurate as vessel-specific adaptation. Ship identity and specifications are largely interchangeable for in-fleet vessels, but only the specifications support zero-shot prediction. Its error grows as a vessel's specifications differ from the fleet's. Per-ship models and vessel-specific adaptation are therefore unnecessary under fair comparison. One global model can serve a whole fleet, including newly delivered vessels with similar specifications.

---


### 530. [Efficient Hybrid Distillation: Synergizing Score and Adversarial Objectives for One-Step Diffusion](https://arxiv.org/abs/2611.03017)

**<font color=#1a73e8>作者：</font>** Fei Peng, Junqiang Wu, Haoxian Tan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Numerous distillation methods have been developed to accelerate diffusion models. Recent research indicates that hybrid strategies---blending different paradigms---yield superior results compared to single-method approaches. However, current works predominantly rely on a simple combination of objectives, leaving the question of how to effectively synergize them largely underexplored. In this paper, we specifically investigate the synergy between Score Distillation and Adversarial Distillation. We reveal that their operating zones are distinct and complementary: Score Distillation is effective in high-noise regimes for capturing the global distribution yet lacks fine-grained supervision in low-noise regions. Conversely, Adversarial Distillation is effective in low-noise regions but is prone to instability and suffers from discriminator failure when applied to high-noise intervals. Leveraging this insight, we propose Efficient Adversarial Score Distillation (EASD), a framework that synergizes these objectives via a regime-adaptive sampling strategy, directing each objective to focus on its effective interval. We further apply this paradigm to DiT-based Flow Matching models. Empirically, our method achieves a promising one-step FID of 1.39 on ImageNet 256$\times$256 using the SiT-XL/2+REPA model. This work provides a concrete guideline for maximizing the potential of hybrid distillation. Our code and model are available at this https URL .

---


### 531. [How Data Journalists Visualize Uncertainty: Editorial Constraints and Design Heuristics in Newsroom Practice](https://arxiv.org/abs/2611.03018)

**<font color=#1a73e8>作者：</font>** Carmen Garro, Annemarie Wisbar, Benjamin Possin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Communicating uncertainty is increasingly recognized as important in data journalism, yet in practice it is often oversimplified, downplayed, or omitted. To understand how uncertainty is handled in newsroom visualization practice, we conducted a full-day workshop with 11 data journalists from major German-speaking newsrooms. The workshop combined presentations of newsroom examples, collaborative scenario classification, World Café discussions on authoring hurdles, and group reflections on audience needs and future directions. Our findings suggest that uncertainty communication is primarily a workflow- and context-dependent editorial decision, constrained by production overhead, anticipated audience misinterpretation, publication formats, and the need to preserve a clear takeaway. Rather than relying on advanced visualization techniques, practitioners favor pragmatic defaults, layered communication, and explanatory guidance tailored to audience and medium. The scenario-based framework we provided is valued less as a strict taxonomy for classifying finished visualizations than as a planning prompt for early design reasoning. Based on these insights, we contribute (i) practitioner-informed findings on the challenges and strategies of visualizing uncertainty in journalistic practice, (ii) a refined scenario-based framework to support communication about uncertainty, and (iii) practice-oriented heuristics for designing uncertainty visualizations in newsrooms. Our work contributes to bridging visualization research and newsroom practice by grounding uncertainty communication in the realities of journalistic production. Supplemental material is available at this https URL.

---


### 532. [The Tower of Babel in artificial intelligence: who should speak, and when it pays to listen](https://arxiv.org/abs/2611.03020)

**<font color=#1a73e8>作者：</font>** Mohammad Salahshour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two machines can each recognize an object well and still fail together. We study classifiers that see different parts of one object and send short messages to a receiver that identifies its class. Coordination asks how to design messages together; cooperation asks whether the team outperforms one sender given the whole budget. On three digit datasets, messages designed together beat messages designed apart by 18.07 to 22.68 percentage points on average with two-bit messages, with gains in all 24 configurations. A fixed agreement, you report the row and I the column, recovers about half this gain, with only the receiver learned. Senders that draw the same distinctions waste a narrow vocabulary, and senders whose distinctions cross multiply it. A team has no more possible messages than one sender with the same budget, so a partner must bring evidence the first lacks. A solvable model shows individual statistics alone cannot determine whether a partnership helps. On MNIST digits, six shared bits remove 49.54 percent of the strongest tested solo's errors on average. Paired measurements correctly predicted most sensor teams would reduce average accuracy on new participants. Who should speak is a property of the pair, and must be measured in pairs.

---


### 533. [MetamorphX: An Ungrounded 3-DoF Moment Display that Changes its Physical Properties through Rotational Impedance Control](https://arxiv.org/abs/2611.03021)

**<font color=#1a73e8>作者：</font>** Takeru Hashimoto, Shigeo Yoshida, Takuji Narumi  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Humans can estimate the properties of wielded objects (e.g., inertia and viscosity) using the force applied to the hand. We focused on this mechanism and aimed to represent the properties of wielded objects by dynamically changing the force applied to the hand. We propose MetamorphX, which uses control moment gyroscopes (CMGs) to generate ungrounded, 3-degrees of freedom moment feedback. The high-response moments obtained from CMGs allow the inertia and viscosity of motion to be set to the desired values via impedance control. A technical evaluation indicated that our device can generate a moment with a 60-ms delay. The inertia and viscosity of motion were varied by $0.01\,\mathrm{kg\,m^2}$ and $0.1\,\mathrm{N\,s}$, respectively. Additionally, we demonstrated that our device can dynamically change the inertia and viscosity of motion through virtual reality applications.

---


### 534. [Improved regret bounds in tabular RL under local differential privacy](https://arxiv.org/abs/2611.03026)

**<font color=#1a73e8>作者：</font>** Hugo Richard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study regret minimization for time-homogeneous episodic tabular reinforcement learning with $S$ states and $A$ actions under non-interactive $\epsilon$-local differential privacy (LDP). In each episode $k \in [K]$, the decision-maker sends a policy to a user, the user executes the policy for $H$ steps, and sends an $\epsilon$-locally differentially private message back to the decision-maker. When $H=1$, the problem reduces to an LDP contextual bandit with $S$ contexts, $A$ arms and horizon $K$. We prove that the minimax regret is $\min\bigg(K, \frac{ \sqrt{\max( S, \exp(\epsilon) + 1) S A K (\exp(\epsilon) + 1)}}{\exp(\epsilon) - 1}\bigg)$, up to constants and a $\sqrt{\log(A)}$ factor. The upper bound is achieved by an adaptation of EXP3 and a unary encoding mechanism. When $H > 1$, and for small $\epsilon$, we show a lower bound in $\Omega(HS\frac{\sqrt{A K}}{\epsilon})$ and an upper bound in $\tilde{O}(H^2 S^2 \frac{\sqrt{ AK}}{\epsilon})$. The upper bound is achieved by an algorithm based on UCBVI and a unary encoding mechanism. For small $\epsilon$, these bounds improve the previously known lower bound by a factor $\sqrt{S}$ and the previously known upper bound by a factor of $H \sqrt{A}$.

---


### 535. [Hybrid Federated Learning for Multimodal Fusion under Missing Modalities and Site Heterogeneity](https://arxiv.org/abs/2611.03032)

**<font color=#1a73e8>作者：</font>** Xiaofei Wu, Rongmei Liang, Jian Qing Shi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multimodal fusion is studied under hybrid federation, where data are partitioned across samples and feature blocks. The proposed two-dimensional federated smooth multiple-kernel large-margin learning method (2D-FedSMKL) integrates availability-corrected modality scores, group-kernel regularization, and smooth worst-site risk aggregation. For fixed maps and propensities, the objective is convex and smooth. Curvature bounds and exact synchronous block-gradient equivalence are established for binary and multiclass scores, giving a conditional accelerated rate. An oracle-propensity binary risk bound and a propensity-perturbation result are also derived. Simulations and two public activity-recognition benchmarks assess site heterogeneity and modality absence. Worst-site aggregation improves worst-site performance under heterogeneity, including reversed and size-balanced designs. On the benchmarks, validation selects the correction; the selected model is not significantly worse than the strongest reference at the worst site, and group-regularization benefits vary by dataset.

---


### 536. [GPU-Native Real-Time Textured Mesh Reconstruction with Seam-Aware Multi-View Radiometric Correction](https://arxiv.org/abs/2611.03033)

**<font color=#1a73e8>作者：</font>** Hiroyuki Sato  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present a GPU-native volumetric-video system for real-time reconstruction of graphics-compatible textured triangle meshes from multiple RGB-D sensors. Existing TSDF systems accelerate fusion and mesh extraction, but extending them to per-frame textured meshing adds CPU mesh processing, CPU-side texturing work, or extra CPU-GPU transfers between stages. After input staging, our method keeps the reconstruction and texturing stages (TSDF fusion, Marching Cubes, connected-component noise removal, view-based texture mapping, inpainting, and radiometric seam correction) resident on the GPU; no intermediate mesh or image data returns to the host between these stages. A fixed-size-array representation of mesh topology gives constant-time neighbor access on the GPU and makes the downstream mesh-level operations data-parallel. Because we texture each face from a single camera, exposure seams that vary smoothly across each image remain; we estimate a per-camera low-frequency gain field and bake it into the atlas on the GPU. On the CMU Panoptic dataset, our method is faster than the baselines at every tested voxel resolution and number of sensors, achieves peak speedups of more than an order of magnitude over CUDA-accelerated nvblox and CPU-based Open3D, and approaches an offline textured-meshing baseline in perceptual re-rendering quality.

---


### 537. [When Does Design Thinking Work? A Convergence Theorem for the Iterate-Test Core](https://arxiv.org/abs/2611.03034)

**<font color=#1a73e8>作者：</font>** Paweł Kuraś, Adrian Michalski, Alicja Gerka 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Design thinking is widely taught as an iterative loop of ideation, prototyping, and testing, yet conditions under which such a loop must improve innovation outcomes remain unspecified. Taking problem framing as given, we formalize the iterate-test core as search over a finite prototype space whose utility is learned through noisy evaluations. We prove that the prototype a team believes to be best converges almost surely to a local optimum under five conditions: finite framing, local ideation, non-summable discovery rates, unbiased repeated testing, and retention of tested prototypes. Bounded test bias or criteria drift degrades the guarantee by a bounded amount, and multiple stakeholders yield convergence to a locally Pareto-optimal set. Finite-horizon simulations across three landscape classes (additive valuation, NK rugged landscapes, and clustered modular architectures) show that asymptotic limits are rarely reached in practice. Teams face an optimizer's curse, overestimating their chosen concept by 4-8% and frequently discarding superior prototypes. Testing every prototype once proves to be the worst allocation; optimal performance requires building one to three prototypes per five tests and repeatedly re-testing leaders. Pre-screening concepts yields greater performance gains than tuning testing policies.

---


### 538. [TSB-SEG: A Systematic Time-Series Segmentation Benchmark](https://arxiv.org/abs/2611.03039)

**<font color=#1a73e8>作者：</font>** Félix Chavelli, Arik Ermshaus, Fan Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series segmentation, studied as either Change Point Detection (CPD) or State Detection (SD), underpins a broad range of monitoring and diagnostic applications. However, the field suffers from a persistent divide between the statistical community (focusing on CPD) and the machine learning and data mining communities (focusing on SD). Consequently, the literature remains fragmented: evaluations typically cover narrow methodological families, datasets are often small or homogeneous, and CPD and SD are rarely evaluated together. We address these gaps with TSB-SEG, a unified benchmark comprising 592 univariate and multivariate time series from 8 heterogeneous datasets and surveying 26 algorithms that span five decades of progress. To ensure a fair comparison, we introduce a two-pool design: a scalable main pool of tractable detectors used for the aggregate ranking, and an extended-scope pool for computationally intensive methods. All methods are unified under tsseg, an open-source library to ensure full reproducibility. Our systematic evaluation yields three insights: (a) no single detector dominates across domains, and per-dataset hyperparameter tuning remains decisive for performance, (b) CPD accuracy is a useful, though imperfect, proxy for SD accuracy, and (c) data characteristics should guide method selection. We provide actionable guidance based on data properties, error tolerances, and tuning budgets, identify impactful hyperparameters, and characterize algorithm robustness to these choices.

---


### 539. [Bayesian Sequential Optimal Experimental Design for Single-Pixel Imaging using Reinforcement Learning](https://arxiv.org/abs/2611.03042)

**<font color=#1a73e8>作者：</font>** Marcos Antonio Obando, Tianyuan Wang, Tanja Tarvainen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Adaptive compressed sensing (CS) aims to select the most informative measurements sequentially, which is crucial for many modern imaging systems. This task can be formulated as a Bayesian sequential optimal experimental design (sOED) problem, where each new acquisition is chosen to maximally reduce uncertainty about the unknown image given prior information and subsequent data provided by acquisitions. However, in single-pixel imaging (SPI), the large design space consists of all possible binary illumination patterns. Directly optimizing the Bayesian sOED objective over this space using conventional methods is generally challenging.
In this work, we reformulate sOED for SPI as a reinforcement learning (RL) problem. In RL, an agent learns a policy through repeated experimental trials to maximize a reward, here given as the expected information gain, the most complete measure of uncertainty reduction in Bayesian OED. This avoids the need to directly optimize complex information-theoretic objectives during a measurement to obtain the next design. Instead, the result is a learned policy function that directly maps the current posterior belief about the image to the next optimal binary measurement pattern, in a computationally efficient way.
Using a simple yet representative SPI imaging scenario, this work evaluates the scalability of the learned policy under two different policy parameterizations. Furthermore, we investigate how performance deteriorates when only approximate posterior information is available or the measurements are impaired by noise, and propose several strategies to introduce additional design constraints motivated by biomedical applications. The numerical experiments demonstrate that the proposed Bayesian sOED-RL framework remains robust and can be extended to more complex, large-scale SPI scenarios.

---


### 540. [Selfrionette: A Fingertip Force-Input Controller for Continuous Full-Body Avatar Manipulation and Diverse Haptic Interactions](https://arxiv.org/abs/2611.03052)

**<font color=#1a73e8>作者：</font>** Takeru Hashimoto, Yutaro Hirao  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We propose Selfrionette, a controller that uses fingertip force input to drive avatar movements in virtual reality (VR). This system enables users to interact with virtual objects and walk in VR using only fingertip force, overcoming physical and spatial constraints. Additionally, by fixing users' fingers, it provides users with counterforces equivalent to the applied force, allowing for diverse and wide dynamic range haptic feedback by adjusting the relationship between force input and virtual movement. To evaluate the effectiveness of the proposed method, this paper focuses on hand interaction as a first step. In User Study 1, we measured usability and embodiment during reaching tasks under Selfrionette, body tracking, and finger tracking conditions. In User Study 2, we investigated whether users could perceive haptic properties such as weight, friction, and compliance under the same conditions as User Study 1. Selfrionette was found to be comparable to body tracking in realism of haptic interaction, enabling embodied avatar experiences even in limited spatial conditions.

---


### 541. [Optimal Subgroup Discovery at Every Support Threshold](https://arxiv.org/abs/2611.03053)

**<font color=#1a73e8>作者：</font>** Lincen Yang, Qi Huang, Niki van Stein 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Subgroup discovery aims to identify regions of the feature space where a target variable deviates from its marginal distribution. A fundamental challenge in this problem is the trade-off between a subgroup's deviation and its support: small subgroups can be highly deviating but statistically meaningless, while large ones cannot deviate much by construction. Existing methods tackle this challenge by collapsing the two into a single scalar quality measure, implicitly committing to one particular trade-off and making it difficult to recover the most deviating subgroup under a user-specified support constraint. We instead provide the first theoretical and structural characterization of optimal subgroups with maximum Kullback-Leibler (KL) divergence under arbitrary support constraints. Under a partition-based generative model, where the feature space decomposes into regions of homogeneous conditional distributions of the target variable called atoms, we prove that every point on the deviation-support Pareto front is a union of whole atoms together with at most one fractional atom. This reduces an uncountable search to a finite combinatorial problem. Guided by this theory, we propose a simple two-step recipe: learn a homogeneous partition, then select atoms greedily. Across 19 benchmark datasets, it finds the most deviating subgroups at a range of support thresholds, and reliably improves subgroups returned by existing methods when applied as a post-processing step. These results empirically validate the sufficiency and necessity of our theoretical contributions.

---


### 542. [SAGE (Subjectivity-Aware Generation Estimator): A Linguistic Framework for AI-Generated Review Detection *](https://arxiv.org/abs/2611.03060)

**<font color=#1a73e8>作者：</font>** Gonzalo Freijedo Aduna, Charles Yaiche, Patrick Bas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We propose a simple, linguistically motivated approach to detecting AI-generated peer reviews based on the inherently human trait of subjectivity. We capture subjectivity at two levels: the semantic level of evaluative language and modality and the pragmatic level of speech acts. Using features derived from speech act annotations and model-predicted subjectivity scores, we train a lightweight classifier that achieves an AUROC of 0.9566 with only these linguistic features. Combining its output with the state-of-the-art detector Sem-Detect raises the TPR at 1% FPR of Sem-Detect on the APRDB benchmark from 0.874 to 0.985, outperforming the current state of the art. Our results show that linguistic features of subjectivity provide an explainable source of information for detecting AI-generated peer reviews and can be readily integrated into existing detection methods. The code and models are publicly available on GitHub (this https URL\_ text\_detection\_hub) and Hugging Face (this https URL), respectively.

---


### 543. [MuCHMDPoser: Multiview RGB-Camera Full-Body Pose Tracking for Virtual Reality](https://arxiv.org/abs/2611.03062)

**<font color=#1a73e8>作者：</font>** Antoine Maiorca, George Fletcher, Thierry Ravet 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate full-body tracking in Virtual Reality (VR) is heavily underconstrained when relying solely on consumer-grade sparse sensors, such as Head-Mounted Displays (HMDs) and handheld controllers. Indeed, the self-avatar full-body pose must be inferred based on the 3 available upper-body joints tracked by these devices. This leads to significant tracking error, especially in lower-body pose. To overcome this issue, we propose to extend the tracking setup with external multiview RGB cameras. We show that integrating RGB-based pose estimation this framework is able to significantly decrease lower-body tracking errors, even under common artifacts in RGB-based estimates. Additionally, we evaluate a only-once HMD-camera calibration procedure that does not require any physical markers. We finally propose an implementation of the overall framework, achieving an end-to-end animation at 60 FPS on a Nvidia RTX3080 GPU. Codes are available at this https URL.

---


### 544. [Networked AI: Architecture, Theory, and Applications](https://arxiv.org/abs/2611.03063)

**<font color=#1a73e8>作者：</font>** Liang Song, Jiayue Jin, Peng Sun 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in Artificial Intelligence (AI), particularly large-scale deep learning, have been driven by monolithic or offline training on massive curated datasets. While successful, these approaches face structural limitations: escalating data and computational demands, limited online adaptability, and a lack of system-level intelligence in open, non-stationary environments. This paper presents Networked AI - a networked intelligent system composed of interacting, heterogeneous, and continuously evolving AI agents. We establish a hierarchical layered architecture comprising an Agent Layer for heterogeneous capability construction, an Interaction Layer for signal-processing-guided online data extraction, and a Regulation Layer for stability-constrained collective evolution. Foundations in data science, signal processing, and system control are hereby synthesized into a unified theoretical framework of Networked AI, providing superior data efficiency, intelligence efficiency, interpretability, and scalability. Theoretical and experimental analysis demonstrates that Networked AI can approach near-linear scaling in resource demand, in contrast to the exponential increase in standalone end-to-end systems. It provides not only online adaptation to out-of-distribution environmental novelties, but also the autonomous evolution towards application-specific intelligence. Application frontiers are discussed for IoT spaces, embodied, spatial, and industrial intelligences, as well as the cellular infrastructure and beyond. Key open challenges are identified towards realizing locally autonomous, collectively intelligent, continuously evolving, globally regulated Networked AI.

---


### 545. [MIRA: Reinforcing Multimodal Reasoning via Deceptive Contextual Augmentation](https://arxiv.org/abs/2611.03087)

**<font color=#1a73e8>作者：</font>** Zhihan Yin, Jianxin Liang, Yifeng Yao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Reinforcement Learning with Verifiable Rewards (RLVR) has significantly advanced multimodal reasoning, existing frameworks suffer from a critical "perception-reasoning gap." Due to an over-reliance on seemingly relevant visual tokens, even minor perceptual perturbations can propagate through the reasoning process, leading to compounding hallucinations. To address this issue, we propose MIRA, a training framework that improves robustness to erroneous visual contexts while enhancing logical reasoning ability. By injecting filtered, deceptive visual contexts during training, we construct challenging "hard traps" that stress-test the model's robustness to misleading information. Furthermore, we introduce a group-wise reflection-triggering mechanism that enables the model to autonomously detect and rectify inconsistencies between visual cues and logical constraints, which is ultimately internalized as an intrinsic policy behavior. Importantly, MIRA does not rely on human annotations. Experimental results across multiple reasoning and perception benchmarks show that MIRA yields an average 7% improvement on in-domain benchmarks, with consistent improvements on vision-centric benchmarks. These findings highlight that active error recovery is essential for robust multimodal reasoning. Comprehensive ablation studies and analyses further provide insights into why MIRA is effective.

---


### 546. [Avatar Intelligence: Amplifying Human Agency Through Persistent Personal Agents](https://arxiv.org/abs/2611.03092)

**<font color=#1a73e8>作者：</font>** Zheng Wu, Xinbei Ma, Yao Yao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Personal AI agents are increasingly capable of handling long-horizon tasks across applications, yet users often need to invest substantial effort in specifying goals, resolving ambiguity, and verifying outcomes. We argue that progress should be measured by how effectively agents amplify human agency: enabling people to pursue their goals with less routine supervision while retaining control over consequential decisions. We advocate Avatar Intelligence, a paradigm of persistent personal agents that represent users' goals, values, and constraints through sustained decision delegation across contexts and time. We describe a maturity roadmap from human-directed execution to autonomous operation within delegated domains, and introduce the Agentic Oversight Index (AOI) as a framework for evaluating delivered value against agent-side operational cost and human oversight burden. We identify three core research challenges: identity-continuous personalization that carries user preferences across tasks, user-situated evolution through Rehearsal Engineering, and safety mechanisms that combine technical control with accountability and recourse. These directions define a research agenda for reliable decision delegation to personal agents across tasks and over time.

---


### 547. [Ray-SCR: Generalizing Scene Coordinate Regression Across Camera Models](https://arxiv.org/abs/2611.03098)

**<font color=#1a73e8>作者：</font>** Jaemin Cho, Oleksii Nasypanyi, Francois Rameau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Among visual localization strategies, scene coordinate regression (SCR) has emerged as an attractive approach for its compactness, accuracy, and speed. Despite these advantages, SCR models generalize poorly across substantially different camera models, such as omnidirectional or strongly rectified imagery. This limitation arises because, changes in field of view, lens distortion, or rectification-induced resampling can make the same scene content appear differently depending on its pixel position, degrading localization accuracy. To cope with this limitation, we introduce Ray-SCR, a lightweight extension to existing SCR architectures that conditions local visual features on their calibrated viewing rays and refines neighboring ray-conditioned features with a shallow local Transformer. We further formulate supervision directly in ray space and use sparse SfM points as metric anchors that link observations across views and camera models. Taken together, these components enable a single scene representation built from a panoramic mapping sequence to accurately localize query images captured with very different cameras, including pinhole, fisheye, and omnidirectional cameras.
We evaluate Ray-SCR across multiple SCR architectures and on datasets with pinhole, fisheye, and omnidirectional cameras. The proposed ray conditioning substantially improves generalization across cameras and leads to state-of-the-art localization performance in these challenging cross-camera settings. The project page is available at this https URL.

---


### 548. [Multimodal Prompt Learning with Dual-Granularity Contrastive Alignment for Preoperative Prediction of Lung Adenocarcinoma Invasiveness Using 3D CT](https://arxiv.org/abs/2611.03109)

**<font color=#1a73e8>作者：</font>** Qing Huang, Xiaotong Tan, Lintong Yao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate preoperative prediction of lung adenocarcinoma invasiveness is important for surgical planning and individualized treatment. However, overlapping CT appearances make it challenging to distinguish invasive adenocarcinoma (IAD) from Pre-IAD lesions. We propose a multimodal prompt-learning framework with dual-granularity image-text alignment for 3D CT-based IAD classification. A 3D ResNet-CBAM encoder extracts global and spatial visual features. A frozen RadBERT backbone is adapted with separate learnable prompts for report-level and keyword-level text encoding. These prompts are initialized using semantic representations derived from real-world clinical reports. Global contrastive alignment connects whole-volume CT representations with reports generated from clinician-annotated radiological attributes to provide overall semantic supervision. A multiple instance learning-based local alignment module associates spatial CT features with vascular-focused radiological keywords, to capture local imaging characteristics potentially associated with tumor invasion. The framework jointly optimizes classification and alignment objectives, while inference requires only CT images. Experiments included 1,593 pathologically confirmed nodules. On the test set, the proposed method achieved an accuracy of 87.92%, F1-score of 87.78%, and AUC of 0.9499. Its AUC significantly exceeded that of the image-only Res-CBAM baseline with the same visual backbone (0.9297; DeLong test, p = 0.0078). Ablation analyses supported the complementary contributions of global and local alignment and the benefit of report-based prompt initialization. Qualitative visualizations showed activation within nodules and adjacent vascular structures. These findings suggest that dual-granularity radiological supervision can enhance CT-based invasiveness prediction while preserving a CT-only inference workflow.

---


### 549. [3D Gaussian Splatting within Self-Learned Neural View-Dependent Color Fields](https://arxiv.org/abs/2611.03114)

**<font color=#1a73e8>作者：</font>** Yixiao Yang, Yu-Shen Liu, Zhizhong Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D Gaussian Splatting (3DGS) has become a vital tool in novel view synthesis. 3D Gaussian functions with attributes like color, opacity, and scale are stacked together to explicitly model a radiance field. However, discrete 3D Gaussians usually produce poor depth with few geometry details but lots of floaters, which hinders the effective modeling of smooth radiance fields. To address this issue, we propose to learn a radiance field within a continuous view-dependent color field parameterized by neural networks. With continuous constraints in color, the bias on low-frequency signals of neural networks can highly encourage the geometry modeling to contribute to high-frequency color variations on images, getting rid of solely relying on the color attribute itself. Moreover, we impose a constraint to improve the Lipschitz continuity of the neural color field, making large changes of each Gaussian's color also match with large changes of its position in terms of a ratio. To this end, we additionally introduce novel self-learning strategies to improve the learning of the neural view-dependent color field without any external knowledge or priors, aiming for better generalization on unseen scenes. Our numerical and visual comparisons on widely used benchmarks justify our idea and show better ability of high fidelity geometry recovery in 3DGS. Project page: this https URL.

---


### 550. [KAUSTics-Net: Diffusion-Based Through-Water UAV Restoration with a Semi-Synthetic Dataset](https://arxiv.org/abs/2611.03120)

**<font color=#1a73e8>作者：</font>** Dario Scilla, Omar A. Lopez, Kasper Johansen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate mapping of shallow-water environments using unmanned aerial vehicle (UAV) imagery is challenged by water-induced distortions, including refraction, caustics, and wavelength-dependent attenuation. The scarcity of paired distorted and reference imagery further limits the development of supervised restoration methods. To address this challenge, we introduce KAUSTics, a semi-synthetic dataset combining 1,280 reference patches derived from 32 high-resolution UAV images with 12,800 degraded observations generated through Blender-based water-surface rendering and empirical color and blur augmentations. We further propose KAUSTics-Net, a pixel-space conditional diffusion framework integrating a multi-scale conditional encoder, feature-wise linear modulation (FiLM), cross-attention, and a composite reconstruction objective to restore shallow-water imagery. We evaluated the framework against eight image-restoration methods, complemented by architectural ablations and cross-dataset experiments. On KAUSTics, KAUSTics-Net achieved a mean peak signal-to-noise ratio (PSNR) of 31.715 +/- 0.439 dB, structural similarity index (SSIM) of 0.849 +/- 0.002, and learned perceptual image patch similarity (LPIPS) of 0.145 +/- 0.007 across three training seeds. On the independent Sea-Undistort dataset, sampler-aware fine-tuning improved restoration fidelity, reaching 19.469 +/- 0.332 dB PSNR and 0.554 +/- 0.005 SSIM under combined water-surface distortions, although perceptual trade-offs remained. Additional experiments on real UAV imagery examined feature preservation and segmentation behavior. These findings demonstrate the potential of semi-synthetic training and conditional diffusion for shallow-water image restoration while highlighting the importance of evaluating both reconstruction fidelity and downstream remote-sensing utility.

---


> [!TIP]
> 当前位于：**501-550**（第 11/13 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | **501-550** | [551-600](./part-12.md) | [601-633](./part-13.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
