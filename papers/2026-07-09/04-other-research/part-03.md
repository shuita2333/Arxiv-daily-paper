# 📦 其他研究 | 2026年07月09日

> 本类共 **195** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-195](./part-04.md)

---

### 101. [Bit2Watt: A Cyber-Physical Vulnerability Exploiting GPU Workloads Across Power and Computing Infrastructures](https://arxiv.org/abs/2607.05993)

**<font color=#1a73e8>作者：</font>** Zhouhao Ji, Kaikai Pan, Wenyuan Xu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern data centers increasingly rely on large-scale GPU clusters and on-site renewable energy resources, resulting in a tightly coupled cyber-physical system between computing workloads and power-electronic-dominated grids. In this paper, we reveal Bit2Watt, a previously unexplored vulnerability in which an adversary manipulates GPU workloads to induce controlled, high-frequency power modulations that destabilize local power infrastructure and propagate back to disrupt computing services. Unlike traditional attacks that compromise grid-side devices or communication channels, Bit2Watt operates entirely within the cyber layer as a legal tenant, which could amplify fluctuations, harmonic distortion, and damping degradation, particularly in high-DER-penetration scenarios. This risk is difficult to detect under routine cloud- and facility-side monitoring because it exploits legitimate workload execution paths and concentrates much of its distinctive behavior in high-frequency components that are weakly captured by common telemetry. We validate Bit2Watt through impedance-based analysis, power system simulations, and real-world experiments on GPUs and grid-connected PV inverters. Under the synchronized worst-case aggregation model studied in the paper, manipulating 1,000 GPUs in a 1-MW local power system with 90% DERs raises current THD to 46.8% and results in a damping ratio of -0.27. We further show that the resulting power-quality degradation can stress data-center power-delivery equipment, trigger protection mechanisms, and, in extreme simulated cases, induce cascading failures in transmission-scale systems. In addition, we analyze a plausible Watt2Bit feedback path, including denial-of-service risks and covert information exfiltration via EMI side channels. This work highlights the urgent need for cross-layer defenses that jointly consider workload scheduling and power electronics.

---


### 102. [Unlearnable Faces: Privacy Protection Surviving Extraction Pipeline](https://arxiv.org/abs/2607.05996)

**<font color=#1a73e8>作者：</font>** Byunghoon Oh, Sunghwan Park, Jaewoo Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unlearnable examples keep publicly shared photos from being learned by unauthorized face-recognition models. An imperceptible perturbation, added before sharing, makes any model trained on the protected photos fail on clean faces. The perturbation is crafted on the shared image, however the attacker trains on the face it extracts, cropped and resized to the recognizer input, and under this extraction the protection collapses. We propose LPID, which builds the extraction into the unlearnable-example objective. LPID confines the perturbation to the extracted face region and optimizes it through a differentiable model of the extraction, concentrating its energy in the frequency band the extraction preserves. Because this robustness is a property of the transform rather than of any identity, LPID is re-optimized per album and protects even users it has never seen. LPID attains the lowest attacker accuracy of all methods in every setting we evaluate, holding the attacker below $10\%$ under crop+resize extraction on identities unseen at protection time, while remaining imperceptible at $32.7$\,dB PSNR and $0.161$ LPIPS.

---


### 103. [AgoraSim: A Hybrid Agent-Based Modeling Framework](https://arxiv.org/abs/2607.05999)

**<font color=#1a73e8>作者：</font>** Chung-Chi Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-agent simulations make natural-language social scenarios easy to instantiate, but their outputs can be overread as predictions and are often difficult to compare with explicit social dynamics. We present AgoraSim, a hybrid agent-based modeling framework for scenario-oriented social reaction analysis. AgoraSim resolves textual or multimodal artifacts into editable ABM configurations, runs ratio-controlled populations that mix LLM, vision-language, custom-endpoint, random, and classical agents, and compares the same scenario against matched classical reference dynamics. All agents emit a shared structured decision object, enabling common action spaces, interaction protocols, metrics, and audit records. Exposed through a local UI, Python SDK/CLI, and REST API, AgoraSim helps users inspect scenario trajectories, compare modeling assumptions, and identify cases that warrant empirical validation.

---


### 104. [OBBSeg: Irregular Lesion Segmentation under Oriented Bounding Box Annotations](https://arxiv.org/abs/2607.06007)

**<font color=#1a73e8>作者：</font>** Jun Wei, Xinchang Liu, Yu Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pixel-level annotation remains a major bottleneck in medical image segmentation, making weak supervision an attractive yet under-constrained alternative. We propose OBBSeg, an intermediate supervision paradigm guided by Oriented Bounding Boxes (OBBs) that bridges the gap between full and weak supervision. By jointly encoding spatial extent and orientation, OBBs provide compact geometric supervision that better aligns with elongated or anisotropic lesions, reducing the ambiguity of coarse box annotations. To mitigate the inherent rectangular bias of OBBs, we introduce a Mask-to-OBB loss, a differentiable formulation that enforces geometric consistency between predicted masks and OBB regions. Furthermore, we incorporate prompt-driven semantic guidance through two complementary modules-PAFE and DBFE-which enhance foreground representation and suppress background interference. Extensive experiments on 13 datasets across 5 imaging modalities show that OBBSeg not only outperforms existing weakly supervised methods but also achieves performance comparable to fully supervised approaches, demonstrating its potential for efficient and scalable medical image segmentation. The code is available at this https URL.

---


### 105. [Stability Annealing Selects the Implicit Bias of Smoothed Sign Descent: A Rate-Indexed Barrier Path on Separable Data](https://arxiv.org/abs/2607.06013)

**<font color=#1a73e8>作者：</font>** Xiangwu Wang, Chengwei Cao, Yicheng Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Adaptive gradient methods can favor max-margin separators that differ from gradient descent, yet a fixed positive numerical stability constant eventually changes the update geometry again. This paper studies the rate-controlled middle case for full-batch linear classification on separable data. For memoryless stability-annealed smoothed-sign descent with weighted exponential loss, we prove that the normalized iterates converge to the minimizer of a convex Burg-type barrier over a margin slice. The proof rewrites the dynamics exactly as entropic mirror ascent on a concave dual objective, controls the dual gap by a KL recursion, and yields an explicit S_t^{-1/2} normalized-iterate envelope. The static barrier geometry is fully characterized, including KKT conditions and both endpoint limits. Experiments validate the exact dual identities to floating-point error, illustrate the predicted path and rate diagram, and show an empirical fixed-epsilon crossover scaling in cumulative time. We further report robustness and boundary diagnostics for logistic tails, fixed-epsilon crossover, and adaptive-method variants, delineating the scope of the proved smoothed-sign theory.

---


### 106. [Learning When to Automate: Queue Control in Human-AI Service Systems](https://arxiv.org/abs/2607.06017)

**<font color=#1a73e8>作者：</font>** Giovanni Montanari, Marco Scarsini, Vianney Perchet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study a human-AI service system in which tasks arrive sequentially and are processed through a two-stage architecture: an automated chatbot followed, when necessary, by a human agent. We consider $T$ sequentially arriving tasks, each belonging to one of $K$ heterogeneous types. For each task the decision maker chooses how many resources to allocate to the chatbot, whose type-dependent success probabilities are initially unknown. Tasks not resolved by the chatbot enter type-dependent human-service queues, where they are processed by a human agent with unknown service rates. This model captures a central tradeoff in hybrid service systems: relying more on automation reduces human congestion but increases chatbot costs, while insufficient automation may overload the human agent. We propose the UCB-DPP policy, which combines Upper Confidence Bounds with Drift-Plus-Penalty control to learn the unknown parameters of the system while making queue-aware decisions. We prove that UCB-DPP achieves regret $\widetilde{\mathcal{O}}(K\sqrt{T})$ and guarantees mean-rate stability of the human-service queues. Simulations on synthetic instances show that the proposed policy outperforms natural baselines.

---


### 107. [KOAL: Knowledge-Driven Prostate Cancer Grading with Ordinal-Aware Learning](https://arxiv.org/abs/2607.06019)

