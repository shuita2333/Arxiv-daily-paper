# 📦 其他研究 | 2026年06月26日

> 本类共 **222** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-222](./part-05.md)

---

### 151. [FeVOS: Foresight Expression Video Object Segmentation](https://arxiv.org/abs/2606.25585)

**<font color=#1a73e8>作者：</font>** Kehan Lan, Kaining Ying, Henghui Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Referring Video Object Segmentation tasks focus on referring expressions describing events, actions or appearances of relevant objects within the observed frames, lacking evaluation in scenarios that require pre-decisive spatio-temporal reasoning, thereby limiting their applicability. To address this, we propose Foresight Expression Video Object Segmentation, a task that queries future events in upcoming video segments and requires masks of the objects in the observed frames as visual answers. For example, in ego-centric scenes, the question "What tool will be used?" demands reasoning over spatio-temporal cues to predict the masks of the next tool to be used, which helps with the understanding of future actions and decisions. To support this task, we introduce FeVOS, a dataset with 968 video clips, 14,525 foresight expressions, and 2,904 chain-of-thought annotations to provide explicit and interpretable reasoning steps. We further develop FeVOS-R1, an MLLM-based model trained on our dataset via a two-stage pipeline of supervised fine-tuning and reinforcement learning. FeVOS-R1 not only achieves state-of-the-art performance on FeVOS, but also demonstrates strong generalization to existing RVOS benchmarks. We hope this work can inspire more research on predictive reasoning in video perception.

---


### 152. [Leaking Circuit Secrets: Gradient Leakage Attacks on Graph Neural Networks](https://arxiv.org/abs/2606.25589)

**<font color=#1a73e8>作者：</font>** Rupesh Raj Karn, Johann Knechtel, Ozgur Sinanoglu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As graph neural networks (GNNs) become standard tools for critical tasks in circuit design and analysis, their security and privacy risks require careful attention. Here, we present the first comprehensive evaluation of gradient leakage attacks (GLAs) on GNNs in circuit-design and hardware-security tasks, a practical threat that has been largely overlooked. We assess state-of-the-art (SOTA) GNNs, including GraphSAGE, GCN, GIN, and GAT, trained on standard netlist benchmarks (ISCAS'85, EPFL, and TrustHub), for their fundamental vulnerability to GLAs. We find that GLAs can expose sensitive information, such as gate types and distinctive properties of hardware Trojans, which may assist adversaries in analyzing logic locking schemes or evading Trojan detection mechanisms. Our analysis shows that these risks are influenced by architectural features, with attention mechanisms (GAT) exacerbating leakage, while injective aggregation (GIN) provides comparatively stronger resilience. We further evaluate several SOTA defense techniques, including differential privacy, gradient clipping, secure aggregation, model compression with quantization, and adversarial training. We find that these techniques improve resilience only in specific settings and can also compromise model performance. Overall, our work provides key insights toward privacy-preserving GNNs and highlights the need for more robust and efficient defenses. We release our full methodology and artifacts.

---


### 153. [VPA-Guard: Defending and Benchmarking Image-to-Video Generation Against Visual Prompt Attacks](https://arxiv.org/abs/2606.25592)

**<font color=#1a73e8>作者：</font>** Yining Sun, Haoyu Kang, Jiajun Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advancements in Image-to-Video (I2V) generation have transformed input images from simple appearance references into interactive control interfaces where visual cues such as arrows, sketches, and emojis orchestrate complex video dynamics with unprecedented controllability. However, these seemingly innocuous static cues can be interpreted by models as executable temporal instructions, unfolding into harmful actions in the generated videos. Despite the severity of this threat, existing safety benchmarks remain predominantly focused on text-based and content-only image-based jailbreaks, leaving implicit visual prompt attacks insufficiently explored. To bridge this gap, we present VVA-Bench, the first systematic benchmark for evaluating video generation safety under categorized vision-centric prompt attacks. Extensive experiments on VVA-Bench demonstrate that state-of-the-art models are highly susceptible to such attacks, with Attack Success Rates (ASR) reaching 100.0\% on Wan 2.7 and 74.8\% on Veo 3.1. To mitigate these risks, we propose VPA-Guard, a retrieval-augmented and self-evolving defense framework. By leveraging few-shot reasoning to identify latent malicious intents, our method reduces the attack ASR by 44.2\% and the harmfulness score by 73.4\% on average, while maintaining the model's utility for legitimate user edits. Our work provides both a rigorous benchmark and an effective defense strategy to advance safe and socially responsible multimodal generation.

---


### 154. [Low-Complexity Policy Tessellations in Structured Markov Decision Processes](https://arxiv.org/abs/2606.25593)

**<font color=#1a73e8>作者：</font>** Fredy Pokou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study optimal-policy geometry in structured Markov decision processes. While approximate dynamic programming and reinforcement learning typically approximate high-dimensional value functions, we show that optimal policies induce simpler decision tessellations. We propose boundary-based policy approximations that learn policy regions directly. A policy-loss decomposition links performance degradation to action margins and explains why errors concentrate near indifference boundaries. Inventory control and queue admission experiments show lower policy error, smaller value gaps, faster error decay, and stability than reinforcement learning baselines.

---


### 155. [Expresso-AI: Explainable Video-Based Deep Learning Models for Depression Diagnosis](https://arxiv.org/abs/2606.25606)

**<font color=#1a73e8>作者：</font>** Felipe Moreno, Sharifa Alghowinem, Hae Won Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Given the widespread prevalence of depression and its consequential impact on individuals and society, it is crucial to obtain objective measures for early diagnosis and intervention. As a multidisciplinary topic, these objective measures should be interpretable and accessible to health care professionals, ensuring effective collaboration and treatment planning in the realm of mental health care. Even though current automated depression diagnosis approaches improved over the last decade, a critical gap exists as they often lack affect-specificity and interpretability, limiting their practical application and potential impact on mental health care. In particular, interpretability from temporal activities from videos when deep models are used is not fully explored. In this study, we present a novel framework for analyzing Deep Neural Networks' decisions when trained on facial videos, specifically focusing on automatic depression severity diagnosis. By fine-tuning Deep Convolutional Neural Networks (DCNN) pre-trained on Action Recognition datasets on depression severity facial videos from AVEC depression dataset, our framework is able to interpret the model's saliency maps by examining face regions and temporal expression semantics. Our approach generates both visual and quantitative explanations for the model's decisions, providing greater insight into its reasoning. In addition to this interpretability, our video-based modeling has improved upon previous single-face benchmarks for visual depression diagnosis, resulting in enhanced predictive performance. Overall, our work demonstrates the successful development of a framework capable of generating hypotheses from a facial model's decisions while simultaneously improving depression's predictive capabilities.

---


### 156. [ScaleHP: Estimating Hand Pose in Metric Space](https://arxiv.org/abs/2606.25619)

**<font color=#1a73e8>作者：</font>** Ruitao Jing, Xingyu Chen, Hongyang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate metric-space hand pose estimation (HPE) is essential for immersive human-computer interaction and robotics. However, most existing methods predict poses in a root-relative coordinate system and cannot estimate the hand in absolute metric scale. In this work, we observe that the intrinsic proportional relationships among human hand bones encode stable anthropometric priors that implicitly correlate with the overall metric size of the hand. Leveraging this insight, we present ScaleHP, an end-to-end one-stage hand pose estimation framework that bypasses fragile extrinsic depth modules to recover the hand in metric space. ScaleHP employs a transformer-based decoder with a novel scale token to fuse multi-scale morphological and appearance features. By solving for metric coordinates through a perspective-constrained least-squares approach, we achieve high-precision pose estimation in the camera coordinate system. ScaleHP delivers state-of-the-art performance, including 35.8 CS-MPJPE on FreiHand and 4.6/5.9 PA-MPJPE on DexYCB and HO3Dv3. These results demonstrate that internal biological constraints significantly reduce relative geometry and absolute metric errors, offering a robust solution for generalized, real-world hand tracking.

---


### 157. [Probabilistic Agents in Deterministic Audits: Evaluating Multi-Agent Systems for Automated Audits Based on the German IT-Grundschutz](https://arxiv.org/abs/2606.25622)

