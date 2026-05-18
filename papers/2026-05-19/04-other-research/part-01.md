# 📦 其他研究 | 2026年05月19日

> 本类共 **234** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

---

### 1. [DeepSlide: From Artifacts to Presentation Delivery](https://arxiv.org/abs/2605.15202)

**<font color=#1a73e8>作者：</font>** Ming Yang, Zhiwei Zhang, Jiahang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Presentations are a primary medium for scholarly communication, yet most AI slide generators optimize the artifact (a visually plausible deck) while under-optimizing the delivery process (pacing, narrative, and presentation preparation). We present DeepSlide, a human-in-the-loop multi-agent system that supports preparing the full presentation process, from requirement elicitation and time-budgeted narrative planning, to evidence-grounded slide--script generation, attention augmentation, and rehearsal support. DeepSlide integrates (i) a controllable logical-chain planner with per-node time budgets, (ii) a lightweight content-tree retriever for grounding, (iii) Markov-style sequential rendering with style inheritance, and (iv) sandboxed execution with minimal repair to ensure renderability. We further introduce a dual-scoreboard benchmark that cleanly separates static artifact quality from dynamic delivery excellence. Across 20 domains and diverse audience profiles, DeepSlide matches strong baselines on artifact quality while consistently achieving larger gains on delivery metrics, improving narrative flow, pacing precision, and slide--script synergy with clearer attention guidance.

---


### 2. [Does Theory of Mind Improvement Really Benefit Human-AI Interactions? Empirical Findings from Interactive Evaluations](https://arxiv.org/abs/2605.15205)

**<font color=#1a73e8>作者：</font>** Nanxu Gong, Zixin Chen, Haotian Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Improving the Theory of Mind (ToM) capability of Large Language Models (LLMs) is crucial for effective social interactions between these AI models and humans. However, the existing benchmarks often measure ToM capability improvement through story-reading, multiple-choice questions from a third-person perspective, while ignoring the first-person, dynamic, and open-ended nature of human-AI (HAI) interactions. To directly examine how ToM improvement techniques benefit HAI interactions, we first proposed the new paradigm of interactive ToM evaluation with both perspective and metric shifts. Next, following the paradigm, we conducted a systematic study of four representative ToM enhancement techniques using both four real-world datasets and a user study, covering both goal-oriented tasks (e.g., coding, math) and experience-oriented tasks (e.g., counseling). Our findings reveal that improvements on static benchmarks do not always translate to better performance in dynamic HAI interactions. This paper offers critical insights into ToM evaluation, showing the necessity of interaction-based assessments in developing next-generation, socially aware LLMs for HAI symbiosis.

---


### 3. [SkillSmith: Compiling Agent Skills into Boundary-Guided Runtime Interfaces](https://arxiv.org/abs/2605.15215)

**<font color=#1a73e8>作者：</font>** Duling Xu, Zheng Chen, Zaifeng Pan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, skills have been widely adopted in large language model (LLM)-based agent systems across various domains. In existing frameworks, skills are typically injected into the agent reasoning loop as contextual guidance once matched to a runtime task, enabling specialized task-solving capabilities. We find that this execution paradigm introduces two major sources of redundancy: irrelevant context injection and repeated skill-specific reasoning and planning. To this end, we propose SkillSmith, a boundary-first compiler-runtime framework that compiles skill packages offline into minimal executable interfaces. By extracting fine-grained operational boundaries from skills, SkillSmith enables agents to dynamically access and execute only the relevant components at runtime, thereby minimizing unnecessary context injection and redundant reasoning overhead. In the evaluation on SkillsBench benchmark, SkillSmith reduces solve-stage token usage by 57.44%, thinking iterations by 42.99%, solve time by 50.57% (2.02x faster), and token-proportional monetary cost by 57.44% compared with using raw-skills. Moreover, compiled artifacts produced by a stronger model can be reused by a smaller or more efficient runtime model, improving task accuracy in cases where raw skill interpretation fails. The source code and data are available at this https URL.

---


### 4. [CAX-Agent: A Lightweight Agent Harness for Reliable APDL Automation](https://arxiv.org/abs/2605.15218)

**<font color=#1a73e8>作者：</font>** Chenying Lin, Yichen Hai, Yi He 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models deployed for MAPDL finite-element simulation face practical reliability challenges: without structured execution control, tool encapsulation, and fault recovery, outputs may be inconsistent and task failures are common. The Agent Harness paradigm addresses this by inserting domain-specific orchestration middleware that manages tool lifecycles, workflow state, and recovery escalation. This paper presents the architecture of CAX-Agent, a lightweight agent harness purpose-built for MAPDL automation, and empirically evaluates one of its core components -- the recovery this http URL-Agent organizes execution into three layers -- LLM service, agent harness, and solver backend -- with a recovery ladder that escalates from deterministic rule patching through model-driven regeneration to context enrichment and human intervention. We evaluate three recovery strategies (no_recovery, rule_only, and model_only) on 50 standard structural benchmarks with three repeated runs per strategy (450 case-runs total). Two independent human raters score task completion under blind conditions; inter-rater agreement is strong (quadratic weighted Cohen's kappa = 0.84, 96 percent of score pairs within one point). Model_only achieves the best completion rate (0.9267), task score (3.59/4), total score (9.16/10), and zero-intervention rate (0.84), outperforming rule_only (0.7733, 3.17/4, 7.03/10, 0.00) and no_recovery (0.6933, 2.74/4, 5.60/10, 0.00) with large effect sizes (Cliff's delta = 0.81-0.87). The benchmark uses deliberately simple geometries to isolate recovery-policy effects; we discuss the scope of these findings and directions for broader validation.

---


### 5. [NOVA: Fundamental Limits of Knowledge Discovery Through AI](https://arxiv.org/abs/2605.15219)

**<font color=#1a73e8>作者：</font>** Salman Avestimehr, Ken Duffy, Muriel Médard  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can AI systems discover genuinely new knowledge through iterative self improvement, and if so, at what cost? We introduce the NOVA framework, which models the common ``generate, verify, accumulate, retrain'' loop as an adaptive sampling process over a knowledge space. We identify sufficient conditions under which accumulated genuine knowledge eventually covers a finite domain, and show how their violations produce distinct failure modes: contamination, forgetting, exploration failure, and acceptance failure. We then analyze imperfect verification and identify a contamination trap: as easy-to-find knowledge is exhausted, the model mass assigned to new valid artifacts shrinks, so even small false-positive rates can cause invalid artifacts to enter the knowledge base faster than genuine discoveries. We clarify that Good--Turing estimation is a local batch-diversity diagnostic, not an estimator of the historically undiscovered valid mass that governs long-term discovery. Under a separate tail-equivalence assumption relating the model's effective discovery distribution to a Zipf law with exponent $\alpha>1$, we prove that the cumulative generation cost required to obtain $D$ distinct genuine discoveries satisfies $R_{\mathrm{cum}}(D)=\Theta(c_{\mathrm{gen}}D^\alpha)$, where $c_{\mathrm{gen}}$ is the per-candidate generation cost. This scaling law quantifies asymptotic diminishing returns as the discovery frontier advances. Finally, we formalize human amplification through guidance, generation, and verification, explaining why expert input is most valuable near autonomous exploration barriers.

---


### 6. [Always Learning, Always Mixing: Efficient and Simple Data Mixing All The Time](https://arxiv.org/abs/2605.15220)

**<font color=#1a73e8>作者：</font>** Michael Y. Hu, Apurva Gandhi, Kyunghyun Cho 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data mixing decides how to combine different sources or types of data and is a consequential problem throughout language model training. In pretraining, data composition is a key determinant of model quality; in continual learning and adaptation, it governs what is retained and acquired. Yet existing data mixing methods address only one phase of this lifecycle at a time: some require smaller proxy models tied to a single training phase, others assume a fixed domain set, and continual learning lacks principled guidance altogether. We argue that data mixing is fundamentally an online decision making problem -- one that recurs throughout training and demands a single, unified solution. We introduce OP-Mix (On-Policy Mix), a data mixing algorithm that operates across the entire language model training lifecycle. Our main insight is that candidate data mixtures can be cheaply simulated by interpolating between low-rank adapters trained directly on the current model, eliminating separate proxy models and ensuring the search is always grounded in the model's actual learning dynamics. Across pretraining, continual midtraining, and continual instruction tuning, OP-Mix consistently finds near-optimal mixtures while using a fraction of the compute of the baselines. In pretraining, OP-Mix improves upon training without mixing by 6.3% in average perplexity. For continual learning, OP-Mix matches the performance of both retraining and on-policy distillation while using 66% and 95% less overall compute, respectively. OP-Mix suggests a different view of language model training: not a sequence of distinct phases, but a single continuous process of learning from data.

