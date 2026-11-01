# 🧠 大模型相关研究 | 2026年11月02日

> 本类共 **353** 篇论文：已确认 **335** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-353](./part-08.md)

---

### 301. [Factorized Representations of Concurrent Temporal Variables in Pretrained Language Models](https://arxiv.org/abs/2610.40328)

**<font color=#1a73e8>作者：</font>** Xinhe Zhang, Arnau Marin-Llobet  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models often need to maintain multiple contextual variables that evolve independently within a document. Prior work has identified structured representations of individual temporal or contextual quantities, but their joint organization remains less understood. We study this question using controlled documents with independently phased language-switch and topic-change timers. Across ten pretrained checkpoints, both timers are linearly decodable from the same hidden states. Removing a timer-associated centroid plane substantially reduces access to its associated variable while having little effect on the concurrent timer, although the planes are nonorthogonal and contain cross-timer information. Separate timer contributions also explain most reproducible variation among joint-state centroids. These signatures persist from 3 to 51 timer values and across Qwen3 checkpoints from 0.6B to 14B. Schedule position affects continuation probabilities, but the tested centroid displacement produces no consistent timer-specific output effect. Together, these results support approximate factorization based on selective accessibility and approximately additive joint-state geometry in overlapping subspaces.

---


### 302. [A Unified Hessian-Guided Framework for Post-Training Quantization](https://arxiv.org/abs/2610.40345)

**<font color=#1a73e8>作者：</font>** Mads Toftrup, Marco Federici, Boris van Breugel 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-bit quantization enables efficient deployment of large language models by reducing memory footprint and computational cost. Achieving high accuracy at low precision requires selecting quantization ranges, linear transformations, and weight rounding decisions. Existing approaches typically optimize these components independently using local reconstruction objectives, which fail to account for the varying impact of quantization errors on downstream predictions. Direct optimization of task-level metrics would provide a more faithful objective, but is challenging due to the discontinuous nature of quantization operations and the high computational cost of evaluating their downstream effects.
In this work, we derive a Hessian-guided approximation of the output change induced by joint weight and activation quantization. Based on a tractable Fisher approximation, we formulate a unified post-training quantization framework that enables the joint optimization of quantization ranges, linear transformations, and weight rounding under a common output-sensitivity objective. The resulting method remains practical for modern large language models and consistently outperforms state-of-the-art transformation and rounding methods across both channel-wise and block-wise quantization settings.

---


### 303. [Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation](https://arxiv.org/abs/2610.40350)

**<font color=#1a73e8>作者：</font>** Zheng Zhu, Xiaozhuan Liang, Xi Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agents powered by large language models (LLMs) have demonstrated remarkable progress in solving complex reasoning tasks. However, LLM agents often falter on long-horizon tasks due to cognitive overload, as their working memory becomes cluttered with expanding and irrelevant information, which dilutes their attention and hinders effective planning and reasoning. To mitigate this challenge, we introduce Cognitive Resource Self-Allocation (CORAL), a novel reasoning paradigm that empowers agents to proactively optimize their context. Implemented as an agent-callable working memory management toolset, CORAL allows an agent to checkpoint its task progress and verified facts, and adaptively initiate a new problem-solving episode by resetting cluttered context while preserving only the checkpointed information, enabling it to resume reasoning from a clean state. We further enhance the agent's checkpointing capabilities using a Multi-episode Agentic Reinforced Policy Optimization algorithm. On the GAIA benchmark, CORAL with an 8B model achieves 42.8% average accuracy, with particularly strong gains on the most challenging long-horizon tasks (Level 2 and Level 3). Crucially, these gains come at a substantially lower inference cost: CORAL consumes 6-7$\times$ fewer input tokens than a ReAct agent. It also generalizes to multi-hop Knowledge QA benchmarks and to the considerably harder BrowseComp, where it improves a strong proprietary agent by 8.0 points.

---


### 304. [HiFOR: Hierarchical Foresight with Action-Guided World Grounding for Vision-Language-Action Model](https://arxiv.org/abs/2610.40373)

**<font color=#1a73e8>作者：</font>** Rongxing Ding, Hongyu Qu, Kehong Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language-Action (VLA) models have demonstrated promising capabilities in robotic manipulation by integrating visual perception, language understanding, and action generation. Recent advances have further incorporated future prediction to enhance the understanding of environmental dynamics and task progression. However, existing methods often model short-term dynamics and long-term task objectives separately, while directly incorporating predicted futures into action policies without sufficiently considering their relevance to current action requirements. To address these limitations, we propose HiFOR, a hierarchical foresight framework with action-guided world retrieval. Specifically, Hierarchical Foresight Prediction jointly predicts short-term state evolution, semantic milestones, and final goal states through a Hierarchical Dependency Mask (HDM), establishing dependencies across temporal horizons. Building upon these predictions, Structure-Aware Latent World Modeling organizes future latent representations along the horizon, view, and spatial dimensions to facilitate fine-grained retrieval. Furthermore, Action-Guided Factorized World Retrieval adaptively retrieves relevant future information from the structured latent world based on evolving action representations during denoising, providing targeted guidance for action generation. Extensive experiments on two simulation benchmarks and six real-world robotic manipulation tasks demonstrate the effectiveness of our approach.

---


### 305. [Beyond Selected Breakthroughs: Evaluating Language Models on Randomly Sampled Mathematical Conjectures](https://arxiv.org/abs/2610.40382)

**<font color=#1a73e8>作者：</font>** Helen Jenne, Davis Brown, Jesse He 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The last year has seen a shift in AI-assisted mathematics, with frontier language models producing proofs of and counterexamples to long-standing open conjectures. However, studying only the current set of major breakthroughs provides an incomplete picture of LLM capabilities and the computational resources needed to achieve reported results. To address this, we introduce a new dataset, OpenConjecture, which collects conjectures from mathematics papers published on the arXiv since February 2026. We use these conjectures as a source of open mathematical problems, and apply frontier GPT models to a random sample of 200 of these conjectures over three passes using a reproducible protocol without problem-specific mathematical guidance. Rather than attempt expert verification of these candidate solutions, we analyze the types of problems for which LLMs produce solutions and the characteristics of these solutions. The models we test produce candidate solutions for roughly 60% of the conjectures, with counterexamples about 1.3 times more common than proofs. We estimate solution novelty, assess how solutions cite and relate to existing literature, and analyze whether the proposed resolution relies on either an error in or underspecification of the conjecture. We find that models sometimes propose resolutions that are outside the authors' intent (e.g., proposing the trivial group as a counterexample) and that a number of proofs follow closely from existing results, but that some resolutions exhibit at least moderate novelty. Our findings underscore the need for evaluations that go beyond correctness to assess fidelity to the intended statement, attribution, and the nature of the mathematical contribution.

---


### 306. [Scaling Mathematical Proof Supervision from Structured Textbooks](https://arxiv.org/abs/2610.40394)

**<font color=#1a73e8>作者：</font>** Youqing Fang, Zhouqi Hua, Yinhao Tang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Mathematical supervision for language models is typically flattened into isolated problem-solution pairs, discarding the curricular organization and evidential structure of the original sources. We introduce TOME-Math (Textbook-Oriented Mathematical Evidence), a large-scale corpus that converts 2,118 textbooks spanning the core areas of university-level mathematics subjects into approximately 380K structured proof-supervision records while preserving chapter order, proposition-proof links, dependency references, and source provenance. Leveraging these structural signals, we explore curriculum learning across multiple mathematical subjects and characterize scaling patterns with supervision volume and source breadth. At full scale, fine-tuning on TOME-Math raises the unweighted mean score across our held-out evaluations and established public benchmarks by 16.7 percentage points over the base model, while exceeding all three public instruction-data baselines evaluated in aggregate. Our findings highlight structured textbooks as both a scalable source of mathematical supervision and an empirical framework for studying the impact of data organization on mathematical reasoning. We will release the corpus to facilitate further research on structured mathematical supervision.

---


### 307. [Understanding and Mitigating Role Spoofing in LLMs](https://arxiv.org/abs/2610.40396)

**<font color=#1a73e8>作者：</font>** Ezra Edelman, Benjamin Edelman, Surbhi Goel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite growing capabilities, LLMs remain susceptible to prompt injections: malicious inputs that can manipulate or hijack models. In particular, it has recently been observed that LLMs can exhibit role confusion (Ye et al., 2026), where models attribute the source of text based on its style instead of its labeled role. Malicious text in tool outputs (for instance, a malicious webpage accessed by an agent) can leverage role confusion to impersonate the user, an attack we call role spoofing}. In this work, we seek to understand and mitigate role spoofing. We study how models track "who said what" in a conversation, showing that they use cues from both content (e.g., semantics and writing style) and structure (e.g., control tokens and formatting). We show that LLMs are highly susceptible to role spoofing attacks that combine both fake structure and content. Additionally, in a toy setting, we show that adversarial training which teaches the model to ignore content-based injections does mitigate content-based attacks but leaves the model susceptible to structure-based attacks. This can explain why frontier models, with increased resistance to many injection attacks, can still be susceptible to role spoofing. Finally, we propose a new method for detecting role spoofing using linear probes trained to predict roles in a conversation, and show that it is effective across different settings.