**<font color=#1a73e8>作者：</font>** Lea Roxanne Muth, Marian Margraf  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The NIS-2 Directive mandates robust Risk Management from thousands of small and medium enterprises. To ensure compliance, companies rely on established standards such as the German IT-Grundschutz (IT-GS) of the Federal Office for Information Security. However, IT-GS certification is resource-intensive and requires a high level of manual effort for documentation, validation, and revision, making scalable implementation difficult and expensive.
Building upon our previous conceptual framework, this paper presents the technical implementation and empirical evaluation of a Multi-Agent System (MAS) architecture combined with Hybrid Retrieval Augmented Generation (HybridRAG) for the partial automation of IT-GS certification. We introduce two novel technical contributions to the MAS architecture to enforce the compliance rigor. The Hypothesis-Verification Loop in the Structural Analysis (SA) phase that cross-references agent-inferred dependencies against the Knowledge Graph to reduce hallucinations, and a Decoupled Reasoning Pipeline that separates agent-driven semantic extraction from the deterministic protection need inheritance. We utilize the BSI's "RecPlast GmbH" case study as a human expert-generated reference data set for end-to-end evaluation of the architecture and to quantify Precision, Recall, and F1-scores. The performance of the system is investigated across the phases of SA, Protection Needs Assessment (PNA), Modeling, and IT-GS Check.
The empirical results reveal noticeable differences throughout the different steps of IT-GS. While the MAS demonstrates high efficacy in semantic tasks (SA and Modeling), significantly reducing manual effort through automated information extraction, quantitative results reveal limitations in logical reasoning phases (PNA and IT-GS Check) as the probabilistic nature of current LLMs struggles to meet the deterministic rigor required by IT-GS.

---


### 158. [Reasonable Motion: A General ASP Foundation for Environment Constrained Movement Trajectory Computation](https://arxiv.org/abs/2606.25626)

**<font color=#1a73e8>作者：</font>** Julius Monsen, Jakob Suchan, Mehul Bhatt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We present a general answer set programming based hybrid quantitative-qualitative method for computing constrained branching trajectory modes for moving objects in real-world settings. The method performs constrained traversal of an environment graph, enumerating geometrically admissible motion behaviours as stable models, each constituting a distinct trajectory mode characterised by both domain-dependent and independent factors such as derived event sequence, map topology, and domain norms. The hybrid trajectory computation method is generally applicable across motion characteristics typically encountered in diverse dynamic domains with moving objects, e.g., autonomous driving. We demonstrate applicability and highlight how computed trajectories are traceable to their underlying stable model, thereby affording verifiable interpretability that purely learned approaches cannot provide. We also perform an empirical evaluation with Argoverse 2, a large-scale real-world autonomous driving benchmark representative of the class of dynamic domains within the scope of the proposed method.

---


### 159. [TL++: Accuracy and Privacy Preserving Traversal Learning for Distributed Intelligent Systems](https://arxiv.org/abs/2606.25627)

**<font color=#1a73e8>作者：</font>** Erdenebileg Batbaatar, Young Yoon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Distributed intelligent systems increasingly need to train across data silos without centralizing raw data. Federated learning keeps data local but can suffer under heterogeneous partitions and requires repeated full-model exchange. Split learning reduces communication through cut-layer activations, but standard protocols generally do not recover centralized mini-batch gradient behavior and may expose activations and gradients in plaintext. We present TL++, a two-mode traversal-learning framework that constructs virtual batches across nodes to recover centralized mini-batch gradient behavior under explicit synchronization assumptions. Base mode exchanges cut-layer activations and gradients rather than full models. Secure mode secret-shares each cut-layer activation and gradient between an orchestrator and a non-colluding helper, preventing either server from observing plaintext cut-layer tensors. This protection is limited to a semi-honest two-server setting; labels and loss-related outputs remain visible to the orchestrator. In the lightweight secure path evaluated here, exactness requires a linear or affine server path, while nonlinear operations require nonlinear MPC or approximation. We formalize TL++, analyze communication and computation costs, and evaluate it against federated and split-learning baselines on CIFAR-10 and BioGPT/PubMedQA using full fine-tuning and LoRA. On CIFAR-10, TL++ base cut 1 and exact secure cut 3 achieve accuracies of 91.41% (SD 0.19) and 90.93% (SD 0.17), respectively, exceeding the strongest measured non-TL++ baseline by more than 12 percentage points. TL++ base cut 1 also reduces per-step communication by 13.1-fold relative to full-model synchronization. PubMedQA results similarly favor TL++. Overall, TL++ approaches centralized-training performance while reducing communication and providing activation-level secret sharing.

---


### 160. [Staying In Character: Perspective-Bounded Memory For Book-Based Role-Playing Agents](https://arxiv.org/abs/2606.25632)

**<font color=#1a73e8>作者：</font>** Xushuo Tang, Junhe Zhang, Zihan Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent LLM role-playing systems build character agents from novels by extracting characters, scenes, and relations. Yet long-narrative role-playing suffers from two failures: Factual Overreach, where shared retrieval or parametric memory lets a character use facts outside its perspective, and Stylistic Monotony, where profile descriptions flatten a character into a fixed voice. To address these failures, we propose REVERIEMEM, a three-layer memory architecture for book-based character agents. The episodic layer stores first-person scene memories; the semantic layer stores visibility-tagged facts; and the personality layer stores situation-dependent speech and behaviour patterns. For evaluation, we construct KBF-QA, a 4,386-question benchmark over eight novels for testing knowledge boundaries. REVERIEMEM improves Knowledge Boundary Fidelity by 34.6 percentage points over the strongest prior method. On BOOKWORLD's five-dimension pairwise narrative protocol, REVERIEMEM achieves a ~ 79% win rate, suggesting that perspective-bounded memory improves both boundary fidelity and character-grounded narrative generation.

---


### 161. [Taxonomy of Risks on Automated Fact-Checking Systems Considering its Propagation](https://arxiv.org/abs/2606.25645)

**<font color=#1a73e8>作者：</font>** Jun Yajima, Tatsuya Oka, Takao Okubo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In recent years, the posting of fake news including disinformation and misinformation on social networking services (SNS) has become a social problem. To combat this fake news, fact-checking that is the process of assessing the veracity of posts on SNS has become increasingly important. While fact-checking is currently performed by fact-checking organizations, it is difficult to fact-check all posts on SNS. Therefore, the use of automated fact-checking systems is effective. Recent automated fact-checking systems utilize artificial intelligence and large language models, so there are risks of incorrect judgments and posting incorrect results on social media which can lead to the spread of misinformation or to engage in defamation. In this paper, as a first step toward enabling the safe use of automated fact-checking systems, we categorize the specific risks on automated fact-checking systems. In this categorizing, we consider a three-stage risk propagation: risk factors, hazardous situations, and harm. Our analysis revealed that 32 specific risks exist in automated fact-checking systems. In this paper, we utilize the categorized risks as analytical cues (guide words) to present the risk assessment of the automated fact-checking system DEFAME. This assessment result indicates that risks that cannot be derived using STRIDE, a conventional IT security risk assessment method can be derived using our guide words.

---


### 162. [Auto-Labelling-Based Domain Transfer for 3D Object Detection on a Bicycle-Mounted LiDAR Platform](https://arxiv.org/abs/2606.25652)

**<font color=#1a73e8>作者：</font>** Mario Finkbeiner, Max A. Buettner, Kanak Mazumder 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable 3D perception of vulnerable road users (VRUs) such as cyclists and pedestrians is essential for their safety in urban traffic and a core requirement for autonomous driving (AD). Alongside advances in vehicle-based perception, research increasingly equips bicycles with sensors to study traffic from a perspective native to VRUs. Such platforms still rely on LiDAR detectors originally trained on vehicle data, yet annotated 3D data from a cyclist's perspective is scarce. How well these detectors generalise to this setting has not been evaluated. We present a 3D object detection benchmark of 1,027 annotated LiDAR keyframes (over 18,000 3D bounding boxes) from the FUSE-Bike platform in urban Munich. We evaluate four nuScenes-pre-trained detectors against 1,854 human-verified ground-truth (GT) boxes both in their original form and after finetuning on training labels produced by a VRU-dedicated auto-labelling pipeline that requires no manual annotation. The zero-shot domain gap is concentrated on the VRU classes. Finetuning recovers most of it, improving mean average precision (mAP) by up to 23.4 points with the largest gains on pedestrians and cyclists, and the adapted detectors even surpass the quality of the auto-labels they were trained on. The benchmark provides a reproducible baseline for VRU-centric 3D detection and shows that auto-labels are a viable substitute for manual annotation when adapting vehicle-trained detectors to a cyclist platform.

---


