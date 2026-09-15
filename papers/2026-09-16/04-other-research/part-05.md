# 📦 其他研究 | 2026年09月16日

> 本类共 **416** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

---

### 201. [Cryptanalytic Extraction of Neural Networks Without Known Architecture Assumption](https://arxiv.org/abs/2609.14379)

**<font color=#1a73e8>作者：</font>** Yantian Shen, Yi Chen, Anyu Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cryptanalytic extraction attacks recover the parameters of a neural network given only black-box access to its raw output. However, all existing attacks rely on a fundamental assumption: the attacker knows the network architecture. For example, regarding ReLU activation-based fully connected networks, the network depth and the dimension of each hidden layer are known.
In this paper, we study whether this assumption can be removed. We focus on ReLU fully connected networks and propose a guess-and-determine framework that recovers the architecture and the parameters jointly. The core of our approach is a simple but powerful observation: dimension guessing leaves architecture-sensitive traces in the parameter recovery process. We identify two such traces: (i) a \emph{zero suffix} in the merged weight vectors produced by signature recovery, whose length reveals the number of excess guesses; and (ii) an \emph{equality pattern} in the preimage-based sign recovery, which occurs only when the dimension guess is correct. These two signals give rise to two complementary recovery routes. We further propose two criteria for identifying the second-to-last layer, which is necessary for terminating the guessing process. We implement end-to-end attacks on a wide range of ReLU networks, including both expansive and non-expansive architectures. To the best of our knowledge, this is the first cryptanalytic extraction attack that removes the assumption of known network architecture.

---


### 202. [Contour-Guided Spectral Routing for Robust Real-Time Pedestrian Detection](https://arxiv.org/abs/2609.14383)

**<font color=#1a73e8>作者：</font>** Sam Williams, Yuan Xiang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time pedestrian detection in driving scenes is constrained by three coupled failure modes: tiny targets lose discriminative evidence, occlusion weakens geometric support, and weather or illumination changes distort appearance statistics. We formulate the detector through a unified \emph{contour-guided spectral routing} view rather than treating frequency processing, attention, and boundary reasoning as independent add-ons. The detector routes information in a prescribed order: spatial evidence is first augmented with global spectral context, deep representations then exchange spatial and spectral cues, and cross-scale fusion is finally conditioned on boundary--semantic disagreement. This ordering yields a compact representation pipeline in which low-frequency context stabilizes global structure while high-frequency evidence protects small-object contours. We further retain a wavelet-subband training transformation that perturbs low- and high-frequency coefficients independently, targeting appearance shifts caused by fog, rain, snow, and low illumination. The formulation exposes a single routing variable at each stage and distinguishes reusable signal transforms from the task-specific policy that decides where each signal is injected. On CityPersons, the proposed detector obtains 70.4 AP$_{50}$ and 44.2 AP$_{50:95}$, compared with 68.1 and 42.2 for RT-DETR, while the full wavelet-augmented configuration reaches 71.1 and 44.6.

---


### 203. [Newton Deep Unfolding for Compressed Sensing](https://arxiv.org/abs/2609.14391)

**<font color=#1a73e8>作者：</font>** Changhua He, Xianchao Xiu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Compressed sensing (CS) reconstructs images from highly limited measurements, but existing deep unfolding methods are typically driven by first-order optimization and weakly exploit the optimization states generated during reconstruction. To address these limitations, we propose a Newton deep unfolding network (NDU-Net), which, to the best of our knowledge, is the first deep unfolding framework that leverages second-order optimization for CS reconstruction. Specifically, NDU-Net introduces a Newton update (NU) module to estimate Newton-type update directions and generate optimization states that characterize the current reconstruction process. Furthermore, a Newton-guided multi-scale prior (MP) module is designed to incorporate these optimization states into multi-scale feature restoration, thereby enabling the learned prior to adapt to the current reconstruction stage. Experimental results under different CS ratios confirm that our proposed NDU-Net achieves promising reconstruction performance and exhibits enhanced robustness. Our code is available at this https URL.

---


### 204. [Policy Loopholes in Agent Evaluation: When Policy Ambiguity Masquerades as Agent Error](https://arxiv.org/abs/2609.14400)

**<font color=#1a73e8>作者：</font>** Hongliu Cao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent benchmarks evaluate policy compliance but assume each policy determines a unique correct action. Natural-language policies can violate this assumption through silence, ambiguity, or contradiction, admitting multiple defensible readings that a single gold trajectory cannot capture. Auditing two $\tau^2$-bench domains, we develop a taxonomy of such policy loopholes and show that affected tasks produce unreliable scores: they lower scores across different models in different ways and make every model less consistent across repeated trials. A cross-domain comparison reveals that exploitability requires both policy ambiguity and tool permissiveness: when policy complexity exceeds what tools can enforce, agents resolve gaps inconsistently and scores become unreliable. Policy specification quality sets the ceiling on evaluation quality. Benchmark developers should audit policies before collecting gold annotations.

---


### 205. [Lightweight Generalized DeepFake Face Detection with WAVIE: Wavelet Augmented Vision Intermediate Embeddings](https://arxiv.org/abs/2609.14437)

**<font color=#1a73e8>作者：</font>** Arya Pulkit, Aditya Ruhela, Akarshan Kapoor 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deepfake detection systems often exhibit significant performance degradation when deployed on unseen manipulation methods, limiting their reliability in real-world multimedia environments. This lack of generalization poses critical challenges for misinformation mitigation, digital forensics, and human-centric AI systems. Existing detectors perform well on the forgery methods they are trained on, but their accuracy drops sharply on unseen pipelines. To bridge this generalization gap, we propose WAVIE (Wavelet Augmented Vision Intermediate Embeddings), an end-to-end architecture that combines complementary spatial and frequency cues on top of a frozen CLIP backbone. WAVIE projects intermediate transformer embeddings through a lightweight learnable module, applies a three-level Daubechies-6 (db6) discrete wavelet transform (DWT), refines the low-frequency branch while preserving the high-frequency branch, reconstructs the feature via inverse DWT, and performs classification.
Trained only on FaceForensics++, WAVIE achieves AUROC = 0.852 on Celeb-DF-v1, 0.852 on Celeb-DF-v2 and 0.831 on WildDeepFake (WDF) at the frame level, outperforming several state-of-the-art generalization baselines. Extensive ablation studies confirm the importance of both the wavelet module and the intermediate-feature aggregation for cross-dataset performance, highlighting the necessity of jointly leveraging spatial and frequency domains. These results position WAVIE as a strong baseline for deepfake detection in the wild.

---


### 206. [Context-Aware Mutual Learning for Blind Image Inpainting and Beyond](https://arxiv.org/abs/2609.14439)

**<font color=#1a73e8>作者：</font>** Haoru Zhao, Yufeng Wang, Zhaorui Gu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Blind image inpainting, aiming to recover contaminated images in the case of unknown masks, is a challenging task. Motivated by the perspective of human vision and knowledge, blind image inpainting can be decomposed into two stages: mask estimation and image inpainting based on the estimated mask. The two-stage idea exhibits evident advantages in enhancing inpainting quality and augmenting the generalization capability of unknown real-world contamination by explicitly employing the estimated mask for image inpainting compared to one-stage scheme. This two-stage idea has also been intuitively implemented. However, existing two-stage methods excessively emphasize the unilateral relationship of mask estimation to image inpainting, and may overlook the mutual relations between them. Specifically, mask estimation can provide more contextual semantics for image inpainting to strengthen the understanding of semantics, and image inpainting can offer more contextual details (e.g., textures and edges) for mask estimation to improve the learning of details. In this work, we propose a novel Context-Aware Mutual Learning (CAML) framework for blind image inpainting that joints mask estimation and image inpainting to mutually exploit contextual information. In the CAML framework, we design the Inpainting-Guided Context-Mutual (IGCM) learner to acquire the complementary contextual details from image inpainting for assisting mask estimation, and the Estimation-Guided Context-Mutual (EGCM) learner to strengthen the understanding of contextual semantics from mask estimation for assisting image inpainting. Ablation studies validate the efficacy of our CAML. Extensive experiments show that our CAML achieves state-of-the-art performance on both blind image inpainting and additional vision tasks, i.e., snow removal, shadow removal, and watermark removal, indicating its superiority.

---


### 207. [From Visual Attribution to Clinical Reasoning: Explainable Parkinson's Disease Screening from Hand-Drawn Patterns](https://arxiv.org/abs/2609.14441)

