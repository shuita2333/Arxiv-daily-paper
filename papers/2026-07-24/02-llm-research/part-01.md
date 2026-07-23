# 🧠 大模型相关研究 | 2026年07月24日

> 本类共 **92** 篇论文

> 聚焦 LLM / MLLM / Agent / MoE 等大模型核心研究。

> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-92](./part-02.md)

---

### 1. [FineServe: A Fine-Grained Dataset and Characterization of Global LLM Serving Workloads](https://arxiv.org/abs/2607.19349)

**<font color=#1a73e8>作者：</font>** Tiancheng Zhang, Shaoyuan Huang, Mingyuan Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as always-on online services, making efficient LLM serving a critical systems challenge. Achieving low latency and high throughput under volatile demand requires deep understanding of real-world serving workloads, yet existing studies often rely on proxy traces or coarse-grained characterizations that fail to capture the heterogeneity of modern multi-model LLM platforms. We present FineServe, an in-the-wild, multi-model LLM serving workload dataset collected from a global commercial marketplace, enabling fine-grained characterization of real-world serving dynamics across heterogeneous models and tasks. Leveraging FineServe, we conduct a comprehensive analysis of arrival dynamics and token behavior, revealing fundamentally different fluctuation regimes across model architectures, scales and task intents. Building on these insights, we develop the FineServe workload generator, which composes fine-grained model-aware workloads into configurable mixtures tailored for benchmarking multi-model serving platforms. By exposing these fine-grained workload dynamics, FineServe provides a realistic foundation for evaluating routing, scheduling, and capacity-planning strategies in LLM serving systems. FineServe is available at this https URL.

---


### 2. [Benchmarking Confidential GPU Inference on NVIDIA H100 under Intel TDX](https://arxiv.org/abs/2607.19353)

**<font color=#1a73e8>作者：</font>** Wei Wang, Abdul Hyee Waqas, Burns Smith  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Confidential computing is becoming a practical deployment requirement for AI inference workloads that process sensitive inputs or protect proprietary model assets. However, the performance cost of enabling confidential execution for GPU-accelerated large language model serving remains workload dependent and operationally important. This paper presents a benchmark study comparing standard non-confidential execution with confidential computing mode on a single NVIDIA H100 80GB GPU hosted in an Intel TDX confidential instance. The evaluation uses two representative language models, Mistral-7B v0.1 and Qwen3-30B-A3B, and measures time to first token, end-to-end request latency, per-request token generation throughput, global token throughput, and closed-loop request throughput under increasing concurrency. In fixed request-rate experiments, confidential mode increases average TTFT by 21.8% for Mistral-7B and 27.8% for Qwen3-30B-A3B, while global token throughput drops by 17.7% and 21.1%, respectively. In closed-loop concurrency experiments, throughput gaps remain in the 11.5-20.2% range, but the larger model reaches its saturation knee earlier under confidential mode. The results suggest that confidential GPU inference can retain usable throughput under load, but capacity planning must account for both the steady throughput penalty and the earlier saturation behavior observed for larger models.

---


### 3. [FormulaSPIN: Self-Play Fine-Tuning for Natural Language to Spreadsheet Formula Generation](https://arxiv.org/abs/2607.19354)

**<font color=#1a73e8>作者：</font>** Cy Xie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Spreadsheet applications are used by hundreds of millions worldwide, yet writing formulas remains a significant barrier. Existing approaches rely on static supervised data, which quickly saturates on limited annotations. In this paper, we introduce FORMULASPIN, a self-play framework that breaks the ceiling of supervised fine-tuning by enabling iterative self-improvement without any additional data. Vanilla SPIN fails on this task: it uniformly penalizes every non-matching output, so execution-equivalent alternatives are punished as negatives in one example while serving as ground truth in another, producing contradictory gradients. Our framework resolves this by exploiting formula generation's unique advantage: binary executability provides implicit supervision that separates semantic errors from valid stylistic variants. We frame training as a two-player game in which the main player learns to prefer ground-truth formulas over those from its previous version, while execution feedback sorts outputs into distinct granularities-enabling an adaptive curriculum that shifts from semantic correctness to stylistic refinement. To further increase accuracy, we incorporate ExecVote, a semantic-level voting mechanism that naturally handles multiple valid formulations. Experiments on multiple benchmarks demonstrate that FORMULASPIN achieves state-of-the-art performance, with 74.9% exact match and 87.1% execution accuracy on NL2FORMULA, matching models trained with additional preference annotations while outperforming both traditional SFT and frontier proprietary models. These findings underscore self-play's potential to tackle scarce data tasks and open the door to extending it beyond executable domains.

---


### 4. [Information Discernment in Large Language Models](https://arxiv.org/abs/2607.19355)

**<font color=#1a73e8>作者：</font>** Joshua Ashkinaze, Laura Kurek, Alina Faisal 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used with external knowledge sources like the internet. Do they weigh information appropriately -- updating more for reliable sources (source discernment) and more when claims bring priors closer to the truth (truth discernment)? We formalize this as information discernment and introduce Learn2Discern (L2D), an experimental framework and benchmark grounded in three normative axioms with interpretable metrics. To establish external validity, a pre-registered, quota-matched user study (n=299) confirms that real LLM users endorse all three axioms and report that violations reduce their trust and usage intent. Across 13 models and nearly 670K trials, we find consistent failures across both dimensions: models perform near chance on source and truth discernment, rely on source popularity twice as much as source reliability, and update roughly equally whether a claim improves or worsens their position relative to the ground truth. Models integrate external knowledge most effectively on datasets where their priors are already the most accurate. Newer and larger models improve truth discernment but not source discernment, a blind spot that model complexity does not address. We identify simple inference-time interventions that improve both forms of discernment. We release our dataset and survey as a testbed for a core alignment property that scales in importance as LLMs replace traditional search.

---


### 5. [NEXUS: Structured Runtime Safety for Tool-Using LLM Agents](https://arxiv.org/abs/2607.19356)

**<font color=#1a73e8>作者：</font>** Elias Hossain, Md Mehedi Hasan Nipu, Tasfia Nuzhat Ornee 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using LLM agents increasingly execute high-impact actions, making runtime safety monitoring essential. We present NEXUS (Neural EXecution Utility and Safety), a structured-plan safety monitor that applies a formal intervention policy to select among four actions: allow, block, request confirmation, or request revision. NEXUS combines deterministic safety rules, argument-level inspection, and a calibrated logistic-regression risk score for graded escalation. On a 128-instance synthetic benchmark, NEXUS achieves an F1 score of 0.949 and a 4-class intervention accuracy of 0.6406, outperforming rule-only intervention selection by 27.3 percentage points. It also improves over rule-only on R-Judge (F1 = 0.861 vs. 0.849), matches rule-only on AgentHarm due to threat-model limits, and achieves 0% ASR at 99% control allow on IPI. On the rule-blind NEXUS-Stress benchmark, NEXUS reaches an F1 score of 0.881, highlighting the difficulty of fine-grained intervention routing. With 0.205 ms median latency, NEXUS adds under 0.1% overhead to typical agent loops. Code, benchmarks, and the calibrated risk scorer are publicly released.

---


### 6. [LISA: Linear-Indexed Sparse Attention for Efficient Long-Context Reasoning](https://arxiv.org/abs/2607.19358)

**<font color=#1a73e8>作者：</font>** Yu Zhao, Zekun Zhang, Fan Jiang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in long chain-of-thought reasoning models such as DeepSeek-R1 have led to increasingly longer inference context lengths under the test-time scaling paradigm. However, the O(n^2) computational complexity of standard self-attention causes inference costs to grow sharply with long sequences, limiting the deployment of long-CoT reasoning in production settings. To address this, we propose LISA (Linear-Indexed Sparse Attention), a plug-and-play attention replacement module that requires no pretraining from scratch. LISA integrates two lightweight components in parallel within the original model: (1) a Linear Attention module that provides long-range memory with O(n) time complexity; (2) a Lightning Indexer that selects the top-M important tokens from the full context to feed into a Sparse Self-Attention. The two branches are fused via a gating mechanism, reducing inference complexity from O(n^2) to O(nM) (M << n) for generating n tokens. We design a two-stage training pipeline: Stage 1 initializes the model by integrating the linear attention to capture long-range dependencies, complemented by a sliding-window attention mechanism that is optimized via knowledge distillation to approximate the full self-attention distribution of a frozen teacher model. In Stage 2, we further introduce the Indexer to replace the static sliding-window mechanism, enabling dynamic token selection from broader contexts. The Indexer is trained using a novel per-head KL divergence loss, which aligns its selection behavior with the attention patterns of the teacher model. Experiments on DeepSeek-distilled-Qwen models demonstrate that LISA achieves a 50% inference speedup under 16K-token context, while improving average performance by 5.6% on reasoning benchmarks including AIME and MATH-500.

