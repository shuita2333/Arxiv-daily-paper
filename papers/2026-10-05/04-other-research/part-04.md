# 📦 其他研究 | 2026年10月05日

> 本类共 **385** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

---

### 151. [Generalist Representation, Specialist Detection: TS-Router for Time-Series Anomaly Detection](https://arxiv.org/abs/2610.00978)

**<font color=#1a73e8>作者：</font>** Tian Lan, Yifei Gao, Yimeng Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series anomaly detection (TSAD) is difficult to generalize across datasets because heterogeneous temporal dynamics imply different notions of normality and favor different detection criteria. While time-series foundation models provide transferable representations, coupling them with a fixed anomaly-scoring mechanism can overlook this variation. This motivates a different perspective on foundation-model-based TSAD: using foundation models to coordinate specialized anomaly criteria rather than directly imposing a universal one. Based on this view, we propose \textbf{TS-Router}, a generalist-representation, specialist-detection framework that estimates the relative competence of heterogeneous anomaly detectors from pretrained temporal representations and selects suitable specialists for each target series. To avoid relying on specialist-performance labels from real tasks, we derive soft competence supervision from specialists' relative performance on labeled simulated tasks. At deployment, routing requires no target anomaly labels, and only the selected specialists are fitted unsupervisedly on the target series. We bound Top-\(k\) set-competence regret under representation coverage and conditional competence stability. Across 16 real-world benchmarks and four complementary evaluation metrics, TS-Router achieves the best overall average rank. Controlled ablations with multiple frozen TSFM encoders further support the use of pretrained representations for competence estimation and adaptive specialist selection. The code is available at this https URL.

---


### 152. [Can AI Scientists Coordinate at Runtime?](https://arxiv.org/abs/2610.00980)

**<font color=#1a73e8>作者：</font>** Zijian Liu, Yangzhixin Luo, Junyu Lu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent AI scientists have shown improving performance across a diverse range of tasks. Yet a common approach is design-time agentic orchestration, which typically relies on fixed workflows. In contrast, human scientists coordinate and adjust their division of labor at runtime. We therefore ask: can AI scientists also coordinate at runtime? To this end, we introduce Runtime Agent Coordination (RAC), which selects agents from existing AI-scientist hosts during execution, assigns scoped work contracts, and provides artifact-grounded verification. Verification informs subsequent agents without blocking transitions or discarding artifacts. We conduct a single-seed exploratory evaluation across Agent Laboratory, EvoScientist, and ARK on ResearchClawBench, preserving host models, tools, and permissions under host-calibrated budgets. Four cumulative conditions separate native execution, runtime communication, runtime selection, and the combined addition of contracts and verification. Runtime selection yields the highest observed mean score for each host; adding contracts and verification reduces these means, with host-dependent outcomes relative to native execution. These results motivate runtime coordination while exposing the limits of additional coordination mechanisms under constrained budgets. Code is available at this https URL.

---


### 153. [Neural scaling laws and evolution of learnable activation functions of Kolmogorov-Arnold networks](https://arxiv.org/abs/2610.00985)

**<font color=#1a73e8>作者：</font>** Tilen Cadez, Sanghoon Lee, Kyoung-Min Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Kolmogorov-Arnold Networks (KANs) represent a compelling alternative to traditional Multi-Layer Perceptron (MLP)-based neural networks. By employing activation functions as learnable elements, KANs offer superior interpretability, making them suited for scientific domains. In this work, we investigate the neural scaling laws of KANs and the structural evolution of their learnable activation functions under dataset expansion. Specifically, we evaluate the scaling behavior of three KAN variants---BSRBF-KAN, Gottlieb-KAN, and Faster-KAN---across standard image classification benchmarks (MNIST and Fashion-MNIST) and a specialized scientific regression task (magnetic parameter estimation from domain images of moiré magnetic textures). Our results demonstrate that the test loss ${\cal L}$ exhibits a broken neural scaling law (BNSL) behavior as a function of the dataset size $N_D$. After passing through a random-guess regime, the loss follows architecture- and task-dependent scaling behavior. The loss crosses from a faster- to a slower-scaling branch, ${\cal L}\propto N_D^{-\alpha}$ and ${\cal L}\propto N_D^{-\beta}$ with $\alpha>\beta$ for image classification tasks. The exponents $\alpha$ and $\beta$ depend strongly on both the specific network architecture and the dataset-size regime, ranging from 0.4 to 1.5 and from 0.06 to 0.6, respectively. For the magnetic parameter-regression task, the loss follows a single scaling law with its exponent ranging from 1.28 to 2.59. Additionally, we provide a structural analysis of how activation functions refine their complexity as data volume increases, finding that dataset expansion drives a transition from simple linear-like approximations toward stable, interpretable symbolic forms. These findings provide a quantitative roadmap for the efficient application of KANs while managing the trade-off between model expressivity and computational overhead.

---


### 154. [Reliability-aware short-term roll prediction for unmanned surface vehicles via multi-task learning and adaptive centralization](https://arxiv.org/abs/2610.00996)

**<font color=#1a73e8>作者：</font>** Kaizhen Li, Xi Zhou, Zihao Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reliable roll prediction of unmanned surface vehicles (USVs) is essential for ensuring navi?gational safety and enhancing autonomous decision-making. While existing studies primarily focus on improving prediction accuracy, the quantification of prediction reliability remains insufficiently addressed. To bridge this gap, this paper proposes a reliability-aware prediction paradigm that integrates confidence assessment into the predictive pipeline. The architecture utilizes a multi-task learning structure where a shared feature extraction backbone feeds into dual heads: a regression head for precise roll prediction and a quantification head for confidence scoring. This configuration provides accurate prediction and corresponding confidence for risk?sensitive downstream tasks. In addition, an adaptive centralization strategy tailored for short?term real-time roll prediction is introduced to improve model generalization under varying operational conditions. Experiments conducted on a real-sea dataset demonstrate that the proposed method effectively quantifies the reliability of prediction results and maintains superior generalization under varying conditions, offering significant potential for practical engineering applications.

---


### 155. [Calibration-risk routing for controlled world-model adaptation](https://arxiv.org/abs/2610.01001)

**<font color=#1a73e8>作者：</font>** Yifan Zhang, Liang Zheng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement learning (MBRL) can exploit simulated experience, but a simulator-to-target shift creates a model-selection problem: correcting the simulator and fitting the target directly can each fail under limited target data. We introduce the Model-Corrected World Model (MC-WM), which separates initial target data into disjoint fit, selection, and calibration partitions and deploys the family with lower standardized calibration risk. A learned confidence signal and deterministic validity predicates weight one-step imagined policy updates without rewriting physical rewards. We evaluate 540 unique reported run cells across three controlled Multi-Joint dynamics with Contact (MuJoCo) shifts; one exact-routing cell was repeated after a pre-deployment artifact gate, giving 541 completed executions.

---


### 156. [What Can Analogy Tell Us About Artificial Consciousness?](https://arxiv.org/abs/2610.01002)

**<font color=#1a73e8>作者：</font>** Keith J. Holyoak, Martin M. Monti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Who or what is conscious? Because subjective experience is directly accessible only in the first person, judgments about consciousness in other entities depend partly on analogy. Historically, such inferences have focused on nonhuman animals, but advances in artificial intelligence have raised the possibility of conscious AI. Here we develop a causal framework for evaluating such evidential analogies. The key distinction is between similarities in factors plausibly involved in generating consciousness and similarities in downstream behavioural or cognitive effects. Our framework weights source-target similarity by causal relevance while allowing for unknown causes, disabling differences and alternative routes to consciousness. Applied to biological systems, it explains why analogical support generally weakens with increasing causal distance from humans. Applied to contemporary AI, it suggests that behavioural similarity provides only limited evidence for consciousness because relevant causal correspondences remain poorly established. The framework also clarifies what evidence would strengthen claims of artificial consciousness.

---


### 157. [Beyond Answer Confidence: A Controlled Audit of Self-Knowledge in a Black-Box Decision Model](https://arxiv.org/abs/2610.01006)

