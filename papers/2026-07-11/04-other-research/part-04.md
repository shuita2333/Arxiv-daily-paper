# 📦 其他研究 | 2026年07月11日

> 本类共 **189** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**151-189**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-189**

---

### 151. [CommuniWave:A Machine Learning Model for Quantifying the Degree of Temporary Informal Behavior in Urban Communities](https://arxiv.org/abs/2607.08554)

**<font color=#1a73e8>作者：</font>** Hongye Yang, Shien Liu, Zhihao Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> For urban managers and designers, improving the functional attributes of urban communities to enhance territorial resilience in the face of complexity and uncertainty is crucial. Currently, community planning often follows a top-down approach and lacks effective metrics to quantify informal behaviors of residents, leading to frequent conflicts with original plans. This study introduces CommuniWave, a machine learning model designed to efficiently detect and quantify the Degree of Informal Behavior (DIB) in urban communities. The model integrates a Behavior Capture Net (BCN) based on mmaction2, a self-developed YOLOv10 model (YLX), and a Behavior Eval Model (BEM) using random forest. Ultimately, by generating DIB fluctuation charts from street videos, the model facilitates dynamic monitoring, supporting urban managers in making refined decisions to enhance the overall resilience of communities.

---


### 152. [SHAP-Weighted Cross-Modal Expert Fusion for Emotion and Sentiment Recognition: Evidence and Limits](https://arxiv.org/abs/2607.08573)

**<font color=#1a73e8>作者：</font>** Adis Alihodzic, Selma Skopljakovic Hubljar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion and sentiment recognition is commonly addressed by early fusion, which concatenates modalities before classification, or late fusion, which combines independently trained unimodal predictors. Early fusion can be accurate but monolithic, while late fusion is modular but may lose cross-modal interactions. This paper revisits XAI-guided adaptive fusion (\xgaf), a tree-based mixture of unimodal and cross-modal experts whose sample-level weights are derived from TreeSHAP attribution magnitudes. We focus on the effect of SHAP attribution reduction when experts have unequal feature dimensionalities. In this setting, mean-abs and median-abs reductions can suppress high-dimensional cross-modal experts, whereas sum-abs reduction preserves total attribution mass. On MELD 7-class emotion recognition, sum-abs \xgaf{} nearly matches early fusion across three face-sequence aggregators; the Transformer variant reaches 0.5983 \wf{}, compared with 0.6018 for early fusion and 0.4598 for probability-average late fusion. McNemar testing shows no significant difference between sum-abs \xgaf{} and early fusion on MELD ($p=1.000$), while \xgaf{} remains significantly better than late fusion ($p<0.0001$). On CMU-MOSEI 3-class sentiment recognition, sum-abs \xgaf{} reaches 0.6519 \wf{}, slightly exceeding early fusion (0.6485) and late fusion (0.5696). Ablation studies show that the main gain comes from adding cross-modal experts, especially the trimodal expert, rather than from complex per-sample routing. Diagnostics further show that mean-abs and median-abs weights are nearly uniform, while sum-abs weights concentrate on the trimodal expert. Thus, the main contribution is a transparent empirical analysis of how SHAP reduction, expert dimensionality, and cross-modal expert design affect modular multimodal fusion.

---


### 153. [ImputeViz: A Visual Analytics Dashboard for Diagnosing Missing Data and Comparing Imputation Methods](https://arxiv.org/abs/2607.08579)

**<font color=#1a73e8>作者：</font>** Aitik Dandapat, Lalith Punepalle Raveendrareddy, Mithilesh Kumar Singh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Missing data is a persistent obstacle in scientific, social science, and public health research, often biasing analyses and placing accountability on analysts for how they handle missing values. We introduce ImputeViz, an integrated visual analytics dashboard that supports diagnosing missingness, configuring imputation models, and evaluating results. The system brings together widely used methods, including MICE, Random Forest, XGBoost, and kNN, within an interactive environment that makes missingness patterns explicit. To support geospatial reasoning, we introduce gKNN, a geographically informed kNN variant that blends socioeconomic and spatial distances and exposes donor contributions, enabling provenance-based visual accountability by showing which regions drive each estimate. Our primary contribution is a method-agnostic visual analytics environment that makes cross-method comparison a first-class visual task and integrates gKNN alongside standard methods. Coordinated views reveal missingness structure through heatmaps, co-missingness summaries, and distributional diagnostics that help analysts reason about missingness patterns (MCAR/MAR) and cases where missingness may be non-random (MNAR). Users can compare and tune models and interrogate results via distributional overlays, a Method Comparison Summary reporting MAE, RMSE, Delta RMSE, and runtime for each algorithm on the current target and mask, along with variable-level discrepancy views. Cached per-method results and locked axis scales reduce cognitive overhead from shifting ranges during method switching. These comparisons highlight where methods disagree, which variables are sensitive, and how imputation choices affect downstream summaries. Case studies demonstrate how ImputeViz helps analysts select effective strategies, surface sensitive variables, and assess model robustness.

---


### 154. [Spectral Stability of Pseudoinverse-Based Extreme Learning Machine](https://arxiv.org/abs/2607.08581)

**<font color=#1a73e8>作者：</font>** Bich Van Nguyen, Ngoc Anh Khong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Extreme Learning Machine (ELM) computes output weights analytically using the Moore-Penrose pseudoinverse. Although this leads to fast training, its numerical stability depends strongly on the conditioning of the hidden layer matrix. This paper studies pseudoinverse-based ELM from a spectral perspective. We show that the smallest singular value governs perturbation amplification in the output weights, while the condition number provides a quantitative measure of hidden-layer instability. We compare SVD-based pseudoinverse computation with iterative hyperpower methods and discuss width-dependent conditioning through a random feature interpretation. Experiments on synthetic matrices and ELM benchmarks show that SVD-based methods remain the most reliable under ill conditioning, while iterative methods are more sensitive to spectral properties. The results suggest that ELM stability is fundamentally governed by the singular value structure of the hidden layer matrix.

---


### 155. [Robust Bayesian Decision Making under Adversarial Uncertainty](https://arxiv.org/abs/2607.08590)