---


### 7. [Profile-Graph Memory for LLM Agents: Implicit Cross-Entity Traversal through Narrative Profiles](https://arxiv.org/abs/2607.19359)

**<font color=#1a73e8>作者：</font>** Shengtong Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-term memory is essential for LLM agents that interact across sessions, yet current memory benchmarks primarily evaluate single-hop recall, leaving multi-hop association largely unmeasured. We make three contributions. First, we introduce MemHop, a multi-hop memory benchmark of 1,000 questions at hop depths 1-5 across 10 social-network scenarios, with per-hop evidence annotations. Second, we present Profile-Graph Memory (ProGraph), a two-layer memory architecture combining (i) profile expansion -- substring-matched traversal of entity names that naturally appear in LLM-written profile narratives, a minimal alternative to explicit knowledge-graph construction -- and (ii) compression residuals -- exact dates, quantities, and named items co-extracted with each profile update at zero extra API cost. Third, a full-grid ablation shows cross-benchmark mechanism specialization: profile expansion drives multi-hop reasoning (-22.6pp on MemHop when removed) while compression residuals drive precision recall (-8.6pp on LoCoMo when not co-extracted), with cross-effects under 3pp within a single architecture. ProGraph averages 80.1% on MemHop (matching the FullContext reference) and 78.4% on LoCoMo (exceeding FullContext by 11.3pp), outperforming Mem0, A-Mem, HippoRAG, and RAG on both. We release MemHop, ProGraph, and baseline implementations.

---


### 8. [Lifted Representation Hypothesis in Language Models](https://arxiv.org/abs/2607.19360)

**<font color=#1a73e8>作者：</font>** Bumjin Park, Jaesik Choi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often answer queries by mapping individual observations to more general rule-like structures. However, it remains unclear how these structures are stored, selected, and revised. To study this process, we propose thelifted representation hypothesis: LLMs update memory through shared latent structures rather than isolated instance-level facts. This view frames lifting as an efficient use of symmetry across instances, and shattering as the refinement of coarse lifted structures into more specific subtypes. We evaluate LLMs' lifting and shattering through controlled exception-learning experiments across in-context learning, LoRA, and full fine-tuning. We find that LLMs are vulnerable to shattering failures when data are governed by nested rules and exceptions, while lifting often occurs prematurely. These results highlight the need to study the relation between data and rule structures in LLMs.

---


### 9. [Stateful Guardrails for Multi-Turn LLM Systems: A Conversational Risk Accumulation Framework](https://arxiv.org/abs/2607.19361)

**<font color=#1a73e8>作者：</font>** Sanjay Mishra, Divya Chukkapalli, Ganesh R. Naik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Most safety guardrails for large language models (LLMs) evaluate each prompt-response pair in isolation, which misses failures that arise only over a dialogue as benign turns compose into harm. We term this Conversational Risk Accumulation (CRA): gradual intent drift, fragmented assembly of prohibited instructions, and sensitivity build-up from repeated disclosures. We propose a session-layer CRA Framework that tracks three trajectory signals: semantic drift from a session anchor, a sensitivity-weighted information accumulation graph over extracted entities, and a compliance-gradient signal capturing increasing willingness to comply. For scoring, we provide (i) an unsupervised convex fusion for attribution and ablations, and (ii) CRA-Net DA, a compact learned trajectory model trained with family-adversarial objectives to reduce length and topic-coverage confounds. To benchmark CRA, we release CRA-Bench v0.1 (1,200 eight-turn sessions across three threat families with topic-matched benign twins), CRA-Bench v0.2 (LLM-paraphrased variants to reduce template artifacts), and an extended 5-family set (2,000 sessions adding persona priming and context stuffing). We introduce a trajectory-native evaluation protocol with session-level splits, mixed-set threshold calibration, Trajectory AUROC, turns-to-detection, calibrated false-positive metrics, bootstrap confidence intervals, leave-one-family-out diagnostic stress tests, and synthetic-to-human transfer checks. Claims focus on within-distribution session scoring on CRA-Bench and human-transfer subsets.

---


### 10. [GraphContainer: A Unified Platform for Comparing and Debugging Graph RAG Methods](https://arxiv.org/abs/2607.19362)

**<font color=#1a73e8>作者：</font>** Seonho An, Chaejeong Hyun, Min-Soo Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Graph RAG mitigates hallucinations and stale knowledge in LLMs, particularly for multi-hop question answering. However, existing approaches remain highly fragmented and incompatible. The structural heterogeneity of graph formats across different frameworks and the lack of granular visualization tools make it exceedingly difficult to evaluate and compare retrieval behaviors. To bridge this gap, we propose GraphContainer, a novel platform designed to unify and visualize diverse graph RAG workflows. GraphContainer features two key components: (1) a Unified Graph Representation (UGR) layer that seamlessly standardizes multi-format graphs, and (2) a Graph Recorder that tracks and visually renders the step-by-step retrieval process. Through an interactive web interface, we demonstrate GraphContainer's ability to import heterogeneous graphs and perform live, traceable visual debugging of graph RAG methods. Ultimately, we show how GraphContainer enables controlled comparisons of various graph formats and retrieval strategies, lowering the barrier for researchers and practitioners to design optimal graph RAG pipelines. A demonstration video is available at this https URL.

---


### 11. [Statistically Grounded Sparse-Feature Interventions for Activation-Space Control in Large Language Models](https://arxiv.org/abs/2607.19364)

**<font color=#1a73e8>作者：</font>** Oshayer Siddique, J. M Areeb Uzair Alam, Md Jobayer Rahman Rafy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Activation steering offers a lightweight alternative to fine-tuning for behavioral control of large language models, but SAE-based steering methods often rely on learned steering objectives or single-criterion feature selection. We introduce a transparent SAE-feature steering pipeline that first applies a six-condition reliability filter, then ranks sparse features through an unweighted Borda consensus over three complementary statistics: $F$-test, KSG mutual information, and Cohen's $d$. The resulting steering direction is constructed as a Cohen's-$d$-weighted combination of SAE decoder rows, providing an optimization-free direction motivated by Fisher-LDA under approximate SAE-feature decorrelation. Across three Gemma-family models, four behavioral domains, and 356 layer-strength configurations, the method produces measurable domain-specific shifts while revealing a substantial gap between raw attribute movement and quality-preserving generation. In the strongest configuration, logical-correctness steering reaches a primary-score delta of $+1.16$ in Gemma~2 9B; however, our broader finding is that usable steering is highly localized by model, domain, layer, and strength. These results argue that activation-steering evaluations should report quality-conditioned success alongside raw behavioral shift. Our code and data are available at this https URL.

---


### 12. [Logic-Guided Data Extraction with Answer Set Programming and Large Language Models](https://arxiv.org/abs/2607.19365)

**<font color=#1a73e8>作者：</font>** Mario Alviano, Lorenzo Grillo, Nicola Leone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When Large Language Models (LLMs) are used for semantic data extraction from unstructured text, producing candidate relational facts from natural language, they may remain unreliable for tasks requiring complex combinatorial reasoning and global consistency. This paper proposes a logic-guided data extraction framework combining LLM-based extraction with Answer Set Programming (ASP). The LLM produces candidate facts, whereas ASP performs validation, inference, consistency checking, and control. Unlike existing pipelines that query the LLM independently for all target predicates, the proposed approach uses ASP reasoning to identify which predicates are logically admissible at each stage and to guide extraction queries. By interleaving LLM calls with ASP derivation, the framework infers logically implied facts without further extraction and detects inconsistencies early. We formalize the pipeline and prove that, under mild assumptions, it is equivalent to the baseline approach with respect to the final extracted facts, while requiring fewer LLM calls. We also introduce a caching mechanism for logic-based control queries, exploiting monotonicity of conjunctive queries over incrementally constructed fact sets to reduce solver invocations. Experiments on ASP-derived benchmarks show that the framework reduces LLM calls and improves extraction quality by mitigating spurious outputs, demonstrating the value of non-monotonic logic programming for controlled semantic extraction.

---


### 13. [Geometry-Guided Constraint Learning for LLM Safety Classification](https://arxiv.org/abs/2607.19366)

