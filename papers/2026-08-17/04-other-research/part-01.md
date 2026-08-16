# 📦 其他研究 | 2026年08月17日

> 本类共 **199** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-199](./part-04.md)

---

### 1. [Comparative Analysis of Multilingual Pre-trained Models for Nepali Automatic Speech Recognition](https://arxiv.org/abs/2608.12327)

**<font color=#1a73e8>作者：</font>** Suman Paudel, Sarbin Sayami  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual pretrained models nominally support Nepali, yet no controlled benchmark has compared them under a single fine-tuning protocol. We fine-tune six pretrained models (XLSR-53, IndicWav2Vec, MMS-1B, Whisper-Medium, Whisper-Large-v3-Turbo, and Conformer-Hi) spanning CTC self-supervised, autoregressive encoder-decoder, and hybrid Conformer-CTC architectures, on the OpenSLR SLR54 Nepali corpus (~165 hours) using identical preprocessing, splits, optimizer, and family-matched learning-rate schedules. We evaluate Word Error Rate (WER), Character Error Rate (CER), and Real-Time Factor (RTF) on three independent test sets (OpenSLR, FLEURS, Common Voice). Whisper-Large-v3-Turbo (14.76% WER) and IndicWav2Vec (14.89% WER) tie at the top despite a 9x parameter gap and 40x pretraining-data gap, providing direct empirical evidence that language-family proximity in pretraining can substitute for raw scale for in-domain Nepali. CTC decoders run up to 29x faster than autoregressive Whisper at the same accuracy, flipping the practical deployment preference toward CTC under any latency budget. Massively multilingual pretraining (MMS-1B) yields the smallest out-of-domain degradation on FLEURS (+12.55 pp), indicating that scale buys robustness rather than peak in-domain accuracy. The resulting benchmark provides the first standardized, multi-model, efficiency-aware reference numbers for Nepali ASR.

---


### 2. [Can Spectral-Clipping Enable Better Learning While Forgetting Less for Low-Rank Adaptation?](https://arxiv.org/abs/2608.12332)

**<font color=#1a73e8>作者：</font>** Hyowon Wi, Noseong Park  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In recent years, low-rank adaptation (LoRA) has emerged as a significant paradigm that freezes pre-trained weights and introduces small, learnable adapters instead of fine-tuning the full set of parameters. In this work, we uncover several key insights regarding the singular components of network parameters based on Singular Value Decomposition (SVD). Firstly, the principal singular components with large singular values in pre-trained network parameters can be effectively reused during fine-tuning, whereas the minor components with smaller singular values are more task-specific and require substantial adaptation. Secondly, we first establish the theoretical connection that the uncontrolled growth of singular values in LoRA adapters leads to the forgetting of pre-trained knowledge -- a well-known issue referred to as catastrophic forgetting. Building on these observations, we propose SCLoRA, which injects parameterized singular components with spectral clipping into the pre-trained model in a way that is aware of the spectral distribution of the pre-trained model. SCLoRA effectively adapts to new tasks by focusing updates on components that require adaptation, while simultaneously alleviating catastrophic forgetting. We conduct extensive experiments and demonstrate that SCLoRA not only improves downstream performance but also effectively retains pre-trained knowledge.

---


### 3. [From Refuse to Richness: Rubric Rewards for Long-Form Hallucination Reinforcement Learning](https://arxiv.org/abs/2608.12337)

**<font color=#1a73e8>作者：</font>** Yudong Wang, Zhe Yang, Wenhan Ma 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rewards that penalize unsupported claims can improve grounding in long-form generation, but they can also teach models to answer less. We study this refusal-to-richness trade-off in long-form hallucination RL. Instead of using global richness proxies such as length, claim count, detail, or pairwise relevance, we represent each question with a key-point rubric that specifies the required and optional information a useful answer should cover. These rubrics define coverage directly and are used both for evaluation and as reward signals. Across grounding-only, proxy-based, rubric-only, and combined rewards, we find a stable trade-off: strict grounding rewards improve support but suppress coverage, while unconstrained rubric rewards improve coverage but weaken grounding. A soft combination of grounding, rubric coverage, and relevance gives the best balance in our experiments, improving in-distribution support while transferring better to out-of-distribution checklist tasks than either grounding-only or rubric-only rewards.

---


### 4. [SDAM: Structure-Difference-Aware Memory Evolution for Complex Text-to-SQL](https://arxiv.org/abs/2608.12338)

**<font color=#1a73e8>作者：</font>** Keyan Xu, Dingzirui Wang, Xuanliang Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL aims to convert natural language questions into executable SQL queries. While memory-based agent system improves complex SQL generation, existing memory design neglect historical experience and suffer from weak structure analysis, shallow semantic understanding, and poor schema alignment. To address these challenges, we propose SDAM. Specifically, SDAM identifies potential errors via a structure-difference aware reasoning tree, extracts deep semantic rules through contradiction-aware reflection, and enhances structural consistency using a schema-grounded memory evolution mechanism to bind memory with database schemas. We integrate SDAM into a Text-to-SQL framework named SDAM-SQL. Experiment shows that SDAM-SQL achieves 2.0 and 0.4 improvement on BIRD-dev and Spider-test compared with mainstream Text-to-SQL methods, showing the effectiveness of SDAM-SQL.

---


### 5. [Position: The Alignment Community is Unintentionally Building a Censor's Toolkit](https://arxiv.org/abs/2608.12346)

**<font color=#1a73e8>作者：</font>** Sarah Ball, Phil Hackemann  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This position paper argues that modern AI alignment methods - originally designed to prevent harmful output - are dual-use technologies that may easily be misused by malicious actors for censorship and manipulation. By mapping current alignment techniques to the possibility and actual cases of misuse, we show that the quest for a "perfectly aligned" model inadvertently also provides malicious actors with an ever-improving tool for informational dominance. We need to discuss this dual-use potential now, as its risk is exacerbated by rapid user adoption of AI as information provider, economic power asymmetries, and a political landscape that increasingly shifts towards authoritarianism. We conclude by urging the community to consider the intentional misuse of AI alignment mechanisms and propose mitigation strategies to safeguard against this dual-use potential.

---


### 6. [DCBA: Detection of Collaborative Black-Hole Attacks in Connected Dominated Set using Baiting Process](https://arxiv.org/abs/2608.12347)

**<font color=#1a73e8>作者：</font>** Lata B T, Venugopal K R  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Mobile Ad-hoc Network (MANET) is temporary and dynamic network topology, wherein nodes are mobile in nature and distributed randomly in a network area. In MANET, nodes cooperate with each other to operate and forward data through multihop communication between source and destination. MANET is exposed to different types of attacks due to absence of central administration. However, some nodes decline to cooperate, misbehaves and appears to be malicious affecting network functionality and connectivity. Providing security and identifying malicious node has become one of the challenging research topics in MANET. Black-hole attack is considered to be most popular attack that degrades the overall network performance. Black-hole node falsely advertises the shortest path to destination intentionally to disrupt the network communication resulting in packet drop. In collaborative black-hole attacks, multiple black-hole nodes cooperate and launch attacks in order to degrade network reliability. In this article we propose a Lightweight technique to detect and isolate Collaborative Black-Hole attacks (LW-CBH) by enhancing existing AODV routing protocol. In this scheme a timer based baiting process and reverse tracing setup is used to detect malicious node through control status message in MAC layer which are Reply Sequence (R-SEQ) and Code Sequence (C-SEQ) message of connected dominated set of nodes. However existing AODV routing protocol fails to detect malicious node during dynamic topology changing in MANET. Simulation of proposed technique is performed using discrete event simulator tool NS-2.35. The simulation results are evaluated for throughput, packet delivery ratio, average end-to-end delay and normalized routing overhead.

---


### 7. [The Affordance is the Message: Creative Media as Complex Systems](https://arxiv.org/abs/2608.12349)

**<font color=#1a73e8>作者：</font>** Ane Espeseth, Elias Najarro  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The affordances of a creative medium strongly condition the creative artefacts the medium will produce. In this work, we present a formalisation of computational creativity (CC) media using the conceptual toolbox of complex systems (CS). We introduce the notions of emergence, collective intelligence and self-organisation, non-linear dynamics, criticality, multi-scale hierarchy, phase transitions, diversity of attractors, path dependence, and open-endedness, and connect them to the existing CC literature. Together these nine properties form a vocabulary with which creative media can be described and compared at the system level, while medium affordances are the design-level mechanisms that determine each medium's complex system properties. The formalisation emphasises the influence of each medium's affordances in determining what the medium can produce in creative processes. To demonstrate the proposed theoretical approach, we characterise a diverse set of media (r/place, Minecraft, cellular automata, Twitter, Boids, ...) using this vocabulary. The proposed formalisation under the CS concepts serves a dual purpose: it establishes a link between the affordances and realised practices of the medium, and it offers a shared lens for characterising existing creative media.