**<font color=#1a73e8>作者：</font>** Haripriya Harikumar, Sammie Katt, Yasir Zubayr Barlas 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scientific experiments are often designed to maximize information gain, yet in many applications the primary objective is to support reliable downstream decision-making. Existing decision-aware experimental design and active learning methods typically assume well-specified outcome models and implicitly rely on the stability of the optimal decision under real-world perturbations. In practice, however, experimental outcomes are frequently influenced by hidden or weakly modeled effects, which can substantially alter decision optimality and lead to misleading conclusions. We study sequential adversarially robust decision-aware experimental design, where data acquisition has to take into account information gain against plausible worst-case unexpected effects, modeled here as variation in adversarial variables. Building on Bayesian decision theory, we formalize an adversarially robust optimal decision under this setting and derive a principled Bayesian experimental design criterion. The criterion explicitly targets decision stability rather than nominal optimality. Experiments on synthetic and real-world scientific datasets show that conventional decision-aware design can converge rapidly to high confidence yet fragile decisions, while our robustness-aware approach yields decisions that are significantly more stable and reliable under adversarial variation.

---


### 156. [Federated Deep Learning for Privacy-Preserving Cardiovascular Disease Risk Prediction](https://arxiv.org/abs/2607.08595)

**<font color=#1a73e8>作者：</font>** Hyunho Mo, Djura Smits, Mahlet A. Birhanu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Cardiovascular disease risk prediction models often rely on data from a single institution or centrally pooled datasets. Extending these models across institutions could be limited by privacy regulations and constraints on sharing patient-level data. Federated learning enables collaborative model development without transferring sensitive patient data, but its application in healthcare remains challenging because datasets often differ in size, population characteristics, and outcome definitions. In this study, we present a federated deep learning approach for privacy-preserving cardiovascular disease risk prediction that integrates two population-based cohorts with different characteristics: Lifelines, including 148,230 participants meeting the study inclusion criteria with self-reported outcomes, and the Rotterdam Study, including a smaller cohort of 10,155 participants with digitally linked clinical outcomes. Model performance was primarily evaluated on the Rotterdam Study because of its complete follow-up. Deep survival models trained using federated learning achieved higher predictive performance than models trained locally without federation. For the Rotterdam Study, the C-statistic increased from 0.728 (95% CI: 0.717-0.739) to 0.739 (95% CI: 0.728-0.749). For Lifelines, the C-statistic increased from 0.783 (95% CI: 0.775-0.791) to 0.787 (95% CI: 0.780-0.792). These findings suggest that federated deep learning across heterogeneous cohorts can improve cardiovascular disease risk prediction while preserving the privacy of individual-level patient data.

---


### 157. [It Takes a MAESTRO To Prune Bad Experts](https://arxiv.org/abs/2607.08601)

**<font color=#1a73e8>作者：</font>** Palaash Goel, Ayush Maheshwari, Tanmoy Chakraborty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparsely-activated Mixture-of-Experts (MoE) language models achieve remarkable inference efficiency by activating only a small fraction of parameters per token, yet their full expert banks reside in memory at all times, creating a prohibitive deployment bottleneck. Existing structured pruning methods, largely designed for dense transformers, assess expert importance using locally derived heuristics that are blind to the interdependent nature of MoE routing. We introduce MAESTRO (Markov-chain Approximated Expert Sparsification via Transition-based ROuting), a structured pruning framework designed for MoE architectures that models autoregressive expert activation trajectories as Ergodic Markov chains whose stationary distributions encode cross-layer dependencies, yielding a globally aware importance heuristic. Evaluated across five diverse domains including Safety, Bias, and Ethics, MAESTRO outperforms state-of-the-art baselines by up to 10.61% in average performance retention under a strict 50% compression regime, while exhibiting substantially lower cross-task variance, indicating that global, routing-congruent pruning produces models that generalize more consistently across heterogeneous tasks.

---


### 158. [The complexities of patient-centred conversational artificial intelligence](https://arxiv.org/abs/2607.08625)

**<font color=#1a73e8>作者：</font>** João Matos, Olivia Buege, Donny Cheung 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Consumer-facing health chatbots powered by large language models (LLMs) are increasingly used for symptom assessment. However, chatbot development and evaluation often rely on cooperative, articulate, simulated patients. We analysed 2,053 real patient-chatbot conversations and found that communication patterns and expression of emotions vary widely across users. We developed a patient simulator that separately models clinical content, emotional state, conversational strategy, and communication style. In a Turing-inspired evaluation of realism with 15 human graders, simulated conversations were nearly indistinguishable from real ones, with human graders achieving an accuracy of 55%. We used five distinct patient personae, across 1,164 clinician-graded cases, to evaluate the performance of four LLMs in urgency assessment. We found that communication style can significantly alter triage outcomes. Patient-centred conversational artificial intelligence must accommodate communication diversity: systems designed for idealised, rather than realistic, interactions risk underperforming and amplifying health disparities when deployed in the real world.

---


### 159. [Steering Neural Network Training through Interpretable Constraints Based on Partial Dependence](https://arxiv.org/abs/2607.08641)

**<font color=#1a73e8>作者：</font>** Yann Claes, Pierre Geurts, Vân Anh Huynh-Thu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Over the last few years, there has been an increased interest in making machine learning models more interpretable. Although a great deal of effort goes into developing techniques for interpreting the interactions learned by a given model, fewer studies focus on assessing the quality of such explanations. Even fewer focus on how to adjust the model to produce explanations faithful to prior knowledge, a process known as explanation-guided learning. Furthermore, most approaches in this area focus on classification problems and usually assume prior knowledge about which input features or regions are most important. In this work, we introduce a new approach to steering neural networks based on partial dependence, such that their average response to certain features aligns with specific functional domain knowledge about the problem. We empirically demonstrate on a range of regression problems, including dynamical systems forecasting, that models whose training has been controlled using our method perform better than unconstrained models and are more data-efficient. Moreover, we highlight that interpretations obtained from the former actually align with the user-provided knowledge, whereas those obtained from the latter do not.

---


### 160. [DominoTree: Conditional Tree-Structured Drafting with Domino for Speculative Decoding](https://arxiv.org/abs/2607.08642)

**<font color=#1a73e8>作者：</font>** Saw S. Lin, Jyh-Shing Roger Jang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates LLM inference by drafting several tokens and verifying them in parallel. Block-diffusion drafters such as DFlash produce
a draft block in one pass but model only per-position marginals; best-first tree methods such as DDTree expand candidate trees from those marginals. The
released Domino drafter adds a GRU-based causal correction that makes each draft token's distribution path-dependent, a structure DDTree's factorized
formulation cannot represent. We introduce DominoTree, a training-free best-first draft tree scored by Domino's conditional, non-factorized correction
along each root-to-node path, made practical by restricting the per-node correction to a candidate top-M. On Qwen3-4B across eight benchmarks, DominoTree
reaches up to 6.6x speedup over autoregressive decoding and the highest mean accept length of any evaluated method, up to 10.7 tokens per round, at every
temperature we test. DominoTree constructs its tree with a GPU-native, CUDA-graph builder that is bit-identical to a reference Python implementation, so
acceptance is unchanged, while keeping per-round tree construction cheap. With this builder as default, DominoTree wins throughput over the released
Domino decoder at every temperature, 9-10% overall on Qwen3-4B and up to +22% on Alpaca, and over DDTree/CaDDTree at every temperature we test. On Qwen3-
8B, DominoTree keeps the highest accepted length at every temperature and adds a decisive throughput win at T=0, +24% over DDTree; at higher temperature
that edge over DDTree/CaDDTree narrows to a tie and a small loss, while its Overall aggregate wins over DFlash and Domino persist.