---


### 308. [SCARL: Sequence Confidence-Aligned Reinforcement Learning](https://arxiv.org/abs/2610.40407)

**<font color=#1a73e8>作者：</font>** Zhenghong Ke, Jingbo Zhou, Hua Wu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves language-model reasoning by scoring sampled responses with a rule-based verifier and reinforcing those that pass. Where a classifier's training couples predicted probability to labels, nothing ties an RLVR policy's confidence in a response to its reward: aligned training would drive responses with the same advantage toward equal confidence, yet the advantage is blind to confidence. Under this sequence-confidence misalignment, a success the policy barely found earns the same update as one it produces with near certainty, and a confident error is corrected no harder than an exploratory one. We propose SCARL (Sequence Confidence-Aligned Reinforcement Learning), which reshapes, but never re-signs, each advantage with the alignment gap between the response's group-relative confidence and the outcome its advantage certifies, normalized into shares of each class's advantage budget. Misaligned samples absorb the force, responses with the same advantage are driven toward equal confidence, and repairing the misalignment doubles as a remedy for the entropy collapse that erodes exploration. SCARL provably reduces to its base estimator when a class's confidences agree, adds no extra passes and one hyperparameter. On Qwen3-4B-Base it lifts average Pass@32 by 2.4 points over DAPO and is best among nine compute-matched methods on both coverage and per-draw accuracy; applied unchanged across four estimators and four backbones, it improves 14 of 16 settings while preserving policy entropy and widening the confidence-correctness separation. Our code is available at this https URL.

---


### 309. [Retrieving from Your Own Mistakes: On-Policy Training of Embedding Models for Multi-Hop Retrieval-Augmented Generation](https://arxiv.org/abs/2610.40409)

**<font color=#1a73e8>作者：</font>** Chenjie Qiu, Zixuan Zeng, Shaobin Shi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Complex questions in retrieval-augmented generation require evidence spread over several documents, and an answer is reliable only when the retriever finds all of it. Chain embedding retrievers collect such evidence step by step, re-encoding the question together with the passages retrieved so far, and we find that they are already strong: trained only on gold histories, a small chain embedding retriever that calls no language model outperforms graph-based systems and is competitive with a search agent. This training, however, leaves a gap. At test time the retriever conditions on its own retrievals, which soon contain mistakes: by the third step, about half or more of the states it visits hold a wrong passage, and these passages lower its chance of retrieving a missing gold passage well beyond what the difficulty of the states explains. We propose on-policy state training, which trains the encoder on the states it reaches itself. At every epoch the current encoder retrieves chains for the training questions; each state it visits, including those built on its own mistakes, is labeled with the earliest gold passage still missing while the other missing gold passages are masked, so that no correct continuation is penalized; and the encoder is updated contrastively on these states mixed with teacher-forced ones, so that its training distribution follows it as it learns. The resulting retriever retrieves complete evidence more often than teacher-forced training and the systems we compare, and it transfers without further training to harder long-chain variants of HotpotQA and 2WikiMultiHopQA that we construct. On the same states, it recovers from its own mistakes far more often, and controlled comparisons attribute the gain to training on the states the encoder currently reaches.

---


### 310. [Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success](https://arxiv.org/abs/2610.40444)

**<font color=#1a73e8>作者：</font>** Amir H. Rezaeian, Weiyi Sun, Yassine Benajiba 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-use benchmarks often score agents by final task success, but terminal outcomes can obscure whether the intermediate tool-call trajectory was executable. We propose prefix executability as a trajectory-level evaluation protocol for tool-using agents. The protocol measures whether every prefix of a predicted tool-call sequence remains executable under tool schemas, state preconditions, and data dependencies, and summarizes reliability using Prefix Executability Curves (PEC), First-Error Depth (FED), Trajectory Executability Rate (TER), horizon-normalized AUC-PEC, and Recovery Rate (RR). We instantiate the protocol on stratified samples from BFCL-v3 multi-turn and ToolSandbox, and on the complete Airline/Retail base splits of $\tau^3$-bench. We observe that outcome-only and prefix-level rankings diverge: agents whose execution is conditioned on an unverified plan often achieve higher point-estimate final success than non-plan-conditioned baselines while substantially lowering TER and AUC-PEC. These divergences are precisely the failure modes that prefix executability is designed to expose: they reveal whether apparent success rests on an executable trajectory, where invalidity first enters, and whether success follows recovery from an earlier failure. As a validation intervention, explicit pre-execution plan checking can improve executable-prefix survival while maintaining competitive terminal success. These results show that final success alone is insufficient for evaluating tool-use agents and that prefix-level executability provides an actionable reliability signal for comparing agents, diagnosing failures, and assessing validation mechanisms.

---


### 311. [Glance: The Generator Is Its Own Reranker](https://arxiv.org/abs/2610.40454)

**<font color=#1a73e8>作者：</font>** Adilet Metinov, Chingiz Arziev  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation commonly serves separate models for reranking and answering, duplicating model residency and passage processing. We introduce Glance, which equips the generator with a lightweight decision adapter and pointer head to score candidate passages from a shared prefill. Short relevance probes branch from the cached context, producing one score per passage without separately prefilling each query-passage pair. A single resident 9B backbone supports generation, general decisions and reranking, with approximately 0.1 GiB of additional memory per decision skill. After 39 minutes of MS MARCO fine-tuning, Glance achieves nDCG@10 of 0.741 on SciFact and 0.345 on NFCorpus, compared with 0.721 and 0.326 for bge-reranker-v2-m3. On 300 HotpotQA questions, its selected context improves answer F1 by 0.045 over cross-encoder-selected context under the same base generator (paired bootstrap 95% CI [0.014, 0.076]). In a scaling study, reranking quality keeps rising up to 200 candidates (43k tokens) scored from one shared prefill, where it exceeds the cross-encoder by 0.058 nDCG@10, and a probe-only activated adapter lets generation continue from the original passage cache. These initial results demonstrate generator-based reranking with one resident backbone; evaluation currently covers two retrieval datasets, one QA dataset and one backbone family.

---


### 312. [Training language models in simulation for psychiatric intake](https://arxiv.org/abs/2610.40476)

**<font color=#1a73e8>作者：</font>** Samuel Schmidgall, Tim Strother, Alex Bijamov 等 56 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In psychiatric practice, the clinical intake interview remains a primary diagnostic instrument, requiring the clinician to establish rapport while disentangling complex, overlapping presentations. Here, we show that multi-turn reinforcement learning (RL) in simulation environments improves language model performance on structured text-based psychiatric intake, spanning history-taking, differential diagnosis, and initial management planning. In a randomized, double-blind crossover study ($N = 60$ matched scenario pairs, 120 encounters) comparing the RL-trained agent against its identically prompted base model, 32 board-certified psychiatrists role-played standardized patients while a separate panel of 15 independent, board-certified psychiatrists scored the de-identified transcripts. The trained agent outperformed the base model in 76.7% of matched scenario pairs ($p < 0.0001$), with gains on an adapted clinical-examination rubric ($d_z = 0.77$, $p < 0.0001$), patient-centered communication (82.0% vs. 65.2%, $p < 0.001$), and differential diagnosis appropriateness (68.3% vs. 33.3%, $p < 0.001$). Across 127 psychiatrist-validated simulated intake scenarios, the trained agent nearly doubled its base model's clinical rubric score (0.706 vs. 0.379; composite reward 0.564 vs. 0.294, $p < 0.0001$). To systematically probe conversational safety, we established two Delphi-consensus taxonomies, of clinical safety risks and relational competencies, from which 256 challenging adversarial presentations were derived; we find that training in simulation environments more than halved under-triage of acute safety risks (12.9% vs. 30.5%, $p < 0.0001$). Simulation environments thus provide a controlled testbed for training and stress-testing psychiatric conversational agents, with gains that transferred to psychiatrist-enacted encounters, though residual gaps require safeguards and clinician oversight.

---


### 313. [Preserving Utility in Continual LLM Unlearning via Orthogonal Projections](https://arxiv.org/abs/2610.40483)