---


### 7. [NIMO Controller: a self-driving laboratory orchestrator based on the Model Context Protocol](https://arxiv.org/abs/2605.15227)

**<font color=#1a73e8>作者：</font>** Naruki Yoshikawa, Ryo Tamura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-driving laboratories (SDLs) have attracted increasing attention as a means of accelerating scientific discovery; however, developing SDL software remains technically demanding. To improve accessibility, orchestration software frameworks have been proposed to coordinate SDL components. Nevertheless, existing frameworks are primarily designed for human interaction and do not provide standardized interfaces suitable for AI agents. In this work, we propose an SDL software architecture based on the Model Context Protocol (MCP), in which all SDL functionalities are exposed through MCP servers. Following this design principle, we introduce an MCP-based SDL orchestrator, named NIMO Controller. It provides a visual programming interface automatically generated through MCP-based tool discovery, allowing human users to design experimental workflows without writing code. The same MCP backend can also be accessed by AI agents, providing a unified interface for both human users and AI agents. We demonstrate the proposed system through a case study on a color-matching SDL. The results validate the usability of the proposed MCP-based SDL architecture.

---


### 8. [Mask-Morph Graph U-Net: A Generalisable Mesh-Based Surrogate for Crashworthiness Field Prediction under Large Geometric Variation](https://arxiv.org/abs/2605.15231)

**<font color=#1a73e8>作者：</font>** Haoran Li, Tobias Lehrer, Yingxue Zhao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Nonlinear finite element crash simulations are accurate but computationally expensive, limiting their use in iterative design optimisation. Machine-learning surrogate models based on graph neural networks (GNNs) offer a faster alternative. Message-passing GNNs are widely used for mesh simulation, and their shared node and edge update functions are relatively generalisable across varying graph structures. By contrast, non-shareable edge-specific aggregation layers can capture nonlinear relationships more accurately but usually require fixed graph connectivity, which limits generalisability. This paper presents Mask-Morph Graph U-Net (MMGUNet), a practical approach to addressing the limitation of hierarchical Graph U-Net architectures that use edge-specific downsampling and upsampling layers. Fixed coarse graph connectivity is required for edge-specific layers. To retain this while improving spatial correspondence, the proposed method morphs the coarsened graph hierarchy to each input mesh using feature-aligned barycentric parameterisation before constructing cross-graph edges. It further applies node masking during supervised pretraining, followed by parameter-efficient fine-tuning in which high-parameter edge-specific layers are frozen. The proposed approach is evaluated in in-distribution, out-of-distribution, and cross-component transfer settings using mean Euclidean distance and maximum intrusion percentage error. Results show that coarse-graph morphing improves test accuracy relative to a fixed-coarse-graph baseline, while masked supervised pretraining reduces the train-test discrepancy and improves data efficiency during transfer. The proposed model also achieves lower prediction error compared with external baselines. These results demonstrate a practical route toward reusable, data-efficient mesh-based surrogate modelling for crashworthiness design exploration.

---


### 9. [Logical Grammar Induction via Graph Kolmogorov Complexity: A Neuro-Symbolic Framework for Self-Healing Clinical Data Integrity](https://arxiv.org/abs/2605.15242)

**<font color=#1a73e8>作者：</font>** Abolfazl Zarghani, Amir Malekesfandiari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The reliability of Healthcare Information Systems (HIS) is frequently compromised by human-induced data entry errors, which existing statistical anomaly detection methods fail to distinguish from legitimate clinical extremes. This paper proposes Logic-GNN, a novel neuro-symbolic framework that treats clinical records as a structured ``private language'' governed by latent logical games. By integrating Temporal Graph Neural Networks (TGNN) with Graph Kolmogorov Complexity, we induce a symbolic grammar that represents the underlying logic of medical interactions. We define anomalies as ``grammatical violations'' that cause a significant expansion in the Minimum Description Length (MDL) of the clinical graph. Evaluated on the Sina System dataset (2M+ records), Logic-GNN achieves an F1-score of 0.94, outperforming state-of-the-art baselines by 12\% in distinguishing between life-threatening medical outliers and data corruption. Our approach introduces a self-healing mechanism that suggests logical corrections to maintain data integrity in real-time HIS environments.

---


### 10. [Reading the Cell, Designing the Cure: Perturbation-Conditioned Molecular Diffusion for Function-Oriented Drug Design](https://arxiv.org/abs/2605.15243)

**<font color=#1a73e8>作者：</font>** Ziyu Xu, Zijian Zhang, Liang Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> When reliable target structures are unavailable at scale or phenotypes arise from dysregulated pathways, transcriptomic perturbations provide a system-level functional readout for drug action. In this work, we formalize \emph{Transcriptome-based Drug Design (TBDD)} as a generative inverse problem: designing drug molecules conditioned on desired transcriptomic state transitions. We analyze the inherently ill-posed nature of this task, which is further complicated by the profound domain gap between biology and chemistry and by the sparsity of transcriptomic signals. To address these challenges, we propose \textbf{\themodel{}} (A \textbf{C}ell\textbf{U}lar \textbf{R}esponse \textbf{E}ngine), a multi-resolution transcriptome-guided diffusion framework. \themodel{} features a specialized \textbf{Transcriptome Perturbation Functional Feature Extractor (TFE)} that (1) distills function-oriented perturbation embeddings from pre/post states, (2) aligns these signatures to dual chemical views to bridge the cross-modal gap, and (3) performs heterogeneity-aware aggregation to extract robust state-specific signals from noisy transcriptomic data. Extensive evaluations on both standard benchmarks and rigorous out-of-distribution protocols demonstrate that \themodel{} consistently outperforms strong baselines in structural quality and functional consistency. Furthermore, we validate its practical utility via a zero-shot gene-inhibitor design task, highlighting the potential of phenotype-driven generative discovery.

---


### 11. [Privacy Evaluation of Generative Models for Trajectory Generation](https://arxiv.org/abs/2605.15246)

**<font color=#1a73e8>作者：</font>** Stavros Bouras, Ioannis Kontopoulos, Chiara Pugliese 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Trajectory data is fundamental to modern urban intelligence, yet its sensitivity raises significant privacy concerns. Generative models such as Generative Adversarial Networks, Variational Autoencoders, and Diffusion Models have been developed to generate realistic synthetic trajectory data by capturing underlying spatiotemporal distributions and mobility patterns. Although these models are often assumed to preserve privacy due to their generative nature, this assumption does not necessarily hold. In this work, we investigate the intersection of generative trajectory modeling and privacy evaluation. By identifying applicable empirical methods for assessing privacy preservation in trajectory generation tasks, we demonstrate a significant gap in the evaluation of privacy for generative trajectory models. Motivated by this gap, we implement Membership Inference Attacks against representative models, demonstrating the feasibility of using such empirical privacy evaluation methods and showing that their generative nature does not eliminate privacy risks.

---


### 12. [Enabling Adversarial Robustness in AI Models through Kubeflow MLOps](https://arxiv.org/abs/2605.15249)

**<font color=#1a73e8>作者：</font>** Stavros Bouras, Ioannis Korontanis, Antonios Makris 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI models are increasingly deployed in cloud-native environments to support scalable and automated services. However, while platforms such as Kubernetes provide strong infrastructure orchestration, security mechanisms specifically designed to protect deployed AI models remain limited. This paper presents security measures for AI models deployed in Kubernetes clusters. The proposed architecture integrates Kubeflow-based MLOps to automatically detect adversarial attacks during the inference phase and trigger defense mechanisms that preserve the model's accuracy and reliability. Specifically, a Fast Gradient Sign Method (FGSM) attack is applied at inference time, and a Projected Gradient Descent (PGD)-based adversarial training defense is automatically deployed when a degradation in accuracy is detected. The experimental results indicate that the deployed defense robustifies the model, significantly recovering accuracy relative to the degradation caused by the attack.

---


### 13. [PDRNN: Modular Data-driven Pedestrian Dead Reckoning on Loosely Coupled Radio- and Inertial-Signalstreams](https://arxiv.org/abs/2605.15252)