---


### 8. [Visibility Asymmetry: How Vendor Attention Shapes Which EdTech Breakdowns Become Product-Visible](https://arxiv.org/abs/2608.12353)

**<font color=#1a73e8>作者：</font>** Lucan Li  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Infrastructure scholarship in CSCW often treats breakdown as the moment when infrastructures become visible. However, in vendor-managed sociotechnical systems, not all breakdowns become visible to actors who have the capacity to repair them. Drawing on a retrospective qualitative study of a Chinese K-12 EdTech deployment, including 11 interviews, 5 classroom observations, and more than 28 days of field notes, this paper introduces visibility asymmetry: a sensitizing concept for understanding how similar local breakdowns encounter uneven conditions for being routed, recognized, and acted upon. The analysis traces a four-stage mechanism through which procurement categories sort schools into attention tiers; staffing and visit cadence follow those tiers; only some local problems travel through staff or administrator channels; and dashboards can re-code unresolved repair labor as evidence of adoption. By shifting attention from the occurrence of breakdown to the organizational channels through which breakdown becomes actionable, this paper extends CSCW work on infrastructure, articulation work, and repair. It concludes by discussing implications for feedback systems that can surface repair needs without expanding surveillance.

---


### 9. [DrawTalking It Out: Creativity-Support Research as Creative Process Itself](https://arxiv.org/abs/2608.12357)

**<font color=#1a73e8>作者：</font>** Karl Toby Rosenberg  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> I think the creative process in conducting open-ended creativity-adjacent research is itself part of the creative process (including ideation, pivots, and tangents excluded from the final work) that deserves greater emphasis. how might we bridge multiple open-ended projects and serve broader non-technical audiences? We may choose to emphasize interaction techniques rather than singular tools in isolation. We may grow a community based on our shareable experiences in creativity interactions, to draw more complete pictures of how we creatively solve creativity problems (or satisfy curiosities). This may lead to new directions. I briefly elaborate on this using the example of "DrawTalking" a drawing+talking interactions work. DrawTalking itself resulted from a winding creative process exploring spontaneous interactive world-building and storytelling when drawing and talking.

---


### 10. [Interaction Readiness: A Framework for Building and Evaluating AI Agents in Human Roles](https://arxiv.org/abs/2608.12358)

**<font color=#1a73e8>作者：</font>** Sudhir Alladi Venkatesh  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Product and engineering teams building role-bearing AI agents face an evaluation gap: an agent can produce accurate, safe, and fluent content while still failing the behavioral requirements of its assigned role. This paper introduces Interaction Readiness as a framework for specifying and evaluating that missing layer of performance. The framework separates content specifications, which govern what an agent knows and says, from interaction specifications, which define how an agent should conduct itself in a role-governed exchange. Interaction specifications require teams to define role purpose, authority boundaries, recurring situations, boundary cases, repair behaviors, and audit criteria before deployment. We operationalize interaction readiness through four agent operations: understanding purpose, calibrating authority, managing tone, and repairing breakdowns. Using StudyChat, a public dataset of student interactions with an AI tutoring agent, we show that content accuracy and interaction quality are independent dimensions: an agent may be factually correct while failing as a tutor, or interactionally sound while technically wrong. The most persistent failure is authority miscalibration: the agent often knows how to answer, but not whether, when, or how the tutor role permits it to answer. The paper translates these findings into a specification template and audit procedures that product and engineering teams can apply before and after deployment

---


### 11. [What Do We Mean When We Talk About Infographics?](https://arxiv.org/abs/2608.12370)

**<font color=#1a73e8>作者：</font>** Xiaoyu Liu, Vishnu Sreekanth, Vraj Patel 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> There has been limited clarity and consistency regarding what the term infographics, or information graphics, refers to in visualization research and practice. In particular, little is understood about where people's conceptualizations of infographics converge or diverge. To address this gap, we conducted a systematic literature review and a practitioner survey to identify and contrast different perspectives on infographics. We performed inductive coding on 487 sentences from 111 visualization and HCI papers, and analyzed questionnaire responses from 44 domain practitioners. Our findings reveal recurring dimensions of conceptual disagreement on infographics: role of text, relationship with data visualization, and relationships with statistical charts and data comics. Based on the results, we recommend future work to explicitly report any assumptions made along these diverging conceptualizations, to investigate the cognitive origins of these disagreements, and to develop more holistic design component frameworks for infographics. The supplementary materials are available via OSF and as an interactive web application.

---


### 12. [Position: We Need Practical AI Alignment Methods to Mirror Human Reasoning](https://arxiv.org/abs/2608.12372)

**<font color=#1a73e8>作者：</font>** Vijay Keswani, Breanna K. Nguyen, Cyrus Cousins 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI systems are increasingly employed as decision aids, decision delegates, or autonomous decision-makers. This position paper argues that in many settings, particularly high-stakes decision-making, we need accurate cognitively-aligned AI systems that reason similarly to their users, and faithfully communicate their reasoning. We review evidence that cognitive alignment improves understandability and trustworthiness, and provide new survey data showing that many users find cognitive alignment "essential" when an AI's rationale for a judgment or action is important to them. We outline the gaps between existing alignment methods and what is needed to achieve cognitive alignment, and present a research agenda to address these gaps. We argue that cognitive misalignment represents a likely impediment to AI adoption in many envisioned applications, and that addressing it is important for creating AI systems on which users are both willing and justified to rely.

---


### 13. [Which Site, and When: A Free-Satellite-Data Test of Himalayan Glacial Lake Bursts, Landslides, and Ice Floods](https://arxiv.org/abs/2608.12422)

**<font color=#1a73e8>作者：</font>** Matthew Kahn, Milan Arjel, Nirmala Adhikari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two free satellite signals carry real information about glacial-lake outburst risk in the Nepal Himalaya: radar interferometry sees a moraine dam slowly sagging, and satellite weather marks the weeks when a primed lake is under stress. A companion feasibility study found that deformation indicates which lake is destabilizing and weather indicates when it is at risk, but proposed no predictive model. To address this gap, we propose and evaluate models that predict which site is susceptible and when a trigger arrives. We test three related hazards on free data alone: large moraine- and ice-dammed bursts, rainfall-triggered landslides, and smaller floods from ponds on and around a glacier. Each hazard gets two questions, never blended. Using 589 dated outbursts from HMAGLOFDB and several thousand catalogued landslides, we match each event against similar but unfailed sites, and hold every model to a strong simple baseline under spatial cross-validation that withholds whole map tiles, so no model succeeds by recognising a trained-on neighbourhood. Antecedent weather times the trigger at ROC 0.73 for big bursts, 0.83 for landslides, and 0.82 for small floods. Terrain ranks susceptibility only in part: scored naively it appears near 0.9, largely because catalogued failures cluster in wetter ranges; matched against comparable nearby sites the honest figures are 0.76, 0.71, and 0.54 (no better than chance). The burst signal holds within single regions, reaching 0.89 in Nepal alone. Five deep-learning models do not decisively beat a simple gradient-boosted baseline. Three score marginally higher on landslides, a hint too small to confirm. For the lake hazards the baseline wins outright, reproduced by a three-rule decision tree on ruggedness and monsoon rainfall. We close with a ranked Nepal watchlist, a prioritisation aid, not a prediction, and note where free data reaches its limits.

---


### 14. [MindMemOS: A Portable and Self-Evolving Memory Operating Layer for AI Agents](https://arxiv.org/abs/2608.12428)