**<font color=#1a73e8>作者：</font>** Zheng Guo, Jiaqi Cui, Haocheng Xiong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Non-invasive prediction of Gleason Grade Group (GGG) in prostate cancer using multiparametric MRI (mpMRI) is clinically vital for reducing unnecessary biopsies. Existing GGG prediction methods face two major limitations. First, they often overlook non-image information critical for GGG prediction, including age, prostate-specific antigen (PSA), and expert priors embedded in radiology reports. Second, they tend to oversimplify GGG as flat categorical labels, failing to account for its intrinsic hierarchy of primary and secondary Gleason patterns. To this end, we propose a novel Knowledge-Driven Ordinal-Aware Learning (KOAL) framework with three synergistic modules. Specifically, the Clinical-Context Modulation (CCM) module uses clinical variables (e.g., age and PSA) to dynamically modulate discriminative image representations. The Knowledge-Guided Prototype Alignment (KGPA) module leverages an LLM to extract group-specific expert knowledge from training radiology reports and clinical guidelines, producing offline semantic anchors describing grade-specific radiological findings without requiring patient-specific reports at inference. Through prototype contrastive alignment, patient-specific mpMRI representations are matched with these anchors to promote pathology-aligned representation learning. The Hierarchical Ordinal-aware Constraints (HOC) module decouples primary and secondary Gleason pattern prediction and maps their probabilistic outputs to GGG via a Differentiable Bio-logic Mapping Layer (DBML), ensuring pathological grading consistency. Experiments on public PI-CAI and in-house datasets demonstrate that KOAL outperforms state-of-the-art methods. Code is available at: this https URL.

---


### 108. [Why does Deep Learning Improve Visual SLAM?](https://arxiv.org/abs/2607.06023)

**<font color=#1a73e8>作者：</font>** Giovanni Cioffi, Davide Scaramuzza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual SLAM is a well-established technology utilized in a wide range of real-world applications. However, its performance still degrades under challenging visual conditions, such as low texture, severe motion blur, and poor illumination. Systems based on deep learning outperform classical geometry-based ones and achieve state-of-the-art results by combining learned 2D data association and uncertainty with differentiable geometric optimization in recurrent architectures. Still, it remains unclear exactly which components are fundamentally responsible for this success. In this paper, we ask: Is the superior performance of deep learning-based systems driven primarily by learned 2D data association, the combination of learned 2D data association and uncertainty, or the recurrent architecture itself? We investigate this question empirically by conducting a controlled study. Our findings reveal that the success of DL-based V-SLAM systems hinges on learned 2D data association and uncertainty rather than their recurrent architecture, underscoring the necessity of learning-based paradigms for the design of these components. Upon acceptance, the code will be released as open source.

---


### 109. [SplineNet: An Isogeometric Deep Learning Method for Complex Shells](https://arxiv.org/abs/2607.06026)

**<font color=#1a73e8>作者：</font>** Shizhou Luo, Xiaodong Wei  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present a novel isogeometric deep learning method, termed SplineNet, for the seamless design and analysis of shell structures with complex geometries. The proposed approach is built upon watertight spline representations, e.g., analysis-suitable unstructured T-splines, and features exact geometric descriptions of Computer-Aided Design (CAD) models in neural networks. Bézier extraction is used to build the network architecture, where Bernstein polynomials serve as the nonlinear activation functions. SplineNet can be applied in a data-free or data-driven way. In the data-free case, energy-based formulations can be naturally incorporated as loss terms, which fulfill the need of Computer-Aided Engineering (CAE) and can be accurately calculated. In particular, the Kirchhoff--Love (KL) model is adopted to solve for the mechanical behaviors of shell structures. This way, CAD and CAE can be tightly integrated in a deep neural network without the time-consuming model/data exchange process. In the data-driven case, SplineNet can be used as the trunk net of Deep Operator Networks (DeepONet) to provide interpretability. Given such a trained network and unseen input data, results can be immediately obtained without retraining the network or repeatedly performing the traditional workflow for analysis. In the end, a variety of numerical examples are studied to demonstrate the effectiveness of the proposed method, especially when real-world complex geometries are involved.

---


### 110. [REAN: Reconstruction-aware ECG Anonymization Based on Privacy--Utility Orthogonality](https://arxiv.org/abs/2607.06037)

**<font color=#1a73e8>作者：</font>** Taerin Ki, Sunghwan Park, Junyoung Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> A shared electrocardiogram (ECG) is itself a biometric fingerprint that can re-identify a patient and reveal personal information. Recent ECG anonymizers transform the signal before sharing to reduce privacy leakage. However, existing methods still face a privacy--utility trade-off, in which preserving privacy often compromises utility while preserving utility reveals personal information. We propose \emph{REAN} (\emph{RE}construction-aware ECG \emph{AN}onymizer), a raw ECG signal anonymizer, to address this privacy--utility trade-off. REAN reconstructs the signal using a 1-D U-Net trained with losses from frozen privacy and utility classifiers to reduce privacy leakage while preserving utility. The privacy and utility gradients are near-orthogonal ($\approx$93.8$^\circ$), so reducing privacy leakage leaves utility almost unchanged. On four public PhysioNet databases, REAN achieves the strongest privacy--utility balance among raw ECG signal baselines. It drives re-identification to chance (0.96$\to$0.00), keeps arrhythmia macro-AUROC at the clean level (Clean 0.9982 vs.\ REAN 0.9991), and maintains re-identification protection under unseen privacy-classifier architectures.

---


### 111. [Nested Episodic State Topology (NEST): A Graph-Theoretic Architecture of Cognitive States](https://arxiv.org/abs/2607.06055)

**<font color=#1a73e8>作者：</font>** Ishant  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present NEST (Nested Episodic State Topology), a foundational graph-theoretic representational ontology for modeling cognition as structured state formation and transformation rather than as a finished empirical model. Concepts, episodes, percepts, and task contexts are represented as typed, weighted graphs whose nodes may carry internal subgraph payloads; edges are typed under six relation classes -- causal, containment, temporal, associative, evidential, and spatial. Durable belief graphs are separated from capacity-limited working-memory graphs that may host transient non-belief content. WM-belief grounding, conflict catalogs, and belief-update operators specify how transient structure is tested against stored knowledge and how belief is revised. A reusable operator toolkit -- activation, graph-property functionals, working-memory transitions, awareness and trajectory functionals, and belief update -- organizes the formal core. Derived diagnostics such as fragmentation, involvement, signed evaluation, coherence, and active conflict define familiar phenomena in the same ontology; self-related processing is modeled through designated self-image subgraphs within belief. Subsequent sections instantiate this core without new primitives: phenomena signatures, a task-instantiation schema for action selection and failure modes, and compatibility mappings that embed ACT-R, Soar, Sigma, the Common Model of Cognition, Global Workspace Theory, semantic networks, Theory-Theory, and chunking as constrained regions of one language. Mappings constitute the culminating technical section; discussion addresses scope, limitations, and open research directions. The contribution is intentionally foundational: a transparent representational substrate for later empirical, computational, and domain-specific work.

---


### 112. [Reward-Density Heuristic for Dynamic Multi-Vehicle Routing: Performance and Computational Efficiency](https://arxiv.org/abs/2607.06066)

**<font color=#1a73e8>作者：</font>** Manish Kolachalam, Rani Malhotra  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The Vehicle Routing Problem (VRP) and its variants represent some of the most practically consequential optimization challenges in modern logistics and urban mobility. In this study, we address a dynamic, online variant combining elements of the VRP and the Orienteering Problem (OP), in which a fleet of vehicles must maximise cumulative reward collected within a fixed time horizon while continuously replanning as new tasks arrive. We propose and evaluate a reward-density heuristic for dynamic multi-vehicle assignment, referred to as the Efficiency heuristic. We evaluate this formulation across two application domains: autonomous drone task allocation and urban taxi dispatch, across multiple fleet sizes and task scales. The proposed method is compared with four classical construction heuristics and three metaheuristic algorithms (Adaptive Large Neighbourhood Search, Genetic Algorithm, and Simulated Annealing), all evaluated under identical conditions. Across all tested configurations, the Efficiency heuristic matches the solution quality of the best metaheuristic algorithms while requiring two to three orders of magnitude less planning time, establishing Pareto dominance over all competing methods on the reward-versus-compute frontier. These findings suggest a practical design principle for real-time allocation and dispatch systems: in dynamic, time-constrained routing environments, carefully designed greedy heuristics can match the output of sophisticated search procedures at a fraction of the computational cost, making them preferable for online deployment.

---


### 113. [Designing Computerized Gait Analysis for Pediatric Care: Clinician Perspectives on Sensing, Workflow, and Care Environments](https://arxiv.org/abs/2607.06076)

**<font color=#1a73e8>作者：</font>** Elizabeth Hong, Andrea Green, Ge Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Computerized gait analysis (CGA) serves as an essential diagnostic tool for evaluating neuromuscular, musculoskeletal, and neurological disorders in children, from cerebral palsy to muscular dystrophy. By enabling objective and comprehensive gait analysis, CGA supports timely clinical interventions that can significantly improve pediatric mobility outcomes and quality of life. Yet pediatric gait analysis introduces unique design considerations often underexplored in existing CGA research, as children's ongoing development shapes assessment requirements. To understand how CGA technologies can be designed for pediatric care, we conducted a qualitative study with 12 pediatric clinicians and one system designer who routinely work with CGA. Participants identified child-specific challenges including managing heightened sensory sensitivities to wearable devices, accommodating body proportions in sensor placement and calibration, and maintaining patient engagement during data collection. Clinicians also articulated needs for workflow adaptations and expressed interest in extending gait analysis beyond controlled laboratory settings into naturalistic environments such as playgrounds and schools, where children's authentic movement patterns emerge. Drawing from these clinician perspectives, we present design recommendations for pediatric-centered CGA that address sensing modalities suitable for sensory-sensitive children and approaches for capturing gait data across diverse care environments. Our findings contribute to the broader challenge of adapting clinical technologies to meet the distinct needs of pediatric populations.