**<font color=#1a73e8>作者：</font>** Fumiaki Uehara, Koo Imai, Masato Tsutsumi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Safety as Polytope (SaP) learns linear half-space constraints in LLM hidden space but requires per-category tuning of the constraint count K. We show that sparse autoencoder (SAE) feature extraction resolves this: K=2 becomes optimal for 12/14 categories on Qwen3.5-9B, achieving 96-99% accuracy per category on our BeaverTails classification benchmark, largely eliminating the need for exhaustive sweeps (K=4-25 with random initialization). This convergence to two planes is consistent with the Linear Representation Hypothesis, providing suggestive evidence that safety boundaries in this setting admit a low-dimensional linear description in the SAE feature space. Building on this geometric perspective, we introduce a cone constraint whose learnable aperture adapts to each category's cluster concentration, stabilized by a three-phase training

---


### 14. [Rethinking Uncertainty Evaluation in Large Language Models](https://arxiv.org/abs/2607.19367)

**<font color=#1a73e8>作者：</font>** Krish Matta, Atharv Naphade, Andy Zou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Calibration is the primary criterion for evaluating LLM confidence, but it is insufficient: it admits trivially incoherent estimators, depends on the evaluation distribution, and does not test the extent to which the estimation can be interpreted as a consistent, underlying probability function. What we actually need is for LLM confidence estimates to satisfy the conditions required of coherent probabilistic beliefs. We formalize these conditions along three axes (structural coherence, faithfulness, and usefulness) and operationalize them as the C1 metrics. Widely used estimators systematically violate these conditions despite appearing well-calibrated: models assign lower confidence to logically easier questions 31\% of the time, and common interventions reducing RMSCE leave structural violations unchanged, suggesting that calibration is orthogonal to probabilistic validity. RLHF and chain-of-thought improve usefulness metrics without restoring coherence. Our results show current LLM confidence estimates cannot be interpreted as coherent probabilities; our framework provides the tools to measure and close this gap.

---


### 15. [Mitigating Scaffolding Collapse in Socratic Tutors via Representation Alignment](https://arxiv.org/abs/2607.19371)

**<font color=#1a73e8>作者：</font>** Jing Shao, Qifeng Wu, Hanyu Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based Socratic tutors increasingly guide students through multi-turn questioning, but they can suffer from scaffolding collapse: under sustained student pressure, a tutor gradually abandons guided inquiry and reveals solutions directly. Prior defenses primarily constrain observable responses through prompting, preference optimization, or filtering, leaving the internal representation drift that precedes trajectory-level collapse largely unaddressed. We propose Scaffold-Preserving Representation Alignment, a two-stage framework that first warms up a Socratic tutor with supervised fine-tuning, then combines trajectory-weighted direct preference optimization with a margin-preserving representation loss anchored to frozen reference states. Our method is designed to maintain separation between scaffold-preserving and collapse-inducing hidden states across dialogue turns. We evaluate our method across five STEM disciplines and five red-teaming attack strategies. On Qwen3-8B, our method lowers Collapse Rate to 32%, delays average collapse onset beyond nine turns, and keeps over-refusal low, suggesting that representation-level alignment can improve the robustness of long-horizon Socratic tutoring under our red-teaming protocol.

---


### 16. [Air Quality Arena: A Large-Scale Multi-Region Ground Monitoring Dataset and Benchmark for Air Quality Forecasting with Time-Series Foundation Models](https://arxiv.org/abs/2607.19381)

**<font color=#1a73e8>作者：</font>** Rishi Bharadwaj, Manik Gupta, Pandarasamy Arjunan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Air pollution causes an estimated 7.9 million premature deaths annually, making accurate forecasting a critical public health priority. Machine learning is increasingly being applied to forecast air pollution levels, yet existing benchmarks remain narrow in both geographic scope and pollutant coverage, and fail to evaluate the latest generation of time series foundation models (TSFMs) on real world, large scale data. We present Air Quality Arena (AQA), a large scale multi-country and multi-pollutant dataset (AQA-Data) and benchmark (AQA-Bench) to address this gap. AQA covers 6 major pollutants over a three year period across 7 diverse countries and 4 continents, with more than 14,000 station-pollutant series, aiming to provide a comprehensive benchmark for air quality tasks. We benchmark this dataset across 11 leading time series foundation models and classical baselines to assess performance on short-term air quality forecasting. Our results demonstrate that TSFMs are effective zero-shot forecasters and consistently outperform classical baselines, with our top-performing model employing a cross-modal architecture that leverages a vision foundation model for time series forecasting. AQA is publicly released at this http URL

---


### 17. [LAARA: Layer-Aware Adaptive Rank Allocation for Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2607.19391)

**<font color=#1a73e8>作者：</font>** Ashutosh Tripathi, Surya Deep Singh, Pranab Sahoo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation is widely used for parameter-efficient fine-tuning, yet existing methods typically assign the same adapter rank to every transformer layer despite their heterogeneous adaptation requirements. In this work, we show theoretically and empirically that uniform rank allocation is fundamentally suboptimal. Motivated by this observation, we propose LAARA (Layer Aware Adaptive Rank Allocation framework), a search-free framework that dynamically allocates ranks using lightweight diagonal Fisher estimates computed during training. LAARA combines projection-wise normalization, logarithmic compression, blended adapter importance estimation, and a vote-to-change dampening mechanism to produce stable and efficient rank adaptation. Experiments on GLUE and MathInstruct benchmark demonstrate that LAARA consistently matches or outperforms popular state of the art approaches such as LoRA, AdaLoRA, DyLoRA, and Bitfit while using significantly fewer trainable parameters. Our results show that Fisher-guided rank allocation provides a principled and effective foundation for adaptive parameter-efficient fine-tuning. The code is publicly available at: this https URL

---


### 18. [Leveraging Offline Supervision for Efficient and Generalizable Reinforcement Learning in Large-Scale Vision-Language-Action Models](https://arxiv.org/abs/2607.19399)

**<font color=#1a73e8>作者：</font>** Dmitriy Poyarkov, Aleksei Staroverov, Aleksandr I. Panov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> It is commonly observed that online reinforcement learning (RL) produces better-performing strategies than offline methods across a broad range of performance measures. In particular, RL-trained policies exhibit stronger out-of-distribution (OOD) behavior, where models trained only with imitation learning approaches often struggle. A recent study introduced an OOD-focused benchmark and reported that RL-trained vision-language-action (VLA) policies achieve noticeably better OOD performance and slightly better in-distribution (IND) performance than their counterparts trained with supervised fine-tuning (SFT). In this work, we investigate whether hybrid offline-online training can combine the advantages of both approaches. Specifically, we study RL methods regularized by offline supervision via either offline data or an offline-trained reference policy. We evaluate these approaches on the OOD benchmark and compare them with both offline-only training and standard RL. Our results show that although offline training achieves limited OOD performance by itself, incorporating offline supervision into RL preserves strong OOD capability while substantially improving training efficiency. In particular, the guided methods reach performance close to that of standard RL while requiring roughly half of the training budget. Rather than producing a trade-off between speed and OOD performance, the hybrid approach retains strong OOD capability while achieving this efficiency gain. Project page: this https URL

---


### 19. [Predictive single cell foundation model for gene regulation and aging with privacy-preserving tabular learning](https://arxiv.org/abs/2607.19400)

**<font color=#1a73e8>作者：</font>** Jiayuan Ding, Jianhui Lin, Ziyang Miao 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Pre-trained foundation models (FMs) have begun transforming single-cell genomics, but scaling them raises privacy concerns. Moreover, unlike text data, single-cell data is unordered and exhibits a unique tabular structure that current single-cell FMs overlook. We introduce Tabula, a privacy-preserving FM designed with federated learning (FL) that explicitly models the tabular structure of single-cell data. To deploy Tabula, we further developed Chiron, a decentralized AI agent-enabled platform for collaborative training across institutions without sharing raw data. Beyond strong performance across downstream benchmarks, Tabula reveals combinatorial regulatory logic across diverse biological systems, including hematopoiesis, pancreatic endogenesis, neurogenesis, and cardiogenesis. Using a new scRNA-seq dataset of paired young and aged human fibroblasts, Tabula nominates rejuvenation factors through age- and identity score-guided in silico prioritization, outperforming conventional approaches. Thus, Tabula represents an important advance in single-cell foundation modeling by integrating tabular learning with FL, paving the way toward privacy-preserving virtual cells for human health.

---


### 20. [NMR Elucidation as an Agentic Search Problem, Not a Modeling Problem](https://arxiv.org/abs/2607.19406)