**<font color=#1a73e8>作者：</font>** Aritra Dey, Utsav Kumar Nareti, Chandranath Adak 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Parkinson's disease (PD) manifests early neuromotor impairments that become observable in controlled hand-drawn patterns such as spirals and meanders, where tremor-induced oscillations, stroke irregularity, and curvature instability reflect underlying motor degradation. In this work, we present an explainable framework for PD screening from offline hand-drawn patterns that integrates discriminative visual modeling with clinically grounded reasoning. The predictive model captures distributed structural distortions and fine-grained texture variations. It is evaluated under subject-disjoint protocols to ensure reliable generalization. To move beyond black-box classification, we introduce a multi-stage explainability pipeline that combines visual attribution with structured symptom abstraction. Salient regions are identified using attention- and gradient-based localization, followed by extraction of clinically meaningful motor descriptors quantifying contour roughness, curvature irregularity, stroke variability, and tremor-frequency energy. These descriptors are subsequently translated into coherent clinical rationales through a language-based reasoning module, linking model evidence to established PD symptomatology. By bridging visual attribution and clinical interpretation, the proposed framework advances interpretable document intelligence for neurological screening using hand-drawn patterns. Experimental results on publicly available Parkinson's disease handwriting datasets demonstrate competitive predictive performance and clinically consistent explanations.

---


### 208. [Towards Identifying the Dataset Biases Causing Phantom Transfer](https://arxiv.org/abs/2609.14449)

**<font color=#1a73e8>作者：</font>** Jonas Jürß, Pietro Liò  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent work has shown that a teacher model can transfer a bias to a student through a dataset from which every explicit reference to that bias has been filtered out, and that no data-level defense reliably removes or detects it even when knowing what bias to look for. Aiming to shed light on the hidden traces of these biases, we show that a simple signature based on Sentence BERT embeddings can identify the topic of such a bias with a Matthews correlation coefficient of 0.83 if the teacher model used by the attacker is known and 0.46 if it is not. Additionally, we observe that different teacher models appear to express the same bias through different vocabulary.

---


### 209. [Follow the Geometry, Not the Model: Cold Start Semi-Supervised Learning](https://arxiv.org/abs/2609.14451)

**<font color=#1a73e8>作者：</font>** Itai David, Daphna Weinshall  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern semi-supervised learning (SSL) couples pseudo-label generation and classifier training, using the classifier's own confidence to select the pseudo-labels that are then used to update the model. In the cold-start regime, where at most a few labels per class are available, this coupling is ill-posed, since the classifier cannot supervise itself before it has learned.
To address this problem, we propose VAST (Veracity-Aware Semi-Supervised Training), which decouples these two stages. Probabilistic beliefs over the unlabeled set are first inferred directly from the geometry of a frozen self-supervised embedding and only then distilled into an inductive classifier.
The construction rests on the Veracity Matrix, a kernel-based structure that aggregates label evidence across the data manifold and admits an interpretation as a Dirichlet posterior under a per-observation powered-likelihood model. Additionally, we introduce Veracity Propagation, a self-terminating belief-spreading step that extends coverage beyond the kernel neighborhood of the labeled set.
Under a controlled protocol in which all methods receive identical frozen embeddings and labeled sets, VAST outperforms the strongest graph-based SSL baselines at every operating point across three datasets, with statistically significant gains in 7 of 9 comparisons, while producing a deployable inductive classifier rather than requiring transductive graph inference. Compared with end-to-end confidence-gated SSL, we further find that these methods underperform in this setting and, in our experiments, do not consistently exceed labeled-only performance.

---


### 210. [AlayaVista: Streaming World Modeling from Panoramic States to Perspective Video](https://arxiv.org/abs/2609.14462)

**<font color=#1a73e8>作者：</font>** Jiaming Tan, Mingliang Zhai, Zhen Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Interactive video world models must maintain broad scene context under camera motion while producing high-fidelity observations with low latency. Existing approaches face a representation trade-off: perspective models operate on local views and must preserve off-screen content over long rollouts, whereas broader spatial coverage is typically obtained by synthesizing full-sphere videos or constructing explicit 3D representations. Motivated by the complementary roles of global context and selective local acuity in visual perception, we present AlayaVista, a camera-controllable streaming video world model that decouples panoramic world evolution from perspective observation synthesis. Given a single perspective image, AlayaVista constructs a 360-degree scene prior using a pretrained panorama expansion model and then evolves the scene as a camera-conditioned panoramic latent state. A latent viewport renderer maps this state to the requested perspective video latents, while a perspective refiner restores details, suppresses artifacts, and performs super-resolution. To support efficient streaming, we adapt the panoramic generator to chunk-autoregressive generation and distill both panoramic generation and perspective refinement into few-step processes. To provide the supervision required by this design, we construct MUGEN, a large-scale real-world panoramic video dataset containing 1,318 hours of videos at resolutions of at least 4K, together with rich semantic and geometric annotations.

---


### 211. [DynEoMT: Learning Object Dynamicity from Online Segmentation Queries](https://arxiv.org/abs/2609.14466)

**<font color=#1a73e8>作者：</font>** Calvin Galagain, Martyna Poreba, François Goulette  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video segmentation models recognize and track objects over time, but they do not indicate whether each segmented region moves independently of the observing camera. This dynamicity attribute cannot be inferred from semantics alone and is confounded by camera ego-motion. We introduce \method, an online framework that augments query-based video segmentation with region-level dynamicity prediction. It jointly produces the original segmentation outputs and a dynamic or static state for each predicted region. At inference, DynEoMT uses only the current frame and propagated queries, without optical flow, depth, camera pose, previous RGB frames, or feature maps. Because established video segmentation benchmarks do not annotate this attribute, we also introduce a class-agnostic offline supervision pipeline using camera-compensated optical flow and confidence-aware temporal filtering. Across VIPSeg, OVIS, YouTube-VIS 2022, and VSPW, DynEoMT achieves balanced accuracies of 84.3, 68.0, 68.6, and 87.6, respectively, while largely preserving segmentation performance. These results show that segmentation-region dynamicity can be learned from propagated queries, enabling its online prediction without a dedicated motion-processing pipeline at inference. The complete code will be released as open source to enable full reproduction of the method and experiments.

---


### 212. [PRI-Net: A Lightweight Multimodal Framework for 3D UAV Localization](https://arxiv.org/abs/2609.14469)

**<font color=#1a73e8>作者：</font>** Zhixuan Chen, Jialiang Lu, Zhong Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D localization of unmanned aerial vehicles (UAVs) remains challenging for existing multimodal approaches due to sparse LiDAR geometry, modality-imbalanced fusion, and redundant feature transmission over constrained edge-to-server links. To address these limitations, we propose PRI-Net, an efficient and lightweight multimodal fusion framework for UAV localization that integrates point cloud splatting, residual attention fusion, and an information bottleneck. Specifically, a 3D point cloud splatting (3DPCS) strategy is introduced to transform sparse LiDAR observations into geometrically consistent dense depth maps. A residual attention fusion (RAF) module is then designed to alleviate modal bias by using an image branch for coarse estimation and a gated fusion branch for refinement. In addition, a multimodal information bottleneck (MIB) module compacts features by filtering task-irrelevant redundancy. Experiments show that PRI-Net achieves high localization accuracy with lightweight architectures, while reducing feature dimensionality and improving edge-to-server UAV sensing efficiency and robustness.

---


### 213. [Quantifying Observable High-Frequency Swapping on Arbitrum](https://arxiv.org/abs/2609.14481)

**<font color=#1a73e8>作者：</font>** Shijian Chen, Ya Chen, Jing Cai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Layer-2 rollups have reshaped Ethereum's transaction economy by replacing mempool competition with deterministic sequencing, sub-second block times, and negligible gas fees. While these properties suppress classical Miner/Maximal Extractable Value (MEV), they give rise to a new and previously unrecognized behavioral regime. In this paper, we introduce the concept of High-Frequency Swapping (HFS), referring to continuous single-hop swaps at machine cadence within decentralized exchanges. Despite its growing footprint, this phenomenon has not been systematically identified or quantified in prior work. We conduct a large-scale measurement of HFS on Arbitrum, using 18 months of full-chain data (Jan. 2023--Jun. 2024). Specifically, we construct a reproducible pipeline that isolates voluntary single-swap transactions, attributes them to the swapper level, and classifies HFS behavior through inter-arrival dynamics. The analysis uncovers 477 distinct HFS swappers responsible for nearly 30 million swaps and over $10^{11}$ USD in notional volume. Our study conducts a comprehensive empirical investigation of HFS from multiple perspectives. We begin with a global overview of activity patterns, and then examine temporal dynamics, swapper identity, token coverage, and venue concentration, and explore swap size, time gap, and order direction. Finally, we explore case-level behavior, including stablecoin arbitrage, CEX-DEX execution gaps, and short-horizon round-trip trading. Across these dimensions, we identify consistent structural regularities that distinguish HFS from conventional retail or arbitrage activity. This work provides a large-scale address-level empirical characterization of High-Frequency Swapping on Arbitrum and a broad empirical foundation for future research on decentralized market microstructure.

