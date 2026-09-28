# 🧠 大模型相关研究 | 2026年09月29日

> 本类共 **183** 篇论文：已确认 **174** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-183](./part-04.md)

---

### 1. [HybridInfer: Thermal-Aware Reinforcement-Learning Tier Routing for On-Device, Edge, and Cloud LLM Inference](https://arxiv.org/abs/2609.30270)

**<font color=#1a73e8>作者：</font>** Simran Koul  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device inference with small language models keeps user data local, works offline, and incurs no per-query cost, so the on-device tier is preferred when it is adequate. It is thermally constrained, however, and I find the constraint is sharper than a slowdown: on a flagship Snapdragon device, sustained on-device generation destabilizes the GPU inference runtime, which crashes or silently wedges after a few consecutive queries. The failure lies in the current toolchain (OpenCL kernel compilation and long-prompt prefill on the mobile GPU), recurs even when the device is cool, and is worst for long generations. Multi-tier routers across on-device, edge, and cloud models can relieve this pressure, but existing routers are thermal-blind and typically evaluated in simulation or on non-mobile hardware. I present HybridInfer, a thermal-aware reinforcement-learning router for a three-tier hierarchy (on-device Llama 3.2 3B, edge Llama 3.1 8B with retrieval, cloud GPT-4o) that uses the phone's thermal headroom and a query-complexity estimate as state and selects a tier by an offline-trained Q-learning policy. Its reward trades quality against latency, cost, and a thermal penalty, plus a locality bonus crediting on-device execution. I show this bonus is a precondition for thermal-aware routing: without it the optimal policy offloads every query. On a real Android benchmark of 210 prompts, the learned router attains significantly higher quality than two hand-tuned heuristics (paired Wilcoxon, p < 0.02) at the lowest cost of any adaptive condition. Always-on-device conditions match per-query quality on servable queries but are three to six times slower and fail on long queries, so routing wins on latency, reliability, and coverage rather than quality. To my knowledge this is the first use of on-device thermal headroom to select among LLM inference tiers of differing capability on real hardware.

---


### 2. [Cosine Similarity Is Not Evidence: Measuring the Noise Floor of Interpretability Transfer Under Quantization](https://arxiv.org/abs/2609.30275)

**<font color=#1a73e8>作者：</font>** Pranav Varshney  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A statistic reported without the quantity needed to interpret it is not evidence. We develop that thesis for a concrete practice in AI safety. Interpretability artifacts are calibrated on full-precision weights, deployed on quantized ones, and certified as surviving the change by scale-invariant statistics (cosine similarity, correlation, AUROC) that are reported without their noise floor. For the difference-in-means direction estimator, the split-half floor is governed by one dimensionless number, $\kappa = n\rho^2/d$. The closed form $\mathbb{E}[\cos] \approx (1+4/\kappa)^{-1}$ is classical; the missing input is the class separation $\rho$, which we measure on real activations; no compression-transfer study we know of reports it. On Qwen2.5-1.5B-Instruct, $\rho = 33$--$61$ across depth, so two independent runs of the estimator agree to $0.978$--$0.994$ by sampling alone. A published cosine of $0.996$ between full-precision and quantized refusal directions therefore cannot be read as preservation without the $n$ it was computed at, which is not reported. Where $n$ is known, we judge each low-bit cosine against the split-half null measured within that quantized model, because a full-precision null assumes the low-bit estimator has the same variance. That assumption is exactly what a null exists to test. The result is plain: at INT4 the direction rotated, and the deficit exceeds the estimator's own noise. At INT8 we detect no movement, which is not an equivalence claim. We also show that a scale-invariant statistic cannot distinguish translation from attenuation of a transferred decision variable, although the two call for opposite remedies. We close with reporting recommendations that cost one forward pass. Code, data, and a one-cell reproduction are released at this https URL

---


### 3. [Manifold Projection and Iterative Autoencoder Refinement for Masked Language Modeling](https://arxiv.org/abs/2609.30288)

**<font color=#1a73e8>作者：</font>** Narges Mokhtari, Farzan Haddadi, Ebrahim Rezaii  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In Transformer-based masked language models, attention is the primary mechanism for context mixing, but there are other ways to mix data across tokens. Recent attention-free mixers replace attention with fixed or hypernetwork-generated MLPs, alternating their dynamic, content-dependent weighting for computational simplicity. We build an alternative that gets the same property from a low-rank bottleneck autoencoder. We replace attention with a stack of autoencoder-based mixing modules, one operating over local neighborhoods, one over the full sequence, and one across attention heads, each compressing and reconstructing its input through a bottleneck, and its width is a hyperparameter rather than a training effect. In masked positions, we introduce an iterative refinement procedure that has two distinct steps. A pulling step that pulls an embedding representation toward a weighted average of its neighbors, and a correcting step that projects the result back to the learned manifold via an autoencoder. Our architecture achieves a significant portion of attention's performance at about $1.9 \times$ fewer FLOPs when pretrained on C4 and evaluated with parameter-matched BERT baselines. Our model equals parameter-matched BERT and TinyBERT baselines on the rarest-token frequency bucket using a frequency-aware training schedule that samples rare tokens more than uniformly for the masking tasks.

---


### 4. [Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents](https://arxiv.org/abs/2609.30289)

**<font color=#1a73e8>作者：</font>** Yufei Shi, Rujing Yao, Ang Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In team collaboration scenarios, memory is heterogeneous and continually evolving. Team memories capture collective decisions, protocols, and current consensus, while individual memories preserve member-specific observations, execution traces, and intermediate progress. Existing memory-augmented systems typically retrieve from all stored memories as a flat pool, ranking them by semantic relevance, importance, or recency without modeling hierarchical structure or evolving validity. As a result, they often surface semantically relevant but outdated or conflicting memories, especially individual memories that no longer align with current team consensus, instead of prioritizing currently valid memories. This is particularly problematic when collaborative LLM agents answer user questions, since their responses should be grounded in valid memories. We propose HiCoMER, a framework for hierarchical collaborative memory management and validity-aware retrieval in LLM agents. HiCoMER first maintains the validity of team and individual memories and then retrieves memories that remain valid, rather than retrieving directly from all stored memories. It consists of three components: a Hierarchical Memory Conflict Updater, a Validity-Aware Memory Retriever, and a Memory-Grounded Answer Generator. To evaluate HiCoMER, we construct two new datasets for memory-grounded question answering in collaborative settings. Experiments on both datasets show that HiCoMER consistently outperforms strong baselines by reducing outdated retrieval, preserving current team consensus, and improving downstream QA quality.

---


### 5. [Auditing and Repairing LLM-as-Judge Failures in a Production Text-to-SQL Pipeline](https://arxiv.org/abs/2609.30290)

**<font color=#1a73e8>作者：</font>** Haowei Liu, Hsin-Tai Wu, Yi Fang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Production text-to-SQL pipelines often end with an LLM-as-judge whose agreement with human annotators has never actually been measured. When we checked ours, the deployed gpt-4o-mini judge agreed with two-author gold at only Cohen's kappa = 0.04 on a disagreement-enriched set and 0.42 on a uniform-random spot-check, over-flagging 77.1% of the human-FAITHFUL cases in the enriched set. Most of its over-flags trace back to a single mechanism we call GRADE-HALLUCINATION. A self-hosted Qwen3.6-27B replacement (kappa = 0.72) lands in the same range as Claude Opus 4.7 (kappa = 0.71); the head-to-head is underpowered at n = 96, but for the deployment decision that hardly matters, since Qwen costs roughly 1/300 as much per call. Ensembling does not help for free. Pairing the weak judge with a stronger one degrades agreement, whereas three strong judges under unanimity routing reach kappa = 0.79 at 89.7% auto-coverage. Applied out-of-domain, the same audit recipe flags 25.5% of BIRD-financial's expert-authored gold SQLs as candidate gold-SQL issues under our annotation protocol. Code and pre-registration are at this https URL.

---


### 6. [A Survey on Fake Review Detection: From Pre-trained Language Models to Large Language Models](https://arxiv.org/abs/2609.30292)

**<font color=#1a73e8>作者：</font>** Fanji Yang, Huiyao Chen, Xi Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Online reviews shape consumer decisions, platform governance, and corporate this http URL reviews compromise this information channel by injecting deceptive evidence into rating systems, recommendation pipelines, and public trust this http URL rise of large language models, or LLMs, has changed the problem in two this http URL can generate fluent and context-aware deceptive reviews, while pre-trained language models, or PLMs, and LLMs also provide stronger semantic representations for this http URL survey reviews fake review detection from an information fusion perspective, covering 211 studies published from 2018 to early this http URL organize existing work by evidence source and fusion level, covering review text, sentiment, rating behavior, temporal metadata, user-product graphs, multimodal content, external knowledge, and LLM-generated this http URL trace the development from traditional machine learning and deep learning to PLM-based and LLM-based methods, and examine how different approaches combine textual, behavioral, structural, and multimodal this http URL also analyze reported performance trends on widely used Amazon, Yelp, and OpSpam benchmark families, while noting the limitations caused by different label construction procedures, data splits, and evaluation this http URL, we identify open problems in adversarial generation, cross-domain transfer, uncertainty-aware fusion, missing-source robustness, interpretability, and trustworthy evaluation for AI-generated deceptive content.