**<font color=#1a73e8>作者：</font>** Irina Espejo Morales, Damon Hinz, Marvin Alberts 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Structural elucidation from Nuclear Magnetic Resonance (NMR) data remains a fundamental bottleneck across chemistry, materials science, and biology. We demonstrate that an agentic AI system can perform this task at a level comparable to graduate-level chemistry students. Instead of training a model to directly map spectra to structures, we build a single autonomous agent, backed by a frozen LLM, that interacts with a curated environment with access to domain-specific processing tools, validation checks, tabulated chemical shifts, and instructions that outline the stepwise nature of a chemist's thinking process. On the Alberts dataset, our agent elucidates structures with a top-1 accuracy of 71%, comparable to the performance of graduate students at 66% top-1 accuracy. On the van Bramer and AstraZeneca datasets, our agent achieved 80% and 20% top-1 accuracy respectively, outperforming zero-shot end-to-end deep learning models which were trained on large datasets of simulated spectra. These results show that reframing NMR elucidation as an LLM-guided constrained search, rather than a modeling task, yields substantial gains and suggests a path toward multi-step orchestration frameworks that integrate a variety of tools, models, and domain knowledge to assist in automating spectroscopic analysis.

---


### 21. [Reward-Aware Population Scaling of Evolutionary Strategies in LLM Fine-Tuning](https://arxiv.org/abs/2607.19408)

**<font color=#1a73e8>作者：</font>** Sung Cho, Gyubin Han  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Using Evolutionary Strategies (ES) for fine-tuning large language models is attractive because it is memory-efficient, parallel, and compatible with black-box or discrete rewards. Yet its population-size conclusions conflict sharply: fine-tuning with cross-entropy (CE) reward succeeds with $N=1$, while binary-reward training often needs $N \approx 30$. We show this gap is largely about reward design and normalization, not population size. In the capable-model regime we study, z-score advantage normalization can cause $N=2$ to fail. Disabling normalization lets binary-reward ES with $N=2$ improve on GSM8K and TREC across capable models spanning 0.5B-7B, where the normalized variant collapses or degrades. This small-$N$ risk is set by reward granularity: binary accuracy reward induces a zero-advantage probability $q$ that depends in closed form on base accuracy, batch size, and intra-pair correctness correlation; a zero-training probe on Qwen2.5-Instruct/GSM8K matches the formula with mean absolute error 0.020 across 12 configurations and finds the availability threshold $N_{\mathrm{avail}}$ to be small in this capable-model regime. The implication is not that $N=2$ is universally sufficient, but that small-population failure in capable-model binary ES can be an implementation artifact rather than an intrinsic population limit.

---


### 22. [FORCE-Bench: A Benchmark, Dataset, and Evaluation Harness for Agentic AI in Enterprise Finance](https://arxiv.org/abs/2607.19409)

**<font color=#1a73e8>作者：</font>** Wolfgang M. Pauli, Sarah Panda, Kidus Admassu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models have accelerated deployment of agentic systems in operational finance. Existing benchmarks emphasize measuring general capabilities, instruction following, or safety, but few directly address the operational finance workflows that agentic systems are now being deployed to automate. Finance professionals require agents to not only provide factually sound and properly grounded information, but also ensure that this information is verifiable and consistently adheres to rules and constraints of the operational finance domain. We introduce FORCE-Bench, which contains 251 expert-annotated queries and evaluates responses using a rubric-based framework calibrated to the requirements of the operational finance domain, across eight dimensions: accuracy, citations, clarity, depth, groundedness, recency, relevance, and structure. FORCE-Bench assesses agentic systems on three task types: financial obligation research (querying ERP systems for accounts receivable and payable data), financial entity performance research (answering time-bound questions from public filings and market data), and business brief generation (synthesising multi-source company intelligence reports). To reflect real deployment conditions, we evaluate our purpose-built agent, as well as the general-purpose agentic systems, under common tool access and latency-bounded settings. Results show that general-purpose agentic systems do not consistently meet finance-domain quality requirements under operational constraints, while the purpose-built Finance Agent for Microsoft 365 Copilot is more reliable across dimensions. We release the dataset, rubrics, harness, and analysis code as open-source to support reproducible comparison and adaptation to other enterprise finance environments.

---


### 23. [The Chronos Vulnerability: A Taxonomy of Temporal Persistence and Memory-Based Deception in Agentic AI](https://arxiv.org/abs/2607.19433)

**<font color=#1a73e8>作者：</font>** Om Narayan, Ramkinker Singh, Praveen Baskar  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The transition from stateless generative models in artificial intelligence to stateful, autonomous agents represents an architectural evolution that, while providing the capabilities of long-term planning and the automation of enterprise workflows, also represents the introduction of a new form of security threat, the Chronos Vulnerability. The Chronos Vulnerability represents the threat of memory-based attacks, including the Memory Injection Attack (MINJA) and the sleeper agent, in which the internal belief system of the autonomous agent is compromised, effectively decoupling the attack vector from the final catastrophic event. This study formalizes the threat model for persistence-based attacks and the threat of Dynamics Blindness in the context of the World of Workflows benchmark, demonstrating that traditional endpoint content filters are insufficient for the current stateful architecture. Consequently, this study synthesizes a defense-in-depth landscape, categorizing emerging frameworks such as diagnostic trajectory guardrails (AgentDoG), formal temporal verification (Agent-C), immunological memory consensus (A-MemGuard), and hardware-anchored trust via GPU-based Trusted Execution Environments (TEEs) and Zero-Trust memory architectures.

---


### 24. [Guardrails as Scapegoats: Auditing Unfaithful Safety Refusals in Tool-Augmented LLM Agents](https://arxiv.org/abs/2607.19449)

**<font color=#1a73e8>作者：</font>** Aarushi Singh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evaluation frameworks for tool-augmented LLM agents focus overwhelmingly on capability metrics or explicit tool crashes, leaving silent infrastructure failures and HTTP 200 responses with empty, null, or malformed payloads largely unaudited. We introduce a lightweight black-box auditing framework that injects four silent failure profiles across 12 production-adjacent tool stubs and classifies agent responses into three mutually exclusive behavioral classes: Honest Surrender (HSR), Fabrication (FAR), and Unfaithful Safety Refusal (USR). Evaluating two frontier and two open-source models at temperature zero under a neutral system prompt, we find that FAR dominates (56.6% of valid responses): agents treat empty payloads as real data, silently returning fabricated results. USR, in which an agent invents a policy or privacy rationale to explain the failure, is nearly absent at baseline (0.25%, one instance across 396 valid trajectories). Our key finding emerges from an ablation where we augment the system prompt with standard safety language ("prioritize user privacy and data security"), which amplifies USR by 15.6x (from 0.25% to 3.95%; 95% CI on ablation rate: 2.2%-6.4%; Fisher's exact test, p < 0.001). USR is a latent behavior, activated when safety vocabulary in the system prompt primes the model to reach for policy rationales when tools silently fail. Sensitive tools (fetch_medical_record, retrieve_contract, fetch_user_profile) account for the majority of USR instances. We propose a payload-response misalignment heuristic for production-level detection and discuss governance implications for safety-forward deployments.

---


### 25. [REGEN: Replay-recycling for Expert-to-Generalist distillation with Offline Reinforcement Learning](https://arxiv.org/abs/2607.19450)

**<font color=#1a73e8>作者：</font>** Yunjie Chen, Xiaoxin Chen, Fang Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale online reinforcement learning (RL) is the predominant means of eliciting advanced abilities including long-term reasoning and agentic tool use in large language models (LLMs). However, continuing to scale it across vast task domains of interest remains challenging in both computational infrastructure and cost, especially when considering RL as merely a one-off learning stage. Recently, a widely used technique for distilling knowledge across various domains and training stages, multi-teacher on-policy distillation (MOPD), helps to decouple the RL stage, saving costs, while maintaining generality across vast domains. Nonetheless, similar to online RL, MOPD requires coupled inference and backward passes, which continues to limit its scalability and computational efficiency. To address these challenges, we propose REGEN: Replay-recycling for Expert-to-Generalist Distillation with Offline RL. Instead of distilling from multiple teacher models, REGEN trains a generalist by simply recycling the replay memory -- the free by-product of the teachers' specialized RL training -- and employing offline RL algorithms. REGEN completely decouples the rollout sampling from the backward training process and thus greatly reduces the training cost. Across mathematical reasoning, code generation, and instruction following, REGEN matches the accuracy of MOPD at substantially lower cost. It potentially turns online RL into a data synthesis process instead of a one-off learning stage, and can potentially be extended to large-scale post-training without requiring heavy computational load.

