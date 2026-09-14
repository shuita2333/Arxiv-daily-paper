# 📦 其他研究 | 2026年09月14日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-189**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-189**

---

### 151. [A Dataset and Model for Imputing Water Surface Elevation on a Large and Extremely Sparse Spatiotemporal Graph](https://arxiv.org/abs/2609.11580)

**<font color=#1a73e8>作者：</font>** Ruben Cartuyvels, Karim Douch, Gabriele Bertoli 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous monitoring of water surface elevation across river networks is critical for flood forecasting, water resource management, and understanding the global water cycle. Yet, the scarcity of in situ gauges across much of the globe constrains the development of reliable modeling frameworks. Satellite altimetry has the potential to alleviate this problem but its use is currently hindered by sparse temporal coverage. To this end, we introduce AmazonSWE, a dataset for training and evaluating large-scale spatiotemporal graph imputation methods that integrates processed satellite altimetry measurements from a range of sources, including the recent wide-swath SWOT sensor. The dataset covers over 19K river sections and 10 years (2016-2026) in the Amazon river basin, with in situ gauges held out for evaluation. Besides contributing a novel real-world use case with the potential for societal impact, AmazonSWE introduces significant technical challenges: with fewer than 1% of sections observed per day, the dataset is far sparser than existing imputation benchmarks, and its directed acyclic river topology is both structurally different from and larger than graphs in existing datasets. We show that prior spatiotemporal graph imputation methods are not adapted to this topology, scale and sparsity, and propose a simple bidirectional selective state space model that outperforms them by sampling connected subgraphs and flattening space and time into a single token sequence with topology-aware positional encodings. Compared to the state-of-the-art published method for SWOT-based WSE densification, which integrates statistics with physical modeling, our model reduces RMSE against in situ gauges by 18-39%, while producing predictions for every river section rather than only those with sufficient nearby satellite coverage.

---


### 152. [From Intent to Execution Grant: An Execution-Boundary Conformance Profile for High-Risk AI Actions](https://arxiv.org/abs/2609.11596)

**<font color=#1a73e8>作者：</font>** Mengting Wu, Lin Wang, Yong Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly propose actions with external consequences, including financial transfers, infrastructure changes, software deployments, disclosures, and physical actuation. Authorization engines, policy languages, runtime monitors, provenance mechanisms, and agent guardrails provide important foundations, but do not necessarily define a common semantic contract for the final transition from a particular candidate action to execution authority.
We specify EBL-Core, an execution-boundary conformance profile for deciding whether one canonical, fully materialized AI-generated candidate may receive action-scoped execution authority under explicit conditions. It binds a structured intent object, Root and Operational Policies, evidence obligations, typed evidence, context, time, and a verifiable Decision Derivation through an Execution Release Contract (ERC). An ERC is not an authority-bearing token; a verified ALLOW ERC may support a separate Execution Grant governed by Redemption-time validation.
EBL-Core specifies action binding, policy non-weakening, evidence handling, deterministic adjudication, derivation verification, and grant lifecycle behavior. An accompanying reference artifact provides schemas, adjudication, separate verification and Semantic Replay, and a linearizable in-memory grant store. In the retained run, 34 static vectors and 15 lifecycle checks matched expected outcomes. Across 100 trials, 32 concurrent Redemption attempts yielded exactly one successful Redemption and protected test effect per trial; 100 Revoke-Redeem races ended in valid terminal outcomes. These bounded results demonstrate executability of the specified subset, not human-intent correctness, evidence truth, complete mediation, production readiness, mechanized correctness, or deployment-level security.

---


### 153. [MMGait: Benchmarking and Unifying Gait Recognition across Heterogeneous Modalities](https://arxiv.org/abs/2609.11601)

**<font color=#1a73e8>作者：</font>** Saihui Hou, Chenye Wang, Qingyuan Cai 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gait recognition is commonly studied using RGB videos or their derived silhouettes and poses. Yet human walking produces heterogeneous photometric, geometric, and motion cues that cannot be systematically examined with RGB-centered benchmarks. We present MMGait, a large-scale multi-sensor benchmark that brings visible, infrared, depth, LiDAR, and radar observations into sequence-level correspondence. It provides diverse modalities spanning appearance, contours, geometry, motion, and body structure. Under a shared impostor-augmented protocol, we evaluate single-modal recognition, cross-modal recognition via directed retrieval, and multi-modal recognition using task-specific experts. Across settings, modality rankings vary with probe conditions, cross-modal alignment remains difficult, and fusion often provides complementary gains. This analysis exposes a scalability problem: individual modalities, modality pairs, and fusion configurations are typically handled by separately trained experts. We formulate Omni-Modal Gait Recognition, which unifies single-modal, cross-modal, and multi-modal recognition within a shared identity space. OmniGait++ uses modality-specific front ends followed by a shared identity encoder to preserve modality-dependent cues while learning comparable identity descriptors. An anchor-guided fusion module aggregates modality subsets of varying size without frame-level synchronization. A jointly trained checkpoint covers all three recognition settings and accommodates modality subsets of different compositions and cardinalities. Experiments show OmniGait++ remains competitive with task-specific experts in many shared settings and extends to higher-cardinality fusion unavailable to fixed-pair models. The results establish MMGait as a common testbed for heterogeneous gait sensing and demonstrate the feasibility of unified recognition under varying modality availability.

---


### 154. [PHAT: PHotonic Accelerator for TFHE](https://arxiv.org/abs/2609.11613)

**<font color=#1a73e8>作者：</font>** Guowei Yang, Farbin Fayza, Beren Aydoğan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully Homomorphic Encryption (FHE) enables secure computation on encrypted data, making it a promising solution for privacy-preserving applications in the cloud. Among various FHE schemes, FHE over the Torus (TFHE) stands out due to its support for arbitrary operations. However, its high computation and communication overhead, particularly in the Fast Fourier Transform (FFT) operations required during bootstrapping, limits its practicality for real-world applications. Conventional electronic accelerators struggle to achieve sufficient throughput due to the limitations of technology scaling and the memory-wall problem.
To address these challenges, we propose PHAT, a PHotonic Accelerator for TFHE leveraging Optically-addressed Phase-Change Memory (OPCM). OPCM-based processing-in-memory systems offer high computation and communication throughput, making them well-suited for accelerating FFT operations in TFHE. However, directly mapping FFT to OPCM presents challenges such as high-precision analog computation and the high latency and energy cost of programming OPCM cells. To overcome these challenges, we introduce a novel electro-photonic accelerator architecture optimized for TFHE, featuring OPCM-based FFT units, a twiddle-stationary dataflow tailored for OPCM, and a scheduling mechanism to maximize the utilization of the FFT units. PHAT delivers $2.14\times$--$5.10\times$ speedup across four real-world TFHE workloads against the state-of-the-art ASIC accelerator. Our approach significantly enhances the performance of TFHE applications, paving the way for practical and efficient homomorphic encryption in cloud computing.

