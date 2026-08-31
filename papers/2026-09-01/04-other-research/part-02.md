# 📦 其他研究 | 2026年09月01日

> 本类共 **151** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-151](./part-04.md)

---

### 51. [What Do Interaction Representations Actually Measure? Pre-Event Separability in Weakly-Supervised Violence Detection](https://arxiv.org/abs/2608.27879)

**<font color=#1a73e8>作者：</font>** Parishruthi Ganesh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Articulated human pose provides detailed body-configuration information beyond coarse spatial relationships, but whether this detail yields greater discriminative information when the downstream pipeline is held fixed remains unclear. We examine this through early violence detection. Holding the tracker, temporal head, supervision, folds, and evaluation fixed, we compare five interaction representations spanning coarse bounding-box geometry, a matched handcrafted pose analogue, enriched pose descriptors, and a matched-capacity encoder learned from raw joints, under video-level evaluation with cluster-bootstrap intervals. No pose-based representation outperforms coarse geometry, though with fifteen anomalous videos this subset cannot rule out small effects. Extending the pipeline to frozen visual encoders, and repeating the comparison on XD-Violence (137 anomalous videos, nine times our UCF-Crime sample), person-crop appearance and whole-frame context both exceed geometry by a wide margin, yet context matches appearance on UCF-Crime and exceeds it on the larger split: cropping to the interacting people yields no advantage over encoding the whole frame. This prompts a direct test of what the benchmark measures. Scoring anomalous videos using only frames preceding the annotated onset, under a control removing sequence length as a cue, retains 39-91% of above-chance separation on both benchmarks, including for seven hand-designed geometric channels. Inspection of the tightest pre-onset windows identifies concrete provenance artifacts: editorial title cards and platform watermarks absent from the surveillance footage supplying the normal class. Video-level AUC here is thus a composite of event evidence and pre-event source cues, a shared source of discrimination that can obscure differences between representations. The diagnostic requires only annotations these benchmarks already ship.

---


### 52. [Beyond Pairwise Graphs in Science: Hypergraph Adaptive Wavelet Operators for Parametric PDEs](https://arxiv.org/abs/2608.27883)

**<font color=#1a73e8>作者：</font>** Rajat Sarkar, Venkataramana Runkana, Souvik Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physical systems are often modeled by solution operators that map input fields, parameters, geometries, or past states to steady or future physical states. Learning these maps is difficult, especially for time-dependent systems that must assimilate history and remain stable under autoregressive rollout. Many neural operators work best on regular, structured grids, while realistic simulations often require unstructured meshes or point clouds to resolve complex geometries; in such settings, grid-centric representations can lose accuracy. Graph neural operators handle these domains through message passing or spectral graph filtering, but pairwise edges do not directly capture group-wise couplings among mesh cells, local neighborhoods, or conservation volumes. We introduce the Hypergraph Adaptive waveLet Operator (HALO), which lifts the domain to a hypergraph and learns in its spectral wavelet domain. HALO avoids explicit hypergraph-Laplacian eigendecomposition through Chebyshev polynomial wavelet filters, giving localized spectral kernels at linear sparse-matrix cost. Its trainable dyadic wavelet scales are regularized toward tight-frame coverage, allowing the frequency response to adapt to each PDE while encouraging stable multi-scale spectral coverage. Across 2D and 3D benchmarks on structured and unstructured discretizations, HALO achieves best or near-best accuracy among frequency-, transformer-, DeepONet-, state-space-, and graph-based baselines and sustains stable multi-step rollouts. The same model scales to industrial aerodynamic geometries: on meshes of a few hundred thousand points it is on par with, or better than, the strongest fixed-discretization transformers, while remaining resolution-equivariant.

---


### 53. [Thread-Efficient Decoding for Neural Texture Compression](https://arxiv.org/abs/2608.27888)

**<font color=#1a73e8>作者：</font>** Janarbek Matai, Sho Ikeda, Lukasz Lipski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Neural texture compression (NTC) achieves higher compression ratios than BCn formats but suffers from GPU thread divergence, which significantly reduces runtime performance. In this work, we propose a shared decoder MLP architecture -- trained with a gradual decoder freezing schedule -- combined with texture clustering to reduce thread divergence by 25%-52% while preserving rendering quality. We evaluate our method on over 500 textures and multiple real rendering scenes, demonstrating up to 8.48x speedup on the Radeon RX 9070 XT GPU compared to non-shared baselines. Our key contributions include: (1) a unified shared decoder architecture that reduces divergence by grouping textures; (2) a training recipe with gradual decoder freezing that improves stability and reconstruction accuracy; (3) a semantic clustering strategy using CLIP embeddings that groups similar textures for effective decoder sharing; and (4) comprehensive performance and ablation studies validating our approach.

---


### 54. [A User-Centric Context-Aware Permission Governance Framework for Privacy Control in Default Mobile Applications](https://arxiv.org/abs/2608.27914)

**<font color=#1a73e8>作者：</font>** Asmau Yetunde Adeniran, Adeniran Kolade Ademuwagun, Fatimah Adamu-Fika 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile operating systems provide runtime permission controls intended to improve user control over sensitive data. However, default or pre-installed applications are deeply integrated into the system, may operate with elevated privileges, and are difficult for users to scrutinize. Existing permission models generally grant persistent or temporary access for an application session without distinguishing among individual features, leaving users uncertain about when and why data are accessed. This paper presents a context-sensitive, user-focused permission governance framework for default mobile applications. It introduces a feature-based authorization option, "Allow When Needed," that restricts access to the functionality requiring the data rather than the entire application session. A weighted scoring system estimates the privacy implications of user choices based on permission sensitivity and authorization type. A web-based simulation platform was developed to model 30 realistic permission-request situations across six commonly used default application types and support controlled early-stage evaluation before native implementation. The exploratory assessment combined a cross-sectional survey of 104 respondents examining permission awareness and behavior with formative usability testing involving eight participants interacting with the prototype. Survey findings indicate that users do not consistently examine default-application permissions and prefer contextual explanations before granting access. The results provide preliminary evidence that context-aware permission governance can improve user understanding and decision clarity. This simulation-based study represents an initial step toward evaluating feature-level authorization and privacy-feedback mechanisms before native mobile deployment.

---


### 55. [PCBnet: A Dataset and Automatic Construction of SPICE Netlists from Schematic Images](https://arxiv.org/abs/2608.27923)

**<font color=#1a73e8>作者：</font>** Zhen Huang, Yuhao Gao, Yuzhi Liu 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Printed circuit boards (PCBs) are fundamental to modern electronic systems, yet AI-driven PCB design automation remains constrained by the lack of large-scale paired schematic-netlist datasets. PCB schematics are particularly challenging due to diverse component types, complex wiring topologies, and noisy textual annotations. To address this gap, we present PCBnet, a large-scale PCB schematic dataset comprising over 300 real-world designs with annotated pins and paired SPICE netlists. It contains more than 50,000 component instances, 150,000 wires, 100,000 text regions, and 400,000 characters. We further develop an automated schematic-to-netlist pipeline that combines visual recognition, topology construction, and domain-knowledge-guided multi-agent correction. The proposed method achieves 94.54% component detection mAP, 98.57% text recognition accuracy, and 84.47% end-to-end connectivity accuracy. PCBnet provides a benchmark and data foundation for future AI-driven PCB design automation.

---


### 56. [GraftyVul: Synthesising Insecure Programs Through Real-World Vulnerability Grafting](https://arxiv.org/abs/2608.27928)

**<font color=#1a73e8>作者：</font>** Omri Ram, Mitchell Horner, Ron Van der Meyden 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Vulnerability datasets underpin a wide range of security research, including vulnerability detection, automated remediation, and secure code generation. However, existing datasets sacrifice at least one of three desirable properties: diversity (of language or vulnerability type), reproducibility/executability, or realism. We therefore present GraftyVul, a system that constructs vulnerable programs by grafting real-world vulnerabilities into open-source projects. This grounds the dataset in vulnerabilities observed in real-world contexts while harnessing known good build and test environments, enabling exploit-verification scripts to guarantee that an introduced vulnerability successfully alters a program's behaviour. Using GraftyVul, we generate 212 verified and exploitable vulnerable programs spanning five programming languages (Python, TypeScript, Java, Go, and C#) across 23 CWE categories. To evaluate fidelity, we introduce a language- and context-agnostic semantic embedding that compares vulnerabilities by sink, mechanism and host-feature rather than surface code. This approach outperforms standard code embeddings on cross-language clone and CWE classification. These embeddings demonstrate that GraftyVul samples retain a strong semantic signature to their source vulnerability. We additionally compare GraftyVul against 13 widely used datasets, where it attains competitive diversity while being the only reproducible-exploit dataset with broad language and CWE coverage. Finally, we illustrate GraftyVul's practical utility through an industrial case study evaluating a production vulnerability remediation system.