**<font color=#1a73e8>作者：</font>** Kaichao Liang, Yuqi Cui, Hao Kong 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory is a core component of AI agents, enabling them to accumulate experience, maintain personalization, and adapt over long-term interactions. However, existing memory systems often remain fixed after development, limiting their ability to adapt their memory models, organization strategies, and procedural knowledge through continued use. We present MindMemOS, a portable and self-evolving memory operating layer that organizes open-world information using a unified entity property timestructure. MindMemOS supports scenario-adaptive memory modeling, higher-order pattern discovery, autonomous memory refinement, and continuous skill evolution. Its MindMemEvolve algorithm employs validation-driven evolutionary search to optimize memory schemas for target scenarios, whiledreaming consolidates accumulated memories by merging redundant records and resolving conflicts. In addition, implicit corrective feedback serves as a human-in-the-loop signal for identifying and revising potentially inaccurate or misaligned memories. Its MindSkillEvolve algorithm further transforms agent execution trajectories into reusable and progressively refined skills. MindMemOS achieves 94.03% accuracy on LOCOMO and 70.63% on PersonaMem. MindSkillEvolve improves SpreadsheetBench success by 9.2 percentage points over the initial-skill baseline.

---


### 15. [The energetic cost of mitigating AI attacks in cellular networks](https://arxiv.org/abs/2608.12431)

**<font color=#1a73e8>作者：</font>** Adrián Losada, Hao Qiang Luo-Chen, David Segura 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The integration of Artificial Intelligence (AI), generally as Machine Learning (ML) algorithms, in all levels and aspects of cellular networks demonstrates the success of data-driven algorithms; for example, the Radio Intelligence Controller (RIC) of the O-RAN paradigm bestows the network with optimised radio resource allocation, load balancing or energy efficiency functions, among others. Nevertheless, this dependency on data opens new security vulnerabilities, as attackers can alter data properties and steer ML models to underperform or degrade. Conversely, the developed mitigation strategies are effective, but they generate a computational load which, in consequence, results in an energy cost generally overlooked, even in the current energy-awareness context. In this work, consumption of a defence technique is characterised, and the challenges raised by the triad of ML accuracy, robustness and energy efficiency are outlined.

---


### 16. [MARCH: Scaling Recurrent Memory with Content-Routed State Anchors](https://arxiv.org/abs/2608.12435)

**<font color=#1a73e8>作者：</font>** Ming Zhang, Kaisen Yang, Shu Yu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers owe much of their strong long-context retrieval capability to a token-level memory that grows with context length. This flexibility, however, incurs a quadratic computation complexity during training and a key--value cache that grows linearly during autoregressive inference. Recurrent alternatives offer efficient decoding by compressing the entire history into a fixed-size state, but often underperform on recall-intensive tasks since earlier associations usually get overwritten by subsequent updates, and only the most recent contextual information is retained. In this paper, we introduce Memory-Anchor Routing across Context History (MARCH), a network architecture that effectively scales state-space models beyond a fixed-size dimension, while maintaining computational efficiency over long-sequences. MARCH periodically caches cumulative recurrent-state checkpoints as state anchors and associates each anchor with a compact, content-conditioned anchor key. This lets MARCH maintain a memory bank, which can grow as context length increases, providing a controllable trade-off between historical resolution and memory cost. At each token, MARCH produces an anchor query to attend all causally available state anchors, and the output is calculated as an attention-style aggregation over all historical anchors along the current state. We show that after standard pretraining, MARCH consistently outperforms multiple linear attention variants across commonsense reasoning, LongBench, and in-context retrieval. These results demonstrate that content-routed state caching substantially strengthens recurrent long-range memory while preserving its native computation path.

---


### 17. [Multi-AUV Ad-hoc network-based Target Tracking: A Value Gradient Guidance Multi-Agent Diffusion Reinforcement Learning Approach](https://arxiv.org/abs/2608.12436)

**<font color=#1a73e8>作者：</font>** Jiaao Ma, Chuan Lin, Guangjie Han 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-AUV ad-hoc network-based target tracking requires networked autonomous underwater vehicles (AUVs) to cooperatively track maneuvering targets under constrained acoustic communication, dynamic topology, and uncertain ocean disturbances. Although multi-agent reinforcement learning (MARL) enables decentralized coordination through centralized training, existing methods suffer from high-dimensional joint state-action modeling, noise-sensitive policy generation, leading to unstable training and degraded tracking. To address these issues, we propose VGG-MADiffRL, a value-gradient-guided multi-agent diffusion RL algorithm, and MDCA, a diffusion?based hierarchical control architecture. Leveraging underwater mission characteristics, we model sonar detection mechanisms and ocean current disturbances, formulating cooperative tracking for multi-AUV ad-hoc networks as an MDP. The proposed MDCA constitutes a three-tier closed-loop control framework: a global intelligent control layer, a local online training layer, and a physical action execution layer. This structure enables synergistic optimization across task allocation, local decision processes, and execution feedback. Within MDCA, the local online training layer is the policy learning framework; VGG-MADiffRL builds on diffusion policies and incorporates value gradients to guide action generation in the reverse denoising process, steering the generated actions towards higher expected returns. It employs twin value networks with joint optimization and soft target updates to mitigate overestimation and training oscillations, promoting more stable convergence. Experimental results show that VGG-MADiffRL consistently achieves faster convergence, higher tracking accuracy, and smoother training dynamics in cooperative tracking scenarios, validating its effectiveness and practical engineering value in dynamic underwater settings.

---


### 18. [Unifying Generative Models with Path Integrals](https://arxiv.org/abs/2608.12438)

**<font color=#1a73e8>作者：</font>** Ramon Winterhalder  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We formulate generative modeling as a path integral in which flow-based, diffusion-based, variational, and adversarial models arise as different evaluation principles for a single master action. Its Martin-Siggia-Rose-Janssen-de~Dominicis (MSRJD) form separates free from interacting probability flows and opens them to diagrammatic perturbation theory. The expansion yields a one-loop correction to deterministic samplers at no stochastic-sampling cost, which we validate on solvable and nonlinear drifts, where it reduces a 53 % tree-level error to 1.6 %. Imperfect learned scores enter as insertions and yield a response-weighted score-matching objective, and symmetry-equivariant drift design becomes an operator expansion with EFT power counting.

---


### 19. [Dual Spatial-Temporal Attribution: Architecture-Aligned Post-Hoc Explainability for Recurrent Graph Anomaly Detection](https://arxiv.org/abs/2608.12441)

**<font color=#1a73e8>作者：</font>** Iyad Assaad Nekka, Hamida Seba, Khaled Walid Hidouci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning detectors for anomalies in dynamic graphs have reached strong accuracy, yet they remain opaque: when an edge is flagged, the analyst receives a score but no reason. This opacity is untenable in the cooperative, regulated information systems where such detectors are deployed, where automated decisions must be auditable and trustworthy. We address this gap for AddGraph, the foundational GCN+GRU framework for edge-level anomaly detection in dynamic graphs, which to our knowledge has never been equipped with any form of explainability. We present a strictly post-hoc explainability framework, X-AddGraph, built on a Dual Spatial-Temporal Attribution (DSTA) mechanism whose three components are each aligned with one of AddGraph's architectural modules: a gradient-based relevance attribution over the current adjacency structure (spatial), a direct reading of the contextual attention weights already computed during inference (short-term temporal, at zero additional cost), and a gradient rollback through the recurrent hidden states (long-term temporal). Because the detector is frozen, detection performance is preserved exactly (Delta AUC = 0, verified empirically to ten decimal places). On the UCI Message benchmark, our trained AddGraph baseline reaches an average per-snapshot AUC of 0.8705, exceeding the originally published result; X-AddGraph reproduces every score identically while adding explanations where none existed. Evaluated across four edge populations - confident true positives, low-confidence true positives, false positives, and random samples - the long-term attribution identifies historical snapshots carrying significantly more counterfactual signal than random selection (0.127 vs. 0.074), a capability that no spatially-blind explainer can provide. We release our implementation for full reproducibility.

---


### 20. [MV2: Multi-View Multi-Vehicle Driving Dataset for Novel View Synthesis](https://arxiv.org/abs/2608.12442)

**<font color=#1a73e8>作者：</font>** Sanjay Bhargav Dharavath, Hanvitha Saraswathi Mukkamala, Faizan Farooq Khan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Differentiable rendering has advanced novel view synthesis (NVS), yet applying it to real-world driving remains difficult due to sparse capture viewpoints, dynamic objects, and limited multi-trajectory data. We introduce the Multi-View Multi-Vehicle (MV2) dataset and benchmark for evaluating NVS models under large viewpoint changes in dynamic urban scenes. MV2 features synchronized captures from a car, scooter, and drone, each following distinct yet synchronized trajectories. Training NVS methods on one vehicle's camera stream and testing on another enables evaluation under substantially larger viewpoint variations than existing single-trajectory datasets. All sequences are registered via Structure-from-Motion and camera poses verified using manual pixel-level correspondence annotations, yielding 50 high-quality scenes with 12000 images. Benchmarking recent NVS and camera pose estimation methods shows that NVS performance degrades with increasing viewpoint disparity, and that feed-forward pose estimators notably lag behind optimization-based approaches, highlighting MV2 as a rigorous testbed for NVS in driving. The dataset, benchmark protocol, and project resources are available at this https URL.