**<font color=#1a73e8>作者：</font>** Peter Bauer, Andreas Porada, Felix Ott 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern pedestrian dead reckoning (PDR) systems rely on fusing noisy and biased estimates of position, velocity, and calibrated orientation derived from loosely coupled sensors to determine the current pose of a localized object. However, discrepancies in the sampling rates of sensor-specific estimation methods and unreliable transmission pose significant challenges. And traditional methods often fail to effectively fuse multimodal sensor data during dynamic movements characterized by high accelerations, velocities, and rapidly varying orientations. To address these limitations, we propose a simple recurrent neural network (RNN) architecture capable of implicitly forecasting asynchronous sensor data streams from diverse estimation methods along reference trajectories. The proposed approach introduces PDRNN, a modular hybrid AI-assisted PDR system that handles each component as an independent ensemble of machine learning (ML) models to estimate both key parameter means and variances. Separate ML-based models are employed to estimate orientation, (un)directed velocity or distance from acceleration and gyroscope data, with optional absolute positioning from synchronized radio systems such as 5G for stabilization. A final fusion model combines these outputs, position, velocity, and orientation, while using uncertainty estimates to enhance system robustness. The modular design allows individual components to be updated, fine-tuned, or replaced without affecting the entire system. Experiments on dynamic sports movement data show that PDRNN achieves superior accuracy and precision compared to classic and ML-based methods, effectively avoiding error accumulation common in black-box approaches. And PDRNN offers forecast capabilities and better component control despite increased system complexity.

---


### 14. [Position: Ideas Should be the Center of Machine Learning Research](https://arxiv.org/abs/2605.15253)

**<font color=#1a73e8>作者：</font>** Jairo Diaz-Rodriguez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning research increasingly bifurcates into two disconnected modes: benchmark-driven engineering that prioritizes metrics over understanding, and idealized theory that often fails to transfer to modern systems. In this position paper, we argue that the field focuses too heavily on these endpoints, neglecting the central scientific object: the idea. We propose an Ideas First framework in which ideas are valued for the behavioral signatures they predict in modern models, and these signatures are tested through tailored experiments designed to detect the relevant patterns rather than to win leaderboards. This shift not only bridges the gap between theory and practice but also promotes equity by removing the "complexity premium," enabling rigorous scientific contributions from researchers with modest computational, financial, and human resources. Ultimately, we advocate for a research culture centered on ideas, treating benchmarks and theorems as instruments for testing mechanistic hypotheses rather than as ends in themselves.

---


### 15. [Curriculum Learning of Physics-Informed Neural Networks based on Spatial Correlation](https://arxiv.org/abs/2605.15254)

**<font color=#1a73e8>作者：</font>** Xujia Chen, Xinyue Hu, Letian Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Physics-Informed Neural Networks (PINNs) combine deep learning with physical constraints for solving partial differential equations (PDEs), and are widely applied in fluid mechanics, heat transfer, and solid mechanics. However, PINN training still suffers from high-dimensional non-convex loss landscapes, imbalanced multiobjective constraints, and ineffective information propagation. Existing curriculum learning and causality-guided strategies improve training stability, but mainly focus on temporal or parametric progression, lacking explicit treatment of spatial information propagation and inter-region consistency. Moreover, they are not directly applicable to boundary value problems (BVPs) with strong spatial coupling. To address this issue, we propose a spatially correlated curriculum learning framework for PINNs. To the best of our knowledge, this is the first work to address PINN training difficulties from the perspective of spatial coupling among subregions. First, spatial causal weights guide information from near-boundary regions inward, reducing optimization failures and spurious convergence. Second, a low-frequency information bridge enforces pseudo-label-based consistency across spatially separated regions, suppressing global low-frequency drift. Third, a region-adaptive reweighting strategy adjusts subregion losses to reduce local residuals and recover high-frequency details. Experiments on PDE benchmarks show that, under comparable computational cost, the proposed method alleviates training failures and improves solution accuracy. The code is available at this https URL.

---


### 16. [Training on Documents About Monitoring Leads to CoT Obfuscation](https://arxiv.org/abs/2605.15257)

**<font color=#1a73e8>作者：</font>** Reilly Haskins, Bilal Chughtai, Joshua Engels  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) monitoring is one of the most promising tools we have for detecting model misbehavior, but its effectiveness depends on models faithfully externalizing their reasoning. Motivated by this vulnerability, we study whether monitor-aware models are capable of obfuscating their reasoning to evade detection. We use synthetic document finetuning to expose eight models to realistic pre-training-style documents describing a CoT monitor and find that monitor-aware models consistently achieve higher rates of undetected misbehavior compared to unaware controls. This effect is weaker but still present on a harder agentic task. We also show that CoT controllability, a model's ability to reshape its own reasoning trace under an imposed constraint, is closely correlated with obfuscation success across the eight models studied ($r=0.800$, $p=0.017$). Monitor-aware models placed under equal reinforcement learning optimization pressure also learn to reward-hack without triggering a CoT monitor substantially faster than unaware controls. Together, these results suggest that knowledge of monitoring combined with high CoT controllability poses a risk to CoT-based monitoring.

---


### 17. [Autonomous Intelligent Agents for Natural-Language-Driven Web Execution with Integrated Security Assurance](https://arxiv.org/abs/2605.15281)

**<font color=#1a73e8>作者：</font>** Vinil Pasupuleti, Siva Rama Krishna Varma Bayyavarapu, Shrey Tyagi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern web test suites rot. A UI refactor breaks locators, a timing change causes race conditions, and within weeks developers abandon the suite entirely. This paper presents an AI-driven autonomous testing framework that addresses these failure modes through five integrated strategies - navigation reliability, context-aware selector generation, post-generation validation, smart wait injection, and failure learning - implemented over a containerised worker architecture that decouples orchestration from long-running browser execution. Evaluated across four production applications and 176 scenarios, the framework improves script generation success from 55% to 93%, achieves an 8x reduction in navigation failures, eliminates 80% of timing-related race conditions, and reduces test creation time by 75% compared to manual Selenium authoring. The framework extends naturally to security validation: testers describe attack scenarios in plain English - "try accessing another user's invoice" - which the agent converts to OWASP Top 10-aligned browser probes, detecting 85% of authentication bypass vulnerabilities and 95% of input validation flaws with false positive rates below 12%. Natural-language-driven security testing of this kind represents, to our knowledge, a novel contribution to the field.

---


### 18. [Universal Approximation of Nonlinear Operators and Their Derivatives](https://arxiv.org/abs/2605.15285)

**<font color=#1a73e8>作者：</font>** Filippo de Feo  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Derivative-Informed Operator Learning (DIOL), i.e. learning a (nonlinear) operator and its derivatives, is an open research frontier at the foundations of the influential field of Operator Learning (OL). In particular, Universal Approximation Theorems (UATs) of nonlinear operators and their derivatives are foundational open questions and delicate problems in nonlinear functional analysis. In this manuscript, we prove the first UATs of non-linear $k$-times differentiable operators between Banach spaces and their derivatives, uniformly on compact sets and in weighted Sobolev norms for general finite input measures, via OL architectures. Our results are the first complete generalizations of the corresponding influential classical results in [Hornik, 1991] to infinite-dimensional settings and OL.
We discuss several open areas where DIOL and our UATs find applications: high-order accuracy in OL, fast constrained optimization in Banach spaces (e.g. optimal control of PDEs, inverse problems) and numerical methods for infinite-dimensional PDEs (e.g. HJB PDEs on Banach spaces from optimal control of PDEs, SPDEs, path-dependent systems, partially observed systems, mean-field control).
We parameterize nonlinear operators via Encoder-Decoder Architectures, renowned classes in OL due to their generality, including classical architectures, such as DeepONets, Deep-H-ONets, PCA-Nets. Our results are based on four key features that allow us to prove UATs in full generality: (i) Approximation Properties of Banach spaces. (ii) $k$-times continuous differentiability in the sense of Bastiani (weaker than $k$-times continuous Fréchet differentiability). (iii) Natural compact-open topologies for UA; indeed, we show that UA in standard compact-open topologies induced by operator norms is violated even for Fréchet derivatives. (iv) Construction of novel weighted Sobolev spaces for the UA.

---


### 19. [GQA-μP: The maximal parameterization update for grouped query attention](https://arxiv.org/abs/2605.15290)