---


### 155. [Distributed Optimization of Modular Production Systems using Model-based Reinforcement Learning with Inverse Models](https://arxiv.org/abs/2609.11615)

**<font color=#1a73e8>作者：</font>** Andreas Schwung, Steve Yuwono, Sofiene Lassoued 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a novel approach for data-driven self-learning control of highly flexible, modular manufacturing systems. Specifically, we employ a novel framework for model-based reinforcement learning which introduces approximate inverse process models within the training of reinforcement policies. This approach disentangles the learning of actuation dynamics and the dynamics in state space, resulting in RL-based training solely within the task space. We propose a lightweight feedforward architecture for approximate inverse models and integrate them within the policy network of standard RL algorithms. We apply the approach to a laboratory modular production testbed with heterogeneous production modules. The results underline the efficiency improvements for modular manufacturing units in terms of both performance and training speed, particularly for off-policy algorithms.

---


### 156. [LangStreet: Persistent Language Fields for Anchor-Decoded Street Gaussians](https://arxiv.org/abs/2609.11616)

**<font color=#1a73e8>作者：</font>** Runyi Yang, Deheng Zhang, Xiaoye Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language Gaussian fields implicitly assume that the primitive carrying semantics remains identifiable across views. This assumption breaks in scalable anchor-decoded representations, where persistent anchors generate view-conditioned child Gaussians whose geometry and appearance vary with the camera. We introduce Ours, a persistent language field for such structured Gaussian scenes. Our key idea is semantic ownership: transient children route observations, while persistent decoder slots and their parent anchors own the language field. We use alpha-compositing responsibilities to accumulate additive directional evidence at slots; these statistics marginalize exactly to anchors. We then complete weakly supported slots with anchor-aligned evidence while preserving the anchor direction, and represent slot detail through low-rank residuals in anchor-relative semantic coordinates. Our primary model, Ours (base), stores anchor features together with compact slot residuals. Ours (light) retains only anchor features, whereas Ours (max) stores the full-dimensional completed slot features explicitly. Without scene-specific semantic optimization, Ours (base) nearly matches Ours (max) across KITTI, Virtual KITTI, and Waymo. On KITTI, it achieves 34.19 2D mIoU with a 2.72 GiB effective feature footprint, compared with 34.20 mIoU and 12.90 GiB for Ours (max). The same accuracy-storage trend holds on Virtual KITTI and Waymo. These results show that language fields on view-conditioned splats require persistent semantic ownership, conserved evidence, and a hierarchy that balances stability, detail, and representation cost. Our code, checkpoints, and benchmark suite will be publicly available.

---


### 157. [Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation](https://arxiv.org/abs/2609.11638)

**<font color=#1a73e8>作者：</font>** Jintao Zhang, Kai Jiang, Jintao Chen 等 35 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We present Vidu S2, which comprises Vidu S2-Avatar, a real-time interactive digital-character model, and Vidu S2-Editing, a real-time video editing model. Moreover, we explore the feasibility of real-time spatial video generation for both Vidu S2-Avatar and Vidu S2-Editing. Compared with Vidu S1, Vidu S2-Avatar supports real-time 720p video generation, generation with dynamic references that can be updated at any moment, and stronger instruction following, such as dancing. Vidu S2-Editing supports editing a video stream in real time, including style rendering, clothing replacement, character replacement, and background replacement. Experiments show that Vidu S2 outperforms all baselines. A playable online demo is available at this https URL.

---


### 158. [LoaDiff: Conditional Generation of Electricity Consumption Time Series for Energy Analytics](https://arxiv.org/abs/2609.11639)

**<font color=#1a73e8>作者：</font>** Mariia Baranova, Adrien Petralia, Etienne Le Naour 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The energy transition is reshaping residential electricity consumption through the increasing adoption of distributed generation, electrified appliances, and demand-response programs. Understanding these evolving behaviors requires access to granular smart-meter data for applications such as load forecasting, appliance detection, and demand-side flexibility analysis. However, such data are subject to strict access restrictions and data-protection regulations. Thus, realistic synthetic alternatives are necessary. In this paper, we introduce LoaDiff, a diffusion-based generative model for year-long, sub-hourly smart-meter load curves. LoaDiff supports flexible conditioning on static household attributes, such as appliance ownership, and dynamic contextual variables, including calendar information and outdoor temperature. We evaluate the model against multiple generative baselines on three residential electricity-consumption datasets. Our experiments assess four complementary dimensions: fidelity and diversity, training-record memorization risk, downstream utility for load forecasting and appliance detection, and conditional controllability under alternative temperature conditions. The results show that LoaDiff generates realistic and diverse load profiles, achieves a favorable trade-off between generation quality and limited evidence of memorization, preserves information useful for downstream energy applications, and responds coherently to changes in conditioning variables.

---


### 159. [RDDMPI: Residual Denoising Diffusion Model for Probabilistic Multivariate Time Series Imputation](https://arxiv.org/abs/2609.11648)

**<font color=#1a73e8>作者：</font>** Ramiro Valdes Jara, David Chapman, Adam Meyers  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multivariate time series imputation (MTSI) aims to recover missing values in temporal data composed of multiple interdependent variables. This problem is central to real-world applications such as healthcare monitoring, traffic networks, and energy systems. Recent diffusion-based approaches have shown strong potential for probabilistic imputation by learning to generate missing values through iterative denoising. However, most existing approaches perform diffusion directly in the original data space, requiring the denoising network to simultaneously capture global structure, temporal dynamics, and stochastic variability. This makes the generative task unnecessarily complex, especially when modern deterministic imputers can already provide accurate initial reconstructions. To address this limitation, we propose RDDMPI, a conditional residual diffusion framework that operates directly in residual space. Instead of modeling the full missing signal directly, we reformulate probabilistic imputation as a baseline-residual decomposition, where a pretrained model captures the dominant signal and a diffusion process models the residual uncertainty. To better exploit deterministic guidance, \model{} conditions the reverse denoising process on both the baseline-completed signal and its latent representation, while a reliability-aware conditioning mechanism adaptively controls the influence of baseline information during residual generation. This formulation simplifies the diffusion learning objective, enabling it to focus on structured correction terms rather than reconstructing the full signal. Experiments on multiple benchmark datasets demonstrate that RDDMPI consistently improves both reconstruction accuracy and uncertainty quantification.

