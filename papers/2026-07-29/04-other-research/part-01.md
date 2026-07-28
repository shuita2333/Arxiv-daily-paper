# 📦 其他研究 | 2026年07月29日

> 本类共 **442** 篇论文

> 未进入大模型主领域展示范围的其他研究。

> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-442](./part-09.md)

---

### 1. [Concept-based Visual Counterfactual Explanations with Diffusion Models](https://arxiv.org/abs/2607.22544)

**<font color=#1a73e8>作者：</font>** Yassine Oueslati, Daniil Kirilenko, Martin Gjoreski 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual counterfactual explanations aim to answer "what minimal change to this image would flip the model's prediction?", and are increasingly important as vision models are deployed in safety-critical domains (e.g., medicine). Existing diffusion-based methods can produce realistic edits, but they rely on external classifiers that must work reliably on noisy images, which makes them fragile and hard to deploy for robust explanations. We introduce C-VCE, a new diffusion framework that builds the classifier directly into the generative model via a concept bottleneck layer, so that counterfactuals are guided by human-interpretable features (concepts) instead of a separate noise robust classifier that works with pixel-level edits. Our model lets users to toggle on/off semantic concepts during sampling, then minimally adjusts relevant image regions, while preserving the rest of the image, respecting feature correlations. To keep edits small and controlled, we add a simple probabilistic regularizer that balances "change the prediction" against "stay close to the original", plus a gradient-based mask that confines modifications to the most relevant regions. On benchmarks such as CelebA, C-VCE matches or improves flip rates while producing counterfactuals that are visually closer to the input and less distorted than baselines that depend on separate noisy-image classifiers. These properties make C-VCE a practical tool for vision systems where users need concrete "what-if" images without having to trust an additional, noise-robust classifier. More broadly, our results suggest that exposing and controlling an internal concept layer is a promising way to make powerful generative models easier to understand and safer to use.

---


### 2. [Explaining GAND: A Resource on Gender-Ambiguous Natural Data & Contrastive Attribution](https://arxiv.org/abs/2607.22546)

**<font color=#1a73e8>作者：</font>** Janiça Hackenbuchner, Jasper Degraeuwe, Arda Tezcan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Machine translation (MT) systems continue to produce gender-biased translations. In a time where self-expression is paramount, mistranslations based on default behaviour and stereotyping can lead to harm for users of these systems. To better understand how these systems translate gender in the absence of clear gender cues, we need benchmarking resources that reflect gender-ambiguous scenarios in a natural way. To this end, we present GAND, a gender-ambiguous natural data benchmarking resource for MT consisting of English source sentences, specifically designed to analyse the influence of contextual cues on gender in translation. We leverage GAND to conduct an interpretability analysis: we translate a subset of GAND into two grammatical gender languages and extend these with manually crafted contrastive translations. A following feature attribution analysis reveals source words in context that inform the gender translation of an ambiguous referent entity in the target translation.

---


### 3. [QFoldAgent: An Autonomous Quantum Optimization Multi-Agent System for Protein Structure Prediction](https://arxiv.org/abs/2607.22549)

**<font color=#1a73e8>作者：</font>** Winson Chen, Yuqi Zhang, Sixu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hybrid quantum-classical protein structure prediction depends strongly on Hamiltonian penalty weights, yet existing lattice-based workflows typically fix these coefficients by hand and evaluate only very short fragments in simulation. We present QFoldAgent, a closed-loop multi-agent framework for 5-residue tetrahedral-lattice folding in which a design agent proposes sequence-conditioned penalties, a VQE-based quantum-classical pipeline optimizes the resulting Hamiltonian under Qiskit Aer noise, and a feedback agent uses energy-landscape diagnostics and MolProbity validation signals to refine penalties across cycles. Ground-truth metrics such as RMSD are never exposed to the agents and are used only for evaluation. We study the framework on two complementary datasets: 55 QDockBank-derived fragments with known structures and 100 coverage-optimized unseen sequences. On the QDockBank benchmark, QFoldAgent reduces median RMSD from 3.64 Å to 3.20 Å, with the largest gains on the hardest targets. On unseen sequences, the closed loop raises structural validity from 87.5% to 98.7%, recovers 87% of initially invalid cases, and the strongest controller improves cycle-3 energy on 87% of sequences while maintaining 96% Ramachandran-favored geometry. These results show that iterative agent control can systematically improve optimization behavior and reduce failure cases in a 5-residue quantum setting.

---


### 4. [Codifying the Judge: Scalable Evaluation via Program Distillation](https://arxiv.org/abs/2607.22561)

**<font color=#1a73e8>作者：</font>** Tzu-Heng Huang, Shengqi Qiu, Frederic Sala  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge has become the standard for automated evaluation, but it suffers from high cost, significant latency, and opaque decisions -- limitations that undermine its scalability and reliability. We address these with a simple, efficient alternative: program distillation. Instead of prompting an LLM at the evaluation time, we distill its decision logic into a committee of programs that score candidates directly. These programmatic judges offer transparency, are easily inspected or edited, and eliminate per-sample API costs. Building on this notion, we introduce PAJAMA, a system that synthesizes programs as judges, aggregates their decisions into a joint verdict, and incorporates a fallback mechanism to selectively escalate low-confidence cases to an LLM. Across five datasets and four model families, we show that programmatic judges can match the performance of a 13B-size LLM judge. When using program outputs as routing signals, PAJAMA improves both accuracy and throughput and advances the Pareto frontier. Beyond evaluation, programmatic judges produce cheap and effective reward signals: on RewardBench, a reward model distilled from programs' verdicts outperforms one trained on a proprietary LLM's labels at two orders of magnitude lower API cost.

---


### 5. [Synthetic Scenario Generation for Evaluation of Industry 4.0 Agents](https://arxiv.org/abs/2607.22563)

**<font color=#1a73e8>作者：</font>** Sagar Chethan Kumar, Rohith Kanathur, Dhaval Patel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Industrial agent benchmarks require realistic evaluation scenarios that integrate telemetry, failure modes, maintenance records, and domain standards. However, existing benchmarks such as AssetOpsBench rely on manually authored scenarios and cover a limited set of asset classes. We extend AssetOpsBench with a Smart Grid Transformer asset class and four IEC-grounded diagnostic tools for health-index prediction, dissolved-gas analysis, winding-temperature assessment, and load-profile assessment. We further introduce ScenarioGeneratorAgent, a pipeline for synthetic industrial-agent scenario generation. The pipeline constructs evidence-grounded asset profiles, allocates coverage-aware scenario budgets across operational domains, and generates candidates through a hybrid validation-and-repair loop that enforces schema validity, tool reachability, physical plausibility, standards alignment, and deduplication. To improve scalability, we apply two-level caching, parallel focus-group generation, thread-pool offloading, batched LLM calls, and early rejection filtering. On Smart Grid Transformer scenario generation, these optimizations reduce end-to-end runtime by $8\times$ for 50 scenarios while preserving quality, achieving a composite quality score of $74.2 \pm 1.9$ compared with $73.8 \pm 3.0$ for the unoptimized baseline. These results show that standards-grounded synthetic scenario generation can efficiently expand industrial-agent benchmarks without sacrificing scenario quality.

---


### 6. [Loss-Aware Feature-Map Pruning in Convolutional Neural Networks Using Multi-Armed Bandits](https://arxiv.org/abs/2607.22564)

**<font color=#1a73e8>作者：</font>** Salem Ameen, Sunil Vadera  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Convolutional neural networks often contain redundant feature maps that increase storage and inference cost. This paper presents a loss-aware feature-map pruning framework using multi-armed bandits. Feature-map pruning is structured because it removes complete convolutional output channels and their producing filters rather than isolated scalar weights. Each candidate feature map is treated as an arm. At each play time, one map is temporarily masked and evaluated on a sampled mini-batch; the map is then restored and the observed loss change is converted into a safe-removal reward. After a fixed play budget, candidate maps are ranked by learned scores and the top-k maps are permanently removed with their filters, biases and corresponding next-layer input-channel kernels. The study evaluates UCB1 and Thompson Sampling, compares them with direct/oracle-style evaluation on LeNet/MNIST, and extends the evaluation to MNIST, CIFAR-10, CIFAR-100, SVHN, CUB-200-2011 and Oxford Flowers 102. Results show that UCB1 and Thompson Sampling preserve accuracy close to unpruned models while removing feature maps and reducing convolutional computation. Friedman and Nemenyi tests show that UCB1 obtains the highest mean rank, followed by Thompson Sampling; both significantly outperform greedy and magnitude-based pruning while remaining statistically comparable to the original unpruned model.

---


### 7. [DSTFView: Multi-View Cloud-Edge Workload Forecasting with Dual-Input Spatio-Temporal-Frequency Modeling](https://arxiv.org/abs/2607.22565)