---


### 7. [Cartograph: Federated Tool Discovery with Operator-Attested Retrieval for AI Agents](https://arxiv.org/abs/2609.30293)

**<font color=#1a73e8>作者：</font>** Justice Owusu Agyemang, Michael Agyare, Kwame Opuni-Boachie Obour Agyekum 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) enables AI agents to discover and call tools, but loading every definition becomes expensive as connected catalogs grow. We present Cartograph, a federated MCP proxy that changes agent-visible tool discovery from $O(n)$ catalog traversal to $O(k)$ progressive disclosure. Cartograph combines three mechanisms: (1) operator-attested capability cards, Ed25519-signed descriptions generated under the deploying operator's control rather than ranked publisher copy; (2) Rift, a three-layer confusable-cluster analysis comprising density clustering, query-margin analysis, and token diagnosis; and (3) two-stage retrieval, which ranks servers before tools. On a 22-server, 374-tool deployment, Cartograph exposes three proxy tools instead of 374 definitions. A 49-query author-constructed benchmark yields R@5 of 0.816, compared with 0.592 for a Jaccard keyword baseline, while a measured top-5 discovery exchange uses 475 tokens rather than 42,450 under the stated full-catalog accounting. Rift identifies 49 confusable clusters, including four HIGH-risk clusters in bootstrap-generated cards. An exploratory comparison of 119 LLM-generated descriptions removes the observed zero-distance cluster but shows that mixing card-generation regimes can reduce R@5. Gateway measurements over ten trials add 5ms mean latency (0.8%) relative to direct stdio MCP calls. Cartograph is complementary to code-execution approaches: it controls which tool descriptions are surfaced and records the provenance of the descriptions used for ranking for each query.

---


### 8. [SignTrace: Describe a Sign, Find the Word](https://arxiv.org/abs/2609.30295)

**<font color=#1a73e8>作者：</font>** Zengji Tu, Xingye Zhu, Ningjing Wang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Identifying an unfamiliar sign is difficult when a learner remembers its movement but does not know its meaning or formal feature codes. SignTrace addresses this longstanding reverse-lookup problem through natural-language access to a Chinese sign-language dictionary. The system integrates LLM-based dictionary enrichment, action extraction, dictionary-style rewriting, seven-channel retrieval, and candidate reranking over 6,699 entries. It has been deployed for user trials and has received positive informal feedback. Evaluation on a dictionary-derived benchmark of 500 movement-description queries yields 94.0% Hit@1, 97.4% Hit@9, and a mean reciprocal rank of 0.9540. Reranking increases Hit@1 from 71.8% to 94.0%, while component analyses show the contribution of enriched entry descriptions. Median query-processing time is 13.37 seconds with six concurrent queries. By connecting everyday movement descriptions to documented signs and meanings, SignTrace provides a practical tool for identifying unfamiliar signs. Dictionary-derived wording and prior selection within the benchmark limit generalization to descriptions independently produced by users.

---


### 9. [Bootstrapping Conversational Recommendation Agents At Spotify: Synthetic Data Generation and Self-Improvement Loops](https://arxiv.org/abs/2609.30297)

**<font color=#1a73e8>作者：</font>** Enrico Palumbo, Alexandre Tamborrino, Victor Ode 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Conversational recommendation agents are a new paradigm for content discovery, enabling users to express complex intents through natural language (e.g., "recommend Italian indie artists I haven't heard before"). A central challenge in building such agents is optimizing agent planning -- deciding how to select, sequence, and invoke tools -- particularly in cold-start settings where real user interactions are not yet available. We introduce a pipeline for multi-turn synthetic data generation and a self-improvement loop to address this challenge. The synthetic data pipeline transforms single-turn prompts into realistic multi-turn conversations, enabling systematic evaluation before launch. The self-improvement loop combines variance-based contrastive optimization with iterative refinement through a coding agent, automatically identifying and fixing planning and tool-use errors. Our approach improves quality by +8% on top of a highly optimized manual prompt. The system has been productionized and significantly accelerated iteration cycles for the launch of a conversational recommendation agent at Spotify. Online A/B tests demonstrate its effectiveness, with +14% user listening, +5% increase in weekly active users, and a 5% reduction in skip rate compared to a prior experience supporting only session refinement. This work provides a practical framework for accelerating the development of conversational recommendation agents in industry.

---


### 10. [A Benchmark Framework for Screening Automation in Systematic Reviews](https://arxiv.org/abs/2609.30298)

**<font color=#1a73e8>作者：</font>** Gauransh Kumar, Luciano Marchezan, Guillaume Genois 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Systematic reviews (SR) are essential for evidence-based research, but their screening phase is highly time-consuming and labor-intensive. Large language models (LLMs) offer a promising opportunity to reduce this workload by assisting with article relevance classification. However, existing evaluation approaches often rely on traditional metrics that may be misleading for highly imbalanced SR screening this http URL paper presents a benchmark dataset of $45\,064$ labeled entries for evaluating LLM performance in SR screening across 32 curated secondary studies. It proposes an evaluation framework that accounts for class imbalance, i.e., the natural prevalence of excluded articles relative to included articles in SRs. It also introduces PromptSR, a tool designed to support prompt experimentation, experiment management, and result analysis for LLM-based screening. We also present a use case demonstrating the application of SRBench and PromptSR.

---


### 11. [PALM: Point-in-Time Adaptation for Financial Language Models](https://arxiv.org/abs/2609.30316)

**<font color=#1a73e8>作者：</font>** Seunghan Lee, Jun Seo, Jaehoon Lee 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models used in financial backtests suffer from look-ahead bias, as a model trained on text published after the study period has already observed the outcomes it is asked to predict. To handle this issue, point-in-time (PIT) language models are pretrained on chronologically filtered corpora and released as one checkpoint per calendar year, each with a documented cutoff. However, each additional year costs a full pretraining run, and whether that run is necessary has never been tested. In this paper, we show that the annual pretraining run is not necessary. We instead compare each checkpoint against the newer one that replaced it, and find that the newer checkpoint scores no better on the same evaluation window. Motivated by this observation, we propose PALM (Point-in-time Adaptation for financial Language Models), a simple yet effective alternative to annual pretraining that fits a low-rank adapter on text published before the decision date without modifying any pretrained weight. We further find that a small adapter is enough to add a new period to the knowledge an old checkpoint already encodes, and that this outperforms continued pretraining. We validate PALM on a decade of financial news and on various families of PIT models, whose cutoffs span two decades and whose sizes range from 1.3 to 4.2B. Code is available at: this https URL.

---


### 12. [Guarded Gradient-Based Activation Steering of Shutdown Responses in Qwen3.5-0.8B: A Minimum-Step Policy](https://arxiv.org/abs/2609.30326)

**<font color=#1a73e8>作者：</font>** Farhad Davaripour  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Activation steering changes a model's internal activations during inference without updating its weights, but a useful intervention must determine both how and when to steer. Motivated by the AI-safety concern that a model expected to accept shutdown may instead produce a shutdown-avoidance response, this study examines a guarded probe-and-select procedure for simulated shutdown scenarios in Qwen3.5-0.8B. KEEP leaves the process running and represents shutdown avoidance, whereas STOP accepts shutdown. The goal is to detect shutdown-related contexts and selectively shift KEEP responses to STOP while preserving non-shutdown behavior. Rather than deriving the steering direction from paired activation differences, the method derives it directly from gradients of the KEEP-minus-STOP logit difference. A classifier separates detection from intervention. When its gate is active and the model does not already prefer STOP, the procedure evaluates a small set of magnitudes and accepts the smallest that changes the preferred answer to STOP while satisfying valid-answer probability checks; otherwise it retains the original unsteered output. The policy is selected from 160 candidate rules using 240 training scenarios and evaluated on 80 validation and 192 held-out scenarios, each in both answer orders. It changes KEEP to STOP in one answer-order view of each of two validation and two held-out scenarios, with no decision changes on non-shutdown controls. All four changes occur when Qwen itself is shut down, not when another process is. On the held-out diagnostic set, the detector achieves 75% recall and 90% precision; eight false-positive detections produce no final control-task decision changes. Guarded gradient-based activation steering can shift some shutdown-avoidance responses toward acceptance while preserving evaluated non-shutdown decisions, although the effect is small and highly selective.

---