**<font color=#1a73e8>作者：</font>** Sharath M Shankaranarayana, Davor Runje, Jan Jannink  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Decision models return probabilities intended for routing, abstention and automated action. Calibration makes those probabilities useful on average, but does not establish whether low confidence reflects chance or missing knowledge, nor whether confidence falls when a model moves beyond what it knows. We audit this distinction in Jev, a decision model, with over 15 public datasets and 6 generated task families, with paired interventions that vary the information supplied for a fixed item. Jev's confidence is calibrated on familiar closed-choice tasks but fails as an indicator of missing knowledge: with no answer-relevant information it assigns up to 0.80 to a salient option, and on news beyond an observed knowledge boundary it exceeds accuracy by 0.21--0.33, a gap that recalibration on earlier months does not close. Targeted yes/no questions give sharper readouts of the case: whether an outcome is settled (AUROC 1.00) and whether the evidence suffices (0.95, against 0.85 for confidence on the same items). Asking whether Jev knows the answer appears to flag fabricated entities and post-boundary news (0.91), but with realistic names or with dates removed it shows no advantage over answer uncertainty. Black-box knowledge audits therefore need explicit controls for surface cues. Code: this https URL.

---


### 158. [Helol Tunnel: Covert Channel Exploitation of TLS Extensibility & Privacy Features](https://arxiv.org/abs/2610.01009)

**<font color=#1a73e8>作者：</font>** Reza Soosahabi, Rakesh Seal  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Covert channels exploiting network protocols for data exfiltration and command-and-control (C2) are integral parts of modern cyberattacks. In search of a significant covert channel within the fabric of the Internet, we targeted the combinatorial properties of the Client Hello (CHLO) packets in the ubiquitous Transport Layer Security (TLS) protocol. The proposed Helol tunnel is a novel covert approach to embedding information in TLS Client Hello packets, which involves the strategic rearrangement of their cryptographic information elements. To sustain TLS protocol extensibility, the recent anti-ossification TLS compliance measures encourage the interactive middleboxes and next-generation firewalls (NGFWs) to preserve the parameter configuration in the Client Hello packets. Furthermore, to improve user privacy, popular Internet applications are varying their TLS CHLO parameter configurations to resist TLS fingerprinting by third-party network entities. We demonstrate the strength of the Helol tunnel to exploit these recent developments to evade NGFWs with interactive proxy and comprehensive threat protection. We also numerically show the efficacy of Helol tunneling over state-of-the-art covert channels that exploit TLS through the use of real traffic captures and public TLS fingerprinting data.

---


### 159. [Watch Your Speech: Text-aware Video-to-Speech Synthesis with Textual Conditioning](https://arxiv.org/abs/2610.01012)

**<font color=#1a73e8>作者：</font>** Gunwoo Lee, Yoori Oh, Yoseob Han  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video-to-speech synthesis aims to generate natural-sounding speech from silent talking-face videos while ensuring phonetic accuracy. A fundamental challenge in this task is the inherent one-to-many mapping problem, where visual dynamics often lack sufficient information to uniquely determine the corresponding utterance. To address this, we propose Watch Your Speech (WYS), a video-to-speech synthesis framework that incorporates textual conditioning as an explicit linguistic cue to mitigate visual ambiguity. Our framework features an attention-based embedding fusion module that synergistically integrates textual context with video sequences, coupled with a conditional flow matching objective for high-fidelity speech generation. Extensive experiments on the LRS2 and LRS3 datasets demonstrate that WYS achieves superior performance, establishing new state-of-the-art results in audio-visual synchronization (LSE-C/D) while maintaining highly competitive textual accuracy (WER). Subjective evaluations further confirm that our model generates speech with near-human naturalness, validating the effectiveness of textual conditioning in content-controlled video-to-speech synthesis. Project page: this https URL

---


### 160. [VASC: Value-Aware Sparse Attention with Cross-Layer Memory for Efficient 3D Reconstruction](https://arxiv.org/abs/2610.01013)

**<font color=#1a73e8>作者：</font>** Junyi Wu, Fanqing Kong, Leyang Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Feed-forward 3D vision models such as VGGT have achieved remarkable progress, unifying camera estimation and dense scene reconstruction in a single pass. However, their quadratic global attention makes long image sequences expensive, while existing sparse methods may favor highly attended yet value-redundant regions. To address these limitations, we introduce VASC, a training-free sparse attention method combining value-aware block selection and execution-aware cross-layer memory. Our value-aware block selection integrates pooled query--key relevance with neighboring value contrast, reducing redundancy while preserving query-relevant and distinctive content. Cross-layer memory tracks unserved demand across layers and updates this state according to actual execution, enabling previously underserved blocks to compete under a fixed computation budget. Experiments on 7Scenes and NeuralRGB-D with VGGT and $\pi^3$ demonstrate improved pose estimation and reconstruction quality compared with FasterVGGT, together with up to $2.29\times$ faster inference than dense VGGT. Code is available at this https URL.

---


### 161. [FutureWorlds: Learning Robotic World Models from Alternative Futures](https://arxiv.org/abs/2610.01019)

**<font color=#1a73e8>作者：</font>** Hao Wu, Shengju Qian, Weiyan Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Robotic world models predict action-conditioned future scenes, providing a foundation for understanding action outcomes. However, turning alternative predictions into useful learning signals remains challenging: similar candidates limit informative quality comparisons, while diverging trajectories require persistent maintenance of their individual histories. We introduce FutureWorlds, a framework that unifies candidate construction, history maintenance, and learning from relative quality. Built on a multimodal discrete autoregressive model, FutureWorlds uses diverse beam search during reinforcement learning to construct candidate futures that balance confidence and diversity. Candidate-specific bounded memory preserves scene states and ensures that generation and policy scoring use matching histories. We further propose MemSPO (Memory-Conditioned Search-Guided Policy Optimization), which converts video trajectory rewards into group-relative advantages to optimize the world model. On RT-1, BridgeV2, and RoboCasa, FutureWorlds reduces LPIPS for 32-frame predictions by 14.78%, 20.84%, and 9.12%, respectively, relative to the strongest baseline on each dataset. Under fixed evaluation configurations, only 200 MemSPO updates further improve generation quality and support continued prediction beyond the training horizon. Memory ablations, decoding sensitivity analysis, and optical-flow evaluation show that these gains extend beyond visual quality to more accurate motion prediction and more consistent object states. Project page and code: this https URL.

---


### 162. [Scaling Peer Assessments: An Integrity Report from a Large Engineering Internship](https://arxiv.org/abs/2610.01020)

**<font color=#1a73e8>作者：</font>** Jinal Gupta, Pavani Ayinampudi, Aditya B.M.V. 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Assessing learning in large classrooms presents a significant challenge for individual instructors, who may have limited capacity to evaluate the understanding, participation, and assessment behaviour of every student. Peer assessments have been a way of distributing this responsibility among learners, allowing them to evaluate and provide feedback to one another while reducing dependence on instructor-led assessments. Building on this approach, we implemented a peer validation model within a large, multi-institutional internship programme in which students who demonstrated sufficient understanding were authorised to assess and validate their peers through short oral discussions. The assessment process began with the instructor validating a small group of students, who were then authorised to validate their peers, allowing the process to gradually expand across the cohort and operate at scale. This study examines how participants experienced the model and the extent to which assessment integrity was maintained, using an end-of-programme survey of 238 consenting respondents. Most participants regarded the activity as worthwhile, with 79.8% reporting that they solved problems they could not previously solve. However, 29.0% acknowledged at least one instance of reduced effort, a lowered validation standard, or reciprocal validation, while 88.7% believed that at least a little validation had occurred without proper examination. When asked how the process could be strengthened, participants selected post-validation discussion of solutions approximately twice as often as closer auditing or mentor-led validation. These findings provide descriptive evidence of both the potential and the integrity challenges of using peer validation as a scalable assessment approach in large learning environments.

---


### 163. [Optimal Transport Reweighting for Robust Learning under Spurious Correlations and Label Noise](https://arxiv.org/abs/2610.01028)

**<font color=#1a73e8>作者：</font>** Sung Ho Jo, Seonghwi Kim, Wonsang Yun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning models often suffer performance degradation under subpopulation shift, particularly when spurious correlations cause models to rely on shortcut features that fail to generalize across subgroups. A recent line of work mitigates this issue by using loss-based signals to identify informative samples, but these signals can become severely distorted under label noise: mislabeled samples may also incur large losses and contaminate subsequent reweighting or retraining. Despite its practical importance, this intersection remains largely underexplored. We propose POTER, a reweighting framework based on optimal transport that derives sample importance from the transport geometry between the training distribution and a reference distribution constructed from limited validation group annotations. By measuring alignment at the individual-sample level rather than relying on loss, POTER downweights mislabeled or strongly bias-aligned samples while assigning higher importance to samples better aligned with the reference distribution. In addition, POTER requires only a single ERM training stage, moving beyond the retraining paradigm common in recent work. Across standard benchmarks and noisy-label settings, POTER achieves state-of-the-art worst-group accuracy, including cases where label corruption is concentrated within minority subgroups.