---


### 161. [Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning](https://arxiv.org/abs/2607.08647)

**<font color=#1a73e8>作者：</font>** Ali Larian, Qian Lin, Chang Zong Wu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As autonomous agents are increasingly deployed across diverse operational contexts, aligning their behavior with human intent demands reward functions that remain robust to such changes rather than overfitting to any single environment. Inverse reinforcement learning (IRL) provides a principled way to infer such objectives from human feedback. However, existing analyses of optimal teaching approaches for IRL focus on single-environment, demonstration-only settings, leaving underexplored how heterogeneous feedback modalities and environment dynamics jointly constrain reward functions that generalize across multiple environments. Because demonstrations in one MDP entangle reward information with that environments specific structure, the resulting rewards frequently fail to generalize when the agent is deployed in a new setting. We first analyze how different feedback modalities constrain rewards, showing that, in the unlimited-data regime, comparisons impose strictly stronger global constraints than other modalities. Beyond this theoretical analysis, we introduce a hierarchical machine teaching algorithm for reward learning that operates across multiple MDPs. The algorithm first greedily selects informative environments that expose complementary reward constraints, then strategically queries low-cost feedback within those environments. Empirically, our method achieves substantially lower regret and stronger generalization to held-out environments than uniform teaching baselines under identical feedback budgets, demonstrating the importance of multi-environment, multi-modal teaching for learning dynamics-robust reward functions.

---


### 162. [Secure Decentralized Federated Learning via Gossip and Virtual Voting](https://arxiv.org/abs/2607.08651)

**<font color=#1a73e8>作者：</font>** Amirhossein Taherpour, Xiaodong Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Decentralized federated learning (DFL) removes the central server by letting nodes exchange model updates through peer-to-peer gossip, but existing gossip-based methods often lack provenance finality and resilience to Byzantine or lazy participants. Ledger-assisted federated learning (FL) improves auditability, yet blockchains, shards, or settlement committees can reintroduce global coordination costs that conflict with DFL locality. This paper proposes \emph{gspDAG-FL}, a secure DFL framework that derives consensus from the same gossip history used to disseminate models. Nodes exchange model payloads only with neighbors, while full nodes collect event certificates and receiver-endorsed accepted gossip proofs, reconstruct a compact Topology directed acyclic graph (DAG), and run Hashgraph-style virtual voting followed by compact full-node certificates. Finality is over unique model-origin tuples, not identical local parameter states. To improve resilience, gspDAG-FL combines payload validation, accepted-proof validation, and private semantic audit before aggregation. We formalize the adversarial setting, prove safety and conditional liveness of the control plane, and give a convergence guarantee for certified perturbed gossip under time-varying effective mixing. Experiments on MNIST classification and Penn Treebank language modeling, using fair held-out validation/audit data and networks up to \(N=100\), show that gspDAG-FL achieves learning quality close to validation-based ledger FL while reducing coordination bottlenecks, improving throughput, and maintaining high invalid-origin detection under mixed Byzantine and lazy participation.

---


### 163. [Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study](https://arxiv.org/abs/2607.08652)

**<font color=#1a73e8>作者：</font>** Eugene Ng Yi Sheng, Bingquan Shen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-interested agents, left unconstrained, tend toward defection in repeated social dilemmas, causing cooperative gains from trade to collapse. This paper investigates what formal mechanisms, layered on top of unrestricted communication, are sufficient for a society of such agents to maintain market stability, and how resilient those mechanisms are to adversarial attack. We instantiate the research question as a multi-agent marketplace simulation where 18 LLM agents (DeepSeek-V3) with complementary production specialties must trade within a constrained social network to obtain utility. We conduct two experimental phases: (1) a mechanism comparison across eight conditions under progressive troll injection over 200 rounds, identifying Mediation as the top-performing mechanism; and (2) adversarial red-teaming of Mediation using iteratively prompt-optimised LLM-driven trolls, finding that the best attack (v6) reduces honest-agent utility by 13.3% but cannot collapse the market. Mediation enables recovery even under sustained adversarial pressure. We define adversarial robustness as a mechanism's ability to sustain positive honest-agent utility under optimised attack, and find that Mediation is robust: it can be bent but not broken.

---


### 164. [EdgeRefine: Privacy-Utility Balance for Graphs via Jaccard Sampling under Edge Differential Privacy](https://arxiv.org/abs/2607.08659)

**<font color=#1a73e8>作者：</font>** Wenxiu Ding, Muzhi Liu, Zheng Yan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Neural Networks (GNNs) have shown considerable success in learning from graph-structured data, but their use in privacy-sensitive areas remains difficult because graph structure can leak sensitive link information. To satisfy edge-level differential privacy, a common approach is to inject noise into all elements of the graph's adjacency matrix, thereby obfuscating the existence of any single edge. However, stronger privacy requires more noise, and excessive noise reduces utility, making the privacy-utility balance a major barrier to practical privacy-preserving graph learning.
To address this issue, we propose EdgeRefine, a local differential privacy framework that improves this trade-off through adaptive edge refinement. EdgeRefine first estimates edge-existence probabilities using Jaccard similarity and ranks edges for noisy edge removal. To ensure the sparsity and reliability of the final graph, it uses the privacy budget $\epsilon$ to determine the ratio of true to false edges, samples them separately based on this probability ranking, and controls the total number of edges with a separate sampling rate $k$. Extensive experiments show that EdgeRefine achieves accuracy comparable to the noise-free baseline and substantially outperforms other privacy-preserving methods across datasets and GNN architectures. Under privacy budget $\epsilon = 2.5$, EdgeRefine improves node classification accuracy over state-of-the-art baselines by 17.8\% on ACM under GAT and 19.7\% on Cora under GCN. In graph classification, it achieves an average accuracy degradation of around 5\% compared to the noise-free baseline. Under graph reconstruction attacks, EdgeRefine maintains relative absolute error levels above 1 across all privacy budgets, averaging 1.962 on Cora and 1.472 on AMAP, indicating strong resilience against privacy leakage.