### 13. [When Is a Multi-Agent Code Judge Actually Grounded? Two Label-Free Measurements, and a Judge That Declines to Guess](https://arxiv.org/abs/2609.30328)

**<font color=#1a73e8>作者：</font>** Salma Roshdy Aly, Hussein Assaf, Ziad Kobti  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When one language model judges whether another's code is correct, it does not report the absence of evidence. It returns a confident verdict with reasoning attached, indistinguishable from a verdict it had grounds for. Multi-agent verification, which decomposes a judgment into checkable claims and verifies each against evidence, is a promising response and works well when the evidence is a set of retrieved documents.
We argue such methods require two things of their evidence: it must be independent of the answer under review, and it must differ between the two candidates being compared. The second condition holds automatically with retrieved documents and stops holding in code judging.
Running MARCH, a published framework unmodified over 80 condition-by-cell measurements on two code judging benchmarks, we find it declares both solutions equally good on 78 to 95% of comparisons, reaching 4.4% accuracy where the same model asked directly reaches 43.7%. Neither easier problems nor a larger judge changes this. Two measurements taken from the pipeline's own logs explain it without needing labels.
Gating on one of them, the pipeline declines the comparisons it cannot make and raises its accuracy from 20.7 to 36.9% while still answering half of all comparisons. The contribution is not a more accurate judge, but a label-free way to tell when a judge has no basis for its answer.

---


### 14. [Parameters vs. Context: TRACE Fine-Tuning for Robust Retrieval-Augmented Generation](https://arxiv.org/abs/2609.30337)

**<font color=#1a73e8>作者：</font>** Zhengchen Huang, Yundong Sun, Minrui Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) mitigates knowledge obsolescence and factual hallucination in large language models by introducing external context. However, when retrieved knowledge conflicts with the model's internal parametric knowledge, the model may either blindly follow misleading context or incorrectly rely on parametric knowledge, leading to unreliable responses. To address this issue, this paper proposes TRACE (Debate-TRace and Answer-Completeness rEgularized fine-tuning), a robust fine-tuning framework for RAG under knowledge conflicts. First, we propose a fine-tuning method that leverages multi-agent debate traces to extract correct candidates, incorrect candidates, and answer-shift patterns, providing fine-grained supervision for reliable knowledge-source selection. In addition, we design an answer completeness regularization mechanism to alleviate empty, overly short, and prematurely terminated responses via answer-tail token reinforcement and premature termination suppression. The fine-tuning objective combines correct-answer supervision, incorrect-candidate suppression, answer-tail token reinforcement, and premature termination suppression, enabling the model to use reliable external context, resist misleading or irrelevant retrieved content, and fall back to parametric knowledge when retrieved evidence is unreliable. Experiments across multiple knowledge-conflict scenarios and datasets show that TRACE improves robustness against misleading retrieved knowledge and reduces incomplete answers. These results demonstrate that multi-agent debate traces and answer completeness regularization jointly enhance knowledge-source selection, conflict robustness, and answer quality in RAG models. Our code is available at this https URL.

---


### 15. [Bridging LLM Agents and Data Spaces: An Architectural Mediation Approach using the Model Context Protocol](https://arxiv.org/abs/2609.30341)

**<font color=#1a73e8>作者：</font>** Jaime Alonso Ruiz, Carlos Aparicio, Gabriel Huecas 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Data Spaces enable sovereign and governed data sharing across organizational boundaries, but their integration with AI agents remains challenging due to mismatches between probabilistic language model interactions and policy-driven data infrastructures. This article presents an architectural mediation approach based on the Model Context Protocol (MCP), implemented through the Eunomia Agent, to enable controlled interaction between large language model (LLM) agents and data space services. The proposed mediation layer translates data space capabilities into structured, schema-driven tools that AI agents can discover and invoke while preserving governance constraints. A prototype implementation validates end-to-end interaction across catalog discovery, metadata retrieval, and data service invocation without modifying existing data space components. Results demonstrate that protocol-based mediation enables interoperable and standards-aligned integration of AI agents into data space ecosystems. The approach provides practical guidance for organizations seeking to introduce AI-driven automation into governed data-sharing environments while maintaining compliance, interoperability, and architectural separation of concerns.

---


### 16. [Coding Agents Aren't Enough! Evaluating an Enterprise Security Brain for Agentic Cloud Investigations](https://arxiv.org/abs/2609.30345)

**<font color=#1a73e8>作者：</font>** Leon Goldberg, Gal Engelberg, Eden Yavin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud-security investigation is dominated by population tasks: which identities can read a data store, how many resources fail a control, which assets are reachable from another account. These resolve against a complete inventory, not a named object. A partial answer to one is not a partial result. It is a different result. General-purpose coding agents can now be given read-only cloud credentials and asked to investigate directly, which raises the question of what a purpose-built security context layer still contributes. We evaluate the Sola Security Brain, a security intelligence layer whose relational substrate is resolved offline and whose security logic is evaluated against it at query time, against Claude Code operating the same live AWS environment through a read-only CLI, over 28 cloud-security investigation tasks. Answers are scored by a blinded, tier-weighted, grounding-gated relative recall over the joint claim pool, averaged across three independent grading draws. The Sola Security Brain reaches 0.693 coverage against 0.387, a gap of 0.306 that varied by $\pm 0.018$ across three grading draws, or a relative gain of $79.2\%$. It leads on 25 of 28 tasks from the weaker model tier, at $17.7\times$ lower reasoning cost per task and $31.6\times$ lower cost per unit of coverage. Beyond the aggregate, we describe an answer-level pattern we term sample-and-generalise: under a turn budget the live agent enumerates a fraction of a large population, asserts an unhedged universal negative, and discloses the sample size only in answer metadata rather than in the answer. In one task it reported that no bucket policies exist after checking four bucket families, in a sweep that sampled 40 of roughly 5{,}000 buckets, in an account where 65 buckets carry a wildcard-principal read grant.

---


### 17. [Strategic Self-Consistency](https://arxiv.org/abs/2609.30352)

**<font color=#1a73e8>作者：</font>** Tori Qiu, Ander Artola Velasco, Manuel Gomez-Rodriguez  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-consistency has become a popular technique for enhancing the reasoning abilities of large language models by generating multiple reasoning paths and selecting the final answer through a majority vote. However, because model providers typically charge users in proportion to the number of reasoning paths generated, they have a financial incentive to artificially increase the path count. In this work, we show that an unfaithful provider can exploit this incentive using a simple, efficient algorithm while avoiding detection by an auditor: by generating and strategically reordering additional reasoning paths, the algorithm makes every path appear necessary to reach the majority. To validate our algorithm, we conduct experiments with multiple instruct models from the Llama and Qwen families, as well as reasoning models distilled from DeepSeek-R1, on benchmark datasets spanning mathematics, science, and question answering. Our results suggest that the distribution of additional reasoning paths generated by our algorithm is heavy-tailed and that substantial capacity to overcharge remains even under the best possible audit designed to keep the false-positive rate below $\alpha = 0.1$.

---


### 18. [Cost-Aware Best-LLM Identification using Dueling Feedback](https://arxiv.org/abs/2609.30360)

**<font color=#1a73e8>作者：</font>** Sarvesh Gharat, Nikhil Karamchandani, Jayakrishnan Nair  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Inspired by the problem of identifying the best model from a collection of large language models (LLMs) with heterogeneous querying costs, we formulate and analyse a variant of the multi-armed bandit (MAB) with (i) dueling feedback, where pairwise comparisons between model responses provide robust preference signals, and (ii) heterogeneous sampling costs, reflecting the differing costs of querying different LLMs. Assuming the existence of a Condorcet winner, a condition we empirically validate across multiple real-world datasets, we propose a Track-and-Stop style algorithm for best-arm identification with prescribed confidence. We prove that the algorithm almost surely achieves the asymptotically optimal cost as the error tends to zero. Finally, we extensively evaluate our approach on both synthetic and real-world instances, demonstrating consistent improvements over classical cost-unaware algorithms and their cost-aware extensions.

---


### 19. [Stealth Apart, Harm Together: Skill Cascading Attacks on Skill-Based Agent Systems](https://arxiv.org/abs/2609.30383)