---


### 160. [Self-Supervised Cardiac Phase Detection via Single-Parameter Latent Orbits](https://arxiv.org/abs/2609.11650)

**<font color=#1a73e8>作者：</font>** John Bonnici, Matthew Baugh, Aleksandra Kulbaka 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate identification of end-diastole (ED) and end-systole (ES) in echocardiography underpins the quantification of ventricular function, yet manual selection of these key frames is subjective and introduces clinically significant inter-operator variability. Recent self-supervised methods either prescribe strict periodic trajectories or learn an unconstrained low-dimensional motion subspace from reconstruction or registration objectives. The former offers interpretability but imposes restrictive assumptions on temporal progression, whereas the latter leaves cardiac phase implicit and ED/ES must be recovered through post-hoc geometric processing of the learned trajectory. We translate the physiological observation that cardiac phase is a one-dimensional signal into a prior by constraining the latent motion component to a single-parameter latent orbit, i.e., a global linear trajectory in latent space indexed by a bounded scalar phase variable. Mapping this variable through a sinusoidal nonlinearity yields an oscillatory motion signal with consistent temporal ordering, enabling direct identification of ED and ES from the learned phase signal. This inductive bias allows the model to capture an interpretable representation of the cardiac cycle, while maintaining flexibility to capture irregular heartbeats. Trained on EchoNet-Dynamic without annotations, our minimal single-parameter cardiac phase model learns an effective latent orbit, significantly improves upon the previous state of the art in ED localisation and matches it in ES localisation while using a more constrained representation and fewer training epochs. This demonstrates that a principled physiological inductive bias can match or exceed the performance of more complex representations. Code is available at: this https URL

---


### 161. [Learnware and AI Model Management System](https://arxiv.org/abs/2609.11656)

**<font color=#1a73e8>作者：</font>** Zhi-Hua Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The transition from file storage to database management systems transformed stored data into managed resources. AI now faces an analogous transition from AI model storage to AI model management. Existing model pools essentially serve as \textit{AI model storage systems}. What is needed instead are \textit{AI model management systems} that enable models trained by different developers, for different tasks, with different data, and under different objectives to be identified, reused, and even assembled to address future user tasks. Because AI model developers are generally unwilling to share their training data, such systems should operate without accessing the training data of model developers and, ideally, without accessing raw data of future users. This requirement poses a fundamental challenge: the functionality of a modern AI model may not be fully understood even by the developer who trained it. How, then, can a system identify which models are useful for a given user task, let alone assemble models developed independently for different purposes? At first glance, this objective may appear unattainable. It becomes possible, however, by upgrading the basic unit of management from a machine learning model to a \textit{learnware}. \textit{Learnware = Model + Specification}. The specification, whose assignment transforms a trained model into a learnware, is generated with the help of a machine learning process without disclosing the training data of the developer and has a theoretically established data-preservation property. The \textit{Learnware Dock System (LDS)} provides a path toward powerful AI model management systems. Because specifications are generated according to a published reference and are comparable across models, they can also serve as an AI model \textit{collaboration protocol} through which independently developed models, including intelligent agents, can collaborate.

---


### 162. [Autonomy, Social Norms, and Alignment: Towards a Developmental Framework for Autonomous Artificial Agents](https://arxiv.org/abs/2609.11660)

**<font color=#1a73e8>作者：</font>** Marica Notte, Ludovica Marinucci, Vieri Giuliano Santucci  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In recent years, artificial intelligence has made extraordinary progress thanks to large-scale models capable of generalization and the generation of complex outputs. However, transferring this potential into embodied agents reveals a significant limitation: the most advanced systems rely on pre-existing datasets and human feedback strategies that are powerful but insufficient in dynamic or unknown contexts. To adapt, an agent must acquire knowledge through direct interaction with its environment. One strategy to address this challenge involves introducing higher-level mechanisms, such as intrinsic motivations, which leverage curiosity and competence, to guide exploration and learning in complex environments. While this flexibility expands autonomy, it complicates the task of ensuring agents remain aligned with human goals. Alignment, already a challenge for artificial systems in general, becomes even more complex in unstructured and dynamic contexts where predefined rules prove insufficient. To be effective and adaptable, norms must be rooted in experience through an epistemological process that starting from simple, situated principles allows for the gradual construction of more complex rules through experience, autonomous learning, and cooperation with other moral agents. Similarly to children learning social norms by exploring their environment and participating in collective practices, artificial agents must also be educated toward alignment. Following Dennett, the status of a moral agent is not innate but is attributed gradually based on the ability to responsibly manage increasing degrees of freedom. From this perspective, the regulatory sandboxes can be viewed as pedagogical environments for AI: dynamic spaces where alignment develops as a formative process, progressively shaping autonomous behaviors through interaction and cooperation in scenarios of increasing complexity.

---


### 163. [Multimodal Taxonomic Conditioning for Generative Plankton Imagery](https://arxiv.org/abs/2609.11673)

**<font color=#1a73e8>作者：</font>** Daniela Ivanova, Ozgu Goksu, Nicolas Pugeault  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated plankton imaging produces severely long-tailed datasets, where the rare taxa of greatest ecological interest have too few images to train or evaluate classifiers reliably. We generate synthetic plankton imagery conditioned on taxonomy: a CLIP encoder is adapted on a large plankton corpus with a ranked contrastive objective extended to deep, ragged taxonomies, then frozen to condition a parameter-efficient diffusion transformer. We evaluate synthetic sample quality on distributional fidelity and downstream classifier utility.

---


### 164. [Single-Stream Multi-Feature Fusion with Temporal Robustness for Gait Emotion Recognition](https://arxiv.org/abs/2609.11680)

**<font color=#1a73e8>作者：</font>** Shirong Lyu, Silu Quan, Yixuan Ding 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D skeleton-based gait emotion recognition faces high annotation costs, data scarcity, and poor generalization on heterogeneous data. This paper proposes SV-GCN, a single-stream multi-feature fusion framework with temporal invariance. We introduce intra-frame relative motion features to eliminate frame-rate sensitivity and embed heterogeneous cues at shallow layers, enabling early fusion without multi-stream complexity. For variable-length sequences, we design a global mask-guided valid-frame spatio-temporal graph convolution module, introducing frame-rate insensitivity for the first time in this domain. On the E-Gait dataset, our method achieves performance comparable to state-of-the-art while demonstrating strong generalization across varying sequence lengths and frame rates, offering a viable pathway for pre-training on large-scale skeleton-based action recognition datasets.

---