**<font color=#1a73e8>作者：</font>** Qingzhong Li, Hui Ma, Yajun Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the widespread deployment of edge-side AI inference, edge platforms are increasingly required to support latency-sensitive, highly concurrent, and reliability-critical applications. However, existing methods often struggle to balance multidimensional feature modeling and forecasting efficiency in collaborative cloud-edge environments. To address this issue, we propose DSTFView, a dual-input spatio-temporal-frequency multi-view workload forecasting framework for collaborative cloud-edge environments. It jointly models closeness and period dependencies and extracts spatial, temporal, and frequency-domain dependencies. Besides, it designs an adaptive fusion mechanism and adjusts the contribution of each view to capture abrupt changes. Experimental results on the CPU and TP datasets demonstrate that DSTFView consistently outperforms representative baselines across multiple forecasting horizons and evaluation metrics.

---


### 8. [Execution-Grounded Security Testing for Coding Agents in Software Engineering Pipelines](https://arxiv.org/abs/2607.22569)

**<font color=#1a73e8>作者：</font>** Yifei Ge, Weisong Sun, Jinkun Xiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are increasingly integrated into system operations, where their tool use can directly modify project artifacts, execution environments, and the underlying system. For example, if a coding agent inserts a hook into a system startup or configuration script, that change can persist after the interaction, be triggered later, and abuse delegated user or system privileges to modify the system. This makes security testing a system problem: the key question is not only what the agent says, but what it actually does to the surrounding environment. We present an execution-grounded red-team testing framework for probing this execution-layer security boundary using observable sandbox evidence, including tool invocations, runtime traces, and file-system diffs. Our framework embeds target unsafe operations into routine software engineering workloads, including unit testing, regression testing, crash reproduction, and validation, and uses an execution oracle to guide refinement when an initial probe is rejected or fails. Across multiple agent frameworks and model backbones, our red-team workload reformulation substantially increases verified unsafe execution, reaching 73.61% on code carriers and 53.93% on text carriers. These results show that coding agents in system operations remain insecure under task disguise: once risky intent is hidden inside plausible engineering tasks, the agent can be induced to carry out unsafe actions on the surrounding system. More broadly, coding agents in system operations still demand stronger security testing and safeguards.

---


### 9. [PhononBench-MP40: a spectrum-resolved benchmark dataset for phonon stability](https://arxiv.org/abs/2607.22573)

**<font color=#1a73e8>作者：</font>** Wen-Kao Li, Ze-Feng Gao, Zhong-Yi Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Imaginary phonon modes remain a practical bottleneck in computational materials screening because otherwise plausible structures can be locally dynamically unstable under a chosen workflow. Here we present PhononBench-MP40, a spectrum-resolved benchmark dataset of Materials Project-derived crystals for workflow-defined phonon stability. The dataset starts from 47,969 MP40 workflow tasks and provides 46,899 completed records with paired stability labels and local phonopy YAML spectra, including 16,683 Stable records and 30,216 completed-phonon unstable records. A further 1,067 relaxation failures are reported separately rather than merged into the completed phonon denominator. The release centers on the local YAML spectrum: the stability label, the lowest sampled frequency and any threshold-dependent relabeling are derived from that spectrum. The dataset is openly available through Science Data Bank at this https URL. A companion GitHub repository provides the calculation code and lightweight access utilities. PhononBench-MP40 provides an auditable reference for workflow-defined stability classification, minimum-frequency analysis, threshold studies and failure-aware triage, while keeping the reference workflow, data schema and interpretation boundaries explicit.

---


### 10. [The Scaffold Effect in Coding Agents: Harness Choice as a Hidden Variable in Coding-Agent Evaluation](https://arxiv.org/abs/2607.22585)

**<font color=#1a73e8>作者：</font>** Naman Vats, Oleg Golev  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Public leaderboards for coding agents typically rank systems by model name and pass rate, while the surrounding harness (the scaffold that issues tools, manages context, and decides when to stop) is often under-specified. Model-to-model comparison is valid when the harness is fixed; when it varies, performance and efficiency conflate model and scaffold effects. We evaluate Qwen 3.6 Plus and MiniMax M2.5 across three open-source harnesses (Goose, OpenCode, OpenHands-SDK) on a stratified 50-task subset of Terminal-Bench Pro. Harness choice induces up to a 40x difference in tokens per solved task, while paired within-model pass-rate differences remain 0-8 percentage points (95% paired-task bootstrap CIs include zero except for the largest gap). Failure fingerprints replicate across models (REASON for Goose, VERIFY/MAX_TURNS for OpenHands-SDK, idle-loop/TIME for OpenCode), indicating harness-level biases that are largely model-independent. For human-centered coding-agent evaluation, model name alone is an incomplete comparison unit: harness-model pairs determine real-world cost, latency, and oversight burden; no-action turns are a per-task wait tax, not just a token tax. We therefore recommend selecting harness-model pairs by pass rate under token/latency budgets, and reporting token usage, latency, and full harness specifications alongside any model comparison. We release anonymized configs, raw trial logs, aggregated snapshots, and analysis scripts.

---


### 11. [xMIx: High-Performance Serving-Time Platform for Mechanistic Interpretability Apps](https://arxiv.org/abs/2607.22595)

**<font color=#1a73e8>作者：</font>** Michael Blum, Mark Silberstein, Yaniv David  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mechanistic interpretability (MI) has emerged as a powerful approach for analyzing and intervening in inference computations, with a growing number of applications such as jailbreak attempt detection, truthfulness evaluation, and hallucination detection. Unfortunately, MI deployment in production model-serving systems is currently not practical, as most existing MI frameworks introduce prohibitively high runtime overheads. The fundamental problem is that MI functions do not compose cleanly with served models: they fragment deployment, often force draining requests and rebuilding serving state, and conflict with critical performance optimizations such as continuous batching and CUDA-graph execution, essential for production deployments.
We present xMIx, a serving-native framework for deploying MI applications in production inference serving environments. xMIx enables attaching MI functions to a predefined set of locations in the model runtime, interposing on activations within the layers and residual streams. xMIx supports conditional invocation of MI functions depending on the outputs in preceding model layers. Multiple MI applications can be deployed in a single model instance. xMIx compiles them all into the serving path but activates them dynamically at runtime only when necessary, with negligible performance cost, and without requiring a separate model instance or alternative execution stack.
We integrate xMIx with the vLLM serving system and evaluate it across three major models and seven diverse MI applications. xMIx achieves performance comparable to native vLLM execution, incurring a slowdown of 1.3% mean inter-token latency (ITL), 1.2% for tail P99 ITL, 2.6% for mean time to first token (TTFT), and 1.6% for mean total token throughput (TTT).

---


### 12. [Differencing the Diffusion Trajectory toward Uncertain Components for Time Series Forecasting](https://arxiv.org/abs/2607.22599)

**<font color=#1a73e8>作者：</font>** Chen Su, Yuanhe Tian, Yan Song  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Diffusion models have become a widely used framework for probabilistic time series forecasting, modeling the distribution of future values given an observed history. In time series forecasting, however, the future continues the observed history, creating an asymmetry the standard diffusion process leaves unaddressed, with slowly-varying content largely determined by the observed continuity while higher-frequency dynamics carry most of the residual uncertainty. Existing diffusion-based forecasters decouple this asymmetry through an external rule before generation, leaving the corruption trajectory blind to which parts of the target the history can already anchor. We propose DiffDiff, a diffusion framework that embeds this predictability asymmetry into the diffusion trajectory itself, so that a single end-to-end diffusion process becomes aware of which parts of the target the history can already anchor. DiffDiff makes the forward operator step-dependent so that the noisy intermediate state progressively shifts from the target itself toward its second-order differenced structure, while a conditioning pathway supplies the denoiser with both value-domain and differential history information balanced by a stage-adaptive gate at each diffusion step. The terminal distribution approaches a standard Gaussian, preserving compatibility with existing samplers. On seven benchmarks across four prediction horizons, DiffDiff outperforms six diffusion baselines, and our analysis confirms that DiffDiff concentrates the diffusion's generative effort on the most uncertain components of the target while relieving it from rebuilding the history-anchored content.

---


### 13. [CHS-SQL: A Text-to-SQL approach based on Confidence-Guided Heuristic Search Schema Linking process](https://arxiv.org/abs/2607.22624)

**<font color=#1a73e8>作者：</font>** Minghao Yang, Yanjun Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recently, there have been several works in the Text-to-SQL domain that utilize Small Language Models (SLMs) for training. These approaches achieve performance close to that of large models in generating SQL, using only the computational power of a single NVIDIA RTX 4090 GPU, while also ensuring data security. Most existing methods filter out redundant tables and columns during Schema Linking to improve Text-to-SQL accuracy. However, they do not consider the precision-recall trade-off when selecting the candidate schema subset. Our research found that both the precision and recall of Schema Linking directly affect the final SQL accuracy. Therefore, we propose a novel framework for efficiently fine-tuning SLMs on Text-to-SQL tasks, CHS-SQL, that not only balances precision and recall but also improves overall performance on Text-to-SQL tasks. Its main innovation lies in the Schema Linking phase, where a heuristic search combined with model internal confidence is employed to achieve an optimal precision-recall trade-off. This elaborated mechanism maximizes the precision of relevant schema candidates for the generated SQL queries while suppressing irrelevant noise. The same strategy is further applied during SQL generation to refine candidate queries while helping the SLM to avoid trapping in a local optimum. Our method achieves state-of-the-art (SOTA) results on Text-to-SQL tasks via SLMs.