---


### 165. [TRM-Raft: A Byzantine-Resistant Raft Consensus via Integrated Trust and Reputation Model](https://arxiv.org/abs/2607.08666)

**<font color=#1a73e8>作者：</font>** Jie Zhang, Xubo Fan, Xiaohong Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Internetware envisions autonomous software entities collaborating over the open Internet. Raft consensus is widely adopted for its simplicity and performance in distributed coordination, e.g., service registries and blockchains. However, Raft assumes crash faults only, making it vulnerable to Byzantine behaviors like election forgery and log tampering. Existing BFT protocols incur high overhead, while ad-hoc hardening lacks unified defense.
We propose \textbf{TRM-Raft}, a Byzantine-resistant enhancement that non-intrusively integrates a Blockchain-based Trust and Reputation Model (B-TRM) into the consensus core. It quantifies multi-dimensional node behaviors, applies adaptive penalties distinguishing accidental faults from malice, and embeds reputation into leader election and log replication. A reputation-aware election penalizes term/index forgery, excluding low-reputation nodes from leadership. A Schnorr-signature-based mechanism lets followers verify log integrity; tampering triggers reputation decay and leader replacement. Evaluated on Hyperledger Fabric in a realistic Internetware setting, TRM-Raft keeps malicious leader ratio below 5\% even with 40\% Byzantine nodes, with <10\% throughput loss and <5\% latency increase over vanilla Raft. TRM-Raft offers a lightweight, practical trustworthiness path for Internetware systems relying on Raft.

---


### 166. [Do Transformations Reveal the Truth? Generative Residual Learning for Generalized AI-Generated Image Detection](https://arxiv.org/abs/2607.08674)

**<font color=#1a73e8>作者：</font>** Kutub Uddin, Nusrat Tasnim, Awais Khan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of generative AI has enabled the creation of highly realistic deepfake media, posing significant threats, including misinformation, digital identity theft, fraud, and manipulation of public opinion. AI-generated image (AIGI) detection is reliably challenging due to the diversity of generative methods and the subtle artifacts they leave behind. In this work, we propose GenRes, a novel framework for generative residual learning via a neural tensor network, which models fine-grained relational features between original and transformed samples to enhance generalization. To address scenarios involving multiple generative transformations, we introduce GenRes++, which employs a learnable attention mechanism to aggregate relational features across multiple transformed samples and enables the model to focus on the most informative cues. Both models leverage PE-Core as a feature extractor, providing generalized and semantically rich embeddings that improve cross-domain performance and enable the detection of AIGI generated by unseen methods. Comprehensive experiments on multiple benchmark datasets demonstrate that the proposed GenRes++ approach outperforms existing methods.

---


### 167. [Multi-Resolution Feature Stem for Diabetic Retinopathy lesion segmentation](https://arxiv.org/abs/2607.08679)

**<font color=#1a73e8>作者：</font>** Indranil Dutta, Taehee Jeong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diabetic Retinopathy (DR) is a leading cause of preventable blindness worldwide, requiring automated lesion segmentation using deep learning models for early detection and monitoring. However, DR lesions vary dramatically in size from tiny microaneurysms to large hemorrhages and exudates. This variability creates conflicting demands on the model architecture and input resolution, posing a challenge for effective design. This work investigates the impact of input resolution on different lesion types. Through systematic experimentation with multiple architectures (U-Net, UNet++, Vision Transformers, DeepLabV3+) at $512 \times 512$ and $1024 \times 1024$ resolutions, we identify a critical, counter-intuitive phenomenon where increasing input resolution has opposing effects on different lesion types. We demonstrate that while higher resolution is essential for resolving fine-grained microaneurysms, it can unexpectedly degrade performance on larger hemorrhages. This finding challenges the common assumption that higher resolution is uniformly beneficial. To address this, we propose a novel Multi-Resolution Feature Stem, an input-level pyramid integrated with a UNet++ backbone. This architecture processes multiple scales in parallel, capturing fine-grained details without sacrificing contextual information. This work contributes crucial empirical evidence of this complex, resolution-dependent behavior and a practical, parameter-efficient architecture that successfully resolves this trade-off.

---


### 168. [SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets](https://arxiv.org/abs/2607.08681)

**<font color=#1a73e8>作者：</font>** Shilin Ou, Yifan Xu, Luyao Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As agentic AI systems are increasingly applied to cyber-physical environments, their evaluation requires assessment of both task performance and trustworthiness. In decentralized energy markets, autonomous agents may improve market utility, but may also exploit invalid physical data, create artificial liquidity, and produce unstable governance decisions. Therefore, we propose SolarChain-Eval, a physics-constrained benchmark for evaluating trustworthy economic agents. It formulates market governance as a Gymnasium-compatible Markov Decision Process, where agents make hourly decisions. SolarChain-Eval evaluates each policy across multiple dimensions, including market utility, physical safety, slippage, action smoothness, spatial fairness, and auditability. To support agentic evaluation, SolarChain-Eval incorporates an LLM-based Planner/Auditor layer. The Planner defines episode-level action bounds and audit rules, while the Auditor reviews and revises high-risk actions. All interventions are recorded through structured logs, including trigger signals, proposed actions, revised actions, and audit rationales. Experiments with static, random, myopic, RL, and RL+LLM policies reveal a clear utility-safety trade-off. RL agents improve market utility but can still produce unsafe behavior. When the physics penalty is removed, reward-maximizing agents exploit invalid generation and increase artificial liquidity. The LLM Planner/Auditor improves auditability and mitigates selected risks, but it cannot fully compensate for a misspecified reward function. These results indicate that trustworthy agentic AI evaluation requires both physical constraints and transparent intervention traces. We release data and code as open access on GitHub for replicability.

---


### 169. [SAM-MT: Real-Time Interactive Multi-Target Video Segmentation](https://arxiv.org/abs/2607.08688)

**<font color=#1a73e8>作者：</font>** Ruiqi Shen, Chang Liu, Henghui Ding  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern Video Object Segmentation (VOS) involves tracking and segmenting user-specified targets. While recent approaches have achieved remarkable performance in single-target scenarios, extending them to multi-target settings typically involves replicating the single-target processing for each individual object, resulting in reduced frame rates (FPS) with unbounded latency as target count increases. Built upon Segment Anything 2 (SAM2), we propose SAM-MT, which addresses this by transforming the model into an interactive framework for real-time Multi-Target video segmentation. SAM-MT uses explicit queries to represent different individual targets, in parallel with a shared representation for global context. It employs decoupled masked attention to keep individual identities distinct from cross-target interference, and sparse memory for stable temporal evolution, along with specialized strategies for occlusion handling and overlap prevention. SAM-MT successfully decouples latency from the number of targets, achieving real-time speed on par with single-target baselines (>36 FPS for 10 targets) while maintaining SAM2's robust video segmentation performance.