### 165. [Spectral Adapters for Segment Anything Model-based Segmentation of Colorectal Liver Metastases in Computed Tomography](https://arxiv.org/abs/2609.11703)

**<font color=#1a73e8>作者：</font>** Ramtin Mojtahedi, Mohammad Hamghalam, Jacob J. Peoples 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate segmentation of colorectal liver metastases (CRLM) in contrast-enhanced computed tomography (CT) is important for response assessment, surgical planning, and follow-up. We propose two parameter-efficient spectral adapters for the Segment Anything Model (SAM): the Directional Spectral Adapter (DiSECT) and Spectral Instance-Guided Adapter (SiGA). DiSECT uses singular value decomposition of frozen weights to constrain residual updates to leading spectral directions, while SiGA adds global and input-conditioned gating through a multilayer perceptron. We evaluate these methods on 446 contrast-enhanced CT volumes (355 training, 91 testing) and compare them with LoRA, QLoRA, convolutional adapters (CAD), and a 3D nnU-Net baseline. Experiments consider single-point, three-point, bounding-box, and no-prompt regimes. SiGA achieves the best single-point performance with a Dice score of 0.77, IoU of 0.69, and HD95 of 35.39 mm. Under no-prompt inference, SiGA reaches 0.76 Dice, 0.68 IoU, and 46.76 mm HD95, comparable to the nnU-Net baseline (0.758 Dice). DiSECT uses only 0.14 million trainable parameters. These results show that spectral adapters can efficiently adapt SAM for CRLM segmentation while retaining strong accuracy with limited trainable parameters.

---


### 166. [Bigger than the EAR BOX: A Theory-Grounded Review of XR Accessibility Research for Deaf and Hard of Hearing Communities](https://arxiv.org/abs/2609.11706)

**<font color=#1a73e8>作者：</font>** Shuxu Huffman, Michaela Okosi, Jose Merino 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Extended Reality (XR) technologies have received growing attention in accessibility research involving Deaf and Hard of Hearing (DHH) communities. Yet less attention has been given to the assumptions shaping this work. We present a theory-grounded review of XR research involving DHH users. Drawing on Disability Studies, Deaf Studies, and DeafSpace, we develop a theoretical framework with four analytical dimensions: orientation toward access, distribution of responsibility, conceptualization of DHH communities, and spatial and perceptual assumptions. We apply this framework to 53 XR studies involving DHH users, identified through a search and screening of ACM publications from 2015 to 2025. Our analysis shows that XR accessibility is frequently framed as supporting communication within hearing-default environments, while overlooking the diversity of DHH communities. We identify directions for redistributing accessibility labor and reconfiguring space, and offer our framework as a tool for future XR research involving DHH communities.

---


### 167. [MC-DeTra: Motion-Consistent Joint Object Detection and Socially-Aware Trajectory Forecasting in Bird's-Eye-View Images](https://arxiv.org/abs/2609.11717)

**<font color=#1a73e8>作者：</font>** Vladislav Diuzhev, Dmitry Yudin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified models for object detection and trajectory forecasting aim to merge perception and prediction for autonomous driving, refining actor trajectories directly over shared bird's-eye-view (BEV) images rasterized from LiDAR and high-definition maps. Their accuracy on dynamic, moving actors, however, remains the hardest part of the task, and the strongest such model, DeTra, has no public implementation. We contribute an openly released DeTra reimplementation with documented approximations, and on top of it MC-DeTra: a family of motion-consistency mechanisms that add supervision through two annotation-derived auxiliary signals -- each actor's observed past motion and the occupancy of the surrounding traffic that forms its social context -- and one inter-output consistency constraint that aligns an actor's predicted heading with its predicted direction of motion. Every proposed loss is train-only and inference-safe: it shapes the shared BEV representation during training and is removed at test time, adding no inference latency. On the Waymo Open Dataset, evaluated under a strict, detection-conditioned forecasting protocol, MC-DeTra improves dynamic, socially-situated trajectory forecasting while preserving or improving detection accuracy; a gradient-based loss-calibration analysis exposes how the auxiliary objectives compete at the shared backbone, and our ablation identifies which signals contribute most. We release code, configurations, and evaluation tooling at this https URL.

---


### 168. [Revisiting Avatar-As-Image: High-Fidelity Registration is All You Need](https://arxiv.org/abs/2609.11722)

**<font color=#1a73e8>作者：</font>** Margaret Kostyrko, Yuxuan Xue, Garvita Tiwari 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The representation of 3D clothed humans as standardized 2D UV texture and displacement maps over an underlying body model has long been studied. This compact representation is enticing as it enables pretrained image networks to process, generate, and edit 3D avatars, but is only useful if scans are accurately aligned and brought into correspondence via high-fidelity registration. This prerequisite has never been met, which we argue explains the limited quality of prior UV-based methods for clothed humans. Despite its significance, no public method produces high-fidelity SMPL(-X)+D registrations with UV texture from arbitrary clothed scans. We present AvaImg, a multi-stage optimization pipeline, to close this gap: it enforces body-inside-clothing constraint via signed winding numbers, made viable by a three-level efficiency cascade (~10x runtime reduced, ~95% storage saved), and recovers fine surface detail using coarse-to-fine displacement optimization. AvaImg outperforms all baselines in body fitting, shape estimation, and surface registration across six datasets, yielding textured registrations near-indistinguishable from scans (PSNR=34.48dB). For validation of AvaImg's Avatar-as-Image representation as imminently compatible with image foundation models, we auto-encode our UV maps via the frozen FLUX VAE. This achieves only 0.76mm added Chamfer error relative to scan and shows that the resulting maps lie within natural-image distributions, supporting the use of 2D generative priors for 3D avatar generation. Code, data, and Singularity containers will be at this https URL.

---


### 169. [Differentially Private EEG Feature Anonymization: A Privacy-Utility Case Study in Clinical Neurophysiology](https://arxiv.org/abs/2609.11777)