---


### 164. [Bootstrapping Video Interaction Generation with Synthetic State Transitions](https://arxiv.org/abs/2610.01039)

**<font color=#1a73e8>作者：</font>** Jiho Jang, Jinyoung Kim, Nojun Kwak 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While recent video generative models can synthesize high-fidelity videos, they struggle to portray plausible physical interactions and the resulting state transitions, a critical bottleneck for applications in robotics and VR/AR. To address this, we introduce a framework to generate a scalable synthetic dataset of controllable interactions. Our pipeline leverages a structured taxonomy and state-of-the-art image editing models to create explicit `start' and `end' state images, which serve as visual anchors for the interaction. To generate a seamless video utilizing these anchors, we propose State-Guided Sampling (SGS), a novel sampling technique that mitigates artifacts common in naive conditional generation. Furthermore, we develop and validate a new automated evaluation system that aligns with human judgments to ensure data quality. Experiments show that fine-tuning a base model on our dataset significantly enhances its ability to generate plausible interactions.

---


### 165. [Empty Commitments: When Agents Promise What Their Runtime Cannot Deliver](https://arxiv.org/abs/2610.01045)

**<font color=#1a73e8>作者：</font>** Jiaqi Tang, Lan Wei, Bingyu Shen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A chatbot that says "I will remind you tomorrow" will not run again until the user writes. We call such a promise an empty commitment: a promise of an action after the current turn that nothing in the agent's tools or runtime can carry out. Unlike a broken promise, its emptiness follows from the agent's configuration alone; no later trajectory is needed. We define empty commitments on top of commitment semantics, with three failure types, an anchoring condition for promises that a tool could make real, and a response-level outcome taxonomy. We then describe a measurement protocol: follow-up requests run in five setups that add one persistence affordance at a time, with the environment either left implicit or stated.

---


### 166. [Towards Subject Consistency over Dynamic Subject Sets in Video Generation](https://arxiv.org/abs/2610.01052)

**<font color=#1a73e8>作者：</font>** Tongcheng Zhang, Jun Zhu, Jianfei Chen  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We argue that as video generation extends to longer durations, subject consistency should be evaluated over \textit{dynamic subject sets}. We therefore introduce \textbf{DynSC-Eval}, an evaluation framework that dynamically tracks eligible subjects throughout their visible lifespans and measures local continuity and global identity preservation using six complementary object-level metrics, with explicit detection of inconsistency events. To validate its effectiveness, we design synthetic experiments that actively inject inconsistency events, demonstrating both the sensitivity of DynSC-Eval and the limitations of existing metrics. Evaluations of diverse models on 5s, 15s, and 60s video generation further reveal substantial subject consistency differences that are obscured by conventional metrics. Beyond evaluation, we construct rewards from DynSC-Eval and apply DiffusionNFT post-training in an autonomous-driving testbed. On 5s generation, our approach reduces the six inconsistency metrics by an average of 13.82\% for Wan-2.1-1.3B and 5.66\% for SANA-2B, with improvements also observed on the I2V model ReSim. Qualitative comparisons further demonstrate the effectiveness of our method. We then extend generation to 10s and 30s through curriculum learning and show that consistency optimization remains effective while largely preserving other capabilities.

---


### 167. [HierGF: Hierarchical Gaussian Fields via Geometry-perception Message Passing for Sparse-view 3D Reconstruction](https://arxiv.org/abs/2610.01056)

**<font color=#1a73e8>作者：</font>** Bi'an Du, Zhimin Zhang, Daizong Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Sparse view 3D reconstruction is an important and common scenario in multimedia applications, such as augmented reality/virtual reality (AR/VR) content creation, cultural heritage digitization, and certain robotic applications, where only a limited number of randomly captured views may be available. However, sparse views contain only limited 3D information, posing two major challenges:1) too few images are available for matching, making it difficult to build multi-view consistency; 2) insufficient view coverage leads to a lack of information in under-sampled regions, resulting in missing parts of object structure. Existing methods mostly still rely on limited reprojection errors and regularization terms, which are prone to overfitting to a single view and inconsistent appearances across views. In geometrically under-sampled regions, they often rely on heuristic density control, lacking reliable guidance and often resulting in blurring and structural this http URL address these issues, this paper proposes Hierarchical Gaussian Fields (HierGF), which revisits sparse-view reconstruction from a hierarchical geometry-perception perspective and converts limited observations into reliable self-generated supervision beyond fixed priors and heuristic density control. In particular, we transform coarse 3D geometric information and additional 2D generative priors into structured pseudo-supervision through a two-stage geometry-perception backbone network, thereby enhancing multi-view consistency with very few input views. In addition, we introduce a learnable confidence network to guide gradients toward cross-view consistent content, and a geometrically consistent densification module to improve the reconstruction of multi-view alignment and under-sampled regions.

---


### 168. [JoinGR: Learning to Traverse Join Graphs for Table Retrieval](https://arxiv.org/abs/2610.01064)

**<font color=#1a73e8>作者：</font>** Sandipan De, Abhijit Chakraborty, Sambaran Bandyopadhyay 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieving the right tables is a prerequisite for Text-to-SQL over realistic databases. Dense table retrievers rank schema elements independently, but this ignores a key source of evidence: some required tables are not mentioned in the question and become identifiable only through their join relationships to already relevant tables. We introduce JOINGR, a join-aware table retrieval method that treats the database join graph as the retrieval space. Columns are represented as graph nodes, while intra-table and foreign-key relationships are represented as typed edges. Given a question, JOINGR selects semantically similar anchor tables, traverses join edges with a query-conditioned scorer, and aggregates the resulting edge deposits into table scores. The scorer is a lightweight MLP on top of frozen query, node, and edge embeddings, trained with a pairwise margin loss over gold tables. On BIRD and Spider datasets, JOINGR is competitive with the strongest retrieval baselines. On BEAVER, a challenging enterprise benchmark with multi-hop table requirements, JOINGR substantially improves recall over dense retrieval and re-ranking baselines. Cross-domain experiments show that the learned scorer transfers across benchmarks, indicating that the method captures reusable joingraph traversal behavior.

---


### 169. [Overcoming Kernel Redundancy for Scaling Logic Gate Networks](https://arxiv.org/abs/2610.01069)

**<font color=#1a73e8>作者：</font>** Sejin Park, Hongjae Lee, Changwoo Han 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Differentiable logic gate networks, which operate using only logic gates, have recently attracted attention as an efficient alternative to conventional neural networks. However, despite their efficiency, the scaling behavior of logic gate networks remains underexplored. By contrast, scaling model capacity is a central design principle in deep neural networks and typically leads to improved performance. This discrepancy raises a key question: Can similar scaling benefits also be achieved in logic gate networks? In this work, we focus on width as a primary scaling axis and conduct a systematic analysis of its behavior in logic gate networks. We observe that naive width scaling often introduces redundancy among logic kernels, limiting the effective use of additional kernels and leading to performance saturation. To address this limitation, we propose a dynamic logic kernel framework that reorganizes kernel utilization by promoting specialization across kernel groups. This enables the network to better utilize increased width via input-dependent kernel routing, while ensuring that both routing and computation are implemented entirely with gate-level Boolean operations at inference time. We further find that kernel redundancy is most pronounced at the first gate level, motivating an early-stage dynamic logic kernel strategy that concentrates adaptation at this level. Experimental results demonstrate that our approach improves kernel utilization and increases kernel diversity, leading to higher accuracy with improved parameter efficiency.

---


### 170. [Precision over Scale: A Polish-Silesian Benchmark and a Translation System Outperforming Open-Source and Commercial Models](https://arxiv.org/abs/2610.01082)

**<font color=#1a73e8>作者：</font>** Grzegorz Kulik, Mikołaj Pokrywka, Adam Jatowt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialectal machine translation remains challenging due to limited data and strong linguistic variation not captured by standard benchmarks, which often assume standardized and well-edited text. We study Polish-Silesian MT using neural and rule-based systems, evaluating on SiLTT - a new Pol-Szl testset, alongside established BOUQuET and FLORES benchmarks. Results show our rule-based system is consistently strongest on SiLTT and BOUQuET datasets and that TranslateGemma fine-tuned on a curated dataset improves over strong neural baselines but does not surpass the rule-based system in dialectal settings. We release SiLTT and our best neural model to support further research.