---


### 57. [TI$^2$PS: A Topology-Informed Inverse Design Framework for Stochastic Multicellular Pattern Formation](https://arxiv.org/abs/2608.27931)

**<font color=#1a73e8>作者：</font>** Kenji Komiya, Andrew Kailiang Jin, Ryo Nishikimi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> This study proposes a novel framework to estimate parameters for reproducing target multicellular patterns using an agent-based model (ABM). Two major challenges in multicellular ABMs are estimating cell-level parameters (agent-specific variables) and quantitatively evaluating the topological characteristics of multicellular arrangements under stochastic cell proliferation and death. To address these challenges, we integrate two approaches: Betti vectors and inverse surrogate modeling. The Betti vectors obtained through topological data analysis can consistently represent features of a wide range of multicellular spatial configurations. The inverse surrogate modeling enables direct inference of the corresponding ABM parameters from the target patterns. We validated the proposed framework using zebrafish pigment pattern formation, a representative model of pattern formation driven by multicellular interactions. The results demonstrate that our framework successfully estimates ABM parameters and outperforms conventional methods such as PointNet++. Notably, the proposed method, which used only 10% of the training data, outperformed PointNet++, which used 100% of the data, across all evaluation metrics.

---


### 58. [A Deep Learning-Based Stacking Ensemble Framework for Turbofan Engine Remaining Useful Life Prediction](https://arxiv.org/abs/2608.27940)

**<font color=#1a73e8>作者：</font>** Limon Bin Hossain, Md. Salehin Seyam, Md Rashedul Islam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study proposes a two-level stacking ensemble framework for Remaining Useful Life (RUL) prediction of turbofan engines, evaluated on the NASA C-MAPSS benchmark using the FD001 and FD003 subsets. The framework integrates four heterogeneous deep learning base learners: Long Short-Term Memory (LSTM), Convolutional Neural Network (CNN), CNN-LSTM, and CNN-GRU, whose out-of-fold predictions are combined by an XGBoost meta-learner to capture complex degradation patterns while mitigating individual model biases. Comprehensive experiments demonstrate that the stacking ensemble achieves superior predictive performance, with Root Mean Square Error (RMSE) of 9.989 and 8.613, Mean Absolute Error (MAE) of 7.081 and 5.195, and R-squared values of 0.899 and 0.906 for FD001 and FD003, respectively. Compared to the best-reported baseline (TCAT: RMSE 11.12 and 11.02), the proposed method achieves RMSE reductions of 10.2 percent and 21.8 percent for FD001 and FD003, respectively. Feature correlation analysis, residual diagnostics, and training convergence curves validate the model's robustness. These findings underscore the efficacy of stacking ensemble methods for prognostics and health management in safety-critical aerospace applications.

---


### 59. [CASTANET: Causality-Aware Spatio-Temporal Adversarial Network Using Traffic Incident Effects](https://arxiv.org/abs/2608.27942)

**<font color=#1a73e8>作者：</font>** Toshiya Kitahara, Ryu Shirakami, Koh Takeuchi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting non-periodic traffic congestion caused by sudden incidents (e.g., accidents and road damage) is crucial for advanced intelligent transportation systems. However, incident-driven congestion is difficult to forecast because incidents are extremely sparse, occur at specific times and locations, and have heterogeneous impacts depending on the traffic context. While recent deep learning approaches have significantly improved periodic traffic forecasting, their performance on non-periodic congestion remains limited, partly because incident records are not explicitly incorporated and their occurrence is strongly biased in space and time. To address these challenges, we propose CASTANET, which integrates spatio-temporal graph neural networks and causal treatment effect estimation to utilize incident records while mitigating selection bias. Experiments on real-world traffic data and accident records from Tokyo, which we treat as incidents, show that CASTANET reduces RMSE by 4.0% overall compared to the best baseline and by 10.1% on incident-conditioned evaluation, with gains reaching 14.55% under severe congestion.

---


### 60. [Temporal Memory-Aware Online Test-Time Adaptation on Dynamic Graphs](https://arxiv.org/abs/2608.27948)

**<font color=#1a73e8>作者：</font>** Bo Li, Xin Zheng, Ming Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time adaptation (TTA) on graphs aims to adapt a graph neural network (GNN) that is well-trained on the training graph to the test graph, which involves potential distribution shifts that may harm model generalization and test-time inference. While recent efforts have investigated TTA on static graphs, there is still a research gap on dynamic graphs learned with dynamic GNN (DGNN) models, where both structural connectivity and node semantics evolve continuously over time. This makes adapting a DGNN model for reliable test-time performance substantially challenging. To fill this gap, in this work, we propose a novel framework of temporal memory-aware Online Test-Time Adaptation on Dynamic Graphs, named DGOTTA, to effectively adapt well-trained DGNNs during test time. Specifically, the proposed DGOTTA contains three modules: (1) temporal-aware augmentation, to extend the diversity of test dynamic graphs for addressing complex temporal and spatial shifts; (2) memory-aware model prediction, to alleviate catastrophic forgetting; (3) consistency-guided online adaptation, to enforce temporal alignment and memory smoothness. Extensive experiments on three real-world datasets and four DGNN backbones demonstrate that DGOTTA significantly improves generalization under diverse distribution shifts and multiple model architectures.

---


### 61. [Lexically conditioned realization ambiguity in Korean predicate morphology](https://arxiv.org/abs/2608.27966)

**<font color=#1a73e8>作者：</font>** Wonjun Oh, KyungTae Lim, Jungyeul Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper examines Korean surface realization as distinct from morphological analysis. It asks whether a sequence of canonical morphemes and grammatical category labels uniquely determines the corresponding surface form. The answer is negative for a restricted but theoretically revealing class of Korean predicates. In these cases, formally identical or near-identical stem-ending configurations yield different outputs depending on lexical identity and realization class membership. We analyze this phenomenon as homonymy with inflectional divergence, focusing on regular versus digeut irregular pairs, regular versus bieup irregular pairs, and reu irregular versus reo irregular pairs. These cases show that stem shape and ending alone do not always determine surface realization. Instead, lexical meaning, subcategorization, and semantic role structure help identify the intended predicate; the predicate determines the realization class; and the realization class determines the surface form. Korean realization thus reveals a limit of bare morphological representation.

---


### 62. [DisCTI: Who Needs to Know Timely? Automated Sector-Aware Cyber Threat Intelligence Dissemination](https://arxiv.org/abs/2608.27967)

**<font color=#1a73e8>作者：</font>** Fajar Wijitrisnanto, Alsharif Abuadbba, Yansong Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The timely dissemination of cyber threat intelligence (CTI) is critical for organizations to mount swift and effective incident response. When valid CTI is delivered to the right sector at the right time, identical attacks can often be contained or mitigated. However, today's rapidly expanding CTI landscape overwhelms analysts, who must sift through massive and heterogeneous feeds. Existing platforms such as the Malware Information Sharing Platform (MISP) provide sector tagging features (e.g., energy, finance, government), but in practice, these remain largely unmapped (98% of events are left uncategorized). This lack of automated and timely sector mapping severely limits the operational value of shared intelligence, leaving organizations that belong especially to the critical information infrastructure sector exposed.
To address this gap, we formulate sector-targeted CTI dissemination as a multilabel classification problem. Leveraging deep field knowledge of CTI structures and sector-specific threat patterns, we construct a novel data set of 872 sector-labelled CTI events from a threat intelligence platform (TIP). We then apply BERT, a transformer-based model, to automate the mapping of CTI events to sectors. Using the structured threat information expression (STIX) format for cross-platform interoperability, our approach achieves a macro-averaged F1-score of 0.89 at a Hamming loss of 0.055 on the custom dataset, i.e. 94.5% of individual sector-label assignments are correct. These results not only demonstrate the feasibility of sector-aware, automated CTI dissemination but also highlight how embedding expert field knowledge into machine learning design fills a crucial gap in the threat intelligence pipeline, enabling faster and context-relevant defensive action.

---


### 63. [GAAT: Geometry-Aware Alignment Transformer for Multimodal UAV Perception](https://arxiv.org/abs/2608.27971)