---


### 170. [A Practical Investigation of Training-free Relaxed Speculative Decoding](https://arxiv.org/abs/2607.08690)

**<font color=#1a73e8>作者：</font>** Guoxuan Xia, Luka Ribar, Paul Balanca  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates sampling from an autoregressive LLM by using a faster auxiliary model to draft tokens which are then verified in parallel by the LLM. Standard speculative decoding is lossless: its rejection and resampling steps exactly preserve the LLM's sampling distribution. Recent work argues that relaxing this strict guarantee can yield further speed-ups, controlled capability-speed trade-offs, or even capability gains. We practically investigate training-free relaxed speculative decoding techniques, unify existing approaches within a shared framework, benchmark them on contemporary settings, and distil takeaways and empirical findings for practitioners. Important takeaways include: relaxation can require considerable capability evaluation unlike lossless speculative decoding, and many relaxed approaches rely on a drafter that is a good language model, making them unsuited for lightweight dedicated multi-token-prediction drafters.

---


### 171. [MPFlow: Learning Budgeted Max-Flow Optimization on the Lightning Network with Deep Graph Reinforcement Learning](https://arxiv.org/abs/2607.08703)

**<font color=#1a73e8>作者：</font>** Harrison Rush, Vincent Davis, Simone Antonelli 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We address liquidity placement in the Bitcoin Lightning Network (LN): given a fixed budget, which channels should a node open to maximize its routing capacity? We cast this as a budget-constrained combinatorial optimization problem on graphs, selecting $k$ edge additions that maximize $s$--$t$ max-flow, a theory-grounded measure of routing capacity, and solve it with graph reinforcement learning. Our lightweight agent combines a message-passing policy network with proximal policy optimization (PPO) and action masking, and is trained under a hub-exclusion curriculum: the network's top hubs are removed from training subgraphs, forcing the policy to learn capacity-aware placement rather than hub attachment. In extensive experiments on real Lightning Network snapshots, our method consistently outperforms strong heuristic baselines on the max-flow objective across multiple seeds and unseen graphs. The agent has been deployed in production for peer recommendations, executing 4640 channel-open decisions that cumulatively allocate 267.3 BTC over $16 million across 30 managed nodes.

---


### 172. [HumanForge: A Human-Centric Deepfake Video Benchmark with Multi-Agent Forgery Rationales](https://arxiv.org/abs/2607.08705)

**<font color=#1a73e8>作者：</font>** Wenbo Xu, Zhimin Chen, Xiaojie Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Rapid advancements in video diffusion models and temporal editing tools have enabled the generation of highly realistic human-centric videos, posing unprecedented challenges to digital content forensics. Existing benchmarks primarily focus on either face-swapping or global text-to-video synthesis, overlooking the crucial dimensions of human-object or human-human interactions and multi-modal alignment. To address these limitations, we introduce HumanForge, a unified, large-scale, and multi-paradigm human-centric video forgery dataset. To construct and annotate this dataset without labor-intensive manual labeling or hallucinated monolithic prompts, we propose Gen2Anno, a modular active multi-agent pipeline built on LangGraph. Gen2Anno coordinates six specialized agents-ranging from source profiling to MoE-based reference analysis and closed-loop forensic verification-to generate over 18K high-fidelity video segments and produce structured, contrastive omni-annotations containing binary decisions, fine-grained artifact categories, and spatio-temporal localization. Extensive benchmarks using state-of-the-art traditional detectors and Large Multimodal Models (LMMs) demonstrate the significant challenges of zero-shot generalization and fine-grained reasoning on HumanForge. Code and dataset will be publicly released.

---


### 173. [LTM: Large-scale Terrain Model for Wildfire-prone Landscapes](https://arxiv.org/abs/2607.08711)

**<font color=#1a73e8>作者：</font>** Xiao Fu, Yue Hu, Meida Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Accurate 3D terrain maps are essential for emergency response when assessing wildfire hazards. However, wildfire-prone regions often span vast areas where conventional reconstruction methods underperform. Airborne LiDAR systems provide high-resolution terrain data, but they are expensive and infrequently updated. Image-based methods offer a lower-cost alternative, but struggle due to sparse visual features and limited image overlap. We propose a multi-modal reconstruction framework leveraging outdated Digital Elevation Models (DEMs) as geometric priors for image-based 3D reconstruction. Our key innovation is physics-based pixel-pixel alignment between images and DEM data, dramatically reducing computational complexity by eliminating expensive feature matching procedures. To validate our approach, we developed a large-terrain simulator based on a real wildfire-prone area, generating realistic images enabling a comprehensive evaluation. Given posed images and legacy DEMs, our method produces high-fidelity depth maps while maintaining real-time performance. We find significant improvements in reconstruction accuracy and computational efficiency over existing techniques, offering a scalable solution for wildfire response.

---


### 174. [Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents](https://arxiv.org/abs/2607.08716)

**<font color=#1a73e8>作者：</font>** Yifan Wu, Lizhu Zhang, Yuhang Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In long-horizon tasks, decision-relevant state is often scattered across an expanding trajectory, while the action agent must surface it and act. As trajectories grow, task requirements, environment facts, prior attempts, diagnoses, and open subgoals can be buried in the context window or pushed beyond it, failing to influence decisions when needed. We call this failure mode "behavioral state decay". We study memory as an active intervention mechanism rather than passive retrieval. A separate memory agent runs alongside an unmodified action agent, updating a structured memory bank from the recent trajectory and deciding whether to inject a memory-grounded reminder or remain silent. The module is plug-and-play with frontier action agents and existing agent harnesses. Across Terminal-Bench 2.0 and $\tau^2$-Bench, it improves pass@1 for both weaker and stronger action agents, with gains of +8.3 pp on Terminal-Bench and +6.8 pp on $\tau^2$-Bench. Ablations show that selective intervention outperforms passive bank exposure, always-on injection, advisor-only guidance, and general retrieval. As an early step toward open-weight memory policies, we train Qwen3.5-27B on SETA using SFT and GRPO, improving validation reward and achieving partial transfer to Terminal-Bench.

---


### 175. [Deep Learning for Joint Narrowband Interference Cancellation and Soft Demodulation in OFDM Systems](https://arxiv.org/abs/2607.08717)