---


### 21. [Personalized Scorer Modeling: A Learning-Based Framework for Deriving Robust Sleep Stage Labels from Multiple Experts](https://arxiv.org/abs/2608.12446)

**<font color=#1a73e8>作者：</font>** Seyyed Ali Hoseini, Javad Baseri, Hamid Saadatfar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Sleep stage classification is important for the diagnosis and management of sleep disorders, yet most automatic staging studies evaluate models against a single reference hypnogram despite known inter-scorer variability. This study investigates whether multi-scored datasets can be used to construct more reliable reference labels from the collective behavior of multiple experts. We use the publicly available DOD-H and DOD-O datasets. EEG (C3-M2) and chin EMG signals were segmented into 30-s epochs, and 30 features were extracted from each modality, yielding 60 features for EEG+EMG. We propose a learning-based hypnogram (LBH) that models the stage-specific behavior of each scorer using confusion matrices derived from machine-learning models. After column normalization, these matrices estimate the probability of each true sleep stage given each scorer's label; probabilities are aggregated across scorers to assign the final label for each epoch. LBH was evaluated with random forest, support vector machine, and multilayer perceptron classifiers under EEG-only and EEG+EMG settings, and compared with the dataset hypnogram (DH) and best-scorer hypnogram (BSH). LBH consistently improved overall performance. The best results were obtained with random forest and EEG+EMG, reaching 86.07% accuracy, 85.46% precision, and 85.29% F1-score on DOD-H, and 86.04% accuracy, 85.21% precision, and 84.70% F1-score on DOD-O. These findings suggest that personalized scorer modeling can improve reference hypnogram construction without discarding information from individual experts.

---


### 22. [Exemplar-based objective classification of gust-induced loads across multiple flight conditions](https://arxiv.org/abs/2608.12448)

**<font color=#1a73e8>作者：</font>** Paolo Olivucci, Kowshik Srivatsan, David E. Rival  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Is it possible to find an objective classification criterion that organizes the complexity of gust-induced loads across many flight conditions? And one that remains as interpretable as a labelling based on coarse parameters, such as the flight attitude? Our approach encodes a large number of experimental observations through a machine-learned representation and applies a summarization procedure to select a minimal subset of highly significant exemplars. The exemplars provide a similarity-based objective classification criterion of all the observations, they can be more conveniently inspected by experts and can become subject of more refined experiments. We demonstrate the approach on a database of 3480 pressure-load measurements induced by random gusts on a flying-wing model across six flight attitudes. We find nine fundamental response types that recur across multiple attitudes; analysis of a type's transient response enables physical intuition into the underlying fluid mechanics.

---


### 23. [Learning Under Treatment-Induced Label Indeterminacy with Expert Annotations of Counterfactual Outcomes: A Case Study in Neurological Prognostication](https://arxiv.org/abs/2608.12477)

**<font color=#1a73e8>作者：</font>** Xiaobin Shen, Chloe Y.H. Huang, Jonathan Elmer 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Clinical prediction models are often developed as if the outcome of interest were cleanly observed for every patient. This assumption fails when treatment decisions make the clinically relevant outcome permanently unobservable. As a case study of this problem, we consider post-cardiac-arrest neurological prognostication using a cohort of 2,497 patients, including 1,429 patients whose outcomes were rendered indeterminate by treatment decisions. These patients with indeterminate outcomes were reviewed by independent clinical experts, who provided their guesses of counterfactual outcomes about what would have happened to the patients. We refer to these patients as uncertain cases. We also have patients for whom we observe their clinically relevant outcomes; we refer to these patients as certain cases. We propose a framework for evaluating prediction models that explicitly splits the evaluation between certain and uncertain cases. Here, we cannot easily evaluate both types of cases in a uniform manner as the available target labels differ. We then propose a simple prediction model that uses target labels from both certain and uncertain cases in a manner that allows us to trade off between them. Across the proposed neural model and a collection of tabular baselines, models with similar certain-case AUROC can nevertheless differ substantially in both certain-case Brier score and their probability estimates for uncertain cases. Improving alignment with target labels of uncertain cases for our proposed model generally comes at the cost of worse accuracy on certain cases, highlighting an explicit tradeoff that standard evaluation conceals. These results show that when treatment decisions determine whether clinically meaningful outcomes remain observable, conventional evaluation metrics can miss important failure modes in the very patients for whom prognostic support matters most.

---


### 24. [When Can You Trust Offline Evaluation of Equal-Cost Top-k Allocation? A Controlled, Reproducible Benchmark and Practitioner's Guide](https://arxiv.org/abs/2608.12489)

**<font color=#1a73e8>作者：</font>** Binshuang Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Organizations decide whom to treat under a budget and want to know what a targeting rule would have earned before deploying it. Off-policy evaluation promises this from logged data, but the deployable rule is a deterministic top-k policy: it removes all averaging over actions, so weak overlap hits the estimate directly. We benchmark six estimators across five datasets and two known-effect sweeps, and validate the mechanisms against a non-simulated paired reference. First, weak overlap is governed by logger-target action alignment, not by logging sharpness alone: what governs support is the logger's probability of the target's actions. Sharpening a logger built from the target's own score barely moves overlap over the tested range; action-level disagreement collapses it. Effective sample size ranks this risk across logging environments, but is weak at ranking candidates within the single log a practitioner holds, and its cut point does not transfer. Second, the optimizer's curse is not fixed by cross-fitting the outcome nuisance. When the rule is fit on the data used to evaluate it, cross-fitting the nuisance alone leaves the reuse bias in place and makes it worse. Honest policy-level splitting avoids the reuse by targeting the learning procedure's value -- a change of estimand, not a de-biasing of the full-sample policy. Third, propensity-estimation error is the largest degradation we measure: an out-of-fold estimate hurts IPS more than any other stress we apply, leaves doubly-robust estimation almost unchanged, and can invert the overlap diagnostic itself. Logging is synthesized and propensities floored at 0.02, so every failure occurs with bounded weights; the floor also reduces the two tuned hybrids to their untuned parents, leaving four practically distinct estimators, and all exact-value surfaces are synthetic or semi-synthetic. We release the benchmark; public data only.

---


### 25. [HIMEC: Directional Change Representation and Fixed-Interface Decoding for Remote Sensing Image Change Captioning](https://arxiv.org/abs/2608.12502)

**<font color=#1a73e8>作者：</font>** Aysha Ashraf, Shaina Ashraf, Wafaa I. M. Hussin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing image change captioning (RSICC) converts bitemporal imagery into a sentence describing semantic changes. Most RSICC methods condition caption decoders directly on fused visual features, leaving intermediate change structure and decoder-interface consistency less studied. We present HIMEC, combining Directional Change Representation (DCR) with fixed-interface decoding. DCR separates signed differences into appearance-oriented, disappearance-oriented, and shared-context streams before fusion. A learned-query encoder converts the fused representation into visually conditioned change-query tokens that form the scene decoder's only sample-dependent memory. A training-only auxiliary phrase decoder supplies caption-derived supervision. With a fixed zero input, the scene decoder maintains the same interface during training and inference. Separately, we evaluate a local-to-scene cascade conditioned on teacher-forced local states during training and autoregressive states at inference. On changed LEVIR-CC validation pairs, these states have a mean cosine distance of 0.69. Regime-matched conditioning recovers most of the associated deficit, whereas permuting state correspondence causes no detectable penalty. These findings are limited to the evaluated cascade. In a matched three-seed comparison, HIMEC reaches a Consensus-based Image Description Evaluation (CIDEr) score of $142.81\pm0.60$ on LEVIR-CC, versus $139.51\pm3.40$ for direct fused-feature memory. On SECOND-CC, fixed-zero and regime-matched diagnostic conditioning reach 75.67 and 76.99 CIDEr, respectively, versus 60.77 for the mismatched cascade. The source code will be made publicly available at this https URL upon publication.