---


### 114. [Scalable Perturbation Learning for Online Self-Supervised Echo State Networks](https://arxiv.org/abs/2607.06079)

**<font color=#1a73e8>作者：</font>** Taiki Yamada, Kantaro Fujiwara  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Intelligent systems should not only solve tasks but also adapt under real-world constraints. Autonomous adaptation via self-supervised learning, sequential adaptation via online learning, and memory-efficient implementation via perturbation-based learning are important requirements for such systems. However, these requirements are generally in tension for high-dimensional systems, because perturbation-based learning suffers from variance that grows with the dimension of the perturbed variables.
In this study, we focus on echo state networks (ESNs), where this tension naturally arises in large reservoirs. We propose a perturbation-based learning rule for online self-supervised learning in ESNs. The proposed rule is derived from an orthogonal decomposition of the self-supervised learning cost, which separates an input-dependent component from a redundant component determined by the fixed ESN parameters. By perturbing only the input-dependent component, the effective perturbation dimension is reduced from the reservoir dimension to the input dimension.
Thus, the proposed method preserves self-supervised adaptation, online learning, and scalar-feedback perturbation learning, while avoiding reservoir-size-dependent variance growth. This suggests a design principle for scalable and hardware-compatible learning: online learning should be restricted to the dynamically necessary low-dimensional component of the objective.

---


### 115. [MSA-DCNN: A Data-Efficient Multi-Scale Deformable CNN for Medical Image Classification](https://arxiv.org/abs/2607.06083)

**<font color=#1a73e8>作者：</font>** Hamza Hussaini, Shahana Bano, Eyad Elyan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing deep learning methods perform well in medical image classification but struggle with multi-scale morphology and limited annotations due to fixed sampling and data-hungry training. Existing approaches address these challenges in isolation: DCN-based models provide adaptive sampling but lack explicit multi-scale attention fusion and label-efficient regularisation; multi-scale architectures typically rely on static fusion; and semi-supervised methods target label scarcity without jointly modelling adaptive cross-scale representations. We propose MSA-DCNN, a scale-consistent deformable attention learning framework that introduces adaptive multi-scale sampling, within-scale saliency refinement, learned cross-scale fusion, and auxiliary self-distillation within a unified optimisation scheme, with potential to generalise to structurally heterogeneous anatomy. We evaluate on three public benchmarks and an external hold-out set for leukaemia. MSA-DCNN demonstrates competitive and often better performance against ViT baselines, CNN baselines, and a MICCAI semi-supervised baseline under distribution shift and label scarcity in accuracy, F1, and AUC (binary), while using fewer parameters. Ablations confirm complementary component contributions, supporting MSA-DCNN as a practical foundation for data-efficient medical image classification.

---


### 116. [PVCap: Towards Accurate 3D Dense Captioning via PseudoCap and VoxelCapNet](https://arxiv.org/abs/2607.06097)

**<font color=#1a73e8>作者：</font>** Xiaopei Wu, Chenshu Hou, Liang Peng 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D dense captioning, an emerging vision-language task, aims to generate descriptive sentences for each object in the 3D scene. Despite the impressive results achieved by previous methods, they suffer from two limitations. First, current research often employs global rigid transformations, such as rotation, to augment scenes without changing their spatial layouts. However, diverse spatial layouts are crucial for training a 3D dense captioning model to describe spatial relations between objects. Second, previous works mainly focus on the design of the caption generation pipeline while utilizing a simple network architecture for other components, i.e., backbone and detection head, which is crucial for extracting rich semantic information for captioning. In this paper, we propose PVCap to alleviate the aforementioned problems. Our PVCap consists of PseudoCap and VoxelCapNet. Specifically, PseudoCap employs a random mixing technique on instances within the dataset, generating numerous pseudo frames with diverse spatial layouts at the instance level. By utilizing a teacher-student framework, PseudoCap obtains pseudo caption labels for these pseudo frames. This data augmentation approach significantly increases the number of training samples and enhances the model's ability to describe the environment effectively. Regarding VoxelCapNet, we introduce a robust caption network that utilizes voxel features and adapts the caption head to the voxel-based network architecture. Our VoxelCapNet can serve as a competitive baseline for future research on 3D dense captioning. Extensive experiments are conducted on two prevalent benchmarks, i.e., ScanRefer and Nr3D. Notably, our method surpasses current state-of-the-art by 11.41% and 13.99% in CIDEr@0.5IoU, respectively. Codes will be made publicly available.

---


### 117. [EcoVision: AI-Powered Drone Imaging for Salt Marsh Vegetation Monitoring and Dominance Mapping](https://arxiv.org/abs/2607.06105)

**<font color=#1a73e8>作者：</font>** Innocent Onyenonachi, Peter J. Lawerance, Nadia Kanwal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution RGB imagery acquired from low-altitude UAV surveys was processed through a modular pipeline incorporating transformer-based semantic segmentation, connected-component vegetation extraction, fine-grained species classification using a ConvNeXt architecture, and grid-based dominance scoring at 2x2m resolution. The framework targeted two ecologically significant halophytic grasses, Spartina maritima and Puccinellia maritima, and was trained using a curated and manually annotated UAV imagery, along with biodiversity imagery sourced from publicly accessible datasets. In order to identify these plants from the imagery, our segmentation yielded reliable species masks (mean IoU = 0.56; pixel-level accuracy = 0.96), while object-level classification achieved very good discrimination (F1 = 0.99). Dominance estimates closely matched quadrat-based field surveys, with mean absolute differences below 8%, preserving fine-scale spatial structure under realistic survey conditions. The developed system, named EcoVision, establishes a practical foundation for scalable, high-resolution salt marsh monitoring, demonstrating how AI-driven workflows can translate pixel-level predictions into ecologically interpretable metrics.

---


### 118. [RoME: Robust Mixture of Low-Rank Experts against Multiple Adversarial Perturbations](https://arxiv.org/abs/2607.06109)

**<font color=#1a73e8>作者：</font>** Woo Jae Kim, Kyle Min, Suhyeon Ha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-perturbation adversarial training (MAT) aims to achieve robustness against multiple $\ell_p$ perturbations but suffers from robustness trade-offs between different threats. To address this, we employ a mixture of experts (MoE) to route different threats through distinct model pathways. However, naive application of MoE encounters two critical challenges: experts tend to overlook threat-specific features and redundantly capture features shared across threats, and gating networks suffer from threat-agnostic routing where they learn nearly identical routing patterns across threats, thus preventing the construction of threat-specific model pathways. To this end, we propose Robust Mixture of Low-Rank Experts (RoME), where each expert is a low-rank additive update to the shared backbone, allowing it to capture threat-common features while experts focus on threat-specific information. To address threat-agnostic routing, RoME introduces (i) dual-scale gating that exploits threat-discriminative signals from local and global level features, and (ii) threat-guided gating diversification that enforces diverse expert utilization across threats. Extensive experiments demonstrate that RoME outperforms existing state-of-the-art MAT in union robustness and natural accuracy and improves robustness against unseen threats. Codes are available at this https URL.

---


### 119. [x-Prediction Is All You Need:Training-Free Accelerated Generation via Endpoint Decodability](https://arxiv.org/abs/2607.06114)

**<font color=#1a73e8>作者：</font>** Xin Peng, Ang Gao  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow matching models generate high-quality samples, but their ODE samplers often need tens to hundreds of neural function evaluations (NFEs). This remains a practical challenge for released checkpoints, since many accelerators require additional design choices and training cost through retraining, distillation, or trajectory redesign. We investigate a different route based on $x$-prediction. During sampling, standard affine probability paths already expose $x_0$ information: an intermediate state and its path velocity determine a principled estimate of the clean sample. We formalize this property as \textbf{endpoint decodability} and show that the decoder is the minimum-MSE estimator $\mathbb{E}[x_0\mid x_t]$ under the usual $\ell_2$ objective. This yields \textbf{Truncated Jump Sampling} (TJS): stop the ODE at an early-exit time $t^*$ and return the decoded $x_0$. TJS requires no retraining, distillation, or architecture change. Across SDXL, SD3.5M, Z-Image-Turbo, and three class-conditional benchmarks, it reduces NFEs by 20--70\% with near-matched quality. The analysis also shows why endpoint prediction can work without straightening the trajectory, providing inference acceleration without trajectory redesign.