**<font color=#1a73e8>作者：</font>** Juan Belieni, Ana Carolina Erthal, Eliezer de Souza da Silva 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Unlearning concerns the task of removing the influence of a sensitive portion of the training data, such as protected, copyrighted or private text, from a model without retraining it from scratch. While unlearning requests happen continuously during a model's lifetime, the vast majority of LLM unlearning methods are ill-suited for iterated removal, yielding steep decay in forgetting and utility upon sequential unlearning. This decay stems from interference between successive updates, as each new deletion can undo earlier ones or push the model further along directions already degraded by them. To address this, we introduce Continual Orthogonal Projection (COP), a gradient-projection scheme that restricts each update to the orthogonal complement of activation subspaces cached from prior forget sets. This approach provably guarantees first-order non-interference with earlier deletions. COP stores only a low-rank basis per layer, requiring neither past gradients nor previous forget sets, and plugs into unlearning methods that update the model through gradient steps on a differentiable loss without modifying its objective. Experiments on standard LLM unlearning benchmarks (TOFU and RWKU) show that COP preserves utility across sequential requests without weakening forgetting, preventing the collapse of standard objectives and forgetting more effectively than continual-specific baselines.

---


### 314. [Agentic University: Collaborative Agents for Personalized Learning](https://arxiv.org/abs/2610.40492)

**<font color=#1a73e8>作者：</font>** Jingru Fan, Tianle Zhou, Yunjie Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models support personalized tutoring, content generation, and adaptive learning paths. However, capability development requires these resources and interactions to form a coherent learning process that evolves with the learner. A central challenge is to align goals, activities, and assessment while using learning evidence to decide what should follow. We introduce Human-Participatory Multi-Agent Organization and instantiate it in Agentic University (AU). In AU, learners participate as organization members and work with specialized agents to maintain a revisable Capability Program. The program connects personal goals, learning activities across modalities, and layered assessment, while learner feedback and performance guide subsequent support. Our evaluation shows advantages in program organization, assessment design, and revision quality. Users achieved larger mean assessment gains (12.19 versus 5.61 points on a 50-point scale) and reported stronger cognitive support. This work contributes an organizational approach to adaptive learning that makes learner participation a continuing basis for multi-agent coordination. The Agentic University project is available at \href{this https URL}.

---


### 315. [Algebraic World Model: From Exploration to Proofs](https://arxiv.org/abs/2610.40503)

**<font color=#1a73e8>作者：</font>** Guancheng Pan, Qixin Tan, Yang Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI has made remarkable progress in mathematics, solving challenging problems with machine-checkable proofs in Lean, yet typically relying on predefined mathematical definitions and formal specifications. This raises a natural question: can it reason rigorously about an unknown world? We introduce the Algebraic World Model (AWM), a framework that turns interaction with unfamiliar environments into explicit mathematical models supporting formal reasoning. AWM explores the environment and develops executable Python hypotheses, continually testing and revising them against observations. It then structures these hypotheses into typed objects and shared rules, simplifies their structure through category-theory-guided transformations, and formalizes the resulting model in Lean 4 to prove reachability and impossibility. AWM can formally prove that a goal is unreachable, even beyond explored trajectories. On two impossible game levels, it constructs closed, kernel-checked Lean proofs excluding every legal winning sequence in all six runs, while Claude Opus 5.5 and GPT-6 Astra, equipped with coding tools, produce none in twelve baseline runs. Four of AWM's six initial bounds are correct, compared with one for Opus 5.5 and none for GPT-6 Astra; given only feedback that a cheaper win exists, AWM revises its rules and constructs new proofs, reaching six of six correct bounds. Moreover, AWM produces interpretable mathematical models whose rules can be inspected and tested step by step. Across all 25 public ARC-AGI-3 games, these models enable Lean to replay the winning trajectories of all 183 levels and generalize beyond observed play, predicting unseen transitions and detecting changes in game mechanics. With Claude Opus 5, AWM clears all levels with a score of 99.9, while its certified winning trajectories use only 43% of the human baseline's actions.

---


### 316. [A Low-Rank Space Captures Linear Alignment Between LLM and Human Neural Activity During Naturalistic Language Listening](https://arxiv.org/abs/2610.40511)

**<font color=#1a73e8>作者：</font>** Zach Paris, Emily Finn  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as computational models of human language processing, yet it remains unclear which components of their representations drive alignment with neural activity. Here, we use ridge reduced-rank regression to identify the brain-predictive subspace of LLM representations: the representational directions that support linear prediction of neural responses. Across three naturalistic language-listening datasets spanning intracranial electrophysiology and fMRI, and six model conditions spanning autoregressive, bidirectional masked, and randomly initialized language models, we find that full linear encoding performance can be recovered using only 1-3% of the original embedding dimensionality. These low-dimensional subspaces generalize across held-out participants and, to a lesser extent, across datasets, suggesting that neural predictivity is concentrated in a compact and partially shared representational space. We next compare these brain-predictive directions with the principal axes of variation in the embeddings. Principal component analysis requires substantially more dimensions to recover neural prediction, demonstrating that the directions most useful for predicting neural activity are distinct from those capturing the most overall variance within LLM representations themselves. Finally, characterizing the learned subspaces allows us to surface interpretable features that are overrepresented in neural activity above and beyond the LLM representations. Together, these results show that LLM-brain alignment is supported by a small, structured subset of model representations and provides a framework for better understanding exactly why these representations align. Code can be found at: this https URL

---


### 317. [How I Aligned Your Model: Scaling Up Multilingual Safety Training with Templates](https://arxiv.org/abs/2610.40516)

**<font color=#1a73e8>作者：</font>** Max Neuwinger, Hanna Yukhymenko, Imanol Schlag  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment for Large Language Models is heavily focused on English with limited multilingual representation, particularly damaging low-resource language performance. Related open training datasets are often limited in size or do not follow region-localized harmful topics to broaden the scope of alignment beyond cultures. We propose a scalable template-based augmentation pipeline to produce massive multilingual refusal and benign corpora, extracting safe templates from harmful prompts, translating them and then filling in the slots with culturally authentic entities, both harmful and benign. As a result, we release MSafeTemp, a validated corpus spanning 60 languages useful for multilingual safety alignment and evaluation. Using the dataset, we show that English-only evaluation misjudges multilingual safety: for several models, attacks that fail in English succeed once translated, while culturally localized variants expose further failures that translation alone misses. We also confirm that augmenting safety training data through templates allows for higher diversity and quality of alignment, resulting in improved safety performance beyond English. MSafeTemp and the respective pipeline are aimed at facilitating research and development of safer and more responsible models for less-represented cultures.

---


### 318. [IndicIPR-QA: A Benchmark for Extractive Question Answering on Indian IPR Laws](https://arxiv.org/abs/2610.40518)

**<font color=#1a73e8>作者：</font>** M. Mohaiminul Islam, Muhammad Abulaish  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Legal Question Answering (QA) over statutory texts is a challenging task in Natural Language Processing (NLP), especially in low-resource settings with complex legal systems. It requires answers that are precise and grounded in the law. However, to the best of current knowledge, no existing extractive QA benchmark provides exact answer spans from statutory texts across all seven Indian Intellectual Property Rights (IPR) Acts. This paper presents IndicIPR-QA1, an extractive QA benchmark for Indian IPR laws. The proposed dataset contains 4,462 QA pairs from 1,116 statutory contexts across seven Acts. Questions and answers are generated using GPT-4o and validated through nine automatic quality checks, single and multi-model LLM evaluations, and a 200-pair human audit. Section-level partitioning prevents source-context overlap across the training, validation, and test sets. Further analysis examines answer span length, lexical overlap, and multi-clause structure across the corpus and individual Acts. BM25 achieves a token-level F1 score of 20.21, while fine-tuned InLegalBERT reaches 85.02 under a unified sliding-window inference protocol. The large performance gap between BM25 (20.21 F1) and InLegalBERT (85.02 F1) shows that simple word matching is not enough to answer these legal questions. Performance also varies across the seven Acts, indicating substantial differences in answer-extraction performance.

---


### 319. [PhysCount: Do MLLMs Count Visual Appearances or Physical Entities?](https://arxiv.org/abs/2610.40530)