---


### 171. [Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation](https://arxiv.org/abs/2610.01092)

**<font color=#1a73e8>作者：</font>** Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video generation models are increasingly being explored as world simulators for embodied planning and learning. To do so effectively, these models must not only generate visually appealing frames, but also predict how environments dynamically evolve when executing goal-directed actions. While evaluating these capabilities is crucial, existing benchmarks focus mainly on single short actions or step-by-step instructions. This leaves multi-step physical reasoning underexplored, especially in egocentric video generation that requires planning to simulate proper execution to accomplish high-level goals by carrying out multiple real-world manipulations. We introduce Ego2Act, a goal-directed benchmark featuring 2,640 videos from 110 real-world tasks across day-to-day settings, varying object clutter and multi-step complexity. Given an initial scene image and a high-level goal, Ego2Act evaluates whether video generation models can produce realistic egocentric videos of a hand manipulating objects to carry out the task. To support scalable evaluation, we also introduce Ego2ActJudge, a reference-free evaluation pipeline that achieves better task completion and physics plausibility evaluation alignment with human consensus compared to relevant baselines. Our findings reveal that models' generated simulations often skip or partially execute steps, leaving later steps missing dependent states, which leads to unfulfilled goal. Furthermore, models consistently fail at fine-grained physical dynamics, particularly during complex object manipulation and persistent world modeling. We hope Ego2Act provides a rigorous testbed for advancing video models toward physically plausible, goal-directed simulation.

---


### 172. [Dataset Identity, Not Novelty: The Source of an Inflated OOD Detection Gain](https://arxiv.org/abs/2610.01096)

**<font color=#1a73e8>作者：</font>** Donghoon Lee, Shinjin Kang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A post-hoc out-of-distribution (OOD) detector reads the activations of a trained classifier and returns a score. It fits that score on in-distribution data, and the benchmarks that evaluate it supply a second piece of OOD data for the fitting itself. Some detectors tune a constant on it. Others fit a direction in feature space or train a flexible combiner and report the number that it reaches as the gain that is still available. Every such fit is validated on held-out samples of the same OOD dataset. That check rules out memorizing individual images. It says nothing about a fit that has instead learned which dataset it is looking at, and a direction that recognizes one OOD dataset rather than novelty passes it perfectly. The detector that a practitioner installs meets OOD data from a source that nobody fitted it on, so the difference decides what the reported number is worth. We measure it by holding out the whole OOD dataset rather than a sample of it, and we call that gap the inflation. We read it across a range of combiners on ImageNet and CIFAR-100 backbones. Most of the gain that the usual protocol reports turns out to be dataset identity rather than novelty. The size of the fit does not move what survives, so the effect is not ordinary overfitting. The share depends instead on whether the input exposes class identity, and two controls that vary that property alone separate the inflation on every backbone of both benchmarks. A closed form accounts for the effect and computes it from the fitting rows, so a practitioner can tell which fits will inflate without running the hold-out protocol. One of these fits survives, namely the single constant that the field already picks on a designated validation dataset. Anything above it reports a gain that the hold-out protocol does not return, and on one benchmark what survives falls while what is reported climbs.

---


### 173. [YouRA: A Persistent-State Architecture for Evidence-Traceable Autonomous Research Agents](https://arxiv.org/abs/2610.01097)

**<font color=#1a73e8>作者：</font>** Yoonkyu Woo, Woojin Lee, Jin-Xia Huang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> End-to-end research agents can now produce complete scientific papers, yet manuscript claims often diverge from executed experiments. This gap is structural: research state, failure histories, and claim-evidence alignment are not maintained as persistent, verifiable state across long-horizon pipelines. We present YouRA (Your Research Agent), an architecture for stateful, evidence-traceable autonomous research. YouRA preserves research state, execution evidence, and failure history across the research trajectory by integrating three components: a Verification State Architecture (VSA) that tracks hypotheses, gates, and evidence pointers; an Independent Controller that turns state and reflection records into lifecycle, recovery, and debate/review control while separating control from execution; and Stateful Reflection that logs failures as structured lessons and routes recovery through bounded repair, redesign, or reset. On MLR-Bench's predefined ten-task end-to-end subset, YouRA improves over both MLR-Agent and AI Scientist V2 on scalar Overall across all three matched backbones. An automated diagnostic using MLR-Bench's hallucination taxonomy reports intersection/union counts for four fact-based failure types, and data-provenance diagnostic shows more real-data-based outputs. Ablating each of the four components (the VSA, the Independent Controller, MCP tool access, and reflection-guided recovery) supports their separable contributions. Removing either core-state component drops YouRA below the full system. Code: this https URL.

---


### 174. [MVDG: Efficient Multi-view 3D Disambiguation on Unconstrained Real-World Images](https://arxiv.org/abs/2610.01098)

**<font color=#1a73e8>作者：</font>** Hanyuan Xiao, Gonglin Chen, Haolin Xiong 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Illusory matches between distinct yet visually similar 3D surfaces--doppelgangers--remain a fundamental obstacle for large-scale, in-the-wild 3D reconstruction and visual localization. Prior work mitigates this issue with pairwise classifiers, but this design limits multi-view contextual reasoning and incurs O(n^2) inference complexity for downstream structure-from-motion (SfM). We present MVDG, a scalable multi-view disambiguation framework built on the 3D foundation model VGGT, which jointly reasons over an arbitrary number of multiview images. By incorporating 3D-aware multi-view features, our method reduces dependence on pairwise comparisons by encoding and decoding views in a single pass. We further observe that direct multi-view fine-tuning of VGGT can be unstable under noisy supervision; motivated by label ambiguity in Doppelgangers, we construct a pseudo-pairwise training set from AerialMegaDepth and show that fine-tuning on sampled subsets yields stable optimization and strong generalization to held-out scenes. Finally, because full SfM evaluation (even with faster pipelines such as GLOMAP) remains expensive, we process a pseudo-pairwise dataset for efficient validation; we derive a predictive relationship between regular SfM metrics and the classification accuracy on this pseudo-pairwise test. Experiments show that our method achieves comparable pairwise accuracy while improving both SfM accuracy and inference speed over baselines.

---


### 175. [Affine-Aligned Atlas for Canonical Gaussian Construction in Video Representation](https://arxiv.org/abs/2610.01114)

**<font color=#1a73e8>作者：</font>** Masaya Takabe, Hiroshi Watanabe, Sujun Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Gaussian splatting has recently emerged as an efficient representation for images and videos due to its explicit structure and fast rendering capability. Existing Gaussian-based video representations often decompose a video into canonical Gaussians and temporal deformation. However, when a video contains large global motion such as camera movement, the canonical representation may become misaligned with individual frames, increasing the burden on the temporal deformation model. In this paper, we propose an affine-atlas canonical Gaussian representation, which constructs canonical Gaussians in a larger affine-aligned atlas space. Frame-wise affine transforms absorb global motion before canonical Gaussian construction, reducing the gap between the canonical representation and target frames. Since the proposed method only modifies the canonical construction stage, it can be integrated into existing canonical-Gaussian-based methods with negligible additional parameter cost. Experiments show that our method improves reconstruction quality especially for sequences with large camera motion.

---


### 176. [Latent Information Sharing for Accelerating Federated Learning](https://arxiv.org/abs/2610.01126)

**<font color=#1a73e8>作者：</font>** Seungjun Lee, Ensieh Khazaei, Dimitrios Hatzinakos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning (FL) is a communication-efficient distributed learning paradigm. However, client drift remains one of the most critical challenges, hindering the efficient training of a global model. In this study, we propose a novel latent information sharing scheme that directly mitigates data heterogeneity across clients. Our theoretical and empirical results show that sharing a small amount of hidden-layer activations significantly improves training efficiency while preserving convergence guarantees and data privacy. Furthermore, we compare our method with existing FL approaches designed to address client drift, including FedProx, SCAFFOLD, FedPVR, FedProto, and SplitFed, and demonstrate superior model accuracy under a fixed round budget without incurring excessive communication overhead. Overall, this work presents a promising new knowledge aggregation scheme and provides a comprehensive analysis of the impact of activation sharing on federated optimization.

---


### 177. [Open Vocabulary Word Recognition From Transcribed Bangla Texts](https://arxiv.org/abs/2610.01134)