---


### 120. [WebRetriever: A Large-Scale Comprehensive Benchmark for Efficient Web Agent Evaluation](https://arxiv.org/abs/2607.06118)

**<font color=#1a73e8>作者：</font>** Wei Dong, Tianyu Fu, Zhe Yu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As web agents increasingly demonstrate capabilities in automated task execution, the development of robust evaluation frameworks for assessing their navigation and task completion performance has emerged as a critical research priority. However, existing benchmarks exhibit fundamental limitations. First, they suffer from insufficient scale and limited domain diversity, constraining comprehensive evaluation of cross-domain generalization. Second, prevailing LLM-as-Judge evaluation methodologies inadequately capture fine-grained interaction semantics, particularly regarding precise query formulation and filtering operations. Third, current benchmarks predominantly emphasize navigation success metrics while neglecting critical requirements for real-world deployment scenarios. To address these limitations, we introduce WebRetriever, a large-scale benchmark encompassing 800 websites and 1,550 tasks across diverse domains, including consumer, professional, and enterprise sectors, with comprehensive coverage of user intent patterns. We propose NavEval (Navigation Evaluation), a novel LLM-as-Judge framework that leverages rich interaction context beyond visual screenshots, achieving state-of-the-art alignment with human judgment across multiple evaluation datasets. Furthermore, we establish three complementary evaluation protocols that collectively provide holistic assessment of web agent capabilities: navigation proficiency, knowledge-assisted interaction, and end-to-end task completion with information extraction. Extensive experimental analysis reveals substantial performance disparities across evaluation protocols, demonstrating that navigation success alone is an insufficient predictor of real-world application effectiveness. WebRetriever delivers fine-grained diagnostic insights into agent capabilities and establishes a rigorous foundation for advancing web agent research and development.

---


### 121. [AEGIS: A Mechanism-Guided Defense against Visual Synonym Jailbreaks in Text-to-Image Models](https://arxiv.org/abs/2607.06120)

**<font color=#1a73e8>作者：</font>** Yuanmin Huang, Zhenfei Zhang, Mi Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-to-image diffusion models have achieved high visual fidelity and broad adoption, but remain vulnerable to safety violations when adversaries exploit them to synthesize illicit content. Existing alignment paradigms, from input sanitization to structural feature pruning, are largely organized around unsafe concepts explicitly exposed during filtering, editing, or localization. This leaves a blind spot for visual synonym attacks (VSA), a jailbreak where benign-looking prompts elicit prohibited imagery through implicit visual associations. As a result, current defenses face a safety-utility dilemma: they may either under-mitigate VSA threats or over-suppress visually similar benign concepts. The core challenge is that VSA hides the unsafe target at the textual surface while revealing it through generation-time visual-semantic convergence. In this work, we therefore shift from static suppression of pre-specified unsafe concepts to dynamic tracing of how unsafe semantics emerge during generation. Our mechanistic analysis shows that VSA and explicit unsafe prompts converge through sparse semantic-injecting attention heads, which serve as inference-time bottlenecks for prohibited visual semantics. Based on this insight, we propose AEGIS (Adaptive Evasion Guard via Identification and Steering), an inference-time defense that applies similarity-aware repulsion only at the identified vulnerable heads. Evaluated against 16 baselines, AEGIS improves both safety and utility. On SD 1.4, it reduces ASR to $\mathbf{0.00}/\mathbf{0.03}$ for in-domain violence/nudity VSA and achieves ASRs $\le \mathbf{0.09}$ on out-of-domain explicit and adversarial attacks. It preserves benign fidelity, avoids suppressing hard-negative concepts, and transfers to SD 2.1 and FLUX.1 after re-identifying the critical heads for each backbone.

---


### 122. [Self-Supervised Implicit CEST Reconstruction via Physics-Informed Lorentz Encoding](https://arxiv.org/abs/2607.06132)

**<font color=#1a73e8>作者：</font>** Dexuan Li, Yupeng Wu, Chenglong Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Pool Chemical Exchange Saturation Transfer (CEST) MRI provides valuable metabolic information but is clinically limited by long acquisition times. Although sparse sampling reduces scanning time, reconstructing high-resolution Z-spectra from limited data remains an ill-posed inverse problem. Conventional interpolation and generic Implicit Neural Rep-resentations (INRs) often lack physical constraints, leading to spectral artifacts and physically invalid signals. To address this, we propose Lorentz Encoding (LE), a physics-informed framework that formulates CEST reconstruction as a self-supervised reconstruction task via implicit continuous coordinate learning. Unlike generic positional encodings, LE regularizes the continuous spectral mapping by projecting sparse coordinates into a physically constrained space governed by a combination of parametric Lorentzian profiles with learnable basis functions. This mechanism effectively reduces noise and enforces consistency with physical models. Experiments on in vivo human brain data demonstrate that LE significantly outperforms state-of-the-art methods. Specifically, under a 39-point sampling strategy, LE achieves a PSNR of 57.58 dB and an SSIM of 0.9994. Furthermore, the learned physics-informed encodings form a continuous, geometrically ordered trajectory in the latent space, ensuring accurate quantitative metabo-lite mapping (APT, NOE, MT).

---


### 123. [Poster: Mind the Gap -- Characterizing the Temporal Blind Spot Between GSB and DNS Resolution](https://arxiv.org/abs/2607.06134)

**<font color=#1a73e8>作者：</font>** Tomer Gal, Fujiao Ji, Doowon Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Google Safe Browsing (GSB) and DNS resolution operate concurrently during browser navigation, yet their packet-level synchronization remains understudied. This work characterizes the timing gap (\(\Delta_{time}\)) between GSB-related query close events and parallel DNS resolution responses, identifying a consistent temporal offset with potential security relevance. Using packet-capture analysis across general and CNAME-domain datasets, we observe positive timing gaps in approximately 79\% of measurements. In these instances, DNS responses lag behind GSB-related query closures with median delays of 67-79 ms and maximum delays surpassing 2,400 ms. These empirical results highlight a measurable window within the browsing workflow. We suggest that such temporal inconsistencies, particularly in complex CNAME-domain resolutions, may create a security-relevant timing precondition under DNS-manipulation threat models. These results provide a foundation for further research into timing-based risks and mitigations in browser safety mechanisms.

---


### 124. [Tuning-Free Latent Diffusion Models for Ultrahigh-Resolution Image Editing](https://arxiv.org/abs/2607.06136)

**<font color=#1a73e8>作者：</font>** Wanglong Lu, Lingming Su, Kaijie Shi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent diffusion-based generative models have shown impressive performance in image generation and editing. However, due to memory limitations and the high cost of collecting high-resolution training images, existing methods are typically restricted to inputs with linear resolutions below 1K. In contrast, photos captured by modern mobile devices often reach linear resolutions up to 8K, revealing a significant gap between current capabilities and real-world demands. Simply upscaling low-resolution edited results often results in visually enlarged but blurry images that lack fine details. This paper introduces UltraDiffEdit, a novel, tuning-free image editing framework that extends off-the-shelf latent diffusion models (LDMs) to ultrahigh resolutions. UltraDiffEdit employs a multi-scale progressive editing strategy, iteratively blending high-resolution edited content with unedited areas in a coarse-to-fine manner. We employ multi-patch encoding to preserve both edited and unedited visual details within the latent space. To mitigate editing artifacts, our global-local consistency denoising technique consistently integrates edited and unedited latent features, ensuring smooth transition at editing boundaries from the latent representation to the final image. We also introduce a patch-based hybrid sampling approach that captures local, intermediate, and global features, ensuring semantic coherence and enhancing fine detail during denoising. We conduct extensive experiments demonstrating UltraDiffEdit's superior editing quality and flexibility: it can handle image resolutions up to 8K using only a single NVIDIA GeForce RTX 3090 GPU. The source code is publicly available at this https URL.

---


### 125. [The Masks We (Think We) Wear: Privacy Threats of Browser-Extension Wallets in the Web3 Ecosystem](https://arxiv.org/abs/2607.06141)

**<font color=#1a73e8>作者：</font>** Weihong Wang, Yana Dimova, Victor Vansteenkiste 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptocurrency wallets are the primary interface for managing pseudonymous blockchain addresses, viewing balances, and interacting with Web3 applications. Although users typically assume that their addresses remain independent of each other unless intentionally revealed, modern wallets routinely communicate with both blockchain infrastructure and decentralized applications (dApps), generating network-side and web-side signals that may undermine this assumption.
In this paper, we identify and formalize five privacy threats that arise directly from wallets interacting with the network and the web browser. Using large-scale dynamic measurements of 85 of the most popular Chrome Web Store browser-extension wallets (representing 35.16 million users), we observe that routine remote procedure call (RPC) operations leak structural links between a user's addresses; that the majority of Ethereum wallets implement permission revocation inconsistently and continue to expose previously revoked addresses across sessions; and that many wallets inject their provider interfaces into cross-origin iframes, enabling passive cross-site tracking beyond dApps and potentially real-world identity deanonymization without user interaction.
Taken together, our results show that these wallet behaviors leak sensitive information that can be used to link multiple addresses to the same user, track wallet users across sessions and sites, and connect their browsing activity to their on-chain wealth.
We discuss practical mitigations and show that many of these threats can be substantially reduced through improved wallet implementation, stronger privacy considerations in ecosystem standards, and stricter controls over provider exposure. Our results highlight the need for standardized, privacy-preserving wallet architectures.