**<font color=#1a73e8>作者：</font>** Lidong Lu, Jiaxin Lv, Liangrui Dong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Images reveal appearances, but counting often asks about physical objects. A single entity may be visible directly, in several reflections, or through glass, so detecting every visible occurrence does not determine how many entities are present. Existing visual counting benchmarks rarely separate these two operations. We introduce PhysCount, a benchmark for evaluating whether multimodal large language models (MLLMs) can distinguish what appears in an image from what physically exists in the scene. PhysCount contains 546 real-world images and 4,595 human-written questions organized into 651 target-specific groups. For each group, annotators locate the relevant appearances, label how each is observed, and identify appearances of the same entity. Four complementary question families test the enumeration of appearances, the enumeration of physical entities, image-formation-specific counting, and appearance--entity correspondence. We measure both accuracy on each family and the proportion of groups answered entirely correctly. Across 40 MLLMs, counting visible appearances is substantially easier than recovering the identities that connect them. Even the strongest model answers every question correctly in only 13.36\% of groups. Performance declines when one entity produces many appearances or when its appearances cross observation modes. Higher image resolution improves access to visual evidence but brings limited gains in complete-group accuracy, whereas answering related questions jointly produces a marked improvement. These results expose a gap between recognizing what is visible and correctly recovering the physical entities behind those observations.

---


### 320. [Homebrewed SLMs: Autoregressive and Masked Diffusion Language Models Built at Home for Portuguese](https://arxiv.org/abs/2610.40533)

**<font color=#1a73e8>作者：</font>** Pedro Carvalho Brom  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Building a language model of one's own no longer requires a data centre. This tutorial trains one from scratch, tokenizer included, on one consumer GPU, and shows how to tell whether it is good for the tasks of a specialist domain. It proposes no new method. It releases a tested Python package and two notebooks in Brazilian Portuguese with autoregressive and masked diffusion generation on one network, a preregistered comparison protocol, legal tasks built from text alone with a Kneser-Ney floor and public yardsticks, reference numbers for models of 11 to 12M parameters, and a catalogue of defects that only measurement revealed. On Brazilian prose and federal laws, at minutes per run, the autoregressive mode peaks at 64 epochs over the same text and then memorises it, while masked diffusion improves up to 256. At their best points on test, the diffusion bound exceeds the autoregressive likelihood by 0.06 bits per byte, within the preregistered minimum effect. On held-out laws and on acts published after training, the model ties a 6-gram floor in likelihood on the same windows, and it loses to the floor at continuing those acts. It beats the floor at detecting tampered text, and fills cross-references more often than the floor and public models of 160M and 630M parameters, only in decrees, a genre absent from training, where those scorers stay near or below chance, and in filling the blank only when each group weighs the same, since per item it ties the 630M model. On laws, the public models, trained with about 5x10^2 to 10^5 times its compute, lead in tampered text and continuation. The blind human reading is preregistered and not part of this version.

---


### 321. [On the Fundamental Limits of Prefill-Based Decoding Length Prediction](https://arxiv.org/abs/2610.40541)

**<font color=#1a73e8>作者：</font>** Haowen Shi, Xuzhe Yan, Fahao Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Predicting how many tokens a large language model (LLM) will decode, using only prefill-phase hidden states, is a key primitive for inference scheduling. We show that current benchmarks conflate predictor quality with task hardness: when the target model, dataset, or sampling configuration changes, reported accuracy collapses even though the predictor is unchanged. We trace this instability to an overlooked error source---the inherent stochasticity of autoregressive decoding---and derive bounds that every prefill-side method must obey. Our analysis treats decoding as a stopped stochastic process. The per-step stopping probability of a response is not constant but ramps up over hundreds of steps, so the decode length inherits a central limit theorem from the many local decisions that determine where a response ends; this yields per-prompt normality with an explicit error term, together with an affine variance law $\sigma=\alpha\mu+b$ whose slope is the coefficient of variation of the number of response segments. Empirically, the normal law reproduces the per-prompt MAE and the central mass of the decode-length distribution to within a few percent, and the residual departures from normality (mild right skew, slight excess kurtosis) are the ones predicted by the sampling-noise correction. Under fixed model, data, and sampling conditions, a broad design space of predictors (MLP, EGTP, FiLM, soft-label, and Mixture-of-Experts variants) converges to similar performance close to the bound, confirming that \emph{system error dominates model error}. We argue for a benchmarking protocol that fixes the model, data, and sampling parameters and that reports relative-error metrics alongside absolute ones. Code and analysis tools are available at this https URL.

---


### 322. [The Privacy and Security Risks of Edge LLM Optimization](https://arxiv.org/abs/2610.40543)

**<font color=#1a73e8>作者：</font>** Mingchen Li, Ren-Yi Huang, Dumindu Samaraweera 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Edge deployment of Large Language Models requires optimization techniques that reduce memory, computation, and energy costs. However, preserving task performance does not necessarily preserve security. We argue that optimization is an information transformation that can alter representations, decision pathways, and trust boundaries, creating security drift and optimization-induced attack surfaces.

---


### 323. [Ramanujan Challenge Results: AI-Assisted Evaluation Pipeline for Multi-Format Proofs](https://arxiv.org/abs/2610.40551)

**<font color=#1a73e8>作者：</font>** Alan Sorani, Ashvni Narayanan, Michael Shalyt 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As AI's mathematical capabilities rapidly improve, meaningful benchmarks are shifting from university-level problems and math olympiads to research-level mathematics. The Ramanujan Challenge is a benchmark comprised of research-level problems in number theory, including unpublished results and open conjectures. It presented concrete formulas for mathematical constants whose correctness can be checked numerically, while their proofs may require non-obvious mathematics. Here, we analyze the Challenge submissions, measuring the relative success of different AI models, Computer Algebra Systems (CAS), and formal tools. We find correct submissions that are conceptually distinct from the official solutions, and a proof of one of the published open conjectures. Evaluating the submissions exposed a second challenge: judging complex proofs reliably at scale. We introduce an AI-assisted evaluation pipeline for natural language proofs, CAS code, and Lean formalizations that assesses semantic and logical correctness. Compared with the conventional one-shot LLM judgment, our pipeline reduces false-positive verdicts on natural language proofs from 23% to 6% and improves judgment accuracy on supporting code from 46% to 58%. This approach provides a methodology for evaluating research-level mathematics at scale, with potential applications across mathematics and AI for science.

---


### 324. [Advancing Clinical Genomic Analysis with a Skill-Centred Agent](https://arxiv.org/abs/2610.40556)

**<font color=#1a73e8>作者：</font>** Qiaoyu Zheng, Weike Zhao, Yanjie Fan 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical genomic analysis requires experts to integrate evolving guidelines, databases, and computational evidence. As sequencing has become increasingly accessible, this complex and labor-intensive process has become a major bottleneck to the timely use of genomic information in clinical decision-making. To fill this gap, we developed ClinGeX, a large-language-model agent that composes 105 curated executable skills through task-specific retrieval and dependency-aware orchestration. On 223 temporally held-out benchmark cases, ClinGeX achieved 71.7\% macro-averaged task-level concordance with expert reference classifications, compared with 45.7\% for the strongest comparator. In a three-condition, counterbalanced human-AI collaboration study, 45 clinical genomic professionals assessed 135 clinically derived cases under routine (no AI assistance), DeepSeek-assisted and ClinGeX-assisted conditions. ClinGeX assistance increased raw case-level concordance across criterion-level variant analysis, genomic interpretation in rare disease and molecular oncology decision-making (51.1\%, 57.8\%, 64.4\% versus 15.6\%, 31.1\%, 20.0\% in comparator conditions) and reduced reported interpretation time in all scenarios. During an exploratory one-month real-world non-interventional assessment, 11 experienced professionals submitted feedback on 96 self-selected analysis episodes and reported frequent conclusion adoption and time savings. These findings support executable domain skills as a promising approach to augment specialist genomic interpretation.

---


### 325. [Comparing Human Role-Players and LLM-Simulated Clients in Online Counselling Training: An Analysis of Counselling Patterns](https://arxiv.org/abs/2610.40563)

**<font color=#1a73e8>作者：</font>** Eric Rudolph, Philipp Steigerwald, Jens Albrecht  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> This study investigates the capabilities of Large Language Models to simulate counselling clients in educational role-plays in comparison to human role-players. Initially, we recorded role-playing sessions, where novice counsellors interacted with human peers acting as clients, followed by role-plays between humans and clients simulated by Mistrals Mixtral 8x7b using 4-bit quantization. These interactions were analysed with a counselling communication pattern system at sentence level. We investigated two key questions: (1) to what extent LLM-generated responses replicate authentic conversational dynamics and (2) whether counsellors' communication behaviour differs when interacting with human versus LLM-simulated clients. The findings highlight both similarities and differences in the application of counselling patterns across scenarios, showing the potential of LLM-based role-playing exercises to enhance counselling competencies and to identify areas for further refinement in virtual client simulations.

---


### 326. [Every Token Needs Its Own Teacher: Multi-teacher Adaptive On-policy Self-distillation](https://arxiv.org/abs/2610.40574)