**<font color=#1a73e8>作者：</font>** Jingpu Yang, Debin Tang, Yilin Sun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unmanned aerial vehicle (UAV) multimodal perception integrates visible (RGB), infrared (IR), synthetic aperture radar (SAR), and depth sensors for scene understanding under diverse conditions. However, differences in optics, resolution, and mounting often limit practical systems to global or image-center alignment. After tokenization, parallax, platform motion, and lens distortion can shift corresponding patch centers across modalities, weakening the spatial correspondence assumed by dense contrastive learning and cross-modal fusion. We propose GAAT (Geometry-Aware Alignment Transformer), an alignment-first pretrained model that estimates local correspondence reliability before cross-modal interaction. GAAT introduces syncPATC, which learns patch-center consistency under synchronized view transformations without correspondence annotations. It emits geometric priors, including token and query confidence, query centers, and sub-token offsets, that identify reliable local anchors across residual misalignment. Guided by these priors, MG-Sparse-MMA performs query-mediated sparse fusion over top-K_s reliable regions, replacing dense all-patch interaction with geometry-calibrated local updates. RA-QCGCL aligns pretraining supervision with this sparse query bottleneck through reliable patch-to-patch, patch-to-query, and query-to-query contrastive branches. We introduce UAVMeta and StateBench, which provide four acquisition-state scores derived from platform telemetry and image statistics: camera reliability, observation scale, viewpoint stability, and flight maneuver complexity. Extensive experiments across six downstream tasks demonstrate consistently superior transfer performance, establishing GAAT as a state-of-the-art multimodal foundation model for UAV perception. StateBench further enables a systematic diagnosis of real-world acquisition conditions.

---


### 64. [PhyMamba: Physics-Modulated Mamba for Robust Battery Health Prognostics](https://arxiv.org/abs/2608.27978)

**<font color=#1a73e8>作者：</font>** Sara Sameer, Yunyi Zhao, Wei Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Battery health prognostics is a core function in battery management systems (BMSs), yet long-horizon health forecasting from BMS signals remains challenging due to operating-condition dependency and sensor noise. In this paper, we propose PhyMamba, a two-stage physics-modulated Mamba framework that integrates electrochemical aging into sequence modelling. PhyMamba does not require explicit identification of internal aging parameters, which often relies on intrusive measurements. In stage-1, a lightweight Mamba encoder first processes BMS signals and produces a latent representation that is transformed via an aging parameterization module, into physics-informed aging features. In stage-2, a customized Mamba forecasting backbone performs multi-cycle prediction, where physics is tightly integrated to regulate the model's internal temporal updates toward degradation-consistent evolution. Experiments on three public datasets under multiple forecast horizons show that PhyMamba achieves the best aggregated performance, with an overall mean error reduction of 31.8% compared with a diverse range of baselines. PhyMamba also offers an optimized accuracy-efficiency trade-off, which supports practical deployment for robust battery health prognostics.

---


### 65. [Is Monte Carlo Tree Search Just Every-Visit Monte Carlo Control?](https://arxiv.org/abs/2608.27985)

**<font color=#1a73e8>作者：</font>** Xianyi Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Monte Carlo Tree Search (MCTS) and every-visit Monte Carlo (MC) control are usually presented as different methods. MCTS is described in the language of search (selection, expansion, simulation, and backup), whereas MC control is described in the language of reinforcement learning (trajectory sampling, return estimation, action-value updating, and policy improvement). This note argues that, at the level of trajectory generation and action-value updating, the distinction is largely terminological. The tree policy and rollout policy can be viewed as the learned and not-yet-learned parts of a single evolving policy; expansion corresponds to first visit and initialization; and backup is the ordinary every-visit Monte Carlo update. Under this interpretation, the four stages of MCTS reduce to two basic operations: trajectory sampling under the current policy and every-visit Monte Carlo updating. In this sense, MCTS is simply every-visit Monte Carlo control expressed in the language and data structure of search. The purpose of this note is expository: to make this equivalence explicit and easier to recognize.

---


### 66. [Predicting Turn-Taking Outcomes in Multi-Party Conversation: Interpretable Modelling of Speech and Gaze Dynamics with Interpersonal Closeness](https://arxiv.org/abs/2608.27988)

**<font color=#1a73e8>作者：</font>** Mark Dourado, Karim Haddad, Henrik G. Hassager 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Smooth speaker transitions are fundamental to effective conversation and rely on an interlocutor's ability to predict when to enter the conversation. This ability depends on accurately interpreting and expressing the verbal and non-verbal cues that signal when a speaker wishes to take or relinquish the floor. The process becomes even more complex in noisy, natural, multi-party settings, with multiple interlocutors available. This study models how gaze and speech, together with perceived interpersonal closeness, signal conversational floor changes in free four-person dialogue. Using the GaMMA corpus, we trained logistic regression models using interpretable, behaviourally motivated features extracted before each turn-taking event to classify floor-transfer outcomes as gaps or overlaps. Predictors included gaze features such as transition motifs and behavioural contrasts, entropy, gaze-based addressee identity, and mutual gaze, alongside speech features derived from speaker loudness, as well as perceived interpersonal closeness (IOS) between speakers. Results show that gaze features capture predictive structure, and that combining them with loudness improves performance (ROC AUC = 0.76 +- 0.04). Loudness reflected speaker control, while gaze dispersion and addressing indexed listener readiness and competitive entry. Performance remained robust across noise conditions, indicating that gaze provides a complementary, noise-resilient cue to turn-taking dynamics.

---


### 67. [GAN-Based Semantic Communication for Image Transmission in IoV](https://arxiv.org/abs/2608.27989)

**<font color=#1a73e8>作者：</font>** Ruixing Ren, Shan Chen, Junhui Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> For cooperative perception in the internet of vehicles, this paper proposes a generative adversarial network-based semantic communication framework to address the efficiency and fidelity bottlenecks of traditional communication systems in visual data transmission under limited bandwidth and dynamic channel conditions. At the transmitter, the framework adopts a pyramid attention network to extract semantic label maps and introduces a semantic priority preservation mechanism. It assigns differentiated weights to distinct semantic categories based on driving safety, guiding bit allocation and loss function design. At the receiver, an image reconstruction module integrating a coarse to-fine multi-resolution generator and multi-scale discriminator is designed. Combined with the temporal consistency branch, spatial pyramid pooling and class-aware convolutional layers, it achieves high-fidelity reconstruction of high-quality images from corrupted semantic labels. The model is trained with combined adversarial, feature matching and perceptual losses, effectively improving semantic consistency and visual realism of generated images. Experimental results on the Cityscapes dataset show that the proposed method outperforms existing counterparts in both semantic segmentation accuracy and reconstructed image quality, and maintains stable reconstruction performance under AWGN and Rayleigh channels.

---


### 68. [GOD: Govern, Observe, and Direct - A Real-Time Control Room for Agent Societies](https://arxiv.org/abs/2608.27992)

**<font color=#1a73e8>作者：</font>** Yige Luo, Ran Guan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Generative-agent systems are easier to start than to inspect. A run can contain many agents, locations, messages, commands, and model calls, yet the operator often gets either a finished replay or raw logs. That makes it hard to ask why an agent moved, test a small intervention, or package a run for another researcher. GOD is a local-first control room for agent societies. From the same browser workflow, an operator can issue targeted questions or interventions and inspect the resulting replay state. The system combines a setup wizard, Agent Studio, Map Studio, a spatial replay interface, Ask and Intervene commands, and portable experiment, map, and agent packs. Its technical contribution is the command and artifact loop: live controls and replay evidence share the same operator command model, while package contracts separate scenario, map, and profile data from local runtime state. The public release includes hosted Smallville-style and PKU replays, the open-source repository, and downloadable packs. We evaluate this path on 15 completed run slots. Across the 14 intervention runs, 78 of 84 target-agent checks recorded the commanded destination, and 169 of 182 state answers matched a saved location or action string.

---


### 69. [Should I Use This Synthetic Dataset for Training? How to Test with Minimal Real Data](https://arxiv.org/abs/2608.27996)

**<font color=#1a73e8>作者：</font>** Zhenyu Tao, Wei Xu, Xiaohu You 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Digital twins (DTs) and learned world models are increasingly used to generate synthetic data that augment the scarce real datasets available for training artificial intelligence (AI) models in engineering systems. Owing to the inevitable simulation-to-reality (sim-to-real) gap, however, augmentation may fail to improve the performance of the trained model on the real data distribution. This paper addresses the resulting decision problem: Given a real dataset, a candidate synthetic dataset, and a fixed learning algorithm, decide whether training on the augmented dataset improves the true, population-level performance, while consuming as few real test data points as possible. Two formulations are considered: a direct test on the mean loss difference between the two trained models, and a symmetry-based test on the paired loss difference, which trades a stronger null assumption for faster evidence accumulation. For the latter, we introduce the {adaptive e-process sign-flip test} (aeSFT), a doubly adaptive procedure that adapts both the number of Monte Carlo sign-flip rounds, and hence the computational cost, and the amount of real test data consumed. aeSFT yields anytime-valid Type-I error control, with no need to pre-specify the test-set size. Experiments on a synthetic-data classification task, a DT-aided wireless packet-scheduling task, and a radio-map prediction task show that aeSFT identifies useful synthetic data using substantially fewer real test samples than mean-based sequential testing, matches the power of fixed-sample sign-flip testing and the paired $t$-test, while keeping the false-positive rate below the target level.