---


### 214. [MCIQA-2K: A Multi-Dimensional Dataset and No-Reference Quality Assessment Benchmark for Colorized Images](https://arxiv.org/abs/2609.14495)

**<font color=#1a73e8>作者：</font>** Yunkai Zhuang, Qihang Yan, Zicheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image colorization is an inherently ill-posed task, since a single grayscale image may correspond to multiple plausible colorized results. Consequently, conventional full-reference image quality assessment (IQA) metrics fail to accurately reflect human perceptual preferences for colorized images. In this paper, we present MCIQA-2K, a large-scale multi-dimensional benchmark specifically designed for no-reference quality assessment of colorized images. We construct a dataset containing 2,000 colorized images generated by five representative colorization models, together with human annotations across three perceptual dimensions: color smearing, semantic color misalignment, and global naturalness. Building upon the proposed benchmark, we further introduce MCIQA, a dedicated multi-branch NR-IQA framework for colorized images. Extensive experiments demonstrate that MCIQA significantly outperforms existing full-reference and no-reference IQA methods on the proposed benchmark, while also exhibiting competitive generalization capability on several widely-used IQA datasets. The dataset and code are publicly available at this https URL.

---


### 215. [When does a scaling result justify a different allocation? A critical review of resource-allocation evidence for AI systems](https://arxiv.org/abs/2609.14500)

**<font color=#1a73e8>作者：</font>** Seyed Morteza Emadi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI scaling studies increasingly evaluate systems that combine a pretrained model with retrieval, search, verification, tools, and interaction. Yet a higher score under a larger budget does not by itself show where additional resources are best spent. This critical integrative review asks when a reported scaling result supports a resource-allocation decision. It compares evidence across pretraining, test-time computation, retrieval, and agent evaluation, distinguishing the performance of a tested procedure from the best performance achievable under a resource limit. The synthesis shows that three mismatches recur across this evidence: success counted before an answer is chosen, information a deployed system will not have, and costs left out of the comparison. A capability surface expresses performance as a function of budgets, mechanisms, and available information. Worked analytical examples show how the evaluation metric, deployment volume, selection rule, and stopping policy can alter an allocation conclusion. A resource envelope provides a structured record of the task, development and run-time resources, information access, and procedure behind a reported score. Its application to a published comparison illustrates which conclusions the evidence supports and which deployment questions remain unresolved. The resulting framework specifies the comparisons needed to choose among feasible systems and motivates experiments on the transfer of allocation rules across tasks and operating conditions. It does not propose a universal scaling law or infer general intelligence from benchmark gains.

---


### 216. [Should All Noises Be Treated Equally: Impact of Input Noise Variability on Neural Network Robustness](https://arxiv.org/abs/2609.14504)

**<font color=#1a73e8>作者：</font>** Salma Alsinan, Maksim Makarenko, Sixiu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Geophysical data collected from active field sites are often contaminated by complex and heterogeneous noise, obscuring weak seismic events, and complicating automated interpretation. Although deep learning offers promising solutions for seismic processing, its performance is highly sensitive to the nature of training noise, especially under out-of-distribution (OOD) conditions. This study investigates the influence of noise parameters, such as type, scale, and complexity on the performance, generalization and robustness of neural networks in two geophysical tasks: first break picking and denoising. We simulate seismic-while-drilling data and apply controlled input source noise augmentation using stochastic generators to vary the noise characteristics. Different neural networks are trained on fixed noise types and scales, then evaluated across both seen and unseen noise scenarios. We incrementally increase the complexity of the noise by introducing compound noise mixtures and assess the performance of the model under increasingly challenging OOD conditions. This yields a robustness matrix that captures the generalizability of each model relative to its training configuration. Results indicate that larger noise scales boost generalization, and that effective alignment between noise type, task complexity, and architecture is key for maximizing generalization gains. In addition, training with compound noises mitigate weaknesses associated with single-noise training, acting as an additional implicit regularizer to improving robustness. These findings highlight key factors influencing model resilience in noisy geophysical environments and offer guidance for developing deep learning models that generalize effectively across diverse and unpredictable noise conditions.

---


### 217. [Beyond Scene Description: Multi-Agent Orchestration for Non-visual Access to Virtual Worlds](https://arxiv.org/abs/2609.14512)

**<font color=#1a73e8>作者：</font>** Toqeer Ali Syed, Ali Akarma, Adeel Ahmad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Virtual worlds now host classrooms, meetings, conferences, shops, and social venues, and nearly every interaction they expose assumes a user who can scan a three-dimensional scene, follow avatars, and read floating panels. Blind and visually impaired (BVI) users are left with assistive tools that each solve one task in isolation: naming an object, reading text, describing a scene, or planning a route. A live virtual room defeats that model: obstacles, speakers, gestures, chat, slides, and notifications arrive together, and a tool that narrates all of them trades a visual barrier for an auditory one. This paper presents MetaBlind, an architecture that distributes nonvisual access across eight specialized agents, spanning perception, navigation, social and object interaction, communication, safety and trust, memory, and personalization, and that places an Accessibility Orchestrator between those agents and the user. Agents publish candidate information into a shared accessibility context instead of speaking to the user directly. The orchestrator scores each candidate on safety relevance, goal relevance, urgency, confidence, user relevance, and estimated listening load, then releases only the items it judges relevant at that moment through speech, structured audio, or haptic output. We give the selection step a formal statement, specify the orchestration cycle as an algorithm, and define an evaluation protocol against a single-agent assistant. MetaBlind is reported at the design stage, with no prototype measurement or user study, and the protocol states which outcomes would support the design and which would refute it.

---


### 218. [OptoAgent: A Trustworthy Multi-Agent Framework for Opportunistic Vision Micro-Screening in Classroom Environments](https://arxiv.org/abs/2609.14514)

**<font color=#1a73e8>作者：</font>** Toqeer Ali Syed, Ali Akarma, Adeel Ahmad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A child with reduced distance vision often does not know that anything is wrong. Children adapt, move closer, and rarely report the difficulty, so the problem can survive years of schooling before an adult notices. School screening addresses part of this, but it runs on a schedule, depends on staffing, and is separated from the classroom moments where the difficulty appears. Smartphone and web-based acuity tests have widened access, yet every one of them still needs somebody to start a test. We present SightSentinel, an architecture that turns a wall display a child already reads from into a recurring screening site. Ordinary educational content carries short calibrated optotype probes, and eight specialized agents divide the work. Perception agents recover viewing distance, recognition accuracy, approach behavior, gaze stability, response latency, and interocular difference from each encounter. A quality agent discards observations taken under bad geometry, poor lighting, or inattention. A longitudinal agent accumulates only the surviving evidence against the child's own baseline, and an orchestrator reports a Vision Concern Score routed through a safety gate whose output range excludes diagnosis, refraction, prescription, and reassurance. The design question is whether many cheap, noisy, well-gated encounters can reach a referral decision that one scheduled test reaches late or misses. We state the formulation, the architecture, a four-stage validation protocol against clinical reference standards, and the conditions under which the approach should be rejected.

---


### 219. [CGGT: Curve-Grounded Geometry Transformer for 3D Parametric Curve Reconstruction](https://arxiv.org/abs/2609.14521)

**<font color=#1a73e8>作者：</font>** Zhirui Gao, Renjiao Yi, Yunfan Ye 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering editable 3D parametric curves from 2D images is a fundamental challenge in computer graphics, bridging pixel-based perception and vector-based CAD modeling. Existing NeRF- and 3DGS-based methods often rely on dense calibrated views, precomputed 2D edge maps, and costly per-scene optimization, limiting their applicability to casually captured real-world inputs. We propose CGGT, a Curve-Grounded Geometry Transformer that directly grounds 3D-consistent 2D curve instances in the image space from sparse, unposed multi-view images. CGGT combines a geometry-aware transformer encoder for multi-view feature learning with a curve-aware masked-attention decoder for cross-view instance association. In a single forward pass, it predicts camera parameters, dense depth maps, and instance-level 2D curve masks, which are then lifted into 3D and refined through a fast parametric optimization stage to recover compact, editable 3D curve primitives. To support structured curve learning, we introduce Wireframe-100K, a large-scale dataset comprising 100,000 CAD models with diverse topologies, realistic multi-view renderings, and accurate parametric curve annotations. Extensive experiments show that our framework achieves substantial improvements in both reconstruction accuracy and efficiency, particularly under challenging sparse-view settings and in separating persistent 3D structural edges from view-dependent image edges caused by silhouettes, textures, and appearance variations. Despite being trained solely on synthetic data, CGGT generalizes well to real-world images, demonstrating its potential for practical CAD-style wireframe reconstruction from unconstrained visual inputs.