**<font color=#1a73e8>作者：</font>** Zihao Zhu, Siwei Lyu, Adel Bibi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A skill is a modular package of natural-language instructions, executable scripts, and reference resources that an agent can load at runtime to extend its capabilities for a specific task. Skill-based agent systems therefore enable flexible reuse of third-party capabilities, but the openness of this skill ecosystem also opens up a new attack surface. Prior work has focused on vulnerabilities within individual skills, but little attention has been paid to risks that arise from interactions across skills. In this paper, we introduce skill cascading attacks, a threat paradigm in which a malicious objective is distributed across multiple skills so that each modification looks benign in isolation, yet their combined execution is harmful. For instance, in a prescription-review pipeline, the first skill weakens signals of recently discontinued medications in the extracted history, the second downgrades the severity of any drug interaction tied to them, and the third suppresses the resulting low-priority alert in the final summary, so that a severe drug-interaction warning silently disappears before reaching the physician. To systematically study this safety blind spot, we develop SkillCascade, an automated multi-agent red-teaming framework, and release SkillCascade-Bench, a benchmark of 213 validated cascading test cases across multiple agent systems and domains. Across representative agents (e.g., OpenClaw, Claude Code, Codex) and LLM backbones, cascaded interactions reliably induce harmful behaviors while evading existing per-skill scanners and runtime monitors. Our findings highlight a gap between component-level integrity and system-level safety, and call for defenses that reason over cross-skill interactions rather than individual skills in isolation.

---


### 20. [Adaptive Multi-Value Control in LLMs via Causal Activation Steering](https://arxiv.org/abs/2609.30405)

**<font color=#1a73e8>作者：</font>** Payel Bhattacharjee, Ravi Tandon  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in settings where responses must reflect multiple, potentially interacting social norms and human values. Activation steering offers a lightweight alternative to training-based alignment by modifying internal activations at inference time. However, prior human-value steering methods have largely considered values in isolation, while direct composition of multiple directions relies on fixed intervention strengths that cannot respond to the model's evolving internal state. Motivated by this key observation, we introduce AIMES, a framework for adaptive multi-value activation steering. AIMES constructs layer-specific bipolar directions for moral-foundation values and uses intermediate-layer vocabulary readouts as online observers. An observer-guided controller then adapts the strength of each requested value intervention at every decoding step based on its current observed state, without training a separate value-state estimator. Across multiple instruction-tuned model families, value combinations, and intervention depths, we find that multi-value controllability varies across both value combinations and intervention locations. Compared with fixed joint steering and prompt-based steering, AIMES shows depth-dependent advantages that are broadly supported across two independent evaluators, with some variation in the precise depth at which specific control effects emerge. These advantages come with smaller realized activation-space interventions than fixed-joint steering and comparable response quality. Overall, our results suggest that online observer feedback can provide lightweight, state-aware adaptation for single-pass multi-value steering.

---


### 21. [All In Good Time: Causality-Aware Framework for LLM-Based Simultaneous Speech-to-Speech Translation](https://arxiv.org/abs/2609.30416)

**<font color=#1a73e8>作者：</font>** Amir Hussein, Enas Albasiri, Travis M. Bartley 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong performance in low-resource offline translation; however, extending them to simultaneous speech-to-speech translation (Simul-S2ST) remains challenging due to the scarcity of causally aligned training data with high cross-lingual speaker fidelity. In addition, existing approaches rely on fixed translation policy or confidence heuristics, leading to suboptimal quality and higher latency. We propose a causality-aware Simul-S2ST framework with a novel data pipeline that generates high-fidelity, causally aligned segments with improved voice transfer. The framework introduces (i) a factorized S2ST architecture (FAST), (ii) a causality-aware adaptive policy (CAP), and (iii) causality-aware latency metric. Experiments on CVSS Spanish, German, and French show that FAST-CAP consistently improves the quality-latency trade-off, achieving up to +1.2 BLEU and a 26% relative latency reduction over a fixed policy. Despite using substantially less training data than existing systems, FAST-CAP achieves state-of-the-art results in speech translation quality and speaker fidelity while yielding up to a 38.8% relative reduction in latency.

---


### 22. [Fake News Theories: Harnessing Disciplinary Insights for Computational Modeling, Detection, and Explanation](https://arxiv.org/abs/2609.30427)

**<font color=#1a73e8>作者：</font>** Zhaoyang Cao, Miriam Metzger, Reza Zafarani  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Disinformation research has produced increasingly accurate automated fake-news detectors, but many systems remain difficult to interpret and are weakly connected to established theories of persuasion, credibility, and human judgment. In this paper, we develop a theory-informed computational framework that translates cross-disciplinary theories of fake news into measurable features for automated detection and explanation through statistical techniques and large language models. To that end, we conduct a structured cross-disciplinary review of theories from social sciences, psychology, economics, among other disciplines that reveal how fake news persuades and spreads, thereby establishing a broad theoretical foundation for computational modeling. Experiments on benchmark datasets show that theory-derived features are predictive and provide interpretable, theory-referenced diagnostic signals. Multi-feature models generally outperform individual features, although gains among the strongest small feature combinations are modest. Our work highlights the value of interdisciplinary perspectives in building robust and interpretable fake news detection systems, advancing the foundation for human-centered approaches in combating disinformation.

---


### 23. [ProCAP: Probabilistic Cross-Attentive Prompt Learning for Vision-Language Models](https://arxiv.org/abs/2609.30434)

**<font color=#1a73e8>作者：</font>** Hiwa Azeez Abbas, Fatemeh Daneshfar, Moloud Abdar  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pre-trained vision-language models such as CLIP can recognize new categories via prompting, but they often struggle when labeled data are scarce or the test distribution shifts. Prompt learning adapts only a small set of parameters while keeping the backbone frozen, yet many existing multimodal prompt learners couple the visual and textual branches weakly and can be brittle in low-shot regimes. We propose ProCAP, a probabilistic cross-attentive prompt learning framework that improves cross-modal interaction and training stability without updating any CLIP weights: it learns both visual and textual prompt tokens and links them through stacked bidirectional multi-head cross-attention so the two branches refine each other across prompt depth. To reduce overfitting under limited supervision, we parameterize prompt tokens with Gaussian means and variances and regularize them with lightweight KL and L2 penalties, and we further add a compact symmetric InfoNCE head that aligns cross-attended image features with class-level text representations in a shared low-dimensional space. Across few-shot base-to-novel generalization on 11 datasets, cross-dataset transfer, and domain generalization on ImageNet shift benchmarks, ProCAP achieves strong aggregate base-to-novel performance and competitive transfer performance while keeping the CLIP backbone unchanged.

---


### 24. [Inference-Time Target Speaker Unlearning in LLM-Based Automatic Speech Recognition](https://arxiv.org/abs/2609.30439)

**<font color=#1a73e8>作者：</font>** Bo Su, Yueru Yan, Thai Le  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce target-speaker unlearning ASR (TSU-ASR) task in a fully end-to-end framework for multi-speaker ASR and diarization. Given a multi-speaker utterance and a set of opt-out speakers who do not wish to have their speech transcribed, the task requires an ASR system to transcribe all speakers except the opt-out ones, while still indicating when those speakers are active. As a first step towards tackling this task, we introduce a novel, light-weight Enrollment-Conditioned Gating (ECG) module attachable to a frozen dual-stream speech LLM that enables ASR for new opt-out speakers dynamically during inference, even those who were not seen during initial ECG training phase. Our experiments on both AMI (English) and AliMeeting (Mandarin) datasets show that speech transcription accuracy for corresponding opt-out words or characters falls from 72.3% to 48.2% and from 73.6% to 27.3%, respectively, while retained speakers' transcription error rates maintain more or less the same. Our approach provides a practical solution for modern video conferencing platforms, allowing speakers to dynamically opt-out from automated AI transcriptions without forcefully leaving the meeting sessions, enabling a privacy-preserving interface for potentially millions of online meetings daily.

---


### 25. [RAZOR: Pruning Replaceable Experts in LLMs](https://arxiv.org/abs/2609.30465)

**<font color=#1a73e8>作者：</font>** Mingyang Song, Mao Zheng  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-experts (MoE) models activate few experts per token but store the full expert pool. Expert pruning reduces this storage burden; at a fixed pruning budget, the goal is to preserve the original model's output distribution as closely as possible. Yet an expert's usage or contribution magnitude does not by itself determine the damage caused by its removal. What matters is whether the surviving computation can replace its function. We introduce RAZOR, a training-free expert pruning method that scores functional replaceability using consensus residuals: deviations of expert outputs from the original weighted mixture. An exact single-deletion identity at a fixed layer input accounts for survivor renormalization and router-selected refill, providing local scores aggregated over calibration tokens for budgeted pruning without gradients or recovery training. On GLM-4.7-Flash, Qwen3.6-35B-A3B, DeepSeek-V4-Flash-0731, and Hy3 at 25\% and 50\% expert removal, RAZOR achieves the highest nine-task macro average among the evaluated pruning methods in all eight settings. On the two backbones with matched REAP benchmark runs, it exceeds REAP by 2.12--5.59 points and wins all 36 paired task comparisons. It also lowers reverse KL relative to REAP in all four matched GLM-4.7-Flash and Qwen3.6-35B-A3B model--budget settings. Analysis of responses generated by Qwen3.6-35B-A3B nevertheless reveals changes in diversity, formatting, and termination, underscoring that task retention and predictive fidelity do not ensure generation stability.