### 163. [Learning Subset-Shared Invariances for Domain Generalization with Mixture-of-Experts](https://arxiv.org/abs/2606.25665)

**<font color=#1a73e8>作者：</font>** Tien-Hung Nguyen, Tien-Dat Tran, M.-Duong Nguyen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Domain generalization (DG) aims to learn a model from one or more source domains that generalizes to an unseen target domain without accessing target data during training. A common approach enforces invariance of representations across all source domains, assuming predictive structure is globally shared. However, we demonstrate that enforcing invariance across more domains gradually restricts the feasible representation space, discarding transferable predictive factors that are not universally shared. To address this limitation, we propose subset-shared invariance, where predictive structure is assumed stable only within domain subsets. We implement this principle with a mixture-of-experts architecture, where each expert aligns the specific domains it serves and a routing mechanism composes subset-invariant components for prediction. This creates a routing-conditioned invariance, jointly learned with the representation. To facilitate effective decomposition, we develop training objectives that encourage selective alignment, confident and balanced routing, and diverse expert specialization. Experiments on DomainBed benchmarks demonstrate improved out-of-domain generalization and greater robustness under increasing domain heterogeneity. Our results suggest that DG should move beyond enforcing a single global invariance and instead model invariance through partially shared structure across domain subsets.

---


### 164. [Dissociable Spatial and Temporal Effects of Interaction Latency in Virtual Reality](https://arxiv.org/abs/2606.25681)

**<font color=#1a73e8>作者：</font>** Xiaoye Michael Wang, Catherine M. Sabiston, Timothy N. Welsh  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Motion-to-photon latency is inherent in immersive virtual reality (VR) systems and can arise from multiple sensorimotor loops, including view-contingent latency between head movement and display update and interaction latency between hand movement and the virtual effector. Although prior work shows that interaction latency can impair VR performance, it remains unclear whether common spatial, temporal, and efficiency measures reveal the same latency-related disruption. This study addressed this question by experimentally imposing delays between the physical and virtual hands during manual pointing in VR. Participants pointed to targets on a horizontal surface in VR and in the physical environment as an unmediated baseline. In VR, pointing was performed with a virtual hand avatar controlled by a motion capture pipeline, and additional delays (0-500 ms) were imposed between the participant's hand movement and the rendered movement of the virtual hand. Relative to the baseline, performance in VR showed greater endpoint error, longer movement time, greater endpoint variability, and lower throughput. Within VR, added interaction latency further increased endpoint error and variability, reduced throughput, and altered movement time, but these effects followed different profiles: endpoint error increased even at the shortest delays, whereas movement time remained stable at short delays and increased primarily at longer delays. These findings show that interaction latency produces dissociable spatial and temporal consequences in immersive VR, such that endpoint accuracy revealed disruption before movement time or throughput. Thus, latency-sensitive VR interactions cannot be fully evaluated using movement time or efficiency measures alone. Instead, HCI evaluations should assess both spatial and temporal performance, particularly when VR tasks involve visually guided manual actions.

---


### 165. [GUI agent: Guided Exploration of User-Sensitive Screens](https://arxiv.org/abs/2606.25705)

**<font color=#1a73e8>作者：</font>** Aradhana Nayak, Mussadiq Nazeer, Wang Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly being used to automate tasks for users within an open GUI environment. They inevitably encounter screens containing user-sensitive information, for which takeover of task execution by the user is highly desirable or even necessary. State-of-the-art LLM-driven agents are usually fine-tuned to complete tasks regardless of the safety implications of their actions. This makes their real-world deployment difficult and adversely affects the reliability. Therefore, it is crucial to identify and categorize user-sensitive states and define user-sensitive queries. This dataset would be to engineers to recognize and request handover to the user in critical scenarios. This short paper develops an explorer agent that systematically explores the query space starting from one demonstrated task to identify queries that, if executed, would lead to user-sensitive states in a GUI environment.

---


### 166. [Cellular Predictions on the Move: What about Data?](https://arxiv.org/abs/2606.25709)

**<font color=#1a73e8>作者：</font>** Natalia Vesselinova, Pauliina Ilmonen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile cellular load forecasting is native to network resource optimization and delivery of services with reliability, latency and quality guarantees. The mainstream of machine learning research in the area is focused primarily on developing powerful learning structures for improved prediction accuracy. The data used for forecasting traditionally belong to the cellular domain and at most contain exogenous information about the surroundings of the base stations. We approach the prediction task from the perspective of data as a vital component of any data learning process. We hypothesize that substantial improvements could be achieved when the data inform on the processes that create the cellular load. Specifically, we propose to characterize the population dynamics -- the potential number of cellular traffic sources and their mobility -- in addition to employing historical time series of mobile data traffic. We validate our hypothesis for the rarely examined highway scenario. Comprehensive experiments show forecasting improvements on the order of $60\%$ due to the use of these data alone.

---


### 167. [Position Spaces and Graphs](https://arxiv.org/abs/2606.25719)

**<font color=#1a73e8>作者：</font>** Rita-Nathalia Assaf, Tom Davot, Frédéric Lardeux 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this paper, we introduce position graphs, a graph-based reasoning framework based on the formalization of position spaces. This framework utilizes two strict partial orders, representing horizontal and vertical alignment and precedence, to model the relative positions of discrete tokens. Unlike general qualitative spatial calculi, position graphs are constrained by a chain condition and compatibility requirements that focus on rows and columns. We provide a comprehensive theoretical analysis of this representation, beginning with a characterization of graph consistency. Conditions to ensure the consistency of position graphs are established. Furthermore, we investigate the computational complexity of structural pattern discovery, modeled as the induced subgraph isomorphism problem. We demonstrate that this problem remains NP-complete even within the restricted class of position graphs. While initially motivated by document processing, this work focuses on the underlying mathematical properties and algebraic consistency of position-based constraints, providing a formal logical layer that is independent of specific data extraction techniques.

---


### 168. [Tracing Target Answers in Poisoned Retrieval Corpora via Token Influence Attribution](https://arxiv.org/abs/2606.25721)

**<font color=#1a73e8>作者：</font>** Yan-Lun Chen, Pin-Yu Chen, Chia-Mu Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) systems are vulnerable to corpus poisoning attacks that manipulate model outputs through malicious retrieved documents. Existing detection methods typically rely on auxiliary classifiers or additional LLM-based verification, introducing substantial computational overhead. We present TRACE, a lightweight detection framework that identifies poisoning attacks by tracing answer-related tokens through token influence attribution. TRACE first discovers recurrent high-influence keywords across retrieved documents and then performs a secondary verification to confirm their influence on model predictions. Experiments on three QA benchmarks and six LLMs demonstrate strong detection performance while simultaneously uncovering attacker-specified target answers.

---


### 169. [Efficient Real-World Dehazing via Physics-Inspired Global-Local Decoupling](https://arxiv.org/abs/2606.25732)

**<font color=#1a73e8>作者：</font>** Yifei Qu, Ru Li, Junjie Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world single image dehazing is highly ill-posed due to spatially and spectrally varying scattering, while practical deployment demands lightweight and low-latency models. Existing approaches either rely on fragile physical inversion under simplified assumptions or adopt heavy blind architectures unsuitable for edge deployment. To overcome these limitations, we propose PGL-Net (Physics-Inspired Global-Local Decoupling Network), a lightweight framework that incorporates physical inductive biases via operator-level emulation, avoiding explicit parameter estimation. It decouples dehazing into global distribution rectification and local structural refinement. A Physics-Inspired Affine Fusion (PAF) module performs globally conditioned alignment across hierarchical skip connections to compensate for haze-induced bias, while a compact Degradation-Aware Modulation (DAM) block adaptively restores spatially and spectrally variant details through dynamic feature modulation. Extensive experiments on multiple real-world benchmarks demonstrate that PGL-Net achieves state-of-the-art restoration quality with significantly reduced complexity. Compared with the recent SOTA SGDN, the Tiny variant (PGL-Net-T) improves PSNR by up to 2.6dB and consistently enhances downstream object detection accuracy, while achieving over a 10x reduction in inference latency. Code is publicly available at: this https URL.

---


### 170. [Shoot the Honey, Cloak the Player: Towards Zero-Runtime-Overhead Proactive Defense and Detection for Visual Game Cheating](https://arxiv.org/abs/2606.25734)