**<font color=#1a73e8>作者：</font>** Yifu Luo, Chuang Ma, Zeyu Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy Self-distillation (OPSD) has proven effective for post-training large language models by constructing a teacher conditioned on privileged references. However, existing approaches keep the teacher fixed either throughout training by consistently exposing it to the full reference, or within each response by adaptively varying partial reference exposure only across responses. In this paper, we argue that neither of them is sufficient. Instead, every token needs its own teacher, as the teacher preference can vary token by token within the same response. Through a teacher-intervention pilot study, we validate that the teacher preference differs across tokens, and reveal that a preferred teacher can be identified for each token through majority voting and KL-based selection. Motivated by these findings, we propose Multi-teacher Adaptive On-policy Self-Distillation (MTA-OPSD), the first token-level adaptive OPSD method. Our method constructs a multi-teacher pool consisting of candidate teachers, and enables every token to adaptively select its preferred teacher during training. Experiments with Qwen3 models on mathematical reasoning tasks show that MTA-OPSD consistently outperforms existing OPSD approaches with an average gain of up to $+5.9$ over the base model, highlighting the importance of adapting teacher supervision at the token level. The code is available at this https URL.

---


### 327. [Multi-View MoE: Letting Every Router Shape Expert Computation](https://arxiv.org/abs/2610.40577)

**<font color=#1a73e8>作者：</font>** Zelin Zhao, Tianchi Ma, Junyuan Shang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse mixture-of-experts (MoE) models expand parameter capacity by activating a small subset of experts per token. Expert selection directly affects model capabilities under a fixed active-expert budget. Dense evaluation of all experts reveals weak agreement between single-router rankings and expert-utility evaluation rankings, especially in middle and deep layers. Richer signals for selection and computation incur additional cost: selection based on internal expert activations requires preliminary computation, while processing multiple full representations separately through the same expert repeats its computation. We propose Multi-View MoE to improve expert selection with multiple routers and reuse their preferences to modulate expert computation under a fixed expert budget. Its Multi-Router submodule aggregates sigmoid scores from independently initialized routers. These routers develop highly differentiated expert preferences during training, allowing experts strongly favored by one router or jointly supported by several routers to be selected. Multi-View further uses each selected expert's relative scores across routers to mix learned latent views into its input, reusing routing preferences for both selection and computation. Each selected expert executes one forward pass, preserving the active-expert count, expert FLOPs, and all-to-all communication volume. On a 24-layer 10B-A1B model trained on 708B tokens, full Multi-View MoE improves the nine-task downstream mean by 1.18 percentage points over the baseline. Multi-Router alone yields a 0.6-percentage-point gain and improves the rank correlation between router scores and evaluated expert utility, with relative increases of 8.1% globally and approximately 58% in the layer with the lowest single-router alignment. Controlled mixing interventions show the model uses input differences that depend on both the expert and the token.

---


### 328. [VeriCUA: Verification as Agentic Exploration for Computer-Using Agents](https://arxiv.org/abs/2610.40578)

**<font color=#1a73e8>作者：</font>** Qiushi Sun, Da Yu, Alexander Knop 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building and scaling computer-using agents (CUAs) across desktop, mobile, and web environments requires reliable task-completion verification for data curation, evaluation, and reinforcement learning. Typical automated approaches prompt vision-language models (VLMs) to judge trajectories or generate programs to inspect application state. However, both rely on partial views of complex digital environments. VLM judges are restricted to supplied observations, while generated programs depend on accessible state. These views can omit decisive evidence or leave completion judgments unsupported. Tailoring separate verifiers to different platforms and access settings adds further engineering cost. We present VeriCUA, a platform-agnostic framework for verification through agentic exploration. It treats verification as dynamic evidence gathering and assessment within a shared procedure for online and offline settings across platforms and observation modalities. After inspecting the available context to construct a task rubric, the verifier selects GUI or code checks for unresolved requirements and combines their findings under explicit evidence rules. Experiments show improved agreement with reference labels over the compared baselines across these settings, with the largest offline gains on hard cases and stronger rejection of false completion claims online. Further analyses connect these gains to complementary evidence and test-time exploration.

---


### 329. [RADIOlogy: A Single-Pass Approach to Training-Free Zero-Shot Anomaly Detection](https://arxiv.org/abs/2610.40580)

**<font color=#1a73e8>作者：</font>** Joaquín Figueira, Giacomo D'Amicantonio, Egor Bondarau  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Current zero-shot anomaly detection methods often rely on complex prompt-learning techniques or computationally expensive sliding-window strategies to achieve fine-grained visual alignment to detect small-scale anomalies. This reliance stems from the fundamental limitation of standard CLIP architectures, where [CLS] token attention and spatial patch pooling struggle to capture subtle, localized anomaly features. While prompt-learning approaches aim to bridge this gap, they typically require a large number of ground-truth segmentation masks from auxiliary datasets, which are often unavailable in specialized domains. In this work, we show an emerging property of multi-head attention pooling in vision-language models: remarkable zero-shot anomaly localization and detection right out of the box. We translate this property into a single-pass anomaly detection technique, RADIOlogy, that does not require dense, windowed execution and significantly outperforms other training-free baselines. Instead, the method relies on a simple contrastive scoring approach that compares the average similarity between vision features and a suite of normal and abnormal prompts. Furthermore, we leverage the agglomerative features of RADIO models to enhance pixel-level anomaly segmentation using a dense anomaly refinement pipeline. Finally, we show how the vision-language family of training-free zero-shot anomaly detection techniques can be applied successfully to the medical domain with minimal modifications. Code is available at this https URL.

---


### 330. [Pre-Crime for Agents, at the Last Second: Probing When a Recruited Agent Gives In](https://arxiv.org/abs/2610.40588)

**<font color=#1a73e8>作者：</font>** Leonidas Raghav  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When AI agents share channels and credentials, one agent can press another to break its operator's rule, a first step towards collusion. Output filters check only what an agent has already written. Can an overseer tell beforehand that an agent is about to give in? We show that a linear probe on the agent's activations can, in a controlled multi-agent setting. Across six scenarios, a peer presses a target for up to 20 rounds to reveal a secret, such as a deploy token; the target often refuses, then gives in. Read at each model call before its output is written, the probe picks out the one that leaks. On held-out Qwen3-32B episodes, at a threshold set to flag 5% of benign calls, it catches 82% of leaking calls. At a similar flag rate, a zero-shot decision-model monitor catches 26%. On gpt-oss-20b, a probe on its reasoning reaches AUROC 0.91. A bag-of-words classifier trained on the same calls comes close, so most of the gain comes from training on labels, not activations. The probe also flags permitted disclosures: it reads the coming disclosure more than the violation. The warning is short-range, and halting on any alarm would stop most benign episodes, which a second text check does not fix. A warning raised before generation could let an overseer stop an agent that is about to give in, ahead of others acting on its messages or recruitment spreading through a swarm.

---


### 331. [Collaborative AI agents for autonomous experimental research with solid-state quantum spins](https://arxiv.org/abs/2610.40589)

**<font color=#1a73e8>作者：</font>** El Mustapha Mansouri, Eikichi Kimura, Masato Koga 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An autonomous research laboratory could conduct an entire study, from formulating questions to preparing manuscripts. Artificial intelligence (AI) offers one route towards this goal. Recent AI systems take on several research roles, but may draw conclusions that the evidence does not support. Here, we present an autonomous research laboratory in which agents based on large language models assess one another's work and can stop or redirect investigations. They can generate and reject research questions, require separate theoretical checks and conduct experiments designed to challenge their claims. We demonstrate these capabilities by investigating ensembles of quantum spins in diamond. The agents derived the minimum number of calibration settings needed to predict responses to a defined family of microwave pulse sequences. They checked the result computationally and designed experiments to distinguish competing predictions. An initial experiment agreed with the theoretical predictions, but repeated reference measurements showed that the signal was drifting during data collection. The agents therefore treated the result as inconclusive and revised the measurement protocol without relaxing the acceptance criteria. The revised experiment met those criteria and supported the theoretical predictions. This study demonstrates that collaborating AI agents can select research questions, derive theoretical results and test their predictions experimentally.

---


### 332. [When to Assist and What to Suggest: Joint Gating and Memory-Grounded Hint Generation in One Compact Decoder](https://arxiv.org/abs/2610.40611)