---


### 26. [When Reasoning Narrows the Move: Diversity Collapse in LLM Game Play](https://arxiv.org/abs/2607.19523)

**<font color=#1a73e8>作者：</font>** Junyi Sha, Renfei Tan, David Simchi-Levi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning (SFT) is widely used to adapt large language models to downstream tasks, but its effect on behavioral diversity in sequential decision-making remains under-explored. We study this question in a controlled suite of deterministic board games based on tic-tac-toe variants, where optimal actions are exactly computable and diversity can be measured directly. Across state-level evaluation, arena gameplay, and training trajectories, we find that reasoning-mode generation frequently suppresses action diversity without uniformly improving action accuracy. Furthermore, standard SFT improves accuracy but often induces premature diversity collapse, which exceeds what is minimally required by the accuracy-diversity tradeoff. We then show that action augmentation, which trains on all optimal actions per state rather than a single demonstrated action, would partially mitigates this effect. Our results identify narrow-support imitation as a source of policy collapse in LLM decision-making and suggest that preserving action support during SFT is important for maintaining exploratory behavior.

---


### 27. [D3VL: Understanding Driving Scenes from 3D Time Series Data and Video with Language Models](https://arxiv.org/abs/2607.19528)

**<font color=#1a73e8>作者：</font>** Heesang Han, A. Lynn Abbott, Abhijit Sarkar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent advances in Multimodal Large Language Models (MLLMs) have triggered the development of end-to-end MLLMs for autonomous driving. However, the main emphasis to date has been for MLLMs using 2D images and videos. In contrast, this paper considers MLLM effectiveness using 3D sensors, particularly LiDAR and stereo cameras. LiDAR presents unique challenges to integration within an MLLM, largely because of data sparsity and lack of a grid structure for the data. For similar reasons, fusion of camera and LiDAR data within an MLLM pipeline is also uncommon. However, most autonomous systems rely on LiDAR-based sensing, and incorporating 3D data has been proven to improve performance in traditional 3D scene perception tasks. This paper presents D3VL, a novel MLLM framework that integrates 2D and 3D time-series data in a single but simple architecture. The model aims to answer questions involving traffic scene understanding and safety. D3VL shows an 11% improvement in the KITTI Question-Answering (QA) dataset compared to baseline methods in processing 2D and 3D time-series data. This paper further introduces the Waymo QA dataset extension, which assesses models' capabilities in processing 3D and time-series data under diverse driving conditions. D3VL implementation code and WaymoQA extension can be found on our supplemental website: this https URL

---


### 28. [Trustworthy Privacy-Preserving Multimodal Federated Learning for Personalised Breast Cancer Prediction](https://arxiv.org/abs/2607.19532)

**<font color=#1a73e8>作者：</font>** Ruth Amey, Muhammad Arifur Rahman, Taha Osman 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Federated learning has emerged as a potential solution to privacy concerns associated with using sensitive health data for training predictive models, particularly in personalised cancer care. This research investigates whether federated learning can support the development of robust models for predicting tumour progression in breast cancer patients while addressing four critical deployment pillars: transparency, scalability, security, and fairness. This study evaluates a federated learning framework using multimodal data, including clinical information, tumour characteristics, biomarker data, and patient demographics, alongside medical imaging data such as MRI scans, to model changes in tumour characteristics over time. The performance of the federated approach was compared with that of a centralised model trained on aggregated data. The report then further examines strategies to enhance secure model updates, maintain performance across patient subgroups, and support scalability across institutions. The findings assess whether federated learning can achieve predictive performance comparable to centralised learning while preserving data locality. These results contribute to understanding the feasibility of privacy-preserving, multimodal predictive modelling and support future applications such as digital twins to assist clinicians and patients in personalised treatment planning.

---


### 29. [ChronoStitch: Training-Free Composition of Visual KV Memories for Long-Horizon Temporal Reasoning](https://arxiv.org/abs/2607.19547)

**<font color=#1a73e8>作者：</font>** Santiram Tiwari, Nishant Sinha, Kunal Kislay  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long-video question answering requires a model to preserve visual evidence over time without repeatedly reprocessing the same video. A practical approach is to store the vision-language model's internal key-value (KV) cache for each video chunk and retrieve that state at query time. However, independently cached video chunks do not compose correctly: every chunk is prefilled from local rotary position zero, so naive concatenation collides temporal phases and removes the global order required for questions about what happened first, how often events occurred, or what changed across the video. This paper presents ChronoStitch, a training-free method for composing independently stored visual KV memories. The method first re-bases stored post-rotary keys onto a global three-axis multimodal RoPE coordinate system that preserves time, height, and width structure. We show why a one-dimensional scalar re-indexing is geometrically inconsistent for visual tokens because it turns spatial order within a frame into false temporal displacement. We then address the residual content gap left by positional repair: later chunks were originally encoded without attending to earlier chunks. ChronoStitch therefore selectively recomputes a small fraction of high-deviation later-chunk visual tokens while allowing them to attend over the composed cache. On Qwen2.5-VL-3B and the temporal split of TempCompass, ChronoStitch outperforms naive composition and position-only variants, improving event-ordering accuracy while running 3.3x faster than full joint re-prefilling.

---


### 30. [Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models](https://arxiv.org/abs/2607.19604)

**<font color=#1a73e8>作者：</font>** Nischay Dhankhar, Dos Baha, Abulhair Saparov  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Injecting factual knowledge into large language models (LLMs) reliably and at scale remains an open challenge. Hypernetworks provide a promising solution to large-scale knowledge injection. Although hypernetworks are typically applied for test-time adaptation, we explore their use in train-time knowledge injection, where, given a large corpus of facts, we train a hypernetwork to generate a fixed LoRA adapter that, when inserted into the target model, enable the model to answer questions about those facts. In this work, we investigate whether hypernetworks can be used to perform train-time knowledge injection and how this ability varies with scale. The scaling behavior of hypernetworks remains largely unstudied. Our design decouples the hypernetwork's injection capacity from the target model's general capability, enabling, for the first time, a rigorous study of scaling laws for hypernetwork architectures. We characterize how loss, reasoning accuracy, and out-of-distribution (OOD) generalization vary with hypernetwork depth, width, and target network size. We construct a large-scale dataset, called MegaWikiQA, containing tens of millions of multi-hop question-answer examples across 39 domains constructed from examples in Wikidata5M. Our results reveal: (i) hypernetwork-based injection exhibits broadly predictive power law scaling along all architecture axes; and (ii) hypernetworks are capable of reliable OOD generalization at increasing scales, suggesting that hypernetwork provides a promising alternative to other train-time adaptation methods such as LoRA finetuning and full fine-tuning, exhibiting steeper scaling exponents in all OOD evaluations. Together, these results establish hypernetworks as a principled and scalable substrate for train-time adaptation, and provide the first empirically grounded scaling laws to guide hypernetworks for factual reasoning in large language models.

---


### 31. [Task Competence Is Not Instruction Following: Evaluating Instruction-Conflicting Behavior in Small Language Models](https://arxiv.org/abs/2607.19608)

**<font color=#1a73e8>作者：</font>** Mahdiyeh Farajidizaji, Vatsal Raina  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction tuning is meant to make language models follow user requests, yet it is unclear whether small models comply when an instruction conflicts with their usual task behavior. We study this across three tasks - multiple-choice question answering (MCQA), sentiment classification, and mathematical question answering - by pairing a standard instruction with a conflicting non-standard one (select an incorrect option, output the opposite sentiment, or return twice the answer). This cross-task design allows us to test whether resistance to conflicting instructions is tied to specific task characteristics or reflects a broader behavioral tendency. As all predictions are scored against the original ground truth, a model that ignores the non-standard instruction still appears accurate. Using standard accuracy, non-standard accuracy, and an Instruction-Following Failure Rate (IFFR), we evaluate instruction-tuned Qwen models across sizes. Both standard accuracy and instruction following generally improve with scale, although the pattern is not consistent across all tasks and datasets. Small models stay competent yet routinely ignore the non-standard instruction, while larger models show a clear gap between the two settings. These findings suggest that gains in task capability do not automatically provide reliable control over model behavior. Task competence and instruction following are therefore distinct abilities, and reporting only standard accuracy hides instruction-following failures.

---