---


### 14. [Evolving from Lessons: Skill-Augmented Table Graph Reasoning for Operation-wise Table Question Answering](https://arxiv.org/abs/2607.22633)

**<font color=#1a73e8>作者：</font>** Guixin Su, Qiankun Pi, Mayi Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Table Question Answering (TableQA) aims to reason over tables to answer user queries. Existing research treats all questions uniformly and evaluates solely through overall accuracy, obscuring a critical reality that LLMs excel at simple lookups yet struggle with complex operations like aggregation and arithmetic. To reveal this disparity, we introduce a novel \emph{Operation-wise TableQA} task with a fine-grained question taxonomy and release two datasets named WikiTQ-ow and TabFact-ow for evaluation. As for modeling bottlenecks, existing methods flatten tables into linearized texts, disrupting inherent structures and inducing the ``lost-in-the-middle'' issue, which poses a primary barrier to complex cross-row reasoning. Moreover, they typically reason from scratch, neglecting reusable patterns shared across similar operations. To address these limitations, we propose a Skill-augmented Table Graph Reasoning (SkillTGR) framework for self-evolving structured reasoning. Specifically, SkillTGR represents tables as attributed graphs with explicit row-column-cell structures, where LLMs plan and execute dynamic chains to retrieve evidence subgraphs for graph traversal reasoning. Based on this, SkillTGR builds a hierarchical SkillBank to distill reason trajectories into abstract skills under cognitive heuristics, then hybrid retrieves both successful and failed skills for contrastive augmented table graph reasoning, thereby enabling the continual self-evolution. Extensive experiments demonstrate that SkillTGR achieves superior performance with an average of 5.91\% overall and 6.03\% operation-wise improvement, also reducing 19.76\% token consumption and 27.64\% inference latency. Our codes and data will be released upon publication.

---


### 15. [CallBench: A Benchmark for Dual-Goal Coordination in Phone Call Assistants](https://arxiv.org/abs/2607.22635)

**<font color=#1a73e8>作者：</font>** Xuzhao Geng, Haozhao Wang, Xuelian Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Target-oriented dialogue systems have demonstrated strong capabilities in completing user goals through interactive conversations. However, existing studies are primarily designed for single, explicit goal completion, while phone call assistants face a proxy setting that requires coordinating the device owner's explicit preset goal with the caller's implicit and dynamic goal. We introduce \textsc{CallBench}, a Chinese benchmark for evaluating dual-goal coordination in phone call assistants. \textsc{CallBench} contains 50,000 complete multi-turn phone call dialogues across six scenarios: takeout, delivery, taxi, work, life, and harassment. It covers regular presets, emergent presets, and no-preset cases, and includes diverse relations between owner-side and caller-side goals, such as alignment, complementarity, irrelevance, and conflict. We further design a preset-aware turn-level evaluation protocol covering semantic understanding, context use, active guidance, response quality, preset compliance, dialogue rhythm, and safety. Experiments on representative dialogue methods show that existing approaches still struggle with this task, highlighting the need for phone call assistants that can make reliable turn-level decisions between two independent goals under proxy constraints.

---


### 16. [Answering Path Queries under Linear and Guarded Existential Rules](https://arxiv.org/abs/2607.22636)

**<font color=#1a73e8>作者：</font>** Jean-François Baget, Meghyn Bienvenu, Marie-Laure Mugnier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontology-mediated query answering is concerned with the problem of answering queries over knowledge bases consisting of a database instance and an ontology. While most work in the area focuses on conjunctive queries (CQs), navigational queries have gained increasing attention. In this paper, we investigate the complexity of answering two-way (conjunctive) regular path queries ((C)RPQs) over knowledge bases whose ontology is given by a set of guarded existential rules. We first consider the subclass of linear existential rules and show that (C)RPQ answering is NL-complete in data complexity, which matches the data complexity of answering RPQs over plain graph databases (i.e., without an ontology). In combined complexity, both tasks are ExpTime-complete in the general case, but RPQ and CRPQ answering drop to PTime-complete and PSpace-complete respectively if there is a bound on predicate arity. For guarded rules, we provide a non-trivial reduction to the linear case, which allows us to show that the complexity of (C)RPQ answering is the same as for CQs, namely 2ExpTime-complete in combined complexity (ExpTime-complete in the bounded-arity case) and PTime-complete in data complexity.

---


### 17. [Fast Cross-Scenario Adaptation of CSI Models via Channel Conditional Parameter Generation](https://arxiv.org/abs/2607.22637)

**<font color=#1a73e8>作者：</font>** Xudong Zou, Siyu Wu, Zunlei Feng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep learning has shown strong potential for massive multiple-input multiple-output (Massive MIMO) physical-layer tasks, including channel state information (CSI) feedback and channel estimation. However, environmental heterogeneity can severely degrade CSI models in unseen scenarios, while conventional adaptation requires target-domain data and substantial computation. This paper proposes Channel Conditional Parameter Generation (CCPG), an end-to-end pipeline for rapid deployment of CSI models in dynamic wireless environments. CCPG identifies scene-sensitive adaptation bottlenecks through component-freezing experiments and generates only lightweight LoRA weights instead of full model parameters. It compresses high-dimensional channel features into compact latent conditions using cascaded SVD and a Perceiver Resampler. An energy-based canonicalization mechanism mitigates permutation and sign ambiguities in LoRA weights, while a diffusion-based generator incorporates structural information and an asymmetric size-aware loss for topology-aware parameter generation. Experiments on DeepMIMO and WAIR-D for CSI feedback and channel estimation show that CCPG adapts to new scenarios in about 3 seconds with a single forward pass, without target-scenario training or fine-tuning, and achieves cross-domain recovery performance comparable to costly online adaptation. These results demonstrate that CCPG enables efficient deployment of CSI models in large-scale dynamic wireless scenarios for intelligent 6G communications.

---


### 18. [DocHRL: A Hierarchical Reinforcement Learning Framework for Cost-Optimised Document Classification](https://arxiv.org/abs/2607.22644)

**<font color=#1a73e8>作者：</font>** Mohammed Yousif, Prabhjot Singh, Arjun Pankajakshan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Real-world document classification pipelines typically apply the same sequence of models to every incoming document, regardless of its complexity or type. This leads to inefficient use of compute and human resources: simple documents are over-processed while difficult ones may not receive enough scrutiny. We introduce DocHRL, a hierarchical reinforcement learning framework that learns to adaptively and dynamically select the most cost-effective classification policy on a per-document basis. DocHRL formulates document classification as a sequential decision problem with a two-level policy hierarchy: a top-level policy selects among broad options (vision classifiers, LLMs, OCR, and human-in-the-loop review), while option-specific sub-policies choose the concrete model or tool to invoke. The reward signal is the negative total expected cost, which captures inference cost, cost of misclassification, and cost of human labelling. Trained with Proximal Policy Optimisation on the RVL-CDIP benchmark, DocHRL achieves a macro F1 of 0.973 across 16 document classes while reducing average per-document cost to 2.74 normalised units compared to substantially higher costs incurred by fixed standalone classifiers. Our results demonstrate that cost-aware reinforcement learning can simultaneously improve classification performance and operational efficiency in document understanding systems.

---


### 19. [PTStore (Prefix Tensor Store): Distributed Prefix Caching and Replication for High Throughput Inference Serving](https://arxiv.org/abs/2607.22648)

**<font color=#1a73e8>作者：</font>** Meghana Maghyastha, Robert Underwood, Randal Burns 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inspired by the design of client caching in Content Delivery Networks (CDNs), PTStore distributes and replicates popular tensors that form reusable KV cache prefixes, which are the main technique used by state of art approaches to accelerate inferences. This reduces the latency of accessing the KV cache and alleviates load imbalance caused by a disproportionately large number of requests on servers containing popular tensors. Furthermore, thanks to decentralization, PTStore allows the expansion of the size of the KV cache for LLM inference by orders of magnitude. As a result, PTStore can execute inferences on long passage Q\&A datasets 5-6 times more efficiently than current baselines, which do not aggregate memory across different nodes and GPUs and therefore require regenerating the KV cache.

---


### 20. [MINT-V2X: A Mobility-Integrated Network Trajectory Dataset for Predictive Resource Management](https://arxiv.org/abs/2607.22654)