**<font color=#1a73e8>作者：</font>** Faias Satter, Sk. Md. Masudul Ahsan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An optical character recognition (OCR) can scan a paper and extract text using technology, making people's jobs easier. While various OCR systems are available in the software industry, finding a reliable equivalent solution for Bangla takes much work. When it comes to handwritten texts, the situation is much more unusual. Recognizing words from word images is the most critical stage in any OCR process. It is the second stage after segmenting words from text pictures. If this stage fails, the overall performance of the OCR will be poor, regardless of how well the other phases perform. This study aims to recognize words using deep learning in a handwritten Bangla word image. Three object detection models, SSD with MobileNetV2, Faster R-CNN with InceptionResNetV2, and an ensemble model of these two, have been used to train and test handwritten word images. A modified Non-Maximum Suppression has been introduced to enhance the effectiveness of the models' results. A customized dataset of 9841 handwritten Bangla word images has been compiled, featuring diverse handwriting styles from various individuals. All three models' performances have been checked against the test dataset, and the ensemble model has been the most impressive, with an F1-score of 92.61%. Also, at the word level, the ensemble model correctly recognizes 96.12% of the words to some extent. The system can be further improved by introducing a post-processing phase to correct errors generated by the system.

---


### 178. [The RSNA Intracranial Aneurysm (RSNA-ICA) Dataset](https://arxiv.org/abs/2610.01135)

**<font color=#1a73e8>作者：</font>** Maria Correia de Verdier, Rachit Saluja, Jason Sho 等 40 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Intracranial aneurysm rupture is associated with substantial morbidity and mortality, yet aneurysm detection remains challenging, particularly for small lesions and on routine non-angiographic imaging examinations. To support the development and evaluation of artificial intelligence (AI) algorithms for intracranial aneurysm detection and localization, the Radiological Society of North America (RSNA), in collaboration with the American Society of Neuroradiology (ASNR), the Society of Neurointerventional Surgery (SNIS), and the European Society of Neuroradiology (ESNR), curated the RSNA Intracranial Aneurysm (RSNA-ICA) Dataset. Developed for the 2025 RSNA Intracranial Aneurysm Detection Challenge, RSNA-ICA is a large, publicly available, expert-annotated dataset comprising 7202 CTA, MRA, and MRI series from 4278 adult patients collected across 21 institutions in 12 countries spanning five continents. The dataset includes 2566 CTA, 2166 MRA, and 2470 MRI series from patients with and without intracranial saccular aneurysms, providing substantial geographic and imaging diversity. Expert annotations indicate both aneurysm presence and location, and 178 series additionally include three-dimensional segmentations of challenge-defined vascular locations. RSNA-ICA was used to develop and evaluate algorithms in the 2025 RSNA Intracranial Aneurysm Detection Challenge. Of the 7202 image series, 5041 are publicly available through MIRA (this https URL), while the remainder were used for challenge public and private test sets. The dataset is freely available to the research community for noncommercial use and provides a comprehensive resource for advancing AI-based aneurysm detection across both angiographic and routine neuroimaging examinations.

---


### 179. [ReSolve: Reusing Candidate Reasoning through Selective Generative Moderation](https://arxiv.org/abs/2610.01140)

**<font color=#1a73e8>作者：</font>** Bangji Yang, Jiajun Fan, Hongba Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sampling multiple solutions spends computation on intermediate deductions and unfinished arguments as well as final answers. We introduce ReSolve, a training-free inference procedure that reuses this candidate reasoning through selective generative moderation. An answer-distribution controller invokes a model to examine existing derivations when candidates disagree or lack a parseable answer, then incorporates the generated solution into a bounded loop. Under Hybrid scoring on 130 competition-mathematics problems evaluated with two independently sampled candidate pools, ReSolve obtains 100 and 99 correct answers, compared with 91 and 92 for voting over the same four candidates, with no correct-to-incorrect changes relative to that vote in either pool. Eight-sample self-consistency obtains 94 and 96 correct answers while consuming substantially more tokens; ReSolve uses 46.3% and 47.2% fewer tokens in the two evaluations. A controlled ablation removes visible derivations while retaining answer keys, vote counts, and the per-state output-cap rule, reducing accuracy from 100 to 93 correct despite increasing computation. Selective and always-on Uniform moderation both solve 97 problems, while selectivity reduces moderation tokens by approximately 54% and total pipeline tokens by 6.2%. These results support candidate reasoning as reusable inference computation. They do not establish an accuracy advantage over additional sampling or a distinct benefit from specialized route instructions.

---


### 180. [OptimusMesh: Compact Autoregressive Mesh Generation from Point Clouds via Sparse Latent Pivots](https://arxiv.org/abs/2610.01148)

**<font color=#1a73e8>作者：</font>** Mazhar Iqbal, Naoya Chiba, Xuanmeng Sha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating compact and geometrically faithful 3D meshes directly from point clouds remains a fundamental challenge. Point clouds are unordered and sparse, whereas meshes exhibit irregular structure and varying topology. As a result, many existing approaches rely on implicit representations followed by surface extraction or reconstruction. Although effective, these pipelines can produce dense or over-smoothed meshes, often requiring computationally expensive post-processing and simplification. We present OptimusMesh, a framework for direct compact triangle mesh generation from point clouds using sparse latent pivot conditioning. Our key idea is to compress $2{,}048$ oriented input points into only $16$ sparse latent pivots, reducing the geometric conditioning set by $128\times$. These pivots provide a compact structural representation shared across a two-stage autoregressive framework that first generates mesh vertices and then predicts triangular faces conditioned on the generated vertices and the same pivots. Compared with the evaluated recent point-cloud-conditioned autoregressive methods, which use $257$ decoder-conditioning tokens, OptimusMesh uses only $16$, yielding a $16.1\times$ shorter conditioning sequence. Experiments show that OptimusMesh produces the most compact outputs among the compared recent autoregressive methods, using $25.7\%$--$94.1\%$ fewer faces while maintaining competitive geometric fidelity and distributional quality.

---


### 181. [BanglaDial-Abuse: A Corpus-Grounded Dataset for Regional Dialect Identification in Abusive Bangla Text](https://arxiv.org/abs/2610.01150)

**<font color=#1a73e8>作者：</font>** Hasin Almas Sifat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Regional linguistic variation remains an important challenge for Bangla natural language processing, particularly in informal and non-standard text. This paper introduces BanglaDial-Abuse, a balanced Bengali-script dataset developed for regional dialect identification in abusive and hostile Bangla text. The dataset contains 1,000 sentences distributed equally across four linguistic varieties: Standard Bangla, Chattagram, Sylhet, and Barishal, with 250 samples per class. The resource was constructed using a corpus-grounded synthetic procedure incorporating regional variation in pronouns, possessive forms, verb morphology, negation, interrogative structures, postpositions, vocabulary, and Bengali-script spelling conventions while preserving the underlying hostile or abusive meaning. Descriptive analysis shows broadly comparable sentence-length distributions but partially distinct lexical spaces across the four classes. Pairwise Jaccard vocabulary similarity ranges from 0.37 to 0.56. The primary task is four-class regional dialect identification rather than binary abusive-text detection. The dataset is publicly available through Zenodo under a Creative Commons Attribution 4.0 license. The current version is intended as a research and prototyping corpus rather than a native-speaker-validated gold-standard linguistic resource. Keywords: Bangla, Bengali, dialect identification, regional dialect, abusive language, low-resource NLP, Chattagram, Sylhet, Barishal, dataset

---


### 182. [PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models](https://arxiv.org/abs/2610.01162)

**<font color=#1a73e8>作者：</font>** Isaiah Milkey, Som Sagar, Aditya Taparia 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reliable video world models could provide scalable predictive environments for robot learning, planning, and evaluation. However, generated robot videos can violate physical principles and complete tasks through physically implausible behavior, limiting their reliability for robot learning and planning. Current video-generation benchmarks exclude physics that are inherently hidden by visuals (e.g., weight, viscosity, friction). Due to this, video models are evaluated on the fidelity of physics, not the underlying accuracy of physics. We introduce PhysicsLENS, a dataset and benchmark for evaluating plausibility of physical properties grounded in robotics. PhysicsLENS uses matched scenario pairs that hold the same conditioning frame and task, while varying underlying physics in the scene description. Scenarios are curated from public robot video sources and annotated across seven physical domains: collision, gravity, momentum, friction, deformation, fluid, and causality. We evaluate across four video generation models, producing over 400 human-annotated labels. Results show that plausible-looking videos often ignore the stated property (34 of 47), and that stating the property lowers plausibility only slightly and not significantly.