---


### 126. [RFHNet: Relational and Frequency-Aware Hashing Network for Large-Scale Fine-Grained Food Image Retrieval](https://arxiv.org/abs/2607.06148)

**<font color=#1a73e8>作者：</font>** Junsong Wang, Weiqing Min, Guorui Sheng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained food image retrieval is a key task in computational gastronomy, with applications in food traceability, dietary monitoring, and smart catering systems. Although hashing-based retrieval is attractive for large-scale search due to its storage efficiency and fast Hamming-distance computation, existing methods often perform poorly in fine-grained food scenarios, where subtle local semantics and frequency-sensitive visual cues are essential. To address this challenge, we propose RFHNet, a cascaded hierarchical hashing network that captures both global structure and fine-grained local details through multi-level representations. RFHNet includes three components: (1) Fine-grained Relation Modeling (FRM) to capture subtle visual differences among similar food components; (2) Multi-Frequency Modulated Fusion (MFMF) to extract informative multi-frequency features; and (3) Hierarchical Semantic Synergy (HSS) to adaptively integrate multi-level representations and generate discriminative hash codes. Experiments on six food-specific benchmarks show that RFHNet consistently outperforms state-of-the-art hashing methods, with mAP gains of 4.44\% to 17.20\% at 12 bits. These results validate the effectiveness of RFHNet for large-scale visual food retrieval and smart catering applications. The source code will be released upon publication.

---


### 127. [BlossomPsy: A User-Centric AI System for Adaptive and Engaging MBTI Personality Assessments](https://arxiv.org/abs/2607.06149)

**<font color=#1a73e8>作者：</font>** Bingjia Huang  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> There has been growing public interest in understanding personality traits and emotional characteristics, as such knowledge helps individuals better accept themselves and manage negative emotions. While professional personality scales remain the standard tool for assessment, they are often perceived as tedious or inaccessible to the general public. AI-driven systems can make assessments more accessible, but it is difficult to balance user engagement with predictive consistency in existing works. We tackle this challenge by introducing BlossomPsy, a user-friendly AI-driven MBTI assessment system. MBTI, a widely recognized but psychometrically debated personality framework, serves as the foundation for many recent systems. BlossomPsy integrates multi-turn dialogue and photo-based questions to enhance user engagement while supporting confidence-aware predictions. By combining deep learning, multi-armed bandit algorithms, and control theory, the system dynamically adapts to users' responses. In particular, photo-based questions are designed to increase interactivity and provide additional user information, thereby improving prediction confidence. Experiments involving both human volunteers and large language models (LLMs) provide preliminary evidence that BlossomPsy can produce stable predictions, with higher reported user satisfaction compared to MBTI-M (Chinese version), while maintaining comparable consistency with the reference scale.

---


### 128. [Enhanced Seam Segmentation for Automated Welding Robot in Construction Through Transfer Learning: Addressing Limitations of Bilateral Segmentation Network](https://arxiv.org/abs/2607.06150)

**<font color=#1a73e8>作者：</font>** Keonvin Park, Yong Ann Voeurn, Hyeokjun Kweon 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable seam segmentation is essential for autonomous robotic welding in construction, where harsh illumination, specular reflections, and thin weld geometries often degrade segmentation performance. This study proposes a reflection-robust seam segmentation framework that enhances a BiSeNetV2 backbone through transfer learning and a hybrid Cross-Entropy--Lovász loss. Rather than increasing architectural complexity, the proposed framework improves reflection robustness through learning-stability-oriented optimization. Experimental results show that the proposed method achieves 81.76\% Joint IoU and 90.73\% mIoU, improving Joint IoU by +22.36 percentage points over the OHEM-based baseline while maintaining identical FLOPs, parameter count, and inference speed. The proposed approach also recovers 96.33\% of severe zero-IoU failure cases under reflective conditions. Comparative experiments across BiSeNetV2, DeepLabV3+, UNet, and SegFormer further demonstrate that the proposed optimization strategy is particularly effective for lightweight real-time segmentation architectures. Qualitative analyses additionally show improved seam continuity and reflection robustness in challenging welding environments. These findings suggest that the proposed framework provides a practical and lightweight perception solution for robotic welding applications involving reflective metallic surfaces.

---


### 129. [High-Resolution Artwork Outpainting with Global Blueprint Guidance and Layout Control](https://arxiv.org/abs/2607.06162)

**<font color=#1a73e8>作者：</font>** Junha Kim, Hyunjoon Park, Donghyeon Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image outpainting extends an image beyond its original borders, requiring seamless style integration and globally coherent scene completion. Building on the success of diffusion models, recent methods have achieved substantial improvements in visual quality. In practice, however, high-resolution outpainting is commonly performed via progressive expansion around a fixed source image, particularly in artwork scenarios. Despite this progress, existing approaches still suffer from three key limitations: (i) the absence of a reliable global planning mechanism, which leads to structural instability and error accumulation at high resolutions; (ii) limited spatial controllability beyond text prompts, making it difficult to place objects at user-specified locations; and (iii) high inference latency caused by inherently sequential patch generation. To address these issues, we propose a global blueprint-guided two-stage diffusion framework for layout-controllable high-resolution outpainting with efficient parallel synthesis. In Stage 1, we generate a low-resolution global blueprint using a layout adapter that injects bounding-box conditions into a Stable Diffusion inpainting backbone, producing a globally consistent structural plan while extracting global guidance features. In Stage 2, we synthesize high-resolution local patches in parallel by injecting the blueprint-derived global guidance and initializing each patch from the blueprint using the low-frequency preservation property of forward diffusion. This design eliminates sequential dependency while maintaining global coherence. Extensive experiments on large-scale artwork datasets demonstrate improved visual fidelity, stronger semantic consistency, and substantially reduced inference time compared to prior baselines, while uniquely supporting explicit layout control for artwork outpainting.

---


### 130. [When do prophets profit in prediction markets?](https://arxiv.org/abs/2607.06166)

**<font color=#1a73e8>作者：</font>** Anri Gu, Nicole Kagan, Alec Sun 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prediction markets aggregate dispersed beliefs into prices that act as probabilistic forecasts of uncertain events. Classical theory establishes a clean equivalence between forecasting accuracy and trading profit, but only for the specific automated market maker (AMM) design. However, the largest exchanges today are based on central limit order books in which informed forecasters routinely lose money while uninformed strategies can profit on simple heuristics. We resolve this discrepancy by establishing a formal equivalence between predictive accuracy and profitability. For any strictly proper scoring rule $S$, we exhibit a "proper" betting strategy that depends only on the forecaster's prediction $\mathbf{p}$ and the market price $\mathbf{q}$, and earns positive expected profit whenever $\mathbf{p}$ outperforms $\mathbf{q}$ under $S$ and the market has sufficient liquidity. Moreover, this proper betting is essentially the only strategy with such robust profitability guarantee. The proof rests on a decomposition of expected profit that strictly generalizes the classical AMM guarantee and also explains how strategies can profit without an accuracy edge. Empirically, across thousands of forecasts by AI models, proper betting is the only strategy that reliably converts accuracy into profit, and we further identify systematic forecasting personas and show how the optimal proper strategy varies across them. A month-long live deployment on Kalshi achieves $+80.33\%$ return on investment with a Sharpe ratio of $3.35$.

---


### 131. [MobileWan: Closing the Quality Gap for Mobile Video Diffusion](https://arxiv.org/abs/2607.06173)

**<font color=#1a73e8>作者：</font>** Mohsen Ghafoorian, Denis Korzhenkov, Adil Karjauv 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in video diffusion have been driven by scaling transformer-based architectures to billions of parameters, substantially improving visual fidelity and motion coherence. In contrast, existing mobile video diffusion models remain limited to relatively small parameter budgets, typically 0.4-1.8B, restricting generation quality. In this work, we show that high-quality mobile video generation does not require small models. Instead, we demonstrate that a server-scale 5B-parameter video diffusion transformer can be deployed efficiently on memory-constrained mobile hardware through recurrent reformulation and structured compression. Starting from Wan2.2-5B, we rely on a recurrence distillation framework that converts video generation into a chunk-wise autoregressive process with constant-memory attention computation. Combined with causal linear attention, the model operates as an RNN at inference time while preserving temporal coherence across chunks. We further propose a learnable attention head pruning method based on binary per-head gates optimized end-to-end using a noise-biased sparsity objective and distillation-based finetuning. Together with sampling-step distillation and memory-optimized VAE decoding, MobileWan becomes the first 5B-scale video diffusion model deployable on a commercial mobile device. Our system generates 5-second 480x832 videos at 16 FPS in 20 seconds end-to-end latency, achieving a VBench score of 83.79 and establishing a new state of the art in mobile video generation. Project page: this https URL