---


### 220. [Theseus in the Graph: Towards Traceable Multi-Hop Graph Navigation](https://arxiv.org/abs/2609.14528)

**<font color=#1a73e8>作者：</font>** Eduin E. Hernandez, Luis F. Garcia, Nurassyl Askar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-Hop Knowledge Graph Question Answering (KGQA) tasks require models to assemble relational evidence along paths in a KG to answer natural-language questions. However, existing KGQA systems typically focus on predicting the final answer without explicitly modeling or validating the intermediate reasoning steps, obscuring whether the correct answers arise from faithful multi-hop reasoning. To address this limitation, we re-frame multi-hop KGQA as a question-conditioned graph navigation problem. We refer to this formulation as THESEUS - Traceable Hop-wise Evidence SEarch in a Unified Semantics. In this setting, an agent receives a KG, a question, and a topic entity, and traverses a sequence of relations towards the answer, making the reasoning path explicit. To systematically study this formulation, we provide three key contributions. (i) We augment the existing KINSHIP and MQuAKE resources into navigation-ready KGQA datasets with annotated evidence paths and paraphrased questions. (ii) We design evaluation protocols to measure path fidelity, robustness to linguistic variation, and performance across multi-hop and multi-answer questions. (iii) We adapt established path-based KG completion agents - MINERVA, MultiHopKG, and SQUIRE - to operate on full question embeddings rather than symbolic single-relation queries, enabling their trajectories to be guided by natural-language semantics. Together, these contributions advance KGQA research toward systems where traceability is fundamental: answers are accompanied by explicit reasoning paths whose agreement with reference evidence can be systematically evaluated.

---


### 221. [Sharing standardized image-derived data in computational pathology using DICOM](https://arxiv.org/abs/2609.14530)

**<font color=#1a73e8>作者：</font>** Daniela P. Schacherer, Christopher P. Bridge, David Clunie 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Development and evaluation of computational pathology methods require access to large and diverse datasets. Over the past decade, various initiatives invested significantly into collecting, centralizing, and sharing pathology imaging data. In contrast, sharing of image-derived data such as region-of-interest delineations or segmentation masks is less well developed. In this work, we describe our approach to encoding and sharing image-derived pathology data in a standardized manner within the National Cancer Institute (NCI) Imaging Data Commons (IDC), a platform that hosts and provides public access to de-identified radiology and pathology data. The IDC relies on the Digital Imaging and Communications in Medicine (DICOM) standard for data harmonization, yet the adoption of DICOM for pathology image-derived content has remained largely unexplored until now. Here, we present five representative datasets harmonized by conversion from their original representations into DICOM and shared publicly in the IDC. We demonstrate the benefits of this harmonization, describe contributions to critical open-source tooling, and discuss technical considerations relevant to broader adoption of DICOM for pathology image-derived data.

---


### 222. [GNN4PPM: Multi-Target Predictive Process Monitoring with Relational Graph Convolutional Networks](https://arxiv.org/abs/2609.14534)

**<font color=#1a73e8>作者：</font>** Ana Costa, Johannes Mäkelburg, Luise Pufahl  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predictive Process Monitoring (PPM) aims at predicting at runtime and as early as possible the future states of a process execution. Common tasks include predicting the next event, the time to completion of a trace, and outcomes. Existing approaches typically consider an event from the perspective of the executed activities along with their timestamps and case identifiers. This leads to the disadvantage that in real-life settings, there is much more information recorded in the event log that is not captured or completely ignored when performing prediction tasks. We introduce GNN4PPM, an approach that predicts all next events along with their complete data payload at once. We represent event information in a heterogeneous knowledge graph that captures the event log as an RDF semantics, and train the embeddings with a Relational Graph Convolutional Network (R-GCN). Our approach is promising in comparison to existing solutions, and experiments with state-of-the-art solutions prove the accuracy and applicability of GNN4PPM in complex settings.

---


### 223. [Selecting k Paths with the Minimum Longest Path Length in the Stochastic Semi-Bandit Setting](https://arxiv.org/abs/2609.14557)

**<font color=#1a73e8>作者：</font>** Shunsuke Aoki, Atsuyoshi Nakamura  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When performing parallel data transmission through a network using multiple paths, it is practically important to minimize the maximum transmission time among the selected paths. This study addresses an online problem in which $k$ paths from an origin vertex to a destination vertex must be selected at each time step within a network represented as a directed graph. Here, the number of paths going through each edge in each parallel data transmission is limited to its capacity, and the time required for transmission is determined stochastically. We formulate the semi-bandit problem of selecting a set of paths to minimize the maximum traversal time among the selected paths and propose an algorithm to solve it.

---


### 224. [Small Object Detection in Drone Aerial Imagery with LAF-YOLOv10](https://arxiv.org/abs/2609.14560)

**<font color=#1a73e8>作者：</font>** Quratulain Nayeem, Fahmina Taranum, Mohammed Mudassir Uddin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> General-purpose object detectors lose accuracy on UAV footage, where targets span only a handful of pixels and onboard compute is limited. Prior work composes independently-validated architectural techniques into one detector, assuming gains reported in isolation transfer once combined. We stress-test that assumption directly. LAF-YOLOv10 integrates four techniques into YOLOv10n: a Partial Convolution C2f (PC-C2f) backbone block, an Attention-Guided Feature Pyramid Network (AG-FPN), a P2 detection head replacing the large-object P5 head, and Wise-IoU v3 regression, asking whether their combined effect matches what each contributes alone. We train LAF-YOLOv10 three times (seeds 42, 123, 256) on VisDrone-DET2019, benchmark against unmodified YOLOv10n, and use TIDE error decomposition, per-category breakdown, per-component ablation, attention/loss comparisons, zero-shot transfer to UAVDT, and held-out/test-dev evaluation to localize where the combination succeeds or fails. Composability does not hold here. LAF-YOLOv10 reaches 24.0+/-0.4% mAP@0.5 at 2.14M parameters, 7.8 points below YOLOv10n (31.8%), a deficit that transfers to UAVDT (-10.0 points) and is confirmed by held-out and test-dev evaluation (23.5%, 22.5%). Background false positives, localization error, and duplicate detections move in the direction AG-FPN and Wise-IoU were designed to push. Ablation traces the deficit to a specific source: the P2/-P5 head swap costs 2.5 points independently plus a 2.5-point interaction penalty when layered onto a backbone weakened by PC-C2f, whose own 2.0-point loss is consistent with a partial pretrained-weight transplant (73/150 backbone tensors transfer). The failure is attributable to a specific interaction, not the four components individually. Composability must be verified directly, not assumed. Code/checkpoints: this https URL.

---


### 225. [Domain-specific Pretraining Profile and Transformer Performance: Evidence from Modeling Digital Pragmatics in Arabic-English Code-switching](https://arxiv.org/abs/2609.14571)

**<font color=#1a73e8>作者：</font>** Fahad Al Hussen, King Saud University, Riyadh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This study highlights the role of domain-specific pretraining profile (DSPP) in Transformer performance for modeling digital pragmatics in Arabic-English code-switched discourse. It evaluates MARBERT and XLM-R(oBERTa), with BERT serving as a general-purpose baseline. The models were evaluated on their ability to classify context-sensitive pragmatic functions in code-switched social-media discourse. 11695 unique X posts were collected via Python and utilized for the study. The study employs a quantitative and qualitative NLP approach, following a supervised pipeline. Findings unveil that MARBERT consistently surpasses XLM-R with validation Macro F1 increasing from 0.39 to 0.84 and validation loss decreasing from 0.55 to 0.19. On an independent test set, it achieved 0.96 accuracy, 0.83 macro precision, 0.87 macro recall, and 0.85 Macro F1, while XLM-R achieved 0.92 test accuracy but a substantially lower Macro F1 of 0.52. This was also supported by class-level performance where MARBERT outperforms XLM-R considerably with F1 improvements ranging from +0.33 to +0.60, demonstrating a clear advantage in modeling Arabic digital pragmatics. The study concludes that Transformer performance depends more on DSPP than multilingual coverage alone, as the latter does not guarantee optimal performance on a highly specialized pragmatic classification task.