**<font color=#1a73e8>作者：</font>** Kyle R. Chickering, Huijuan Wang, Mengxi Wu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperparameter transfer across model architectures dramatically reduces the amount of compute necessary for tuning large language models (LLMs). The maximal update parameterization ({\mu}P) ensures transfer through principled mathematical analysis but can be challenging to derive for new model architectures. Building on the spectral feature-learning view of Yang et al. (2023a), we make two advances. First, we promote spectral norm conditions on the weights from a heuristic to the definition of feature learning, and as a consequence arrive at the Complete-P depth and weight-decay scalings without recourse to lazy-learning. Second, we consider a modified spectral norm that preserves the valid scaling law of network weights when weight matrices are not full rank. This enables (to our knowledge, the first) derivation of {\mu}P scalings for grouped-query attention (GQA). We demonstrate the efficacy of our theoretical derivations by showing learning rate transfer across the GQA repetition hyperparameter as well as experiments regarding transfer over weight decay.

---


### 20. [GESD: Beyond Outcome-Oriented Fairness](https://arxiv.org/abs/2605.15295)

**<font color=#1a73e8>作者：</font>** Gideon Popoola, John Sheppard  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Machine learning (ML) algorithms are increasingly deployed in high-stakes decision-making domains such as loan approvals, hiring, and recidivism predictions. While existing fairness metrics (e.g., statistical parity, equal opportunity) effectively quantify outcome-oriented disparities, they offer limited insight into the procedure or explanation behind biased decisions. To address this gap, we propose Group-level Explanation Stability Disparity (GESD), a \textit{procedural-oriented} fairness metric that measures disparities in the stability, robustness, and sensitivity of model explanations across different subgroups in a protected category. %GESD is explainer-agnostic, model-agnostic, and extends the scope of fairness analyses to the level of explainability. We further integrate GESD into a multi-objective optimization framework that jointly optimizes for utility, outcome-based fairness, and explanation-based fairness called FEU (Fairness--Explainability--Utility). Empirical results on multiple benchmark datasets show that GESD effectively captures group-wise discrepancies in explanation quality, and that FEU improves both utility and fairness over state-of-the-art methods. By bridging outcome-based and explanation-based fairness, GESD offers a comprehensive tool for diagnosing and mitigating bias in predictive modeling. Our code and datasets are available on GitHub {\hyperlink{this https URL}{this https URL}}

---


### 21. [DiscoExplorer: An Open Interface for the Study of Multilingual Discourse Relations](https://arxiv.org/abs/2605.15304)

**<font color=#1a73e8>作者：</font>** Amir Zeldes  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The relations connecting propositions in discourse such as cause (A because B) or concession (A although B) are a subject of intense interest in Computational Linguistics and Pragmatics, but challenging to study and compare across languages. Recent progress in standardizing discourse relation inventories across datasets offers the potential to facilitate such studies, but is hindered by the complexity of relevant data and the lack of easily accessible interfaces to analyze it. In this paper we present DiscoExplorer, a new open source web interface, capable of running on local computers, which we use to make datasets from the DISRPT Shared Task on discourse relation classification publicly available, covering 16 different languages. We present the query language, search and visualization facilities for relations and signaling devices such as connectives, as well as some example studies.

---


### 22. [How Data Augmentation Shapes Neural Representations](https://arxiv.org/abs/2605.15306)

**<font color=#1a73e8>作者：</font>** Tianxiao He, Alex H. Williams, Sarah E. Harvey  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Data augmentation is widely recognized for improving generalization in deep networks, yet its impact on the geometry of learned representations remains poorly understood. In this work, we characterize how different data augmentation strategies reshape internal representations in neural networks. Using tools from shape analysis, we embed network hidden representations into a metric space where distance is invariant to scaling, translation, rotation and reflection. We show that increasing augmentation strength leads to well-behaved trajectories in this space, and that different augmentation types steer representations in distinct directions. Moreover, we investigate how neural representation shapes are distorted along data augmentation trajectories, and show that insights from neural geometry can predict which representations provide the most improvement when ensembling models. Our results reveal shared geometric patterns across architectures and seeds, and suggest that analyzing shape-space trajectories offers a principled tool for understanding and comparing data augmentation methods.

---


### 23. [SMCEvolve: Principled Scientific Discovery via Sequential Monte Carlo Evolution](https://arxiv.org/abs/2605.15308)

**<font color=#1a73e8>作者：</font>** Jiachen Jiang, Huminhao Zhu, Zhihui Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-driven program evolution has emerged as a powerful tool for automated scientific discovery, yet existing frameworks offer no principled guide for designing their individual components and provide no guarantee that the search converges. We introduce SMCEvolve, which recasts program search as sampling from a reward-tilted target distribution and approximates it with a Sequential Monte Carlo (SMC) sampler. From this view, three core mechanisms emerge as principled components: adaptive parent resampling, mixture of mutation with acceptance, and automatic convergence control. We further provide a finite-sample complexity analysis that bounds the LLM-call budget required to reach a target approximation error. Across math, algorithm efficiency, symbolic regression, and end-to-end ML research benchmarks, SMCEvolve surpasses state-of-the-art evolving systems while using fewer LLM calls under self-determined termination. The code is available at this https URL.

---


### 24. [One Pass Is Not Enough: Recursive Latent Refinement for Generative Models](https://arxiv.org/abs/2605.15309)

**<font color=#1a73e8>作者：</font>** Mehdi Esmaeilzadeh, Alexia Jolicoeur-Martineau, Chirag Vashist 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite remarkable progress, image generation is far from solved. The dominant metric, FID, conflates sample fidelity with mode coverage and is close to being saturated. Yet a model can still exhibit mode collapse while achieving a low FID, since a handful of sharp, near-duplicate images can outscore a model that faithfully covers the full data distribution. We argue that precision and recall are essential complements to FID, and that because FID is already saturated, the more meaningful goal is to improve diversity and coverage. Achieving high recall requires a model that explicitly prioritizes mode coverage, unlike most generative models, which optimize sample fidelity. We introduce RTM, which replaces the single-pass latent mapping in style-based generators with an iterative refinement process, and show that this consistently improves both quality and diversity. Integrated with Implicit Maximum Likelihood Estimation (IMLE), which optimizes mode coverage by design, RTM achieves the highest precision and recall among current state-of-the-art approaches while maintaining competitive FID, with improvements across CIFAR-10, CelebA-HQ at 256x256, and nine few-shot benchmarks. RTM also improves StyleGAN2 and StyleGAN2-ADA on CIFAR-10 and AFHQ-v1 at 512x512, demonstrating that the benefit is not specific to IMLE. Unlike flow-matching baselines that achieve competitive FID at the expense of coverage, recursive refinement improves both quality and diversity simultaneously.

---


### 25. [Time-Varying Deep State Space Models for Sequences with Switching Dynamics](https://arxiv.org/abs/2605.15311)

**<font color=#1a73e8>作者：</font>** Sanja Karilanova, Subhrakanti Dey, Ayça Özçelikkale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The identification and modeling of time-varying systems is a fundamental challenge in signal processing and system identification. To address this challenge, we propose a class of time-varying state-space model (SSM) based neural networks in which the neurons' states are governed by time-varying dynamics. The proposed model provides the learnable time-varying dynamics through a dictionary of basis functions, where each basis function evolves differently over time. We evaluate the proposed approach on both synthetic data from switching systems and a speech denoising task where real audio is corrupted with switching dynamics noise. The results show that the proposed time-varying model consistently outperforms its time-invariant counterparts while maintaining comparable computational complexity. Our investigations also reveal which aspects of the time-varying dynamics of the data most need to be captured by the proposed time-invariant models, how the additional freedom provided by time-varying basis functions should be allocated across model components, and to what extent larger models can compensate for time-invariant limitations.

---


### 26. [Beyond Bounded Variance: Variance-Reduced Normalized Methods for Nonconvex Optimization under Blum-Gladyshev Noise](https://arxiv.org/abs/2605.15314)