---


### 26. [Exploring Oversmoothing with Householder Matrices](https://arxiv.org/abs/2608.12514)

**<font color=#1a73e8>作者：</font>** Bhaskar Karol  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep graph neural networks(GNNs) suffer from oversmoothing- a progressive collapse of node representation towards a low information subspace as network depth increases because the normalized graph propagation operator is repeatedly applied directly to the hidden representations. In this work we study Householder Graph Neural Network (HouseGNN). Rather than updating the hidden state like standard GCN, HouseGNN uses the aggregated neighbourhood message solely to estimate a reflection direction; the node embedding is then updated by a Householder reflector followed by GroupSort, yielding a piecewise orthogonal layer that preserves Euclidean norm at every node and at every depth. We prove three core properties: (i) every internal layer preserves the node-wise Euclidean norm; (ii) the Householder reflector is scale scale and sign-invariant in the message; and (iii) pairwise distance between nodes can change through mismatch between node-wise orthogonal operators.

---


### 27. [Entropy-Augmented Multi-Objective Policy Optimization in Multiagent Systems](https://arxiv.org/abs/2608.12534)

**<font color=#1a73e8>作者：</font>** Jamie Santos, Ayhan Alp Aydeniz, Raghav Thakar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Autonomous agent teams deployed in settings such as marine and extraterrestrial outposts must coordinate actions to achieve optimal outcomes across multiple competing objectives. Multi-objective evolutionary algorithms such as NSGA-II optimize for diversity in the objective space, but neglect diversity in the behavior space, possibly leading to premature convergence and a collapse in behaviors that may differentiate policies in different external conditions. To address this, we introduce an entropy-augmented policy evaluation strategy that incorporates an entropy bonus into agent fitness scores, discouraging behavioral homogeneity across the evolving population. By augmenting policy evaluation with a behavior-space diversity signal while preserving the underlying Pareto optimization framework, our method is designed to encourage exploration of behaviorally distinct policies in multiagent domains. We evaluate our approach across rover-domain experiments with qualitatively distinct reward structures and observe hypervolume improvements of up to 48% relative to the NSGA-II baseline, suggesting that behavioral diversity is a promising and underexplored direction for improving multi-objective multiagent evolutionary optimization.

---


### 28. [GENADA: efficient generative time series adversarial attack framework](https://arxiv.org/abs/2608.12535)

**<font color=#1a73e8>作者：</font>** Michael Baronov, Denis Vorobev, Margarita Rusanova 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Deep learning models are widely used for time series analysis in domains such as healthcare, finance, energy systems, and environmental monitoring. However, these models remain vulnerable to adversarial attacks, where small input perturbations cause severe degradation in predictive performance. Commonly used gradient-based attacks, iterative first-order methods, are computationally burdensome, as they repeatedly backpropagate through the victim model to compute input gradients during a number of iterative refinement steps. We propose a GENerative ADversarial Attack (GENADA) that learns a generative model to produce deceptive perturbations directly in a single forward pass and a procedure to train it. Variants include single-step and iterative generative attack schemes. The validation considers attacks on several neural models and datasets in the time-series domain, a controlled, low-dimensional setting. Empirically, GENADA achieves comparable attack quality to strong baselines while requiring less time to generate perturbations during inference.

---


### 29. [Surface-to-Skeleton 3D Cephalometry: Estimating Hidden Skeletal Landmarks from CT-Derived External Soft-Tissue Surfaces](https://arxiv.org/abs/2608.12537)

**<font color=#1a73e8>作者：</font>** Tomoki Abe, Taiki Kanaya, Kazuki Saita 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing 3D facial-landmark methods localize points on visible skin, but whether CT-defined internal skeletal landmarks can be inferred from external soft-tissue geometry remains unclear. We formulate a coordinate-consistent surface-to-skeleton task using same-acquisition CT-derived surfaces, separating estimation from optical-to-CT registration, scanner-domain, and acquisition-state effects, with coverage analyzed separately. From 240 clinical CT scans from two hospitals, we construct a locked retrospective protocol pairing CT-derived external soft-tissue point clouds with 21 skeletal landmarks and three visible soft-tissue landmarks. An integrated hierarchical point-cloud model achieves 2.97 mm mean radial error on skeletal landmarks and 3.03 mm on deep or surface-invisible landmarks in 40 held-out patients. Patient-mismatch controls support patient-specific signal beyond a fixed population configuration or global similarity alone, while coverage ablations indicate dependence on non-anterior geometry. Optical-transfer diagnostics reveal substantial coverage-related and global-configuration components, although deployable optical inference remains unresolved. These results answer the controlled feasibility question affirmatively and provide a basis for hidden skeletal landmark inference.

---


### 30. [Transforming Interactions in Thesis Supervision: An Exposé-First Workflow in Higher Education](https://arxiv.org/abs/2608.12546)

**<font color=#1a73e8>作者：</font>** Lin-Yin Huang, Dennis Zyska, Iryna Gurevych  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> At the studied research institute, one professorship oversees approximately 20 theses per semester, while day-to-day supervision is distributed among doctoral and postdoctoral researchers. To manage this supervision demand, the institute uses an exposé-first workflow in which students prepare a research proposal before entering the main thesis-writing phase. This paper asks how students, supervisors, and administrators experience the exposé-first workflow as a structured process for early thesis preparation, and how it redistributes responsibility, supervision, and administrative coordination work across roles and two digital platforms. Based on a mixed-methods study analyzed through Frauenberger et al.'s four reflective design lenses, the findings show that the exposé-first model made thesis preparation more structured by turning early research planning into a staged process of proposal writing, feedback, and approval. Students reported that this process helped them clarify research goals and take ownership of their research plans at an early stage. However, the workflow redistributed rather than reduced work: supervisors shifted toward iterative feedback, feasibility checking, and preliminary quality assurance, while administrators carried much of the coordination across platforms, deadlines, submissions, and feedback. The paper contributes an analysis of exposé-first thesis preparation as a sociotechnical workflow, showing how workflow redesign can improve structure while leaving essential administrative coordination work underrecognized.

---


### 31. [Analysis of Motor Signatures of Social Adaptation in Autism for Efficient Human-Centric Systems](https://arxiv.org/abs/2608.12548)

**<font color=#1a73e8>作者：</font>** Lara Pereira, Teresa Sousa, Miguel Castelo-Branco 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dance imitation integrates motor planning, sensorimotor integration, and social cognition, offering a sensitive framework to characterize motor behavior in autism. In this work, we explore a computational analysis framework to identify potential biomarkers that allow the design and development of improved medical and human-machine systems. We analyzed 3D motion capture data from autistic and neurotypical adults performing dance imitation under solo and socially-framed duo conditions. Methodologically, using Dynamic Time Warping, we quantified movement consistency and propose the Social Context Sensitivity Index (SCSI) to measure modulation of variability by social framing. These features were then used on a classifier to discriminate subjects into autistic or neurotypical groups. Results show that neurotypical adults exhibited increased movement variability in socially-framed imitation, especially in upper and lower limbs, whereas autistic adults maintained consistent movement across contexts. Classification achieved 79.2% balanced accuracy in distinguishing groups. These findings suggest that social context sensitivity in motor imitation constitutes a robust biomarker of autism-related motor behavior, highlighting the importance of social modulation in motor assessments and informing the development of inclusive human-centric technologies.

---


### 32. [Legally Mandated, but Still Inaccessible: Digital Tensions in Older Adults' Use of Norwegian Web Services](https://arxiv.org/abs/2608.12552)

**<font color=#1a73e8>作者：</font>** Yavuz Inal, Sujay Shalawadi, Eleftherios Papachristos  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Norway is among the most digitalized countries in the world, where access to essential services increasingly depends on digital systems. Although universal design of ICT is legally required across public and private sectors, ensuring cognitive accessibility for older adults involves more than technical compliance. We analyzed responses from 294 participants aged 55 to 90 to examine the barriers they encounter when using digital services. Our findings identify four tensions, namely navigational, semantic, procedural, and temporal, which reveal how accessibility barriers emerge through misalignments between service design, system assumptions, and older adults' capabilities. Together, these tensions show that checklist-based compliance does not necessarily translate into lived accessibility when engaging with mandatory or near-mandatory digital services. We discuss the need to move beyond minimum compliance frameworks toward accessibility approaches that better support older adults' independent participation in digital society.