---


### 70. [A-PAIR: A Benchmark and Identity-Consistent Grounding Framework for Air-Ground Cross-View Referring Person Detection](https://arxiv.org/abs/2608.27997)

**<font color=#1a73e8>作者：</font>** Zhoupeng Guo, Xinjie Yao, Yunqi Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Air-ground cross-view referring person detection is a necessary component in the language-to-perception-to-control chain of collective embodied intelligence, grounding a language command into the same physical target before ground and aerial agents can coordinate downstream actions. Existing referring expression comprehension and open-vocabulary grounding methods do not jointly account for cross-view identity consistency, making them insufficient for Air-Ground Cross-View Referring Person Detection (AGCV-RPD), which involves similar pedestrian distractors, weak aerial appearance cues, and cross-view identity consistency. To study this problem, we introduce Air-Ground Paired Identity-Aware Referring (A-PAIR), the first comprehensive AGCV-RPD benchmark, containing 22,137 cross-view referring samples. To construct A-PAIR efficiently, we propose Factorized Annotation and Referential Alignment (FARA), a semi-automatic annotation framework that generates factorized referring descriptions and identity-consistency supervision at reduced cost. We propose Identity-Consistent Referring Grounding (ICRG), a framework that combines factorized referential grounding, candidate-completeness supervision, and cross-view consistency calibration for joint air-ground pair selection. ICRG improves ground, aerial, and pair-level detection over strong baselines, increasing pair F1 from 16.65% to 22.28%. These results show that AGCV-RPD requires paired detection and identity-consistent reasoning.

---


### 71. [PhenoIntel: A Lifecycle-Aligned Multi-Agent Web Application for Verified, Accessible Plant Phenotype Analysis](https://arxiv.org/abs/2608.27999)

**<font color=#1a73e8>作者：</font>** Narendren S V, Soumyashree Kar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing conversational plant-phenotyping platforms are difficult for plant scientists to use and lack the reliability scientific research demands: failed analyses are reported as valid measurements rather than flagged as missing, statistical tests run without checking assumptions, predictions carry no uncertainty estimate, and specialised hardware limits accessibility. We present PhenoIntel, a lifecycle-aligned multi-agent web platform that turns the full machine-learning workflow into a reliable, user-friendly phenotyping system. Nine specialised agents divide the analysis into stages, from image collection through model selection, inference, and reporting, rather than handing the whole task to one AI manager. Independent checks separate these stages, and every agent reads from and writes to one shared, fixed-structure record, so an inconsistent output from one stage is caught before it reaches the next. Uncertainty is matched to each model family, conformal prediction, detection-confidence spread, or Monte Carlo Dropout, rather than applied uniformly, and quality thresholds adapt to crop and task instead of one global cutoff. When no suitable model exists, PhenoIntel can propose, validate, and integrate a new one on its own. The model repository spans ten trained models across five crops and four imaging modalities. Classification models reach Macro F1 of 0.78-0.996; object-detection models reach 0.96 mAP@50 with a 54% reduction in counting error over an unoptimised baseline; and a temporal model reaches held-out Macro F1 of 0.7050. PhenoIntel runs in a browser on standard hardware, requiring no GPU, and a 1,200-test automated suite confirms complete pipeline execution. Every result carries calibrated uncertainty, validated statistics, and FAIR-compliant provenance, a combination existing conversational phenotyping tools do not offer.

---


### 72. [FocusGen: Expanding Visual Design Exploration with a Simulated Focus Group of Persona Agents](https://arxiv.org/abs/2608.28001)

**<font color=#1a73e8>作者：</font>** Jaewon Choi, Helena Vasconcelos, Hyun Lee 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Creative professionals rarely design for themselves--they design for audiences whose preferences they must anticipate. Yet current text-to-image exploration tools derive diversity entirely from the designer's own input--their prompts, their chosen dimensions, their search queries--confining exploration to what the designer already knows to look for. We present FocusGen, an interactive system that introduces external perspectives into visual design exploration through a "virtual focus group" of simulated persona agents. In contrast to prior persona systems in which multiple agents converge as critics on a single evolving artifact, FocusGen uses personas as parallel generators: each agent--constructed from demographic data, a procedurally generated backstory, and aesthetic preferences elicited through interviews--independently drives an iterative generation loop that produces its own visual concept, transforming one design brief into a spectrum of audience-conditioned directions. With real human participants, we confirm that the iterative refinement loop produces outputs people prefer over zero-shot generation. With synthetic agents at scale, we show that persona conditioning yields higher visual diversity than a generic-assistant baseline--measured by CLIP distance and corroborated by human perceptual judgments--and that open-ended preference interviews yield more diverse outputs than structured ones for both human and synthetic cohorts, while also revealing that agent cohorts recover only part of the diversity of comparable human cohorts. A qualitative study with 16 creative professionals suggests FocusGen helps designers discover unanticipated directions, overcome fixation, and probe audience contexts--while surfacing stereotyping risks that we analyze. We position FocusGen as a divergence scaffold for early-stage ideation rather than a substitute for audience research.

---


### 73. [Exact Risk Ratios for Weighted Data Selection in Linear Regression](https://arxiv.org/abs/2608.28007)

**<font color=#1a73e8>作者：</font>** Guangjian Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hanneke, Moran, Shlimovich and Yehudayoff (COLT 2025) posed the following open problem. A selector sees a finite dataset $D \subseteq \mathbb{R}^d \times \mathbb{R}$, picks at most $n$ examples together with nonnegative weights, and hands the weighted least squares objective to the minimum-norm ERM. Writing $F_w(d,n)$ for the worst-case ratio between the loss of the returned predictor on all of $D$ and the optimal loss, they proved $F_w(d,n)=\infty$ for $n<d$, $F_w(d,d)=d+1$ and $F_w(d,n)=1$ for $n \ge 2d$, and asked for the value in the open regime $d<n<2d$. We determine this value in several cases. For every $d$ we prove $F_w(d,2d-1)=1+1/d$, which confirms a claim stated without proof in the original note. We further prove $F_w(3,4)=5/3$ and $F_w(4,5)=2$, the two smallest cells not covered by the endpoint formula. For every intermediate budget $n=d+k$ we prove the lower bound $F_w(d,d+k) \ge 1+\Gamma_{d,k}$, where $\Gamma_{d,k}$ is an explicit harmonic quantity over balanced partitions, and we show that this bound is the exact minimax value over the class of datasets whose whitened gradient systems carry an orthogonal circuit-block structure. All three exact values match $1+\Gamma_{d,k}$, and we conjecture that equality holds throughout the open regime. The upper bound proofs run on a common geometric spine: a rigidity theorem for positive spanning configurations of loss gradients, classifications and structural reductions of small positive bases in $\mathbb{R}^3$ and $\mathbb{R}^4$, and a dimension-free extremal-basis argument that converts sign-cone geometry into five-point selections. We also give explicit counterexamples showing that several shorter routes fail, and constructive polynomial-time selection algorithms for all proved cases.

---


### 74. [The Impact of Magma: A Ground-Truth Fuzzing Benchmark](https://arxiv.org/abs/2608.28016)

**<font color=#1a73e8>作者：</font>** Ahmad Hazimeh, Adrian Herrera, Srividya Subramanian 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Magma is an open-source and ground-truth fuzzing benchmark that enables uniform fuzzer evaluation and comparison. Magma was originally released with a research paper published at ACM SIGMETRICS 2021. This short paper explains the motivation, the design, and the impact of Magma, with a description of extensions to the original benchmark.

---


### 75. [3D-USE: From Image-Level to Scene-Level Underwater Enhancement](https://arxiv.org/abs/2608.28020)

**<font color=#1a73e8>作者：</font>** Jieyu Yuan, Yuanlin Zhang, Jihong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Underwater 3D reconstruction faithfully reproduces the color shifts and visibility loss of captured views, while physical inversion may leave estimation errors in the recovered scene appearance. We formulate Underwater Scene-level Enhancement (USE) as learning a persistent, visibility-enhanced 3D scene representation from degraded multi-view underwater observations, enabling consistent enhanced rendering. Realizing USE requires both a reliable scene representation for enhancement and a consistent enhancement target without paired enhanced 3D data. Therefore, we present 3D-USE, a two-stage framework. First, the Medium Radial Basis Anchor Representation (MediumRBF) establishes a medium-aware Gaussian scene by representing water effects with shared radial-basis anchors and explicitly decomposing object and medium contributions. Based on this fixed scene representation, Appearance Transition Consensus (ATC) transfers paired 2D underwater image enhancement (UIE) knowledge into scene-global and Gaussian-local targets, avoiding direct supervision from inconsistent enhanced views. An Underwater Bilateral Appearance Field (U-BAF) then realizes these targets in Gaussian radiance and medium appearance. The scene directly renders enhanced novel views without a 2D UIE model at inference. Experiments on real underwater scenes show improved visibility and cross-view consistency while preserving reconstruction quality.