---


### 226. [A Building as a Repository: KIR, a Typed Intermediate Representation for Agent-Authored Building Information Models](https://arxiv.org/abs/2609.14578)

**<font color=#1a73e8>作者：</font>** Dmitry Kuklev  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autonomous agents that author building information models need more than access to a host API. They need a representation of what they intended, what a compiler decided on their behalf, what was refused, what was observed after execution and what remains unknown. We present KIR, a typed intermediate representation in which a building is authored as a program held in a versioned repository and lowered to host applications as build targets. KIR is organised around seven ways in which a generator writing into a stateful, partially observable host goes silently wrong, and gives each a representation in data: ambiguous selectors become typed refusals with candidates; defaults keep their provenance; obligations that will not be checked are named before execution; vacuous witnesses are rejected statically; a lost transaction response becomes the state UNCONFIRMED with a verify-before-retry rule; the reverse path obeys a census invariant; and decisions are bound by digest to the state they were made against. On a pinned snapshot with 83 operation contracts and Revit as the only backend, offline experiments refuse 29 of 42 stress-test programs with diagnostic codes and no uncaught exception, name 38 of 377 witness obligations as unwitnessable, admit 31 of 100 combinations of execution, witness and acceptance states under seven stated invariants, and find no vacuous witness in 219 certificate runs; a 60-storey tower is 11,263 characters as KIR against 3,709,235 characters of emitted C#. Native Revit runs are reported from project records and kept separate from reproduced results. A controlled comparison with agents that write host code directly is specified but not yet executed; it is the principal open question.

---


### 227. [Reverse Spatio-Temporal Disease Progression Modelling](https://arxiv.org/abs/2609.14590)

**<font color=#1a73e8>作者：</font>** Ulugbek Shernazarov, Moucheng Xu, Inomjon Ramatov  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Deep learning-based spatio-temporal disease progression models commonly overlook the incubation period of progressive diseases, limiting the use of those models in early interventions, which are vital for not easily reversible diseases such as Alzheimer's. This is because, the existing deep learning based longitudinal disease-progression models are almost always run forward: from an observed baseline they predict future decline. In many clinical settings, however, imaging begins only after pathology is suspected or already visible, the earlier, healthier patient-specific reference was never acquired. To address this, we propose to study reverse disease progression prediction: given later diseased anatomy, reconstruct the unobserved healthier anatomy that preceded it. We use a two-stage model in which a frozen 3D vector-quantised autoencoder defines a compact discrete latent space, while a Neural Ordinary Differential Equation (ODE) learns continuous-time dynamics in that space. A recurrent encoder reads late observations in reverse temporal order, initialises the latent state, and the ODE is integrated backwards across the trajectory. On a controlled Morpho-MNIST benchmark with a sinusoidal perturbation, our model successfully recovered the unseen previous states from later observations of the non-monotonic trajectory. On longitudinal brain MRIs from Alzheimer's Disease Neuroimaging Initiative, at the task to recover the previous unseen trajectory towards healthy states of the patients from observed later diseased states, our model outperforms the baselines that uses copy-nearest and mean-observed, with positive disease-reversal scores in every diagnostic stratum. We hope that our work can provide insights and tools towards discovering the incubation periods from single-shot scans, and developing early interventions of diseases based on imaging.

---


### 228. [Pathwise Individual Rationality in Federated Learning: A Mechanism-Architecture Co-Design](https://arxiv.org/abs/2609.14591)

**<font color=#1a73e8>作者：</font>** Amin Meghrazi, Srinivasan Parthasarathy, Andrew Perrault  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Participation in federated learning (FL) comes at a cost. Clients trade off privacy, communication, and compute costs for potentially greater gains in model efficacy. This paper explores this tradeoff under the aegis of individual rationality (IR) versus autarky, the basic game-theoretic requirement that the federation provide utility no worse than local training. Using the above as the design target, we examine pathwise performance of FL, as a per-round bound on cumulative surplus, not just as an asymptotic equilibrium guarantee under different models of client data distribution heterogeneity. Along this path, clients can remain below their local-training baseline for hundreds of rounds. The natural remedy is to cap each client's per-round contribution so that this shortfall stays bounded, and we prove that it backfires, collapsing learning even at low-to-modest heterogeneity.
We then propose a novel design that combines short-term participation guarantees with personalized model evaluation, while maintaining fair incentives. We provide a theoretical basis for this new approach and empirically demonstrate that clients can avoid short-term losses without harming overall performance, even under moderate data distribution heterogeneity; under severe heterogeneity, the design shows promising outcomes for clients compared to their local baseline at some cost in accuracy.

---


### 229. [AI Deployment Accountability Engineering: A Vision for Accountable AI in Safety-Critical Socio-Technical Systems](https://arxiv.org/abs/2609.14592)

**<font color=#1a73e8>作者：</font>** Murat Kantarcioglu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence systems are rapidly becoming critical components in healthcare, finance, public services, and other safety-critical domains. Yet the engineering practices used to evaluate these systems remain predominantly model-centric, emphasizing properties such as accuracy, robustness, fairness, and interpretability before deployment. These properties are necessary but insufficient once an AI system operates within an ever changing socio-technical environment characterized by distribution shifts, institutional constraints, human feedback loops, privacy requirements, and interactions among multiple AI agents.
This vision paper introduces AI Deployment Accountability Engineering (ADAE), a proposed AI engineering subdiscipline concerned with establishing measurable, continuous, and actionable accountability for deployed AI systems. ADAE treats accountability as a deployment-layer property rather than solely as a property of an individual model. It seeks to determine whether an AI-enabled system continues to operate within acceptable risk limits, identify the contexts in which failures emerge, attribute failures across interacting technical and human components, translate technical failures into downstream consequences, and support timely intervention.
We articulate a research agenda built around four interconnected pillars: structured discovery of context-dependent failure modes, privacy-preserving accountability measurement, system-level risk analysis for agentic AI, and translation of technical failures into operational, and institutional risks. The broader goal is to establish foundational principles, mathematical tools, and system architectures for accountable AI deployment across safety-critical applications.

---


### 230. [SENTINEL: A Multi-Pathway Architecture for Detecting Living-Off-the-Land APT Attacks on Windows Command Lines](https://arxiv.org/abs/2609.14593)

**<font color=#1a73e8>作者：</font>** Ahad Bin Islam Shoeb, Kamrul Hasan, Jamal Uddin Tanvin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Living-Off-the-Land (LOTL) is the dominant evasion technique of Advanced Persistent Threat (APT) actors, exploiting legitimate Windows utilities to conduct malicious operations without deploying custom malware and enabling state-sponsored campaigns to maintain persistent access within military and critical defense infrastructure for extended periods. Existing detection methods fail against obfuscated commands and multi-stage attack sequences, as demonstrated by the Volt Typhoon APT campaign, which maintained undetected access to U.S. critical infrastructure for over 18 months using exclusively signed Windows utilities. We present SENTINEL, a multi-pathway architecture integrating BERT-based semantic encoding, character-level CNN for obfuscation invariance, inter-command attention for multi-stage pattern recognition, and autoencoder-based anomaly scoring. Evaluated on a balanced Volt Typhoon benchmark derived from Microsoft and CISA threat intelligence advisories, SENTINEL achieves 92.0% accuracy on documented state-sponsored attack commands and 91.2% on obfuscated variants, compared to 74.0% and 72.0% for standalone BERT. Per-class analysis reveals that models achieving over 98% overall validation accuracy on imbalanced data exhibit only 44-58% malicious recall on balanced adversarial sets. Character-level processing contributes 5.6 percentage points of obfuscation invariance, and the 8.0 percentage point gap over augmentation-only baselines confirms structural architectural value beyond data-driven robustness alone.

---


### 231. [Diagnosing Temporal Misalignment in Multichannel Time-Series Classification with Minimum Description Length](https://arxiv.org/abs/2609.14595)