**<font color=#1a73e8>作者：</font>** Jianing Wang, Chuqi Zhang, Yuancheng Jiang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Visual aimbots have emerged as a serious cheating threat in first-person shooter (FPS) games, as they evade existing anti-cheat defenses by operating only on rendered frames rather than game memory. However, existing defenses fail to provide an end-to-end solution: post-hoc behavior detectors cannot protect match integrity in real time and are increasingly fragile against human-mimicking aimbots, while proactive runtime defenses often lack accountability, incur substantial overhead, or require intrusive system integration.
We present AimTrap, the first end-to-end defense against visual aimbots that combines real-time protection with post-game detection using two adversarial texture mechanisms. Adversarial Camouflage Textures (ACT) hide real players from aimbots, while Adversarial Honeypot Textures (AHT) lure aimbots into locking onto fake targets, yielding strong evidence of cheating. To make this practical, AimTrap integrates differentiable rendering with Expectation over Renderings for robust 3D texture synthesis, secure texture management, and a novel honeypot-interaction trajectory analysis pipeline for accurate cheating attribution.
In real-game evaluation against a state-of-the-art visual aimbot, ACT achieves 85.1% defense success, AHT achieves 96.9%. Compared with prior baselines, AimTrap attains extremely low false-positive rates, while incurring negligible runtime overhead. These results show that AimTrap provides a practical and effective end-to-end defense against visual aimbots.

---


### 171. [UniTeD: Unified Temporal Diffusion for Joint Perception and Planning in Autonomous Driving](https://arxiv.org/abs/2606.25736)

**<font color=#1a73e8>作者：</font>** Bo Zhao, Xinting Zhao, Naifan Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have shown strong potential for multi-modal planning in end-to-end autonomous driving. However, most existing methods confine diffusion to the planning module, conditioning on fixed outputs from separate discriminative perception networks. This decoupled design propagates perception errors to the planner, increasing optimization difficulty and reducing robustness. To overcome these limitations, we propose UniTeD, a Unified Temporal Diffusion framework that jointly models perception and planning through iterative denoising in a shared generative space. By enabling bidirectional information exchange, the framework facilitates mutual refinement between tasks and improves robustness via noise-conditioned multi-task training. We further extend this unified diffusion paradigm to a streaming setting by incorporating temporal context. A Temporal Transition Module (TTM) is introduced to resolve the noise-level mismatch between historical and current frames. In addition, we propose an Anchor Refresh Strategy (ARS) to alleviate the training-inference distribution shift commonly observed in sparse diffusion-based end-to-end driving frameworks. Without bells and whistles, UniTeD achieves state-of-the-art performance across multiple benchmarks, surpassing both recent discriminative end-to-end methods and diffusion-based planning approaches.

---


### 172. [Point Cloud Diffusion with Global and Local Reconstruction for Instance-Level 3D Anomaly Detection](https://arxiv.org/abs/2606.25740)

**<font color=#1a73e8>作者：</font>** Linchun Wu, Qin Zou, Jiwen Lu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> 3D anomaly detection in point clouds is critical for high-precision industrial manufacturing. Reconstruction-based methods have laid a strong foundation by detecting 3D anomalies through comparisons between defective inputs and their reconstructed normal counterparts. However, existing methods still suffer from two challenges: 1) the foreground weak defective regions such as scratches are hard to reconstruct and detect, where the anomaly deviations in normalized point clouds can be as small as $10^{-3}$; 2) the background non-defective regions are prone to get positional bias in reconstruction, which leads to false positives. To address these challenges, we propose \textbf{PCDiff}, a point cloud diffusion framework for instance-level 3D anomaly generation and detection. In the generation phase, an instance-level multi-modal attention is embedded into the generation framework, where anomalies are conditioned with texture gradient, image patch, text and mask. The instance-level condition enables the high-quality generation of weak-defective anomalies. In the detection phase, a joint local-global reconstruction algorithm is introduced to ensure local anomaly restoration and global geometric consistency, which preserves background normal structure while restoring the foreground defect. Extensive experiments demonstrate that the proposed PCDiff significantly outperforms state-of-the-art methods in both 3D anomaly generation fidelity and reconstruction quality, leading to substantial improvements in anomaly detection accuracy.

---


### 173. [Black-Box Assisted Regression: Phase Transitions and Minimax Optimality](https://arxiv.org/abs/2606.25743)

**<font color=#1a73e8>作者：</font>** Yan Zhou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Foundation models are often used as fixed black-box predictors for downstream tasks with limited labeled data, but their predictions may be biased and unsafe to trust blindly. We study this setting through black-box assisted nonparametric regression: a learner observes labeled samples and can query a fixed predictor $f_0$, while the target $f^*$ is close to $f_0$ in $L_2(P_X)$ up to an unknown radius $\delta$. We give a finite-sample minimax characterization showing a phase transition at $\delta_c(n) \asymp n^{-\beta/(2\beta+d)}$, with leading risk $\min\{\delta^2, n^{-2\beta/(2\beta+d)}\}$. We then analyze a Safe Residual Estimator: it learns a correction around $f_0$, initializes the residual head at zero so the initial predictor equals $f_0$, and uses holdout selection to revert to $f_0$ when the learned correction is not supported by validation data. Here, "safe" means avoiding negative transfer, i.e., performing worse than the black-box predictor alone. The estimator matches the leading minimax term up to an additive validation-selection cost. Synthetic regression experiments verify the predicted phase transition, while CIFAR-100 with CLIP and AG News with Qwen3-8B provide practice-facing evidence that the same residual-correction tradeoff is useful beyond the formal squared-loss regression setting.

---


### 174. [Gradient-based inverse lithography for EUV masks via the waveguide method and a physics-informed neural operator](https://arxiv.org/abs/2606.25753)

**<font color=#1a73e8>作者：</font>** Vasiliy A. Es'kin, Egor V. Ivanov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-based inverse lithography technology~(ILT) for extreme ultraviolet~(EUV) masks is presented. A novel framework treats the differentiable waveguide method and the recently proposed waveguide neural operator~(WGNO) as end-to-end physics engines, recovering the permittivity of the absorber of the mask through automatic differentiation of the full forward diffraction model. Numerical experiments on realistic 2D and 3D absorbers of the mask (TaBN, La, U) at $\lambda{=}11.2$~nm show that the considered ILT methods make it possible to obtain a mask structure that achieves the desired field on the wafer.

---


### 175. [Dual Distribution Estimation for Zero-shot Noisy Test-Time Adaptation with VLMs](https://arxiv.org/abs/2606.25758)

**<font color=#1a73e8>作者：</font>** Wenjie Zhu, Yabin Zhang, Liang Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While test-time adaptation (TTA) empowers vision-language models to adapt without costly retraining, it remains highly vulnerable to out-of-distribution (OOD) outliers prevalent in real-world applications. This discrepancy motivates Noisy TTA (NTTA), an online task to filter noisy OOD samples on the fly while maximizing in-distribution (ID) classification accuracy. Existing zero-shot NTTA approaches typically rely on test-time discriminative training, leading to overconfident misclassifications and significantly degraded inference efficiency. To address these limitations, we propose a novel framework named Dual Distribution Estimation (DDE), shifting the zero-shot NTTA paradigm from instance-level learning to training-free Gaussian distribution modeling. DDE incorporates two novel modules: Positive Feature Distribution Estimation (PFDE) and Negative Label Distribution Estimation (NLDE). PFDE explicitly models class-wise inclusion and exclusion Gaussian distributions to formulate a calibrated contrastive score, robustly enhancing ID accuracy. In parallel, NLDE improves OOD identification by explicitly modeling the negative label distribution to mine highly discriminative labels, effectively mitigating spurious correlations. Extensive experiments show that on the large-scale ImageNet benchmark, DDE achieves an improvement of 3.70\% in harmonic mean accuracy and reduces the FPR95 for OOD detection by 6.20\%, while ensuring highly scalable and efficient online inference. Furthermore, DDE is zero-shot and training-free, demonstrating remarkable robustness in data-scarce scenarios. Codes are available at this https URL.

---


### 176. [Bridging Spherical Black-Box Optimizers](https://arxiv.org/abs/2606.25761)