---


### 76. [ZipMVS: Multi-View Stereo with Compressed Cost Volumes](https://arxiv.org/abs/2608.28033)

**<font color=#1a73e8>作者：</font>** Guanglin Jin, Hongshan Yu, Javier Civera 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-view stereo (MVS) methods typically deliver highly accurate 3D reconstructions from multiple registered RGB images, thanks to the highly informative, geometric constraints between them. However, their substantial memory requirements remain a major obstacle for deployment in domains such as aerospace and autonomous systems, where resource efficiency is critical. In this work, we introduce ZipMVS, an MVS method specifically designed for efficient high-quality reconstruction. We propose a novel depth-hypothesis strategy that enables substantial compression of the cost volume, hence greatly reducing GPU memory consumption while preserving reconstruction accuracy. Experiments on the DTU and Tanks and Temples datasets show that ZipMVS achieves competitive reconstruction quality compared with other efficiency-oriented MVS methods, while achieving a competitive balance between reconstruction quality and GPU memory usage. The code is available at this https URL

---


### 77. [A Shaky Voice Is Not Always a Dodge: Benchmarking Textual and Vocal Evasion Detection in Earnings Calls](https://arxiv.org/abs/2608.28040)

**<font color=#1a73e8>作者：</font>** Mirae Kim, Seonghun Jeong, Youngjun Kwak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing approaches to evasion detection in earnings calls focus on textual transcripts, treating evasion as a single-dimensional phenomenon. We argue that evasion in spoken communication is inherently multidimensional: beyond what executives say, how they say it carries independent and complementary information. To study these dimensions jointly, we introduce DualEvasion, a benchmark for evasion detection across text and audio in earnings call Q&A. The benchmark contains 505 annotated question-answer pairs from 60 earnings calls, each with two independent labels: textual evasion (direct vs. evasive) and vocal cues operationalized as speaker confidence (confident vs. unconfident). Our experiments show that state-of-the-art multimodal models struggle to detect vocal confidence, particularly on unconfident responses. Our analysis suggests these models interpret acoustic cues in isolation rather than relative to each speaker's baseline. Providing speaker-level references yields modest improvements, but a substantial gap with human performance remains.

---


### 78. [Too Much of the Same: From Algorithmic to Human Bias in Learning to Defer](https://arxiv.org/abs/2608.28050)

**<font color=#1a73e8>作者：</font>** Dario Pesenti, Alessandro Bogani, Stefano Teso 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Learning to Defer (LtD) extends supervised learning by allowing a Machine Learning (ML) model to defer harder or less confident decisions to a human expert. Despite being geared for human-AI collaboration, LtD strategies neglect the potential negative interference of human cognitive biases. Our contribution is twofold. First, we demonstrate that standard LtD strategies show class-dependent sampling bias in classification tasks in practice, and thus may disproportionately defer the minority classes when applied to imbalanced datasets. Second, we show that such asymmetries in task delegation may trigger human biases, ultimately leading to poorer downstream decision making. Specifically, we conduct a user study ($N=226$) where participants complete a classification task on a set of deferred items, with conditions presenting different levels of class imbalance. Our results show that participants exposed to a highly imbalanced rejection set achieved lower classification accuracy in the majority class compared to those exposed to a more balanced set, regardless of which class constituted the majority. Exploratory analyses suggest that this may be an instance of the Test-taker's effect, which stems from a mismatch between the actual distribution of classes and the participants' expectations about that distribution. Finally, we discuss the implications of these findings for the deployment of LtD algorithms.

---


### 79. [Explainable Uncertainty Estimation for Reliable Medical AI](https://arxiv.org/abs/2608.28052)

**<font color=#1a73e8>作者：</font>** Li Rong Wang, Jamie Duell, Xinran Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial intelligence has strong potential to support clinical decision-making, yet its adoption in healthcare remains limited due to a lack of trust. Uncertainty estimation can signal unreliable predictions, and explainable AI (XAI) can clarify how predictions are made but existing methods treat them separately, providing no feature-level insight into why a prediction is uncertain or which tests to prioritize to reduce it. To address this gap, we propose explainable uncertainty estimation, which unifies uncertainty estimation and XAI to both quantify uncertainty and explain feature-level contributions. We introduce the Expected Gradients Reconstruction Uncertainty Estimate (egRUE), which incorporates prediction explanations into its uncertainty computation and decomposes uncertainty into feature-wise contributions. We prove theoretical properties of egRUE and show through experiments that it improves reliability and interpretability compared to existing methods. A user study with medical experts further demonstrates that egRUE's explanations improve calibrated trust over uncertainty scores alone, increasing confidence in correct predictions and reducing confidence in incorrect ones. By combining prediction uncertainty with feature-level explanations, egRUE strengthens decision-making support in safety-critical healthcare settings, clarifying both when predictions may be unreliable and which features drive that uncertainty.

---


### 80. [User Preferences for UI Anchoring in MR: Effects of Task Mobility and Interface Properties](https://arxiv.org/abs/2608.28064)

**<font color=#1a73e8>作者：</font>** João Belo, Sina Elahimanesh, Anna Maria Feit  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Anchoring - the choice of frame of reference for mixed reality (MR) interface elements - is a critical design decision involving trade-offs between accessibility, interaction comfort, and visual interference. Despite its importance, user preferences for anchoring across different mobility contexts and interface properties remain poorly understood, as prior work has largely focused on specific tasks or fixed interface configurations. We address this through a mixed-methods user study in which participants configure anchoring strategies across different mobility conditions and interface types. Combining behavioral analysis with structured qualitative inquiry, we analyze how participants select and reason about anchoring modes. Our results show a clear transition from world-anchored interfaces in stationary contexts to body-anchored interfaces during locomotion. However, no single body anchor consistently dominates, highlighting the personal nature of anchoring strategies. Our qualitative analysis reveals the factors users consider in their anchoring decision, including interface accessibility, stability during interaction, visual clutter, and individual mental models. These findings inform the design of adaptive and controllable MR interfaces and highlight the importance of supporting user customization.

---


### 81. [Learning to Allocate Incentives for Incentivized Advertising via Offline Model-Based Reinforcement Learning](https://arxiv.org/abs/2608.28065)

**<font color=#1a73e8>作者：</font>** Zilin Zhao, Han Yang, Tianpei Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complete your ad view and grab a 5-cent bonus! In incentivized advertising, a platform promises users a bonus before observing downstream ad revenue, encouraging them to click and complete ads. It must balance the incentive promised in advance against the revenue realized afterward: insufficient incentives forfeit monetization opportunities, whereas excessive incentives reduce net profit. Because current incentives may also shape user expectations and future engagement, incentive allocation is a sequential decision problem with delayed revenue, cost sensitivity, and carryover effects.
Existing work has not studied decision-making algorithms for this setting. Auto-bidding assumes available ad opportunities, while targeted promotion optimizes incentives outside the ad monetization pipeline. We formulate the problem as an MDP and develop an offline model-based RL framework for cost-controllable sequential incentive allocation. It learns a world model of user feedback and ad revenue, then performs conservative policy optimization. An independent counterfactual scorer evaluates each learned policy on held-out logs, enabling pre-launch selection without costly online exposure. Experiments on large-scale industrial data and online A/B tests show that the scorer provides a stable offline signal. The deployment path from causal inference to offline RL and then Offline-MBRL further validates the framework: MB-IQL improves per-user net profit by 7.96\% over TD3+BC, whereas reverting to plain IQL reduces it by 6.56\% (both \(p<0.0001\)).

---


### 82. [VersaGauss: A Versatile Framework for Generating Multiphase Dynamics with 3D Gaussians](https://arxiv.org/abs/2608.28069)

**<font color=#1a73e8>作者：</font>** Ruijie Su, Lingxiao Yang, Xiaohua Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress has been made in 3D Gaussian representation for reconstruction, generation, and physical simulation. However, current approaches mainly concentrate on physics-based dynamic generation of solid objects and only handle single-phase collision interactions. We introduce VersaGauss, a unified framework for generation, simulation, and rendering that supports versatile physics-based dynamic generation, particularly for multiphase interactions. Our system takes a few images as input and produces a realistic, physics-driven 3D dynamic scene with multiple objects. To optimize the Gaussian kernel distribution, we develop a particle pruning algorithm. We also propose the Coupled Multiphase Point Method (CMPM) to effectively model and generate multiphase interactions. Additionally, harmonic interpolation within CMPM and a Gaussian evolution strategy are introduced to achieve realistic fluid rendering. Extensive experiments demonstrate that our framework can simulate interactions among various materials such as fluid, rubber, sand, snow, and others. Code is available at this https URL.