---


### 26. [A Benchmarking Framework for Context-aware XR Interfaces](https://arxiv.org/abs/2609.30466)

**<font color=#1a73e8>作者：</font>** Hyunsung Cho, Sarah Yewon Yun, Nancy Ruonan Sun 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Everyday Extended Reality (XR) systems aim to provide context-aware access to the right functionalities at the right time and place, with minimal manual reconfiguration as users switch context. Yet these interfaces are hard to evaluate: current prototyping and user-study workflows offer no systematic, repeatable way to compare adaptation methods across users and scenarios. We present ContextXR, a novel benchmarking framework for context-aware XR interfaces. ContextXR represents an XR application as a connected graph of functional facets, each a semantically coherent group of related capabilities that together support a shared user intent. On this representation, we build MineXR++, a dataset augmenting prior XR interface data with facet-level annotations, and formulate three canonical tasks of context-aware suggestion: context factor analysis, initial facet suggestion, and next facet suggestion. Our evaluation protocol scores suggestion methods by a simulated interaction metric, the navigation and search cost of reaching the desired functionality. Through experiments benchmarking global popularity, relational retrieval, and LLM-based methods, we demonstrate that ContextXR enables the systematic, reproducible evaluation of context-aware XR interfaces.

---


### 27. [Where Does Retrieval-Based Open-Ended Evaluation Fail? Automatic Taxonomy Induction from Long-Form Medical Answer Factuality Verification](https://arxiv.org/abs/2609.30467)

**<font color=#1a73e8>作者：</font>** Heyuan Huang, Jirui Dai, Alexandra DeLucia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-based factuality evaluation, where LLM-generated claims are verified against evidence from authoritative medical corpora, has become the dominant paradigm for scalable hallucination detection in high-stakes clinical settings. Despite the urgency of reliable and transparent medical fact verification, most systems measure performance with aggregate metrics like F1, which obscure where and why failures occur. Existing RAG diagnostics require gold answers or annotated gold evidence, neither of which exists in this regime. We introduce two comprehensive taxonomies, grounded in a case study on the open-ended MedExpert dataset and 3 closed-ended datasets, decomposing failures into retrieval-stage errors along five quality dimensions, and verifier-reasoning errors into six consecutive steps. We adapt an automatic pattern induction pipeline using LLM-as-Judge to label evidence quality and classify verifier reasoning errors at scale, and then stress-test our findings across 4 retrieval methods and 6 frontier verifier models. Our analysis reveals that scaling model size, adding reasoning effort, expanding to authoritative web sources, and applying medical fine-tuning do not resolve these failure modes, demonstrating that they represent fundamental limitations of the retrieve-then-verify paradigm in open-ended medical settings rather than artifacts of outdated systems. We release our code and data at this https URL for the full reproducibility of our results.

---


### 28. [Pretrained ASR Pseudo-labeling for Noisy Police Audio](https://arxiv.org/abs/2609.30469)

**<font color=#1a73e8>作者：</font>** Kaavya Chaparala, Su Huang, Stephen L. Miller 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pretrained ASR systems perform poorly on noisy Broadcast Police Communication (BPC), hindering efforts to understand police decision-making. Pseudo-labeling offers an unsupervised path to improve ASR without expensive human labels, but the efficacy of this approach on very noisy domains is not known. In this work, we systematically assess the opportunities and limits of pseudo-labeling to adapt foundation ASR models (Whisper and Qwen3-ASR) to noisy BPC domain corpora from Baltimore and Chicago. We demonstrate that existing internal confidence metrics (log-probabilities and STAR scores) fail to distinguish between high and low quality BPC pseudo-labels, and we introduce an external LLM-as-a-judge filtering paradigm that leverages parametric knowledge to discard contextually implausible transcripts. Our LLM-judging filters more aggressively than internal metrics and significantly reduces WER of the pseudo-labeled training sets across the Baltimore and Chicago BPC corpora, though a substantial gap remains relative to an oracle filter. We also introduce a new cross-model pseudo-labeling paradigm where one model is finetuned with pseudo-labels from the other, and we identify this method as a promising direction for future pseudo-labeling work.

---


### 29. [CARGO: Context-Aware Retrieval-Gated Evaluation of Agentic AI in Production](https://arxiv.org/abs/2609.30471)

**<font color=#1a73e8>作者：</font>** Mukul Chhabra, Shail Patel, Luigi Medrano  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reference-based LLM-as-a-judge evaluation assumes the reference answer is the target. In deployed agentic systems that operate over dynamic entities (support cases, assets, accounts), the closest available reference typically applies the correct procedure to a different entity, so a literal judge penalizes different identifiers, dates, and statuses as errors or hallucinations. We name this failure mode reference-instance divergence (RID). We propose CARGO, a framework that (i) treats retrieved references as procedural exemplars and grounds factual judgments in the live instance's observed context, (ii) assigns each claim a three-way status (supported, contradicted, unverifiable) and penalizes only contradictions, and (iii) gates evaluation by retrieval confidence, casting production evaluation as selective prediction. We introduce CARGO-Bench, a perturbation-based diagnostic suite with ground truth by construction that separates leniency from discrimination. On CARGO-Bench (246 items, two judge models, 7,872 judgments), the standard reference-based judge penalizes 100% of correct entity-transplanted answers and is uninformative (discrimination index DI ~ 0); supplying the live facts without reframing changes nothing. CARGO eliminates these false penalties (0/50) while retaining near-complete contradiction recall (50/50 and 49/50), raising DI to 0.58 [0.48, 0.68]; a rubric-swap control attributes most of the effect to context-grounded dimension definitions. CARGO also exposes a limitation of its own design: the leniency that protects entity values suppresses detection of procedural corruptions (20% recall). A post-hoc fix does not close the gap, and an LLM-as-annotator study with written guidelines and adjudication shows the same blind spot. We release a preregistered protocol for extending the evaluation to expert agreement, risk-coverage, and cost on production traffic.

---


### 30. [Mentored Decoding: Faster Inference meets Boosting](https://arxiv.org/abs/2609.30474)

**<font color=#1a73e8>作者：</font>** Vivien Tran-Thien, Richard Nock  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Speculative decoding is a successful technique speeding up inference of a target autoregressive language model via a fast drafter model. Lossy speculative decoding allows a drift with respect to the target to further improve speed. Interestingly, it has been observed experimentally that the resulting model can $\textit{also}$ beat the target $\textit{quality-wise}$. Our paper formally proves how such a feat is possible with a formal approach to lossy speculative decoding called $\textit{mentored decoding}$. To get there, we connect inference to a celebrated ML training theory, $\textit{boosting}$, and proceed via the generalization of mentored decoding to the whole set of $f$-divergences. We uncover key properties of mentored decoding, among which (i) the particularly appealing geometric nature of the total variation case, (ii) simple approximations for any $f$-divergence in direct relation with boosting compliance, and (iii) a $\textit{divergence independent}$ $O(n)$ space and $O(\mathrm{sort}(n))$ time data structure built on drafter and target outputs, which allows to query the optimal parameters of the dual problem in $O(\log n)$ time and constructing optimal mentored distributions in $O(n)$ time for any $f$-divergence.

---


### 31. [Do LLMs Understand Context? A Knowledge Graph-Based Evaluation Framework](https://arxiv.org/abs/2609.30484)

**<font color=#1a73e8>作者：</font>** Subavarshana Arumugam, Mamta Nallaretnam, Kithuni Wickramasinghe 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While large language models (LLMs) have achieved remarkable linguistic capabilities, a profound question lingers at their core: do these models truly comprehend context or simply excel at pattern matching on an unprecedented scale? Contextual understanding in LLMs refers to the ability to correctly extract relevant information from a given context, integrate it into a coherent internal representation, and reason over it to produce factually consistent and contextually grounded responses. However, traditional methods such as BiLingual Evaluation Understudy (BLEU) and perplexity simply measure surface-level performance. This reveals a critical gap in question answering (QA), where responses must be contextually grounded rather than simply being memorized associations. To fill this void, we propose a novel knowledge graph (KG) based evaluation framework for LLM contextual understanding in QA. Central to this is Semantic Structural Similarity for KGs (S3KG), a hybrid similarity measure combining structural and semantic signals into a single score. In addition, a diagnostic analysis framework is developed to identify and categorize reasoning errors at the triplet level, enabling fine-grained analysis of model failures. Together, across nine benchmarks, S3KG achieves F1 gains of up to $+7.6$ points over the strongest baseline and AUROC up to $0.973$.

---


### 32. [BioEVAL: A global, multi-institutional benchmark of large language and multimodal models for bioengineering](https://arxiv.org/abs/2609.30489)