**<font color=#1a73e8>作者：</font>** Emmanouil Kavvousanos, Francky Catthoor, Vassilis Paliouras  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Narrowband interference (NBI) severely degrades orthogonal frequency-division multiplexing (OFDM) systems by corrupting subcarriers and rendering classical soft demodulation ineffective. Conventional compressed-sensing (CS) mitigation exhibits high sequential latency and leaves structured, non-Gaussian residuals that cause log-likelihood ratio (LLR) unreliability, decoder saturation, and severe error floors when employing classical Gaussian demappers. We resolve this pipeline mismatch using a unified deep learning framework for joint NBI cancellation and robust soft demodulation. First, NBI-CNet employs a physics-informed convolutional architecture to estimate NBI parameters and remove multi-tone interference in a single forward pass. Without requiring prior knowledge of the active interferer count, NBI-CNet reduces computational complexity by up to 60% ($N{=}2048, Q{=}64$) compared to the state-of-the-art EOMP-IDS algorithm. Second, LLR-CNet acts as a structural whitener by mapping non-Gaussian post-mitigation residuals onto well-calibrated soft metrics. Simulations demonstrate that this joint framework eliminates the error floors inherent to traditional baselines across dense grids. Under severe interference ($\text{SIR}{=}{-}10$ dB), the pipeline operates within a $0.2$ to $0.5$ dB SNR margin of the optimal iterative baseline at a target block error rate (BLER) of $10^{-4}$. Under mild interference ($\text{SIR}{=}10$ dB) with heavy spectral overlap ($Q{=}12$), where classical greedy algorithms erroneously subtract valid data components and corrupt the payload, NBI-CNet avoids signal-peak confusion to deliver a coding gain exceeding $3$ dB. Finally, the architecture circumvents the $2{\times}10^{-4}$ error floor triggered by interferer-estimation errors, while its scale-invariant design enables robust generalization across arbitrary FFT sizes without retraining.

---


### 176. [Latent Memory Palace: Reasoning for Control as Autoregressive Variational Inference](https://arxiv.org/abs/2607.08724)

**<font color=#1a73e8>作者：</font>** Chuning Zhu, Eva Xu, Jose Barreiros 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Human decision-making is highly flexible -- some actions are taken immediately; others require longer deliberation. Language models have exhibited a similar capacity for adaptive "reasoning." However, transferring this capability to continuous control policies has been challenging, as directly reasoning in language space may lack the granularity for spatial understanding and precise motions. In this work, we show that reasoning for control policies can emerge by organizing information in an autoregressive latent space reminiscent of a memory palace, where retrieval is iterative and adaptive. Our method, Latent Memory Palace (LMP), formulates reasoning as variational inference with an autoregressive latent distribution. We derive a latent-space reinforcement learning technique to tractably optimize its variational lower bound. The resulting policy, LMP-$\pi$, achieves strong empirical performance in simulation and real-world domains while exhibiting interpretable, adaptive allocation of test-time compute. We further show that the same framework yields a variable-length action tokenizer, LMP-$\texttt{tok}$, which significantly improves the performance of downstream autoregressive policies. Together, these results present a new perspective on latent reasoning for control through the lens of variational inference.

---


### 177. [Pose-to-Biomechanics: Bridging 3D Human Pose Estimation and Biomechanical Attribute Prediction](https://arxiv.org/abs/2607.08725)

**<font color=#1a73e8>作者：</font>** Ayda Eghbalian, Kevin Desai  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent progress in 3D human pose estimation has made markerless recovery of skeletal motion increasingly accurate and scalable. However, most pose estimators remain optimized for geometric keypoint accuracy, while many real-world applications in rehabilitation, sports science, ergonomics, and clinical movement analysis require biomechanical quantities that describe how the body moves, loads, and activates. In this work, we propose BioModule, a lightweight plug-in temporal transformer that attaches downstream of any 3D pose estimator and predicts biomechanical attributes from standard 17-joint 3D skeletons. BioModule is estimator-agnostic and requires no modification of the upstream pose model, enabling existing pose estimators to be extended toward physically interpretable motion analysis.
To train and evaluate BioModule, we construct a large-scale aligned dataset pairing Human3.6M video and 3D keypoints with the biomechanical label space of Human3.6Mplus. We establish and verify anatomical correspondence between coordinate systems of the two datasets, enabling frame-accurate cross-modal supervision. Using this aligned supervision, BioModule predicts biomechanical quantities. We further benchmark BioModule across seven state-of-the-art 3D pose estimators, providing the first systematic analysis of how upstream pose estimation quality propagates to downstream biomechanical prediction fidelity. The results position BioModule as a compact, modular bridge between vision-based pose estimation and biomechanically meaningful human motion analysis.

---


### 178. [WaspMOT: A Benchmark for Long-Term Multi-Object Tracking of Trichogramma Wasps](https://arxiv.org/abs/2607.08729)

**<font color=#1a73e8>作者：</font>** Tomasz Stanczyk, Yuan Gao, Hardik Agarwal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-object tracking (MOT) has achieved strong performance on benchmarks dominated by short video sequences. However, such datasets do not adequately evaluate long-term identity preservation, where objects must be tracked consistently over extended durations. We introduce WaspMOT, a benchmark designed to address this gap through long-duration tracking of Trichogramma wasps in controlled ecological experiments. The dataset contains 10 sequences of approximately 12,000 frames each (over 8 minutes at 25 FPS), with dense MOTChallenge annotations and oracle detections to isolate association performance.
Unlike existing benchmarks, WaspMOT forms a closed-set tracking scenario where all individuals remain present throughout the sequence, requiring consistent identity assignment across thousands of frames despite abrupt jumps, occlusions, and highly similar appearance. We establish a benchmark by evaluating five tracking-by-detection methods, including ByteTrack, BoT-SORT, C-BIoU, OC-SORT, and McByte, under a unified protocol. Results show that all methods suffer from significant trajectory fragmentation, highlighting the difficulty of long-term identity preservation even with perfect detections. A simple spatial tracklet stitching baseline consistently improves performance, indicating that substantial gains remain possible.
WaspMOT provides a new benchmark for studying long-term association and reveals limitations of current tracking approaches that are not observable on conventional datasets. The benchmark will be made publicly available at the project repository: this https URL .

---


### 179. [Sculptable Mesh Structures for Room-Scale Form-Finding](https://arxiv.org/abs/2607.08736)