---


### 83. [CF-YOLO: Context-Aware Feature Refinement for Camouflaged Industrial Micro-Defect Detection](https://arxiv.org/abs/2608.28070)

**<font color=#1a73e8>作者：</font>** Xinda Yu, Kunxin Zheng, Chunan Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated detection of surface micro-defects on industrial components, such as copper tubes, is critically important for quality assurance but remains challenging due to the minute scale of anomalies and their visual camouflage against complex backgrounds. These factors lead to weak feature representations and high rates of false positives and missed detections. To address these issues, we propose a novel real-time detection framework designed for efficient context perception and feature refinement. Our method integrates a Context-Perception Aggregation Module (CPAM), which synergises large-kernel perception for macro-texture context and small-kernel aggregation for sharp boundary delineation, effectively breaking the background camouflage. Furthermore, a Feature Additive Refinement Module (FARM) employs a linear-complexity additive token mixer to globally verify and refine the representation of fine-grained anomalies, suppressing noise-induced errors. To support research in this domain, we introduce the Copper Tube Defect Dataset (CTDD), a manually annotated benchmark containing 1,847 images and 4,898 boundingbox defect instances from copper-tube inspection scenarios. Extensive experiments demonstrate that our detector achieves strong and consistent performance on CTDD, outperforming representative baseline detectors, including YOLOv11, by 2.2% in mAP@50 and 3.9% in Precision while maintaining real-time inference speed. This work provides a robust and efficient solution for high-precision industrial inspection, bridging the gap between contextual understanding and detailed feature analysis. Our code and model are available at: this https URL

---


### 84. [Task-State Adaptation with Prototype Memory for Multi-Task Dense Prediction](https://arxiv.org/abs/2608.28078)

**<font color=#1a73e8>作者：</font>** Yangyang Xu, Haobo Yuan, Yuzhu Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation backbones provide strong representations for dense prediction, yet a single shared feature still needs to support tasks with different, image-dependent adaptation requirements. We propose MemMTL, a multi-task dense prediction framework that estimates a compact task state from global visual context and refines it through a learnable task-state prototype memory. The refined state is converted into task-conditioned expert logits and combined with token-level logits before sparse top-$k$ selection over a local expert bank shared by all tasks. A separate task-agnostic residual bank provides a common adaptation path, and both paths are added once to the backbone feature before task-specific prediction. We specify a matched evaluation protocol on NYUD-v2 and PASCAL-Context with SAM 3 and ViT-L backbones to measure predictive quality, computational cost, and the contributions of task-state conditioning, prototype retrieval, and sparse routing. The numerical record in the present working draft predates this canonical implementation and must be regenerated before it can support empirical claims.

---


### 85. [Cyc3D: Evaluating Cyclic Structural Stability and Asset Usability in Image-to-3D Generation](https://arxiv.org/abs/2608.28080)

**<font color=#1a73e8>作者：</font>** Liwen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image-conditioned 3D generation has advanced rapidly, yet existing evaluation protocols largely judge rendered-view plausibility and semantic alignment, overlooking whether a generator forms a stable 3D interpretation and produces assets usable in graphics pipelines. We introduce Cyc3D, a multidimensional benchmark that evaluates image-to-3D generation along two complementary axes: Cross-View Object Consistency and Representation Quality. At the asset level, Cyc3D measures whether object identity remains semantically coherent across rendered viewpoints. At the model level, we propose View-Cycle Structural Consistency, a closed-loop render-regenerate-align protocol that repeatedly re-observes a generated asset from novel views and quantifies geometric, perceptual, and semantic drift across generations. To assess native asset usability beyond rendered appearance, Cyc3D further evaluates geometric structure, reference-image fidelity, mesh discretization and efficiency, and UV parameterization quality. Together, these diagnostics expose failures obscured by a single perceptual score and provide interpretable evidence of both model instability and representation defects. Experiments on five representative image-to-3D systems show that closed-source feed-forward models consistently outperform open-source optimization-based baselines in geometric fidelity, mesh quality, and cycle stability. Nevertheless, even the strongest methods achieve cycle-stability scores below 48, revealing a persistent gap between visually plausible generation and robust 3D object understanding.

---


### 86. [Attribute Token Arithmetic: Disentangled and Continuous Semantic Control for Visual Autoregressive Models](https://arxiv.org/abs/2608.28082)

**<font color=#1a73e8>作者：</font>** Xindi Yang, Yicheng Wu, Cheng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Autoregressive text-to-image generation has recently achieved remarkable progress, offering high-fidelity synthesis via a unified generative framework. However, fine-grained semantic control remains challenging due to the attribute entanglement and the misalignment between textual and fine-grained visual representations. In this paper, we introduce Attribute Token Arithmetic (ATA), a method that enables disentangled and continuous attribute control in visual autoregressive modelling. Inspired by the vector arithmetic property observed in word embeddings, ATA identifies semantic directions corresponding to visual attributes (e.g., aging, fatness, emotion) directly within the pretrained autoregressive latent space. These directions are learned from a single reference image, without model retraining or large-scale supervision. During generation, attributes can be continuously adjusted and compositionally combined through simple arithmetic operations with other attribute tokens. Extensive experiments demonstrate that ATA achieves identity-preserving, fine-grained, and multi-attribute adjustment, outperforming existing autoregressive editing baselines in controllability, generality, and computational efficiency. Our code will be available at this https URL.

---


### 87. [Comparing Classical and Quantum Machine Learning for Regression in High Energy Physics Collision Data](https://arxiv.org/abs/2608.28084)

**<font color=#1a73e8>作者：</font>** Tariq Mahmood, Zain ul Abidin, Itzel Luviano Soto 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The classification and regression of particle collision events constitute a persistent computational challenge in experimental high energy physics, where large volumes of simulated data must be processed with both speed and precision. This work carries out a systematic comparison of four classical machine learning architectures, support vector machines (SVM), artificial neural networks (ANN), convolutional neural networks (CNN), and long short-term memory (LSTM) networks against their quantum counterparts: quantum SVM (QSVM), quantum neural networks (QNN), quantum CNN (QCNN), and quantum LSTM (QLSTM). All models are trained on simulated proton-proton collision events with electron-positron and muon-antimuon final states from the CERN Open Data portal, using transverse-momentum components as input features and transverse-momentum magnitude as the regression target. Classical architectures, and in particular the CNN and LSTM, achieve marginally better quantitative performance under current hardware and dataset constraints. Quantum models, however, reach competitive accuracy with substantially fewer trainable parameters: the QCNN reproduces the performance of the deep classical CNN using only four qubits and a circuit of depth three, pointing to a genuine parameter-efficiency advantage on near-term quantum devices. A baseline analysis confirms that the regression problem is non-trivial for shallow polynomial fits, supporting the relevance of the architectural comparison. These results characterize the trade-offs between classical and quantum approaches under realistic, resource-constrained conditions and provide a benchmark for future studies on actual quantum hardware.

---


### 88. [Ex-Sim(3)-Reg: 2D-3D Correspondence Pruning via Extended Sim(3) Registration](https://arxiv.org/abs/2608.28096)

**<font color=#1a73e8>作者：</font>** Pei An, Muyao Peng, Junfeng Ding 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning-based image-to-point-cloud (I2P) registration has garnered increasing attention in recent years. Nevertheless, existing methods still struggle with severe outliers under challenging scenarios with unseen, low-inlier, or distorted cases. A fast and robust 2D-3D correspondence pruning method is therefore highly desirable. Recently, a promising scheme lifts 2D-3D correspondences to 3D-3D correspondences using depth priors, casting correspondence pruning as a Sim(3) registration problem. However, depth priors estimated from monocular images are inherently noisy, which undermines the reliability of this scheme. In this paper, to explicitly model non-negligible depth noise, we reformulate correspondence pruning as an extended Sim(3) registration problem and propose a simple yet effective pruning algorithm termed Ex-Sim(3)-Reg. We further provide a theoretical analysis to justify the effectiveness of our method. Extensive experiments on the 7-Scenes, RGBD-V2, ScanNet, and TUM datasets demonstrate that Ex-Sim(3)-Reg achieves up to \textbf{24.7\% improvement} in registration recall over state-of-the-art baseline methods. Code is released at this http URL

---


### 89. [Generalized Gibbs Ensemble Weighting for Forecast Combination](https://arxiv.org/abs/2608.28116)