---


### 132. [Revisiting Scene Graph Generation from the Perspective of Detector-Conditioned Reachability](https://arxiv.org/abs/2607.06176)

**<font color=#1a73e8>作者：</font>** Runfeng Qu, Pia K Bideau, Ole Hall 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scene graph generation (SGG) approaches can be broadly classified into detector-based and query-based methods according to their underlying reasoning mechanisms. However, the discrepancy in their predictive behaviors, induced by these distinct mechanisms, has not been systematically analyzed. In this work, we design a controlled experimental setup to examine prediction discrepancies from the perspective of detector-conditioned reachability. The results suggest clear complementary clues. Motivated by this observation, we introduce a Dual-SGG method that consolidates both reasoning mechanisms via a dual-query design, thereby leveraging the complementary predictive behaviors of both detector-based and query-based methods. Extensive experiments on the Visual Genome, Open Images v6, and GQA-200 datasets demonstrate the effectiveness of the proposed method.

---


### 133. [Claimed or Attested? A Commit-Signature Dataset and Identity Trust Tiers across the World of Code](https://arxiv.org/abs/2607.06194)

**<font color=#1a73e8>作者：</font>** Audris Mockus  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An author string in a git commit is free text the committer typed, so identity resolution over a global commit corpus rests on a claim that nothing in the commit verifies. A cryptographically signed commit is different: it binds the commit to a key the committer controls, and when that key ties back to a real-world identity the git identity becomes attested rather than merely claimed. We release the first commit-signature axis for the World of Code (WoC), extracted for the V2604 collection. The signature travels in the commit object's gpgsig header and is already carried, unparsed, in the commit-message field of the WoC commit tables, so the axis is a scan over existing tables rather than a re-read of the object database. Over the V2604 corpus of 5,866,595,698 commits, 17.59% carry a signature (PGP dominant at 98.96%, with a growing minority of SSH and X.509/sigstore signatures), or 1,031,721,316 signed commits. We release the per-commit signature map c2sigFull, a key-to-author graph gated so that shared organization and continuous-integration keys are separated from person keys, and A2trust, a per-identity attestation tier (unsigned, signed, real-world-bound, cross-corpus attested) that extends the published A2cls identity-class dataset. The signature axis is a precision anchor, not a coverage layer: signed commits skew toward recent and security-conscious developers, a population that overlaps the scholarly authors a bibliography join targets. We use the person keys to build a cryptographically grounded alias gold that calibrates the heuristic WoC alias map independently of hand-labeled pairs, and to attach an attestation provenance to science-to-software identity links. All artifacts are released as a self-contained, in dependently hosted replication package keyed to the WoC V2604 collection.

---


### 134. [FDIFormer:Protocol-Aware Transformer Learning for False Data Injection Attack Detection in Smart Grid Networks](https://arxiv.org/abs/2607.06213)

**<font color=#1a73e8>作者：</font>** Sandara Sathsarani Wijethunga, Muneeb Ul Hassan, Nasrin Sohrabi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Smart grids use communication networks and intelligent electronic devices for reliable, automated power system operation. As these systems become more interconnected, they are increasingly exposed to cyberattacks such as message tampering, false command injection, and denial-of-service attacks. A particularly concerning threat is False Data Injection (FDI), where attackers manipulate communication messages by deleting, modifying, or adding packets. This is especially critical in IEC 61850-based substations, where Generic Object-Oriented Substation Event (GOOSE) messages deliver time-critical protection and control information between devices. Detecting FDI attacks in IEC 61850 GOOSE traffic is challenging because malicious packets closely resemble legitimate communication, and many existing detection methods depend heavily on manually engineered protocol features requiring extensive domain knowledge and limited generalisability. This paper proposes FDIFormer, a feature-engineering-free framework for FDI attack detection using structured textual representations of GOOSE packet sequences and fine-tuned pre-trained Transformer models. The framework converts protocol packets into structured text windows that capture communication behaviour, enabling Transformer models to learn attack-related patterns directly from the data. Evaluated on the QUT-ZSS-2023-GOOSE dataset under a scenario-level three-fold cross-validation strategy, GraphCodeBERT achieves an MCC of 0.595 +/- 0.122, comparable to the strongest feature-engineered baseline, XGBoost (MCC = 0.604 +/- 0.121), while improving MCC by 0.133 over TF-IDF baselines. These findings show that pre-trained Transformer representations offer an effective technique for FDI attack detection in IEC 61850 GOOSE communication without relying on manually engineered protocol features.

---


### 135. [A toy framework for single and multi-agent human-AI curiosity ecosystems](https://arxiv.org/abs/2607.06214)

**<font color=#1a73e8>作者：</font>** Ilya E. Monosov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper offers a toy framework for considering curiosity as an ecosystem. First, it suggests that a single agent's inquiry policy (how, when, and why an agent asks a question) depends on how the agent values immediate uncertainty reduction, costs, delayed return, and the value of keeping the question open. A key concept in the framework is that the weights on these decision-related terms can change with experience. For example, a period of cheap, quickly answered questions may change the cost of inquiry on a short timescale and change which kinds of questions the agent is drawn to answer over a longer timescale. Second, these ideas are extended to many agents exploring a shared knowledge landscape, and there the framework tracks inquiry volume, topic diversity, frontier-directed inquiry, redundancy, and reusable knowledge. The result is a conceptual toy framework for studying curiosity ecology and for future efforts towards designing multi-agent AI systems for discovery. It serves as a companion piece for a paper currently under review in Trends in Neurosciences.

---


### 136. [EeveeDark: A Binary Neural Framework for Low-Light Video Enhancement via Event-Guided Sensor-Level Fusion](https://arxiv.org/abs/2607.06217)

**<font color=#1a73e8>作者：</font>** Onur Eker, Erkut Erdem, Aykut Erdem  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Enhancing videos under extreme low-light conditions remains challenging due to the difficulty of balancing restoration quality and computational efficiency in resource-constrained settings. This paper introduces EeveeDark, a low-light video enhancement framework that combines the spatial richness of sensor-level RAW data with the temporal precision of event streams. Central to our model is a Binary Neural Network (BNN) architecture that reduces computational overhead by quantizing weights and activations while preserving detail. EeveeDark incorporates (i) modality-specific binary encoders for processing RAW frames and event data, (ii) a lightweight fusion block for integrating spatial and temporal cues, and (iii) an event-guided skip gating mechanism for dynamic spatiotemporal refinement. Experiments on synthetic and real-world datasets show that EeveeDark outperforms prior BNN-based methods and offers a favorable performance-efficiency trade-off compared to full-precision models. The project page is available at this https URL.

---


### 137. [Spider 2.0-AIFunc: Extending Real-World Text-to-SQL to AI-Native SQL Workflows](https://arxiv.org/abs/2607.06229)

**<font color=#1a73e8>作者：</font>** Tianyang Liu, Canwen Xu, Fangyu Lei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Major cloud data platforms now expose large language model capabilities as native SQL functions, enabling analysts to perform classification, filtering, sentiment analysis, extraction, similarity search, and aggregation within ordinary SQL queries. Yet existing text-to-SQL benchmarks evaluate only conventional SQL and provide no signal on whether models can generate such AI-native SQL. We introduce Spider 2.0-AIFunc, a benchmark of 465 verified instances across 125 real-world databases covering six types of AI functions on the Snowflake platform. Starting from an existing enterprise text-to-SQL benchmark, we construct Spider 2.0-AIFunc through an agent-based pipeline that rewrites source tasks into AI-native form, simultaneously transforming target queries and refining natural language instructions to make the intended AI-native solution explicit and reduce ambiguity. All instances pass a multi-round repeated execution protocol across temporally separated windows to confirm result stability before release. Evaluating ten state-of-the-art language models, we find that the strongest proprietary models reach 67-70% execution accuracy while the best open-source model achieves 58.1%, a gap driven primarily by errors in predicate specification, schema grounding, and AI function parameterization. Agent frameworks designed for traditional text-to-SQL challenges, such as schema retrieval and relevant table selection, do not transfer effectively to AI-native SQL: a minimal agent setup consistently matches or outperforms more elaborate alternatives, suggesting that the strategies these frameworks employ are less critical in this setting. Data are available at this https URL .

---