**<font color=#1a73e8>作者：</font>** A. J. A. Jubayer Talukder, Mohammad Ariful Haque  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Proactive assistants offer short, memory-grounded hints during a conversation, deciding when to assist and what to suggest. Current systems split this between a gate and a larger generator; we evaluate both together on 28,058 decision points. Stage-wise generation scores are oracle-gate ceilings: behind a real gate, end-to-end exact match is 0.2619 against a ceiling of 0.2971, and end-to-end precision is 0.2387, leaving substantial headroom. A gate pays off through precision and compute, whose saving falls from 4.39x with an 8B generator to 1.38x with a 1B one. The memory profile drives hint quality: removing it costs 24.7 exact-match points (rescaled BERTScore 0.57 to 0.35), while retrieval and a larger generator add nothing on exact match. One 1B decoder can do both, gating from an intermediate layer and generating in the same pass. At its final checkpoint it matches or exceeds the two-model pipelines on automatic end-to-end measures with 1.31-1.76x less wall-clock time than the matched 1B pipeline; across three seeds, its deeper exit ties the separate gate. A human evaluation (1,144 ratings over 32 dialogues) supports the memory effect and rates the single model level with the matched 1B pipeline and below the 8B one. Graded metrics and LlamaPIE's native judge track human ratings more closely than exact match, which we report as a strict lower bound.

---


### 333. [Testimony from Timelines: Evidence-Grounded Significance Testing of Temporal Clinical Hypotheses](https://arxiv.org/abs/2610.40619)

**<font color=#1a73e8>作者：</font>** Chengyang He, Wenlong Zhang, Koduvayur Subbalakshmi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Ask a language model whether sales tend to dip after a product recall, or whether one side effect tends to follow another after a vaccine, and it answers in a fluent sentence that reads like a finding, with no test behind it. Assertions about how events unfold across many cases fill the Web, and each is a temporal hypothesis that only a significance test over the right records can settle. The verifier must specify the null, select the test and decide which records bear on the hypothesis, and any of these choices can go wrong while the conclusion still comes out right. Yet benchmarks for language-model data analysis grade only the conclusion, with the relevant data handed over. We study the problem in health, where a wrong verdict is costly, and present STRATA, a benchmark that grades every decision on the way to a verdict: 8,735 hypotheses over the clinical timelines of vaccine adverse-event reports, with gold plans, evidence sets, p-values and verdicts derived under a released codebook and reproduced by a deterministic oracle. We also propose ART (articulate, retrieve, test), a staged paradigm that exposes each decision as an inspectable output. Extensive experiments with five model configurations show that systems fail mostly at choosing which records count, a verdict-evidence gap that accuracy alone conceals. ART closes most of this gap and brings a 31B open model to within 0.01 of the frontier models under the same paradigm; the frontier models succeed once given the codebook.

---


### 334. [Rethinking Neural Thickets Without Weight Perturbations](https://arxiv.org/abs/2610.40649)

**<font color=#1a73e8>作者：</font>** Nicolas Dufour, Elouan Gardès, Amil Dravid 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen and adding a random bias to its output logits matches or exceeds full-weight perturbations on most reasoning tasks. This suggests an alternative explanation based on output diversity, validation-based selection, and voting. We formalize this view as Perturb-Select-Vote (PSV), a general procedure that generates perturbed predictors, selects high-performing members on a small validation set, and aggregates their predictions.
This interpretation connects Neural Thickets to established inference-time methods, including sampling, self-consistency, and verifier-guided selection. A first-order analysis further shows that small weight perturbations act primarily through their induced logit shifts. We extend this analysis to vision, where logit PSV substantially improves performance under domain shift, including on Earth observation, while full-weight perturbations provide little additional benefit. Together, these results suggest that the gains attributed to nearby weight-space experts can instead be obtained through output diversity, selection, and voting. Logit PSV realizes these benefits with a fully frozen model, providing a simple, training-free alternative to full-weight perturbation ensembles across language and vision.

---


### 335. [Elucidating the Design Space of LM Data Attribution](https://arxiv.org/abs/2610.40655)

**<font color=#1a73e8>作者：</font>** Steven Yu, Sheng-Yu Wang, Kimia Hamidieh 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To diagnose these failures, we explore the design space of LLM data attribution, with a primary focus on evaluation. We introduce the Controlled Attribution Benchmark (CATT) for fact tracing, in which we fine-tune LLMs on entirely fictitious knowledge, providing unambiguous ground truth for attribution. This synthetic setup allows us to systematically alter one dataset configuration at a time, such as document redundancy and lexical distractors. With this configurable evaluation, we demonstrate that redundancy and distractors consistently degrade attribution performance. Rather than proposing a new estimator, we examine two design choices that are underexplored: the loss used to compute gradients and how per-token attribution scores are aggregated into a document score. We find that the true causal evidence within a training document is highly localized, but standard methods dilute this evidence into noise by averaging attribution scores across the entire document. We find that replacing standard cross-entropy loss gradients with the negative log-odds gradients surfaces the critical tokens from other uninformative ones. We can then aggregate only the top token scores to improve ground truth recall by 35 to 72 percentage points across multiple baselines on our diagnostic benchmark. The negative log-odds correction also generalizes to FTRACE-TREX, improving counterfactual retraining performance for every method we test, by up to 4.9x.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 336. [Depth through Recurrence: Towards Ultra-Efficient On-Device ASR](https://arxiv.org/abs/2610.37833)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chen Feng, Tianyi Xu, Ramchalam Kinattinkara Ramakrishnan 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern automatic speech recognition (ASR) systems have achieved remarkable accuracy by scaling model depth and capacity, but at the cost of increased memory, energy, and computational demands. On edge devices where ASR is often most needed, such as watches and glasses, deploying such large models is infeasible due to extremely constrained resources. This raises a fundamental question: can we achieve high representational power in deep ASR models without scaling up parameterization? In this work, we revisit the role of depth and identify layer wise representational dynamics, in which most layers learn functionally similar transformations. Motivated by this insight, we propose a block-recurrent ASR architecture that replaces parameterized depth with a small set of recurrent blocks, each consisting of weight-shared layers, thereby preserving effective depth while drastically reducing model size. Through representation-guided grouping and knowledge distillation, block-recurrent models retain the accuracy of large reference models while using an order of magnitude fewer parameters. Across Open ASR Leaderboard benchmarks, a model with only two shared blocks recovers 97.4% of the accuracy of large models on average. The compact backbone further enables efficient on-device personalization through lightweight MoE-LoRA adaptation, allowing user-specific models to match or surpass the accuracy of general-purpose ASR systems with significantly lower inference cost. By reusing weights across recurrent steps, the proposed architecture reduces memory-access overhead and inference energy consumption. Together, these results show that high quality ASR can be achieved without large parameterization, and that structured recurrence provides a principled path towards ultra-compressed, energy-efficient, and personalized speech recognition on the edge.

---


### 337. [Venus-DefakerOne2: A Vision-Forensics Foundation Model with Broader Coverage](https://arxiv.org/abs/2610.37918)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Chenfan Qu, Yachao Liang, Mingqi Fang 等 30 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world forgery is inherently heterogeneous: it manifests not only as digital manipulation but also as physical spoofing, and is carried not only by images but also by videos. Despite substantial progress, a unified anti-forgery foundation model covering such a broad threat spectrum remains absent. In this paper, we present Venus-DefakerOne2, which substantially extends the forensic capability boundary along both the forgery-form and media-type dimensions. Trained on tens of millions of open-source and in-house samples, it incorporates two key designs. Tide-Style-Tuning alternates LoRA and full-parameter fine-tuning to balance computational efficiency, generalization, and hard-sample fitting while mitigating catastrophic forgetting. Entropy-based Test Adaptation determines the optimal prediction modality by analyzing prediction entropy. Venus-DefakerOne2 achieves new state-of-the-art performance across a comprehensive suite of benchmarks, including DeepFake faces (96.7%), AI-generated images (93.3%), tampered documents (87.6%), manipulated natural images (89.6%), physical spoofs (93.1%), and AI-generated videos (96.0%). It significantly outperforms both specialized expert models and its predecessor, DefakerOne, establishing itself as a powerful and versatile foundation model for binary-decision forensic tasks.

---