**<font color=#1a73e8>作者：</font>** Johannes Ackermann, Stefano Peluchetti  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When gradient information is unavailable, black-box optimization (BBO) methods provide a practical alternative. While Evolution Strategies (ES), Consensus-Based Optimization (CBO), Optimization via Integration (OVI), and related methods have each been studied independently, their connections remain underexplored. We unify these approaches within a common theoretical framework, revealing that they differ primarily in two design choices: fitness aggregation (controlling sharpness preference) and consensus scope (controlling modality). Leveraging these insights, we introduce hybrid optimizers that interpolate between existing methods. Our ES-OVI hybrid allows explicit control over the preference for flat minima, enabling a trade-off between performance and robustness in continuous control tasks. Our CBO-OVI hybrids combine the higher-dimensional efficiency of parametric methods with the multimodal capabilities of particle-based approaches, achieving competitive results on language model merging under limited evaluation budgets. We validate our methods on standard BBO benchmarks and higher-dimensional locomotion tasks, demonstrating that the hybrid methods can outperform their constituent algorithms.

---


### 177. [OncoSynth: Synthetic data generation for treatment effect estimation in oncology](https://arxiv.org/abs/2606.25762)

**<font color=#1a73e8>作者：</font>** Octavia-Andreea Ciora, Julian Welzel, Dennis Frauen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In oncology, access to patient-level data is often restricted. Synthetic data provides an alternative for analyzing treatment effectiveness, but existing methods for synthetic data generation fail to preserve the causal relationships between covariates, treatments, and outcomes, thereby leading to biased estimates of treatment effects. Here, we introduce OncoSynth, a generative, causally-aware machine learning framework designed to produce synthetic cohorts that enable accurate estimation of population- and patient-level treatment effects. OncoSynth uses a diffusion-based sequential approach to model how covariates influence treatment assignment and how treatment affects survival. We evaluate OncoSynth using large lung (N = 37,128) and breast cancer (N = 17,046) cohorts. Our results show that OncoSynth generates high-fidelity synthetic patient cohorts that preserve real-world patient, treatment, and outcome distributions. Notably, OncoSynth improves treatment effect estimation over existing approaches, by reducing population-level treatment effect error by up to 66%, and patient-level treatment effect error by up to 58%. Thereby, OncoSynth supports reliable evidence generation for precision oncology in settings where data sharing is restricted.

---


### 178. [Deep Neural Networks with Ordinal Loss for Medical Applications](https://arxiv.org/abs/2606.25769)

**<font color=#1a73e8>作者：</font>** Tal Dvora, Rotem Haba, Gonen Singer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In many prediction problems in medical applications, target labels exhibit an inherent ordinal structure, where class ordering reflects clinically meaningful severity levels. The cost associated with misclassification is often non-uniform and asymmetric, as errors between distant ordinal categories may have substantially more severe consequences than errors between adjacent ones, and overestimating disease severity may have different clinical implications than underestimating it. Traditional loss functions such as multi-class cross-entropy treat all misclassifications equally and fail to incorporate this ordering information. Recent advances in ordinal regression aim to address this limitation by integrating rank-based structures into deep learning models. In this work, we introduce the \textbf{Ordinal Cross-Entropy (OCE)} framework, a general and architecture-independent approach for learning from ordinal data. The proposed method extends the standard cross-entropy formulation to account for misclassification severity through an ordinal cost matrix while preserving the probabilistic interpretation and optimization benefits of the conventional loss. We provide a theoretical analysis of the OCE gradient behavior and show that it yields smoother optimization dynamics and improved ordinal consistency. Experiments on benchmark datasets show that our method achieves lower prediction error costs and better calibration compared to existing state-of-the-art ordinal approaches, establishing OCE as a simple yet effective solution for ordinal regression in deep neural networks.

---


### 179. [Re-mixing Embeddings for Patient Augmentation in Data Scarce Multiple Instance Learning](https://arxiv.org/abs/2606.25770)

**<font color=#1a73e8>作者：</font>** Muhammed Furkan Dasdelen, Fatih Ozlugedik, Anastasia Litinetskaya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data scarcity is a major bottleneck in medical Multiple Instance Learning (MIL), especially for rare diseases or expensive modalities. We introduce a statistically grounded patient augmentation approach that generates realistic patients directly in embedding space. Using Gaussian Mixture Models as a probabilistic clustering approach on pooled instance embeddings from all patients, our method learns disease-specific "recipes"-statistical distributions of instances across unsupervised clusters. New patients are then generated by sampling embeddings from clusters based on learned recipes. Unlike existing methods that require examples from all categories, our method can generate patients offline by re-mixing pooled embeddings. Generated patients are further selected based on uncertainty quantification to improve MIL performance. We evaluate our method across three clinically relevant scarcity scenarios: (i) cross-dataset transfer, where an entirely missing "healthy" class is generated using statistics from an external cohort; (ii) low-data regimes, where class sizes are extremely limited; and (iii) small-cohort non-image tasks, including single-cell RNA-seq and flow cytometry. Across all experiments, our method improves performance over baseline, often outperforming other bag-mixing strategies. Notably, in the missing-class scenario, a performance comparable to full-dataset training is achieved, demonstrating its potential for rare disease diagnostic and privacy-preserving patient augmentation. The code is available at this https URL

---


### 180. [Fuzzy Quantification over OWL Ontologies and Knowledge Graphs](https://arxiv.org/abs/2606.25778)

**<font color=#1a73e8>作者：</font>** Enrique Palacín, Fernando Bobillo, Ignacio Huitzil 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents a versatile framework for evaluating fuzzy quantification queries over both standard and fuzzy ontologies as well as knowledge graphs. The primary objective is the retrieval of individuals that satisfy queries articulated via Type I or Type II fuzzy quantified expressions. A key advantage of the proposed approach is its inherent adaptability: it remains entirely agnostic to the quantifier type, the underlying evaluation method, and the specific data source of the ontology (i.e., OWL ontologies or RDFS knowledge graphs). Furthermore, we present Q2S2, a publicly accessible implementation of this system developed to support future research.

---


### 181. [$S^{2}$-FracMix: Label-Preserving Self-Saliency Mixup Augmentation](https://arxiv.org/abs/2606.25784)

**<font color=#1a73e8>作者：</font>** Khawar Islam, Arif Mahmood, Xin Jin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data augmentation is known to improve generalization of deep visual models. Recent methods favor mixup strategies that generate interpolated samples to improve model performance. However, these techniques not only incur significant computational overhead, they also lead to semantic disruption of augmentation data due to cross-sample mixing. We first propose Self-Saliency ($S^2$) Mixup, which constructs challenging yet label-consistent samples by extracting multi-scale salient patches and reinserting them into non-salient regions of the same image. This promotes scale-invariant feature learning while avoiding cross-sample interference. To further enhance model robustness, we introduce FracMix, a mixing scheme that injects self-similarity patterns into salient regions using adaptive ratios. Collectively, our unified framework, $S^{2}$-FracMix, enables simultaneous learning from fractal and non-fractal structures within a single image, yielding a targeted and structurally coherent augmentation strategy. We theoretically analyze the advantage of our technique, and empirically establish its superiority over the existing methods by achieving state-of-the-art performance in extensive evaluation with seven benchmarks across classification (coarse and fine-grained), robustness, calibration, object detection, and transfer learning tasks. Project page is available at \href{this https URL}{this http URL}

---


### 182. [Confidence Sequences for Online Statistical Model Checking of Markov Decision Processes](https://arxiv.org/abs/2606.25797)

**<font color=#1a73e8>作者：</font>** Konstantin Kueffner, Tobias Meggendorfer, Maximilian Weininger 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Markov decision processes (MDPs) are a classic model of decision making under uncertainty, exhibiting both non-deterministic choice as well as probabilistic uncertainty. Traditionally, exact knowledge of the underlying probabilities is assumed. However, this often is unrealistic, e.g.\ when modelling cyber-physical systems or biological processes. Here, statistical methods provide a way towards obtaining meaningful guarantees. The classical approach is to gather samples in the MDP, use these to draw statistical conclusions about the transition probabilities, and from there obtain bounds on the true value; then, if these bounds are too broad, repeat. However, existing implementations of this approach are either subtly incorrect or sub-optimal, and quite often both. We present several \emph{confidence sequences}, which are specifically designed for such \enquote{online} settings, implement all of them in an efficient tool, and show their practical applicability. In particular, we show that they outperform classical \enquote{union-bound} style approaches, and overall our implementation requires 50x less samples on average than previous state of the art.

---


### 183. [ROAD-VLA: Robust Online Adaptation via Self-Distillation for Vision-Language-Action Models](https://arxiv.org/abs/2606.25800)