### 138. [Demonstrating TOFFEE: A Learned System for Synthesizing Data Agent Trajectories at Scale](https://arxiv.org/abs/2607.06233)

**<font color=#1a73e8>作者：</font>** Ziting Wang, Yin Li, Zuhao Yang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-powered data agents are playing an increasingly important role in data-driven decision making. However, existing data agents struggle to generalize to unseen data environments and analytical workflows, especially in heterogeneous enterprise settings. This creates a growing need for synthesizing high-quality data agent trajectories that capture complex analytical workflows for given data environments. Such trajectories support two key downstream uses: they can serve as supervised finetuning (SFT) data that adapts data agent models to the target domain, and as in-context learning (ICL) demonstrations to guide general-purpose LLMs in unfamiliar data environments. Thus, we introduce TOFFEE, a system for synthesizing high-quality data agent trajectories from given data environments via Monte Carlo Tree Search (MCTS) with adaptive model selection and cross-task prefix reuse. We show that TOFFEE can effectively generate scalable trajectory data for complex analytical tasks across heterogeneous environments. In this demonstration, we present the system framework of TOFFEE, including its task pool construction, trajectory explorer, and learned cost model. We also introduce the web interface of TOFFEE and its workflow, and demonstrate two end-to-end scenarios: trajectory synthesis for data agent finetuning, and demonstration-augmented data agent reasoning.

---


### 139. [WING: A Window-Prior-Based Generative Network with Gated Inception for Cross-Modality CT Synthesis](https://arxiv.org/abs/2607.06234)

**<font color=#1a73e8>作者：</font>** Siyuan Mei, Yan Xia, Yipeng Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating CT volumes from MRI and CBCT can improve treatment planning in adaptive radiotherapy while avoiding additional radiation exposure. However, direct regression of CT intensities is challenged by the inherently high dynamic range and long-tailed distributions, thereby averaging out sparse yet clinically important structures. To alleviate this issue, we reformulate the regression target into multiple windowed representations, leveraging the inductive prior that CT intensities are structure-deterministic and window-separable. These windowed views exhibit smoother distributions and admit structured fusion back to the full-range CT. Building on this reformulation, we introduce WING, a WINdow-prior-based Generative network comprising: 1) a new Gated Inception Generator to produce multi-window predictions, enabling multi-shape kernel interactions to capture cross-modality correspondence; 2) a Fuse-and-Refine Transformer to aggregate the windowed outputs and learn residuals for detail refinement; and 3) a joint adversarial training objective to enhance window-conditioned realism. Extensive experiments demonstrate that our compact WING achieves state-of-the-art performance on the MRI-to-CT and CBCT-to-CT benchmarks, while supporting multi-anatomy synthesis with a single model.

---


### 140. [PhyMRI-SR: Toward Physics-Aware MRI Image Super-Resolution](https://arxiv.org/abs/2607.06238)

**<font color=#1a73e8>作者：</font>** Lihua Wei, Huatong Gao, Jia Gong 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Magnetic resonance imaging (MRI) super-resolution is vital for improving diagnostic accessibility, yet most methods treat it as a deterministic mapping from a fixed low-resolution input to a high-resolution target. This overlooks a key property of MRI acquisition physics: spatial resolution and signal-to-noise ratio (SNR) are inherently coupled, making any given low-resolution scan merely one of many possible realizations under varying acquisition trade-offs. We rethink MRI super-resolution as a physics-aware reconstruction problem, in which the goal is to identify the optimal resolution-SNR configuration and then super-resolve it to obtain high-quality MRI results. A key implication of this formulation is that MRI resolution becomes dynamic rather than fixed. To handle such resolution-heterogeneous inputs, we adapt 2D Gaussian Splatting (2D GS) to MRI by formulating reconstruction as a coordinate-based, resolution-agnostic rendering problem. To further enhance fidelity, we introduce three innovations: (1) a prior-aware Gaussian representation that combines an Anatomical Structure Prior for tissue-specific kernel initialization with an Imaging System Prior that captures hardware characteristics via a covariance dictionary; (2) a physics-constrained signal modeling scheme that predicts intrinsic tissue parameters (proton density rho and effective relaxation rate R2) and synthesizes intensities through governing physical equations, ensuring biophysically plausible contrast; and (3) a meta-learning framework that alleviates paired-data scarcity by pretraining on simulated data and adapting to real-world conditions. Extensive experiments on dynamic-resolution datasets and standard benchmarks demonstrate that our method achieves state-of-the-art performance, highlighting its strong potential for clinical deployment.

---


### 141. [VendorBench-100: A Unified Cross-Paradigm Benchmark for Deepfake Image Detection](https://arxiv.org/abs/2607.06254)

**<font color=#1a73e8>作者：</font>** Sharayu N. Deshmukh, Md Rashidunnabi, Nelton Tiago Gemo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake image detection is currently served by three fundamentally different paradigms: commercial APIs, zero-shot vision-language models (LLMs), and open-source detectors. Despite their widespread use, these paradigms are rarely evaluated under a common protocol, making direct comparison difficult. We introduce VendorBench-100, a cross-paradigm benchmark that evaluates 36 representative models using a single adversarial 100-image corpus, a unified output schema, and a common evaluation framework. To ensure reliable assessment under the corpus's intentional class imbalance, models are ranked primarily by the Matthews correlation coefficient (MCC), with ROC-AUC reported as a threshold-independent measure of ranking ability. Rather than maximizing dataset size, VendorBench-100 emphasizes challenging real-world scenarios through a curated taxonomy of eight edge-case families, including face swaps, text-to-video stills, AI photo edits, avatar compositing, opaque-provenance images, and compressed research frames. Our evaluation shows that commercial APIs achieve the strongest median performance, followed by vision LLMs and open-source detectors. However, individual open-source models remain competitive with the best vision LLMs. More importantly, we identify a consistent divergence between ranking ability (ROC-AUC) and operating-point quality (MCC), demonstrating that strong score discrimination does not necessarily produce reliable default-threshold decisions. This metric disagreement, rather than any single leaderboard ranking, is the central finding of the benchmark. We release the complete evaluation framework and benchmark results to support reproducible future research. The source code and data are available at: this https URL

---


### 142. [Early Language Learning via Spreading Activation and Category Exploration in Complex Networks](https://arxiv.org/abs/2607.06258)

**<font color=#1a73e8>作者：</font>** Salvatore Citraro  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Is word acquisition in children uneven with respect to semantic and lexical categories? To answer this question, we model early language learning as a search on a graph-based mental lexicon, driven by two interacting processes: spreading activation and an enforced exploration (rather than exploitation) of lexical categories. We evaluate model performance on four languages (German, English, Dutch, and Rioplatense Spanish), using CDIs as ground-truth data for lexical categories, normative ages derived from the Wordbank repository, and state-of-the-art resources for reconstructing graphs of word similarities. We find that spreading activation outperforms a shortest path baseline in simulating normative word acquisition. At the category level, we highlight complex transitions between CDIs. By studying their sequences in terms of burstiness and average persistence time within the same CDI, we find that spreading activation better captures the exploration dynamics observed empirically. Overall, our findings suggest that vocabulary development can be understood through the non-trivial interplay between activation dynamics and some degree of constraints regulating the visiting of lexical categories in complex networks.

---


### 143. [MAC-XA: Multi-view Anatomy-Correspondence Fusion for Coronary Stenosis Reporting from X-ray Angiography](https://arxiv.org/abs/2607.06268)

**<font color=#1a73e8>作者：</font>** Chen Jia, Baochang Zhang, Fatia Kusuma Dewi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view reasoning in coronary X-ray angiography is inherently a cross-projection geometric problem, yet automated report generation in this setting remains largely unexplored. The 3D vascular topology leads to projection-dependent branch overlap and foreshortening, rendering single-view modeling fundamentally incomplete and unstable for lesion localization and stenosis grading. Although multi-view fusion appears promising, learning anatomically consistent fusion from real angiograms is impeded by a critical limitation: cross-view alignment is unobservable and cannot be explicitly supervised. Consequently, conventional fusion relies on implicit correlations rather than verified anatomical correspondence. We address this by reformulating multi-view stenosis reporting as an alignment-constrained aggregation problem. A controllable synthetic angiography generation strategy is introduced to expose geometry-derived patch-level correspondence supervision unavailable in real data. An anatomy-correspondence module learns cross-view correspondence matrices that explicitly align auxiliary features within the main-view coordinate space prior to fusion, thereby constraining evidence aggregation to anatomically consistent regions. Experiments on synthetic data and zero-shot transfer to real angiograms show that this alignment-constrained design improves correspondence consistency and structured stenosis reporting compared to single-view modeling and conventional multi-view fusion methods. The code will be publicly available upon publication.

---


### 144. [Straight-Path Flow Matching for Incomplete Multi-View Clustering](https://arxiv.org/abs/2607.06281)