**<font color=#1a73e8>作者：</font>** Antesh Upadhyay, Arda Fazla, Abolfazl Hashemi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study nonconvex stochastic optimization under the Blum-Gladyshev ($\mathsf{BG}$-0) noise model, where the stochastic gradient variance grows quadratically with the distance from the initialization. We consider this problem under both standard smoothness and the symmetric generalized-smoothness framework, which captures objectives whose local curvature can scale with the gradient norm. We prove that normalized stochastic gradient descent with momentum, using only one stochastic gradient per iteration, converges under $\mathsf{BG}$-0 noise with oracle complexity $O(\varepsilon^{-6})$. This rate holds both for standard smoothness and for $\alpha$-symmetric generalized smoothness, showing that generalized smoothness is rate-neutral for normalized momentum in this setting. We then study a variance-reduced normalized STORM method. Under mean-square smoothness and sharp initialization, the method achieves the minimax optimal $O(\varepsilon^{-4})$ complexity, matching the lower bound. Under expected $\alpha$-symmetric generalized smoothness, the STORM recursion couples gradient-dependent smoothness with distance-dependent noise, leading to complexity $O(\varepsilon^{-(4+\alpha)})$ for $\alpha\in(0,1)$ and $O(\varepsilon^{-5})$ for $\alpha=1$. When the distance-growth parameter in the noise model vanishes, our guarantees recover the standard bounded-variance rates: $O(\varepsilon^{-4})$ for momentum, $O(\varepsilon^{-3})$ for variance reduction, and $O(\varepsilon^{-2})$ in the deterministic case. To our knowledge, these are the first convergence guarantees for normalized methods in non-convex stochastic optimization under $\mathsf{BG}$-0 noise without bounded domains, increasing batch sizes, or explicit anchoring, covering both standard and generalized smoothness regimes.

---


### 27. [Context Pruning for Coding Agents via Multi-Rubric Latent Reasoning](https://arxiv.org/abs/2605.15315)

**<font color=#1a73e8>作者：</font>** Jingjing Wang, Xiwen Chen, Wenhui Zhu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-powered coding agents spend the majority of their token budget reading repository files, yet much of the retrieved code is irrelevant to the task at hand. Existing learned pruners compress this context with a single-objective sequence labeler, collapsing all facets of code relevance into one score and one transition matrix. We show that this formulation creates a modeling bottleneck: a single CRF transition prior must serve heterogeneous retention patterns, including contiguous semantic spans and sparse structural support lines. We propose LaMR (Latent Multi-Rubric), a structured pruning framework that decomposes code relevance into two interpretable quality dimensions, semantic evidence and dependency support, each modeled by a dedicated CRF with dimension-specific transition dynamics. A mixture-of-experts gating network dynamically weights the per-rubric emissions conditioned on the query, and a final CRF layer on the fused emissions produces the aggregate keep-or-prune decision. To supervise each dimension without additional annotation cost, we derive multi-rubric labels from the existing training corpus via AST-based program analysis, simultaneously denoising the teacher's binary labels. By effectively filtering distracting noise, LaMR frequently matches or even outperforms unpruned full-context baselines. Experiments on four benchmarks (SWE-Bench Verified, SWE-QA, LCC, LongCodeQA) show that LaMR wins 12 of 16 head-to-head multi-turn comparisons. It saves up to 31% more tokens on multi-turn agent tasks and improves Exact Match by up to +3.5 on single-turn tasks, while performance is frequently enhanced by denoising the context, and any remaining drops are marginal.

---


### 28. [Overreliance in Writing Tasks: Exploring Similarity-Based Measures of AI Influence on Writing and Proposing a Reflective Writing Interface Intervention](https://arxiv.org/abs/2605.15322)

**<font color=#1a73e8>作者：</font>** Vitor H. A. Welzel, Nicholas Vincent  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI (GenAI) systems become increasingly proficient at simulating human-like and well-reasoned text, users may attribute authority to AI outputs, shaping how they engage with writing and reasoning tasks. While prior work has raised concerns about AI overreliance, empirical approaches for observing this phenomenon during open-ended writing remain limited. In this paper, we examine how GenAI assistance influences users' interactions with AI suggestions during writing. We report results from a mixed-methods study in which 47 participants completed analysis and synthesis writing tasks with or without AI assistance. We quantify the textual overlap between AI suggestions and participants' writing and analyze participants' reflections. Our results show that AI assistance is associated with patterns of suggestion reuse. Building on these findings, we design and evaluate an interactive writing interface that may support reflection on the usage of the AI suggestions during writing. Evidence from a small follow-up think-aloud study (n = 4) suggests that the interface can increase users' awareness of how AI outputs are incorporated into their writing and may support more conscious engagement with AI assistance. Together, our findings contribute empirical methods for studying AI adoption in writing contexts and demonstrate how interface design can shape user-AI interaction.

---


### 29. [COPRA: Conditional Parameter Adaptation with Reinforcement Learning for Video Anomaly Detection](https://arxiv.org/abs/2605.15325)

**<font color=#1a73e8>作者：</font>** Darryl Cherian Jacob, Xinyu Liu, Kai Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have shown strong performance in video anomaly detection (VAD) while providing interpretable predictions. However, existing VLM-based VAD methods suffer from a fundamental mismatch between training and inference in both data distribution and model configuration. First, most approaches rely on static post-training adaptation, limiting generalization under distribution shifts such as unseen environments or anomaly types. Second, they train VLMs on sparse frames from long videos, but perform inference on densely sampled short segments, creating inconsistencies between training and testing. To address these limitations, we propose COPRA, a conditional parameter adaptation framework for VLM-based VAD. Instead of fixed prompts or shared parameter updates, COPRA generates input-specific parameter updates to dynamically adapt a frozen VLM for each video segment during both training and inference. Experiments show strong performance on standard VAD benchmarks, consistently outperforming static baselines in both in-domain and cross-domain settings. Moreover, COPRA generalizes beyond VAD to unseen tasks such as multiple-choice Video Question Answering and Dense Captioning. These results highlight COPRA as an effective weight-space generation framework for scalable, adaptive, and context-aware video understanding. The code will be released at this https URL

---


### 30. [From Weight Perturbation to Feature Attribution for Explaining Fully Connected Neural Networks](https://arxiv.org/abs/2605.15328)

**<font color=#1a73e8>作者：</font>** Thodoris Lymperopoulos, Denia Kanellopoulou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fully Connected Neural Networks (FCNNs) are often regarded as simple and intuitive architectures, yet they serve as the foundation for more complex models. Nonetheless, the lack of consensus on their interpretability continues to pose challenges, underscoring the enduring relevance of simpler, attribution-based approaches for understanding even the most advanced neural architectures. In this regard, we explore a novel idea for estimating feature attribution, by applying perturbation to the features' attached weights instead of their values. This method offers a fresh perspective aimed at mitigating common limitations in Occlusion techniques, such as Added Bias and Out-of-Distribution data. The application of this rule leads to the formation of a pair of novel attribution methods we call XWP and XWP_c. Founded on simple rules, our methods achieve competitive performance in identifying image signals for simple DNNs, competing with the most established attribution methods on standard baseline metrics. Our work thus contributes to the field of Explainability by introducing a robust framework that paves the way for addressing these long-standing vulnerabilities, and leads to more reliable and interpretable model explanations.

---


### 31. [Distance-Preserving Digests: A Primitive for BFT Consensus](https://arxiv.org/abs/2605.15329)

**<font color=#1a73e8>作者：</font>** Ryan Patrick Mercier  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Every BFT consensus protocol uses collision-resistant hashes to compare validator state. Collision resistance destroys distance: two validators agreeing on 19 of 20 transactions produce unrelated hashes, indistinguishable from validators sharing nothing. This forces three design constraints across the BFT literature: validators must synchronize state before voting, agreement quality cannot be measured until votes are counted, and hierarchical committees must be large enough for independent BFT, limiting tree depth. This paper introduces distance-preserving transaction digests, a primitive that replaces collision-resistant hashes with commutative vector sums in 8-dimensional space. The primitive has three properties hashes lack: distance is proportional to disagreement, weighted means are exact, and set differences are identifiable via bloom filter diff. We demonstrate three applications: a two-phase BFT protocol (Proxima) that achieves single-round finality when validators agree; tree-structured consensus with groups of 10 validators (vs 128 in Ethereum), enabled because distance filtering replaces per-group BFT; and cross-shard consistency verification at 128 bytes per shard pair, replacing the per-transaction coordination of two-phase commit. Safety is proved: fewer than N/3 Byzantine validators cannot cause conflicting finalization, independent of Phase 1 clustering or tree topology. At N =100,000, Proxima Tree uses 2.2x fewer messages than HotStuff (a structural property unaffected by parallelism). Single-core finality is 0.9s vs 18s for HotStuff; multi-core BLS narrows but does not eliminate this gap.

---