**<font color=#1a73e8>作者：</font>** Kejing Wang, Toan Nguyen, Minh Hoang Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Effective online adaptation of vision-language-action (VLA) models remains challenging, as sparse rewards provide weak supervision for high-dimensional autoregressive action policies. Although self-distillation can in principle provide denser training signals, we find that text-based privileged teachers conditioned on demonstrations, retrieved experiences, or high-level plans are ineffective for VLA adaptation, exposing a modality gap between symbolic guidance and low-level robot actions. We propose ROAD-VLA, an advantage-guided self-distillation framework that constructs a proximal teacher directly in action space by perturbing action-token logits with calibrated advantage estimates. This converts sparse rewards into dense token-level supervision while keeping the teacher close to the current policy. We further derive a policy-improvement lower bound under calibrated advantages and accurate teacher matching. Across seven robotic manipulation environments with in-distribution and out-of-distribution shifts, ROADVLA outperforms PPO in nearly all settings, demonstrating robust online VLA adaptation.

---


### 184. [Shift Variant Image Degradation and Restoration Using Singular Value Decomposition](https://arxiv.org/abs/2606.25818)

**<font color=#1a73e8>作者：</font>** Arun D. Kulkarni  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Shift-variant image degradation is frequently encountered in practical imaging systems where the point spread function (PSF) varies across the image field due to motion, optical aberrations, atmospheric turbulence, or sensor-related effects. Unlike shift-invariant, shift-variant degradation presents significant challenges for image restoration because the degradation process cannot be represented by a single convolution kernel. This paper proposes a singular value decomposition (SVD)-based framework for restoring images degraded by shift-variant motion blur. The proposed approach determines the contribution of small singular values using a singular-value energy retention criterion. Specifically, the number of small singular values is selected based on a specified percentage of cumulative singular-value energy, providing a systematic approach for controlling noise amplification while preserving useful image information. The degradation model is formulated using a position-dependent PSF represented by a shift-variant imaging operator. Three representative one dimensional shift-variant motion PSFs are considered: bidirectional linear motion, Gaussian motion, and simple harmonic motion. The image degradation process is modeled as a linear system, and SVD is employed to analyze and invert the corresponding degradation operator. The singular-value representation provides insight into the ill-conditioned nature of the restoration problem and enables the development of stable inversion techniques. The proposed SVD-based restoration algorithm is applied to three degraded images. Experimental results demonstrate the effectiveness of the proposed approach in recovering image details and reducing blur artifacts under different motion models.

---


### 185. [Edges Before Embeddings: A Confidence-Aware Blur Gate for Vision-Language Pipelines](https://arxiv.org/abs/2606.25838)

**<font color=#1a73e8>作者：</font>** Duy Tran Thanh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Production vision pipelines silently degrade on blurry input, wasting compute on downstream OCR, retrieval, and vision-language model (VLM) calls that cannot recover a usable output. We present MagikaDocumentFromPixel, a lightweight, CPU-friendly image quality gate that classifies a single image as sharp, blurred, or uncertain in roughly 7 ms on a single CPU core. The contributions are (i) a recipe selected from a 46-configuration, 8-sweep empirical search that isolates input resolution as the dominant lever and shows architecture capacity only pays off at >= 384 px; (ii) a confidence-aware routing formalism grounded in classical selective prediction; (iii) the Edge Prior Module (EPM), a Laplacian-magnitude auxiliary input channel that gives the network direct access to the spectral evidence that classical blur heuristics rely on and that lifts test F1 by +1.3 points in a matched-env comparison; and (iv) an observation that the gate is one instance of a recurring design pattern that appears independently in Magika content-type detection, risk-controlled OCR with VLMs, and DocVLM. The final recipe MobileNetV3-Large with the EPM trained at 384x384 on paired GoPro Large frames, evaluated with 5-scale test-time augmentation reaches F1 = 0.9803 (AUC 0.9989) with a 17 MB ONNX artifact, improving over our fixed-scale baseline on the same hardware (F1 = 0.9672) by +1.31 points. We are explicit about limitations: results are on a single motion-blur distribution, numbers are from a single seed, and calibration is qualitative rather than measured.

---


### 186. [Naturalness Predicts but Does Not Cause Transferability in Image Encodings of Real-World Streams](https://arxiv.org/abs/2606.25844)

**<font color=#1a73e8>作者：</font>** Faruk Alpay, Baris Basaran  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A common practice converts a one-dimensional signal into an image so that a vision backbone pretrained on natural photographs can be reused for recognition, yet the encoded image is rarely examined. We ask how the visual naturalness of an encoded image relates to its transfer accuracy under a frozen backbone. We build WorldStream, a corpus of 299 heterogeneous current-value series from key-free public APIs (weather, air quality, earthquakes, gold and oil, equities, crypto, foreign exchange, web activity and space weather), with a nine-way source-recognition task over 3143 temporally split windows. Across seven encodings and six frozen backbones, the Frechet distance of an encoding to natural images (FID) predicts its accuracy: Spearman $\rho=-0.72$. Two controlled interventions show this is not causal in the spectrum. Our invertible encoder has a single adjustable part, a spectral exponent $\beta$ (power $\propto |f|^{-\beta}$); varying $\beta$ moves the image toward or away from the natural-image manifold at fixed content. FID is lowest near the natural value $\beta \approx 2$, but frozen accuracy stays flat and far below the structured baselines (19.2% vs. 73.0%), and FID and accuracy are only weakly related over the sweep (Pearson $-0.32$). A second intervention, phase scrambling, holds the power spectrum exactly fixed while removing local structure; now FID and accuracy fall together (Pearson $-0.89$). The cross-encoding correlation is thus mediated by local structure, not spectral naturalness: FID predicts accuracy because Inception reads the same structure the backbones do. Full fine-tuning does not close the gap (27% vs. 67%), so the deficit is structural. The encoder is exactly invertible, recovering the signal from the 8-bit image at 72.9 dB, so the image doubles as a lossless record of the data.

---


### 187. [Color Matters: Trigger Color Affects Success in Federated Backdoor Attacks](https://arxiv.org/abs/2606.25858)

**<font color=#1a73e8>作者：</font>** Kavindu Herath, Joshua C. Zhao, Saurabh Bagchi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning is vulnerable to backdoor attacks in which malicious clients inject poisoned updates while preserving benign-task performance. In this paper, we study a semantics-driven backdoor mechanism in which attackers use natural visual accessories as triggers and manipulate only the trigger color while keeping the attack pipeline fixed. Our framework considers semantic trigger objects such as masks and sunglasses, instantiated in black and white variants, and evaluates their effect in a controlled federated learning setting. Malicious clients construct poisoned samples by applying a trigger to source-class images and relabeling them to an attacker-chosen target class, while benign clients train only on clean data. We analyze this mechanism under both a standard poisoning objective and a stronger SABLE-based objective that combines clean classification loss, triggered target loss, feature-separation loss in the penultimate representation space, and regularization to keep malicious updates close to the global model. This design enables the attack to remain effective while reducing excessive update drift. Experiments on a four-class CelebA hair-color task show that trigger color significantly changes attack success rate even when trigger semantics, placement, and poisoning budget are unchanged. White triggers are more effective for attacks targeting the blond class, whereas black triggers perform better for attacks targeting the black class. The same trend persists under robust aggregation, showing that trigger color is a meaningful factor in the operation, persistence, and evaluation of semantic backdoor mechanisms in federated learning.

---


### 188. [An Analysis of Posterior Collapse, Parameterization and Initialization in Variational Deep Gaussian Processes](https://arxiv.org/abs/2606.25882)

**<font color=#1a73e8>作者：</font>** Francisco Javier Sáez-Maldonado, Juan Maroñas, Daniel Hernández-Lobato  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> DGPs are probabilistic models with remarkable prediction performance that concatenate GPs across several layers. Exact inference in DGPs is intractable, and variational inference is often used to approximate the posterior with a parametric distribution tuned by minimizing the Kullback-Leibler divergence. Moreover, finding a good VI approximation is challenging. In particular, a problem of VI is posterior collapse, where VI converges to a variational posterior that matches the prior. In variational DGPs, this implies explaining the data as noise. This work studies posterior collapse in DGPs and identifies its connection to the DSVI algorithm and the widely used linear prior mean function employed in all but the last layer. We show that the benefit of the linear prior mean does not arise from avoiding the non-injective pathology in very deep DGPs, as previously believed, but from improving the conditioning of the optimization problem at initialization. Thus, we propose an alternative initialization of a zero prior mean DGP that mimics a DGP with a linear prior mean at initialization. This enables successful training of DGPs without imposing optimization-driven constraints on the prior, allowing to choose the prior based on modeling assumptions rather than optimization convenience. Our analysis considers three common parameterizations of DGPs and shows that not all of them benefit from a linear prior mean. We also explain why a whitened parameterization of the \DGP provides more stable convergence, something often assumed from experience, but lacking a rigorous analysis. Furthermore, we show that this stability is also beneficial to avoid the posterior collapse problem. Extensive experiments validate our findings: the proposed initialization prevents posterior collapse, improves stability, and achieves performance comparable to (and sometimes better than) DGPs with a linear prior mean.