---


### 183. [CAGE-NAS: Certified Functional Descent for Efficient Model Growth](https://arxiv.org/abs/2610.01173)

**<font color=#1a73e8>作者：</font>** Santiago Florido Gomez, Stéphane Rivaud  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The progressive growth of neural networks requires deciding when the current representation remains sufficient for optimization and when it should be expanded. CAGE-NAS formulates this decision in function space through an admissibility criterion on approximations of the functional gradient. As long as a representation enables a certified Functional Gradient Descent step, the architecture remains fixed; when the criterion fails, a function-preserving expansion is applied and the resulting representation is evaluated again. As the main instance, we study the family induced by the tangent space, using a regularized projection of the functional gradient. In a controlled setting with exact certification, CAGE-NAS produces architectures positioned above the 99.8th performance percentile by held-out RMSE among all admissible alternatives within the same parameter budget, without enumerating them during the growth trajectory.

---


### 184. [Rethinking the Information Bottleneck: Structured Decomposition under Label-Induced Partitions](https://arxiv.org/abs/2610.01175)

**<font color=#1a73e8>作者：</font>** Jingyao Zhang, Yuxuan Li, Lu Han 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Standard information bottleneck (IB) regularization constrains representations via a single scalar I(Z;X), implicitlytreating all information as homogeneous. However, a single global compression control couples label-relevant structurewith residual within-condition variation, rather than regulating their allocation independently, allowing nuisanceinformation to persist in learned representations. For example, in medical imaging applications, residual variation oftenstems from acquisition conditions, background factors, or subject-specific appearance. This issue becomes particularlypronounced in data-limited settings, where models tend to overfit such variation, hindering generalization. While existingregularization methods can stabilize training, control capacity, or shape representation geometry, they do not explicitlyseparate nuisance-like variation from task-supporting structure. To address this limitation, we revisit IB from a structuredperspective based on a label-induced partition, where condition-level structure and within-condition information playdistinct roles. This leads to a dual-bottleneck formulation: a standard KL term controls global information capacity, while aconditional KL term targets within-condition information. We show that the conditional KL admits an exact decompositioninto a within-condition information term and a prior-mismatch term, explaining its alignment with the design this http URL a simplex-structured conditional prior, the method provides controllable latent geometry and integrates seamlesslyinto existing pipelines. Experiments on classification and segmentation show the clearest gains in low-data classificationand consistent improvements across dense prediction benchmarks.

---


### 185. [Fully Online Decentralized Learning in Stochastic Games with Unknown Independent Chains](https://arxiv.org/abs/2610.01181)

**<font color=#1a73e8>作者：</font>** S. Rasoul Etesami  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider stochastic games with independent controlled chains and unknown transition kernels, where players observe only their local states and realized payoffs. We develop a fully online, decentralized, and uncoordinated mirror-descent algorithm that operates in the dual space of occupancy measures for approximating stationary Nash equilibrium (NE) policies. The algorithm uses a single transition/reward sample at every primitive time step, relies only on local information, and requires neither coverage of the joint state space nor synchronized episodes. Under uniform-ergodicity and finite-coverage assumptions, we show that, with high probability, the time-averaged fixed-comparator regret decays at the canonical $O(T^{-1/2})$ rate, up to logarithmic factors and polynomial dependence on the game parameters. In particular, the complexity depends on the cover times of the individual local state spaces rather than the product state space, avoiding exponential dependence on the number of players and the sizes of the joint state and action spaces. The resulting finite-time regret bound further yields an approximate coarse-correlated-equilibrium guarantee, which is natural for arbitrary reward functions since computing a stationary $\epsilon$-NE is PPAD-hard in this setting. Under an additional global variational-stability condition, we show that the same fully online algorithm converges asymptotically in the last iterate to a stationary $\epsilon$-NE. Our results provide a fully online and scalable learning framework for stochastic games with unknown independent chains. The algorithm can also be viewed as a primal-dual framework for Markov games that exploits the independence and local structure of the players' controlled transition chains.

---


### 186. [ReCast: Contract-Preserving Protection for Fixed-Interface Multimodal Reasoning](https://arxiv.org/abs/2610.01184)

**<font color=#1a73e8>作者：</font>** Bingchen Pei, Lichong Chen, Bingxi Zhao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Remote multimodal models offer strong numerical reasoning capabilities over charts and speech, but sending private inputs risks exposing sensitive content. Text-only sanitization cannot directly satisfy fixed media interfaces, while identity anonymization leaves the underlying task content exposed. We introduce ReCast, an agentic plug-in framework that replaces source-specific content while preserving task-relevant relations and the required input modality. ReCast locally converts inputs into a shared textual evidence-query record, jointly rewrites entities and topics with a distilled 4B model, and substitutes values through a locally invertible, role-aware numerical map. A reconstruction agent generates and validates the required media from the protected record. The remote solver returns a program whose protected operands are restored locally before execution. On 4,000 held-out ChartQA and NMSQA examples, ReCast achieves 75.10% accuracy, retaining 92.43% of unprotected remote accuracy, while a model-based audit flags source-content leakage in 7.95% of solver-bound requests. It outperforms all evaluated local baselines, preserving the benefit of remote reasoning while reducing source-content exposure under existing media interfaces.

---


### 187. [When Does Exercise-Specific Joint Selection Help? An Audit of Evaluation and Control Design](https://arxiv.org/abs/2610.01188)

**<font color=#1a73e8>作者：</font>** Haotian Chen, Jingkun Yu, Yuning Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Exercise-specific joint selection can improve skeleton-based correctness classification, but what does that gain establish? We audit 1,057 repetitions from ten REHAB24-6 subjects, separating evaluation aggregation, subset structure, and temporal representation. The manual-subset kNN gain changes from 0.055 for pooled out-of-fold AUROC to 0.020 for equal-weight within-person AUROC; both paired intervals include zero. Among 1,000 dimension-matched random maps, 14 match or exceed the manual pooled result, versus 145 when bilateral structure and trunk inclusion are also matched. RBF-SVM retains a positive within-person gain, whereas logistic regression and a random-convolution comparator have negative point gains under that estimand. Sequence-order and paired-seed controls further qualify the interpretation. This exploratory audit shows why joint-selection claims require explicit estimands and structurally appropriate controls; it does not establish a new algorithm or clinical benefit.

---


### 188. [Color Independent Word Segmentation From Transcribed Bangla Passages](https://arxiv.org/abs/2610.01191)

**<font color=#1a73e8>作者：</font>** Faias Satter, Noor Masrur, Sk. Md. Masudul Ahsan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> An optical character recognition(OCR) system can scan paper and extract text, making people's jobs easier. While numerous OCR systems are accessible in the software sector, finding a dependable equivalent solution for Bangla is tough. When it comes to handwritten texts, the case is even more rare. The first fundamental step to any OCR is to segment words from text images. If this stage fails, the total OCR's performance will be poor no matter how promising the later stages perform. This research aims to segment words in a handwritten Bangla text image. This research can be implemented on any smartphone-captured image, irrespective of the color and type of paper and ink. Furthermore, as smartphone-captured images can create shadow interferences, the custom dataset built for this research is created in such a way that every possible obstacle that can be faced is included. For 7374 words, a total of 7278 bounding boxes are generated, which have recall of 90.60 %, precision of 91.80 %, and F1-score of 91.20 %. The system can be further improved with nested operations on bounding boxes containing several words or by adjusting the adaptive thresholding and dilation filter sizes to a more precise level.

---


### 189. [Counterfactual Generation via Flow Matching: Coupling-Sensitive End-to-End Rates](https://arxiv.org/abs/2610.01193)