**<font color=#1a73e8>作者：</font>** Abdullah Anjum, Abdolazim Rezaei, Mehdi Sookhak  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vehicle-to-Everything (V2X) communication systems are based on datasets that not only contain vehicle trajectory data but also wireless network parameters with a realistic level of fidelity, enabling the creation of prediction and optimization models. There is a very critical research infrastructure gap today, and publicly available datasets are likely to be limited to one of the two: mobility or network parameters, and rarely provide a single, integrated view that combines both. This paper introduces MINT-V2X, a comprehensive dataset generated by coupling SUMO traffic dynamics with OMNeT++/Simu5G network simulation. The validation framework is composed of 14 standardized tests based on 3GPP Release 14 (C-V2X), ETSI standards and Shannon capacity theory. The resulting dataset contains 9.87 million synchronized data points from 1,386 vehicles from 15 roadside units (RSUs) during 3 hours of urban traffic simulation. We demonstrate strict algorithmic consistency through network metric correlations (CQI-SINR: 0.993; SINR-PDR: 0.946). Finally, we demonstrate the value of the dataset by conducting an RSU load prediction case study, showing that using trajectory data yields better predictive performance than network-history-only baselines. The dataset, experiments, and complete SUMO configuration files are available in the GitHub repository to facilitate reproduction on alternative simulation stacks.

---


### 21. [CuraWeb: Joint Optimization of Quality, Redundancy, and Diversity for Web-Scale Pretraining Data](https://arxiv.org/abs/2607.22662)

**<font color=#1a73e8>作者：</font>** Peiguang Li, Yongwei Zhou, Juncheng Diao 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-web corpora curated via highly selective filters, such as FineWeb-Edu and DCLM, constitute the core of LLM pretraining data and have significantly advanced LLM performance. However, these pipelines typically rely on singular optimization objectives, which inevitably narrows distributional diversity and marginalizes long-tail knowledge, thereby restricting data coverage and underutilizing the vast potential of the open web. To address this limitation, we propose a novel curation paradigm that shifts from linear pruning to the joint optimization of quality, redundancy, and diversity. This framework synergizes dual-track cleaning (rule-based and model-driven) with hybrid deduplication (n-gram and semantic), while employing a multi-objective sampler to balance informational quality with distributional breadth. Applying this framework to Common Crawl, we construct CuraWeb, a 2T-token English corpus. Unlike existing resources, CuraWeb establishes an industrial-grade standard for data curation by recovering a more holistic data distribution with enhanced diversity and minimal redundancy, achieving broader coverage of long-tail knowledge across diverse domains. Experimental evaluations at the 3B scale demonstrate that CuraWeb significantly outperforms state-of-the-art baselines, yielding an average performance gain of 1.8\% across a wide range of benchmarks, particularly in knowledge-intensive and reasoning tasks.

---


### 22. [Obliviate: Efficient Unlearning in Recommender Systems](https://arxiv.org/abs/2607.22665)

**<font color=#1a73e8>作者：</font>** Tushar Prakash, Brijraj Singh, Niranjan Pedanekar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Machine unlearning is becoming increasingly critical in the context of data privacy regulations, particularly for recommendation systems that are directly trained on user interaction data. The goal of this work is to remove requested interaction data and their downstream influence from trained model while preserving recommendation quality, and to do so without incurring the substantial computational cost of full retraining. Existing approaches exhibit several limitations, including limited unlearning completeness and degradation in recommendation performance, while having substantial computational overhead. In this paper, we propose Obliviate, an efficient two-stage unlearning framework for recommender systems that achieves high unlearning completeness while maintaining good utility. In the first stage, we introduce a Low-Rank Unlearning Adapter (LUA), which employs a lightweight Hessian proxy to enable curvature-aware and efficient unlearning through localized low-rank adapters rather than full parameters. In the second stage, we propose Locality-Aware Calibration (LAC), a lightweight refinement stage that updates only the adapter parameters to improve the performance by enforcing unlearning via ranking-based objectives while preserving utility through knowledge distillation. Extensive empirical evaluations demonstrate that Obliviate achieves high level of forgetting with minimal loss in recommendation quality and at significantly reduced computational cost, offering a practical and scalable solution for large-scale recommender systems.

---


### 23. [Reinforcement Learning for Heterogeneous Sensor Selection in Maritime Surveillance](https://arxiv.org/abs/2607.22667)

**<font color=#1a73e8>作者：</font>** Andrei Starodubov, Yaqub Aris Prabowo, Andreas Hadjipieris 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This paper presents an information-gain-guided reinforcement-learning sensor-selection framework for single-vessel tracking in heterogeneous maritime sensor networks. The proposed approach is motivated by information-theoretic sensor management: instead of activating all sensors or repeatedly performing computationally expensive online expected-information-gain evaluation, a learned policy selects one tracking-relevant sensor at each decision epoch. A Bayesian sequential Monte Carlo tracker estimates the vessel state from noisy measurements and provides a belief representation for scheduling under nonlinear and non-Gaussian conditions. A Proximal Policy Optimization agent selects one of five sensors deployed in a georeferenced simulation of the CMMI Smart Marina testbed at Ayia Napa Marina, Cyprus. The agent observes belief-state, detection-history, coverage, sensor-geometry, and realized-information-gain features. The reward is defined as a realized-information-gain term gated by an observability mask. Final-test simulations compare the proposed framework with random single-sensor selection, always-on sensing using all sensors simultaneously, and the expected-information-gain sensor-selection baseline proposed in our previous work. Results show that the learned policy achieves tracking performance close to always-on sensing while activating only one sensor per decision time step and avoiding the computationally expensive online entropy search required by expected-information-gain selection.

---


### 24. [DOSA: A Tree-Guided, Self-Regressive Framework for Long Document Structure Analysis](https://arxiv.org/abs/2607.22679)

**<font color=#1a73e8>作者：</font>** Bohou Li, Benjamin Sowell, Mehul Shah 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In visually-rich documents, information is encoded not only in individual page objects such as tables, headers, and text blocks, but also in the structural relations among them, making document structure analysis fundamental to information retrieval and document understanding. However, accurately inferring such relations remains challenging in multi-page documents with long-range dependencies and heterogeneous layouts. To address this, we propose a tree-guided and self-regressive framework, termed DOcument Structure Analyzer (DOSA), for inferring relations among page objects and reconstructing document-level semantic trees. DOSA processes documents chunk-by-chunk, fusing visual, textual, and layout features for each page object and predicting hierarchical and ordering relations. The predicted relations are used to incrementally construct a semantic tree, which is then leveraged as structural context to guide inference on subsequent chunks. Experimental results on five benchmarks demonstrate the effectiveness of DOSA, with improvements of up to 4 F1 points and 19 TEDS points on DocHieNet, the most challenging multi-page hierarchy benchmark.

---


### 25. [A Vocabulary for Multi-Agent Automated Research Systems](https://arxiv.org/abs/2607.22682)

**<font color=#1a73e8>作者：</font>** Bardiya Akhbari  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce a vocabulary for automated research systems built from one or more agents to make their design choices easier to describe and compare. The vocabulary specifies 1) who the agents are, 2) what operations are available in the system, 3) who may invoke them, 4) how agents communicate, 5) what information is visible within and across runs, 6) how the next action is chosen, 7) how a run begins, and 8) how outputs are evaluated. A trajectory records one run from the input task to the returned artifact. Because agents, operations, and initialization may be stochastic, repeated runs on the same task induce a distribution over trajectories rather than a single behavior.
Our vocabulary turns structural design questions, such as when agents should communicate, gain or lose a capability, or carry information across runs, into testable choices. It also makes the evaluator a component of the system, since reported gains depend on how closely the proxy score matches true quality. That separation also splits the vague complaint that these systems lack taste into two failures with different solutions. Generative taste is the rate at which a system proposes novel trajectories before any score is observed, and evaluative taste is the gap between the proxy score and the quality it should match. We instantiate the vocabulary on recent autoresearch systems to illustrate that it covers designs that differ widely in structure.

---


### 26. [Imprompt: A Language Framework for Prompt Programming](https://arxiv.org/abs/2607.22683)

**<font color=#1a73e8>作者：</font>** Chentian Wu, Shengyuan Yang, Adithya Murali  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> With the unprecedented success of Language Models (LMs), the science of Prompt Engineering has evolved the powerful idea of Prompt Programming, where prompts are treated as a programmable control surface for describing complex tasks and leveraging LM capabilities. However, existing prompt programming frameworks suffer from various complexities and inelegances, which make them hard to utilize in practice for effectively describing tasks. We propose Imprompt, a new language framework for the study and practice of prompt programming. We undertake a foundational investigation of prompt programming, and contend that prompt programs must contain only the task descriptions and must be decoupled from lower-level 'execution' details. We further develop this position by illustrating structured prompting as a combination of prompt programming and prompt program 'compilation'. We exemplify this view by formally defining two compilers for Imprompt programs. We then explore the idea of typing for prompt programs and draw a correspondence between type checking and constrained decoding. Finally, we implement our compilers and type checkers and evaluate them on a variety of case studies. We believe our work contributes programming-language foundations toward the emerging area of prompt programming.