**<font color=#1a73e8>作者：</font>** Noman Sadiq, Mohsen Toorani  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Clinical electroencephalography (EEG) data are valuable for healthcare research and for developing artificial intelligence (AI)-based clinical decision-support systems, but EEG recordings and derived features may contain sensitive patient-specific information. This creates privacy risks when data are reused, analyzed, or shared across clinical and research environments. Conventional anonymization methods are often insufficient for high-dimensional biomedical signals, since removing direct identifiers does not necessarily prevent re-identification, linkage, or inference risks. At the same time, strong privacy protection may distort clinically relevant signal characteristics and reduce data utility. This paper studies subject-level differential privacy for protecting clinical EEG-derived feature representations using Gaussian and Laplace perturbations. The proposed framework considers three deployment scenarios: client-side anonymization, centralized server-side anonymization, and decentralized local training. Following EEG preprocessing and feature extraction, Gaussian and Laplace perturbations are applied to the resulting patient-level EEG feature representations. The Laplace experiments evaluate the implemented noise scales, while the scales required for formal full-vector calibration are derived separately. The effects of both perturbations are assessed using statistical utility measures and a downstream machine-learning-based utility check. The results show that differentially private perturbation can be integrated into EEG processing workflows, but the selected mechanism, privacy parameters, and sensitivity calibration strongly influence data utility. The study highlights the practical privacy-utility trade-off in DP-based EEG feature anonymization and the challenges of preserving downstream utility in small and imbalanced clinical EEG datasets.

---


### 170. [Predicting Privacy Leakage from Weight Spectral Density](https://arxiv.org/abs/2609.11780)

**<font color=#1a73e8>作者：</font>** Richard J. Preen, Jim Smith  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Membership inference attacks (MIAs) are widely used to audit the privacy disclosure risk of machine learning models, however current state-of-the-art attacks require training computationally expensive shadow models, making large-scale privacy evaluation impractical. In this work, we investigate whether inexpensive spectral metrics derived from the heavy-tailed self-regularisation framework can serve as proxies for MIA vulnerability. We evaluate several WeightWatcher spectral metrics on image and tabular classification tasks and compare their relationship with MIA privacy leakage against conventional measures of generalisation. Across datasets, stable rank exhibits a strong positive correlation with overall MIA success, while Log alpha-Norm shows a consistent negative correlation with MIA vulnerability at the low false-positive regime. These associations are observed to be stronger than those obtained using the generalisation gap. The results indicate that neural network spectra may contain information about privacy leakage that is not fully captured by conventional measures of overfitting, motivating spectral analysis as a promising direction for scalable privacy auditing.

---


### 171. [Thinking with Looped Flows](https://arxiv.org/abs/2609.11801)

**<font color=#1a73e8>作者：</font>** Ayhan Suleymanzade, Chanhyuk Lee, Floor Eijkelboom 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Humans and machines often solve harder problems by spending more time on computation. In deep learning, looped models implement this idea during inference by recurrently updating a hidden state. In practice, however, their training backpropagates through only one or a few updates, making it hard to train early updates to support future ones. We propose looped flows, an approach that sidesteps this issue by training the recurrence with local denoising objectives. By imposing temporal association across denoising objectives through progressively decreasing noise levels and shared noise, the model is incentivized to learn recurrent states that transfer useful computation over time, even when gradients cover only a few updates. We then formulate inference as integrating the velocity of a probability flow parameterized by the learned denoiser, coupled with recurrent states. This allows solving harder problems by spending more computation through a finer temporal grid and enables multiple valid predictions from different initial noise samples. Across six reasoning benchmarks including two multi-solution benchmarks, looped flows outperform prior state-of-the-art looped models overall, achieving 58.8% test accuracy on ARC-AGI-1 and 12.2% on ARC-AGI-2.

---


### 172. [Logit Refiner: Improving Visual Autoregressive Models via Intra-Scale Dependency Modeling](https://arxiv.org/abs/2609.11804)

**<font color=#1a73e8>作者：</font>** Meimingwei Li, Stefan Andreas Baumann, Felix Krause 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual Autoregressive Models (VAR) generate images through next-scale prediction, producing all tokens within each scale in parallel. We show that this parallel decoding constitutes a mean-field-style approximation that discards spatial dependencies among same-scale tokens, causing locally incoherent samples regardless of backbone capacity -- a limitation of the decoding rule. Addressing this limitation, we introduce the Logit Refiner, a lightweight autoregressive module that restores intra-scale dependencies by sequentially sampling tokens conditioned on frozen backbone features. Adding only ~10% parameters and less than 5% of the base model's training compute, it plugs into any pretrained VAR checkpoint without retraining. Controlled ablations isolate joint intra-scale sampling -- rather than additional capacity or training -- as the critical ingredient. Across backbones from 310M to 2B parameters on class-conditional ImageNet 256x256, the refiner consistently improves generation quality, enabling a 1.1B-parameter model to surpass one twice its size. The approach further generalizes to text-to-image generation, confirming that the mean-field bottleneck persists across VAR variants and is effectively alleviated by our method.
Project page: this https URL

---


### 173. [Understanding Operator Attitudes Toward AI-Supported Decision Making in Maritime Operations](https://arxiv.org/abs/2609.11805)

**<font color=#1a73e8>作者：</font>** Doreen Jirak, Armeen Saroukanoff, Dirk van Rooy  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Maritime Autonomous Surface Ships (MASS) and AI- supported decision assistants are expected to transform maritime operations, but their safe integration depends on how maritime professionals perceive and trust such systems. This paper presents a survey study on maritime stakeholders' attitudes toward an AI-supported assistant in collision-avoidance scenarios. Participants evaluated technology anxiety, trust in automation, and explanation quality using established and adapted questionnaires, complemented by sentiment and thematic analysis of open-ended responses Results indicate a generally positive disposition toward maritime technology, no clear age-related differences in openness, stable trust across scenarios, and more scenario-sensitive, multidimensional explanation ratings. Open responses showed that participants valued support for decision-making, situation awareness, and confidence-building, while raising concerns about AI reliability, over- reliance and loss of expertise. The findings suggest that maritime AI systems should not focus solely on increasing automation or trust, but on supporting calibrated reliance through transparent, reliable, and operationally meaningful design with domain experts in the loop.

---


### 174. [Don't Trust the Super-App: A Case Study of Russia's Max](https://arxiv.org/abs/2609.11814)

**<font color=#1a73e8>作者：</font>** Richa Priyanka, Aaron Ortwein, Joel Reardon 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Super-apps, an emerging mobile architecture, host third-party mini-apps inside a single app, allowing users to access diverse services. A decade of security research on the super-app ecosystem has all assumed super-apps to be a trusted intermediary. We argue this implicit trust is difficult to justify: China's WeChat is already shown to passively track its user's activity across mini-apps at extraordinary scale; Russia's MAX's parent company is reported to be deeply entangled with the state prosecution of online speech; and Iran's Bale was reported to be functioning in the world's longest internet shutdown due to its state-backed support.
In this paper, we show how malicious super-apps have undeniable capabilities to silently undermine the security and privacy of mini-apps and users without leaving any trace. Using MAX as an example, we show how it can capture mini-app UI, read and write mini-app local storage, inject arbitrary JavaScript into a mini-app's runtime, mediate mini-app network traffic, and control authentication context in ways that can enable silent user impersonation. Sadly, these capabilities manifest themselves in any super-app because of the architectural privileges granted to them by design. We argue that mobile OS and app store interventions are urgently needed to close this architectural blind spot before it is further exploited.