### 32. [From I/O to Code with Discovery Agent](https://arxiv.org/abs/2605.15334)

**<font color=#1a73e8>作者：</font>** Yihong Dong, Jiaru Qian, Haoran Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The automatic synthesis of a program from any form of specification is regarded as a holy grail of computer science. Fueled by LLMs, NL2Code has achieved tremendous success, yet the fundamentally more challenging task of synthesizing programs from input-output behavior, which we refer to as IO2Code, remains largely unsolved. Whereas NL2Code can exploit the semantic alignment between natural language and code acquired during pretraining, IO2Code requires recovering underlying principles from concrete computational behavior, navigating a vast and underspecified hypothesis space. To address this, we propose DIO-Agent, a discovery agent for IO2Code. Our method frames IO2Code as an evolutionary search over discrete program space, in which an LLM serves as the mutation operator and concrete error signals from execution guide each mutation. To prevent the search from wandering into structurally complex yet incorrect dead ends, we introduce the Transformation Priority Premise as a mutation prior that biases the LLM toward the simplest hypothesis consistent with current evidence, progressively escalating from constants to conditionals to iteration only when simpler constructs are insufficient. To facilitate systematic study, we further construct an IO2CodeBench spanning multiple difficulty levels. Extensive experiments show that DIO-Agent consistently outperforms both traditional program-by-example method and SOTA evolution-agent baselines across all difficulty levels and various LLMs, while substantially surpassing test-time scaling strategies with equivalent sampling budgets.

---


### 33. [Bounded-Rationality, Hedging, and Generalization](https://arxiv.org/abs/2605.15340)

**<font color=#1a73e8>作者：</font>** Pedro A. Ortega  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A learner does not only fit data; it also determines how strongly the training sample may shape its output and how much distortion it can hedge. We study this relation as a bounded-rational decision problem whose primitive object is the induced channel from samples to outputs. The learner's response law determines which changes in this channel are cheap or costly, and therefore induces both a lower tradeoff curve between training loss and sample dependence and a matched upper certificate curve. When the response law is represented by an $f$-divergence regularizer, these curves live in the regularizer's native information geometry, with KL as the special case corresponding to Shannon mutual information. We show how the hedge and the two curves can be recovered from black-box behavior by observing responses to scaled losses and local loss perturbations. In learning, population loss is empirical loss plus the distortion induced by the particular training sample. The recovered hedge gives a practical certificate when it covers that distortion. Thus generalization is treated as a testable hedging property of the learner's own response law.

---


### 34. [Minerva-Ego: Spatiotemporal Hints for Egocentric Video Understanding](https://arxiv.org/abs/2605.15342)

**<font color=#1a73e8>作者：</font>** Arsha Nagrani, Jasper Uijilings, Shyamal Buch 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video reasoning models are a core component of egocentric and embodied agents. However, standard benchmarks for assessing models provide only evaluation of the output (e.g. the answer to a question), without evaluation of intermediate reasoning steps, and most provide answers only in the text domain. We introduce Minerva-Ego, a benchmark for evaluating complex egocentric visual reasoning. We extend recent high-quality video data sources recorded from egocentric / embodied settings with a set of challenging, multi-step multimodal questions and spatiotemporally-dense human-annotated reasoning traces. Benchmarking experiments show that state-of-the-art models still have a large gap to human performance. To investigate this gap in detail, we annotate each reasoning trace in the dataset with the objects of interest required to solve the question, as spatiotemporal mask annotations. Through extensive evaluations, we identify that prompting frontier models with hints of 'where' and 'when' to look yields substantial improvements in performance. Minerva-Ego can be downloaded at this https URL.

---


### 35. [Topical Shifts in the Dark Web: A Longitudinal Analysis of Content from the Cybercrime Ecosystem](https://arxiv.org/abs/2605.15345)

**<font color=#1a73e8>作者：</font>** Roy Ricaldi, Maximilian Schafer, Philipp Zech 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The dark web hosts a dynamic ecosystem of cybercrime forums and marketplaces that adapt to law enforcement pressure, technological change, and economic incentives. Prior research has extracted cyber threat intelligence from these platforms using static snapshots, with limited attention to how discussions evolve over time. In this study, we conduct a longitudinal analysis of 25,065 websites in the dark web using 11,403,638 HTML snapshots (approximately 1245.38 GB) collected over six years. We develop a longitudinal topic-modeling framework combining domain-specific embeddings, density-based clustering and temporal aggregation to measure topic prevalence and lifecycle at the website level. Our analysis identifies 55 thematic clusters. We find that approximately 75% of total discussion volume is concentrated in a small set of persistent core topics, while short-lived themes account for approximately 3% of activity. The median topic lifespan is 75 months, indicating gradual thematic evolution rather than abrupt replacement.

---


### 36. [PACER: Acyclic Causal Discovery from Large-Scale Interventional Data](https://arxiv.org/abs/2605.15353)

**<font color=#1a73e8>作者：</font>** Ramon Viñas Torné, Sílvia Fàbregas Salazar, Soyon Park 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inferring the structure of directed acyclic graphs (DAGs) from data is a central challenge in causal discovery, particularly in modern high-dimensional settings where large-scale interventional data are increasingly available. While interventional data can improve identifiability, existing methods remain limited by soft acyclicity constraints, leading to optimization over invalid cyclic graphs, numerical instability, and reduced scalability. We introduce PACER (Perturbation-driven Acyclic Causal Edge Recovery), a scalable framework for causal discovery that guarantees acyclicity by construction. PACER parameterizes a distribution over DAGs through a joint model of variable permutations and edge probabilities, enabling direct optimization over valid causal structures without surrogate penalties. The framework supports a unified likelihood-based treatment of observational and interventional data, flexible conditional density models, and the incorporation of structural prior knowledge. For linear-Gaussian mechanisms, we derive closed-form expressions for the expected interventional log-likelihood and its gradients, yielding substantial computational gains. Empirically, PACER matches or exceeds state-of-the-art methods on protein signaling and large-scale genetic perturbation benchmarks, while scaling efficiently to networks with thousands of variables and achieving up to two orders of magnitude speedups over penalty-based differentiable approaches. These results demonstrate that exact and scalable causal discovery from high-dimensional perturbation data is achievable through principled search space design.

---


### 37. [Federated Learning of Spiking Neural Networks under Heterogeneous Temporal Resolutions](https://arxiv.org/abs/2605.15355)

**<font color=#1a73e8>作者：</font>** Sanja Karilanova, Subhrakanti Dey, Ayça Özçelikkale  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spiking neural networks (SNNs) are biologically inspired energy-efficient models that use sparse binary spike-based communication between neurons, making them attractive for resource-constrained edge devices. Federated learning enables such devices to train collaboratively without sharing raw data. In time-series applications, edge devices often collect data at different time resolutions due to hardware and energy constraints. This temporal heterogeneity poses a fundamental challenge for federated learning: parameters learned at one temporal resolution do not necessarily transfer directly to another, which might result in the naive federated averaging being ineffective. Targeting SNNs and, more broadly, deep networks with stateful neurons, we propose a federated learning framework that addresses this temporal resolution mismatch. We investigate how neuron parameters learned from data at different temporal resolutions and model aggregation should be integrated. We evaluate the proposed framework across two SNN-native benchmark datasets (SHD and DVS-Gesture) under a range of resolution heterogeneity scenarios. Our results show that the proposed adaptation methods can substantially recover accuracy lost due to temporal mismatch, hence enabling each client to train at their local temporal resolution while remaining compatible with the global model.

---


### 38. [Automatic Construction of a Legal Citation Graph from 100 Million Ukrainian Court Decisions: Large-Scale Extraction, Topological Analysis, and Ontology-Driven Clustering](https://arxiv.org/abs/2605.15362)