---


### 33. [CAS: A Causal Attribution Score for Local and Global Explainable Artificial Intelligence](https://arxiv.org/abs/2608.12555)

**<font color=#1a73e8>作者：</font>** Michael Georgiades, Charalambia Varnava  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predictive explanation methods attribute a model output; they do not, by themselves, attribute an intervention effect on the real-world outcome. We introduce the Causal Attribution Score (CAS), a compact score architecture for causal explanation. CAS starts from an identified interventional coalition game, allocates the joint intervention contrast with causal Shapley contributions, and converts those raw outcome-scale effects into Local CAS, Signed Local CAS, and two complementary Global CAS summaries. The innovation is not a new Shapley formula, but a local-to-global causal reporting layer with an explicit intervention target. In the known-truth benchmark, eight repeated primary-interaction simulations (n = 2,200 each, three actions) gave mean Local CAS MAE of 0.107 for coalition-aware CAS, compared with 0.173 for one-at-a-time normalisation and 0.213 for a global normalised absolute ATE vector. The paired advantage over one-at-a-time normalisation increased from -0.003 under additivity to 0.091 under strong interactions. On both empirical DoubleML datasets, 401(k) eligibility/net financial assets (n = 9,915) and Pennsylvania reemployment bonus/unemployment duration (n = 5,099), predictive SHAP/TreeSHAP rankings differed materially from Feature-CAS rankings of treatment-effect modifiers. In Pennsylvania, dep1 (exactly one dependent) moved from predictive global rank 13 to Feature-CAS rank 2 and was the leading local Feature-CAS modifier. These results isolate the added value of separating what predicts the outcome from what explains heterogeneity in an estimated causal effect.

---


### 34. [Attribute-Conditioned Multimodal Slot Factorization for Controllable Fashion Retrieval](https://arxiv.org/abs/2608.12570)

**<font color=#1a73e8>作者：</font>** Najmeh Forouzandehmehr, Topojoy Biswas, Evren Korpeoglu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fashion retrieval often requires satisfying multiple attributes at once, such as category, color, pattern, and demographic. Monolithic embeddings mix these signals into a single vector, making attribute-specific control difficult at retrieval time. Many existing semantic-ID methods provide discrete item codes, but these codes are typically optimized as item-level or residual addresses and do not expose named, independently controllable attribute slots.
We introduce MM-slotgate, a multimodal slot encoder that factorizes Fashion-CLIP text and image embeddings into four named attribute slots. Each slot learns its own text-image gate, so visually grounded attributes such as color and pattern can rely more on image evidence, while taxonomy-oriented attributes such as category and demographic can remain more text-driven.
On H&M, using a combined slot-similarity and slot-logit retrieval score, MM-slotgate achieves 0.7566 macro ConstraintSatisfied@10, outperforming equal-weight multimodal fusion (0.7142) and fCLIP text-only retrieval (0.4755). The largest gain is on color, which improves from 0.321 to 0.889 (+0.568 absolute), as the learned color gate assigns 57.4% weight to image evidence. The learned gates are interpretable without modality supervision: color is image-leaning, category is text-leaning, and pattern and demographic lie near the middle.
The resulting slots also remain controllable: linear probes show no measured excess leakage beyond the label-correlation baseline, and quantized slot codes support targeted intervention, including a 15.3x lift for color. These results suggest that controllable fashion retrieval benefits from typed, attribute-conditioned multimodal slots rather than either a single global embedding or opaque item-level semantic IDs.

---


### 35. [Prof-K: Probabilistic One-Pass Filtering for Efficient Top-k Selection](https://arxiv.org/abs/2608.12573)

**<font color=#1a73e8>作者：</font>** Tadeusz Dziarmaga, Witold Sikora, Łukasz Struski 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Top-k selection is a fundamental computational primitive with applications spanning databases, information retrieval, signal processing, and modern machine learning workloads, including sparse activations and attention pruning. As data sizes grow, existing approaches become inefficient: exact methods incur high memory and compute overhead, while approximate methods often rely on brittle heuristics that degrade under adversarial or heavy-tailed inputs. In this paper, we introduce Prof-K, a fast, scalable, and distribution-agnostic top-k algorithm with probabilistic correctness guarantees. Prof-K performs a single-pass filtering procedure: a small random sample estimates an adaptive threshold, the N input elements are streamed once into a compact buffer, and an exact top-k routine on this buffer recovers the true top-k elements with probability at least 1 - $\epsilon$, where $\epsilon$ > 0 is user specified. We derive high-probability guarantees for correctness and buffer size, together with an approximately optimal sample size that minimizes overhead as a function of N and k. Empirically, Prof-K achieves 1.5x-10x speedups over the highly optimized PyTorch topk and recent RadiK implementations, with the largest gains in the large-scale, small-to-moderate-k regime where prior methods struggle most. Unlike previous approaches, these guarantees hold independently of the input distribution, ensuring robustness to adversarial settings. By relaxing the recall target (e.g., recovering 95% of the true top-k values), Prof-K additionally provides a principled accuracy-speed trade-off. We further demonstrate its impact on training BatchTopK Sparse Autoencoders (SAEs), where top-k selection constitutes a significant portion of the training cost.

---


### 36. [InvisIto: Weaving Unobtrusive Infrared Markers for Ubiquitous Textile Interaction](https://arxiv.org/abs/2608.12580)

**<font color=#1a73e8>作者：</font>** Hsuanling Lee, Hal Sugiyama, Tian Min 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Textiles are increasingly explored as media for interacting with digital information. However, many of the existing approaches rely on visible tags, printed overlays, or electronic modules that compromise the fabric's aesthetic and tactile qualities. To address this, we present InvisIto, a method for weaving visually unobtrusive yet machine-readable infrared markers directly into fabrics using near-infrared (NIR)-absorbing yarns. Although these yarns look similar to standard fibers in ambient light, they produce strong contrast in NIR imaging. Our method includes: (1) a design tool that helps users easily embed infrared markers into weaving drafts, (2) five disguising strategies that further reduce marker visibility under ambient light, and (3) a camera-based detection pipeline for decoding and tracking the woven markers. InvisIto supports both woven QR codes for data encoding and woven ArUco markers for binary input and deformation tracking. We demonstrate applications across hand weaving, Jacquard weaving, and industrial fabrication, showing that InvisIto supports scalable interaction and fabrication from bespoke artifacts to mass production.

---


### 37. [Represent, Then Generate: Multimodal-Conditioned Time-Series Generation under Irregular Missingness](https://arxiv.org/abs/2608.12592)

**<font color=#1a73e8>作者：</font>** Haochen Zhang, Jiaheng Guo, Yu-Chao Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Continuous physiological time series underpin modern clinical monitoring, yet many of the most informative signals are invasive, expensive, or simply unavailable for a given patient. Conditional generation offers a remedy: an absent signal can be synthesized from co-recorded signals and routine clinical variables. Existing generators, however, are built around a single conditioning modality and degrade when forced to handle the heterogeneous, irregularly missing mix of time-variant signals and static covariates seen in practice. We propose ReCoGen (Represent Conditions, then Generate), a two-stage framework that decouples multimodal condition representation from target generation. Stage I trains one masked autoencoder per modality, distilling each time-variant condition into a compact and missingness-tolerant token sequence. Stage II trains a flow-matching generator that fuses these tokens with static conditions to synthesize the target signal. Across three physiological benchmarks, including continuous glucose monitoring on AI-READI and arterial blood pressure generation on MIMIC-III and MIMIC-IV, ReCoGen attains the best downstream utility on all sixteen (dataset, task, metric) settings, surpassing six representative conditional generators; on thirteen of them its utility also reaches or exceeds the utility measured on the real signal, a reference we read as an approximate anchor rather than a ceiling. Ablations trace the gains to the conditioning path: learnable cross-attention over the frozen per-modality encoders, and a dual token-plus-AdaLN route for the static conditions. ReCoGen thus turns routinely collected signals into informative surrogates for invasive or unavailable ones, a step toward less invasive, lower-cost continuous clinical monitoring.

---


### 38. [DiG-bench: Discovery in Games](https://arxiv.org/abs/2608.12593)