---


### 175. [MotionQ: Operator-Conditioned Motion Quotients for Cross-Observation WiFi Gesture Recognition](https://arxiv.org/abs/2609.11818)

**<font color=#1a73e8>作者：</font>** Xiang Zhang, Huan Yan, Geying Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> WiFi gesture recognition is accurate in fixed deployments but often degrades when user orientation, available links, or transceiver placement changes. Unlike ordinary domain shifts, these changes alter the wireless observation operator, so the same motion is expected to produce different measurements. Existing methods nevertheless pursue domain-invariant features and largely overlook changing layouts and observation configurations. Yet changing the observation operator also changes which task-relevant motion cues are physically observable, rather than merely altering the appearance of a fixed set of cues. Under a local linearization of the WiFi forward process, we derive a common task-observability condition under which a strict common linear representation is recoverable from every geometry-induced operator while preserving the gesture task. When the condition fails, enforcing stronger alignment across additional heterogeneous source operators may discard task-relevant cues still observable under individual operators. We therefore present MotionQ, which generates an operator-conditioned two-support motion measure for each candidate geometry. A motion quotient removes only the arbitrary ordering of its unlabeled supports and is represented by permutation-invariant central moments. Rather than matching quotients across operators, single-link-retention interventions encourage each view to retain information sufficient for gesture recognition. Extensive evaluations show that MotionQ is robust to extrapolative observation operators.

---


### 176. [Model-Aware Schedules Improve Generation via Fiberwise Optimal Transport](https://arxiv.org/abs/2609.11842)

**<font color=#1a73e8>作者：</font>** Luyi Jia, Boyan Zhang, Yilun Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion and flow-matching schedules control the signal and noise coefficients that mix data and noise along affine probability paths. Minimizing a kinetic action defined on coefficient paths, motivated by optimal transport, helps explain strong baselines but remains model-agnostic and ignores prediction error. Here we introduce a model-aware schedule construction based on fiberwise optimal transport. At a fixed time and state on the probability path, compatible signal/noise decompositions form an affine fiber. We define a fiberwise prediction risk by averaging optimal-transport costs between the true and predictor-induced decompositions within these fibers. On a fixed coefficient curve, combining this risk with coefficient-path kinetic action yields a closed-form optimal time allocation. This construction extends to general linear prediction targets, and the risk profile can be estimated from an early baseline checkpoint. We evaluate DDPMs and flow matching across prediction targets, training configurations, risk-estimation checkpoints, datasets, and architectures. Our model-aware schedules consistently outperform strong baselines, including a 38.6% relative FID reduction for flow matching on CIFAR-10 at 16 function evaluations. Each model-agnostic kinetic baseline determines its own kinetic reference coordinate. In these coordinates, fiberwise-risk profiles from independently trained models in different settings align closely after normalization to unit area. The resulting schedule deformations used in training also align, suggesting empirical universality across the evaluated models and settings. Pretrained-checkpoint diagnostics extend this normalized-risk agreement to larger conditional latent diffusion and 2-RF models. A frozen analytic allocation template retains most of the model-aware improvement without further risk estimation or model-specific fitting.

---


### 177. [IndicTriMix: Developing Language Identification Datasets and Models for Tri-Language Code-Mixing](https://arxiv.org/abs/2609.11851)

**<font color=#1a73e8>作者：</font>** Pruthwik Mishra, Rudra Trivedi, Avi Patel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language identification in code-mixed text, largely observed in social media, is highly essential when users frequently switch between multiple languages within a single utterance. Accurately identifying the languages of code-mixed tokens becomes an urgent necessity. Traditional language identification models, designed for monolingual text, are not well suited for token-level language identification in code-mixed settings. We formulate the task as a sequence labeling problem and fine-tune contextual transformer-based models MuRIL and XLM-RoBERTa best suited for Indian languages. We evaluate these systems on three different data configurations (Hindi, Gujarati, and Bengali) to predict language labels for individual tokens. We release a benchmark for language identification in code-mixed tokens with manually annotated test sets. We propose two approaches of code-mixed generation using parallel sentences of three languages. The trained models demonstrate the effectiveness of contextual embeddings for token-level language identification in multilingual social media text. For reproducibility and to facilitate future research, we publicly release our fine-tuned models.

---


### 178. [Epistemic orientation predicts legislative effectiveness among members of the US Congress](https://arxiv.org/abs/2609.11865)

**<font color=#1a73e8>作者：</font>** Segun Aroyehun, Stephan Lewandowsky, David Garcia  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Truth and evidence-based communication provide important foundations for democratic governance, accountability, and collective decision-making. Prior work shows that evidence-oriented language in US congressional floor speeches has declined since the mid-1970s, alongside broader changes in legislative productivity and polarization. This study shifts the analysis from congressional sessions to individual members of Congress to examine whether epistemic orientation varies systematically across legislators and whether it relates to political behavior and legislative effectiveness. Using the Evidence-Minus-Intuition (EMI) score, we measure the relative prevalence of evidence-oriented versus intuition-oriented language in congressional floor speeches and Twitter posts. We link these measures to legislator-level data on ideology, institutional position, communication context, and Legislative Effectiveness Score (LES). The results show that more ideologically extreme members use less evidence-oriented language on the congressional floor. EMI also exhibits cross-platform consistency with members who use more evidence-oriented language in floor speeches also being more evidence-oriented on Twitter, although EMI is lower on Twitter overall. Finally, EMI in congressional speeches is positively associated with individual legislative effectiveness, even after accounting for ideology and extensive political, institutional, demographic, topical, and communication volume controls. These findings suggest that evidence-oriented language is not only an aggregate feature of congressional discourse but also a meaningful attribute of individual-level legislative communication and effectiveness.

---


### 179. [AdamX: Cosine similarity meets gradient descent](https://arxiv.org/abs/2609.11867)

**<font color=#1a73e8>作者：</font>** Francisco Caldas, Ruben Belo, Cláudia Soares  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We introduce AdamX, a first-order optimizer that incorporates cosine similarity as an adaptive mechanism for controlling update magnitudes. The proposed method is scalable, model-agnostic, and straightforward to integrate into existing training pipelines. We further introduce a variance rectification scheme that promotes smoother optimization during the early stages of training. Overall, we provide empirical evidence that AdamX achieves competitive convergence rates across a range of benchmark datasets and architectures. Performance is evaluated in terms of the number of epochs required to reach predefined performance thresholds under a fixed hyperparameter budget. Code and Experiments available at: this https URL.