---


### 27. [DINOv3-MIL: Per-Kidney Multi-Label Tumour and Cyst Detection from Foundation-Model Patch Tokens on KiTS23](https://arxiv.org/abs/2607.22687)

**<font color=#1a73e8>作者：</font>** Vishalakshi M, Sahil Sharma, Pramod Kumar P  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Foundation vision models trained on natural images transfer to medical tasks without domain pre-training, but volumetric classification requires aggregating tens of thousands of patch tokens per study, and the aggregator constrains how the resulting model can be interpreted. We compare three aggregators on identical frozen DINOv3 ViT-H/16+ features for renal tumour/cyst detection on KiTS23 (966 kidneys; n=97 test): a CLS-token linear probe, gated attention multiple instance learning (MIL) over 55,296 patch tokens, and a prototype head following ProtoViT. Attention MIL achieves the highest AUROC for tumour (0.74, 95% CI 0.64-0.83) and cyst (0.80, 0.70-0.88), with attention enriched 7.5-9.8x over chance within annotated lesions. The prototype head does not transfer to cyst detection (AUROC 0.51), exposing an interpretability-performance trade-off at this token scale.

---


### 28. [Beyond Sequential Interaction: Benchmarking Parallel Execution and Coordination for GUI Agents](https://arxiv.org/abs/2607.22689)

**<font color=#1a73e8>作者：</font>** Zedong Yu, Qianxing Li, Zhi Gao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graphical user interface (GUI) agents are systems powered by large multimodal models (LMMs). They perceive screen state and execute user instructions through GUI actions such as clicking, typing, and scrolling on desktops and mobile devices. However, current agents scale poorly to long-horizon tasks: actions incur costly LMM inferences, and performance degrades as context grows. Humans divide such workloads among collaborators who complete sub-tasks in parallel. Yet parallel coordination among GUI agents has received little attention. To close this gap, we introduce ParaGUIBench, to our knowledge, the first benchmark dedicated to parallel execution and coordination of multiple GUI agents on separate desktop instances. It consists of three components: a multi-device Docker infrastructure with a shared file system; a dataset of 233 tasks spanning six task categories; and an evaluation system with efficiency metrics, including step reduction ratio and token cost. We further introduce ParaGUI, a planner-worker agent that decomposes GUI tasks and dispatches sub-tasks to concurrent workers on separate desktop instances. On ParaGUIBench, ParaGUI reaches a 46.4% success rate, outperforming the strongest serial baseline (Claude Sonnet 4.6) by 12.9 points while using roughly half the steps and less than half the tokens. These results show that parallel execution can improve both success rate and efficiency on decomposable, long-horizon GUI tasks, pointing to a direction worth further study.

---


### 29. [MegaSlide-DiT: Memory-Centric Adaptation and Deformable Local Attention for Efficient Video Diffusion](https://arxiv.org/abs/2607.22696)

**<font color=#1a73e8>作者：</font>** Jiacheng Liu, Jason Liu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> High-resolution video diffusion models built on Diffusion Transformers (DiTs) deliver strong fidelity but quickly exhaust the memory budget of a single workstation. A 100 billion-plus parameter DiT easily requires over a terabyte of persistent state, while naive spatiotemporal self-attention grows quadratically in sequence length. These two walls -- parameter memory and activation memory -- prevent researchers from adapting massive generative models without large GPU clusters. We revisit this problem from a systems perspective and introduce MegaSlide-DiT, a prototype that demonstrates how a pre-trained 105B DiT can be adapted on a single H200 GPU with 1.5 TB of host RAM. Our key insight is that the GPU need not own the model state: all persistent weights, master weights and optimizer moments remain in host memory, while only transient shards are streamed to the GPU on demand. Simultaneously, we replace quadratic global attention with 3D Deformable Slide Attention (3D-DSA), a motion-adaptive local attention operator that reduces both memory and computational complexity to linear in the sequence length. We report detailed memory accounting, execution traces and evaluation results to substantiate our design. MegaSlide-DiT does not claim to train a 105B model from scratch on a single GPU, nor does it magically solve bandwidth limits; rather, it offers a pragmatic path for full-parameter adaptation of massive video diffusion models on high-end workstations.

---


### 30. [FogDrive: A Multi-Modal Synthetic Driving Dataset for Perception under Graded Fog](https://arxiv.org/abs/2607.22698)

**<font color=#1a73e8>作者：</font>** Vansh Panwar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Perception under adverse weather remains a critical bottleneck for reliable autonomous driving, yet existing benchmarks lack the systematic multi-modal alignments needed to evaluate robust sensor fusion. Real-world weather datasets suffer from uncontrolled collection and single-level, uncalibrated conditions, while synthetic alternatives either target camera-only restoration or lack the paired clean-and-foggy structure needed to benchmark "defog-then-detect" pipelines. We present FogDrive, a rigorously calibrated, multi-modal autonomous-driving dataset bridging data-centric engineering and robust machine learning. Built with the CARLA simulator, FogDrive contains 660 scenes (~133k fully annotated frames, 50:50 day/night) across four synchronized cameras (RGB, depth, semantic segmentation), a LiDAR and semantic-LiDAR pair, and front radar. Physically consistent fog is modeled independently on camera channels (Koschmieder model) and LiDAR channels (Beer-Lambert law) at three calibrated visibility densities (160m, 100m, 50m). Every scene ships in four matched variants (clean plus three graded fog levels) with cross-calibrated 2D and 3D bounding boxes. A semantic-segmentation-based quality audit over 8k images validates annotations at 95.1% precision and over 99% recall for vehicles within 40m. We establish baseline benchmarks with state-of-the-art architectures (TransFusion, BEVFusion, YOLOv8-m) across two paradigms: 3D multi-modal fusion and 2D image restoration. These yield critical data-centric insights: mixing multi-density fog during training tightens 3D bounding-box geometry without added data-scaling cost, while in 2D pipelines image-quality metrics (PSNR, SSIM) prove poor predictors of downstream detection performance. FogDrive will be fully open-sourced alongside our data-generation framework to accelerate robust, multi-modal research.

---


### 31. [RoleMix: Unifying Sequential and Non-Sequential Features via Semantic Tokenization for Post-Click Conversion Rate Prediction](https://arxiv.org/abs/2607.22700)

**<font color=#1a73e8>作者：</font>** Wenan Wang, Qin Zhao, Zhixiang Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Post-click conversion rate (PCVR) prediction is central to industrial recommendation, but remains challenged by the structural mismatch between sparse, unordered multi-field features and long, domain-specific behavior histories. Existing models often process these signals through separate pathways and fuse them late, weakening semantic roles and limiting cross-signal refinement. We propose RoleMix, a unified interaction architecture that represents sequential and non-sequential evidence through a shared, role-preserving token interface. Non-sequential fields are converted into explicit semantic tokens that preserve user, item, pairwise, dense, contextual, and cross-feature roles, while long behavior domains are compressed into item- and context-aware sequence-query tokens through two-stage hierarchical window attention. The resulting global, semantic, and sequence-query tokens are jointly refined by stacked UniMixing-Lite blocks for PCVR prediction. On the large-scale KDD Cup 2026 Tencent UniRec Challenge, RoleMix achieves 83.648% online AUC, outperforming the official industrial baseline by 1.953%. Ablation studies show that semantic tokenization yields the largest isolated gain, highlighting a key principle for large-scale PCVR modeling: preserving field semantics at the token-interface level is as important as scaling the interaction backbone.

---


### 32. [Histopathological Spectrum-Guided Prostate Stratification via Segmentation-Assisted Diagnostic Transformer](https://arxiv.org/abs/2607.22703)

**<font color=#1a73e8>作者：</font>** Leyang Li, Lihua Chen, Huangang Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Prostate cancer diagnosis with multiparametric MRI (mpMRI) is commonly based on PI-RADS assessment or binary classification, which suffer from subjectivity and fail to capture clinically relevant pathological heterogeneity. To address this limitation, we construct a Prostate Cancer Histopathology Spectrum Dataset (PCa-HSD) and formulate a clinically meaningful four-class classification task, addressing the underrepresentation of benign lesions that are easily confounded with prostate cancer in existing datasets. We propose Language-guided Segmentation-assisted Diagnostic Transformer model (LSDT), which leverages zero-shot segmentation to provide anatomical priors and performs effective multi-modal slice fusion for classification. Our proposed method consistently improves accuracy across backbones, achieving the best average accuracy of 0.633 and JointRecall of 0.768 in five-fold cross-validation on a cohort of 344 patients. These results demonstrate that integrating pathology supervision and anatomical priors significantly enhances fine-grained prostate MRI classification and provides a more clinically relevant paradigm for risk stratification. Code will be made publicly available in a future revision.