**<font color=#1a73e8>作者：</font>** Ruairidh M. Battleday, Kai Sandbrink, Jimi Cullen-Drohan 等 16 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Discovery---formulating novel generalizations---is a central part of the scientific process. Despite its importance, there is a gap in the current AI benchmark landscape, with few benchmarks directly probing the capacity for discovering new knowledge with experimentation in controlled environments where the objective is unknown. To address this gap, we release a new benchmark: DiG-bench (Discovery in Games). DiG-bench consists of a set of 70 independent games. Each game is encoded as a short string and has unique transformation rules that must be discovered through interaction and experimentation. The levels of the game present a series of challenges to test whether the rules have been discovered, where the win conditions for each level are also unknown. We provide games at seven tiers of difficulty for AI agents. The lowest tier is routinely solvable by multiple models, while the highest tier challenges the best models in agentic harnesses. All 70 games were solved by at least one human on first attempt. A subset of 21 games is released publicly, and the remainder is held private for secure evaluation.

---


### 39. [Intensional Anaphora](https://arxiv.org/abs/2608.12598)

**<font color=#1a73e8>作者：</font>** Ezra Keshet, Steven Abney  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Intensional operators are often treated as quantifiers over possible worlds, parallel to the treatment of determiners as quantifiers over individuals. Yet individuals introduced in intensional contexts cannot serve as antecedents to later pronouns as easily as those introduced in merely quantificational contexts. For instance, "Everyone is eating a cheeseburger" may be followed by "They are large", where "they" refers to the cheeseburgers being eaten. However, as Stone (1999) points out, the similar "Andrea might be eating a cheeseburger" does not support later anaphoric references such as "It is large" or "They are large". Stone (1999), Stone and Hardt (1999), and Brasoveanu (2010) address this by requiring a pronoun's value (its referents) to exist in the world of evaluation, ruling out anaphora from non-veridical intensional contexts. We show, however, both cases where such anaphora is disallowed even when the pronoun's referents clearly exist and cases where it is allowed even though they might not exist. We argue that intensional anaphora is best captured using a description-based rather than value-based account. A pronoun presupposes that its corresponding antecedent description is instantiated in each world of the context set. Thus, there must be a cheeseburger being eaten by Andrea in every candidate world for "It is large" to be felicitous after "Andrea might be eating a cheeseburger". We implement our proposal via a new logic, building on Keshet (2018) and Abney and Keshet (2022), called Plural Intensional Presuppositional predicate calculus (PIP). Each PIP formula translates directly into standard first-order predicate calculus with set abstraction, providing a classical foundation for this work.

---


### 40. [PseudoMapLabeler: Confidence-Aware Pseudo-Label Generation for Semi-Supervised Online Mapping](https://arxiv.org/abs/2608.12600)

**<font color=#1a73e8>作者：</font>** Chikao Tsuchiya, Dhaval Bhanderi, David Ilstrup 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A critical challenge in deploying online HD map construction systems to real-world scenarios is the scarcity of labeled training data, which limits model generalization in diverse environments. To address this limitation, we propose a teacher-student semi-supervised learning (SSL) framework that generates high-quality pseudo-labels from unlabeled data through confidence-aware map refinement. Our approach first trains a teacher model on limited labeled data, then leverages Beta-distribution-based confidence maps to assess the reliability of predicted map elements across temporal observations. Unlike conventional filtering methods that discard entire elements, we introduce a spatial clipping technique that selectively preserves high-confidence regions while removing unreliable segments. The refined map elements serve as map priors that improve the teacher model's prediction accuracy on unlabeled data in a second pass. These enhanced predictions become pseudo-labels for training a student model from scratch, followed by fine-tuning on the original labeled data. Experimental results on the nuScenes dataset demonstrate that our teacher-student framework with refined pseudo-labels improves performance by +6.1 mAP under a low-label regime compared to training on labeled data alone, offering a practical solution to the labeled data scarcity problem in online HD map construction.

---


### 41. [Surprise2Refine: Axis-Centered Exploration-To-Refinement for Agent-Assisted Creative Scaffolding](https://arxiv.org/abs/2608.12605)

**<font color=#1a73e8>作者：</font>** Yuzhe You, Gromit Yeuk-Yin Chan, Shunan Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Designers require different design spaces across creative stages: broad during exploration, and targeted during refinement. Yet existing agent-driven tools assume a fixed or continuously expanding space, leaving designers to manage and navigate it themselves. Informed by a formative study with five designers, we propose an axis-centered workflow that adaptively broadens and narrows the design space to support structured exploration and refinement. We implemented this workflow in Surprise2Refine, a prototype that allows users to build and reshape an nxn design space through a set of axis-centered interactions as their creative intent evolves. A within-subjects study with 14 designers shows that Surprise2Refine enhances users' sense of control, supports tracking of scaffolding paths, and improves the perceived creativity of design outcomes. We further distill design insights to guide future agent-assisted tools for creative scaffolding.

---


### 42. [The Boolean Power of ReLU](https://arxiv.org/abs/2608.12617)

**<font color=#1a73e8>作者：</font>** Pablo Barceló, Floris Geerts, Matthias Lanzinger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We prove that, on finite simple undirected graphs equipped with a single Boolean node feature, the Boolean queries expressible in $\Sigma$-MPLang, for any collection $\Sigma$ of eventually constant activation functions and with arbitrary real coefficients, form a strict subclass of the Boolean queries expressible in ReLU-MPLang. We thereby settle a recently posed open problem: whether ReLU-MPLang is more powerful than trReLU-MPLang when it comes to Boolean queries. In particular, this implies that ReLU-GNNs are strictly more expressive than {TrReLU,id}-GNNs with respect to Boolean queries on Boolean-featured graphs.

---


### 43. [Structure-preserving uncertainty quantification for GENERIC dynamics](https://arxiv.org/abs/2608.12624)

**<font color=#1a73e8>作者：</font>** Zequn He, Celia Reina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structure-preserving machine learning embeds physical structure directly into model architectures, yet uncertainty quantification (UQ) for such hard-constrained models remains limited because standard UQ methods may violate the encoded admissibility conditions, require architectural modifications, or impose substantial computational costs. In this work, we propose Structure-Preserving Epistemic Neural Networks (S-PENNs), a general framework for UQ in scientific machine learning models with hard architectural constraints, and instantiate it for GENERIC (General Equation for Non-Equilibrium Reversible-Irreversible Coupling) dynamics. S-PENNs preserve the structural constraints of a pretrained model by attaching lightweight epinets to its constrained components, ensuring that every sampled realization remains physically admissible by construction. When applied to GENERIC dynamics, such a proposed framework yields thermodynamically consistent rollouts that preserve the first and second laws. Furthermore, we combine S-PENNs with split conformal prediction as a post-hoc calibration method to produce prediction intervals with finite-sample marginal coverage guarantees. We validate S-PENNs on three numerical examples: a harmonic oscillator coupled to a heat bath and an idealized chemical motor, both governed by ODEs, and a one-dimensional viscoplastic model governed by PDEs. Across all three examples, S-PENNs produce thermodynamically consistent stochastic realizations and well-calibrated prediction intervals while reducing the computational cost by about one to three orders of magnitude compared to deep ensembles. Although the present study focuses on GENERIC dynamics, S-PENNs can be extended more broadly to scientific machine learning models in computational mechanics with either hard or soft constraints.

---


### 44. [CAKE: Compiler-Agent Co-Design for Frontier Kernel Evolution](https://arxiv.org/abs/2608.12629)

**<font color=#1a73e8>作者：</font>** Zihao Ye, Yingyi Huang, Hongyi Jin 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> GPU kernel agents and GPU programming languages have advanced separately, leaving expert kernels difficult to reproduce. Agents usually treat the compiler as a fixed black box and receive only errors, correctness outcomes, and timing, while existing DSLs either hide critical scheduling decisions or expose them through difficult layout abstractions. We present CAKE, a compiler-agent co-design in which agents author CAKE IR, a typed, hardware-explicit schedule representation. CAKE exposes warp roles, memory movement, synchronization, and pipelines while supporting verification, cost modeling, and localized diagnostics. The harness itself evolves: recurring failures become verifier rules, IR primitives, model calibrations, and reusable optimization tactics. In matched implementation-hidden Flash-KMeans clean starts on B200, the best CAKE IR candidate at an 80-million-token budget runs at 1.144x the tuned FlashML baseline, compared with 0.928x for direct CUDA/PTX. Beyond this benchmark, agent-generated Kimi Delta Attention achieves a 2.05x geometric-mean speedup over official FlashKDA and passes end-to-end serving validation. Dispatcher-backed KNN and KMeans improve performance by 1.42x to 2.12x across more than 400 shapes, and four kernel changes are available as upstream PRs. CAKE targets NVIDIA GPUs from Ampere through Blackwell and separates single-shape evolution from library generalization and dispatch.