---


### 180. [On the Regularization Landscape for the Linear Recommendation Models](https://arxiv.org/abs/2609.11876)

**<font color=#1a73e8>作者：</font>** Dong Li, Zhenming Liu, Ruoming Jin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, a wide range of recommendation algorithms inspired by deep learning techniques have emerged as the performance leaders on several standard recommendation benchmarks. While these algorithms were built on different DL techniques (e.g., dropouts, autoencoder), they have similar performance and even similar cost functions. This paper studies whether the models' comparable performance are sheer coincidence, or they can be unified under a single framework. We find that all linear performance leaders effectively add only a nuclear-norm based regularizer, or a Frobenius-norm based regularizer. The former ones possess a (surprising) rigid structure that limits the models' predictive power but their solutions are low rank and have closed form. The latter ones are more expressive and more efficient for recommendation but their solutions are either full-rank or require executing hard-to-tune numeric procedures such as ADMM. Along this line of finding, we further propose two low-rank, closed-form solutions, derived from carefully generalizing Frobenius-norm based regularizers. The new solutions get the best of both nuclear-norm and Frobenius-norm world.

---


### 181. [From Specs to Apps: Verifying and Monitoring Models of Signal and WhatsApp](https://arxiv.org/abs/2609.11882)

**<font color=#1a73e8>作者：</font>** Moustafa Said, Aurora Naska, Kevin Morio 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Signal protocol is a prominent messaging protocol that secures communication for billions of users. It powers WhatsApp, the most widely used messaging application worldwide, and the Signal app, popular among privacy-conscious users. Extensive research in the computational and Dolev-Yao settings provides strong formal security guarantees for the protocol itself. However, a gap remains between the guarantees of the protocol specification and the implementation's actual behavior at runtime. In this work, we bridge this gap by applying SpecMon, a recently proposed runtime monitor, to check whether observed executions conform to formal protocol models. To this end, we instrument two applications (WhatsApp Web and Signal Desktop) to capture their interactions with the network and the cryptographic components. Using this instrumentation, we develop two multiset-rewrite models that are compatible with Tamarin, thus enabling verification. We derive the first model of WhatsApp Web's implementation of the Signal protocol and the most detailed model to date of Signal's original protocol. Monitoring establishes that observed executions conform to these models, relative to the trusted event extraction and the symbolic abstraction. For the core components of the Signal protocol, we verify authentication and secrecy properties. Finally, monitoring reveals previously undocumented differences between the original libsignal library and WhatsApp's fork. We evaluate our methodology and demonstrate its reproducibility. Developing the WhatsApp Web model, instrumenting the app, adding fuzzing, and running the experiments took three person-weeks. We also demonstrate efficient monitoring of real-world applications and detection of deliberately injected security faults, with low overhead in our measured setting.

---


### 182. [CoRA-NAS: Coarse Ranking and Anchor-Residual Refinement for Neural Architecture Search](https://arxiv.org/abs/2609.11884)

**<font color=#1a73e8>作者：</font>** Yifan Yang, Zhaoyan Wang, Zheng Gao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Zero-cost proxies rank architectures cheaply, but their reliability varies across search spaces. We introduce CoRA-NAS (COarse Ranking + Anchor-residual), a two-stage framework combining a static ranking prior with low-cost learning-curve refinement. CoRA-Rank aggregates capacity and structure-at-initialization proxies through an equal-weight log-rank consensus and a target-free consensus gate. CoRA-Refine samples anchors across this prior, extrapolates their early validation curves, and propagates a learned residual correction with an ExtraTrees model. The refinement uses approximately 1% of the cost of fully training the candidate set. Fully trained architecture-accuracy labels are not used to fit the ranker. One configuration is used across spaces, with space-specific architecture encodings. Across NAS-Bench-201, NAS-Bench-101, TransNAS-Bench-101, and NATS-SSS, CoRA-Refine achieves mean Spearman correlations of 0.946, 0.715, 0.786, and 0.894, respectively. Its worst-space correlation of 0.715 is the highest among the compared methods. On NAS-Bench-201/CIFAR-100, its selected architecture reaches 73.32% accuracy, near the reported ground-truth best of 73.37%. On the pure size space, refinement recovers the static prior's shortfall relative to parameter count, while remaining tied with the strongest capacity proxies within noise. The resulting framework combines cross-space ranking robustness with low-cost architecture selection.

---


### 183. [Guided Super-Resolution of Digital Elevation Models with Diffusion-Based Image Generators](https://arxiv.org/abs/2609.11886)

**<font color=#1a73e8>作者：</font>** Armand Mihai Nicolicioiu, Dominik Narnhofer, Nando Metzger 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution digital surface models (DSMs) play an important role in urban analysis, 3D building reconstruction, and infrastructure monitoring, yet their availability remains limited due to the high cost and complexity of data acquisition. In contrast, coarse DSMs from commercial satellite missions are widely accessible, and high-resolution optical imagery is increasingly available from aerial and satellite platforms. We address the resulting mismatch in spatial resolution and propose a DSM superresolution approach that enhances 5 m DSMs to 0.5 m resolution, using guidance from high-resolution spectral images. Our method employs denoising diffusion to transfer information that is visible only in the image, like crisp outlines and detailed roof structures, into the elevation maps. In this way, surface details are reconstructed more accurately than with conventional interpolation or filtering techniques. Experiments on several cities in Central Europe demonstrate that the proposed approach produces high-quality DSMs with improved structural detail and accurate surface geometry. Our results highlight the potential of guided super-resolution with foundational image priors as a means of reconstructing high-resolution surface models.

---


### 184. [3D Point Splatting for mmWave Radar Novel View Synthesis](https://arxiv.org/abs/2609.11894)

**<font color=#1a73e8>作者：</font>** Adnan Armouti, Yixuan Gao, Rajalakshmi Nandakumar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Solving novel view synthesis (NVS) for millimeter-wave (mmWave) radar requires a renderer that is physically faithful, complex-valued, and multi-viewpoint-tractable. No prior method achieves these three properties simultaneously. Differentiable Monte Carlo (MC) ray tracers implement the radar forward model directly with explicit material modeling and complex outputs, but do not scale to the multi-view optimization NVS demands. Optical-NVS ports of NeRF, hash grids, and 3D Gaussians train fast but discard phase and replace explicit material modeling with opaque learned features, restricting them to power-only range-azimuth (RA) magnitudes. We propose 3D Point Splatting (3DPS), the first differentiable point renderer for radar, derived directly from the standard solid-angle form of the radar equation. Each oriented 3D point carries an ITU-R P.2040 material model, evaluated in closed form, with the resulting complex phasor splatted into range bins through a precomputed point spread function (PSF). The complex-valued output makes the renderer product-agnostic. The same optimized scene yields analog-to-digital converter (ADC), complex range profile (CRP), and RA outputs through standard fast Fourier transform (FFT) pipelines without retraining for each format. On six outdoor ColoRadar scenes, 3DPS reaches 0.587 mean Pearson correlation on held-out RA images. This is between 1.7x and 5.2x the three optical-NVS baselines (RadarSplat, Radar Fields, DART). Training takes approximately 3 minutes per scene on a single RTX 4090.