**<font color=#1a73e8>作者：</font>** Jesse T. Gonzalez, Yanzhen Zhang, Dian Zhu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> It can be hard to design a physical structure entirely within the confines of a computer monitor. To better capture the interplay between real-world objects and a designer's work-in-progress, practitioners will often go through a sequence of low-fidelity prototypes (paper, clay, foam) before arriving at a form that satisfies both functional and aesthetic concerns. While necessary, this model-making process can be quite time-consuming, particularly at larger scales, and the resulting geometry can be difficult to translate into a CAD environment, where it will be further refined.
This paper introduces a user-adjustable, room-scale, "shape-aware" mesh structure for low-fidelity prototyping. A user physically manipulates the mesh by lengthening and shortening the edges, altering the overall curvature and sculpting coarse forms. The edges are equipped with resistive length sensors, and transmit their configuration to a central computer. The structure can later be reproduced in software, connecting this prototyping stage to the larger computational design pipeline.

---


### 180. [Dimensionality Reduction Meets Network Science: Sensemaking on UMAP's kNN Graph](https://arxiv.org/abs/2607.08746)

**<font color=#1a73e8>作者：</font>** Duen Horng Chau, Donghao Ren, Fred Hohman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> While UMAP is widely used for exploring high-dimensional data, typical workflows focus on its lower-dimensional embedding, largely overlooking the rich k-nearest-neighbor (kNN) graph that UMAP constructs internally. This graph encodes the data manifold in its original high-dimensional space, before the distortion that UMAP's 2D projection introduces. We demonstrate the untapped potential of this internal representation, showing how standard graph algorithms applied to this graph enhance data sensemaking: (1) PageRank identifies representative data points, (2) k-core decomposition reveals dense core regions versus sparse periphery, and (3) clustering coefficient detects tight-knit neighborhoods with highly-similar data points. Through quantitative and qualitative evaluation on MNIST and Fashion MNIST, we show that these graph-based analyses are not only practical but also competitive with or complementary to purpose-built methods (e.g., k-medoids for exemplar selection, HDBSCAN for density-based clustering).

---


### 181. [Using AI-based Learning Assistants in Higher Education: A Large-Scale Descriptive Analysis](https://arxiv.org/abs/2607.08748)

**<font color=#1a73e8>作者：</font>** Kristina Schaaff, Quintus Stierstorfer, Valerie Heckel  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this study, we present a large-scale descriptive analysis of the use of an AI-based learning assistant (Syntea) in higher education. Based on objective log data from 77,543 students enrolled in distance studies, we examine usage patterns across gender, age group, study cluster, degree, and study mode. To date, existing research on educational chatbots has largely relied on comparatively small samples and self-reported survey data, while large-scale evidence on actual usage behavior remains limited. Our findings show that Syntea is already embedded in the study routines of many learners, but that usage differs across demographic and structural contexts. By identifying these patterns, our study provides an empirical basis for the further development of AI-based learning support and contributes a large-scale analysis of educational chatbot usage in higher education.

---


### 182. [SLORR: Simple and Efficient In-Training Low-Rank Regularization](https://arxiv.org/abs/2607.08754)

**<font color=#1a73e8>作者：</font>** David González-Martínez, Shiwei Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-rank factorization is widely used to compress neural networks, but modern models are often not naturally amenable to aggressive factorization without significant accuracy loss. Existing training-time low-rank regularizers can improve compressibility, but they often require SVDs of large weight matrices, modify the model architecture (introducing additional trainable parameters), or rely on stateful cached quantities. To address these limitations, we introduce SLORR, a simple, stateless, and architecture-preserving framework for in-training low-rank regularization, instantiated with two main variants based on the Hoyer sparsity metric and the nuclear norm. SLORR directly regularizes the original weight matrices using GPU-friendly approximations for the forward and backward passes of the regularizers, for which we provide approximation guarantees. We first evaluate SLORR on ImageNet-1K across short-horizon continued training of ResNet-50, ViT-B/16, and ViT-L/16, and pretraining of ResNet-18, where SLORR induces compressibility while introducing less than 8% training overhead. We further evaluate SLORR-Hoyer in LLM pretraining at 135M and 560M scales: SLORR-trained compressed models preserve performance substantially better than unregularized models while adding less than 1% average training overhead.

---


### 183. [Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation](https://arxiv.org/abs/2607.08758)

**<font color=#1a73e8>作者：</font>** Yifan Zhou, Qihao Yang, Yan Li 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Scientific ideas rarely start from a blank page. They inherit mechanisms, repair known limitations, and recombine pieces of earlier work, much like biological genomes. Current benchmarks still say little about whether AI systems can follow this inheritance structure. We present IdeaGene-Bench (IG-Bench), a benchmark for scientific lineage reasoning and lineage-grounded idea generation. IG-Bench is organized around the IdeaGene framework: each paper or proposal is represented as a set of minimal, typed, evidence-grounded Idea Genome objects, and a GenomeDiff aligns these objects to record inheritance, mutation, loss, external import, and novel insertion under six operational evolutionary dynamics. The benchmark contains 1,961 golden lineage traces, 1,085 curated Idea Genome objects, and 920 pairwise GenomeDiff records across 10 scientific domains. It supports two evaluations. IG-Exam (42 task types, 1,029 instances) tests closed-form lineage reasoning across Idea Genome abstraction, inheritance tracing, evolutionary reasoning, and lineage verification. IG-Arena evaluates generation with a lineage-conditioned Population-Evolution Score(PES), asking whether a proposal can be inserted as a coherent descendant of a given lineage population: it should inherit the right Idea Genome objects, vary meaningfully from nearby work, and offer selection value for future research. Experiments on 14 LLM-based scientists expose a compositional bottleneck. The strongest system reaches only 27.3% exact accuracy on lineage reasoning, and structured lineage context reshuffles system rankings rather than helping every participant uniformly.

---


### 184. [OpenCoF: Learning to Reason Through Video Generation](https://arxiv.org/abs/2607.08763)

**<font color=#1a73e8>作者：</font>** Xinyan Chen, Ziyu Guo, Renrui Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning has become a core capability for large models, especially when reliable decisions require understanding logical consequences. Recent video generation models offer a reasoning path distinct from previous Chain-of-Thought (CoT): reasoning can unfold through temporally connected frames, known as Chain-of-Frame (CoF) reasoning. However, existing video generators are primarily trained on general video corpora, still lacking diverse supervision and dedicated designs for CoF reasoning. To address this gap, we introduce OpenCoF, a framework comprising the OpenCoF-17K dataset, a reasoning video dataset spanning 11 task families, and Wan-CoF, a fine-tuned video model for studying whether diverse temporal supervision improves CoF behavior. Across four video reasoning benchmarks, Wan-CoF achieves considerable gains over the Wan2.2-I2V-A14B baseline. Building on this, we empirically explore more advanced designs for CoF capabilities, i.e., equipping the model with visual and textual reasoning tokens. This mechanism respectively captures low-level visual cues and high-level semantic priors for spatial and temporal reasoning. Through performance comparisons and attention analysis, we examine how these tokens contribute across model depth, denoising steps, space, and time. Our results suggest that stronger video reasoning requires both broad temporal supervision and explicit mechanisms for organizing intermediate reasoning state. We open-source the dataset, model, and code to facilitate future research on reasoning-oriented video generation.