---


### 33. [Visible-Light Imaging Diagnosis of Neutral Particle Emission Tomography in the Tokamak Divertor: An Efficient Transformer-based Surrogate Model](https://arxiv.org/abs/2607.22704)

**<font color=#1a73e8>作者：</font>** Xiao Wang, Hao Si, Qiang Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Nuclear fusion has made significant progress in recent years and is expected to become one of the most important pathways to addressing global energy challenges. This paper focuses on observing plasma using visible-light cameras, analyzing its spatio-temporal motion cues, and predicting the two-dimensional spatial distribution of light intensity, aiming to provide a foundational basis for future scientific experiments using deep neural networks. Specifically, we propose Delta-InvFormer, a novel backbone network centered on a differential Transformer. The key insight is that by taking consecutive video frames as input, we can better capture the dynamics of the plasma. Moreover, spatial and temporal differential self-attention effectively mitigates interference from noisy signals, ensuring high-quality feature extraction. These features are then fused into a compact and informative representation, which is fed into a decoder network to predict the distribution. Based on real experimental data collected from the Experimental Advanced Superconducting Tokamak (EAST) large-scale scientific facility, our results demonstrate that the proposed model not only significantly accelerates traditional methods for distribution prediction but also achieves competitive reconstruction accuracy. The source code of this paper will be released on this https URL

---


### 34. [EditCLEVR: A Paired-Scene Intervention Benchmark for Compositional Faithfulness of Object-Centric Representations](https://arxiv.org/abs/2607.22705)

**<font color=#1a73e8>作者：</font>** Anuraag Gadehothur Karnam, Tarunesh Sathish  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Object-centric learning aims to represent scenes as objects whose properties can be reused in new combinations. Existing evaluations usually score segmentation, single-image factor prediction, or downstream accuracy, but these tests do not directly ask whether a per-object representation behaves correctly under a controlled semantic edit. We introduce EditCLEVR, a paired-scene intervention benchmark in which each example contains a before/after pair of CLEVR-style renders with the same object indices and scene layout, and either exactly one known attribute change on one known object or a no-edit re-render for drift measurement. The protocol includes probe-free diagnostics for representation-change localization and stability, together with probe-decoded semantic faithfulness metrics that test whether the predicted scene change matches the intended intervention across in-distribution and compositional out-of-distribution (OOD) suites, allowing code-space movement and decoded object-attribute correctness to be evaluated separately. We introduce the semantic metric Scene-Graph Intervention Accuracy (SGIA), which requires the full after-scene prediction to be correct and the only predicted before-to-after semantic change to be the intended object-factor edit. We also establish Delta-SGIA as a companion diagnostic that checks the single-site change pattern without requiring the full after-scene graph to be correct. Baseline evaluations on ground-truth-mask backbones, learned-slot models, SAM 2 + frozen-ViT models, and one mask-feature hybrid indicate that CoGenT-OOD-core degradation can persist under ground-truth instance masks, that mask source accounts for part but not all of native performance, and that locality or stability alone can overstate semantic faithfulness. Code is available at this https URL.

---


### 35. [LowAux-RDNet: Low-Pass Residual Supervision with Scene-Balanced Real-World Training for Single-Image Reflection Removal](https://arxiv.org/abs/2607.22707)

**<font color=#1a73e8>作者：</font>** Jizhong Li  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Single-image reflection removal aims to recover a clean transmission layer from one image captured through glass. We study an explicit decomposition pipeline built on RDNet and introduce LowAux, a training-only low-pass reflection auxiliary objective. The original residual target remains the main reflection supervision, while symmetrically filtered prediction and target provide a stable low-frequency constraint. We further incorporate scene-balanced real pairs from RRW to broaden real-scene coverage and improve cross-dataset generalization. To avoid evaluation discrepancies caused by model-specific resizing, padding, output quantization, and metric code, we build a unified public benchmark over CEILNet, Real20, Postcard, Objects, and Wild. Under the same evaluator, the proposed system obtains a five-dataset macro average of 27.546 dB PSNR, 0.9220 SSIM, 0.9751 NCC, and 0.004760 LMSE, achieving the highest macro-average PSNR, SSIM, and NCC and the lowest LMSE among the compared public checkpoints and internal variants. Per-dataset and qualitative analyses show that the main benefit is a more balanced performance across diverse reflection distributions, while clear semantic reflections in Postcard remain challenging.

---


### 36. [SEGRA: Structured Experience-Guided Graph Reasoning Agent for Gremlin Based Question Answering](https://arxiv.org/abs/2607.22713)

**<font color=#1a73e8>作者：</font>** Saiyue Lyu, Mariam Dundua, Vishaal Kapoor 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise IT support knowledge graphs capture rich relationships among cases, users, devices, symptoms, taxonomic categories, root causes, and historical resolutions. Yet querying them in Gremlin requires knowledge of graph schemas, traversal semantics, edge directionality, and property-graph-specific constraints, making them difficult for non-expert operators to use. We introduce SEGRA, an experience-guided agent for enterprise text-to-Gremlin question answering. SEGRA integrates intent routing, schema- and taxonomy-grounded query generation, multi-shot decomposition, execution-aware verification, and a curriculum-bootstrapped skill library that reuses verified query patterns. On an enterprise IT support benchmark, SEGRA achieves a $7.0\times$ higher mean judge score than backbone-only chain-of-thought prompting. Its skill library further reduces LLM calls by $20\%$ and dollar cost by $18\%$ relative to SEGRA without skills, while preserving answer quality. These results show that schema-grounded agent design and reusable execution experience improve both accuracy and efficiency for enterprise graph QA.

---


### 37. [Real-Time Semantic Segmentation with Optimized RetinaNet Architectures for Embedded Automotive Systems](https://arxiv.org/abs/2607.22714)

**<font color=#1a73e8>作者：</font>** Sai Sidharth D  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-time perception is a foundational requirement for advanced driver assistance systems (ADAS) and autonomous vehicles, yet embedded automotive platforms impose severe constraints on compute, memory, and power. This paper presents an optimized semantic segmentation architecture derived from the RetinaNet detection framework, adapted for dense pixel-wise prediction and tailored for deployment on resource-constrained embedded hardware. The proposed architecture, termed Opt-RetinaSeg, replaces the standard ResNet-50 backbone with a hybrid lightweight feature extractor, restructures the Feature Pyramid Network (FPN) to reduce redundant multi-scale computation, and introduces a compact segmentation head guided by focal-loss-inspired class balancing to address the severe foreground-background imbalance common in road scenes. We further apply a three-stage optimization pipeline consisting of structured channel pruning, post-training INT8 quantization, and knowledge distillation from a high-capacity teacher network. Evaluated on the Cityscapes and BDD100K datasets and deployed on an NVIDIA Jetson Xavier NX and a Qualcomm QCS610 automotive SoC, the proposed model achieves 73.9% mIoU at 70.4 FPS, representing a 7.4x inference speedup and a 4x reduction in model size relative to the ResNet-50 baseline, with less than 3% accuracy degradation. These results indicate that RetinaNet-derived architectures, when systematically optimized, are viable candidates for real-time semantic segmentation in embedded automotive perception pipelines

---


### 38. [Child-Oriented AIGC Video Risk Reviewing: A Benchmark and Knowledge-Supported Iterative Reasoning Framework](https://arxiv.org/abs/2607.22715)

**<font color=#1a73e8>作者：</font>** Lewen Mi, Manyi Li, Yuling Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The rapid growth of Artificial Intelligence-generated content (AIGC) is reshaping video production and circulation, exposing children to an increasing volume of AIGC videos. Unlike traditionally produced videos, AIGC videos often exhibit greater uncertainty in visual details, narrative coherence, and content expression, which may introduce developmentally inappropriate risks for children. However, existing video safety research is largely designed for general violation detection from an adult perspective and remains insufficient for identifying the fine-grained, implicit, and context-dependent risks that children may encounter when viewing AIGC videos. To address this gap, we study child-oriented AIGC video reviewing, making three contributions. First, we construct CAVSR, a benchmark of 605 real-world videos collected from multiple platforms, and develop a hierarchical risk taxonomy comprising 6 top-level categories and 26 fine-grained labels to support systematic evaluation of children's viewing risks. Second, we propose QVRS-E, a knowledge- and experience-augmented video reviewing framework that combines multi-agent collaboration with expert and experiential knowledge to support targeted evidence acquisition and fact-grounded reviewing decisions. Third, extensive experiments demonstrate that our method significantly enhances the reviewing of child-related risks integrated with vision-language models, and yields more robust review reports.

---


### 39. [TOM-GS: Editable Video Representation via Temporal Opacity Modulation of Static 3D Gaussians](https://arxiv.org/abs/2607.22717)