---


### 189. [Enhancing Brain MRI Anomaly Detection and Reasoning with ROI Rethink and Synthetic Data](https://arxiv.org/abs/2606.25894)

**<font color=#1a73e8>作者：</font>** Shangkun Li, Jie Xu, Yi Guo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical vision-language models typically generate diagnoses through single-pass inference without indicating which image regions support their conclusions. This lack of spatial grounding limits clinical utility: outputs cannot be audited, and models may hallucinate findings on normal scans. We present BrReMark (Brain Rethink via ROI Marking), a framework that introduces explicit region marking into brain MRI diagnosis. The model first generates hypotheses about potential abnormalities and grounds them through explicit bounding box marking, then verifies conclusions by re-examining the marked evidence. Training combines supervised fine-tuning on structured reasoning trajectories with reinforcement learning using a composite reward over localization accuracy and diagnostic reasoning. Furthermore, we integrate a domain randomization-based pathology synthesis augmentation strategy to improve the model's generalizability to out-of-distribution (OOD) data. On internal benchmark, BrReMark improves mAP50 from 0.74% to 37.54% compared to the base model, while achieving 21.57% Clinical F1 and 45.26% diagnostic accuracy. On NOVA OOD benchmark, it also achieves competitive overall performance with a 45.7% reduction in false positives compared to the state-of-the-art, indicating reduced hallucination on rare pathologies. These findings suggest that explicit hypothesis-verification grounding is a practical path toward trustworthy open-ended brain MRI diagnosis across both in-distribution and OOD settings.

---


### 190. [Variational Autoencoder Layer](https://arxiv.org/abs/2606.25900)

**<font color=#1a73e8>作者：</font>** Gananath R  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Variational Autoencoders (VAEs) belong to a family of autoencoders with probabilistic properties, making them well suited for generating data by producing a smooth and continuous latent space. Despite being introduced over a decade ago, the method continues to be widely adopted in both research and industry for diverse applications. While VAEs are typically used as standalone models, this paper introduces a novel approach to integrate them as a neural network layer. Furthermore, a new training strategy is proposed for models incorporating these layers, and their performance is thoroughly analyzed.

---


### 191. [FunPiQ: A New Benchmark for Pixel-Level Quality Assessment in Fundus Images](https://arxiv.org/abs/2606.25915)

**<font color=#1a73e8>作者：</font>** Pengwei Wang, José Morano, Virginia Mares 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Color fundus photography (CFP) is the most common ophthalmic imaging modality for large-scale screening. However, it is highly susceptible to degradations, making robust fundus image quality assessment (FIQA) crucial. The criteria for what constitutes high-quality at the image level vary across clinical tasks, making FIQA dependent on expert knowledge. This motivated the development of automated methods and datasets. While existing datasets aim to standardize image-level quality, their criteria often differ. Furthermore, image-level labels preclude the quantitative evaluation of localized degradations, which is essential for trustworthy FIQA. We argue that pixel-level FIQA based on anatomical visibility represents a more task-agnostic, explainable approach. In this work, we introduce FunPiQ, the first FIQA benchmark to provide pixel-level quality annotations. In addition, we propose EFIQA-CP, an explainable-by-design (EBD) method that uses quality pseudo-labels based on anatomical visibility to train a CNN via Non-Negative Positive-Unlabeled learning. Extensive evaluations of classification methods with post-hoc explanations, anomaly detection methods, and EBD methods demonstrate the superior performance of the last and, particularly, of EFIQA-CP.

---


### 192. [$\text{DT}^2$: Decision-Targeted Digital Twins](https://arxiv.org/abs/2606.25923)

**<font color=#1a73e8>作者：</font>** Harry Amad, Mihaela van der Schaar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A digital twin (DT) is a virtual model of a real-world system that can assist decision-making by simulating scenarios induced by different policies. However, typical machine learning-based DTs do not optimise for this use case. We prove that, when model capacity is limited, training DTs to minimise one-step transition errors can produce suboptimal models for ranking sets of policies according to a reward function. We further show that this holds empirically, even with expressive model classes. To address this, we introduce $\text{DT}^2$, a decision-targeted DT training paradigm. Firstly, $\text{DT}^2$ uses fitted Q-evaluation to estimate values of candidate policies from offline data. A DT is then trained to generate rollouts that preserve pairwise policy rankings derived from these proxy ground-truth values with an architecture-agnostic loss function. We empirically demonstrate the efficacy of our method across a range of settings and architectures. $\text{DT}^2$ consistently improves policy ranking and reduces decision regret during policy selection relative to conventional DT training, both for policies used during training and for unseen policies, while maintaining a good level of raw simulation fidelity.

---


### 193. [A Tattered Cloak of Invisibility: Measuring Anonymity Loss in Railgun on Ethereum](https://arxiv.org/abs/2606.25926)

**<font color=#1a73e8>作者：</font>** Kanan Huseynov, Ali Shahzaib, István András Seres 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> From a user's perspective, perhaps the most significant difference between traditional banking services and widely used blockchain-based financial systems is that, in the latter, transactions and, either directly or indirectly, account balances and transaction histories are publicly observable. Therefore, a growing number of cryptographic solutions have been proposed to add a privacy layer to such systems. However, the privacy that users actually obtain does not depend solely on the security of the underlying cryptographic protocol: user behavior, transaction amount patterns, and timing decisions can substantially reduce anonymity.
In this work, we study behavioral leakage in cryptocurrency mixers, focusing on Railgun on Ethereum. We aim to heuristically estimate the probability that a given deposit and withdrawal transaction belong to the same user. We consider five sources of leakage: characteristic timing patterns, address reuse, proximity in the transaction graph induced by prior public transactions, amount fingerprints that preserve distinctive digit patterns across transaction values, and knapsack type matches in which groups of transaction amounts add up in revealing ways. Our results show that even cryptographically strong privacy systems may suffer substantial anonymity loss due to user behavior and transaction patterns. Our five heuristics are able to uniquely link 17.65% of Railgun withdraw transactions to deposit transactions. We also applied a knapsack solver algorithm that was able to produce a 3.42 bit median anonymity loss for withdraw transactions. This work contributes to a better understanding of the practical privacy limits of mixers and anonymity pools, and points toward safer usage practices and design principles.

---


### 194. [Overview of HIPE-2026: Person-Place Relation Extraction from Multilingual Historical Texts](https://arxiv.org/abs/2606.25935)

**<font color=#1a73e8>作者：</font>** Juri Opitz, Maud Ehrmann, Corina Raclé 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Was this person ever at that place, and if so, when? Answering such questions from noisy, multilingual historical documents is the central challenge of HIPE-2026, the third edition of the HIPE evaluation series. Moving from named entity recognition and linking (HIPE-2020, HIPE-2022) to reasoning about relationships between entities, HIPE-2026 targets two temporally grounded relation types: $at$, indicating that a person was present at a location at some point prior to a document's publication date, and $isAt$, indicating presence contemporaneous with that date. This paper presents the results of the evaluation campaign, which confronted 17 participating teams with the challenges of historical language variation, OCR noise, and indirect contextual cues across three languages: French, German, and English. The datasets include historical newspaper text from the nineteenth and twentieth centuries, as well as a surprise-domain generalization set drawn from early modern French literary texts. A distinctive feature of HIPE-2026 is its three-fold evaluation framework, which assesses predictive accuracy, computational efficiency, and cross-domain generalization, reflecting the practical demands of large-scale historical document processing in the cultural heritage domain. Across more than 40 submitted runs, results reveal a wide range of strategies, from state-of-the-art large language models to lightweight task-specific classifiers, and highlight the trade-offs between accuracy, efficiency, and robustness inherent to historical relation extraction at corpus scale. System descriptions, datasets, and findings are presented and discussed, offering a detailed picture of the current state of temporally grounded relation extraction for historical documents.

---


### 195. [Do (Not) Tell Me About My Insecurities: Assessing the Status Quo of Coordinated Vulnerability Disclosure in Germany Amid New EU Cybersecurity Regulations](https://arxiv.org/abs/2606.25950)