---


### 185. [TART: A Modular Tool for Technique-Aware Audio-to-Tablature Guitar Transcription](https://arxiv.org/abs/2609.11904)

**<font color=#1a73e8>作者：</font>** Akshaj Gupta, Hwi Joo Park, Andrea Guzman 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic Music Transcription (AMT) for guitar remains limited by three challenges: existing systems often fail to capture expressive techniques such as slides, bends, and percussive hits; they often assign notes to incorrect string-fret combinations; and they are typically trained on clean recordings, limiting their generalization to noisy real-world audio. To address these challenges, we propose TART, a modular four-stage audio-to-tablature pipeline consisting of (1) an audio-to-MIDI transcription model, (2) an expressive technique classifier, (3) an audio-conditioned T5 encoder-decoder for string-fret assignment, and (4) an automated tablature generator. We evaluate TART in a zero-shot setting on GuitarSet, EGDB, and two augmented benchmarks, Noisy GuitarSet and Noisy EGDB. Averaged across these four benchmarks, TART achieves 81.35% audio-to-MIDI F50 (+6.67 points over the best prior baseline), 71.8% string-fret Tab F1 (+8.5 points over the best prior baseline), and 54.08% end-to-end Tab F1. To our knowledge, TART is the first framework to generate guitar tablature with both fingering and expressive technique annotations directly from guitar audio.

---


### 186. [From Protocols to Evidence: Bounded Claims for AI in Service of the Common Good](https://arxiv.org/abs/2609.11910)

**<font color=#1a73e8>作者：</font>** Nitesh V. Chawla, Paulo Benanti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence does more than create a governance problem. It can also reveal where institutions have already failed to provide responsiveness, belonging, care, and accountability. Once deployed, AI becomes an intervention in those conditions. It can repair, compound, substitute for, or conceal the failures it encounters. Responsible AI must therefore evaluate both the system and the institutional rupture into which it is introduced. The move from principles to protocols is already underway. The EU AI Act, NIST AI RMF, ISO/IEC 42001, and assurance practices translate commitments into roles, requirements, records, oversight, and assessment. The harder questions are what these protocols actually establish, whose power they leave untouched, and where measurement must stop. Pope Leo XIV's Magnifica Humanitas provides a broader moral frame centered on dignity, technological power, and the common good. Drawing on that frame, we develop a rupture test that links institutional baselines to system evaluation. We distinguish evidence-bounded deployment, which limits claims to what has actually been evaluated, from measurement-bounded governance, which records constraints that favorable evidence cannot override. Within those limits, RISE AI provides an architecture for making bounded, evidence-based claims about Responsibility, Inclusivity, Safety, and Empowerment. Responsible AI requires better engineering, institutional repair, and continued moral and political judgment.

---


### 187. [Artificial Id: Drive and Persistent Alignment in Agentic AI](https://arxiv.org/abs/2609.11911)

**<font color=#1a73e8>作者：</font>** Yakov Pyotr Shkolnikov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic AI is moving from bounded task execution toward systems that retain consequential state, continue operating and adapt across task boundaries. That shift creates a control problem that current harnesses largely solve by hand: objectives, retries, verification, stopping rules and other behavioral transitions are specified externally. We propose an artificial id, an adaptive internal drive for determining whether behavior should continue, stop or change. In a minimal virtual Petri-dish experiment, a controller too small to perform general-purpose reasoning and receiving no task-specific behavioral objective develops useful control through differential persistence. The same mechanism selects an unintended physical strategy when that behavior persists better and later replaces a learned sensor mapping when its environmental meaning changes. These results show that adaptive direction can emerge without being explicitly specified as a behavioral objective. The same persistence that makes such adaptive agency useful can also allow misalignment, corrupted state and unintended behavior to persist across task boundaries. A scalable artificial id would carry consequential state and adaptive drive across those boundaries, making alignment a property of the continuing agentic system rather than of a model response or single trajectory. Such systems require a persistent alignment boundary over trusted observations, consequence channels, persistent state, authority, identity, provenance and hard constraints.

---


### 188. [Distance generalization in transformers: why bother with positional encoding?](https://arxiv.org/abs/2609.11913)

**<font color=#1a73e8>作者：</font>** Daniel Henrik Nevermann, Claudius Gros  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Out-of-distribution length generalization, namely to extrapolate a task from short to longer context, has been studied intensively for transformers. Here we focus on distance generalization, which probes performance when inter-token distances are changed between training and inference, while keeping a fixed context length. We construct two synthetic delay copy tasks, both involving finite distances between source and recall, where tokens are copied either fully or selectively, and test models on delays unseen during training. We address three questions: (A) Do positional encoding schemes such as RoPE and ALiBi improve distance resolution relative to no positional encoding (NoPE)? (B) How does data diversity, the number of inter-token distances seen in training, affect performance? (C) When is distance transfer learning positive or negative? We present a thorough investigation, finding that it is paramount to improve our understanding of the underlying mechanisms.

---


### 189. [General Quantification of Covariate and Concept Shifts](https://arxiv.org/abs/2609.11918)

**<font color=#1a73e8>作者：</font>** Hongbo Chen, Li Charlie Xia  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generalization under distribution shift remains a core challenge in modern machine learning, yet existing learning bound theory is limited to narrow, idealized settings and is non-estimable from samples. In this paper, we bridge the gap between theory and practical applications. We first show that existing definition of concept shift breaks when the source and target supports mismatch. Leveraging entropic optimal transport, we propose a key notion: $\gamma^{*}\!$-concept shifts, and derive a general error bound unifying covariate and $\gamma^{*}\!$-concept shifts, which applies to broad loss functions, label spaces, and stochastic labeling. We further develop estimators for these shifts with concentration guarantees, and the DataShifts algorithm, which can quantify distribution shifts and estimate the error bound in most applications - a rigorous and general tool for analyzing learning error under distribution shift.

---


> [!TIP]
> 当前位于：**151-189**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-189**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