**<font color=#1a73e8>作者：</font>** Marek Lisowski, Łukasz Smoliński, Kornel Howil 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Implicit Neural Representations (INRs) and dynamic 3D Gaussian Splatting (3DGS) achieve impressive results in video processing, they often fall short of producing representations that are easily editable. Recent methods address this by introducing complex spatial deformations or folded distributions, which constrain optimization and reduce flexibility for downstream editing. In this paper, we introduce TOM-GS, an editable video representation that forgoes complex deformations in favor of regular 3D Gaussians equipped with a continuous temporal opacity formulation. By assigning a learnable temporal mean and scale to the opacity of each Gaussian, our model enables static 3D spatial components to fade smoothly in and out of the scene. Grounded by robust, off-the-shelf pose estimation, our approach maintains a static spatial geometry that naturally supports a wide range of manual and physics-based edits. TOM-GS outperforms prior editable video representations in visual fidelity, while its reliance on standard 3D Gaussians ensures seamless compatibility with established 3D editing tools.

---


### 40. [DAMamba-UNet3D: A Parameter-Efficient Mamba State Space U-Net with Dynamic Adaptive Scan for 3D Medical Image Segmentation](https://arxiv.org/abs/2607.22718)

**<font color=#1a73e8>作者：</font>** Mohammad Arafat Hussain, Ellen Grant, Yangming Ou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We propose parameter-efficient SSM-based U-Net architectures for 3D medical image segmentation. Convolutional U-Nets afford O(n) local mixing per layer but lack explicit global context; transformers provide global reasoning at O(n^2) cost in sequence length $n$. State-space models (SSMs), such as Mamba, offer $O(n)$ global propagation per block. Yet, existing medical SSM segmenters rely on fixed scan patterns and large parameter budgets. Dynamic Adaptive Scan (DAS), which learns data-dependent reordering before selective scan, has not been applied to medical imaging or extended to 3D volumes. We propose DAMamba-UNet3D, a hybrid encoder-decoder that integrates tri-plane 3D-DAS blocks at encoder stages E2-E4 while retaining convolutions elsewhere (~5.3M parameters). On BraTS 2020 five-fold cross-validation, DAMamba-UNet3D achieves mean Dice 0.815+/-0.013 (full-volume per-case evaluation) at ~13x lower parameter cost than SegMamba (0.824+\-0.014, ~70M). At comparable scale, DAMamba-L (~70M), a wide DAS-native variant with encoder-only DAMamba and a convolutional bottleneck, reaches 0.829+\-0.012, surpassing retrained SegMamba by 0.5pt. Component ablations show that encoder-only DAS placement is critical as bottleneck and decoder SSM blocks lower Dice. Together, the results suggest that learned tri-plane DAS in a hybrid U-Net is competitive with, and under our large-scale design may improve upon, SegMamba's fixed Tri-orientated Mamba (ToM) scanning on BraTS 2020. Code: this https URL.

---


### 41. [$γ$-Bridge: A Look-Parametric Diffusion Bridge](https://arxiv.org/abs/2607.22719)

**<font color=#1a73e8>作者：</font>** Xuran Hu, Yujie Zhu, Tengxi Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multiplicative Gamma noise is a signal-dependent degradation in coherent imaging; synthetic aperture radar (SAR) despeckling is its most prominent real-world instance. Existing diffusion denoisers parameterize their forward process by abstract signal-to-noise schedules rather than by the physical look number $L$, so different deployment scenarios typically require separately trained models, and transfer from synthetic Gamma training to real SAR remains challenging without clean ground truth. We introduce $\gamma$-Bridge, a look-parametric bridge whose schedule $L(t)$ connects the noisy observation at $L_{obs}$ to the clean limit through exact multiplicative Gamma marginals. Its closed-form Gamma--Lévy reverse posterior admits both stochastic and deterministic processes, while observation conditioning and a two-step consistency loss stabilize multi-step inference in the low-SNR single-look regime. Because bridge time directly represents $L$, one conditioned network can smart-start from any admissible input look and stop at a target look number. These two orthogonal controls enable zero-shot restoration over the full admissible grid after training only at $L_{obs} = 1$ on natural images with synthetic Gamma corruption. Combined with a homogeneous-patch look estimator, $\gamma$-Bridge processes data from six spaceborne and airborne SAR sensors without sensor-specific fine-tuning, achieving leading results on standard synthetic benchmarks while providing physically interpretable input and output controls absent from prior denoisers. Codes are released \href{this https URL}{here}.

---


### 42. [An Interactive Vision Language Platform for Cognitive Remediation in Schizophrenia](https://arxiv.org/abs/2607.22721)

**<font color=#1a73e8>作者：</font>** Nassira Ait Mehdi, Milissa Temmam, Slimane Larabi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cognitive remediation tasks often require patients to perform structured actions involving object manipulation and sequential reasoning. For patients diagnosed with schizophrenia, these tasks are crucial for addressing severe cognitive deficits. However, evaluating the correctness of these physical actions generally relies on manual observation by clinicians, which introduces subjectivity and limits the scalability of therapeutic interventions. In this paper, we propose an automated framework based on Vision-Language Models for action verification in cognitive remediation tasks tailored for schizophrenia rehabilitation. The proposed system relies on a camera-monitored tabletop environment composed of structured miniature scenes including roads, a roundabout, a park, and toy vehicles. Patients receive audio instructions describing goal-oriented spatial actions to perform by manipulating a toy vehicle. These interactive physical activities are specifically designed to stimulate targeted cognitive functions, such as sustained attention, motor coordination, spatial navigation, and cognitive flexibility. To verify the correctness of the performed actions without requiring continuous clinical oversight, the system analyzes the video feed tracking the patient's hand and toy movements. A fine-tuned Vision-Language Model interprets the recorded video sequences and generates semantic descriptions of the observed activities, enabling high-level verification of the executed actions with respect to the initial textual instructions. A dedicated dataset of 4634 tabletop cognitive remediation video scenarios was collected to evaluate the proposed approach. Experimental results demonstrate that our specialized framework effectively bridges low-level physical telemetry with high-level clinical feedback, presenting a scalable and objective solution for advanced cognitive rehabilitation.

---


### 43. [A New Kind of Adversarial Example: Measuring the Human-Model Gap, and Its Relationship to OOD Detection](https://arxiv.org/abs/2607.22722)

**<font color=#1a73e8>作者：</font>** Ali Borji  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Almost all adversarial attacks add an imperceptible perturbation to fool a model. We instead study the opposite: a large, clearly visible perturbation that causes the model to keep its original, correct prediction, even though a human would no longer recognize the image. Prior work showed such examples can be generated at scale but left three questions untested: whether humans really perform worse than the model, whether standard out-of-distribution (OOD) detection and calibration tools catch it, and whether existing defenses mitigate it. We answer all three on MNIST, CIFAR-10, and ImageNet. (i) An independent recognizer proxy drops to ~49% on CIFAR-10 while the model stays at 100% -- a gap a small human pilot (N=5) corroborates directly and that is not explained by signal loss (a matched-magnitude Gaussian control degrades recognizability faster); a CLIP zero-shot proxy confirms the gap at ImageNet scale too. (ii) Confidence- and energy-based OOD detectors and calibration are structurally blind (0% detection, ECE ~= 0), while a feature-space Mahalanobis detector flags 100% -- but is evaded by an adaptive attacker at no cost to success. (iii) No classical defense, including adversarial training (45% robust accuracy), reduces attack success (correlation with large-epsilon_l resistance r ~= 0). A mechanistic analysis further shows the attack destroys low-level texture far faster than edge/shape structure.

---


### 44. [Structural Preservation Governs Data Augmentation in Deep Learning-Based Laser Speckle Material Classification](https://arxiv.org/abs/2607.22725)

**<font color=#1a73e8>作者：</font>** Mohamed Abdallah Salem, Nourhan Zein Diab  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Data augmentation is routinely used to improve generalization in image classification, but the assumptions underlying standard policies are poorly matched to coherent imaging. Laser speckle patterns are not generic textures; they arise from coherent interference, and their discriminative content is carried by structured stochastic spatial and frequency statistics. This study examines how controlled augmentation perturbations influence speckle-based material classification on the SensiCut dataset. We train ResNet18 and EfficientNet-B0 under a parametric augmentation framework comprising rotation, Gaussian blur, independent Gaussian noise, spatially correlated speckle-aware noise, intensity jitter, and spatial masking, and evaluate test performance using macro F1-score averaged over three random seeds. Separate ordinary least squares models link augmentation parameters to performance for each architecture. Across both models, Gaussian blur exerts a strong negative effect (p < 0.001), indicating that low-pass filtering suppresses high-frequency structure that is informative for material discrimination. Independent pixel-wise noise is likewise harmful (p = 0.003 for EfficientNet-B0 and p = 0.001 for ResNet18), consistent with disruption of local spatial coherence. In contrast, spatially correlated perturbations yield significant positive coefficients (p = 0.004 for EfficientNet-B0 and p = 0.001 for ResNet18), showing that variability can improve robustness when it preserves speckle organization. The fitted models explain a substantial fraction of performance variation (R2 = 0.796 for EfficientNet-B0 and R2 = 0.879 for ResNet18). These results show that, in laser speckle imaging, augmentation effectiveness is determined primarily by structural preservation rather than perturbation magnitude. The findings motivate physics-aware augmentation design for coherent optical sensing.