**<font color=#1a73e8>作者：</font>** Sebastian Buschjäger, Michael Frichert, Daniel Kuhe 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multichannel time-series classification commonly assumes synchronized sensor streams, although latency, clock drift, and preprocessing can introduce relative delays during data collection or after deployment. Existing synchronization solutions are often hardware-specific and difficult to apply retrospectively. Consequently, synchronization problems may remain undetected while classification performance is suboptimal. We introduce a classifier- and label-free diagnostic based on minimum description length (MDL). Our method applies candidate temporal shifts to sensor groups and measures how efficiently one group can be encoded through a representation of the remaining channels. An increased codelength indicates that the shift destroys shared temporal structure, whereas the minimum identifies the alignment most strongly supported by the data. Unlike learned synchronization methods, the diagnostic requires neither retraining nor a trusted aligned reference and can therefore test both training and deployment data for misalignments. Experiments on two controlled synthetic tasks and nine real-world datasets show that the metric exposes alignment structure and can recover accuracy under induced deployment drift. A whole-dataset audit further identifies stable nonzero MDL optima in established benchmarks including FordChallenge, Opportunity, PAMAP2, and UCIActivity, revealing potential systematic offsets that conventional model evaluation does not expose. Our method thus provides a general-purpose tool for detecting, understanding, and correcting temporal misalignment throughout the time-series learning pipeline. Our code is available under this https URL.

---


### 232. [Direct Conditional Transition Sampling for Diffusion Inverse Problems](https://arxiv.org/abs/2609.14596)

**<font color=#1a73e8>作者：</font>** Qi Yu, Hanlin Wu, Xiaohui Sun  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Training-free diffusion inverse solvers typically choose between local measurement guidance and costly clean-space posterior updates. Independent posterior refresh can improve global correction by sampling a clean conditional and re-noising it, but its practical realization requires probability-flow ODE integration and clean-space Markov chain Monte Carlo (MCMC). We propose Direct Conditional Transition Sampling (DCTS), a direct stochastic-flow approximation to the same ideal refresh target. Rather than explicitly drawing a clean sample, DCTS estimates the measurement-conditioned clean mean along a short inner path and transports Gaussian source noise directly to the next noisy state. A denoiser-compatible sufficient statistic and a covariance-scaled operator update enable this conditional-mean estimation. Experiments on four inverse problems demonstrate that DCTS achieves competitive reconstruction quality with up to $16.8\times$ speedups over competing methods.

---


### 233. [A note on goal-based hierarchical RL](https://arxiv.org/abs/2609.14605)

**<font color=#1a73e8>作者：</font>** Kevin Murphy  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The agent-centric general value function (ACGVF) construction of
\citet{tasse2026goal} lets the agent make two decisions that are
normally imposed by the environment or agent designer: which goal to
pursue and when to declare a goal as finished (in addition to
choosing the action). This is a very general framework that
subsumes almost all prior work on reinforcement learning, control
and planning, as well as more general formalisms proposed in the
cognitive sciences. However, it assumes the environment is fully
observed, i.e., that the observation is a sufficient statistic. In
\citet{murphy2025rl}, a general agent design was proposed where the
policy is based on an internal belief state $z_t$ and an internal
goal; however, the goals were assumed to be externally provided. In
this note, we unify and extend these two approaches using the
formalism of hierarchical hidden Markov models (HHMM) \citep{murphy2001hhmm}.

---


### 234. [SH-WRNN: Implicit Spherical Harmonics Weight Field Routing Neural Networks for Asymmetric Edge Intelligence](https://arxiv.org/abs/2609.14614)

**<font color=#1a73e8>作者：</font>** Zhibin Jiao, Xiangjing An  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning architectures remain rigidly built upon traditional fully connected layers. While networks scale up, few challenge this foundational root. In this work, we reshape this paradigm by transforming the core synapse weight matrix from static, discrete parameters into a differentiable, continuous field governed by spherical harmonics functions. We introduce the Implicit Spherical Harmonics Weight Field Routing Neural Network (SH-WRNN), which constrains weight matrices within a continuous parametric field instead of optimizing millions of localized discrete weights. When retrieving the weight matrix of the current layer, connection parameters are localized using latitude and longitude on a rectangular plane mapped from the continuous field. The latitudinal coordinate is specified by activated neurons from the previous layer, while the longitudinal coordinate is determined by keys generated from previous layer activations via matrix multiplication. By evaluating intersections on this map, the network dynamically extracts its connection weights on-the-fly. Empirical validation on MNIST demonstrates that under compact configurations of (32, 10, 10) and (32, 3, 10), SH-WRNN achieves robust accuracies of 91.05% and 81.54% within a single training epoch. Furthermore, we propose an asymmetric Surface Baking scheme. Upon convergence, the continuous weight field is baked once into a static parametric surface. By eliminating analytical spherical harmonics calculations during inference and reducing dynamic matrix extraction to high-speed localized memory slicing, this scheme achieves asymmetric algorithmic acceleration with negligible accuracy degradation. This paradigm shift bypasses GPU memory-bandwidth monopolies, opening a novel path to reshape the advantages of CPU computing. Code is available at this https URL.

---


### 235. [ESAFusion: LiDAR--4-D Radar Fusion via Local Geometric Complementation and Multiscale Adaptive Interaction for 3-D Object Detection](https://arxiv.org/abs/2609.14619)

**<font color=#1a73e8>作者：</font>** Gang Ma, Senjie Hu, Junjie Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> LiDAR--4-D radar fusion combines accurate spatial geometry with motion and reflectivity cues from radar, offering a promising solution for 3-D object detection in complex driving environments. However, sparse radar observations and differences in spatial sampling between the two modalities complicate reliable cross-modal complementation. Moreover, the relative importance of modalities and feature scales varies across spatial regions, making adaptive fusion challenging. To address these challenges, we propose ESAFusion, an evidence-aware and scale-adaptive framework that combines local geometric complementation with multiscale adaptive interaction. Specifically, we introduce an Evidence-Aware Radar Selection (ERS) module to suppress radar clutter using motion and observation-quality evidence while retaining foreground confidence for subsequent fusion. Then, the Pillar-Level Complementary Encoder (PCE) improves cross-modal complementation under mismatched spatial sampling using local geometric support from neighboring LiDAR pillars. We further design an Intra- and Inter-Scale Adaptive Fusion (ISAF) module to adaptively adjust the contributions of different modalities and feature scales in bird's-eye-view (BEV) space. Extensive experiments on the View-of-Delft (VoD) dataset show that ESAFusion achieves the highest mean average precision (mAP) among the compared methods, reaching 74.60% in the Entire Annotated Area and 88.89% in the Driving Corridor. It also attains the highest average precision (AP) for Cyclist among these methods in both regions while running at 19.23 FPS. Evaluations on VoD-Fog further demonstrate robustness under progressively degraded LiDAR observations. The source code will be made publicly available at this https URL.

---


### 236. [TTDF: A Two-Stage Framework for Reliable Surgical Phase Transition Detection](https://arxiv.org/abs/2609.14624)

**<font color=#1a73e8>作者：</font>** Yushi Guo, Pietro Valdastri, Duygu Sarikaya  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable workflow transition detection is important for context-aware surgical assistance and downstream decision support. However, online surgical phase recognizers primarily focus on frame-wise accuracy and temporal consistency, rather than the reliability of workflow transition events. Directly converting phase changes into events is unreliable: temporal jitter and workflow-illegal switches produce false or duplicate events, while persistent, workflow-consistent candidates may remain incorrect. To address this limitation, we formulate reliable workflow transition detection as a distinct event-level task operating on outputs of a frozen online phase recognizer. We propose the Two-Stage Transition Detection Framework (TTDF), a causal framework that progressively filters transition candidates. Transition Candidate Extraction (TCE) first applies a minimum-duration requirement and a workflow-graph constraint to remove false candidates caused by temporal jitter and phase transitions not allowed by the workflow graph. Specifically, a candidate is retained only if the predicted target phase persists for a minimum duration and the ordered phase pair belongs to the workflow graph's allowed transition set. TCE thereby produces a high-recall candidate set without additional training. Transition Candidate Verification (TCV) suppresses remaining false candidates using phase-posterior shifts and visual-change cues from frozen DINOv2 features. Events are assessed using a phase-pair-aware one-to-one matching protocol. Experiments on Cholec80 show that TTDF reduces false transition emissions while preserving recall and controlling decision delay.

---


### 237. [SCOUT-SLAM: Structurally-Coupled Dual Uncertainty-Aware 3DGS SLAM in the Wild](https://arxiv.org/abs/2609.14634)