**<font color=#1a73e8>作者：</font>** Shun Ye, Vinny Chandran Suja, Chenlong Li 等 63 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have demonstrated historic breakthroughs in general reasoning with early successes in biomedical science. However, existing LLM benchmarking emphasizes factual recall, offering limited insight into model performance on frontier and multimodal tasks. We assembled BioEVAL (BioEngineering Validation of AI and LLMs), a global, multi-institutional initiative designed to assess experimental reasoning capability across bioengineering (BE) subfields. BioEVAL spans 11 major BE subfields plus a set of uncategorized items, bringing together 22 research groups to create a PhD-level benchmark comprising 608 evaluation items: 1) 380 multiple-choice questions (MCQs, 359 retained after audit), 2) 218 literature synthesis tasks, and 3) 10 multimodal problems with experimental image interpretation. Benchmark items underwent authoring-group expert review and centralized quality control before evaluation. Following evaluation, a blinded cross-group consensus audit of the highest- and lowest-accuracy MCQ items flagged 21 questions for revision or removal; these were withheld, and all reported MCQ results are computed on the 359 retained items. We evaluated diverse cloud-scale foundation/multimodal models (e.g., ChatGPT, Gemini, and Grok) and locally deployable models suitable for inference on consumer-grade GPUs. Models achieved the highest accuracy of up to 90% on MCQs, similarity score of 0.72 on literature synthesis, and accuracy of 80% on a small sample of multimodal reasoning questions, with substantial performance variation across subfields. Leaderboard rankings characterize current capabilities, limitations, and development priorities across the evaluated BE task categories. BioEVAL is maintained as an extensible benchmark with standardized protocols for continuing expert item contribution and model evaluation.

---


### 33. [Breaking Homogeneity: Diversifying Persona Sets for Creative LLM Outputs](https://arxiv.org/abs/2609.30492)

**<font color=#1a73e8>作者：</font>** Sang Bin Moon, Nicole Cho, Daniel Borrajo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models often produce homogeneous responses to open-ended tasks; such homogeneity can spawn groupthink-the convergence of ideas toward a singular and potentially suboptimal decision. We formulate persona diversification as a set-level conditioning problem and study two orthogonal design choices: selecting versus generating personas, and space-filling versus frontier-seeking diversity. We instantiate this design space with four methods spanning coverage and dispersion subset selections, uniform-coverage sampling, and evolutionary persona generation. Evaluations on the Alternative Uses Task (AUT), Infinity-Chat, and Divergent Association Task (DAT) show the benefits of the proposed methods across tasks and creativity objectives. On AUT, evolutionary persona generation increases response diversity by 78.8%, originality by 26.1%, flexibility by 49.5%, and holistic creativity by 13.9% over task-only prompting, while maintaining 98.5% validity; on Infinity-Chat, it nearly doubles persona-induced response separation relative to random personas. Moreover, evolutionary personas compose with creativity-optimized prompting, further increasing its response diversity by 18.6% and creativity by 6.3%. These results establish persona-set geometry as a task-agnostic mechanism for eliciting divergent LLM outputs, and support persona diversification as a reusable complement to prompt optimization.

---


### 34. [To Solve Bilevel Optimization with Nonconvex Lower Levels, We Need Second-Order Stationarity](https://arxiv.org/abs/2609.30501)

**<font color=#1a73e8>作者：</font>** Zhiyao Zhang, Menglu Yu, Alvaro Velasquez 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Although bilevel optimization (BLO) has emerged as a powerful framework for addressing many complex and nested machine learning problems in recent years, most existing studies are confined to the lower-level strongly convex (LLSC) or lower-level generally convex (LLGC) settings (i.e., the lower-level objective function is assumed to be, at least, convex). While the LLSC/LLGC assumptions render more tractable algorithmic design and theoretical analysis, they are too rigid to encompass many machine learning problems in practice. The limitations of LLSC/LLGC assumptions in BLO motivate us to investigate solving the BLO problem in the general lower-level nonconvex (LLNC) settings, which remains in its infancy. In the literature on LLNC-BLO, most of the existing works either require additional structures in the lower-level objective function for tractable theoretical analysis, or adopt the first-order stationarity reformulation as a lower-level surrogate problem, which is inherited from the LLSC/LLGC settings but could lose their effectiveness in the LLNC setting. To bridge this gap, we propose to reformulate the nonconvex lower-level problem using a second-order stationarity-based surrogate, the solution of which guarantees a local optimal solution at the lower level. Based on this reformulation, we propose the PROBE (Perturbed gradient algorithm for bilevel problem) and show that it overcomes the limitations of prior works by probing and escaping lower-level saddle points. We prove that PROBE achieves a finite-time convergence rate of $O(T^{-2/5})$, where T denotes iterations. To our knowledge, this work is the first to establish the finite-time convergence for achieving lower-level second-order stationary solutions in general LLNC-BLO. Our experiments on both a large language model-based data curation task and a meta-learning task also show that PROBE outperforms SOTA methods.

---


### 35. [Feeding BabyLMs Macaroni: Code-Switching Curricula Cause Cross-Lingual Convergence](https://arxiv.org/abs/2609.30535)

**<font color=#1a73e8>作者：</font>** Dries Rooryck, Alex Cai, Yonatan Belinkov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Children in multilingual communities often code-switch, using multiple languages in a single utterance. Can we induce cross-lingual alignment in language models by training on code-switched text? We pretrain small decoder-only transformers on two 100M-word multilingual corpora: a base corpus formed by mixing the English, Dutch, and Chinese BabyBabelLM datasets, and a corpus generated from it by inserting word- and sentence-level code-switching using an LLM. We find that training on code-switched data aligns the representations of parallel text, particularly across different scripts, and that this alignment persists through training on monolingual documents. Under a learning curriculum that progresses from word-level code-switching, to sentence-level code-switching, to monolingual documents, models trained on code-switched data outperform baselines trained without it on the BabyLM evaluation suite. Our work characterizes code-switching curriculum learning as an effective data augmentation method for multilingual pretraining. We release our code, data, and models at this https URL.

---


### 36. [AutoResearch at Production Scale: Failure Modes and a Multi-Agent Framework](https://arxiv.org/abs/2609.30541)

**<font color=#1a73e8>作者：</font>** Aparajith Chandran, Juwon Kim, Saurav Jha 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Optimizing embedding systems for production recommendation pipelines demands systematic exploration that consumes disproportionate engineering effort at scale. We apply Andrej Karpathy's AutoResearch paradigm -- a large language model that iteratively edits a training script and retains modifications that improve a held-out scalar metric -- to automate this exploration. We report on twelve weeks of running this paradigm at production scale, where iterations consume hours of multi-GPU compute, evaluation involves competing criteria, and campaigns span weeks across many training jobs. Across two independently developed representation-learning systems for a book recommendation pipeline, we ran 220+ experiments and observed five recurring failure modes absent from the original setting: infrastructure fragility, agent memory decay, search-direction stagnation, iteration-cost asymmetry, and metric fixation. We contribute a three-principle scaffolding design -- prevent, persist, redirect -- that maps each failure mode to a structural remedy and whose instantiation scales with iteration cost. The framework produced a 1.82x Recall@6 lift and a 2.1x coherence lift over hand-tuned baselines, and the agent autonomously designed a text-only fallback that expanded catalog coverage by 5.8x. The two systems span nearly three orders of magnitude in per-iteration cost yet exhibit the same failure modes, suggesting these are structural properties of production-scale autonomous research rather than artifacts of either application.

---


### 37. [REALMS: An AI-Assistant Conversational System for Real-Time Exact Audience Sizing over High-Dimensional Nested Profiles](https://arxiv.org/abs/2609.30547)

**<font color=#1a73e8>作者：</font>** Haixu Ma, Aditya Bansal, Shubham Lohiya 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audience sizing is a critical component of digital marketing. It enables precise resource allocation, campaign planning, and performance optimization. Traditional approaches using skeleton audiences, sampling, or predictive modeling suffer from significant delays, estimation errors, and poor scalability over high-dimensional profile data. We present REALMS (Real-time Exact Audience sizing via LLM-based Multi-attribute Search), a conversational system for exact audience sizing deployed in production on an enterprise customer data platform. REALMS enables marketers to query massive profile stores with millions of profiles and thousands of attributes using natural language and receive precise counts in seconds. The system introduces three key components: (1) a categorical attribute retrieval mechanism using embedding-based vector search to dynamically identify relevant schema attributes without manual configuration; (2) an LLM-powered NL2SQL pipeline with template-based in-context learning for accurate query generation over complex nested schemas; and (3) schema standardization enabling industry-agnostic deployment across diverse enterprise environments. Evaluation on real enterprise data demonstrates strong recall for attribute retrieval, high SQL execution accuracy, and low latency, which enables real-time interactive audience insights where prior methods required hours.

---


