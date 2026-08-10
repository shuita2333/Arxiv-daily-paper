# 📦 其他研究 | 2026年08月10日

> 本类共 **221** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-221](./part-05.md)

---

### 51. [A Transferable Autologistic Model for Predicting Rare Failures in Heterogeneous Equipment](https://arxiv.org/abs/2608.06695)

**<font color=#1a73e8>作者：</font>** Islam Benamirouche, Djemel Ziou, Feriel Fass  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Predicting failures before they occur remains a major challenge in predictive maintenance, particularly when failures are rare, when equipment of the same family differ in sensor configurations, and when the goal is anticipation rather than diagnosis of an already observed fault. This paper proposes a common-to-target probabilistic model that learns shared failure-related patterns across a family of heterogeneous equipment and adapts parsimoniously to target equipment. The model explicitly accounts for sensor heterogeneity, operating context, and degradation dynamics to produce calibrated failureprobability estimates suitable for maintenance planning. Its performance is evaluated on a synthetic refrigerator dataset comprising 27 simulated refrigerators with varying sensor configurations, operating conditions, and failure types, providing a controlle

---


### 52. [Scalable Long-Horizon Planning with Staggered Updates for Lifelong MAPF](https://arxiv.org/abs/2608.06702)

**<font color=#1a73e8>作者：</font>** Vaibhav Sanjay, Jiaoyang Li  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Lifelong Multi-Agent Path Finding (LMAPF) requires generating collision-free paths for large agent fleets under strict real-time constraints. Reactive frameworks such as PIBT and Enhanced PIBT (EPIBT) scale effortlessly to thousands of agents through rule-based, step-by-step coordination but suffer from severe temporal myopia, making them ineffective in scenarios where long-horizon reasoning is essential. RHCR plans windowed paths over multi-step horizons but incurs substantial planning overheads that hinder scalability. TP tackles both challenges by planning only subsets of agents at each timestep, yet its applicability is restricted to highly structured maps. To achieve long-horizon planning at scale across general maps, we propose Path Updates over Staggered Horizons (PUSH), a LMAPF planner capable of coordinating thousands of agents in under a second while planning over multi-step horizons. PUSH combines the key advantages of PIBT, RHCR, and TP. Like TP, PUSH reduces computational complexity by planning only a subset of agents at each timestep using staggered planning windows. Unlike TP, however, PUSH plans RHCR-style windowed paths in general maps without relying on restrictive map assumptions. To maintain high throughput in congested environments, PUSH further integrates EPIBT-inspired priority inheritance, backtracking, and anytime improvements into its windowed planning. Empirical evaluations across two realistic MAPF scenarios requiring long-horizon reasoning show that PUSH scales to the same massive agent loads as EPIBT (e.g., 10k agents) while achieving significantly higher system throughput than all baselines.

---


### 53. [WebRider: Persona-Conditioned Intent Controllers for Live-Web Assistance](https://arxiv.org/abs/2608.06704)

**<font color=#1a73e8>作者：</font>** Zhi Li, Tao Zhou, Yeqing Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Delegating a web task involves more than asking a question; it requires transferring a policy: what to verify, how to handle uncertainty, which preferences matter, and when to stop. Yet, current live-web agents are evaluated solely on the final answer, ignoring the policy constraints that define the delegation. A plausible final answer can conceal violations of that policy. Our full live audit reveals this critical gap: a strong controller completes 99.2% of tasks but honors all policy constraints in only 38.8% of cases. Finishing does not imply fidelity. WebRider bridges this gap by formalizing the delegated policy as an intent contract---an operational record of goals, constraints, evidence obligations, answer form, and task-local persona controls that must hold even as web pages change. WebRider employs a hierarchical architecture: a top-layer controller maintains the contract, a middle layer realizes intentions as guarded executable actions, and a tool layer executes these actions via browser, search, and maps tools. Our benchmark, RiderBench, evaluates this design on 4,096 live-web contracts across 42 public websites, auditing both the internal contract state and the visible user experience to determine if a rollout preserved its policy and if the steps were persona-consistent. The guarded middle interface also serves as a high-quality training signal; an 8B action-policy model trained through this interface outperforms executable-only baselines under a fixed controller. By making the browsing path a first-class object, WebRider enables a system that is auditable, human-judgeable, and learnable without conflating action realization with final-answer decisions. Dataset URL: this http URL.

---


### 54. [Suppress and Diversify: Refining Robust Pathways for Corruption Robustness](https://arxiv.org/abs/2608.06712)

**<font color=#1a73e8>作者：</font>** Jiangang Yang, Wenhui Shi, Xiaoran Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Model robustness against natural image corruptions is essential for safety-critical applications. While existing methods primarily focus on implicit representation learning, we provide the first systematic exploration of computational pathways to explicitly characterize internal robustness. We identify a progressive decay of robust features across network layers and establish a functional dependency between the prevalence of these features and model performance. To exploit these insights, we propose Suppress and Diversify (S\&D), a non-intrusive refinement approach that enhances robustness by dynamically selecting robust pathways and diversifying them through symmetry-preserving transformations. S\&D is architecture-agnostic, parameter-free, and incurs zero test-time overhead. Extensive evaluations across eight benchmarks demonstrate that S\&D consistently improves performance across multiple vision tasks, diverse backbones, and complex real-world scenarios, highlighting its broad efficacy and scalability.

---


### 55. [MolBioKG: Grounding Out-of-Graph Molecules in Biomedical Knowledge Graphs via Multi-Resolution Structural Anchoring](https://arxiv.org/abs/2608.06713)

**<font color=#1a73e8>作者：</font>** Yiming Zhang, Hikaru Shindo, Shuan Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Biomedical knowledge graphs (KGs) accelerate drug discovery, but standard pipelines assume query molecules already exist as graph entities, leaving unregistered molecules disconnected. We address this cold-start challenge, termed the out-of-graph molecule problem, by introducing MolBioKG. This two-layer system grounds unseen molecules in biomedical evidence via multi-resolution structural anchoring. It connects an index of 2.74 million molecules (represented by scaffolds, fragments, functional groups, and fingerprints) to a 9.6-million-edge KG. Given only a SMILES string, MolBioKG retrieves structurally related graph entities and traverses their biomedical neighborhoods without task-specific training. It features two inference mechanisms: static multi-anchor retrieval using Reciprocal Rank Fusion, and Adapt-KG, a tool-using LLM policy for adaptive traversal. Evaluated across in-graph link recovery, complex multi-hop reasoning, and out-of-graph generalization, MolBioKG outperforms strong baselines. Notably, it raises Hits@10 from 0.585 to 0.876 in multi-hop reasoning and out-of-graph target recall from 0.145 to 0.269, all while ensuring predictions retain traceable structural anchors and source-attributed KG evidence.

---


### 56. [The Optimizer Is the Agent: Reasoning-Driven Search across Prompts, Programs, and ML Workflows](https://arxiv.org/abs/2608.06714)

**<font color=#1a73e8>作者：</font>** Junbo Li, Boyi Liu, Canwen Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent systems for optimizing prompts, programs, and ML workflows typically rely on explicit outer-loop controllers such as evolutionary search, bandits, or textual-gradient methods. We ask a fundamentally different question: how much of this search policy can be internalized by a single tool-using agent? We present ReASearch, a unified framework for reasoning-driven optimization in which the agent autonomously decides what to evaluate, how to diagnose failures, which edits to make, and when to verify or restart. Rather than serving only as a proposal generator guided by hand-designed heuristics, the agent actively analyzes outcomes, allocates budget, and refines its strategy over long horizons through persistent memory. With a shared agent loop and domain-specific tools, ReASearch instantiates the exact same scaffold to optimize prompts, programs, and ML workflows. Across 14 diverse tasks, it is competitive with and mostly better than specialized optimization systems, achieving gains of 2% to 40% over strong domain-specific baselines, and in some cases discovering solutions that improve on prior human best-known results. Crucially, we observe that complex search behaviors, which are typically implemented by explicit controllers, emerge naturally from the agent's reasoning process.

---


### 57. [WaveFreqAnchor: Wave-Structural Anchoring and Frequency Correction Diffusion for Training-Free Face Restoration](https://arxiv.org/abs/2608.06717)

**<font color=#1a73e8>作者：</font>** Zelin Du, Wenjie Li, Zhengxue Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based face restoration that adjusts the sampling trajectory of pre-trained diffusion models has achieved remarkable progress. However, existing approaches provide insufficient constraints during reverse diffusion, causing identity-related structural drift and degraded fidelity under severe degradations. To address this, we propose WaveFreqAnchor, a training-free framework based on Wave-Structural Anchoring and Frequency Correction Diffusion. Specifically, Anchor-Space Wave-Structural Guidance (ASWG) constrains facial structures through anisotropic wave-response consistency, while Multi-scale Wavelet-Fourier Injection (MWFI) aligns the predicted low-frequency subband with the observation by replacing its phase, correcting inconsistencies accumulated during reverse diffusion. For real-world scenes, we further introduce Subband High-Frequency Enhancement (SHE), which performs bounded, spatially masked refinement on the predicted high-frequency subbands to recover fine facial details under unknown compound degradations. Together, these designs effectively preserve facial identity while restoring sharp and realistic facial details. Extensive experiments show that our method consistently outperforms existing methods, achieving high-quality and high-fidelity face restoration.