**<font color=#1a73e8>作者：</font>** Sebastian Neef, Cenk Schlunke, Anne Hennig  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In our increasingly interconnected world, good IT security practices are necessary to prevent vulnerabilities and data breaches. Providing security contacts, e.g., via Coordinated Vulnerability Disclosure (CVD) programs or this http URL files, is an important practice for businesses to facilitate vulnerability reporting by external parties. As part of a longitudinal study, we analyzed the adoption of, as well as the challenges and experiences with, CVD programs among the 40 companies listed on Germany's DAX (the country's primary stock market index). In addition to monitoring publicly available information about their CVD programs, we sent out questionnaires via email and postal mail in 2023 and 2025, and received answers from 20\% of the companies. The adoption rates show a significant increase from 50\% (2023) to over 90\% (2025), with ten new CVD programs and 25 new this http URL files now available. The survey answers reveal that, for example, legal obligations (e.g., NIS2 and CRA) drive the adoption of CVD practices, but a lack of (human) resources and varying report quality are considered drawbacks. As the first study to survey 40 German stock market index (DAX) companies on their CVD practices, our results can help foster the adoption and understanding of security programs among SMEs and other companies, and provide policymakers with insights into practical challenges and industry experiences.

---


### 196. [Pulmonary Embolism Risk Stratification from CTPA and Medical Records: Vascular Graphs Are Not All You Need](https://arxiv.org/abs/2606.25956)

**<font color=#1a73e8>作者：</font>** Nathan Painchaud, Tristan Habémont, Morgane des Ligneris 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Risk stratification for pulmonary embolism (PE) is critical for clinical decision-making. Stratification guidelines are based on patient medical records, parameters measured from computed tomography pulmonary angiography (CTPA), and blood tests. However, blood tests are often missing in routine practice. This work studies whether state-of-the-art models can accurately classify risk stratification from only medical records and biomarkers extracted from CTPA images. We benchmark different approaches to combine medical records and cardiac biomarkers with rich pulmonary vascular information; we add vascular biomarkers to tabular models and apply graph neural networks (GNNs) on the vascular tree's intrinsic graph representation. We use a private dataset (n=353) with uniquely complete data for PE risk stratification. Our results show that, among global features, medical records and cardiac biomarkers are the most significant predictors, while vascular biomarkers do not further improve stratification. Even more surprising, even GNNs on vascular graphs fail to outperform strong tabular baseline on global features. We consider hypotheses, on both models and data, that could explain this suboptimal performance. Our investigation suggests that, counter-intuitively, vascular graphs might hold no discriminative information for PE risk stratification. Code is available from this https URL.

---


### 197. [A Benchmark for Heterogeneous Stereo Deblurring with Physically- and Epipolar-constrained Cross Attention](https://arxiv.org/abs/2606.25962)

**<font color=#1a73e8>作者：</font>** Hoju Shin, Jiah Kim, Seung-Wook Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern stereo-capable smartphones enable immersive XR content capture. However, hardware heterogeneity across camera modules often causes severe asymmetric blur artifacts. Existing methods and benchmarks largely assume homogeneous stereo setups and therefore do not explicitly address such asymmetric degradation. To bridge this gap, we present a dedicated framework for heterogeneous stereo deblurring. First, we introduce the heterogeneous stereo deblurring (HSD) dataset, constructed from real smartphone stereo captures via multi-frame integration. Second, we propose physically- and epipolar-constrained cross attention (PECA), a lightweight module that restricts cross-view matching to an epipolar search window bounded by a optics-derived disparity upper bound. By enforcing physically valid disparity constraints, PECA enables efficient and reliable cross-view feature fusion. Moreover, our confidence-weighted attention with residual fusion emphasizes cross-guided deblurring when correspondences are reliable, while naturally falling back to self-deblurring in occluded or unreliable regions. PECA is architecture-agnostic and consistently improves CNN-, Transformer-, and NAFNet-based baselines. Extensive experiments on HSD show that PECA-enhanced models achieve improved restoration performance with favorable efficiency.

---


### 198. [WinDOM: Self-Family Distillation for Small-Model GUI Grounding](https://arxiv.org/abs/2606.25964)

**<font color=#1a73e8>作者：</font>** Chengheng Li-Chen, Zhiqian Zhou, Hao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Small ($\sim$2B) GUI-grounding agents are attractive for on-device deployment, accessibility tooling, and low-cost iteration, but at this scale they face two open recipe questions: how to obtain bounding-box training data without expensive human annotation, and how to combine supervised fine-tuning with reinforcement learning. We address both, with the explicit goal of pushing small-model performance rather than scaling up. WinDOM is a $54{,}425$-record grounding corpus harvested by driving an open-source Windows 11 web reimplementation under headless Playwright, with bounding boxes read directly off the DOM and no OCR or human annotation. Self-Family Distillation (SFD) is a single rejection-sampling cold-start parameterised only by the teacher choice: either an EMA of the student (no external model) or a frozen larger same-family teacher. We then treat the saturation depth of the SFD cold-start as an explicit GRPO hyperparameter. On a Qwen3.5-2B student, the under-saturated cold-start is a better GRPO initialiser than the converged one: SFD-4B with Early-init RL gains $+5.4$ OOD-mean ($+3.5$ ScreenSpot-Pro, $+7.0$ OSWorld-G, $+5.8$ ScreenSpot-V2) over the base. The same-size EMA mode lands within roughly one OOD-mean point of the cross-size $4$B variant ($65.2$ vs $66.3$) without an external teacher.

---


### 199. [Improving Neural Network Training by Decoupling the Magnitude and Direction of Weight Vectors](https://arxiv.org/abs/2606.25971)

**<font color=#1a73e8>作者：</font>** Alexander Hägele, Alejandro Hernández-Cano, Atli Kosson 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern neural network training relies on optimizers such as Adam and Muon which act on each weight matrix as a single object. Yet every weight matrix carries two distinct quantities -- a \emph{magnitude} and a \emph{direction} -- and all optimizers stepping in the matrix as a whole couple their dynamics: the directional change from an update depends on the current magnitude, while the magnitude drifts as a byproduct of learning the direction, so neither is governed directly by the learning rate. Typical training therefore leans on surrounding recipes such as weight decay and warmup to keep learning stable at scale, though these regulate the coupling only indirectly; other recent methods instead constrain the weight to a fixed-norm sphere, but add no learnable magnitude, leaving scale control to normalization layers alone. We propose \emph{Magnitude--Direction (MD) Decoupling}, an optimizer modification that factorizes each weight into a fixed-norm direction on a hypersphere and learnable per-row and per-column magnitude gains, updated at separate learning rates, all while the model still sees a single fused weight tensor. The method is agnostic to the base optimizer and removes the need for weight decay and warmup. Across both Adam and Muon, MD Decoupling improves on well-tuned baselines, transfers the optimal LR across model width without retuning, and continues to help at scale on large Mixture-of-Experts (MoE) models. Treating magnitude and direction as separately controlled quantities thus yields more predictable training dynamics and a simple, broadly applicable improvement to modern optimizers.

---


### 200. [Tensorion: A Tensor-Aware Generalization of the Muon Optimizer](https://arxiv.org/abs/2606.25975)

**<font color=#1a73e8>作者：</font>** Vladimir Bogachev, Vladimir Aletov, Alexander Molozhavenko 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Common first-order optimizers, such as Adam, implicitly treat each parameter block as an unstructured vector, which disregards the multilinear weight structure present in many modern machine learning models. Recent work has shown that exploiting matrix structure can improve optimization dynamics. A notable example is Muon, which performs steepest descent under the spectral norm constraint. We take the next step and introduce Tensorion, a tensor-aware optimizer that extends Muon's constrained optimization perspective from matrices to higher-order tensors. Tensorion is built around a linear minimization oracle (LMO) over a tensor norm ball. The norm is carefully chosen to balance two objectives: tightly bounding the tensor spectral norm, while still keeping the LMO tractable. This LMO becomes computable because it reduces to operations on adaptively selected unfolding matrices. Notably, when restricted to order-2 tensors (i.e., matrices), Tensorion recovers Muon exactly. Experiments on tensor-based computer vision problems suggest that Tensorion can offer improved convergence behavior and more stable gradient updates compared with Adam-based and existing tensor-aware baselines in the evaluated settings.

---


> [!TIP]
> 当前位于：**151-200**（第 4/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-222](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