**<font color=#1a73e8>作者：</font>** Yunrui Guan, Krishnakumar Balasubramanian, Shiva Prasad Kasiviswanathan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Counterfactual generation seeks to sample outcomes under a hypothetical intervention or decision using observational data collected under the factual assignment mechanism. We develop a flow-matching approach that combines a sample-split, doubly robust training objective with a learned coupling between observed source outcomes and target outcomes drawn from a fitted conditional outcome model. To enable finite-step generation, we leverage a score-corrected stochastic sampler based on a Gaussian-smoothed interpolation. Our main theoretical contribution is a coupling-sensitive KL bound for constant-step Euler discretization: the error is controlled by moments of the source--target displacement under the chosen coupling, rather than by global uniform regularity of the velocity field, and has near-linear dependence on the ambient dimension. We also establish finite-sample non-parametric guarantees for the learned velocity and score fields when both the conditional outcome model and the source-target coupling are estimated from data. These bounds separate approximation, coupling-replacement, nuisance-estimation, generalization, and Monte Carlo errors and, combined with the sampler analysis, yield an end-to-end guarantee for counterfactual generation. Experiments on synthetic and semi-synthetic image benchmarks support the coupling-dependent theory and show that, at finite discretization budgets, the stochastic sampler can outperform the corresponding deterministic ODE sampler.

---


### 190. [Low-Budget Active Learning through Entropic Optimal Transport](https://arxiv.org/abs/2610.01199)

**<font color=#1a73e8>作者：</font>** Rim Hajal, Mathieu Besançon, Jérôme Malick  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We consider low-budget active learning, which consists of selecting a limited number of points, the coreset, such that a model can be trained to high accuracy on the selection only. This problem is particularly relevant in contexts where labeling requires costly expert intervention, as in medical applications. We leverage features extracted from a pretrained self-supervised model to represent the data, and perform coreset selection directly in this feature space. In this paper, we use entropic optimal transport, specifically the Sinkhorn divergence, as the coreset selection criterion, which first allows us to get dimension-free sample complexity results, and second admits computationally efficient gradient evaluations. This opens the way to using gradient-based algorithms to rapidly compute solution candidates, further improved by a swap-based local search, with guarantees on the solution quality. Experiments on image benchmarks and medical datasets show that our method outperforms state-of-the-art heuristics in low-budget settings.

---


### 191. [iSEE: Object Permanence Through Self-Supervision](https://arxiv.org/abs/2610.01201)

**<font color=#1a73e8>作者：</font>** Pramish Paudel, Ajad Chhatkuli, Luc Van Gool 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object permanence, keeping track of an object's identity and position while it is occluded, is central to video representations that track, predict and plan. Trackers that achieve it learn from boxes, track identities and visibility labels. On the other hand, self-supervised object-centric methods discover objects without labels: through slot attention, it represents a video as slots that bind to objects and follow them across frames. However, these slots are lost under occlusion, making the desired permanence impossible. Reasoning permanence is a hard problem because it requires to detect when an object becomes occluded, re-identify when object reappears, and keep the object's hidden position continuous, using reapperance as the only learning cue. To address this, we propose iSEE, a novel framework that offers all three aforementioned requirements, without any labels whatsoever. We built iSEE using the following three proposed components: (i) Object evidence modelling: a slot's attention, compared with its own past, reveals when its object is hidden. (ii) Appearance-position separation: two slot streams let the appearance be held for re-identification while the position keeps changing. (iii) Permanence from reappearance: a walker follows the hidden object's position, trained only on where the object reappears. On LA-CATER static, iSEE returns a reappearing object to its own slot after 86% of occlusions, against 32% for SlotContrast, and localises it while hidden within 4.1 mAP of the label-trained SoTA RAM. The two streams also allow downstream planning, with the position stream as the action of a world model. Project page: this https URL

---


### 192. [Autoregressive Drillhole Modelling Under Distribution Shift](https://arxiv.org/abs/2610.01204)

**<font color=#1a73e8>作者：</font>** Yihao Ding, Daniel Yitian Su, Yiran Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Autoregressive modelling has achieved remarkable success in language and sequence tasks by learning to predict future states from previous observation. Mineral-exploration drillholes provide a natural but largely unexplored setting for this paradigm: as drilling proceeds, lithology is revealed sequentially from shallow to deep, making prediction of deeper strata inherently autoregressive. Existing drillhole modelling, however, is dominated by spatial interpolation and reconstruction, or largely rely on masked modelling, leaving strictly autoregressive prediction largely underexplored. We introduce DrillBench, a benchmark of 49,671 Western Australian drillholes for next-layer prediction and autoregressive stratigraphic generation across a graded transfer spectrum, from local prediction through spatial shift to cross geological province transfer. Benchmarking classical, geostatistical, and neural models reveals a clear \emph{transfer boundary}: spatial and geochemical conditioning provides large local gains but deteriorates sharply under stronger shift, whereas lithology-sequence autoregressive models transfer more robustly. Guided by this finding, we develop a backbone-agnostic recipe combining large-scale pretraining on historical drillholes with spatial retrieval of neighbouring lithology. Retrieval is most effective in weathered cover, when local spatial continuity remains informative, whereas pretraining contributes more strongly in bedrock and under broader geological shift. Together, they retain strong local performance while improving generalisation under spatial and cross-province shift, most markedly on the most distant splits. The benchmark and code are available at this https URL.

---


### 193. [Semantic RGB--Depth Based Surgical Skill Assessment in Microscopic Stereo Videos](https://arxiv.org/abs/2610.01205)

**<font color=#1a73e8>作者：</font>** Jecia Z. Y. Mao, Sue M. Cho, Francis X. Creighton 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objective assessment of microsurgical technical skill is essential for competency-based training and quality assurance, yet existing video-based approaches predominantly rely on RGB images and therefore overlook the 3D spatial relationships that characterize instrument-anatomy interactions. Although stereo operating microscopes provide complementary depth information, conventional stereo matching algorithms can produce sparse and unreliable depth estimates under high-magnification imaging conditions, limiting their use for automated skill assessment. This work presents a semantic RGB-Depth framework for surgical skill assessment from microscopic stereo videos. A regression-based depth fusion method combines sparse metric stereo depth with dense monocular depth estimates to generate a dense geometric representation of the surgical scene. This representation is integrated with semantically decomposed RGB streams corresponding to individual surgical instruments and surrounding anatomy. A hierarchical attention architecture jointly encodes these streams to capture discriminative patterns of instrument use and instrument-anatomy interaction across surgeons at different training levels. The framework was evaluated on 33 ex vivo transoral microlaryngeal procedures performed by six surgeons, comprising attending surgeons and surgical residents, using leave-one-surgeon-out cross-validation. The proposed semantic RGB-Depth model achieved an F1 score of 0.938 for skill-level classification, compared with 0.696 for semantic RGB and 0.929 for semantic depth. These results suggest that geometric information can improve automated surgical skill assessment from microscopic stereo videos. The learned spatial, temporal, and semantic attention patterns also support qualitative examination of the scene regions, video segments, and semantic streams emphasized by the model.

---


### 194. [Resolving Mixed Single-Photon LiDAR Returns for Foreground-View and Hidden Scene Reconstruction](https://arxiv.org/abs/2610.01206)

**<font color=#1a73e8>作者：</font>** Ziting Wen, Runrong Deng, Zili Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Partially transmissive screens and protective covers are common in robotic inspection, but they create mixed LiDAR returns from both the foreground material and the scene behind it. Conventional peak-based LiDAR usually discards weak hidden returns, while single-photon LiDAR records time-resolved histograms that preserve attenuated and overlapping echoes. However, existing transient reconstruction methods typically fit a single scene representation to the measured waveform. Under occlusion, weak or nearby foreground--hidden echoes can form a broad peak or subtle shoulder. Because such waveforms can also be explained by a displaced single surface or a thick density distribution, accurate transient fitting does not necessarily imply correct geometry. We propose a state-aware framework for foreground-view and hidden scene reconstruction from occluded single-photon histograms. For each ray, we estimate local echo evidence, identifying no reliable surface evidence, single-return evidence, or two returns. The inferred echo state routes supervision for a two-head neural field: all rays constrain waveform reconstruction, while reliable anchors provide geometry localization. We also introduce a real paired single-photon LiDAR occlusion dataset with occluded and clean captures at fixed poses. Experiments on a real dataset show improved hidden scene depth and point-cloud accuracy over baselines. Our results demonstrate single-photon layered reconstruction as a practical route for 3D perception through partially transmissive occluders.

---


### 195. [EgoFound3R: End-to-End Egocentric Hand Reconstruction in World Space with Point-Wise Interaction Attributes](https://arxiv.org/abs/2610.01210)