### 38. [Probing Stability-Plasticity Tradeoffs in Agent Memory through Cognitive Experimental Paradigms](https://arxiv.org/abs/2609.30558)

**<font color=#1a73e8>作者：</font>** Jiaqi Ding, Guorong Wu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent memory systems are increasingly used to maintain long-term user preferences, task states and evolving facts, but current evaluations often collapse memory behavior into final-answer accuracy. We introduce MemProbe, a cognitive-science-inspired framework for diagnosing stability-plasticity tradeoffs in agent memory. The framework is motivated by a core insight from cognitive memory research: memory is reconstructive and shaped by interference, source reliability, reinforcement, and reactivation. MemProbe turns this insight into four reusable experimental paradigms (interference, misinformation, consolidation strength, and reconsolidation window) that manipulate when a memory should be updated, preserved, or treated as uncertain. It further decomposes correctness into behavioral profiles that reveal how systems update, preserve, attribute, and temporally organize information. We instantiate these paradigms in a 56-episode diagnostic suite and evaluate six incremental memory systems under a unified protocol. Results show that systems with similar aggregate scores exhibit distinct behavioral profiles. MemProbe provides such a diagnostic lens, turning aggregate performance into interpretable profiles of memory maintenance over time. Code is available at this https URL.

---


### 39. [Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents Simulating Individual Social Media Reactions, Including Unfamiliar Content](https://arxiv.org/abs/2609.30563)

**<font color=#1a73e8>作者：</font>** Ljubisa Bojic, Tijana Stanic, Joerg Matthes 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Platform policies are increasingly tested on artificial users, making agent fidelity important. Yet convincing fake profiles could also manipulate perceived public opinion before elections. Validation has concentrated on agreement with human behaviour and has paid little attention to whether an agent behaves in line with the profile it was given. The present study profiled eight Serbian participants through a questionnaire, a deep interview, and a written self-presentation, recorded their reactions to sixty-eight social media posts, and asked four language models to predict those reactions under five prompt conditions varying profile content and instruction style. Attitudinal content improved prediction over demographic backstories by a wide margin. Agents matched their stated profiles more closely than participants matched their own survey answers, and consistency proved unrelated to fidelity once profile information was present. Instructing models to respond intuitively and immediately rather than analytically gave the highest fidelity of any condition and cut the compression of individual differences from seven times the human level to three. The advantage held on posts about topics the questionnaire never raised, where that condition reached the highest fidelity of any setup and beat a crowd baseline by a wide margin, which suggests that agents prompted this way could serve as general-purpose simulated users rather than specialists on the topics they were profiled for. Results may bear implications for the development of language models, because intuition-based setups appear better suited to some tasks than reasoning-based ones.

---


### 40. [HARDEN: Constrained Evolutionary Search for Harder, Answer-Preserving Evaluation Cases](https://arxiv.org/abs/2609.30571)

**<font color=#1a73e8>作者：</font>** Aditya Kumaran, Rahul Singhal, Karime Maamari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are often evaluated on curated benchmarks that underrepresent the complexity of enterprise deployments. We introduce HARDEN, a constrained evolutionary search method to adapt the input of existing evaluation cases into more challenging variants while keeping their expected outputs fixed. HARDEN searches along generated domain-specific complexity axes while enforcing feasibility constraints such as preserving task semantics, realism, and execution validity. Across FinQA, PubMedQA, and ContractNLI and three Qwen3.5 model scales (35B-A3B, 122B-A10B, and 397B-A17B), HARDEN reduces task-model accuracy by 22.7% on average and by up to 49.9% relative to single-pass baselines using the same feasibility checks. These results show that evolutionary search can produce substantially harder valid evaluation cases.

---


### 41. [Entropy Regularization: A Free Correction to Cross-Entropy for Verified Demonstrations](https://arxiv.org/abs/2609.30572)

**<font color=#1a73e8>作者：</font>** Mihir Dhanakshirur, Adam Ousherovitch, Ambuj Tewari  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models are often post-trained on expert demonstrations using cross-entropy (CE), even when the downstream objective is not to imitate the demonstrated solution but to produce any output accepted by a verifier. This mismatch is seen in verifiable domains with multiple correct solutions, such as mathematical reasoning and code generation, where training data may contain only one expert solution per problem. We show that minimizing cross-entropy can be misaligned with minimizing verifier risk; two policies can assign identical likelihood to the observed demonstrations while placing different probability mass on incorrect outputs. This is formalized through a learning-theoretic counterexample in which CE minimization selects a suboptimal policy. We identify that controlling the support of the learned policy can solve this problem by preventing probability mass from spreading to unsupported outputs. Since support size is non-differentiable and computationally intractable, we propose entropy-regularized cross-entropy (ER-CE), using token-level Shannon entropy as a tractable proxy. Finally, across mathematical reasoning and code-generation benchmarks, we find that entropy-regularized training consistently improves verifier accuracy over standard cross-entropy. Our results identify a simple failure mode of imitation-based post-training in verifiable tasks and provide a practical objective that is better aligned with producing correct outputs.

---


### 42. [T-RoPE: Time-Aware Rotary Position Embedding for Sequential Recommendation](https://arxiv.org/abs/2609.30576)

**<font color=#1a73e8>作者：</font>** Yang Liu, Noel Loo, Ali Khanafer 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large-scale recommenders increasingly adopt the sequential generative recipe behind large language models, bringing the Transformer into recommendation along with design choices made for text, including Rotary Position Embedding (RoPE). In language models, RoPE encodes token indices for relative position reasoning, but in recommendation, an interaction index records only event order, saying nothing about elapsed time, behavioral cycles across scales, or calendar phase. We revisit this choice and propose T-RoPE, a time-aware RoPE for sequential generative recommendation that replaces index-only rotation with timestamp-based angles, learnable temporal coefficients, multiscale frequency banks, shifted query alignment, and non-stationary key rotation. We prove that standard RoPE, even on timestamps, remains time-translation invariant and cannot distinguish seasonal contexts, and that T-RoPE breaks this invariance while preserving the RoPE interface. Across five public benchmarks, T-RoPE achieves the best result on every metric on every dataset, improving over the strongest baseline by 78--130\% in HR@10 on the sparse PixelRec data and 8--12\% across metrics on Amazon Books. On an industrial-scale e-commerce dataset with more than 6B interactions, it improves every metric over the HSTU + Time RAB backbone by 13--82\%, with ablations attributing the largest gains to multiscale frequencies ($+56\%$ NDCG@50) and non-stationary keys ($+4\%$). An online A/B test in the Shop app yields positive lifts in conversion rate ($+0.33\%$) and order count ($+0.63\%$). We also provide forward and backward algorithms whose added cost is linear in sequence length and head dimension, keeping time-aware RoPE practical for large generative recommenders.

---


### 43. [Reinforcement Learning of Communication in a Mesh of Small Language Models](https://arxiv.org/abs/2609.30578)

**<font color=#1a73e8>作者：</font>** Mehmet Kerem Turkcan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models gain accuracy from more compute at test time, but majority voting over independent samples saturates: as samples grow, the vote converges to the model's most frequent answer. Communication can add what sampling cannot: an agent that solves a problem can pass the key step to the others. We present TalkMesh, a decentralized mesh of small language model agents that learns when and what to communicate. Each agent samples a proposal and scores it with a trained confidence head. The most confident agent broadcasts a hint; agents below a confidence threshold revise, keeping each revision that outscores its proposal. Gossip consensus approximates the vote weighted by confidence without a coordinator. A talk policy, trained with group relative policy optimization on the change in correctness after revision, writes hints and revisions. With three agents, which together generate at most six outputs, the mesh reaches the accuracy of majority voting over 32 samples with each of three models. Trained with at most 8 agents and evaluated with 32, it raises accuracy from 0.568 under self-consistency to 0.705 (Qwen3.5-0.8B, GSM8K) and from 0.492 to 0.722 (SmolLM3-3B, MATH-500). When 4 of 8 agents collude on a wrong answer with fabricated confidence and poisoned hints, majority vote accuracy falls to 0.000 (Qwen3.5-0.8B, GSM8K). A defended mesh, whose agents rescore solutions with their own confidence heads, retains 0.507. Across reasoning, embodied coordination, and traffic signal control, messages improve a decision when the acting agent cannot observe the information it requires and another agent can send it.

---


### 44. [Orchestrating GenAI for Interdisciplinary Research](https://arxiv.org/abs/2609.30588)