**<font color=#1a73e8>作者：</font>** Yiteng Yuan, Junyan Wang, Zheyuan Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Incomplete Multi-View Clustering addresses the problem of clustering multi-modal data when certain views are missing. Recent end-to-end generative approaches leverage diffusion models to recover missing views via stochastic noise-to-data trajectories. While expressive, such mechanisms are not explicitly designed for clustering, as they initialize from cluster-agnostic noise and rely on stochastic denoising dynamics. In this work, we revisit probability path design in end-to-end generative IMVC. We introduce a flow-matching framework with a linear interpolation path between paired view representations, that replaces diffusion with probability flows between observed and missing views. We provide a formal analysis showing that deterministic ODE flows are inherently better aligned with clustering objectives than diffusion-based stochastic trajectories, especially in terms of transport mechanisms that respect class-conditional data distributions and maintain cluster consistency in finite-step regimes. Building upon this insight, we develop an end-to-end IMVC architecture that integrates straight-path flow-matching view completion with cluster-level and entropy-based alignment to enforce cross-view clustering consistency. Extensive experiments on standard IMVC benchmarks demonstrate that the proposed framework establishes new state-of-the-art performance.

---


### 145. [Task Decomposition-Guided Reranking for Adaptive Agent Skill Retrieval](https://arxiv.org/abs/2607.06283)

**<font color=#1a73e8>作者：</font>** Yanping Chen, Weijie Shi, Wen Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill usage can significantly enhance the ability of modern agent systems to complete complex tasks. However, the growing scale of skill libraries makes accurate skill selection increasingly challenging. In real-world scenarios, ambiguous semantic matching often arises between a specific task requirement and multiple generic yet semantically similar candidate skills. Moreover, existing methods tend to overlook the dynamic influence of task difficulty and skill applicability when selecting the optimal target skill set. To address these issues, we propose SkillReranker, an inference-time reranking framework for adaptive skill selection. Specifically, we first perform semantic decomposition on both the task and skill sides, yielding informative subtask and execution-state descriptions as well as transition-state descriptions that characterize each skill's functionality. These descriptions are then used to construct a directed acyclic execution graph, where intermediate task states are modeled as nodes and candidate skills as edges, thereby establishing a structured task-skill correspondence. On this basis, SkillReranker determines whether each state node satisfies the split condition to identify subtask intervals. For each task interval, we employ a cross-encoder to perform comprehensive scoring over candidate skills and select the most suitable ones to form the final target skill set. Experiments on ALFWorld and ScienceWorld with three backbone LLMs show that SkillReranker effectively improves task performance, reduces environment interaction steps, and lowers token consumption compared with existing skill selection baselines.

---


### 146. [From Sinhala to Dhivehi: Cross-Lingual Transfer Learning for Low-Resource Speech Recognition](https://arxiv.org/abs/2607.06289)

**<font color=#1a73e8>作者：</font>** Lukmal Ilyas, Nevidu Jayatilleke  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dhivehi, the national language of the Maldives, is currently under-resourced for automatic speech recognition (ASR) and other NLP tasks. This study investigates whether cross-lingual transfer learning from Sinhala, a linguistically related, relatively well-resourced Insular Indo-Aryan language, can improve Dhivehi ASR. We conduct seventeen experiments across five transfer learning paradigms: Dhivehi-only baselines, sequential fine-tuning, multilingual fine-tuning, continual pre-training, and a control using Turkish as an unrelated language. The strongest system, continual pre-training on Sinhala followed by fine-tuning on Dhivehi with KenLM, achieves 12.89% WER and 2.70% CER, outperforming the Dhivehi-only baseline by 13.50% WER and 3.02% CER. However, the adaptation strategy and decoding configuration are equally critical for a successful transfer learning experiment. We conduct seventeen controlled experiments spanning five transfer learning paradigms: Dhivehi-only baselines, sequential fine-tuning, multilingual fine-tuning, continual pre-training, and a control experiment using Turkish as an unrelated language. The strongest system, continual pre-training on Sinhala followed by fine-tuning on Dhivehi with KenLM, achieves 12.89% WER and 2.70% CER, outperforming the Dhivehi-only baseline by 13.50% WER and 3.02% CER. The Turkish control experiment confirms that observed improvements stem from linguistic relatedness; adaptation strategy and decoding configuration are also critical.

---


### 147. [Quantitative Gaussian-Process limits of Tensor Programs](https://arxiv.org/abs/2607.06290)

**<font color=#1a73e8>作者：</font>** Andrea Agazzi, Eloy Mosig García, Dario Trevisan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study the infinite-width Gaussian-process limit of random neural networks
through the lens of tensor programs, and we provide a quantitative convergence
theory in Wasserstein distance.
Our main result gives explicit finite-width error bounds, of order inverse square-root of the widths
between finite-network executions and their
Gaussian-process limits. The framework is architecture-agnostic and covers feed-forward models together
with weight-sharing schemes relevant for recurrent and transformer-type
architectures.

---


### 148. [AlayaWorld: Long-Horizon and Playable Video World Generation](https://arxiv.org/abs/2607.06291)

**<font color=#1a73e8>作者：</font>** AlayaWorld Team, Kaipeng Zhang, Chuanhao Li 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Game worlds have traditionally been built through labor-intensive production pipelines, making them costly to develop, difficult to customization, and expensive to modify after deployment. Recent advances in video world models offer a fundamentally different paradigm. Rather than explicitly authoring every component of a virtual environment, these models autoregressively synthesize future observations conditioned on the current world state and user interactions, enabling playable worlds to be generated online. Trained on both gameplay recordings and real-world videos, they can capture diverse visual appearances and physical dynamics, opening new opportunities for interactive applications beyond gaming, including embodied intelligence. In this paper, we present \textbf{AlayaWorld}, a full-stack open-source framework for building interactive generative worlds. AlayaWorld enables open-ended real-time interaction, allowing users to freely navigate and perform diverse actions such as combat, spell casting, and monster summoning. The framework unifies the complete development-from data preparation model architecture, model training, inference acceleration, and deployment-within a modular and extensible architecture. Alongside the framework, we release reproducible pipelines, reference implementations, evaluation tools, and comprehensive documentation, establishing a practical foundation for future research and real-time applications of generative world models.

---


### 149. [Visual graphs for image classification: does the structure affect performance?](https://arxiv.org/abs/2607.06295)

**<font color=#1a73e8>作者：</font>** Alessandra Ibba  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning models have emerged in machine learning and related fields, demonstrating astonishing performance in various visual tasks. Despite their great success, however, these models are unable to fully encode intrinsic visual structures, and often ignore the spatial, topological, and semantic information contained within an image. Graph neural networks offer a good framework to face this aspect, but their effective use for visual tasks has been only partly explored and mainly starting from a limited perspective. This work aims to address this gap by conducting a systematic comparison of current graph construction techniques within the context of a fixed three-layer GCN architecture. Through an empirical study, it demonstrates in particular how the network structure affects performance and provides an important methodological contribution regarding the computational stages preceding graph utilization, which will be strongly influenced by the structure itself.

---


### 150. [DS-MTNet:Structured Multi-Task EEG Decoding for Human-Machine Collaboration](https://arxiv.org/abs/2607.06297)

**<font color=#1a73e8>作者：</font>** Xinjia Yu, Yang Zhou, Jing Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Current human-machine collaboration (HMC) systems rely on environment-facing sensors to observe visible actions and scene states, but the internal perceptual, intention-related, and state-related processes of operators remain insufficiently integrated into machine perception. Electroencephalography (EEG) provides a non-invasive, time-resolved modality to capture neural activity associated with these processes and can serve as an additional sensing channel in HMC. However, HMC-relevant EEG evidence is often mixed in continuous recordings. Existing EEG decoding methods usually target task-specific classification or aggregate prediction, so multiple HMC-relevant readouts are rarely organized in a unified EEG representation. To address this gap, this paper proposed the Decomposed-Source Multi-Task Network (DS-MTNet), a structured multi-task EEG decoding framework. DS-MTNet integrated three streams, namely EEG waveforms, task-routed source embeddings, and temporal-spectral power features, into reusable slots and used dual gating mechanisms to route task-specific components. The model was tested on a sustained-attention driving EEG dataset with three representative readouts: lane-departure-related epochs for environmental-event processing, steering-response stage for response preparation, and reaction-time-defined alertness state for internal state. DS-MTNet achieved the best mean performance among traditional, single-task deep, and multi-task EEG baselines, with the most robust gains observed for steering-response stage decoding. Ablation and interpretability analyses suggested that DS-MTNet jointly decoded multiple readouts and organized event-related, response-related, and state-related EEG evidence in a unified source-slot representation. These findings provide a computational step toward incorporating operator-related neural evidence into machine perception in HMC.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-195](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