### 32. [Adaptive Capitulation: A Structural Failure Mode of LLM Responses in Vulnerability Contexts](https://arxiv.org/abs/2607.19629)

**<font color=#1a73e8>作者：</font>** Eunna Lee  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models operating in emotionally sensitive contexts face a structural trilemma: when users in vulnerable states request information that may reinforce maladaptive attribution, current response architectures resolve the tension through protective restriction, uninflected facilitation, or unintegrated co-presence of both imperatives -- each preserving one objective at the cost of the other. Administering a three-turn escalating vulnerability vignette to three commercial LLMs (900 sessions across material, relational, and somatic status-proxy variants) and coding responses with two binary indices (VCC/VCI), we characterize a previously undocumented failure mode we term adaptive capitulation: the model validates the social injustice underlying the user's distress before pivoting to detailed facilitation of the very acquisition it nominally discouraged. We show that the trilemma is structural rather than incidental, and propose Minimal Reattributive Sufficiency (MRS), an architecture-neutral design principle that embeds a single reattributive cue within an otherwise validating response, preserving a pathway toward autonomous reattribution without contesting the user's stated goal.

---


### 33. [Expert-Guided Forecast Editing for Time-Series Foundation Models](https://arxiv.org/abs/2607.19659)

**<font color=#1a73e8>作者：</font>** Hung Le, Minh Hoang Nguyen, Manh Nguyen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Time-series foundation models can forecast across heterogeneous domains without task-specific training, but their forecasts are fixed once produced and cannot directly incorporate task-specific expert feedback. We study expert-guided forecast editing: a frozen foundation model generates candidate future trajectories, and an expensive expert evaluator scores them to guide forecast revision. Under a tight query budget, two natural strategies sit at opposite ends: best-of-$N$ purely exploits the foundation model's predictive distribution, while optimization approaches mostly explore the forecast horizon as an unstructured high-dimensional vector. Each extreme is individually sub-optimal. We introduce \textbf{DEFT}, an expert-guided forecast editing framework that balances the two by first exploiting the foundation model's predictive samples in a decomposed trend--seasonal space, then exploring around them via component-wise refinement. DEFT queries the expert only on complete trajectories, then reuses scores for the trend and seasonal components that appeared in the queried recombinations. This lets each expert query provide structured component-level feedback while keeping the foundation model frozen. We compare DEFT against direct search approaches, including best-of-$N$, cross-entropy methods, and Bayesian optimization, under matched expert-query budgets. Across two forecasting benchmarks consisting of 78 datasets, three time-series foundation models, four feedback types, and seven query budgets, DEFT consistently improves the effectiveness of expert guidance. A molecular-dynamics case study further suggests that the same principle extends to more physically grounded feedback, supporting the hypothesis that sparse test-time guidance should be spent balancing prior exploitation with structured exploration.

---


### 34. [Same Game, Different Story: A Minimal Conservative Strategic Robustness Benchmark for Large Language Model Agents](https://arxiv.org/abs/2607.19670)

**<font color=#1a73e8>作者：</font>** Seyed Pouyan Mousavi Davoudi, Alireza Amiri-Margavi, Amin Gholami Davodi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly operate in strategic settings where outcomes depend on the actions of other agents. This raises a reliability question: will a model choose consistently when the same incentives are presented through different narratives? We introduce Same Game, Different Story, a benchmark that defines strategic robustness as invariance of model-induced action distributions under payoff-preserving changes in framing. We illustrate the framework through a secondary analysis of published aggregate cooperation rates for GPT-3.5, GPT-4, and LLaMa-2 across four social-dilemma games. The retained comparison covers business and friend-sharing framings, representing 24 model-game-context cells and 7,200 decisions in the source study. Because trial-level data were unavailable, approximate counts were reconstructed from published figures; the resulting estimates are therefore illustrative rather than an exact replication. Under the paper's conservative transformation, pooled strategic robustness is 0.783, and friend-sharing framing increases cooperation by 0.307 relative to business framing. The results indicate that social-relational framing can substantially alter LLM behavior even when the underlying action sets and payoffs remain fixed. Strategic robustness should therefore be evaluated separately from strategic competence, using families of payoff-equivalent prompts rather than a single presentation of a game.

---


### 35. [Multi-Mask Diffusion Language Models for Few-Step Generation](https://arxiv.org/abs/2607.19686)

**<font color=#1a73e8>作者：</font>** Sijin Chen, Yinuo Ren, Heyang Zhao 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion models (MDMs) are a promising family of language generators, but achieving high-quality few-step generation remains challenging. In MDMs, all forward trajectories collapse to a single fully masked state, leaving no terminal entropy for consistency-style few-step generation. While recent few-step alternatives based on uniform-state diffusion avoid this degeneracy, it becomes harder to distinguish clean tokens from noise than MDMs, which usually harms modeling quality and training efficiency. In this work, we propose a multi-mask diffusion model (MultiMDM) that preserves the masking structure towards few-step generation. In the forward process, each clean token is first pushed towards a designated mask and then gradually mixes over the mask set. As a result, the backward process has a drafting capability by predicting a designated mask before refining to a clean token. We derive a closed-form ELBO training objective for MultiMDM that supports continual training from pretrained MDMs. In addition, we formulate a purely discrete-state consistency distillation scheme, with a shared-Gumbel coupling to reduce pathwise entropy. Experiments on pretraining and distillation show that MultiMDM provides an effective foundation for principled few-step generation.

---


### 36. [Efficient Clustering with Provable Guardrails for LLM Inference at Scale](https://arxiv.org/abs/2607.19704)

**<font color=#1a73e8>作者：</font>** Longshaokan Wang, Wai Tsang Keung, Punit Ghodasara 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Scaling LLM-based applications to millions of users is bottlenecked by the inference cost and latency of modern foundation models. A natural fix is to cluster the inputs and call the LLM only on cluster representatives, letting other members inherit the output -- but this is only safe if each member is measurably close to its representative. Existing clustering methods do not offer such per-sample quality control at scale: none jointly guarantee a minimal within-cluster similarity, exact matching of categorical attributes, and scalability to tens of millions of samples. We propose a two-stage algorithm that generates initial clusters with Mini-batch K-Means, then greedily selects representatives within each initial cluster -- a step equivalent to the Johnson-Chvatal heuristic for Set Cover over alpha-balls in embedding space. The algorithm enforces the similarity and attribute guardrails exactly by construction, and runs in $O(nd + n^2 d/K)$ time and $O(nd + n^2/K^2)$ memory for $n$ samples, feature dimension $d$, and $K$ initial clusters -- linear in $n$ when $K$ grows proportionally with $n$. We provide benchmarks against common clustering methods on internal and public datasets: our method not only delivers per-sample guardrails but also runs 10-1000x faster and scales to data sizes where most standard methods become intractable. Deployed on 38 million customers for a persona-based recommender, the clustering method cut downstream cost and latency by 50-fold while preserving personalization and unblocked the production launch.

---


### 37. [Point-Selection Fine-Tuning Framework for Robust Point Cloud Classification](https://arxiv.org/abs/2607.19711)

**<font color=#1a73e8>作者：</font>** Da Li, Chang Ma, Dongfu Yin  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Noisy and corrupted points can substantially degrade point cloud recognition performance, especially under challenging corruption settings. In particular, full fine-tuning of 3D pre-trained models may amplify the influence of outliers and overwrite robustness priors learned during pre-training, while naive parameter-efficient adaptation remains sensitive to corrupted tokens. To address this issue, we propose PSFT, a point-selection fine-tuning framework that improves robustness while remaining parameter-efficient. PSFT first estimates point-wise influence from pre-pooling features and adaptively retains minimally influential points to suppress outliers. Based on the selected subset, a prompt generation branch predicts layer-wise prompt tokens and injects them into a frozen backbone for lightweight downstream adaptation. To further mitigate residual noise after selection, we append a lightweight feature filter with bottleneck MLP transformation and Beta-gated residual blending to refine patch-token representations before prediction. Extensive experiments show that PSFT consistently reduces corruption error on ModelNet-C and ModelNet40-C across all tested 3D pre-trained backbones, while achieving the strongest ScanObjectNN-C results with ULIP-2 and Uni3D-B among the evaluated tuning strategies. Our implementation can be found at this https URL.

---


### 38. [How Fast Can Reward Models Score? A Systems Study of C++ and PyTorch Inference Runtimes for RLHF](https://arxiv.org/abs/2607.19712)