---


### 185. [Enhancing In-context Panoramic Generation via Geometric-aware Pretraining](https://arxiv.org/abs/2607.08765)

**<font color=#1a73e8>作者：</font>** Haoran Feng, Ruiyang Zhang, Longyi Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> In this work, we present Canvas360, a two-stage framework for in-context panoramic generation that combines geometry-aware pretraining with downstream task-specific fine-tuning. To address the lack of large-scale, high-quality training data tailored to in-context panoramic tasks, we propose Canvas360Dataset, a collection of 1M high-quality paired panoramic samples for style transfer, inpainting, outpainting, and editing, enabling effective supervision across diverse in-context generation scenarios. On the modeling side, Canvas360 enhances text-to-panorama generation through parallel depth generation, velocity circular padding, and similarity loss regularization, enabling the model to learn geometry-aware representations, capture object distortion details, and improve geometric consistency and global coherence. Furthermore, empowered by strong panoramic priors, Canvas360 enables a unified in-context panoramic generation framework that supports diverse downstream tasks via token-level concatenation, surpassing prior methods in both task coverage and modeling flexibility. Extensive experiments show that Canvas360 improves panoramic image fidelity, achieving particularly strong performance on the panorama-specific FAED metric and competitive or leading results across the reported quantitative evaluations. More information can be found on our project page: this https URL

---


### 186. [Geometry and Gradient-based Partitioning for Panoramic Outdoor Reconstruction](https://arxiv.org/abs/2607.08769)

**<font color=#1a73e8>作者：</font>** Weijian Chen, Weibo Yao, Yuhang Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scaling 3D Gaussian Splatting (3DGS) to large outdoor scenes is costly in both data acquisition and computation. Adopting panoramic images with equirectangular projection (ERP) can reduce capture effort via their full $360^{\circ}$ field of view, yet the resulting omnipresent visibility invalidates existing partitioning strategies that rely on local camera frustums, causing block-wise optimization to degenerate into global training. Thus, we propose PanoLOG, a two-stage coarse-to-fine framework equipped with a Geometry and Gradient-based Partitioning Strategy tailored for large-scale panoramic 3DGS reconstruction. In the global coarse stage, PanoLOG leverages sky-sphere modeling and panoramic monocular depth supervision for reliable geometry, while in the refinement stage, G$^2$PS builds adaptive bounding volumes via parallax-driven uncertainty and assigns cameras via gradient-based importance scoring. Furthermore, we construct Pano360, the first benchmark on large-scale panoramic dataset for outdoor scene reconstruction. Extensive experiments demonstrate that G$^2$PS achieves state-of-the-art rendering quality while maintaining scalable, block-parallel training. Our models, training code, and dataset are publicly available.

---


### 187. [LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models](https://arxiv.org/abs/2607.08770)

**<font color=#1a73e8>作者：</font>** Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recovering high-quality video from sparse event streams is a challenging task. Regression methods often blur textures, while existing generative models struggle with long-term stability. We propose LongE2V, a novel approach that leverages pre-trained video diffusion priors to jointly handle event-based video reconstruction, prediction, and frame interpolation. By fine-tuning a foundational video model, our approach achieves high data efficiency and superior perceptual quality. We introduce Autoregressive Unrolling and Adaptive Context Switching to mitigate temporal drift in extremely long sequences. We also propose Reencoding Alignment with Cross Residual Correction to ensure precise bidirectional consistency during frame interpolation. Furthermore, Event Voxel Density Augmentation ensures robustness across varying sensor resolutions. Extensive experiments on real-world benchmarks demonstrate that LongE2V outperforms state-of-the-art methods across all three tasks, exhibiting exceptional temporal coherence and zero-shot generalization. Project page: this https URL

---


### 188. [ZipDepth: Bringing Lightweight Zero-Shot Monocular Depth Anywhere, on Any Device](https://arxiv.org/abs/2607.08771)

**<font color=#1a73e8>作者：</font>** Fabio Tosi, Luca Bartolomei, Matteo Poggi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Monocular depth estimation has seen remarkable progress through foundation models achieving robust zero-shot generalization, yet their computational demands place them far beyond the reach of embedded and mobile platforms. Lightweight alternatives exist, but have been developed almost exclusively within single-domain, self-supervised paradigms, failing silently under domain shift. We present ZipDepth, a compact monocular depth network that bridges this gap by combining an efficient reparameterizable encoder-decoder with large-scale knowledge distillation from a foundation model over a large multi-domain training set. Comprising just 6.1M parameters, ZipDepth runs at real-time rates from server GPUs to power-constrained devices, achieving the best trade-off between zero-shot accuracy and deployment efficiency among lightweight models across five benchmarks, taking a significant step towards the accuracy of foundation models with 50x more parameters.

---


### 189. [Wat3R: Underwater 3D Geometry Learning without Annotations](https://arxiv.org/abs/2607.08772)

**<font color=#1a73e8>作者：</font>** Jiangwei Ren, Xingyu Jiang, Zijie Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Estimating 3D geometry in underwater environments presents unique challenges due to light attenuation, scattering, and the absence of large-scale, high-quality 3D annotations. Pioneering methods rely on massive dense annotations that are impractical in underwater settings. In this paper, we propose Wat3R, a cross-domain semi-supervised learning framework designed to adapt feed-forward 3D reconstruction models from air to underwater scenes. Uniquely, our method eliminates the need for any annotated underwater data following a teacher-student architecture, that learns robust geometry representations merely on abundant unlabeled real underwater video footage. We also design a cross-view consistency loss that leverages geometric cues from other views to compensate for the information degradation in the current view caused by water attenuation and scattering. Furthermore, considering the lack of comprehensive evaluation benchmarks, we construct Water3D, a diverse dataset covering various water bodies and underwater scenarios, designed for geometric task evaluation. Experimental results demonstrate that Wat3R outperforms current state-of-the-art methods in underwater multi-view depth estimation and point cloud reconstruction. The dataset and code are available at this https URL .

---


> [!TIP]
> 当前位于：**151-189**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-189**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