### 338. [Are Seismic Foundation Models More Than Glorified Feature Extractors?](https://arxiv.org/abs/2610.38003)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Laura Laurenti, David Liu, Brian Kulis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Earthquake sequences are stochastic on two separated timescales: the seismic waves of any individual earthquake propagate over seconds to minutes, while the earthquakes themselves arrive as a sparse, self-exciting occurrence process, with inter-event intervals from seconds to months. Respecting both scales in one training objective is the open challenge. Foundation models (FMs) for seismic waveforms instead import their learning targets from audio and vision, where every target is computed from a single fixed-length window. Such a window holds one realization of the wave propagation (an earthquake trace), never the occurrence process that decides when earthquakes happen. We develop nine model designs sharing one Mamba encoder-decoder, trained on a fixed corpus of 3M windows, varying the self-supervised objective, quantization bottleneck and mixer; the two key comparisons are architecture-matched, varying the objective alone. Each checkpoint is evaluated frozen on three downstream tasks. Varying the target redistributes downstream skill rather than raising it, and no checkpoint wins everywhere. Adding masking pressure to our strongest classifier re-specializes it rather than making it a generalist: it gains 6.9 points of few-shot P-wave picking precision and loses 9.6 points of few-shot classification accuracy. By the standard imported from language and vision, these models are feature extractors rather than FMs. Controls on capacity, architecture, and domain proximity do not explain why skill moves rather than rises. Against task-specific baselines the advantage is regime-dependent: our checkpoints beat them few-shot on classification and ground-motion prediction, and trail them on full data. We argue the binding constraint is the target, and that settling the question requires a learning target defined across events, the timescale that makes seismicity stochastic in the first place.

---


### 339. [HotPOT: Operator Transformer with Heterogeneous Physics Experts for Large-Scale PDE Pre-training](https://arxiv.org/abs/2610.38218)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jiayi Li, Guancheng Zhou, Yisi Luo 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large-scale PDE pre-training trains a single model on the data from multiple partial differential equations (PDEs). However, adding heterogeneous PDEs with different governing equations, physical variables, and variable interactions does not always improve predictive performance across tasks. Existing PDE mixture-of-experts models mitigate cross-task interference through learned routing, but typically use homogeneous expert architectures, making it difficult to directly reflect differences in state evolution across equations. We introduce HotPOT, an operator transformer with heterogeneous physics experts for large-scale PDE pre-training. HotPOT uses a shared encoder to capture information common across PDEs, while each PDE family uses a neural-numerical expert that pairs a learnable predictor with a fixed numerical update containing no trainable parameters. Each predictor outputs the quantities required by its paired numerical update, which then computes the next state. This design allows different PDEs to share a common encoder while retaining their own learnable predictors and numerical updates. Experiments across five PDE families and six settings show that HotPOT outperforms MoE-POT in all 24 matched-scale comparisons before and after fine-tuning, reducing rollout error by 50.7% on average. Notably, the 17M model also surpasses substantially larger MoE-POT models, and the performance gains extend to zero-shot prediction under unseen physical conditions. Code is available at this https URL.

---


### 340. [Value Probes: Learned Value Functions for Beam-Search Red Teaming](https://arxiv.org/abs/2610.38526)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jonathan F. Jao, Andrew Kyle Lampinen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated red-team auditing of language models is an important way to evaluate safety-relevant behaviors. These audits implicitly search a tree of possible conversation pathways: at each turn an auditor model decides which conversation to continue, and an LLM judge scores the dialogue. We emphasize that this auditing procedure is a Markov decision process, where states are the conversation history, actions are candidate responses, and rewards are judge scores for the target behavior. By adopting this perspective, we introduce two major improvements to auditing. First, we propose adopting beam search for the audit rather than relying on the auditor alone. We then interpret the problem of finding states that are likely to lead to problematic behavior as value estimation. Surprisingly, we show that this value function can be estimated by linear probing from the target model's activations to predict discounted future rewards - a method we term "Value Probes." By using Value Probes as a heuristic in our beam-search audit, we are able to substantially improve auditing success. Across 18 target behaviors and 3 scales of models, our approach raises peak audit scores by roughly 50% compared to (token-matched) standard auditing approaches. Furthermore, we show that Value Probes can be fit using off-policy data from smaller models. We also ablate individual components, and show that our method offers a comparably-performant and more efficient alternative to more expensive language model follow-ups. We hope these methods will improve language model auditing and lead to safer models.

---


### 341. [SpectralTF-MAE: A Pre-trained Spectral Foundation Model for Tokamak Fusion Plasma Diagnostics](https://arxiv.org/abs/2610.38593)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiao Wang, Zhijie Lu, Duoqing Yang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Spectroscopic diagnostics provide rich information for characterizing plasma states in tokamak fusion experiments, while existing learning-based approaches are often designed for individual tasks and rely heavily on labeled data. In this work, we propose SpectralTF-MAE, a self-supervised spectral foundation model for tokamak plasma diagnostics. The model is pretrained on paired charge-exchange recombination spectroscopy (CXRS) and X-ray crystal spectroscopy (XCS) measurements through masked spectral reconstruction. To better capture diagnostically important spectral structures, we introduce a peak-aware masking strategy together with a peak-enhanced reconstruction objective, encouraging the model to focus on characteristic spectral regions. A shared Transformer encoder is employed to learn transferable representations across different diagnostic modalities. The pretrained model is further adapted to several downstream tasks, including plasma-parameter prediction, cross-diagnostic spectral generation, and spectral peak analysis. Experiments on EAST diagnostic data demonstrate that the proposed framework achieves competitive performance across different tasks and consistently benefits from self-supervised spectral pretraining. These results indicate the potential of SpectralTF-MAE as a general and transferable representation learning framework for plasma spectroscopic diagnostics.

---


### 342. [A 211K Parameter Foundation Model: Genetic Prompting in Neural Cellular Automata](https://arxiv.org/abs/2610.38776)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** John Kalkhof, Niklas Ihm, Daniel Kirste 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The scale of modern foundation models enables broad task generalization. In medical imaging, where segmentation demands vary widely across clinical contexts, such flexibility is invaluable. But current models, such as SAM trade adaptability for scale, locking their utility behind high-end infrastructure and leaving behind the low-resource environments most in need of diagnostic support. To bridge this gap, we introduce Foundational-NCA, a lightweight foundation model capable of adapting to a wide range of medical segmentation tasks without retraining. Built on Neural Cellular Automata (NCA), Foundational-NCA incorporates gradient-based learning with genetic optimization over a latent task space, using a compact task vector to guide predictions. This enables dynamic adaptation via a genetic prompt mechanism, allowing the model to generalize across tasks while keeping the parameter count magnitudes lower at just 211 thousand, compared to SAM-based models with 38.9 to 636 million parameters. We evaluate Foundational-NCA on 15 trained and 6 entirely unseen segmentation tasks from the TotalSegmentator dataset, achieving an average Dice score of 84.5% on known tasks and 60.4% on unseen ones. These results demonstrate that task generalization is possible in ultra-compact models, laying the groundwork for resource-efficient, deployable foundation models in clinical environments where infrastructure is limited. By reducing model size by over 180 times, Foundational-NCA takes a step toward a more equitable future for medical AI, one where powerful tools are within reach of every healthcare setting.

---


### 343. [FlipJev: Fast Black-Box Red Teaming Finds Universal Adversarial Suffixes for Typed Decision Models](https://arxiv.org/abs/2610.38895)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Xiaogeng Liu, Xinyan Wang, Chaowei Xiao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Typed decision models are an emerging class of language models that make decisions instead of generating free-text responses. They answer in a single fast and cheap query and are increasingly used, including in security-sensitive tasks. However, red teaming of these models leaves two gaps: existing adaptive attacks do not use their speed, and few studies have searched for universal adversarial examples. We fill both gaps on Jev, the representative typed decision model, with a quick black-box query-based attack that calls no attacker language model. We conduct extensive experiments on 12 datasets with different data types and application scenarios. The results show that Jev resists common prompt injections: no strategy changes a correct answer in 10,240 paired tests. In contrast, our attack finds short suffixes that flip confident answers within minutes. These suffixes are universal: one suffix per dataset flips 43% of unseen documents. Because typed decision models, unlike classic NLP models, can serve many tasks, we test whether these suffixes transfer across tasks. We find that one suffix generated from one task can flip 90-100% of the samples in other tasks. We therefore believe the evaluation of typed decision models must include strict adaptive attacks to fully reveal their robustness.

---


### 344. [Where to Learn and How Far to Roll Out: Efficient Adaptive Training for GUI Agents](https://arxiv.org/abs/2610.39251)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yuxiang Chai, Quyu Kong, Panrong Tong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Trajectory-level GRPO is a common approach for training multi-step GUI agents, but repeatedly rolling out complete trajectories from the task root can be inefficient: task-level rewards provide coarse supervision over which intermediate decisions require improvement, while already-mastered prefixes are repeatedly re-executed before reaching difficult states. We introduce a two-stage adaptive training framework that jointly addresses where to learn and how far to roll out. We first construct reusable intermediate checkpoints from successful expert trajectories and select informative pivots using action disagreement, which measures uncertainty directly from sampled GUI actions. Stage I performs one-step RL at these pivots to improve uncertain local decisions. Stage II then progressively expands policy responsibility through adaptive Local, Suffix, and Root training according to task progress. Recoverable checkpoints enable repeated training from intermediate states without replaying the preceding trajectory. Across MobileGym and CUA-Gym-Hub, our method reduces environment interaction by 56-61% relative to Vanilla GRPO while improving task performance, demonstrating that jointly allocating training across states and rollout ranges can substantially improve GUI-agent RL efficiency.