**<font color=#1a73e8>作者：</font>** Prasen R. Nuthanakaluva, Nava K. Gaddam  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Forecast combination is a reliable way to improve predictive performance when several forecasting models are available. Simple aggregation rules such as the mean, median, trimmed mean, inverse-loss weighting, and exponential weighting are often strong baselines, but their relative performance can vary across datasets, forecast horizons, deployment settings, and levels of disagreement among base forecasters. We develop Generalized Gibbs Ensemble Weighting (GGEW), a probabilistic framework that treats forecasting models as experts and assigns ensemble weights using a Gibbs-style exponential transformation of normalized predictive loss. The framework extends this basic weighting rule through numerical stabilization, diversity-aware score corrections, and online hyperparameter adaptation. GGEW produces a family of related methods, including Stable Gibbs weighting, Directional Gibbs-NCL, and Symmetric Gibbs-NCL. These variants share one core algorithm and differ only in the score used inside the exponential weighting rule. For sequential deployment, we adopt a UCB-style bandit mechanism, called online Local-UCB, to adapt the learning rate, diversity strength, and Gibbs variant without evaluating the full hyperparameter grid at every prediction step. We evaluate GGEW on official M4 competition forecast submissions and external rolling-origin deployment experiments using Monash Traffic Hourly, Electricity Hourly, and Solar Weekly datasets. Results suggest that Gibbs-style adaptive weighting is a useful and competitive tool across several benchmark settings, although its relative performance varies across datasets, forecast horizons, deployment protocols, and forecast disagreement groups. The contribution is not a universal dominance claim, but a framework and empirical study motivating further investigation of when adaptive Gibbs-style forecast combination is useful.

---


### 90. [Learning to Difference: Adaptive Reversible Differencing (AdaRDiff) for Time Series Forecasting](https://arxiv.org/abs/2608.28134)

**<font color=#1a73e8>作者：</font>** Morad Laglil, Younes Hlal, Marouane El Hadari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable long-horizon time series forecasting is an important yet difficult problem. Trends and seasonality introduce complex temporal structure that challenges learning-based forecasting models. Differencing, which subtracts nearby past values to remove such structure, is the classical remedy, but its reliance on hand-picked orders and periods has kept it largely absent from recent deep architectures. We propose \textbf{\underline{Ada}}ptive \textbf{\underline{R}}eversible \textbf{\underline{Diff}}erencing \textbf{(AdaRDiff)}, a generalized differencing approach that uses learnable weights to simplify the series through weighted differencing with previous time instants. This yields stabilized residuals on which forecasting is performed, after which the removed components are restored autoregressively to reconstruct the forecast, capturing trend and seasonality jointly through a single operator. This reconstruction admits a closed-form convolutional expression, which parallelizes on GPU and yields up to $33.7\times$ speedup over the naive recurrence. We furthermore rely on a two-phase training schedule that separates temporal structure discovery from reconstruction learning, as suggested by a theoretical analysis of the gradient when using a linear forecasting model. AdaRDiff attains state-of-the-art forecast accuracy across eight benchmarks spanning electricity, weather, traffic, and energy, at negligible parameter cost. Furthermore, it is designed as a plug-and-play module: integrating AdaRDiff improves eight diverse backbones, from linear models to Transformers, in the large majority of cases, by up to $25.9\%$ with a linear backbone and $18.3\%$ with iTransformer.

---


### 91. [Conditional Diffusion Models for Energy-Efficient Driving](https://arxiv.org/abs/2608.28142)

**<font color=#1a73e8>作者：</font>** Hemanth Neelgund Ramesh, André Snoeck, Chyi-Fu Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electrification of commercial delivery fleets is shifting fleet routing from distance- and time-based optimization toward energy-aware decision-making. Existing sequence models primarily provide deterministic point estimates or limited uncertainty summaries, which do not capture the range of plausible energy-consumption trajectories required for operational decision-making. In this work, we introduce a conditional diffusion framework that generates EV battery-current profiles conditioned on route features such as vehicle velocity and ambient temperature. The model combines a latent conditioning encoder with a temporal 1D U-Net denoising backbone that enables trip-related conditions to be mapped into a shared representation and guides the reverse diffusion process. We evaluate the framework on an open-access commercial EV telemetry dataset containing 12k trips from 9 vehicles. The proposed latent-conditioned diffusion model generates realistic cur- rent trajectories that capture both the dominant temporal envelope and sharp transient events. The model achieves a Wasserstein distance of 0.0029 between generated and measured current distributions below the real vs real reference distance of 0.0085 indicating that generated samples lie within the empirical variability of the test set. We further demonstrate that learned latent conditioning substantially improves performance over direct condition injection, reducing the Wasserstein distance by 89.1% and MAE by 52.8%. This work demonstrates a generative modeling framework for characterizing EV energy consumption under real-world operating conditions, providing an essential foundation for uncertainty-aware fleet planning in large-scale operational settings.

---


### 92. [The Approximation Rank of Softmax Attention: Sharp Geometric Laws and Robust Interaction Dimension](https://arxiv.org/abs/2608.28150)

**<font color=#1a73e8>作者：</font>** Yuhe Sui, Jianing Zhang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Which geometry controls the rank complexity of normalized softmax attention? We study maximum-row-$\ell_1$ approximation rank, exactly the least unrestricted rank preserving every bounded vector-valued output. Two sharp worst-case laws isolate support geometry: for fixed $d$ and error $\varepsilon$, spherical self-attention has rank $\Theta_{d,\varepsilon}(\min\{n,(1+\beta)^{(d-1)/2}\})$, while full-ball geometry adds one radial degree and, for $\beta\ge\beta_0(d,\varepsilon)$ and $n\ge C_d e^{\beta/8}$, gives $\Theta_{d,\varepsilon}(\beta^{d/2})$. For a fixed head, row-softmax quotients out row-scalar logit directions: the remaining visible query--key interaction dimension $r$ yields an $r/2$ per-instance upper law, and bounded constructions show this exponent is minimax sharp. Approximate interaction subspaces incur an explicit residual output error and yield a tolerance-indexed SVD dimension. On an 84-head BERT-base calibration set, we observe modest effective-dimension reductions across many head--temperature settings, together with positive associations with finite constructive rank upper certificates. Together, these results separate support geometry, which sets worst-case temperature scaling, from softmax-visible interaction geometry, which controls per-head approximation complexity.

---


### 93. [Under-Mattress Temporal Sensing for Next-Day Agitation Risk Scoring in Dementia Wards](https://arxiv.org/abs/2608.28152)

**<font color=#1a73e8>作者：</font>** Zhen Liu, Marta Bono, Robbe Decloedt 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agitation fluctuates over short time horizons in people living with dementia, yet continuous physiological information for anticipating next-day risk is limited. We assessed whether contactless under-mattress signals from the preceding night inform next-day agitation risk and whether preserving minute-level temporal structure improves performance over conventional nightly summaries. We analyzed 423 patient-nights from 65 subjects in a specialized hospital dementia unit using two under-mattress sensing systems. A unified four-paradigm benchmark compared nightly handcrafted summaries, three-period handcrafted features, full-night sequence modeling, and sliding-window multiple-instance learning. Source-specific preprocessing and five-fold patient-grouped cross-validation were used, with performance estimated from pooled out-of-fold predictions. Evaluation included discrimination, calibration, fixed-threshold metrics, and a comparison of period-signal attribution patterns across two temporal models. Full-night sequence modeling achieved the highest discrimination (AUROC, 0.692; AUPRC, 0.849) and balanced accuracy (0.658). Both minute-level pipelines had higher AUROC than nightly summaries, but differences from three-period handcrafted features were uncertain. Cross-model attribution prioritized activity, heart rate, and respiratory rate during the core overnight period. Calibration remained limited. The preceding night's signals supported modest next-day risk discrimination, with minute-level temporal modeling outperforming nightly summaries. Prospective calibration and external validation are needed before use in individual care decisions. This patient-grouped benchmark identifies contactless overnight sensing as a promising biomedical engineering direction for agitation-risk research in hospitalized dementia cohorts.

---


### 94. [Empowering Local Agriculture: A Deep Learning-Powered Web System for Identifying Bangladeshi Mango Varieties](https://arxiv.org/abs/2608.28161)