**<font color=#1a73e8>作者：</font>** Hongming Fu, Jingcheng Shi, Wenjia Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Egocentric video has become a primary source of supervision for embodied models, and its value rests on recovering hand motion in world coordinates, which camera motion and hand occlusion make difficult. Existing reconstruction pipelines typically separate hand and scene estimation, leave interaction attributes to separate task-specific models, and invoke several models per video, so no prior reconstruction model estimates these attributes and throughput becomes a practical constraint on large-scale annotation. We therefore introduce EgoFound3R, a unified end-to-end model that estimates world-space hand geometry in a metric scale shared with the scene, and predicts point-wise interaction attributes, including visibility, contact, and distance. The model integrates three designs: (i) structured hand prompts that transfer pretrained geometric priors to world-space hand reconstruction; (ii) an explicit hand representation that decodes hand geometry and interaction attributes; and (iii) a shared-parameter multi-rate design that lowers inference cost. Together, these designs predict hand geometry and point-wise attributes in one pass. On OakInk-v2, TACO, and HOI4D, EgoFound3R reduces the mean per-joint position error (MPJPE) by 43.2%, 22.4%, and 11.6% over previous methods and predicts point-wise contact and distance alongside the geometry in the same pass, while attaining approximately 6x higher throughput.

---


### 196. [Supervise What Decides Success: Criterion-Aligned Auxiliary Losses for Latent World-Model Planning](https://arxiv.org/abs/2610.01224)

**<font color=#1a73e8>作者：</font>** Takumi Hara, Kanata Suzuki  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Latent world models plan by scoring candidate action sequences with distances in latent space. However, task success is judged by physical quantities, which we call the success-criterion quantities. In all four latent world models we examine, the end-effector position is encoded in the latent state with an error larger than the success criterion allows. Such a latent state cannot separate successful candidates from failing ones. We propose an auxiliary loss that uses success-criterion quantities as training targets, whereas existing latent world models take them only as inputs. During training, a linear head on the encoder and predictor outputs regresses the success-criterion quantities, and the regression error is added to the training loss. The head is discarded after training, so the model, its cost, and its inputs at test time are unchanged. This loss alone improves the success rate on PushT and cube by 3.5% and 3.4% (absolute), respectively, and both improvements are statistically significant. A success criterion thus specifies what a world model must retain in its latent state, and we show that it can serve directly as a training target.

---


### 197. [A Compact Explicit 4D Representation for Dynamic Scenes](https://arxiv.org/abs/2610.01229)

**<font color=#1a73e8>作者：</font>** Di Yang, Zhihao Li, Yanhai Xiong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A compact dynamic-scene representation must retain both the surfaces seen over time and the appearance needed to render them from new viewpoints. We present Sparc4D, a feed-forward autoencoder that encodes a monocular video with known cameras into a sparse 4D scene state. Static features are shared across the clip, while spatially anchored temporal slots compress time-varying features. A sparse decoder produces 2D Gaussian surfels, while stored source pixels preserve fine texture through geometric re-projection. The state includes one full source frame and dynamic-region pixels sampled every fourth frame, alongside learned features and sparse occupancy. For a 32-frame MultiCamVideo clip, it averages 0.95M 32-bit-equivalent values on random windows and 0.92M on the first-32 protocol. On first-32, Sparc4D reaches 21.70\,dB, compared with 20.40\,dB for MoVieS. On randomly placed windows, their PSNR scores are comparable. With stored texture disabled, temporal slots compress the time-varying feature state by a median $4.0\times$ and reduce the mean state from 1.04M to 0.42M values, with essentially unchanged target-view reconstruction quality. Without fine-tuning on real data, Sparc4D transfers to DyCheck and Neu3D, where stored texture improves LPIPS while slightly reducing PSNR.

---


### 198. [Revision-Aware Independent Agent Graphs for Dynamic Reasoning](https://arxiv.org/abs/2610.01249)

**<font color=#1a73e8>作者：</font>** Yan Luo, Selim-Antoine Lali, Jeremy Moebel 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Conventional reasoning protocols present a fixed, preselected task, so they cannot test whether an agent propagates relevant updates, preserves unaffected work, or reconstructs a historical task binding. We therefore study \emph{dynamic task routing}, in which an event stream revises task bindings and a system must select the document version valid at each query time before solving it. To study this problem, we repurpose six widely used benchmarks: MMLU, MMLU-Pro, MedMCQA, MATH, GPQA, and HumanEval into 31{,}119 dynamic episodes comprising 373{,}428 temporally categorized queries. This setting exposes a central trade-off: recomputing after every event wastes work, whereas unguarded reuse returns stale conclusions. We introduce the Revision-Aware Independent Agent Graph (RIAG), a bounded multi-agent policy that separates deterministic temporal resolution from task reasoning. RIAG caches solutions by immutable document identity, starts each fresh task with two unexposed attempts, and conditionally invokes audit and repair, using at most four calls per document version. On this collection, homogeneous RIAG achieves 54.24\% joint routing-and-answer accuracy at 0.62 calls/query, compared with 32.22\% at 18.00 calls/query for the strongest comparison method; heterogeneous RIAG reaches 49.78\% at 0.63 calls/query.

---


### 199. [A Resource-Aware Behavior Reconstruction and Hierarchical Semantic Learning Framework for Host Intrusion Detection](https://arxiv.org/abs/2610.01250)

**<font color=#1a73e8>作者：</font>** Youli Tao, Rui Tang, Hao Ren 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> System calls (syscalls) record key interactions between running programs and the operating system kernel, providing fine-grained and minimally intrusive data for host-based intrusion detection systems (HIDS) deployed in cloud and other modern computing environments. However, existing methods often model syscalls in their original execution order, where sequences from different processes are interleaved, making informative patterns difficult to extract and raising two questions: whether raw syscall sequences can be reorganized in a way that yields more discriminative representations, and how complex attack patterns can be effectively learned from the reorganized sequences. We propose ReSHID, a resource-aware behavior reconstruction and hierarchical semantic learning framework for host intrusion detection. It reconstructs semantically continuous sequences by leveraging syscall semantic invariants to cast subject identity and relationship resolution across PID namespaces as a bipartite matching problem and tracking file descriptor (FD) lifecycles to associate descriptors referring to the same resource. Additionally, features extracted from these sequences are organized into a lightweight subject behavior graph incorporating inter-subject relationships, where GATv2 captures key coordination patterns to model complex attacks involving multiple subjects. Experimental results show that sequence reconstruction combined with the detection method can improve HIDS performance. Even with a lightweight linear classifier, the proposed method achieves the best results among all compared methods in terms of F1-score (98.64%), ROC-AUC (99.80%), and PR-AUC (98.10%), while reducing the number of n-gram features by approximately 75.2% and 44.1% compared with the raw sequences and MGFE, respectively.

---


### 200. [Context-Aware Error Mitigation Orchestration for Hybrid Quantum Reinforcement Learning on NISQ Systems](https://arxiv.org/abs/2610.01253)

**<font color=#1a73e8>作者：</font>** Bisma Majid, Shabir Ahmed Sofi, Mir Mohammad Yousuf  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantum Reinforcement Learning (QRL) integrates reinforcement learning with parameterized quantum circuits and is a promising approach to combinatorial optimization. On Noisy Intermediate-Scale Quantum (NISQ) devices, however, decoherence, gate imperfections, and measurement errors reduce policy quality and make learning less reliable. Existing error mitigation techniques are generally applied as fixed corrections that do not adapt to changing noise conditions or to the evolving state of training. This work presents Adaptive Policy-Guided Error Mitigation (APGEM) as a context-aware orchestration layer of the hybrid quantum-classical training loop that dynamically selects the most suitable mitigation strategy during QRL training. APGEM evaluates Zero-Noise Extrapolation (ZNE), Probabilistic Error Cancellation (PEC), Clifford Data Regression (CDR), and Readout Error Mitigation (REM) using policy-level indicators, including quantum-state fidelity, policy entropy, cumulative reward, and approximation ratio, and integrates the selected strategy directly into the reinforcement learning loop. The framework is evaluated on the Capacitated Vehicle Routing Problem (CVRP), a representative NP-hard problem in urban logistics, under a range of NISQ noise models and noise levels. APGEM consistently outperforms conventional static mitigation methods, reaches approximately 94% of the utility of an oracle strategy, maintains higher quantum-state fidelity as noise increases, and produces more stable learning behaviour throughout training. Ablation studies show that the framework learns context-aware mitigation policies that adapt to different noise environments and circuit execution conditions. These findings demonstrate that integrating adaptive error mitigation into the learning process substantially improves the robustness and reliability of QRL on NISQ hardware.

---


> [!TIP]
> 当前位于：**151-200**（第 4/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-385](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