---


### 58. [Tight Security for BBS Signatures](https://arxiv.org/abs/2608.06724)

**<font color=#1a73e8>作者：</font>** Rutchathon Chairattana-Apirom, Dennis Hofheinz, Stefano Tessaro  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> This paper studies the concrete security of BBS signatures (Boneh, Boyen, Shacham, CRYPTO '04; Camenisch and Lysyanskaya, CRYPTO '04), a popular algebraic construction of digital signatures which underlies practical privacy-preserving authentication systems and is undergoing standardization by the W3C and IRTF.
Schäge (Journal of Cryptology '15) gave a tight standard-model security proof under the q-SDH assumption for a less efficient variant of the scheme, called BBS+--here, q is the number of issued signatures. In contrast, the security proof for BBS (Tessaro and Zhu, EUROCRYPT '23), also under the q-SDH assumption, is \emph{not} tight. Nonetheless, this recent proof shifted both standardization and industry adoption towards the more efficient BBS, instead of BBS+, and for this reason, it is important to understand whether this tightness gap is inherent. Recent cryptanalysis by Chairattana-Apirom and Tessaro (ASIACRYPT '25) also shows that a tight reduction to q-SDH is the best we can hope for.
This paper closes this gap in two different ways. On the positive end, we show a novel tight reduction for BBS in the case where each message is signed at most once--this case covers in particular the common practical use case which derandomizes signing. On the negative end, we use a meta-reduction argument to prove that if we allow generating multiple signatures for the same message, then {\em no} algebraic reduction to q-SDH (and its variants) can be tight.

---


### 59. [bioMoR: Biology-Guided Mixture-of-Recursions for Effective Genomic Learning](https://arxiv.org/abs/2608.06727)

**<font color=#1a73e8>作者：</font>** Koushik Howlader, Tirtho Roy, Md Tauhidul Islam 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Transformer models for high-dimensional omics analysis process thousands of genes or pathways, although only a subset requires deep computation. Mixture-of-Recursions (MoR) improves efficiency through adaptive token-choice or expert-choice routing. We propose bioMoR, which, to the best of our knowledge, is the first framework to apply MoR to gene-level and pathway-level learning. Our contributions include identifying three locations for integrating structured biological knowledge within an MoR backbone: graph-based information sharing refines token embeddings, a structural bias guides self-attention toward biologically related tokens, and a graph-aware router uses neighborhood information to determine each token's recursion depth. These techniques are centered on our insight that additional knowledge of token interaction can effectively help models construct embeddings and select which tokens should be learned more deeply. Across eight benchmarks spanning diverse omics data types and evaluated under a unified five-fold cross-validation protocol, bioMoR improves average macro-F1 by 8.2 percentage points and balanced accuracy by 7.1 percentage points over the strongest biology-agnostic MoR baseline while using 75 percent fewer parameters and up to 58 percent fewer FLOPs than a non-recursive Transformer. The selected marker genes or pathways provide biological interpretability, while their token-specific recursion depths reveal how computation is allocated.

---


### 60. [From Cheap Fakes to Pure Synthesis: Addressing the New Era of T2V Fake News Videos](https://arxiv.org/abs/2608.06732)

**<font color=#1a73e8>作者：</font>** Yifeng Luo, Yupeng Li, Liang Lan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent text-to-video (T2V) generation models enable fake news videos to be synthesized from scratch, shifting the threat beyond cheap fakes assembled from existing footage. Such news videos can closely match fabricated narratives, creating a modality alignment trap for existing detectors. Existing datasets lack pure synthesis fake news videos. Although directly prompting T2V models with descriptions of fake news videos can yield perfectly aligned samples, it reduces the fake news video detection (FNVD) to unimodal shortcuts and causes semantic-visual degeneration. To counter this, we formulate T2V-FNVD as a novel ternary classification task with three labels (real, cheap fake, and pure synthesis fake) and construct the first pure synthesis fake news video dataset (PS-FNVD). PS-FNVD includes fabricated events with aligned deception (Type 1) and true events with false visual provenance (Type 2), preventing models from exploiting unimodal shortcuts. Furthermore, we propose the Reasoning-guided T2V-FNVD (R-T2V) framework. Trained through conditioned rationale generation and supervised fine-tuning, R-T2V integrates high-level semantic logic with low-level physical generative traces to predict the ternary veracity label. Extensive experiments across 10 prevailing baselines show that R-T2V achieves the state-of-the-art performance, outperforming the second-best baseline by 12.20 percentage points in accuracy and 8.46 percentage points in macro $F_1$.

---


### 61. [Solver-Guided Reasoning for Mixed-Equilibrium Strategies](https://arxiv.org/abs/2608.06741)

**<font color=#1a73e8>作者：</font>** Han Wang, Philippe Beardsell, Boning Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning in large language models (LLMs) is often grounded in human text, human demonstrations, and human-generated rationales. For equilibrium reasoning in complex games, however, relying on human data can be suboptimal. In fact, human play is often guided by intuition and heuristics and can deviate substantially from game equilibrium. This discrepancy is amplified in games with mixed-strategy equilibria, where human data is heavily biased toward pure strategies. Consequently, conditioning LLMs on this data yields weak game strategies. To grant LLMs the reasoning capacity in games, in this work, we study how to elicit equilibrium play using solver output. We propose Mixed-Strategy Decision Tree (MDT), which articulates the silent optimality of the equilibrium into sparse strategic rules that both humans and LLMs could understand. Using solver output rather than human annotation allows us to extend the input to arbitrarily new states and continuations. We instantiate this study on No-Limit Texas Hold'em by querying a solver oracle for over \textbf{250 million mixed-strategy decisions}; MDT together with other techniques \textbf{reduces the $\ell_1$ distance to the equilibrium by $52.6\%$} across $8$ different LLM configurations. A Route-only ablation tests the incremental contribution of the shadow-based contrast, while complete River-endgame and Liar's Dice experiments evaluate strategic fidelity and portability beyond the original NLH communication setting.

---


### 62. [MemPrism: Task-Conditioned Relational Memory Views for Long-Horizon Agents](https://arxiv.org/abs/2608.06745)

**<font color=#1a73e8>作者：</font>** Zhisheng Chen, Bingfan Zeng, Bangde Cao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon agents rely on memory to reuse experiences, yet existing memory systems often assume that evidence can be directly consumed through a fixed representation. This leads to representation mismatch, where relevant information is available but not organized for the current decision. To this end, we propose MemPrism, a task-conditioned relational memory framework that separates persistent experience storage from decision-time working memory. MemPrism records interactions as the event stream and dynamically constructs relational views according to the current task context. A lightweight view policy selects the relation structure, evidence range, outcome condition, and granularity, while a deterministic composer and render transform historical facts into a temporary optical working-memory view for a frozen task policy. Experiments on long-horizon embodied and web-agent benchmarks show that MemPrism consistently improves the task performance, especially as trajectories become longer, while reducing memory token consumption. Furthermore, the learned view policy transfers across different VLMs without additional adaptation, demonstrating the effectiveness of task-conditioned relational views as a general memory interface for agents.

---


### 63. [KReF: Training-Free Retrieval for Long-Term Time-Series Forecasting and Predictive Uncertainty](https://arxiv.org/abs/2608.06748)

**<font color=#1a73e8>作者：</font>** Yang Zhang, Rui Su  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Probabilistic long-term time-series forecasting commonly relies on trained models. Training-free conformal methods typically construct intervals around a pre-existing point forecaster and do not natively represent a complete predictive distribution; sequential variants additionally suffer from increasingly delayed feedback at long horizons. We propose KReF, a training-free retrieval framework that treats retrieved historical futures as a querylocal empirical predictive distribution. After robust preprocessing, KReF embeds each lookback using handcrafted statistics or frozen random Fourier features and retrieves similar historical lookback-future pairs. Their similarity weights directly define predictive masses, quantiles, CRPS, and a weighted-mean point forecast. KReF further uses the observed query lookback to construct a probability-integral-transform map and applies validation-selected expansion and shrinkage rates to adapt interval boundaries. Across six LTSF benchmarks and four horizons, KReF obtains the lowest CRPS in all 12 dataset-embedding settings and the lowest IS90 in 9 settings. Without gradient-based fitting, its point forecasts also match or surpass trained baselines on two of six datasets. An archive-oracle analysis further reveals substantial headroom under finer horizon- and channel-wise routing. These results establish retrieval as a useful and underexplored inductive bias for LTSF.

---


### 64. [Progressive Content Refinement with Decaying Reward Joint LinUCB](https://arxiv.org/abs/2608.06750)

**<font color=#1a73e8>作者：</font>** Shion Ishikawa, Pablo Loyola, Young-joo Chung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Iterative refinement has significantly enhanced Large Language Model (LLM) performance; however, existing methods ranging from feedback-based Self-Refine to traditional bandit approaches often rely on static options or overlook the saturation effect. This neglect leads to over-exploitation, where the continuous use of identical prompts or arms results in diminishing rewards over time.
To address this challenge, we propose a novel contextual bandit algorithm that explicitly incorporates reward decay modeling. Utilizing an Expectation-Maximization (EM) algorithm, our method simultaneously estimates both arm-specific and decay parameters. Furthermore, by embedding prompts as arms, we facilitate the joint learning of arm values, distinguishing our approach from the traditional disjoint Linear Upper Confidence Bound (LinUCB) framework.
Experimental results on Sentiment Reversal and GSM8K benchmarks demonstrate that our method achieves significant performance gains over strong baselines. Finally, our ablation study confirms that the integration of reward decay modeling within the bandit framework is crucial for mitigating over-exploitation and optimizing the iterative refinement process.

---


### 65. [Beyond Starry Night: Shortcut-Aware Control-State Planning for Artist-Grounded Text to Image Generation](https://arxiv.org/abs/2608.06751)

**<font color=#1a73e8>作者：</font>** Kuan Xing, Ye Wang, Changyi Gan 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Artist-grounded image generation requires more than appending an artist name to a prompt. Image models often respond to artist names through canonical shortcuts, such as recurring motifs, generic palettes, or overrepresented period signatures, rather than preserving the user's intended scene. We introduce Atelier, a shortcut-aware control-state planning framework for artist-grounded image generation. Atelier translates underspecified artistic intent into an explicit control state that separates scene anchors, preserve/transform decisions, style-regime hypotheses, role-bound artist evidence, and shortcut-avoidance constraints. It grounds this state using artist-level knowledge and local patch references, compiles backend-aware generation plans, and iteratively refines candidates through global and local authenticity feedback. We further introduce ArtIntentBench, a benchmark covering Van Gogh and Qi Baishi across artwork re-rendering, period/style-controlled generation, historically unseen subjects, shortcut auditing, and human preference evaluation. Across open-weight and closed-source generators, Atelier improves artist-level style fidelity, preserves source structure more faithfully, and substantially reduces shortcut substitution compared with prompt-engineered, retrieval-augmented, and general-purpose agent baselines. These results suggest that artist-grounded generation is bottlenecked not only by image synthesis, but by the upstream inference of explicit, evidence-grounded artistic controls.

---


### 66. [Stockmark-Nemotron-3-Nano-Omni-JapanDocReader: Structured Document Parsing via Capability Injection and Forgetting Control](https://arxiv.org/abs/2608.06758)

**<font color=#1a73e8>作者：</font>** Shi Chen, Hayato Aida, Makoto Morinaga 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present Stockmark-Nemotron-3-Nano-Omni-JapanDocReader, a Japanese document understanding model built from Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16. The central goal of this work is structured document parsing via capability injection and forgetting control: we inject Japanese structured document parsing capability into a reasoning-oriented multimodal model while preserving its document VQA capability as much as possible. We study parsing-centric SFT, which uses only structured document parsing data; mixed SFT, which combines structured document parsing and VQA data; and parsing-centric RL, which optimizes structured parsing with a task-level reward. Our experiments show that parsing-centric SFT substantially improves structured document parsing performance but causes measurable VQA forgetting. Mixed SFT mitigates this forgetting while preserving nearly the same structured parsing performance. Applying DAPO-based parsing-centric RL on top of the mixed SFT checkpoint further improves structured document parsing beyond the SFT ceiling, producing the final released model. The training data is constructed with a data engine consisting of two complementary synthetic streams: a Japanese Document VQA Stream and a programmatic structured document parsing stream. We also discuss reward design and variance-based prompt filtering for continuous structured document parsing rewards, highlighting their importance for making RL effective in long-reasoning structured document parsing tasks.

---


### 67. [LiFTER: A Grounded Neuro-Symbolic Microscope for Continuous-Time Dynamic Graph Forecasting](https://arxiv.org/abs/2608.06765)

**<font color=#1a73e8>作者：</font>** Minwoo Yu, Young-guk Ha  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Continuous-time dynamic graph models predict future links by compressing past interactions into neural states. Although effective for forecasting, this computation obscures which entities are shared across events and how temporal patterns contribute to a prediction. We treat this gap as a property of the predictive architecture rather than a problem to be addressed after prediction. Link-Fact Temporal Rule Inducer (LiFTER) is a neuro-symbolic predictor that preserves observed interactions as grounded temporal facts and applies executable tempo- ral rules to pre-query facts. Each score is a signed sum of rule exe- cutions whose historical facts, entity bindings, and temporal order are explicitly satisfied. The evidence and rules responsible for a prediction can therefore be inspected, independently recomputed, and intervened upon. Across four CTDG benchmarks, LiFTER achieves competitive historical-negative forecasting and the highest macro explanation ac- curacy and deletion fidelity. The same architecture also serves as a microscope that separates the contributions of recurrence, history po- sition, and transition across datasets and traces them to individual facts. Independent execution reconstructs all logits for 19,664 test predictions with a maximum error of 0.0000131. LiFTER turns future-link forecasting into a verifiable grounded computation.

---


### 68. [Hidden Gauge Controls Feature Specialization in ReLU Networks](https://arxiv.org/abs/2608.06766)

**<font color=#1a73e8>作者：</font>** Tongxi Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training changes a network's predictions while allocating task-relevant structure across its internal units. In an overparameterized ReLU network, several neurons can begin with exactly the same functional role, yet one may acquire a teacher feature while the others become redundant. We call the identity of that neuron feature ownership and ask whether it can be controlled by a parameter choice invisible to the initial predictor. In a tractable Gaussian teacher--student model, we fix the complete initial function and vary only a positive-homogeneous scaling gauge. Opposite gauges produce distinct feature trajectories and a sharp $\Theta(D^2)$ separation in specialization time that no global change of clock can explain. Among any fixed number of initially duplicate students, assigning the favorable gauge to one neuron deterministically selects it as the owner and drives the remaining functional contribution to zero. An exact reaction--transport decomposition attributes the effect to different mobilities for changing a feature's coefficient and direction. We prove global selection and functional pruning, extend finite-time selection to visible perturbations and small-step full-batch gradient descent, and verify the predicted loss, alignment, pruning, and dissipation trajectories in population and finite-sample training. The initial predictor therefore determines neither when the feature is learned nor which neuron learns it.

---


### 69. [Explore or Converge? Stage-Guided Per-Step Optimization for Diffusion Models](https://arxiv.org/abs/2608.06768)

**<font color=#1a73e8>作者：</font>** Renye Yan, Jikang Cheng, You Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion models have strong generative capabilities. However, their maximum likelihood training objective only focuses on reconstructing the data distribution, making it difficult to align with specific preferences. Reinforcement learning (RL) for preference alignment in diffusion models is promising but limited by reward sparsity. Since a single reward cannot support optimization, existing RL methods usually backpropagate the final reward to all previous steps. However, denoising is stage-wise, with distinct semantics and controllability. Repeating the final reward across all steps creates a temporal objective mismatch, encouraging reward shortcuts that lead to reward hacking. At the same time, due to reward backfilling, each time step receives the same reward, making it impossible to distinguish between actions, thereby weakening the optimization process.
To resolve this issue, we propose Stage-Guided Per-Step Optimization (SGPO) for diffusion models, which jointly leverages signal-to-noise ratio and semantic changes to identify generation stages and adaptively assign stage-specific objectives. Early denoising is chaotic and far from the final reward, resulting in weak reward-behavior correlation. This stage should prioritize exiting the chaotic state. In the mid stage, the latent transitions to a stable structure, where the final reward better corresponds to generative behavior. Therefore, this stage optimizes the final reward while exploring diversity to avoid early convergence to a single mode.
In the late stage, the latent's core structure is largely fixed, and preference optimization mainly amplifies local details, risking overfitting. Therefore, stable convergence is preferred to avoid quality degradation. Results from 16 comparative experiments validate SGPO. Our method achieves 26.7% average gains in generative quality and 36.7% higher convergence speed.

---


### 70. [ArchEGraph: A Large-Scale Graph Dataset for Geometry-Topology-Physics Aligned Building Energy Modeling](https://arxiv.org/abs/2608.06772)

**<font color=#1a73e8>作者：</font>** Yihui Li, Yihui Chen, Kaidi Zha 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate estimation of building energy use is essential for achieving carbon neutral and sustainable buildings. To better understand the influence of design decisions on building energy use and calibrate machine learning models that can give architects and engineers rapid design feedback, large-scale datasets are needed that explicitly map building geometry to performance. We present ArchEGraph, a large-scale benchmark dataset that represents buildings as heterogeneous graphs with aligned geometry, topology, weather, and zone-level thermal loads. The dataset contains 5,481 buildings and 49,326 validated building-weather simulation cases. In total, it includes over 133,000 space nodes and 1.44 million face nodes, reflecting substantial geometric and topological complexity. Based on ArchEGraph, we define two benchmark tasks: (i) graph reconstruction from polygonal meshes, aiming to recover topological structure from geometric representations; and (ii) topology-informed load prediction, which leverages graph structure and temporal weather conditions to forecast zone-level response time series. We further introduce standardized evaluation protocols for both tasks and conduct cross-building and cross-climate generalization experiments to assess model robustness. ArchEGraph provides a unified testbed for studying geometry-topology-physics coupling in building energy modeling, enabling the development and evaluation of scalable and generalizable surrogate models.

---


### 71. [AnyTrack: Unifying Visual Object Tracking with Any Modalities](https://arxiv.org/abs/2608.06773)

**<font color=#1a73e8>作者：</font>** Hao Li, Yunzhi Zhuge, Wenning Hao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual object tracking aims to continuously locate specific targets within sequential frames, evolving from single-modal methods to multi-modal ones. However, existing multi-modal trackers are typically designed for fixed modality combinations, requiring separate models for different inputs. This leads to a poor adaptability to missing or imperfect modalities, and limited generalization. To address these issues, we propose a novel unified framework called AnyTrack for object tracking with any modalities. Specifically, we design a Modality-aware Interaction Module (MIM) to facilitate dynamic interaction across diverse modalities. This module bridges modality discrepancies and aggregates temporal cues to maintain spatio-temporal consistency during cross-modal interaction. Furthermore, we introduce a Context Understanding Module (CUM) to establish spatial correspondence between visual features and target locations via global-local prompts. This module employs target-aware context modeling to enhance foreground-background discrimination for precise localization. Finally, to support the training and evaluation under diverse modalities, we extend existing multi-modal object tracking benchmarks by incorporating grayscale images, language descriptions, and audio clips. Extensive experiments with both complete and missing modality settings demonstrate that our AnyTrack achieves state-of-the-art performance, validating its effectiveness and flexibility. The source code is available at this https URL.

---


### 72. [Faster Query-Key Learning Sharpens Attention in Self-Attention Models](https://arxiv.org/abs/2608.06776)

**<font color=#1a73e8>作者：</font>** Rahul Vashisht, Harish G. Ramaswamy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A standard self-attention layer consists of two interacting circuits: the query-key circuit that governs attention allocation, and the output-value circuit that maps attended representations to predictions. Collapsed and factorized parameterizations of the query-key and output-value circuits lead to qualitatively different attention patterns. In particular, some parameterizations give sharper attention to task-relevant tokens, at a similar training loss. We analyze how the parameterizations of these circuits shape the parameter trajectories in single-layer self-attention models trained for next-token prediction. Through gradient-flow analysis, we show that factorization induces implicit rescaling of the two circuits' learning rates. We derive closed-form dynamics showing that output-value and query-key parameters move along a line, with relative speeds determined by their learning rates. Faster query-key learning relative to output-value learning thus produces sharper attention, as the model compensates for slower output-value learning by increasing attention mass on relevant tokens. Experiments show that differences in the relative learning rates of the two circuits govern attention concentration. This improves attention interpretability proxies while maintaining comparable predictive performance.

---


### 73. [UniCycleFlow: Bidirectional Unpaired Image Translation with a Shared Rectified Flow](https://arxiv.org/abs/2608.06784)

**<font color=#1a73e8>作者：</font>** Xianhao Zhou, Jianghao Wu, Shaoting Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Bidirectional unpaired image translation must preserve source-specific structure while learning coherent transformations in both directions without paired supervision. Existing methods typically employ two direction-specific generators or train separate one-way models. Even when linked by cycle consistency, such models constrain only the round-trip endpoint reconstruction, without requiring the two directions to obey a common local transformation rule. We propose UniCycleFlow, a rectified-flow framework that represents bidirectional translation as forward and reverse integration of a single time-conditioned velocity field. This formulation organizes both directions within the same continuous dynamics, rather than coupling otherwise separate endpoint mappings. A key challenge is that unpaired data provide no meaningful source--target coupling from which rectified-flow trajectories can be constructed. UniCycleFlow addresses this challenge by learning deterministic source-conditioned endpoints whose marginal distributions are adversarially matched to the opposite domains. The resulting paths are regularized by stop-gradient self-flow matching for intermediate velocity supervision, discrete cycle closure for forward--reverse consistency, and representation path-velocity regularization for controlling localized feature changes along the trajectory. Across ten translation directions, UniCycleFlow achieves the lowest FID on 7 of 10 tasks using a single Euler evaluation and obtains the best average FID of 55.1.

---


### 74. [Multi-Perspective Triad Interaction Graph Neural Network for Cognitive Distortion Detection](https://arxiv.org/abs/2608.06785)

**<font color=#1a73e8>作者：</font>** Jun Seo Kim, Hye Hyeon Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Cognitive distortion detection is a key task in computational mental health, yet existing approaches often overlook the psychological structure of distorted thoughts. We propose MTI-GNN (Multi-Perspective Triad Interaction Graph Neural Network), which models Beck's cognitive triad---negative views of the self, world, and future---as complementary perspectives for classification. An LLM decomposes each utterance into the three perspectives, from which perspective-specific similarity graphs are constructed and encoded by a Multi-Perspective GNN. A Triad Interaction module models cross-perspective dependencies through sequential source-conditioned updates and feature-wise gating, while Prototype-Guided Perspective Fusion performs label-conditioned aggregation. Label-expanded supervision incorporates all available distortion annotations during training. We evaluate MTI-GNN on 9,764 samples from four Korean, English, and Chinese datasets spanning ten distortion categories. MTI-GNN significantly outperforms all supervised variants and exceeds eight prompted generative models under zero-shot and few-shot settings. Leave-one-perspective-out ablations show that all three perspectives contribute significantly, while human expert evaluation provides preliminary evidence of their alignment with the intended cognitive dimensions.

---


### 75. [PAST: Prompt-Adaptive Sampling Termination for Efficient Diffusion Model](https://arxiv.org/abs/2608.06794)

**<font color=#1a73e8>作者：</font>** Renye Yan, Jikang Cheng, You Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While diffusion models have made significant progress in text-to-image tasks, they still exhibit limitations when directly optimizing downstream objectives. Although Reinforcement Learning (RL) enables targeted optimization, existing methods are generally constrained by low-efficiency fine-tuning and sparse rewards. To address these challenges, we propose PAST, which provides differentiated rewards while adaptively regulating training episode length by jointly perceiving denoising progress and prompt difficulty. Specifically, we design an intrinsic reward paradigm to compensate for sparse extrinsic rewards and guide the model to explore paths that diverge more efficiently from noise patterns. We further provide theoretical justification for intrinsic rewards. Then, PAST dynamically monitors denoising completion and semantic alignment between image structures and prompt semantics. When both metrics satisfy generation requirements, the system adaptively terminates training. This enables appropriate allocation of episode lengths based on prompt difficulty and the current generation process. Finally, based on the predicted residual noise level, we establish a dual adaptive coordination mechanism. Specifically, it not only balances the extrinsic and intrinsic rewards but also balances the exploration and convergence. Experimental results demonstrate that PAST enhances computational efficiency of existing RL fine-tuning methods by up to 66.7%, while improving preference optimization quality by up to 29.5% through its dual adaptive regulation mechanism.

---


### 76. [AdvTiles: Physical Adversarial Camouflage Clothing against Person Detectors via Learnable Tiles](https://arxiv.org/abs/2608.06801)

**<font color=#1a73e8>作者：</font>** Jinlei Wang, Jiahuan Long, Mingkai Sun 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Physical adversarial attacks against person detectors have evolved from localized patches to full-body textures. However, achieving both visual naturalness and strong attack effectiveness remains challenging. Existing natural-looking methods typically optimize camouflage textures as a whole, limiting the flexibility to refine local adversarial patterns and their spatial arrangement. To address this issue, we propose AdvTiles, a physical adversarial camouflage framework built from learnable tiles, enabling strong attack performance while preserving a natural camouflage appearance. Specifically, we use a Straight-through (ST) Gumbel-Softmax estimator for differentiable tile selection, enabling joint optimization of tile patterns and spatial layouts. This design provides fine-grained control over adversarial texture generation. To improve robustness in diverse physical conditions, we further optimize the camouflage through differentiable 3D Gaussian Splatting rendering with variations in viewpoints, scales, illuminations and backgrounds. Extensive experiments across multiple detectors demonstrate that AdvTiles achieves an average ASR of 86.2%, outperforming existing state-of-the-art attack methods. We further fabricate the optimized camouflage into wearable adversarial clothing, validating its effectiveness in real-world scenarios across diverse distances, angles and backgrounds.

---


### 77. [Simple-OPD: Demystifying Warm-up for On-policy Distillation](https://arxiv.org/abs/2608.06802)

**<font color=#1a73e8>作者：</font>** Tao Liu, Taiqiang Wu, Mao Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own rollouts with token-level supervision from teacher models, but its effectiveness can depend strongly on the warm-up stage before OPD. In this paper, we demystify warm-up for OPD from both data and training perspectives. For data, we find that effective warm-up relies on teacher-compatible chain-of-thought supervision, and that even incorrect teacher rollouts can provide comparable benefits to correct ones. This suggests that warm-up primarily transfers a teacher-compatible thinking pattern rather than merely correct answers. For training, we show that low-rank adaptation (LoRA) with a near-saturation training duration better balances in-domain adaptation and out-of-distribution generalization than full-parameter SFT. Based on these findings, we propose Simple-OPD, a plug-and-play initialization method that warms up the student on teacher-generated CoT with LoRA before OPD. Experiments across diverse settings demonstrate the effectiveness and robustness of Simple-OPD.

---


### 78. [Fact-Check Your Information (FYI): A Design Probe to Understand How People Actually Fact-Check Data-Driven Articles](https://arxiv.org/abs/2608.06804)

**<font color=#1a73e8>作者：</font>** Nguyen-Truong Thinh, Yuxuan Du, Phongsakon Mark Konrad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Data-driven journalism and policy reports frequently rely on statements grounded in statistical evidence, referred to as data claims. Verifying such a claim requires connecting it to the underlying structured dataset. However, existing systems typically isolate automated fact-checking from manual data exploration, leaving it unclear how readers coordinate AI assistance with manual inspection of the evidence in practice. We present FYI, a browser extension that embeds fact-checking in the reading environment, and use it as a design probe to study how people detect, verify, and determine the validity of data claims against the underlying dataset. FYI provides four complementary tools spanning the spectrum from full automation to manual data exploration. In an exploratory study (N=22), participants used FYI to fact-check claims in a data-driven article. We find that participants adopted three distinct workflow archetypes---AI-first with manual confirmation, manual-first with AI supplement, and parallel co-review---with visualization serving as the primary mechanism for auditing AI conclusions. Trust in AI shifted dynamically, growing when multiple tools converged and eroding when AI outputs were inconsistent. These findings suggest that fact-checking systems should treat AI as a starting point that human verification complements rather than a definitive authority, elevate visualization as a core verification capability, and support flexible, user-driven workflows. We release FYI as open-source software for further research at this https URL.

---


### 79. [On a General Theoretical Framework for Radio Frequency Fingerprint-Based Authentication](https://arxiv.org/abs/2608.06805)

**<font color=#1a73e8>作者：</font>** Yuanyu Zhang, Jianing Wang, Shuangrui Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> While radio frequency fingerprint (RFF)-based wireless device authentication has been widely studied across different datasets and scenarios, there still lacks a fundamental theory to explain why and how RFF can serve as a reliable device identity, significantly hindering the practical application of such an authentication technology. In this article, we integrate the RFF modeling with authentication property analysis to propose a general theoretical framework to facilitate the development of such a theory. The RFF modeling process reveals how RFFs are induced, evolved and observed along the transmitter-channel-receiver chain, built upon which, the authentication property analysis process then outlines how the trustworthiness of an RFF should be examined in terms of its uniqueness, stability, distinguishability, and unforgeability. By linking the RFF formation/evolution to these authentication properties, the framework offers a solid foundation for understanding why and how RFF-based authentication is trustworthy in practice. We also discuss the communication-authentication co-design issue based on the theoretical insights from the proposed framework.

---


### 80. [Understanding Differentiable Embeddings Through Differential and Integral Geometry](https://arxiv.org/abs/2608.06809)

**<font color=#1a73e8>作者：</font>** Xinyu Zhang, Klaus Mueller  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How can an analyst decide whether a nonlinear dimensionality reduction embedding can be trusted? Existing diagnostics provide only partial answers: projection glyphs characterize local sensitivity, map-continuity scores measure local conditioning, and transport-based analyses reveal path-dependent inconsistencies. However, these methods appear unrelated and provide no common framework for understanding when they agree or not. We show that they are all derived from a single geometric object induced by every differentiable embedding, whether defined implicitly through optimization or explicitly by a learned mapping. This framework provides two complementary geometric views of an embedding. The differential view explains local behavior: its first-order term recovers projection glyphs, while its second-order curvature quantifies how far their linear approximation remains reliable. The integral view follows the same geometry along high dimensional paths and determines whether an embedding depends only on the current state or also on the path taken to reach it. We further show that map-continuity is a prerequisite for the other analyses. The framework is theoretically complete for diagnostics derived from the embedding geometry, and we prove the integral view irreducible: no amount of local measurement at any number of points, to any order of derivative, reproduces what it detects. Classical rank-based metrics form a complementary class based on finite-scale neighborhood relationships. Experiments on synthetic and real datasets validate theoretical predictions, demonstrate accurate curvature-based trust estimates on single-cell embeddings, and show that the integral analysis distinguishes single-valued embeddings from path-dependent optimization-based embeddings in ways that existing pointwise diagnostics cannot.

---


### 81. [Multiscale Reward Hedging from Correct Demonstrations](https://arxiv.org/abs/2608.06825)

**<font color=#1a73e8>作者：</font>** Pahan Dewasurendra  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Learning from correct demonstrations is harder than supervised learning when many answers are correct: after predicting, the learner sees one valid answer but not whether its own answer was valid, nor any reward. Existing reward-hedging guarantees consequently assume a finite reward class. We give the first horizon-free guarantee for continuous classes. The key is to hedge in one shared vote over tolerant optimality tests at every accuracy scale. A target reward has one surviving proxy per scale, and a prediction with gap above that scale doubles the proxy. This yields the simultaneous tail bound $|\{t:\ell_t>2^{-j}\}|\leq \log_2\mathcal N(\mathcal G,2^{-j-1})+j$, where $\mathcal G$ is the class of optimality-gap functions. Integrating the tails gives cumulative hidden gap bounded by a metric-entropy integral, independently of the number of rounds. Polynomial entropy $(A/\epsilon)^d$ gives $O(d\log A)$ total gap and a fast $O(d/m)$ statistical rate. For bounded linear contextual recommendation, the result is $O(d)$ regret for arbitrary compact menus. This is the first polynomial finite bound without structural restrictions on the menus, at the price of improper prediction. Although the general vote can be expensive, it is exactly polynomial-time for one-dimensional Lipschitz parameter curves. Fixed-radius rank-two recommendation takes $O(KT^2)$ time for menus of size $K$. We also prove an $\Omega(d)$ lower bound, low-rank and bounded ReLU-network corollaries, and a robust theorem that adds only the demonstrator's cumulative suboptimality. A reproducible adaptive stress test illustrates the predicted scale adaptation. After factorization, an exact MovieLens audit runs in 1.7 CPU seconds across ten users and improves mean latent gap over both a demonstrated-rating policy and a proper online baseline. The learner uses only action demonstrations and never observes a reward or a loss.

---


### 82. [POKEx: Performance analysis of POKE-key exchange and SIDH-variants](https://arxiv.org/abs/2608.06826)

**<font color=#1a73e8>作者：</font>** Hyeonhak Kim, Suhri Kim  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> In this paper, we present a comparative performance analysis of the POKE-based key exchange and SIDH variants. SIDH gained attention for its small key size and efficient performance, and has been selected as an alternate candidate in NIST PQC Round 4. However, following the key recovery attack by Castryck and Decru in 2022, SIDH was shown to be vulnerable to polynomial-time attacks on classical computers, undermining its security and removing it from consideration. Given that SIDH was regarded as the leading isogeny-based algorithm, several countermeasures, such as MSIDH, MD-SIDH, and bin/terSIDH have been proposed. However, these approaches still face performance limitations. Meanwhile, POKE, proposed by Basso and Maino at Eurocrypt 2025, is an isogeny-based public key encryption scheme that combines a SIDH-like protocol with higher-dimensional isogenies and has drawn attention for its efficient performance. In this work, we adapt POKE into a key exchange algorithm and benchmark it against M-SIDH, terSIDH, and CSIDH. Targeting NIST security level 1, POKE-based KEM is approximately 21.21 times faster than terSIDH and 64.97 times faster than CSIDH, showing that the POKE-based KEM is currently the most promising isogeny-based key exchange candidate.

---


### 83. [Bend the Basics: Degradation-Aware Deformable Tokenization for All-in-One Image Restoration](https://arxiv.org/abs/2608.06832)

**<font color=#1a73e8>作者：</font>** Zihao He, Yunfeng Wu, Xinchao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> All-in-one image restoration seeks a single model that can recover images degraded by diverse and spatially non-uniform corruptions. However, many unified Transformers rely on fixed patch partitioning: task/degradation condition is injected only into the backbone blocks after tokenization, leaving the embedding and reconstruction stages insensitive to local degradation variations. In contrast to previous approaches, we present Flexible Image Transformer (FIT) that explicitly models degradation awareness across the entire pipeline, from patch sampling to pixel reconstruction. Specifically, FIT employs a lightweight Degradation Encoder to predict a global degradation vector $\mathbf{g}$ and a spatial degradation map $\mathbf{M}$ from local degradation severity, which jointly condition the patch embedding and unembedding through adaptive deformation. Moreover, to improve robustness across degradation types, we introduce a task-token dropout strategy that regularizes task conditioning during training. On five standard benchmarks (BSD68, Rain100L, SOTS, GoPro, and LOLv1), FIT achieves state-of-the-art performance with 30.72 dB average PSNR on the five-degradation setting and 32.83 dB on the three-degradation setting, outperforming recent unified restoration methods by +0.5$\sim$1.1 dB. Moreover, the learned offsets provide a direct handle for visualizing degradation-aware spatial adaptation.

---


### 84. [Graph Machine: Exploring Edge Mechanisms as an Inductive Bias](https://arxiv.org/abs/2608.06834)

**<font color=#1a73e8>作者：</font>** Lintai Hou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Transformers provide a powerful architecture for global content-based matching, but reasoning problems may benefit from a stronger inductive bias toward iterative traversal of latent relations. We introduce Graph Machine, an architecture with two explicit edge-based mechanisms: Edge-augmented attention, in which edges modulate attention between nodes, and edge-centric referral, in which nodes exchange addresses to update their edges. Conceptually, this enables the model to dynamically and differentiably construct and revise relational graphs across layers. We study this inductive bias using Sudoku under controlled settings and find that Graph Machine outperforms Transformer baselines, with ablation studies and mechanistic analysis attributing the gains to the edge mechanisms. Surprisingly, we found that the model discovers a compact edge-based construction for Sudoku geometry. Our results support explicit edge mechanisms as a promising architectural design, motivating broader evaluation.

---


### 85. [GOPI: Generation-Oriented 3D Pose Inference for Furniture Insertion from Single-View RGB-D Indoor Scenes](https://arxiv.org/abs/2608.06836)

**<font color=#1a73e8>作者：</font>** Ruifeng Zhai, Renjie Liu, Guangrun Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We study the problem of inserting new furniture into indoor scene images. Under masked single-view 2D image-plane conditioning, however, the physical scale of the inserted furniture relative to the scene cannot be uniquely determined, making physically grounded furniture placement underdetermined from image evidence alone. We therefore reformulate the task as a combination of 3D pose inference and geometry-guided image generation, where estimating a geometrically plausible 3D placement is essential for reliable synthesis.
To this end, we propose a two-stage framework. For 3D placement, we introduce GOPI, a generation-oriented 3D pose inference framework that addresses the underdetermined nature of single-view furniture insertion through data-driven iterative inference, producing geometrically plausible object placements. For image generation, we develop a geometry-guided conditioning strategy that projects the inferred 3D pose into the image plane as a pixel-aligned constraint, enforcing consistency between the synthesized image and the underlying 3D geometry.
Experimental results validate the proposed framework from both 3D pose estimation and image synthesis perspectives. For 3D placement, GOPI produces poses with stronger geometric feasibility and better consistency with reference layouts than direct regression and vanilla baselines. For image synthesis, our method preserves alignment with the projected 3D geometry across different furniture scales, showing stable projection-generation alignment across the tested furniture scales.

---


### 86. [MIFA: An MILP-based Framework for Improving Differential Fault Attacks](https://arxiv.org/abs/2608.06837)

**<font color=#1a73e8>作者：</font>** Hanbeom Shin, Insung Kim, Sunyeop Kim 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> At ASIACRYPT 2021, Baksi et al. introduced DEFAULT, a block cipher designed to algorithmically resist Differential Fault Attack (DFA), claiming 64-bit DFA security regardless of the number of injected faults. At EUROCRYPT 2022, Nageler et al. demonstrated that DEFAULT's claimed DFA resistance can be broken by applying an information-combining technique. More recently, at ASIACRYPT 2024, Jana et al. improved DFA by searching for differential trails with a single solution. They showed that, for DEFAULT with a simple key schedule, injecting five faults at the fifth-to-last round reduces the key space to one, and for BAKSHEESH, injecting twelve faults at the third-to-last round achieves the same result. In this paper, we propose a new DFA framework that utilizes a Mixed-Integer Linear Programming (MILP) solver. This framework makes it possible to attack deeper rounds than previously achieved, reducing the number of fault injections required for key recovery. Furthermore, we present a method to determine the most efficient fault injection bit positions by systematically analyzing the input differences from all possible single bit-flip faults, thereby further reducing the required number of faults. This systematic analysis has the significant advantage of allowing us to theoretically calculate the required number of faults. Applying our framework, for DEFAULT, injecting three faults at the sixth-to-last round and two faults at the seventh- and eighth-to-last rounds reduces the key space to one.

---


### 87. [Mathematical Principles and Experimental Discoveries of the Emergence of Symbolic Patterns in Artificial Neural Networks](https://arxiv.org/abs/2608.06839)

**<font color=#1a73e8>作者：</font>** Quanshi Zhang, Qihan Ren, Siyu Lou  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Artificial Neural networks (ANNs) are often treated as black-box models, making explainability a central challenge in deep learning. Many engineering methods have been proposed to approximately explain the ANN from various perspectives, such as feature attribution and visualization. However, it remains a long-standing open question whether the complex inference logic of an ANN can be explained exhaustively and concisely as sparse symbolic patterns. This raises a deeper inquiry: does the emergence of symbolic patterns reflect a natural law rather than chance? Here, we show that across a broad class of ANNs trained on diverse tasks, their inference logic can indeed be reformulated as sparse symbolic interactions. We further prove that two common mathematical criteria, which are implicitly required across tasks, lead to the emergence of such sparse symbolic interactions. Empirical evidence confirms that the two criteria hold for the majority of input samples in diverse models. Furthermore, the faithfulness of these interactions is also demonstrated by their strong sample-to-sample and model-to-model transferability, as well as their ability to explain the overall generalization power of ANNs. Our theoretical analysis and extensive experiments provide a solid foundation for symbolic explanations of ANNs, and offer novel insights into the ANN's generalization power. Our findings also highlight the potential of communicative learning, a paradigm in which the inference logic of an ANN can be directly inspected and tuned at the level of symbolic patterns, thus complementing traditional end-to-end learning paradigm. Finally, the observed emergence of symbolic patterns in ANNs suggests that similar symbolic representations may also emerge in other types of black-box systems under certain conditions, because our proof does not depend on any specific ANN architecture.

---


### 88. [ECAD: Expanding Class-Agnostic Detection Beyond Thing-Centric Objectness](https://arxiv.org/abs/2608.06841)

**<font color=#1a73e8>作者：</font>** Liang Wan, Zixin Ren, Yupeng Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection is a fundamental task in visual perception, providing structured region representations for recognition, grounding, reasoning, and interaction. However, existing detection paradigms largely inherit a thing-centric notion of objectness, where detectors are mainly trained to localize discrete and countable object instances. Consequently, many semantically meaningful visual elements, such as sky, road, grassland, water, and sports courts, are often absorbed into the background despite their importance for scene understanding and spatial reasoning. In this paper, we formulate Expanded Class-Agnostic Detection (ECAD), a new setting that aims to discover category-agnostic visual candidates beyond conventional thing-centric objects. To support this setting, we construct BTCO-Bench, a Beyond Thing-Centric Objectness benchmark with category-agnostic box annotations covering both real-world and cross-domain scenarios. We further propose ECADet, a lightweight DETR-based detector built upon a frozen DINOv3 encoder, and introduce Geometry-Aware Expert Regression (GAER) and Prototype-Guided Query Modulation (PGQM) to improve localization and objectness estimation for diverse visual elements, respectively. Extensive experiments show that ECADet consistently outperforms representative class-agnostic and proposal-based detectors on BTCO-Bench, demonstrating the effectiveness of expanded objectness discovery. Code and benchmark will be released.

---


### 89. [Not Always Top-Left: Untangling the Signals that Guide Dashboard Reading Order](https://arxiv.org/abs/2608.06845)

**<font color=#1a73e8>作者：</font>** Nicole Sultanum, Vidya Setlur  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dashboards are widely used interfaces for data analysis, combining multiple visualizations, text, and interactive controls within a single view. While dashboard authors often structure layouts to suggest a logical consumption flow, users may interpret and navigate dashboards differently depending on the interplay between design features, analytical goals, and personal preferences. In this work, we investigate how people make sense of dashboards by examining their reading orders, i.e., the sequences in which users engage with dashboard components. We conduct a mixed-methods study with 18 dashboard authors and 16 end-users, capturing how participants design for and reason through these component transitions. Through qualitative and quantitative analyses of participant-generated flows, we outline a set of factors that influence dashboard reading order, including layout, visual saliency, semantics, functional roles, interaction, and user context. We also identify emergent reading patterns and analyze them through aggregate and variability measures, revealing where users converge and diverge in their interpretations. Finally, we discuss implications and opportunities for computational approaches that aim to automatically model, guide, or serialize dashboard consumption.

---


### 90. [Understanding and Improving Model Editing for Secure Code Generation](https://arxiv.org/abs/2608.06848)

**<font color=#1a73e8>作者：</font>** Weifeng Sun, Quanjun Zhang, Yuchen Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used for code generation, yet they can reproduce vulnerable implementations learned from insecure training patterns. Prior work has mainly explored inference-time hardening, which reduces insecure generations without modifying the target model but relies on auxiliary components and adds runtime overhead. We conduct the first systematic study of model editing as a model-level hardening mechanism for secure code generation. We evaluate 3 state-of-the-art editing methods across diverse LLM families and compare them with CoSec, a representative inference-time approach, focusing on security, robustness, generalization, and functional correctness. Model editing yields larger security gains than CoSec on seen vulnerability types, improving security ratios by 15%-25% over vanilla models, with gains remaining stable under prompt perturbations. However, these improvements transfer unreliably to unseen vulnerabilities and can reduce functional correctness. To mitigate this trade-off, we propose SafeEdit, a post-edit refinement method combining functional tuning with edit-aware regularization. Across eight target LLMs, SafeEdit improves Pass@1 over UltraEdit by 11.73/13.70/15.50 percentage points at T=0.1/0.4/0.8 while largely preserving security. Compared with CoSec, it achieves relative security-ratio gains of 7.54%-12.04%. Additional evaluation on CodeGuard+ confirms improved joint secure-and-correct generation. SafeEdit and CoSec are also complementary, and their combination can further improve security while maintaining strong functional correctness. Overall, our results provide evidence-backed guidance for applying model editing to secure code generation.

---


### 91. [Autonomy-of-Heads: Data-Free Sparse Attention from Frozen Query-Key Geometry](https://arxiv.org/abs/2608.06849)

**<font color=#1a73e8>作者：</font>** Yehan Yang, Junyuan Shang, Yang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context LLM inference is bottlenecked by quadratic attention computation and growing KV-cache costs. Existing sparse attention and KV-compression methods typically decide which tokens or heads to preserve from runtime attention scores, observation windows, calibration prompts, or learned gates, making head diagnosis input-dependent and costly to deploy. We propose Autonomy-of-Heads (AoH), a data-free method that identifies retrieval and streaming heads from the spectral geometry of query-key projections. AoH defines the kernel attention operator $M_h = W_K^{h\top}W_Q^h$ and uses its effective-rank as a weight-space measure of head function: concentrated spectra indicate a small number of dominant query-key matching directions and are associated with retrieval heads, whereas diffuse spectra indicate the absence of a dominant global matching direction and are associated with streaming heads. We further derive an efficient $d_\text{head}$-dimensional computation that avoids constructing the full $d_\text{model}\times d_\text{model}$ matrix. We conducted extensive experiments across models demonstrating that at 50\% sparsity, AoH retains 96.5\% of Full Attention performance on average while reducing prefill and decode latency by up to 41.4\% and 66.0\%, respectively, and KV-cache memory by 50.0\% at 256K tokens.

---


### 92. [RegionDet: A Benchmark for Region Detection Beyond Object Instances](https://arxiv.org/abs/2608.06850)

**<font color=#1a73e8>作者：</font>** Liang Wan, Yuhan Wang, Yupeng Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object detection is a fundamental task in computer vision and has achieved remarkable progress on standard benchmarks by localizing discrete and well-bounded object instances. However, many visual targets in real-world scenarios are not individual objects, but regions defined by visual states, scene context, object relations, and human activities, such as construction areas, damaged road regions, queues, group conversations, and vendor regions. Existing detection benchmarks are mainly built around object instances, providing limited support for systematically evaluating such region targets. To address this gap, we introduce Region Detection, a task that extends conventional object detection beyond object instances, and construct RegionDet, a benchmark for region target localization. RegionDet contains eight region categories, including Construction, Crossing, Damage, Queuing, Talking, Vendor, Waiting, and Walking, with COCO-style bounding-box annotations and evaluation protocols. We systematically evaluate representative closed-set and zero-shot/open-vocabulary detectors on RegionDet. Results show that closed-set detectors can partially learn region-level patterns under supervision, while zero-shot/open-vocabulary detectors struggle severely, revealing the strong object-centric bias of current vision-language detectors. Further analyses highlight key challenges in Region Detection, including weak boundary cues, strong context dependency, and insufficient relation-level region understanding. The RegionDet will be released.

---


### 93. [Bridging the Gap Between Hyperdimensional Computing and Kernel Methods via the Nyström Method](https://arxiv.org/abs/2608.06860)

**<font color=#1a73e8>作者：</font>** Quanling Zhao, Anthony Hitchcock Thomas, Ari Brin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Hyperdimensional computing (HDC) is an approach from the cognitive science literature for solving information processing tasks using data represented as high-dimensional random vectors. The technique has a rigorous mathematical backing, and is easy to implement in energy-efficient and highly parallel hardware like FPGAs and "processing-in-memory" architectures. The effectiveness of HDC in machine learning largely depends on how raw data is mapped to high-dimensional space. In this work, we propose NysHD, a new method for constructing this mapping that is based on the Nyström method from the literature on kernel approximation. Our approach provides a simple recipe to turn any user-defined positive-semidefinite similarity function into an equivalent mapping in HDC. There is a vast literature on the design of such functions for learning problems. Our approach provides a mechanism to import them into the HDC setting, expanding the types of problems that can be tackled using HDC. Empirical evaluation against existing HDC encoding methods shows that NysHD can achieve, on average, 11% and 17% better classification accuracy on graph and string datasets respectively.

---


### 94. [DAEP: Difficulty-Aware Evidence Planning for Medical Video Corpus Temporal Answer Grounding](https://arxiv.org/abs/2608.06869)

**<font color=#1a73e8>作者：</font>** Tianjian He, Yujie Liu, Zhiping Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We describe DAEP, team BIGC's submission to NLPCC 2026 Shared Task 1 Track 3: Difficulty-Aware Temporal Answer Grounding in Video Corpus (DA-TAGVC). The task requires retrieving the target video from 50 candidates and localizing the answer-supporting span. DAEP ranks videos with subtitle, visual, and procedural-context evidence, expands high-scoring anchors into temporal spans, and reranks spans for final output. Its main design is to convert the task-provided simple/complex input label into an inference-time evidence plan controlling modality weights, Top-K aggregation, boundary threshold, expansion length, and reranking strength. In the official evaluation, BIGC ranks first among ten systems with an Average score of 0.2728. Validation ablations show that visual evidence, procedural context, and difficulty-aware planning improve ranking quality, with the largest gain on complex questions.

---


### 95. [CEDAR: Agent-Orchestrated Tree Search for Goal-Directed Optimization of Complex Systems](https://arxiv.org/abs/2608.06871)

**<font color=#1a73e8>作者：</font>** Yingtao Tian  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex systems, core objects of study in artificial life, model diverse phenomena through nonlinear, feedback-driven interactions that produce emergent behavior, with applications from population dynamics and biology to economic policy and strategic decision-making. Yet the difficulty of predicting how feedback structure gives rise to emergent behavior, a central open problem in artificial life, makes goal-directed design exceptionally challenging. In established practice, system structures are written in specialized modeling languages such as DYNAMO or STELLA, compounding the challenge with labor-intensive workflows that limit adoption and hinder timely decision-making. To address these challenges, we introduce CEDAR, an autonomous method that uses Large Language Model (LLM) agents to discover complex systems satisfying user-specified behavioral goals. Our key innovation is an LLM-driven Monte Carlo Tree Search (MCTS) deeply coupled with complex systems: at each iteration, an LLM Judge evaluates emergent behavior against specified goals and an LLM Editor proposes improved variants, with the Judge acting as a fitness function and the Editor as a variation operator, akin to a generate-and-evaluate loop in evolutionary computation. We represent complex systems as a restricted, runnable subset of Python with domain-specific primitives, letting LLMs modify system dynamics directly. CEDAR formalizes this as an MCTS variant with an LLM-parameterized transition kernel and value function, enabling goal-directed discovery of complex system behaviors while preserving solution diversity, and its LLM-based interpretability reveals how structural changes drive emergent behavior. CEDAR reduces human effort while enabling capabilities difficult to achieve with existing approaches, facilitating broader adoption of complex systems across domains.

---


### 96. [ControlRef: Efficient Layout-Guided Multi-Instance Generation via Anchored 4D-RoPE](https://arxiv.org/abs/2608.06878)

**<font color=#1a73e8>作者：</font>** Yunkai Yang, Yudong Zhang, Xinying Chen 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Layout-guided multi-instance generation is essential for controllable image synthesis in Multi-Modal Diffusion Transformers (MM-DiTs). However, integrating this capability into unified architectures remains challenging. Prior frameworks rely on redundant full-resolution canvas padding and Shifted-RoPE to manage multiple reference images. This mechanism drastically inflates computational overhead for sparse layouts and disrupts critical low-frequency RoPE features, creating a severe spatial-frequency compromise that blurs absolute spatial correspondence. To overcome these limitations, we propose ControlRef, a highly efficient and precise multi-instance synthesis framework. ControlRef utilizes a Unified Instance-Layout Control (UILC) attention mask to strictly decouple inter-instance semantic interactions and enforce precise regional binding. To further promote region-level spatial alignment, we introduce Anchored 4D-RoPE, a novel positional encoding mechanism that directly anchors tokens to their absolute geometric centers. By pre-aligning reference images to their corresponding bounding box resolutions, physically anchoring both layout and reference tokens to their absolute geometric centers, and stacking the references along the z-axis, Anchored 4D-RoPE natively preserves spatial priors and mitigates the spatial-frequency compromise without lossy shifting. Extensive experiments demonstrate that ControlRef achieves state-of-the-art visual fidelity and localization accuracy, while concurrently slashing inference latency by over 80% in sparse layouts and reducing memory overhead by 50% in dense scenarios.

---


### 97. [SkillAligner: Treating Retrieved Skills as Adaptable Drafts at Execution Time](https://arxiv.org/abs/2608.06880)

**<font color=#1a73e8>作者：</font>** Qinfeng Li, Dalin He, Yuntai Bao 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> General-purpose skills promise reusable procedural knowledge for language agents, yet semantic relevance does not guarantee execution utility: a retrieved skill may encode assumptions that conflict with the current task, execution environment, or other retrieved skills. We formalize this problem as the skill--execution misfit. To address it, we propose SkillAligner, a training-free execution-time skill adaptation framework that treats retrieved skills as adaptable drafts rather than fixed instructions. Before execution, SkillAligner performs a one-time joint adaptation that specializes useful skill fragments to task requirements, aligns their procedural assumptions with the available execution interface, and composes the resulting guidance by resolving dependencies, conflicts, and redundancy across skills. The adapted content is consolidated into a compact execution guide and reused throughout the subsequent trajectory. Extensive experiments across diverse agent benchmarks and model backbones show that SkillAligner substantially improves task performance over existing skill-use baselines, reduces skill-induced regressions at the instance level, and lowers total inference cost.

---


### 98. [Georeferencing Non-Gazetteered Place Names using Biological Specimen Records](https://arxiv.org/abs/2608.06884)

**<font color=#1a73e8>作者：</font>** Aneesha Fernando, Surangika Ranathunga, Kristin Stock 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biological specimen records collected by natural history institutions constitute a rich source of temporal geographic knowledge, capturing biodiversity information about regional landscapes as they were recorded at different times. Using digitised data from the Allan Herbarium (New Zealand), this study identifies place names in these specimen locality descriptions that are absent from current gazetteers; we refer to these as non-gazetteer place names (NGPs). These place names are typically historical, vernacular, or colloquial and were used as landmarks to describe a specimen's location at the time of collection. We then investigate the problem of georeferencing the NGPs using only the limited information available in the specimen records. To resolve this, we leverage repeated occurrences of the same place name across specimen records with different specimen locations and spatial relation terms, extracting and inverting these relations to derive constraints on NGP locations. This approach is instantiated within deterministic, probabilistic, and LLM-based methods, enabling a comparative analysis of their strengths and limitations for text-based spatial inference. On a pseudo-NGP benchmark, probabilistic inference achieves the highest accuracy (median error 1.43 km; A@1 km 36%), while the LLM yields competitive but less precise estimates (median error 1.80 km; A@1 km 31%), indicating that, despite advances in LLMs, traditional modelling remains advantageous when high spatial precision is required.

---


### 99. [Rigid-Covert GNSS Spoofing of UAV Swarms: A Structural Blind Spot, Its Detection Limit, and Absolute-Anchor Defenses](https://arxiv.org/abs/2608.06885)

**<font color=#1a73e8>作者：</font>** Minseok Park, Joon Soo Yoo  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cooperative UAV-swarm defenses commonly cross-check GNSS positions against measured inter-drone geometry. We show that this relative-geometry channel has a structural blind spot: a common, slowly varying translation (a rigid-covert shift, RigidShift) preserves all pairwise distances and is therefore unobservable to any relative-only detector (a gauge-freedom argument). We validate this blindness on distance-verification and semidefinite-feasibility baselines, while explicitly distinguishing it from onboard inertial/GNSS monitors that can raise a bare alarm but cannot recover the swarm's true position. To quantify when an external reference restores observability, we derive the drift-dependent detection floor $2\gamma/(1-t_s/T)$ for a calibrated anchor-residual detector and empirically identify an additional detector-specific noise floor (measured slope 2.66 vs. predicted 2.67). We then present a centralized anchor-rooted recovery pipeline that reconstructs swarm geometry from inter-drone ranges, aligns it to a trusted-anchor subset with Byzantine-robust fitting, and recovers the absolute positions of non-anchored drones. A segmented estimator jointly estimates anchor drift, attack rate, and onset when no clean-epoch label is available. Across statistical simulations, ArduPilot software-in-the-loop experiments, and Gazebo experiments with rendered vision anchors, the method recovers the positions of non-anchored drones to a median error of 0.39 m (20 seeds) under approximately 10.1 m of GNSS drift, and to 7.1 cm (5 seeds) in the rendered-vision multi-SITL setting. We also characterize the explicit limits imposed by non-collinear anchor geometry, anchor coverage, $\tau\to0$ drift-attack aliasing, and majority anchor compromise. All evaluations are simulation-based and use no RF spoofing hardware or physical swarm.

---


### 100. [HazeSpikeMamba: Coupling Spiking-Inspired and State-Space Features for Self-Supervised Real-World Dehazing](https://arxiv.org/abs/2608.06886)

**<font color=#1a73e8>作者：</font>** Haoran Liu, Huibin Li, Mingzhe Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Dehazing networks are commonly trained on synthetic hazy-clear pairs, but their performance often drops on real photographs. Synthetic haze generated using the atmospheric scattering model does not fully capture the variability of real haze, and paired real hazy-clear images are scarce. In this work, we propose HazeSpikeMamba, a compact dehazing framework that combines a spiking-inspired local path and an attentive state-space global path in a multi-scale U-Net. The local path uses TPCNNSpike, a new spike-emission scheme inspired by the neighborhood coupling of Pulse-Coupled Neural Network (PCNN). Unlike grouped directional scanning, TPCNNSpike updates all neurons in parallel using the previous firing states of their Gaussian-weighted neighborhoods. The global path adapts the Attentive State-Space Module of MambaIRv2, retaining semantic prompting and sequence reordering while removing the window self-attention branch. Its state-space processing models long-range dependencies with complexity linear in sequence length. For target-domain adaptation, a frozen degradation network, pretrained on paired NH-HAZE data, re-synthesizes haze from the dehazed prediction. The reconstruction error updates only the final restoration layers of HazeSpikeMamba without haze-free labels during adaptation. A shared checkpoint is adapted once on each complete unlabeled target set, making the evaluation dataset-level and transductive rather than zero-shot or per-image optimization. The forward network contains 2.02M active parameters and requires 13.27G nominal MACs (measured with thop at 256x256 input). This adaptation consistently improves BRISQUE and NIMA on RTTS, URHI, and HSTS. On RTTS, BRISQUE decreases from 30.13 to 27.72 and NIMA increases from 4.13 to 4.87. Under this transductive protocol, the adapted model also achieves the best BRISQUE and NIMA on URHI and HSTS among the compared methods.

---


> [!TIP]
> 当前位于：**51-100**（第 2/5 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-221](./part-05.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