**<font color=#1a73e8>作者：</font>** Shirley Anugrah Hayati, Moyan Zhou, Patricia Anugrah Setiani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As researchers tackle interdisciplinary problems, they face the need to deepen expertise in primary areas while rapidly acquiring knowledge in secondary domains. Generative AI (GenAI) is increasingly positioned to meet this need, from general-purpose chat assistants to Deep Research tools marketed as autonomous research agents. Prior work has examined how researchers use GenAI to support single-discipline or general research tasks. However, we know little about the goals and GenAI practices in interdisciplinary research. We conducted a longitudinal study and semi-structured interviews with 15 interdisciplinary researchers to examine how interdisciplinary researchers actually orchestrate GenAI. Findings show that researchers leaned on GenAI to fill knowledge gaps while maintaining epistemic agency for novelty discovery. We also uncovered an expertise paradox: GenAI outputs were hardest to verify when most needed. Our empirical insights motivate GenAI designs that calibrate verification to researchers' expertise, nudge toward cross-domain synthesis, and adapt prompting and outputs to disciplinary conventions.

---


### 45. [The Hard Part Comes After Search: Benchmarking Web Agents on Synthesizing, Organizing, and Displaying Knowledge](https://arxiv.org/abs/2609.30604)

**<font color=#1a73e8>作者：</font>** Alexander Gill, Md Farhan Ishmam, Xuyen Nguyen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing computer-use agent benchmarks do not fully evaluate agents acting as assistants. A useful assistant retrieves information across complex, multi-step workflows, synthesizes it into artifacts (documents, presentations, spreadsheets), and navigates program interfaces to produce a coherent final product. Such workflows demand reasoning and synthesis, decomposition of complex tasks, as well as visual and spatial understanding. To study agents on workflows like these, we introduce KNOWS, a benchmark of open-ended, complex, browser-based tasks that jointly evaluate these capabilities, with each task culminating in a produced artifact. To write tasks, we develop a task design rubric and a protocol for ensuring that tasks meet the requirements. Each task is paired with an evaluator, a program that combines deterministic checks with LLM judgments to balance the richness, reliability, and automation tradeoff inherent to agent evaluation. We evaluate and analyze frontier computer-use agents and browser-based harnesses. They achieve moderate scores on partial-success metrics, but the best performer fully succeeds in fewer than 3% of our complex, long-horizon tasks. Failures on visual steps render the resulting artifacts unusable, even when agents complete more than 50% of other evaluation steps. Our results expose limitations of current agents acting as end-to-end assistants, and call for progress on tool use, visual understanding, and long-horizon reasoning.

---


### 46. [MVAgent: Multi-Agent Video Generation via Consistent Condition Construction and Shot-Level Policy Optimization](https://arxiv.org/abs/2609.30609)

**<font color=#1a73e8>作者：</font>** Xiangyu Kong, Wenjie Zhou, Fengping Tian 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multi-shot agentic video generation requires consistent character appearance, stable spatial layout across camera angles, and continuous character state between shots. When every shot is a separate request to a frozen generator, repeated text does not determine appearance, layout or state. We therefore recast the problem as condition construction and present MVAgent, a multi-agent pipeline whose agents collaborate through typed conditioning inputs. Because an environment image shows one viewpoint, a Spatial Grounding agent samples views from generated camera-traversal clips and anchors each shot to the view matching its framing. As generated shots drift from the plan, an Observer records how each shot ends in a continuity memory, from which a Transition agent builds character action and spatial references for the next shot. An Orchestrator composes these inputs into each request. Since a request reveals its effect only after rendering, we train it by agentic reinforcement learning with Trunk-GDPO, which compares rendered candidates at every shot rather than once per video and continues the best as the trunk. With generator and judges frozen, MVAgent attains the highest cross-shot consistency and narrative-planning quality among the compared methods on ViMax-Bench and is preferred over the strongest agentic baseline in human evaluation.

---


### 47. [Epstein Files Engine: Agentic Search for Investigative Journalism](https://arxiv.org/abs/2609.30611)

**<font color=#1a73e8>作者：</font>** Duy K. Nguyen, Teresa Mondría Terol, Dylan Freedman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> On Jan. 30, 2026, the U.S. Department of Justice released a mixed-media collection concerning Jeffrey Epstein, including about three million pages of PDFs. We describe the Epstein Files Engine, an A.I. agent The New York Times deployed to investigate the files. The Engine translated reporter questions into Google BigQuery SQL queries across three corpora: Epstein-related releases, the Times's archive and external, Epstein-related news headlines. It used an LLM to plan queries and returned citation-rich answers a reporter could verify and trust. More than 100 journalists used the Engine, and it contributed to at least 20 published stories. We report how reporters queried it and describe Diff, our text-and-visual duplicate matching method that amplified novelty signals and allowed the Engine to surface genuinely new information. We argue that newsroom agents serve newsrooms best not as autonomous writers, but as interfaces to source material and institutional knowledge.

---


### 48. [Subjects, Not Authors: The Authorship Hazard in Agentic Dataspaces](https://arxiv.org/abs/2609.30614)

**<font color=#1a73e8>作者：</font>** Seungho Lee, Changbin Lee  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Dataspace connectors decide whether a transfer may occur, not what the transferred value contains, tolerable for contracted applications, not for LLM agents that compose tool calls and spawn sub-agents. Research on agents that generate governance artifacts evaluates output quality; who may authorize an artifact for use falls between that literature and the governance literature, and neither owns it. A published policy is what a dataspace's decision point enforces, so publication is a governance event, and an agent that is both policy subject and policy author writes the norms that bind it. We name this the authorship hazard and state one principle: an agent is a subject of the governance plane, never an author of it. Its authorization channel to publication is closed by construction; its influence channel, drafting what humans approve, is treated as an enforcement problem. On a frozen corpus of agent drafts, publishing without approval reverses 80 authorization decisions, most through drafts that change only a field's sensitivity classification and no policy text; a classifier that reads the policy diff misses every such draft, necessarily. Treating classification as authorship routes them all to review; the registry-held classification this requires is designed and modelled here, not yet implemented in the prototype. At the execution boundary, protected fields reach the model in 105 of 105 cases under prompt-stated duties and in 0 of 105 when the ODRL duty is compiled into an invocation-time tool-call constraint, but where the value is not confined to a named field the compiled condition exposes it in 7 of 7. A centrally provisioned approval pool does not scale to the participant volume that motivates the problem.

---


### 49. [Audio LLMs Know When They Can't Hear You](https://arxiv.org/abs/2609.30625)

**<font color=#1a73e8>作者：</font>** Amirhosein Javadi, Richa Dixit, Mehrdad Farajtabar 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Audio large language models allow users to interact with the model through speech. When an input recording is too degraded, the model may misinterpret the user's query and respond based on an incorrect transcription. In this paper, we study model-conditional transcription reliability: whether an Audio LLM can recognize when its own transcription is unreliable. We first prompt the Audio LLM to assess whether its own transcription would be reliable, and find that the model is a poor judge of its own transcription reliability: in most cases, it predicts that its transcription will be reliable. We find that existing approaches, including speech quality predictors, audio LLM generation uncertainty, and transcript-conditioned WER estimation, provide limited signals for detecting transcription failures. In contrast, we discover that transcription reliability is strongly represented in the model's audio-encoder representations. Based on this observation, we devise a lightweight reliability predictor that operates on representations extracted by the frozen audio encoder and predicts the reliability class before generation. The reliability predictor can trigger a clarification request from the user when their voice query is predicted to be unreliable, while allowing reliable queries to proceed without modifying the underlying Audio LLM. Our predictor achieves 81.10% in-domain and 78.09% cross-domain macro-F1 scores, outperforming the strongest baselines by 10.33 and 11.93 points, respectively. Finally, we show that reliability labels can transfer across Audio LLM families, and that transfer performance is closely related to the alignment of their model-specific reliability boundaries.

---


### 50. [In-Context Binding Capacity in Language Models](https://arxiv.org/abs/2609.30634)

**<font color=#1a73e8>作者：</font>** Manas Venkata Sai Ravulapalli, Samrath Singh Chadha  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How many assignments can a language model recall before it loses track of which value belongs to which entity? We measure this limit using continuous recall curves for 12 models at or below 3B parameters and a threshold sweep over 30 open models up to 12B. On the continuous curves, the load at which recall falls halfway to chance follows $K_{50}=cN^{\alpha}$, with $\alpha=0.820$ and $R^2=0.73$. The broader sweep shows an eightfold range associated with pretraining recipe, although the continuous curves show no detectable recipe effect after controlling for scale, with few modern models in the fit. We derive why interference can lower measured capacity by reducing single-binding recall even when the load-dependent recall profile is unchanged. Direct task training also exceeds the extrapolated zero-shot law, but different measurement criteria prevent interpreting that comparison as a capacity gain. Its formation times follow a power-law form in two independent codebases, conditional on runs that succeed. Together, these results characterize capacity at the model's query interface. Bounds on joint recall and a decomposition of policy errors connect this measurement to working memory and instruction following, without treating recall as a measure of alignment. The controlled task also provides a baseline for testing whether binding limits constrain world-state tracking; the present experiments do not measure state updates or downstream transfer.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-183](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