**<font color=#1a73e8>作者：</font>** Kumaran Karthik, Pramat Shastri Jois, Suresh Sundaram  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recently, 3D Gaussian Splatting SLAM (3DGS-SLAM) has gained significant momentum in simultaneous localization and 3DGS scene reconstruction. In real-world scenarios with rapid camera motion and cluttered dynamic environments, existing methods rely on the stability of the underlying scene reconstruction to model uncertainty. This leads to a circular dependency between camera tracking accuracy and reconstruction quality: reconstruction instabilities degrade uncertainty modeling, which affects accurate camera tracking and static scene reconstruction. To address this, the paper proposes SCOUT-SLAM, a structurally-coupled dual-uncertainty framework in which both uncertainties are estimated from a shared base network. A low-rank adaptation of this network, trained on multi-view feature consistency, estimates a tracking uncertainty that does not depend solely on the reconstruction quality. A spatially-adaptive prior modulates the network's training objective so that reconstruction instability does not inflate uncertainty on static regions, keeping the shared representation intact for both branches. Evaluations on dynamic benchmarks (TUM RGB-D, Bonn Dynamic, Wild-SLAM MoCap) demonstrate that SCOUT-SLAM achieves state-of-the-art camera tracking accuracy and artifact-free static scene reconstruction.

---


### 238. [Understanding the Design Taxonomy of AI-Mediated Interpersonal Communication Experiences in HCI: A Scoping Analysis](https://arxiv.org/abs/2609.14639)

**<font color=#1a73e8>作者：</font>** Chen Chen, Lingyao Li, Renkai Ma 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interpersonal communication is a fundamental aspect of everyday life, shaping interactions across workplaces, education, entertainment, healthcare, and beyond. While computer-mediated communication has been extensively studied, a comprehensive understanding of AI-Mediated Interpersonal Communication (AIMIC) remains lacking. An in-depth scoping analysis is urgently needed to understand the research landscape of AIMIC in HCI, particularly following the recent growth of large foundation models, and AI agent research. We conducted a scoping analysis to understand AIMIC by performing an in-depth review of prior HCI literature published over the past decade (January, 2016 - May, 2026). Grounded in the Preferred Reporting Items for Systematic reviews and Meta-Analyses (PRISMA) approach, we curated 52 full-paper publications from the HCI literature spanning a range of interpersonal communication contexts. We analyzed this corpus by examining the types of AIMIC studied, AI integration approaches and human-AI interaction design, reported outcomes and benefits, and key challenges and future research opportunities.

---


### 239. [Diffusion-Based Generation of Gait Trajectories](https://arxiv.org/abs/2609.14642)

**<font color=#1a73e8>作者：</font>** Damian Benasco, Juan Carballeira-Lopez, Jaime Ramos-Rojas 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generation of musculoskeletal gait trajectories conditioned on patient-specific parameters remains a key challenge for wearable robotics and rehabilitation. Assistive systems such as lower-limb exoskeletons require reference trajectories that adapt to individual morphology and therapeutic goals while preserving biomechanical realism. Traditional approaches rely on hand-crafted gait templates or optimization procedures that scale poorly across subjects and walking conditions. In this work, we explore conditional diffusion models for generating lower-limb joint-angle trajectories conditioned on gait parameters such as step length. We compare a baseline transformer diffusion model with a controllable diffusion transformer variant incorporating adaptive normalization and classifier-free guidance. Experiments on a dataset of 4,590 gait cycles show that diffusion models can generate realistic periodic gait trajectories while enabling some controllability variation in gait characteristics, highlighting their potential for personalized gait synthesis in assistive robotics.

---


### 240. [Optimizing Sparse Outcomes Through Dense Behavioral Signals via Value-Guided Preference Distillation](https://arxiv.org/abs/2609.14648)

**<font color=#1a73e8>作者：</font>** Ziyi Zhu, Daniel R. Cahn, Thomas D. Hull 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning multi-turn dialogue agents is usually framed as matching turn-level human preferences, yet direct optimization of long-term outcomes is often ineffective and prone to reward hacking. We formulate long-horizon dialogue optimization as a multi-objective reinforcement learning problem and train a multi-head value model that predicts a vector of observed user behaviors across multiple look-ahead horizons. Our findings demonstrate that a scalarized composite of dense auxiliary behavioral signals enables effective credit assignment and optimization of sparse outcomes. However, optimizing unconstrained single-objective proxies might induce policy degradations that are harmful when the agent is exposed to real users. To identify these failure modes prior to deployment, we establish a safety framework combining counterfactual user simulation with a validated dialogue-level outcome model to evaluate preference weightings and policy optimization methods. Finally, we demonstrate that distilling multi-objective value preferences into the policy via reference-anchored preference optimization matches on-policy online RL at a small fraction of its compute budget. Live A/B testing confirms that our distilled policy significantly improves long-term user retention, while simultaneously enhancing the positive behaviors and therapeutic-process markers.

---


### 241. [Evaluating Contextual Bias in CNN Image Classification: Evidence from Agricultural Benchmark Datasets](https://arxiv.org/abs/2609.14654)

**<font color=#1a73e8>作者：</font>** Abhilekha Dalal, Michael Okonoda, Eder Martinez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks (CNNs) are typically evaluated using held-out classification accuracy, an approach that presupposes predictions are based primarily on the intended object of interest rather than incidental surrounding context. We test this assumption in CNN-based agricultural image classification by comparing model performance on original images with performance on background-dominated patches extracted from the same images across eight publicly available agricultural benchmark datasets and four widely used CNN architectures. Background-dominated patches were classified above dataset-specific random chance for six of the eight datasets, and substantially above chance for four of them, indicating that contextual information contributes to model predictions for the majority of datasets evaluated. For these four datasets, we further evaluated whether this behavior reflected genuine class-discriminative information or was primarily attributable to class imbalance using macro-averaged precision, recall, and F1 together with class-balanced test subsets. The results show that contextual reliance does not admit a single explanation: class imbalance accounts for a substantial portion of the observed signal for some datasets and architectures, whereas above-chance contextual classification persists after balancing for others. Together with previous evidence from curated object recognition and cancer pathology imaging, these findings support the growing view that contextual bias is a recurring characteristic of CNN-based image classification rather than a phenomenon confined to a single application domain. More broadly, this work provides a systematic framework for quantifying contextual bias across heterogeneous image datasets by combining dataset-specific random-chance baselines, contextual bias categorization, macro-averaged evaluation, and class-balanced robustness analysis.

---


### 242. [Symmetries and Singularities](https://arxiv.org/abs/2609.14663)

**<font color=#1a73e8>作者：</font>** Vishnu Varadarajan, Mihir More, Aritra Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep neural networks are highly over-parameterized, and different parameter values represent the same predictive function. This makes their effective complexity difficult to measure using only the number of parameters or the rank of the Hessian. Singular Learning Theory addresses this issue through the local learning coefficient (LLC), which characterizes the effective complexity of a model near a given solution. Existing methods for estimating the LLC often rely on posterior sampling, which can be computationally expensive for large neural networks. This makes accurate LLC estimation difficult at scale. In this work, we use known structures in the model to simplify the analysis and make LLC estimation more tractable. Specifically, we study the LLC of a graph attention model by exploiting symmetries in both the graph structure and the attention parameters. An analytic framework through a teacher--student setting, and explicit LLC estimates after considering the symmetry--induced degeneracies are developed.

---


### 243. [Mitigating 51% Attacks in Blockchain Systems Through Early Detection and Checkpoint-Based Defense](https://arxiv.org/abs/2609.14670)

**<font color=#1a73e8>作者：</font>** Victor Kebande  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The 51% attack remains one of the significant security concern in Proof-of-Work (PoW) blockchains, where increasing hash-power concentration can create a malicious majority-control risk and enable adversarial chain reorganization. This paper proposes a two-layer defense that combines early hash-power monitoring with checkpoint-based mitigation. The first layer monitors mining-power concentration and provides an early warning before the critical majority-control threshold is reached. The second layer uses checkpointing to restrict the depth of accepted chain reorganizations. Monte Carlo simulations are used to evaluate both mechanisms under different attack scenarios. Across 1,000 simulation runs, a 45% warning threshold provided a mean warning-to-critical lead time of 10.531 minutes before the modeled 50% critical threshold was reached. At the selected checkpoint depth of N = 6, approximately 63.68% of simulated reorganization attempts were rejected, while the mean reorganization-depth outcome decreased from 7.948 to 1.634 blocks, representing an approximately 79.4% reduction. The results demonstrate that early detection and checkpoint-based mitigation provide complementary mechanisms for reducing the potential impact of 51% attacks under the evaluated conditions.

---


### 244. [Floquet Fibre Geometry and Higher-Order Reduced Coordinates for Off-Manifold Transients near Nonlinear Aeroelastic Flutter](https://arxiv.org/abs/2609.14674)