---


### 45. [Interpretable Causal Discovery via Causal-Effect Constraints](https://arxiv.org/abs/2608.12640)

**<font color=#1a73e8>作者：</font>** Cixuan Zhang, Guy Van den Broeck, Benjie Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Causal discovery aims to uncover the underlying causal relationships given data generated from a system. The goal, however, is not merely to predict causal edges given data, but also to be able to interpret and explain either observed or hypothesized phenomena, such as a particularly large causal effect. We consider this task of conditional causal discovery and cast it as a Bayesian inference problem, in which we target the posterior over causal graphs and parameters conditional on an event such as a causal-effect constraint. Unfortunately, this poses a computational challenge: existing approaches to Bayesian causal discovery struggle when the event has small posterior mass. To address this, we adapt rare-event estimation techniques to perform inference the joint graph-parameter space. Our method gradually drives a particle population toward the constrained region while maintaining samples that approximate the conditional posterior. Empirical evaluation on synthetic graphs validates the accuracy of our approach at small and large scales, and we show in a case study on the Sachs protein dataset how our method can be used to aid scientific exploration by providing pathway-level summaries.

---


### 46. [Training Under Challenge: Executable Certificates and Challenge-Closed Optimality for Neural Networks](https://arxiv.org/abs/2608.12655)

**<font color=#1a73e8>作者：</font>** Farhang Yeganegi, Arian Eamaz, Mojtaba Soltanalian  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A flat training curve does not reveal whether a neural network has reached a global optimum, is locally trapped, is representation-limited, or is mismatched to its trainer. We introduce Training Under Challenge, an executable-certificate framework in which predeclared, architecture-valid procedures construct complete alternatives in the same certified class and reevaluate the same objective. Any lower-valued candidate is a replayable witness that lower-bounds the checkpoint's empirical global-optimality gap. Passing a finite suite is only suite-relative; global-gap conclusions require a separately justified coverage mechanism. We define a resource-indexed challenge-power modulus that characterizes the largest gap compatible with passage. For squared loss, current block-decrease operators make coverage checkable and yield uniform and realized-residual bounds. We prove the converse frontier: without coverage, a first-order ReLU trainer can reach infinitely many exact conditional head optima while converging to a non-global point. On a channel-gated ResNet-18 distillation problem with known optimum, eight internal challenges cover all 240 audited output directions, and realized-residual bounds lie within factors of 1.74--3.02 of the true gap. Paired predictive certificates separate decoder under-use from representation insufficiency, while quantized-denoising studies demonstrate diagnosis, repair, and current-state recertification.

---


### 47. [General Probabilities of Causation with Causal Knowledge](https://arxiv.org/abs/2608.12657)

**<font color=#1a73e8>作者：</font>** Xin Shu, Zhen Lei, Ang Li  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Probabilities of causation (PoCs) characterize individual causal responses that cannot be directly observed and therefore generally require partial identification. Tian and Pearl first derived theoretically sharp bounds for binary PoCs, including the probability of necessity (PN), the probability of sufficiency (PS), and the probability of necessity and sufficiency (PNS). Mueller et al. subsequently tightened the bounds for binary PNS by incorporating causal information encoded in covariates and mediators. More recently, Li and Pearl, as well as Shu et al., extended PoCs to multivalued settings and derived corresponding theoretical bounds. These developments naturally raise the question of whether additional causal knowledge can further tighten the bounds in multivalued settings. This paper addresses this question by deriving tighter bounds for multivalued PoCs through the incorporation of causal information encoded in covariates and mediators. We illustrate the theoretical results with toy examples, while simulation studies further demonstrate that the proposed bounds are tighter than existing nonbinary bounds.

---


### 48. [Inference-Time Orthogonal Seeding Enables Geometry-Aligned 3D Organ Segmentation for Slice-Propagation Methods](https://arxiv.org/abs/2608.12658)

**<font color=#1a73e8>作者：</font>** Md Rakibul Haque, Tushar Kataria, Shireen Y. Elhabian  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dense voxel-level annotation remains a major bottleneck in 3D medical image segmentation. Single-slice propagation methods such as Sli2Vol reduce this burden by propagating one annotated seed slice through a volume using label-free registration. However, axial-only propagation accumulates errors with distance from the seed, especially in surface-distance metrics, because it ignores coronal and sagittal evidence and therefore underuses the 3D information available in CT/MRI volumes. To better leverage volumetric geometry, we study how key training and inference choices affect slice-propagation models, including single-axis versus multi-axis label-free registration, single-seed versus multi-seed propagation, and orthogonal seed configurations. Instead of propagating from a single axial seed, we use three orthogonal seeds---one axial, one coronal, and one sagittal---and fuse their propagated labels with a simple label-free rule. Our results show that the training paradigm has limited impact: an axially trained network applied to off-axis seeds captures nearly all the improvement, while explicit three-axis training adds little. Instead, performance is driven by inference-time seed geometry, especially orthogonality rather than the number of annotated slices, as a budget-matched three-axial control provides no benefit and can even degrade performance. On a multi-organ CT cohort, orthogonal seeding with the axial Sli2Vol backbone improves Dice by 21.9%, Normalized Surface Dice by 25.5%, and reduces Average Hausdorff Distance by 53.5% over the single-axis baseline.

---


### 49. [Demand Transfer Estimation at Scale via Restricted Logit Modeling](https://arxiv.org/abs/2608.12680)

**<font color=#1a73e8>作者：</font>** Lakshya Garg, Deep Narayan Mishra, Swapnil Yadav 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Item demand forecasting is an integral component of store assortment optimization. Existing literature focuses on learning a suitable customer choice model and using this model to determine the value of an objective function (i.e. expected demand) with respect to an assortment proposal. However, for large item universe with many categories, this approach can prove inefficient, needing a separate demand forecast for every possible item assortment. An alternate approach exists whereby we combine the efficiency of forecasting item demand independently, while at the same time applying adjustments to the independent forecasts that account for the relations between item demand and the availability of other similar items on the shelf.
Central to this approach is the estimation of Demand Transfer (DT) coefficients. These DT coefficients represent the percent of a particular target item's (item that the customer walked in the store to buy) demand that is redirected to each other item in the universe should the target item be removed from the shelf. We introduce an approach that allows us to compute these DT coefficients on large item universes (assortments having 1 million+ items). Experiments on data as well as historical transaction data for multiple locations within categories demonstrate that when certain reasonable assumptions about substitution behavior are satisfied, our procedure is able to accurately estimate underlying DT coefficients and lead to improvements in demand forecasting.

---


### 50. [Finding the Needle in a Haystack: Test-Time Analog Circuit Representation Adaptation for Bayesian Optimization](https://arxiv.org/abs/2608.12687)

**<font color=#1a73e8>作者：</font>** Fin Amin, Sounak Dutta, Paul D. Franzon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Bayesian optimization (BO) is a sample-efficient framework for analog circuit topology search, where evaluating each candidate topology can require costly simulation. However, representation-based BO methods typically treat circuit embeddings as fixed after encoder training. This creates a mismatch between representation learning and optimization: embeddings learned to encode or reconstruct circuit structure are not necessarily organized according to the figure of merit (FoM) being optimized. This paper introduces Test-Time Analog Representation Adaptation for Bayesian Optimization (TTARO), an online deep-kernel BO framework that adapts circuit representations throughout the search process. Starting from pretrained circuit embeddings, TTARO jointly learns a nonlinear feature transformation and a Gaussian-process surrogate using the FoM labels of the circuits evaluated so far. Following each new evaluation, TTARO updates the representation and surrogate before selecting the next candidate. We compare TTARO with conventional Gaussian Process-based BO over fixed embeddings and with Deep Kernel Learning (DKL), which learns the representation only from the initial evaluated designs and keeps it fixed throughout the remainder of the search. By continually incorporating newly observed FoM labels into representation learning, TTARO aligns the search space with the optimization objective as BO progresses. In our experiments, TTARO reduces regret AUC by 15.2% on average relative to BO and by 20.7% relative to DKL across 40 encoder/kernel/acquisition settings, outperforming prior art in most settings with reductions as large as 46.7%.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-199](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