**<font color=#1a73e8>作者：</font>** Volodymyr Ovcharov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Half a billion citation edges extracted from 100.7 million Ukrainian court decisions reveal that judicial citation structure encodes legal domain boundaries without supervision and predicts future legislative importance with near-perfect accuracy. We construct the first large-scale citation graph from the complete EDRSR registry (99.5 million full texts, 1.1 TB), extracting 502 million citation links across six types via regex on commodity hardware in approximately 5 hours, with precision of 1.00 on a 200-decision validation sample (95% Wilson CI: [0.982, 1.000]).
Three principal findings emerge. (1) The degree distribution follows a power law (alpha = 1.57 +/- 0.008), placing the Ukrainian court network near the EU Court of Justice and below the US Supreme Court, with hub articles cited by millions of decisions. (2) Louvain community detection on the co-citation projection recovers legal domain boundaries (civil, criminal, administrative, commercial) with modularity Q = 0.44-0.55 and temporal stability (NMI = 0.83-0.86 across periods), constituting an automatically constructed legal ontology grounded in judicial practice. (3) Citation features predict top-1000 articles with AUC = 0.9984, substantially outperforming a naive frequency baseline (P@1000 = 0.655); temporal dynamics detect legislative regime changes as phase transitions and the 2022 invasion as a citation entropy spike (H: 11.02 -> 13.49) with emergent wartime legislation nodes.
The citation-derived ontology is operationalized as the domain layer of a workflow memory system for LLM-assisted legal analysis, connecting to the ontology-controlled paradigm. The extraction pipeline, analysis code, and aggregated statistics are released as open data.

---


### 39. [PRB-RUPFormer: A Recursive Unified Probabilistic Transformer for Residual PRB Forecasting](https://arxiv.org/abs/2605.15363)

**<font color=#1a73e8>作者：</font>** Saad Masrur, Yuxuan Jiang, Matti Hiltunen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate forecasting of residual Physical Resource Blocks (PRBs) is critical for proactive network slice provisioning, energy-efficient operation, and spectrum-aware decision making in cellular systems, where residual PRBs serve as a practical proxy for short- and medium-term spectrum availability. Existing PRB prediction methods typically rely only on historical PRB values and are trained independently per carrier or sector, limiting their ability to capture cross-carrier dependencies and providing no measure of forecast uncertainty. Moreover, point forecasts alone are insufficient for robust spectrum-aware control under highly variable traffic conditions. This paper proposes PRB-RUPFormer, a recursive unified probabilistic Transformer for residual PRB forecasting. The proposed model jointly processes multivariate KPI time series using temporal, seasonal, and carrier-aware embeddings, preserving inter-metric temporal coupling during recursive rollout and stabilizing long-horizon forecasting. A single shared model is trained across all carriers and sectors of an eNB, enabling efficient learning of joint traffic dynamics with low computational overhead. Forecast uncertainty is captured through quantile-based prediction intervals, providing confidence-aware estimates of future PRB availability. Evaluations on six months of commercial LTE network data from multiple U.S. locations demonstrate median MAE below 0.05 and hit probabilities above 0.80 for both one-day and seven-day recursive forecasts. These probabilistic predictions directly support spectrum-aware RAN functions such as dynamic carrier activation, congestion avoidance, and proactive spectrum sharing, making the proposed framework well-suited for dynamic spectrum access scenarios.

---


### 40. [Greedy or not, here I come: Language production under vocabulary constraints in humans and resource-rational models](https://arxiv.org/abs/2605.15365)

**<font color=#1a73e8>作者：</font>** Thomas Hikaru Clark, Sihan Chen, Laura Nicolae  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Communicating using only a limited vocabulary is a common but challenging cognitive phenomenon, requiring an ideal communicator to plan carefully to optimize for intelligibility while circumventing a constrained lexicon. In this work, we investigate how humans respond to a broad array of questions under variable vocabulary limitations, consisting of only 250 highly frequent words at the most restrictive. We provide theoretically motivated comparisons to greedy and globally optimal sampling algorithms using Sequential Monte Carlo inference with large language models. Humans generally resemble greedy sampling more than globally optimal sampling, though more skilled humans are more likely to backtrack and revise -- a non-greedy behavior. An observed human pattern of leaning on semantically light words in high-constraint settings falls out of both greedy and globally optimal sampling. We discuss the results and their broader implications for resource-rational cognition, psycholinguistics, L2 communication, and language impairments.

---


### 41. [Discretizing Group-Convolutional Neural Networks for 3D Geometry in Feature Space](https://arxiv.org/abs/2605.15368)

**<font color=#1a73e8>作者：</font>** Daniel Franzen, Jean Philip Filling, Michael Wand  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Group-convolutional neural networks (GCNNs) are among the most important methods for introducing symmetry as an inductive bias in deep learning: In each linear layer, GCNNs sample a transformation group $G$ densely and correlate data and filters in different poses (with suitable anti-aliasing for steerable GCNNs) to maintain equivariance with respect to $G$. Unfortunately, applying filters to many data items resulting from this sampling is expensive (even for translations alone, i.e., in ordinary CNNs), and costs grow exponentially with increasing degrees of freedom (such as translations and rotations in 3D), which often hinders practical applications. In this paper, we propose sampling in feature space, i.e., replacing geometrically dense samples with representative samples selected by feature similarity. This decouples geometric resolution from memory and processing costs during training and inference, providing a novel way to trade off computational effort and accuracy. Our main empirical finding is that a coarse feature-space sampling already preserves classification accuracy remarkably well, which permits precomputation based on geometric similarity, accelerating the training of equivariant 3D classifiers substantially.

---


### 42. [ChangeFlow -- Latent Rectified Flow for Change Detection in Remote Sensing](https://arxiv.org/abs/2605.15375)

**<font color=#1a73e8>作者：</font>** Blaž Rolih, Matic Fučka, Filip Wolf 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Remote sensing change detection (RSCD) aims to localise changes between two images of the same geographic region. In practice, change masks often follow region-level annotation conventions rather than purely local appearance differences, making them context-dependent and occasionally ambiguous. Most state-of-the-art methods utilise per-pixel discriminative classification, which produces a single prediction per input and fails to explicitly model the changed region as a coherent whole. A natural alternative is generative formulation, which can model a distribution of plausible masks, enabling sampling to capture ambiguity and encourage global consistency. However, existing generative RSCD approaches typically lag behind strong discriminative baselines due to the high computational cost of pixel-space generation and the complexity of their conditioning mechanisms. To address the limitations of prior discriminative and generative methods, we propose ChangeFlow, a generative framework that reformulates change detection as the synthesis of a change mask in latent space via rectified flow. ChangeFlow is guided by a structured yet lightweight conditioning signal, and its stochastic design naturally supports sampling-based prediction ensembling. Namely, aggregating multiple predicted change masks improves robustness, while sample agreement provides a practical confidence estimation that highlights ambiguous regions. Across four benchmarks, ChangeFlow achieves an average F1 of 80.4\%, improving by 1.3 points on average over the previous best method, while maintaining inference speed comparable to recent strong baselines. Project page: this https URL

---


### 43. [Adesua: Development and Feasibility Study of an AI WhatsApp Bot for Science Learning in West Africa](https://arxiv.org/abs/2605.15376)

**<font color=#1a73e8>作者：</font>** George Boateng, Evans Atompoya, Philemon Badu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sub-Saharan Africa faces persistently high student-teacher ratios and shortages of qualified teachers, limiting students' access to personalized learning support and formative assessment. To address this challenge, we present Adesua, a WhatsApp-based AI Teaching Assistant for science education that extends the Kwame for Science platform. Adesua leverages WhatsApp's widespread adoption in Africa to provide accessible, curriculum-aligned learning support for Junior High School (JHS) and Senior High School (SHS) students across West Africa. The system integrates curated textbooks and 33 years of national examination questions with generative AI to enable conversational question answering and automated assessment with feedback via a WhatsApp bot. Students can ask science questions, take timed or untimed multiple-choice tests by topic or exam year, and receive instant grading and detailed explanations of correct and incorrect responses. A 6-month feasibility deployment in 2025 had 56 active users in Ghana, including students and parents. Quantitative evaluation showed a high perceived usefulness, with a helpfulness score of 93.75\% for AI-generated answers, albeit with a small number of ratings (n=16). These preliminary results provide a basis for more extensive future evaluation of a WhatsApp-based AI assistant to assess its potential to offer scalable, low-cost personalized learning support and formative assessment in resource-constrained educational contexts.

---


### 44. [Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute](https://arxiv.org/abs/2605.15377)