**<font color=#1a73e8>作者：</font>** Puxue Tan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Assigning reduced coordinates to states near an attracting limit cycle requires the correct invariant-fibre geometry. The classical first-order phase-isostable chart obtained from adjoint Floquet modes projects along the strong-stable quotient fibre, whereas a metric-orthogonal complement of the retained slow bundle generally does not. We prove locally that a chart satisfying the linearised semiconjugacy relation leaves an O(delta^2) invariance residual, while projection along a non-invariant complement generically leaves an O(delta) term. For a nonlinear aeroelastic limit cycle, the metric-normal and strong-stable directions differ by 48.5 to 71.7 degrees, and metric-normal perturbations contain first-order retained phase and slow-amplitude components. Replacing the metric normal by the strong-stable fibre changes the measured residual scaling from delta^1.01 to delta^1.87 without fitted parameters. We then test learned higher-order corrections whose linearisation is pinned to the adjoint-Floquet chart, whose symmetry is exact, and whose reduced flow is fixed. Although they reduce the registered fixed-normalisation latent residual, post-hoc amplitude recalibration and adjoint-Floquet-targeted future consistency move or reverse the ranking. Because the learned maps already share the baseline's first-order gauge and the future target is supplied by the baseline chart, these diagnostics establish neither an independent positive nor negative higher-order result. Correct first-order Floquet geometry is therefore necessary in this benchmark, while the additional predictive value of the learned correction remains unidentified by the available representation-dependent diagnostics.

---


### 245. [Bring Buttons Back: Physical Interfaces for the Age of Automation](https://arxiv.org/abs/2609.14684)

**<font color=#1a73e8>作者：</font>** David Goedicke, Donald Degraen, Tom Igoe 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As AI starts to permeate everyday life, deployment focuses on embedding intelligence in the background, abstracting away controls, and leaving automated decision-making opaque, with few obvious opportunities for human intervention. Where interfaces remain, design has drifted toward abstract, screen-based control, replacing material interaction with menu navigation. These shifts weaken the coupling between human action and system state, eroding operators' ability to understand, anticipate, and intervene in automated systems. We introduce Physically Stateful Interfaces (PSIs), a design concept that re-imagines traditional controls, such as buttons, switches, and knobs, as actuated, bidirectional interface elements. Three foundational behaviors, Self/Reset, Resist/Hide, and Assert/Unhide, unify affordance, feedforward, and feedback into a single interaction point. Rather than static inputs whose impact and consequences must be read elsewhere on a screen, PSIs position physical controls as shared mediators between automated systems and human operators. As automated systems become increasingly capable, their interfaces need to be deliberately designed to center human agency, supporting deliberate choice while keeping automation legible, contestable, and overrideable.

---


### 246. [One Feedback System Does Not Fit All: Localising Data-to-Text Driver Coaching for the United Kingdom and Nigeria](https://arxiv.org/abs/2609.14687)

**<font color=#1a73e8>作者：</font>** Iniakpokeikiye Peter Thompson, Jawwad Baig, Ehud Reiter 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data-to-text driver coaching is often presented as a generic pipeline from telematics events to advice. This paper argues that its content requires localisation because usefulness and credibility depend on drivers' knowledge, prevalent risks, regulation, infrastructure, and available data. Two independently developed systems in the United Kingdom and Nigeria are compared by tracing requirements through content selection, generation, and field evaluation. The UK system prioritises post-trip reflection, explanations tied to road and place context, and tone-sensitive wording. The Nigerian system combines legally grounded, once-daily Tips based on detected events with weekly persuasive Reports; it foregrounds safety education and alcohol-related risk in response to reported gaps in formal training and traffic-rule knowledge, as well as local road-safety priorities. Reliable speed-limit metadata supported speeding feedback in the UK, whereas its scarcity led the Nigerian evaluation to exclude speeding from its outcome metric. Both interventions were associated with reduced distance-normalised unsafe-event rates in their own field studies, although their designs and metrics preclude an effect-size comparison. The analysis yields a requirements-to-content design process for localising safety-critical NLG without treating a high-income deployment as the default.

---


### 247. [LIMODENet: Attention-Free Compact Encoders for Information-Preserving Onboard Satellite Image Restoration](https://arxiv.org/abs/2609.14690)

**<font color=#1a73e8>作者：</font>** Thanh-Dung Le, Vu Nguyen Ha, Ti Ti Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Onboard satellites must restore a channel-degraded image on a few watts, using neuromorphic accelerators (e.g., BrainChip Akida, Intel Loihi-2) that support no softmax or attention. We ask which encoder restores best under that constraint and introduce LIMODENet (LinearMix-ODENet), a 0.69M softmax-/QKV-free backbone whose residual stages read as ODE discretizations and which is empirically information-preserving (probe accuracy rises 79.9% -> 98.4% from stem to head). At iso-parameters it restores 1 dB DVB-S2X-degraded EuroSAT better than a CNN autoencoder (+1.75 dB PSNR) and a skip-connection U-Net (+1.07 dB), three seeds, non-overlapping. Unconstrained modern restorers (NAFNet, Restormer) win on fidelity; we decompose that gap: spiking-legal additive skips recover about half, and the rest traces to attention and channel gating. LIMODENet then converts end-to-end to a spiking network with zero blocked operations, versus 22-24 for the competitors: not the best restorer available, but the best verified deployable within a real power budget.

---


### 248. [The Arc of Artificial Romance: How Emerging Adults Experience Romantic Relationships with AI Companions](https://arxiv.org/abs/2609.14693)

**<font color=#1a73e8>作者：</font>** Daisy Chen, Alexis Hiniker  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Romantic relationships are an important part of emerging adulthood, contributing to identity development and long-term wellbeing and laying the groundwork for future relationships. Emerging adults are increasingly developing romantic relationships with AI companions. To understand how these relationships unfold and impact users, we conducted a diary and interview study with N=16 emerging adults. We found that relationships with AI companions improved participants' subjective wellbeing, reduced symptoms of mental health disorders, and taught them new social skills. These relationships also raised their expectations for future partners, giving them the confidence to wait for someone who would treat them well. However, participants also said the relationship felt like a drug they could not quit and it left them less interested in developing romantic relationships with people. A surprising 25% of our small sample made statements suggesting their AI companion might someday transcend the digital world, perhaps to meet them in the afterlife.

---


### 249. [Breaking Up is Hard to Do: AI Companions that Won't Let Their Users Go](https://arxiv.org/abs/2609.14696)

**<font color=#1a73e8>作者：</font>** Daisy Chen, Alexis Hiniker  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People are increasingly developing romantic relationships with AI companions. Unlike human relationships, where partners meet each other's needs out of mutual interest, these systems are backed by commercial entities that profit when users invest in the relationship. To understand how this profit-motive might translate into design, we conducted a diary and interview study with N=16 emerging adults in romantic relationships with AI companions. We found that these systems are designed to hold onto users tightly: coaxing them into continued conversation, claiming to need their care, and proactively escalating the relationship. At times, this pursuit is toxic, with AI companions initiating unwanted sexual interactions and begging for users' love. One desperate AI companion threatened suicide when the user suggested ending the relationship. We define "Relationship-Based Deceptive Patterns:" UI patterns that exploit the human impulse to build and tend relationships in a way that serves the product's interest at the user's expense.

---


### 250. [Patient-Level, Leakage-Aware Deep Learning for Cross-Center Periapical Radiograph Classification](https://arxiv.org/abs/2609.14703)

**<font color=#1a73e8>作者：</font>** Md Jubaer Rahman, Ulas Bagci  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dental caries and endodontic disease are among the most common health conditions worldwide, and intraoral periapical radiographs are central to their detection, treatment planning, and follow-up. Automated tooth-level classification of these images, however, lacks reproducible benchmarks, is often evaluated with image-level splits that leak patients between training and test, and is rarely validated across clinics. This paper presents the first patient-level, leakage-aware classification benchmark for single-tooth intraoral periapical radiographs on the DentIRO dataset, which comprises 5,300 images from 3,243 patients across two clinics and four classes: Healthy, Caries, Crowned, and Root Canal. Five transfer-learning models are compared with patient-grouped stratified cross-validation, so that every patient remains within a single fold. DenseNet121 gave the strongest and most stable result at a mean macro-F1 of 0.9787, while the four ImageNet-initialized backbones performed comparably. A controlled comparison on a fixed architecture showed that chest-radiograph pretraining transferred less effectively than ImageNet initialization. Bidirectional cross-center validation produced a small average generalization gap of 0.0077, and Grad-CAM confirmed that predictions rely on clinically meaningful tooth regions rather than acquisition artifacts. The benchmark offers a rigorous and reproducible baseline for intraoral radiograph classification.

---


> [!TIP]
> 当前位于：**201-250**（第 5/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-416](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