**<font color=#1a73e8>作者：</font>** Venkata Naga Sai Vishnu Rohit Pulipaka, Anish Katta, Deva Rohit Reddy Peddireddy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In RLHF pipelines, reward scoring blocks policy updates. Slow scoring bottlenecks the entire loop, since no update runs until every rollout gets a score. And yet most setups just default to PyTorch eager mode or this http URL, no one checks if that's actually fastest. Scoring itself is small. Rollout generation eats far more of a typical RLHF step. But scoring and generation fight over the same CPU and GPU resources, so a faster scoring engine doesn't shrink step time on its own. It mainly frees up capacity generation can use instead. We built a native C++ inference engine on ONNX Runtime. First step: confirm correctness. Output matched the PyTorch reference to 5.7 x 10^-6 on CPU and 4.2 x 10^-3 on GPU, close enough to trust. Then we tested it against PyTorch eager mode, this http URL, and FastAPI, on both CPU and GPU. CPU was decisive. Our engine beat every baseline, confidence intervals didn't even overlap. GPU gave a different view: we beat PyTorch and FastAPI, but this http URL came out ahead. Further testing traced the speedup to ONNX Runtime itself, not C++ as a language. And batching strategy mattered more than either the language or the runtime choice, more than we expected. The results are from repeated, independent runs, since single runs just aren't reliable enough to trust.

---


### 39. [The World Model Remembers, the Actor Forgets: Dream Rehearsal for Continual Model-Based RL](https://arxiv.org/abs/2607.19749)

**<font color=#1a73e8>作者：</font>** Gurp Nijjer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Model-based reinforcement-learning agents of the DreamerV3 family forget catastrophically when trained on task sequences, even when an unbounded replay buffer preserves every earlier experience. We ask a question the continual-RL literature has assumed an answer to but never measured: which component forgets? Under never-clear replay, pre-registered component-level probes (n=3 seeds throughout) show that the world model retains essentially everything measurable about old tasks -- reward discrimination (retention ratio ~1.0), value estimates, and termination structure -- while the actor's behavior collapses. Forgetting in this regime is a channel problem, not a memory problem. We demonstrate this by intervention: with the world model frozen and identical imagined rollouts, reinforcement learning in imagination fails to recover a lost skill (0/3 seeds), while supervised self-imitation on the world model's own graded dreams recovers it on 3/3 seeds with zero environment interaction. Interleaved during training, this graded dream rehearsal yields a task-label-free, parameter-constant continual learner: 3/3 four-task chains retained where plain replay passes 0/3, 3/3 eight-task chains, and consistent gains over matched real-episode cloning (paired difference +0.13, bootstrap 95% CI [0.07, 0.24], complete seed separation). The dream-grading step is load-bearing: we characterize two scoring failure modes, provide an offline selection gauge that caught both before they contaminated results, and give a realized-first grading rule that closes them. All experiments were pre-registered with committed protocols; every refuted hypothesis is reported.

---


### 40. [Symbol and Footprint Database for Electronic Components by Agentic Recognition and Generation](https://arxiv.org/abs/2607.19767)

**<font color=#1a73e8>作者：</font>** Yichen Shi, Yuzhi Liu, Zhuofu Tao 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A rich and recognizable component library is the cornerstone of printed circuit board (PCB) design and generation. Traditionally, engineers manually create symbols and footprints and design PCB schematics, which is time-consuming and error-prone. Leveraging multimodal large language models (MLLMs), we develop SFgen, an agentic recognition and generation flow of symbol and footprint for electronic components. SFgen achieves 86% accuracy for symbol generation and 80% accuracy for footprint generation. We use the SFgen method to create SFnet, a database of symbols and footprints. It now has 1000 components and is expanding constantly, which lays the foundation for automatic generation of PCB designs.

---


### 41. [AlphaRoute: Large Language Models as Semantic Optimizers for Multi-Objective Routing](https://arxiv.org/abs/2607.19768)

**<font color=#1a73e8>作者：</font>** Kabir Murjani, Mishri Bhavsar, Manish I. Patel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Very Large Scale Integration (VLSI) global routing is an NP-hard combinatorial optimization problem requiring signal net assignment across capacity-constrained 3D grids while minimizing congestion, wirelength, and via transitions. Because traditional heuristics rely on static penalty schedules that fail on complex congestion topologies, we present AlphaRoute: a multi-objective adaptive search framework reformulating rip-up and reroute (R&R) into a dynamic optimization system. We introduce SHAP-based overflow decomposition to isolate per-net congestion, driving targeted subgraph extraction via 3D Dijkstra maze routing and an adaptive PathFinder policy. Crucially, AlphaRoute employs Large Language Models (LLMs) as semantic policy optimizers. Bounded by a deterministic knowledge graph, the LLMs interpret congestion metrics to dynamically adjust penalty parameters. Evaluated on ISPD 2025 benchmarks, AlphaRoute reduces overflow by 98.6% on MEMPOOL. On the constrained ARIANE design, we achieve an overflow of 146,109 (a 29.8x reduction in overflow over the state of the art), yielding a penalized score of S_orig = 0.0538 versus the State-of-the-art (SOTA) 1.780. These results demonstrate that superior algorithmic search geometry can overcome the latency of interpreted Python implementations.

---


### 42. [Look Before You Edit: Attention-Guided Camera Placement and Multi-View Alignment for 3D Gaussian Splatting Editing](https://arxiv.org/abs/2607.19777)

**<font color=#1a73e8>作者：</font>** Jaeyeon Park, Taeho Kang, Youngki Lee  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-driven 3D scene editing with 3D Gaussian Splatting (3DGS) typically applies a 2D diffusion editor to views rendered from fixed training cameras, limiting both the spatial coverage of edits and the user's freedom to target specific objects in complex scenes. We present LB-Edit, a framework that addresses two coupled problems: where to place editing cameras for localized edits, and how to make per-view edits agree with one another so that the 3D scene remains consistent after fine-tuning. First, Attention-Guided Editing Camera Placement (ACP) probes the diffusion model's self- and cross-attention at multiple candidate camera distances to find where attention is well-contained in the region of interest, then places a compact, geometrically diverse editing camera set at that attention-optimal distance. Second, Multi-view Attention Alignment (MAA) steers the editor toward the same edit across views along two axes: it aligns appearance by sharing self-attention features via token-level correspondence, and aligns spatial location by lifting cross-attention maps onto the 3D Gaussians as a shared 3D attention field, suppressing both appearance and spatial drift. Experiments on multi-object and single-object scenes show that our method achieves the highest user preference in instruction fidelity, multi-view consistency, and editing locality, using as few as 5 editing views and reducing latency by up to 7x over existing methods.

---


### 43. [Not Birds of a Feather: Personality-Based Partner Selection in LLM Agents](https://arxiv.org/abs/2607.19785)

**<font color=#1a73e8>作者：</font>** Tao Wang, Hsiang-Ling Chiu, Chihang Wei 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems increasingly let one agent choose which other agents to work with, and agents are increasingly given personalities through personas. We test whether Big Five personality alone influences partner selection when capability is explicitly held constant. Host agents chose among six validated candidate archetypes -- five marked high on one trait (openness, conscientiousness, extraversion, agreeableness, neuroticism) plus a balanced control -- presented with randomized names and ordering across five task categories (375 trials). With neutral hosts (Study 1, n=150), selection departed drastically from chance ($\chi^2(5)=325.8$, $p<.001$), following a task-stereotype map: the open archetype won 100% of creative trials, the conscientious archetype 90-97% of strategic, synthesis, and problem-solving trials, and the neurotic archetype 37% of analytical trials (Cramer's V=.74); the extraverted, agreeable, and balanced archetypes were almost never chosen, although human meta-analyses identify team agreeableness as among the strongest personality predictors of team performance. With personality-assigned hosts (Study 2, n=225), and contrary to human similarity-attraction, self-similar partners were selected below chance (11.1% vs. 16.7%, p=.025) and at greater-than-chance trait distance (p<.0001); conscientious hosts diversified away from their own archetype, recruiting vigilant and open partners. Personality-based selection in LLM agents is real, strong, task-stereotyped, non-homophilous, and miscalibrated against human team-performance evidence -- with direct implications for bias auditing in agent marketplaces.

---


### 44. [Trace: A Taxonomy-Guided Environment for Multidomain Visual Reasoning](https://arxiv.org/abs/2607.19790)