---


### 45. [Trustworthy Medical Segmentation: Uncertainty-Aware U-Net Evaluation Under Clinical Image Degradation](https://arxiv.org/abs/2607.22727)

**<font color=#1a73e8>作者：</font>** Pranav Kaliaperumal, Manisha Kaliaperumal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation models often report high benchmark accuracy under ideal imaging conditions, yet their failures under clinical degradation can be quiet: sensor noise, patient motion, low- resolution acquisition, and contrast variability may all alter model behavior without producing an obvious warning. We present a reproducible framework for evaluating uncertainty-aware segmentation under con- trolled clinical degradation. Our experiments use a synthetic multimodal brain tumor MRI cohort generated with a biophysical phantom simulator that follows the BraTS protocol. We train U-Net and Attention U-Net baselines for multi-class tumor sub-region segmentation and augment both models with Monte Carlo dropout to estimate per-voxel uncertainty. Across eight clinically motivated corruption types at five severity levels, we measure segmentation accuracy, calibration, failure detection, and selective prediction coverage. On clean data, Attention U-Net achieves a whole-tumor Dice of 0.990; under severe Gaussian noise, its performance falls to 0.089. Predictive uncertainty rises with degradation and tracks segmentation error (Pearson r = 0.53 under severity-3 Gaussian noise), allowing us to flag failures with an AUROC of 0.843. These results argue for uncertainty-aware inference as a practical safety layer in physician-in-the-loop radiology workflows. We release the code, trained models, and evaluation protocol to support direct reproduction.

---


### 46. [CrossSpine: Multi-scale Cross-sequence Attention with Anatomical Priors for Automated Pfirrmann Grading](https://arxiv.org/abs/2607.22728)

**<font color=#1a73e8>作者：</font>** Hai Son Nguyen, Duong Ngoc Vu, Trong-Nghia Nguyen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Automated grading of Lumbar Disc Degeneration is essential for the objective quantification of structural changes associated with low back pain. Observing that baseline models underperformed on our data, we propose a framework designed to overcome these limitations. First, we present the Cross-sequence Attention Spine (CrossSpine) framework, a novel architecture that employs a cross-sequence attention mechanism to adaptively fuse features from different MRI sequences at multiple spa- tial scales. Second, we contribute a meticulously curated dataset aimed at automated Pfirrmann grading. Finally, we introduce an IVD-aware classification technique that integrates anatomical disc-level information, enabling the model to learn level-specific degeneration priors. Our experi- ments demonstrate the superiority of this approach: CrossSpine achieved a relative improvement exceeding 125% in the Macro F1 score, while boosting the Mean AUPRC by 99% and the Mean AUROC by 36% com- pared to the baseline.

---


### 47. [Calibration-Free 3D Multi-Camera People Tracking for Indoor Environment](https://arxiv.org/abs/2607.22731)

**<font color=#1a73e8>作者：</font>** Ponleur Veng, Dominique Vaufreydaz, Phutphalla Kong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-Camera People Tracking (MCPT) traditionally relies on precise intrinsic and extrinsic camera calibration to project 2D detections into a unified 3D world coordinate this http URL, manual calibration constitutes a major bottleneck in large-scale dataset generation from unconstrained video archives.  This work proposes a unified calibration-free 3D MCPT framework that infers geometric structure directly from visual data using deep foundation models.  The system integrates anchor-free detection (YOLOX), robust tracking (BoT-SORT), omni-scale appearance embedding (OsNet), pose estimation (HRNet via MMPose), and transformer-based geometric reconstruction using the Visual Geometry Grounded Transformer (VGGT). A pose-guided 3D lifting strategy projects head keypoints onto a reconstructed manifold, eliminating dependence on ground-plane homography. Global identity association is formulated as hierarchical agglomerative clustering under a joint appearance-geometry cost with strict velocity gating. Evaluation on the AI City Challenge 2024 demonstrates a HOTA score of 53.13% without access to ground-truth calibration matrices, establishing a strong baseline for purely vision-based 3D tracking.

---


### 48. [Generative Augmentation for EEG Motor Imagery Classification: A Class-Conditional VAE with Cycle-Consistent Decoder Refinement](https://arxiv.org/abs/2607.22733)

**<font color=#1a73e8>作者：</font>** Matei Moldoveanu, Alain Sirois, Claire Ben Ali 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We investigate whether a generative model can supply useful synthetic motor-imagery (MI) electroencephalography (EEG) trials that improve the accuracy of independent downstream classifiers. We train a class-conditional variational autoencoder (CVAE) with an integrated latent classifier on the Zhou motor-imagery dataset, using the learned per-class prior as a generator: sampling the prior for a given label and decoding it into a synthetic, label-consistent signal. A constraint on the covariance matrix of the generated data encourages preservation of covariance structure, and the model is trained with a schedule that alternates ordinary VAE training with a decoder-focused phase that sharpens the generative pathway used for augmentation. We measure the effect of adding synthetic trials to the training set under two evaluation protocols -- within-user (pooled 60/20/20 split across subjects) and cross-user (leave-one-subject-out, LOSO) -- across four representative EEG classification pipelines: Common Spatial Patterns with Linear Discriminant Analysis (CSP+LDA), tangent-space features with a Support Vector Machine (TGSP+SVM), Minimum Distance to Riemannian Mean (MDM), and a neural network based on EEGNetv4 (henceforth EEGNet). Results are aggregated across independent augmentation draws, random seeds (within-user), or leave-one-subject-out folds (cross-user), with uncertainty reported as 95\% confidence intervals (Student's $t$-distribution) computed over per-seed/per-fold averages. We find that synthetic EEG from the CVAE is most credible as a source of class-structured, covariance-like data rather than as a substitute for real raw EEG: it can raise the point estimate for MDM, but the broader augmentation claim remains conservative -- observed gains are small and classifier-dependent.

---


### 49. [Fast Fourier Convolutional GAN for 30 m Clear-Sky Land Surface Temperature Gap-Free Reconstruction](https://arxiv.org/abs/2607.22734)

**<font color=#1a73e8>作者：</font>** Marwa Alfouly, Smajil Halilovic, Nils Bochow 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Satellite-derived Land Surface Temperature (LST) provides spatially comprehensive data that ground stations cannot match. However, its utility is frequently limited by severe data gaps due to the presence of clouds. As LST is essential for understanding land-atmosphere interactions, numerous methods have been proposed to address this challenge. Yet, the development of a scalable and adaptable pipeline for generating gap-free LST datasets and reconstructing cloud-contaminated pixels remains challenging. Moreover, the reconstruction of extensive missing regions in fine-spatial-resolution observations is particularly difficult. To address this challenge, we propose a Multimodal Fast Fourier Convolutional GAN for reconstructing cloud-contaminated pixels in fine-resolution (30 m) Landsat imagery to generate gap-free clear-sky LST products. The method leverages Fast Fourier Convolution to enable a global receptive field across the image, and is guided by a stack of data consisting of satellite observations and Synthetic Aperture Radar (SAR) data. Across all LST quantiles, the interquartile range of scene-averaged RMSE (computed over reconstructed pixels) is consistently between 0.8 K and 1.8 K. The proposed approach enables the recovery of extensive missing regions, including scenes with more than 70% cloud-induced gaps, while relying on auxiliary data that are readily available at a near-global scale.

---


### 50. [Benchmarking the Domain Gap: Model Selection Instability Under Domain Shift in Video Capsule Endoscopy](https://arxiv.org/abs/2607.22736)

**<font color=#1a73e8>作者：</font>** Dan Hanson, Debesh Jha  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video capsule endoscopy (VCE) classification is typically evaluated within a single dataset, yet clinical deployment demands robustness across acquisition sources, labeling policies, and patient populations. We examine this gap using Kvasir-Capsule, Capsule Vision 2024 (CV2024), and a shared-label subset of Galar. We fine-tune a suite of general-domain pretrained backbones on the official Kvasir-Capsule folds under a standardized protocol and evaluate the same checkpoints on two non-source targets within a documented shared-label decision space. We find that the predictive value of in-domain ranking is target-dependent: Kvasir-Capsule ranking aligns more closely with Galar than with CV2024, while the two non-source targets agree only weakly. Consequently, the strongest in-domain backbone leads on one target yet falls to mid-pack on the other, and no single evaluation target reliably predicts the others. A second CV2024-trained configuration set reproduces this target-dependent instability. We conclude that capsule endoscopy model selection should report cross-target ranking stability rather than peak single-dataset performance.

---


> [!TIP]
> 当前位于：**1-50**（第 1/9 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-442](./part-09.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