**<font color=#1a73e8>作者：</font>** Monowar Islam, Safaruzzaman Shovo  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Mango variety identification in Bangladesh is challenging because closely related cultivars can have similar visual characteristics and images are often captured under varying real-world conditions. This work presents a deep learning-based web system for automatic identification of Bangladeshi mango varieties. We collected 2,013 high-quality mango images (3024x4032 pixels) from local markets and farms and organized them into nine classes, combining Bari-4 and Bari-7 as a single Bari class. The dataset was divided into training (70%), validation (15%), and test (15%) sets, with image augmentation applied to improve model generalization. Three pretrained CNN architectures, ResNet18, ResNet50, and EfficientNetB0, were fine-tuned under consistent training settings. EfficientNetB0 achieved the best performance, obtaining 98.01% validation accuracy and 97.36% test accuracy, compared with 86.47% and 78.55% test accuracy for ResNet18 and ResNet50, respectively. Class-wise F1-scores for EfficientNetB0 ranged from 0.93 to 0.99, while the Bari class achieved an F1-score of 0.97. The selected EfficientNetB0 model has approximately 4 million parameters, making it suitable for lightweight deployment. We integrated the model into a Streamlit web application that enables users to upload a mango image and receive a predicted variety with class probabilities. The system provides an accessible, practical tool for mango identification and demonstrates the potential of deep learning for supporting agricultural applications in Bangladesh.

---


### 95. [CrabOS: An Operating System for Human-AI Co-inhabitation](https://arxiv.org/abs/2608.28165)

**<font color=#1a73e8>作者：</font>** Qi Yang, Yun Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents are evolving into long-running computational entities that can invoke tools, maintain memory, and complete complex tasks across applications. In real-world settings, completing a task often requires humans and AI to take turns leading its execution. Such alternation depends on the seamless handoff of the work state of the task between humans and AI. Existing agent systems, however, provide humans and AI with separate work environments. AI agents must therefore rely on additional bridges to continue work: either developers build task-specific interfaces to access the work state, or users manually transfer relevant parts of it through screenshots or textual descriptions. Both approaches make handoffs costly and scale poorly.
We propose Human-AI Co-inhabitation, a type of work environment that enables humans and AI to seamlessly take turns continuing work on the same task, and design and implement CrabOS to realize this concept. CrabOS represents the work state as natural-language-readable text objects shared by humans and AI, allowing both to access and manipulate it directly through the same auditable interface without bridges. Case studies show that CrabOS elevates support for complex tasks with alternating human and AI leadership from bridge-dependent application-level solutions to native operating-system capabilities, which provide a new foundation for developing and running AI agents.

---


### 96. [Manifold4D: Denoising on Point Cloud Rendered Manifolds for Video Re-shooting](https://arxiv.org/abs/2608.28174)

**<font color=#1a73e8>作者：</font>** Yongqi Mao, Zijia Dai, Zhishuo Liu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video re-shooting re-renders a monocular video of a dynamic scene along a user-specified camera trajectory, and the dominant recipe supplies the target geometry explicitly: per-frame depth lifts the source video into a 4D point cloud, which is rasterized along the trajectory into a point cloud render. Because the render and the source video are both handed to the network as visual conditions, they compete at every denoising step, leaving the model with a trust dilemma --- how much of the render to believe --- which can degrade trajectory control or visual quality on data outside the training distribution. We argue that a render already pixel-aligned with the target view does not need to be supplied as an explicit conditioning stream at all. We propose MANIFOLD4D, which injects the render directly into the initial noise of flow matching, so that generation no longer departs from standard Gaussian noise but from a new noise manifold carrying geometric information, leaving the source video as the only visual condition. The render is thus used exactly once, and the network is never asked to learn how to read it; in subsequent denoising steps the model can focus on the source video. On our DAVIS-Traj benchmark and on the Vista4D evaluation set, MANIFOLD4D attains the best camera-control accuracy on every metric, lowering rotation error by 25% and 27% and translation error by up to 32% over the strongest baseline, while matching it in video fidelity and leading on real-world novel-view photometric quality. In a user study, our method achieves clear advantages in trajectory following and dynamic consistency. The gap widens as the yaw amplitude grows past the training range, and the model still recovers correct dynamic motion from the source video when the render is deliberately corrupted, confirming that the geometric prior guides generation without overriding it.

---


### 97. [Beyond Flat Netlist: Hierarchical Graph Representation Learning for Scalable Analysis of Sequential Circuits](https://arxiv.org/abs/2608.28188)

**<font color=#1a73e8>作者：</font>** Jingyi Zhou, Zhengyuan Shi, Jiaying Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Circuit Representation Learning (CRL) offers a powerful paradigm to guide and optimize core Electronic Design Automation (EDA) tasks, but its practical adoption is hindered by the immense scale of industrial netlists and a failure to explicitly model register-level temporal dynamics. To overcome these barriers, we introduce DeepSeq3, a novel hierarchical framework that abstracts circuits into a two-level representation: fine-grained combinational subgraphs partitioned by flip-flops (FFs), and a high-level Super-Node Graph (SNG) that models the register-transfer structure. A dual Graph Neural Network (GNN) architecture learns representations at both levels, capturing local Boolean logic and global state transitions. Crucially, we introduce a state-centric pre-training scheme that predicts the reachability between FF states, endowing the model with a deep understanding of temporal behavior. Demonstrated on large-scale benchmarks, DeepSeq3's approach yields superior scalability and richer representations, reducing bounded model checking (BMC) solving time by 18% while guaranteeing correctness.

---


### 98. [UniLipi: A Unified Multi-Script OCR for Historical Indic Manuscripts](https://arxiv.org/abs/2608.28195)

**<font color=#1a73e8>作者：</font>** Tathagata Ghosh, Sai Madhusudan Gunda, Simran Singh Sandral 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Optical character recognition (OCR) for handwritten Indic manuscripts is essential for large-scale digitization and computational access to manuscript heritage. However, existing approaches are typically developed for one script at a time and require substantial script-specific customization. This limits scalability and practical deployment across diverse collections. We present UniLipi, a unified multi-script OCR model for handwritten Indic manuscripts trained jointly across 13 Indic scripts within a single framework. UniLipi directly handles realistic manuscript conditions, including extreme variation in line geometry, large variation in line length, and partial interruptions caused by non-textual manuscript entities such as holes, stains, or pictorial illustrations. To operate effectively under ultra low-resource conditions, the model leverages script-aware synthetic manuscript data generation, substantially reducing reliance on large volumes of real annotated data. Beyond historical manuscripts, we show that UniLipi serves as an effective foundational pretrained model. Specifically, its learned representations enable good OCR performance for contemporary Indic handwriting and extend to several non-Indic scripts, including Tibetan, Italian, Latin, and Chinese scripts. In addition to transcription, UniLipi predicts script identity and per-line native character counts, supporting practical manuscript cataloging workflows.

---


### 99. [Performative Privacy: When Differential Privacy Maximizes Utility](https://arxiv.org/abs/2608.28198)

**<font color=#1a73e8>作者：</font>** Uddalak Mukherjee, Edwige Cyffers, Yann Chevaleyre  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Privacy-preserving learning is often motivated by the idea that protecting users' data can preserve trust and thus participation, improving utility in the long term. However, this claim has not been formalized so far. In parallel, performative learning provides a framework for studying learning systems whose deployment affects the data they later observe. In this work, we bring these two perspectives together and introduce \emph{performative privacy}, where data leakage reduces future participation. We study a simple model where agents repeatedly contribute data for mean estimation but may leave the system when their data is leaked. Privacy is implemented through differentially private mechanisms, creating a trade-off between estimation noise and future participation. We show, through a theoretical study of the dynamics and numerical experiments, that a finite privacy budget can outperform non-private estimation in the long term when the feedback loop between leakage and participation is sufficiently strong. This provides first evidence that differential privacy can be optimal not only as a protection mechanism, but also from the perspective of long-term utility.

---


### 100. [Cut-ViT: Task-Specific Model Pruning via Gram Anchoring Subspace Consistency](https://arxiv.org/abs/2608.28205)

**<font color=#1a73e8>作者：</font>** Jianjian Yin, Liulei Li, Tao Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pruning visual foundation models has attracted considerable attention. However, existing methods focus on rigid point-to-point token alignment on a single dataset for pruning, suffering from two limitations: i) robustness degradation, and ii) task-specificity deficiency. To address these limitations, we propose a task-specific pruning pipeline, named Cut-ViT. Specifically, we first construct gram anchoring matrices from both spatial and semantic perspectives, and perform the subspace decomposition to extract the corresponding subspace bases. Basis-agnostic and residual constraints are then adopted to align the gram subspaces between the native and pruned DINOv3 models along spatial and channel dimensions, enabling subnetworks to inherit robust feature representations of native DINOv3. Furthermore, we design spectral entropy adaptation, which quantifies the information density of feature manifolds along spatial and channel dimensions, thereby adapting the pruning objective to specific downstream tasks. Experiments show that Cut-ViT requires approximately one minute on a single A100 GPU to obtain subnetworks at various sparsity levels, using only 20.9% of the time and 45.5% of the GPU memory compared with previous methods, while achieving SOTA performance on six tasks across nine datasets.

---


> [!TIP]
> 当前位于：**51-100**（第 2/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-151](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