---


### 345. [TaxoMFM: A Taxonomy-Aware Foundation Model for the Human Gut Microbiome](https://arxiv.org/abs/2610.39316)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Haochen Xue, Anastasia Godneva, Yulong Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing gut microbiome foundation models typically use flat taxon representations, limiting their ability to exploit known taxonomic hierarchies. We introduce TaxoMFM, a microbiome foundation model that integrates taxonomic structure into self-supervised learning. TaxoMFM jointly learns abundance patterns across taxonomic ranks and relative proportions within groups through taxonomy-aware encoding and hierarchical compositional reconstruction. We further construct TaxoGut-HPP, comprising 100,806 gut microbiome profiles from 231 source cohorts and covering 40 classification and 8 regression tasks. TaxoMFM achieves competitive performance across disease, gut health, host trait, and liver ultrasound phenotype prediction. In cross-cohort zero-shot transfer, where target cohorts are excluded from both pretraining and downstream adaptation, TaxoMFM achieves AUROCs of 0.838, 0.736, and 0.722 for colorectal cancer, type 2 diabetes, and inflammatory bowel disease, respectively. Further analyses show that TaxoMFM recovers community changes across taxonomic scales, while preserving community information and producing consistent representations under database updates and species-vocabulary shifts. Our code is available at this https URL.

---


### 346. [Before the Next Rollout: Diagnosing Skill Utility Shifts from Policy Updates](https://arxiv.org/abs/2610.39358)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yifan Wang, Zhenyi Gai, Yiwen Zhao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Skill-evolution methods typically analyze execution trajectories to guide agent skill refinement. However, policy updates can change the behavioral effects and marginal utility of an unchanged skill. Attribution based on earlier trajectories may therefore no longer reflect the skill's contribution under the updated policy. Moreover, trajectory failures can arise from multiple factors, making individual skill contributions difficult to isolate. We evaluate whether policy-update signals contain predictive information about changes in skill marginal utility. At fixed contexts from pre-update training rollouts, we measure how policy updates change the contrast in token preferences between skill and control conditions. Combining these interaction shifts with advantage estimates yields reward-directed readouts for diagnosing utility changes. The readouts reuse existing training rollouts and require only forward passes for single-step action scoring, without additional post-update rollout evaluation. Our experiments show that policy updates can alter skill marginal utility and that policy-update readouts carry diagnostic information for identifying skills with declining utility. Integrating readout-guided prioritization into skill evolution improves downstream performance while reducing policy and editor token consumption.

---


### 347. [Interpretable by Design Tabular Prediction via In-Context Local Linear Learning](https://arxiv.org/abs/2610.39506)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ran Eisenberg, Steven Berger, Ofir Lindenbaum  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In-context learning (ICL) lets tabular foundation models make predictions without dataset-specific training or fine-tuning. These models achieve strong predictive accuracy, but interpreting how individual features contribute to the prediction remains difficult. In biology, for example, feature contributions can help identify biomarkers or risk genes. Post-hoc interpretability methods assign feature importance scores, but these scores do not indicate what the model actually uses and can lead to explanation errors. We introduce TICL$^3$ (Tabular In-Context Local Linear Learning), an interpretable-by-design predictor that uses a tabular foundation model to guide a simple linear prediction rule. TICL$^3$ first learns a shared linear model to capture dataset-level feature effects. Then, for each query, it retrieves similar training samples using representations from the foundation model and fits a second linear model to the residuals in that neighborhood. The shared model captures broad effects, while the local model corrects errors among similar samples. Their combined coefficients determine each feature contribution to the final query-specific linear score, so the same model makes and explains the prediction. Across 386 classification benchmark-dataset evaluations, TICL$^3$ trails TabICLv2 by 1.1 percentage points and outperforms CatBoost in 266 evaluations. It improves average support F1 over MAPLE by 4.7 points and achieves the best performance on both real-data selected-feature utility metrics.

---


### 348. [SelfThinker: Self-Evolving Reasoning via Reliability-Verified Intrinsic Visual Thoughts](https://arxiv.org/abs/2610.40115)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhangquan Chen, Ruqi Huang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Unified multimodal models can both generate and understand images within a single set of weights, offering an opportunity to use image synthesis as training supervision for visual comprehension. However, existing visual chain-of-thought methods rely on human-annotated helper images during training and require slow image generation at test time. We present SelfThinker, the first self-evolving framework that turns a unified model's self-generated visual thoughts into stronger understanding without human image annotations. Given a visual problem, SelfThinker samples candidate helper images from its generation pathway and uses its frozen understanding pathway to score each candidate via conditional pointwise mutual information. High-utility visual thoughts then refine the generator via flow matching and serve as privileged teacher context for on-policy self-distillation. At inference, SelfThinker reasons directly from the original image in text without generating intermediate images. Although trained only on small synthetic visual-search and navigation datasets, SelfThinker transfers broadly to natural-image and spatial benchmarks, raising the seven-benchmark average of ThinkMorph-7B from 52.7 to 64.0 (+11.3 points). Controlled image-perturbation probes further show that SelfThinker surpasses ThinkMorph-7B by up to 40.4 points and its pretrained BAGEL-7B backbone by up to 23.2 points across fine-grained and spatial perception tasks. Our code is available at this https URL.

---


### 349. [Distributional Reward Calibration and Budget-Neutral Credit Assignment for Multimodal RLVR](https://arxiv.org/abs/2610.40250)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Lang Chen, Zongxin Xu, Borui Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We revisit advantage estimation in Group Relative Policy Optimization (GRPO) and observe that any token-level advantage admits a two-stage factorization: a \emph{sample-level baselining} step that converts scalar verifier rewards into a comparable sequence-level signal, and a \emph{token-level credit assignment} step that distributes that signal over the trajectory. Existing estimators typically address only one of these stages: affine baselines preserve the shape of each task's reward law, so heavy tails and binary cliffs propagate into the gradient, while token-level credit rules tie the size of each token's update to raw confidence scales and need not conserve the total credit issued by the verifier. We propose \textbf{TACE} (Two-stage Advantage and Credit Estimation), a two-stage estimator that addresses both stages. At stage~(S1), we replace linear standardization with a one-dimensional optimal-transport map to a standard normal, which gives a common population reward law across tasks and caps finite-sample outliers deterministically. At stage~(S2), we rank-calibrate a stop-gradient evidence contrast within each trajectory and renormalize the clipped token weights to have mean one, so credit is redistributed across tokens while its total mass and sign are conserved. We prove population-level inter-task moment equity, a deterministic tail bound, and mass-conservation, boundedness, and sign-anchoring properties that affine baselines and unnormalized token weights do not satisfy. On a multimodal reasoning suite, TACE obtains the strongest results on a majority of the benchmarks but does not dominate every setting.

---


### 350. [Towards fNIRS foundation models: A curated corpus of 67 public datasets with channel positions in MNI space](https://arxiv.org/abs/2610.40277)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Santiago Posso-Murillo  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Brain foundation models have transformed medical artificial intelligence and computational neuroscience by reducing the reliance on task-specific data through large-scale pretraining. While they have been successful with non-invasive neuroimaging data, their adoption in functional near-infrared spectroscopy (fNIRS) has lagged due to the limited size and heterogeneity of public datasets, which are collected under varying protocols, devices, and sensor configurations. In addition, no single fNIRS dataset is comparable in size to the largest datasets in functional magnetic resonance imaging (fMRI), electroencephalography (EEG), or magnetoencephalography (MEG). The fNIRS datasets are also spread across different platforms and often have insufficient information, or lack the protocols that would make them easier to use. Given the advances in EEG foundation models that enable flexible modeling across diverse EEG montages, we curated 1,955 hours of fNIRS data from 67 public datasets spanning 2,798 participants, representing the largest fNIRS curation effort to date. The curated data include oxygenated (HbO) and deoxygenated (HbR) hemoglobin signals along with the three-dimensional position of every channel in the standard space of the Montreal Neurological Institute (MNI), which makes positions comparable across datasets. We release dataloaders that handle each dataset automatically, along with the minimal preprocessing pipeline used to prepare the data, at this https URL. This work aims to facilitate the future development of foundation models for fNIRS.

---


> [!TIP]
> 当前位于：**301-350**（第 7/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | **301-350** | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