**<font color=#1a73e8>作者：</font>** Eugene Koran, Yejun Yun, Samantha Tetef 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI systems are increasingly deployed in autonomous agentic settings at scale, it is important to ensure the actions they take are safe and aligned with user intent. Monitoring agent actions is a key safety mechanism, yet reliable monitors remain difficult to build and the scale of these systems makes human oversight impractical. We show that combining signals from diverse monitors into an ensemble improves detection of misaligned actions. We build 12 GPT-4.1-Mini monitors using both prompting and fine-tuning strategies. We evaluate them on coding tasks where candidate solutions pass standard tests but fail on adversarial inputs. In this setting, diverse ensembles outperform both individual monitors and homogeneous ensembles. Our best 3-monitor ensemble achieves 2.4x greater detection performance gain compared to an ensemble composed of three identical monitors, with the same ensemble performing strongly on an independent dataset. We contend that these results show that diversity - not scale - drives gains. The best ensembles combine strong individual performance with low correlation between monitors. Furthermore, fine-tuned monitors appear in every top-performing ensemble and maintain this advantage on out-of-distribution attack types, suggesting that fine-tuning enables detection capabilities that prompting alone does not elicit. These results support ensemble monitoring as a practical AI control strategy for safety gains at reasonable inference costs.

---


### 45. [Eskwai for Students: Generative AI Assistant for Legal Education in Ghana](https://arxiv.org/abs/2605.15380)

**<font color=#1a73e8>作者：</font>** George Boateng, Philemon Badu, Patrick Agyeman-Budu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in generative AI have shown their potential to be leveraged for legal education. Yet, work on the development and deployment of such systems for legal education in the Global South is limited. In this work, we developed Eskwai for Students, a generative AI assistant to help law students with their legal education. Eskwai for Students is a retrieval augmented generation (RAG) system that provides answers to a wide range of legal questions for law students grounded in a curated database of over 12K case laws and 1.4K legislation in Ghana. We deployed Eskwai for Students in a longitudinal study of 30 months (2.5 years) used by 3.1K law students in Ghana who made 32K queries. We evaluated the helpfulness of our AI, and provided insight into the kinds of queries law students submit to this generative AI tool, which raises some ethical concerns. This work contributes to an understanding of how law students in the Global South are using generative AI for their studies and the ways it could be leveraged responsibly to advance legal education.

---


### 46. [MorphoHELM: A Comprehensive Benchmark for Evaluating Representations for Microscopy-Based Morphology Assays](https://arxiv.org/abs/2605.15383)

**<font color=#1a73e8>作者：</font>** Emre Hayir, Lorin Crawford, Alex X. Lu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Microscopy images contain rich information about how cells respond to perturbations, making them essential to applications like drug screening. To quantify images, researchers often use representation extraction methods, and recent years have seen a proliferation of deep learning methods. While measuring the quality of these representations is essential, evaluation remains fragmented, with each proposed model evaluated on different tasks and datasets, using custom pipelines and metrics, making it difficult to fairly compare models. Here, we introduce MorphoHELM, a comprehensive open benchmark for evaluating feature extraction methods for Cell Painting, the most widely-used morphological profiling assay. MorphoHELM consolidates evaluation standards in the field, extends and corrects them to be more robust, and evaluates on the widest range of methods to date. A defining feature of the benchmark is that each task is evaluated at different degrees of batch effects (or technical noise), directly quantifying how the ability of methods to detect biological signal degrades as noise increases. Together, these properties enable MorphoHELM to detect trade-offs between methods, and we demonstrate that models that excel at certain kinds of biological signal are weaker at others. We show that no existing model outperforms classic computer vision analytic strategies across all settings, which remain the strongest general use-case representations. All datasets, code, and evaluation tools are publicly available at this https URL.

---


### 47. [Unified High-Probability Analysis of Stochastic Variance-Reduced Estimation](https://arxiv.org/abs/2605.15388)

**<font color=#1a73e8>作者：</font>** Zhankun Luo, Antesh Upadhyay, M. Berk Sahin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stochastic estimators are fundamental to large-scale optimization, where population quantities must be inferred from noisy oracle observations. Although influential methods such as momentum, SPIDER, STORM, and PAGE have been highly successful, their analyses are largely estimator-specific and expectation-based, obscuring the structural tradeoffs that determine reliability. In this paper, we develop a unified framework for stochastic variance-reduced estimation based on a recursion with three components: memory retention, reset probability, and a correction term for iterate movement. This framework recovers several classical estimators, motivates new second-order variants, and yields a bias-variance decomposition of estimation error. Our main result is a unified high-probability bound proved using a new dimension-free vector-valued Freedman inequality, valid for smooth normed spaces involving random sums of vector martingales. The result applies in both Euclidean and non-Euclidean settings, including the analysis of mirror-descent-based methods in Banach spaces. As applications, we obtain high-probability oracle complexities for unconstrained optimization with mirror descent, establishing the logarithmic dependence on the confidence level. We also derive the first $\tilde{\mathcal{O}}(\varepsilon^{-3})$ oracle-complexity bounds for stochastic optimization with expectation constraints, improving upon the existing $\tilde{\mathcal{O}}(\varepsilon^{-4})$ complexity by leveraging variance-reduced estimation for the first time in this setting.

---


### 48. [Breakeven complexity: A new perspective on neural partial differential equation solvers](https://arxiv.org/abs/2605.15399)

**<font color=#1a73e8>作者：</font>** Yijing Zhang, Nicholas Roberts, Tanya Marwah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural surrogate solvers of partial differential equations (PDEs) promise dramatic speedups over numerical methods, especially in scenarios requiring many solves. However, current accuracy-based evaluations do not fully consider two central issues: (1) neural solvers incur substantial up-front costs for data generation, training, and tuning; and (2) classical solvers can also generate low-fidelity solutions at a sufficiently low simulation cost. To explicitly account for these realities and fully incorporate end-to-end costs, we propose an evaluation framework centered on breakeven complexity, a metric that counts the forward solves before a learned solver is cost-effective relative to an error-equivalent traditional solver. To evaluate this measure, we apply scaling laws to determine how much training budget to allocate to data generation and discuss how to achieve smooth error-matching in diverse settings. We evaluate the breakeven complexity of multiple neural PDE solvers on three PDEs on 2D periodic domains from APEBench and a novel benchmark of flows past multiple obstacles generated by the GPU-native PyFR code. Among other findings, our results suggest that neural PDE solvers become more effective as problems get harder in terms of cost, dimension, rollout, physics regime (e.g. higher Reynolds number), etc.

---


### 49. [Beyond Partner Diversity: An Influence-Based Team Steering Framework for Zero-Shot Human-Machine Teaming](https://arxiv.org/abs/2605.15400)

**<font color=#1a73e8>作者：</font>** Wei Sheng, Rohan Paleja  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While AI agents are rapidly advancing from isolated tools to interactive collaborators, data-driven human-machine teaming (HMT) methods remain costly in their reliance on human interaction data across domains, teammates, and team sizes. Zero-shot coordination (ZSC) addresses this bottleneck by simulating diverse partner populations to approximate how unseen partners might behave. However, partner coverage alone is insufficient as team settings scale and communication becomes degraded. To remedy this deficiency, we propose Influence-Based Team Steering (IBTS), a framework that uses influence shaping to incentivize agents to discover diverse, high-performing team interaction patterns and further steers ongoing trajectories toward stronger learned coordination modes. We assess IBTS on Overcooked-AI in both two-agent and three-agent settings, allowing us to test whether learned coordination structure transfers beyond dyadic interaction. Our evaluation includes simulated partners, synthetic partner-style variation, and, to our knowledge, the first 30-subject Overcooked-AI HMT study involving two real human teammates and one machine teammate. Across these evaluations, IBTS improves team performance against competing baselines, highlighting the need for scaled ZSC to combine sparse-reward coordination mechanisms with partner-variation coverage rather than relying on diversity alone.

---


### 50. [$ϕ$-Balancing for Mixture-of-Experts Training](https://arxiv.org/abs/2605.15403)

**<font color=#1a73e8>作者：</font>** Lizhang Chen, Jonathan Li, Qi Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) models rely on balanced expert utilization to fully realize their scalability. However, existing load-balancing methods are largely heuristic and operate on noisy mini-batch assignment statistics, introducing bias relative to population-level objectives. We propose $\phi$-balancing, a principled framework that directly targets population-level expert balance by minimizing a strictly convex, symmetric, and differentiable potential of the expected routing distribution. Using convex duality, we derive an equivalent min-max formulation and obtain a simple online algorithm via mirror descent, yielding an efficient EMA-based routing adjustment with negligible overhead. Across large-scale pretraining and downstream fine-tuning, $\phi$-balancing consistently outperforms prior Switch-style and loss-free baselines, demonstrating more stable and effective expert utilization.

---


> [!TIP]
> 当前位于：**1-50**（第 1/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-234](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