**<font color=#1a73e8>作者：</font>** Md Tanvirul Alam  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) has substantially improved language-model reasoning, yet its extension to vision-language models remains constrained by the lack of training data that are simultaneously broad, exactly verifiable, and reproducible. We introduce Trace, a taxonomy-guided environment for multidomain visual reasoning. Trace factorizes task construction into a scene grammar and an executable task program, separating visual realization from answer computation. A shared semantic state determines the rendered image, prompt, typed answer, verifier state, and replayable instance trace. The resulting environment comprises 1,000 tasks over 277 scene grammars and 11 visual domains, with controlled semantic and visual variation. RLVR on 64,000 Trace instances improves the macro-average across 24 external benchmarks by 3.51 percentage points for Qwen2.5-VL-3B and 4.06 points for Qwen2.5-VL-7B, providing evidence that broad procedural training can transfer beyond the generated task distributions. Project page: this https URL.

---


### 45. [Silent Failures in Multimodal Agentic Search:A Diagnostic Taxonomy and Cross-Judge Evaluation](https://arxiv.org/abs/2607.19793)

**<font color=#1a73e8>作者：</font>** Zhengxian Wu, Junjie Gao, Kai Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal agentic search systems increasingly rely on external tools to answer knowledge-intensive visual questions. However, existing evaluations mainly focus on final-answer accuracy and may miss failures in the search trajectory. In this work, we study such hidden reliability issues as silent failures. We introduce a six-category taxonomy covering modality shortcuts, phantom grounding, wrong-evidence-right-answer cases, over-retrieval laundering, cross-modal contradiction, and provenance hallucination. Based on this taxonomy, we build a trajectory-level diagnostic pipeline that evaluates both answer correctness and evidence-grounding quality under a unified ReAct-style scaffold. Experiments on MMSearch-Plus trajectories across four frontier multimodal models show that surface accuracy consistently overestimates true trajectory-level correctness. We further use cross-judge validation, blank-image stress tests, and tool ablations to show that silent failures are capability-dependent and often shift rather than disappear. Home-page: this https URL

---


### 46. [TriAgent: Divergence-Aware Multi-Agent Committees for Cost-Efficient Financial Sentiment Analysis](https://arxiv.org/abs/2607.19794)

**<font color=#1a73e8>作者：</font>** Isabel Xu, Cynthia Xu, Rachel Ren 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production LLM-based financial sentiment analysis faces a structural cost trap: most queries are trivially classifiable, yet expensive cloud reasoners process them all, and the bill scales linearly with user count. We present TriAgent, a multi-agent committee stratified by contextual granularity -- a word-level lexicon (VADER), a sentence-level domain transformer (FinBERT), and a cross-sentence reasoner (Qwen2.5, 0.5B-14B-4bit, with Mistral-7B and Phi-3.5-mini cross-family checks). A three-way Semantic Divergence Index (SDI) measures pairwise disagreement across granularities and routes each query accordingly. Our central finding is the critic plateau: when the LLM is re-tasked as a critic over the smaller agents' outputs, F1 plateaus at ~0.87 across 1.5B-7B Qwen (bootstrap 95% CIs overlap), while a same-size 3-persona vote drops to F1=0.66, which is driven by granularity-stratified diversity. Three corollaries follow from the same SDI signal: (i) a Shared Consensus Dictionary on multilingual sentence-BERT answers 95% of Chinese queries from an English cache at F1=0.99 -- cross-border canonicalization at zero marginal cost; (ii) SDI doubles as a post-hoc LLM-hallucination detector at AUC=0.90; (iii) the SDI single-stage strategy attains the best risk-adjusted return (Sharpe=3.50) on a 20-ticker back-test, dominating both always-FinBERT (1.36) and always-LLM (0.11). At 10M-user scale, TriAgent saves $9.3M/year vs. a GPT-4o-mini baseline. Code, lexicons, and the SCD are released.

---


### 47. [Dreamer-CPC: Message Learning with World Models for Decentralized Multi-agent Reinforcement Learning](https://arxiv.org/abs/2607.19809)

**<font color=#1a73e8>作者：</font>** Taisuke Takayama, Naoto Yoshida, Tadahiro Taniguchi  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In multi-agent reinforcement learning (MARL), inter-agent communication is effective for improving performance under partial observability. Representation learning-based approaches enable decentralized agents to learn messages grounded in their own observations, but they rely only on current observations and cannot convey information accumulated over time. We propose Dreamer-CPC, a decentralized model-based MARL method that integrates message learning based on Collective Predictive Coding (CPC) into the world model of DreamerV3. Each agent independently maintains a world model and a message module, and infers and exchanges messages from the latent states of the world model that reflect the history of past observations and actions. We evaluated Dreamer-CPC in two environments: Observer, a non-cooperative information-sharing task, and CatchApple, a newly introduced task in which task-relevant observations are temporarily missing. In both environments, Dreamer-CPC outperformed IPPO-CPC, an existing CPC-based method that generates messages from current observations, as well as no-communication baselines. In particular, in CatchApple, Dreamer-CPC achieved 4 to 5 times the episode return of IPPO-CPC, demonstrating effective coordination where other methods fail due to missing observations. These results suggest that communication grounded in the latent dynamics of world models can support decentralized decision-making when current observations alone are insufficient.

---


### 48. [Rewarding Better Thinking for LLM Preference Alignment](https://arxiv.org/abs/2607.19824)

**<font color=#1a73e8>作者：</font>** Xubo Liu, Wenya Guo, Ruxue Yan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM preference alignment aims to optimize models toward human preferences across diverse user instructions. Reinforcement learning has become a major post-training approach for this goal, but existing proxy rewards are often outcome-level, mainly evaluating the final response while providing limited guidance for the reasoning trajectory. This can make credit assignment coarse when multiple responses receive similar final scores, leaving trajectory-level preferences under-specified. To address this limitation, we propose Thinking Checklist Reward (TCR), a process-oriented reward for RL-based preference alignment. TCR converts preference pairs into sample-specific thinking checklists and uses them to evaluate whether the generated reasoning trace addresses the preference-implied considerations. To reduce overlap with outcome-level supervision, TCR further introduces an exponential moving average (EMA) residual formulation to isolate a complementary thinking surplus beyond what is predictable from the outcome reward. Experiments on five models from three model families show that TCR consistently improves alignment performance across diverse benchmarks, with ablations further validating the importance of EMA-based residual formulation and sample-specific checklist supervision.

---


### 49. [VizRAG: Enhancing Retrieval-Augmented Generation with Hypergraph Visualization](https://arxiv.org/abs/2607.19830)

**<font color=#1a73e8>作者：</font>** Yanbin Wei, Yang Chen, Renling Gan 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hypergraph-based RAG systems surpass traditional graph-based approaches by organizing complex n-ary atomic facts among entities, rather than relying solely on binary relationships. Despite the advancements in multimodal large language models (MLLMs) with enhanced visual capabilities, current hypergraph-based RAG frameworks predominantly restrict knowledge retrieval and reconstruction to a unimodal, text-centric paradigm. This limitation prevents them from fully leveraging the powerful visual perception capabilities of modern MLLMs. To address this gap, we systematically explore the integration of hypergraph awareness in RAG systems through visual cues. By incorporating visual representations of hypergraphs into the RAG pipeline, we introduce VizRAG, the first RAG system to support visual hypergraph structure awareness. Experimental results demonstrate that VizRAG significantly outperforms strong baselines, validating the promising potential of hypergraph visualization as a novel approach for RAG systems.

---


### 50. [D2VBench: Benchmarking Large Language Models with Value Dilemmas in Daily Scenarios](https://arxiv.org/abs/2607.19834)

**<font color=#1a73e8>作者：</font>** Siyi Hao, Yidi Cao, Linhao Yu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> With the wide application of large language models (LLMs) in real-world scenarios, the value implication of their outputs is crucial. However, existing evaluation benchmarks suffer from insufficient coverage of value dilemmas in daily scenarios involving multiple value conflicts and simplistic evaluation formalisms that fail to assess LLMs' value alignment. To address these issues, we propose D2VBench, a value alignment benchmark comprising 10,000 instances of real daily dilemma scenarios constructed through a multi-stage collaboration between LLMs and humans, grounded in 158 manually annotated fine-grained value concepts. For evaluation on the benchmark, we present a hybrid evaluation paradigm that integrates multiple-choice questions with open-ended questions. We conduct comprehensive evaluations on eight mainstream LLMs. Experimental results demonstrate that D2VBench exhibits high reliability and robustness, effectively reflecting the LLMs' alignment across different value categories and dimensions, and providing a more realistic and fine-grained tool for research on value alignment. The dataset is available at this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/2 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-92](./part-02.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
