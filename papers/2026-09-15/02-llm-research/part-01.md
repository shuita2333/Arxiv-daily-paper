# 🧠 大模型相关研究 | 2026年09月15日

> 本类共 **134** 篇论文：已确认 **130** 篇，待复核 **4** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-134](./part-03.md)

---

### 1. [R2VC: Modular Fact-Checking with Retrieval, Verification, and Confidence Calibration](https://arxiv.org/abs/2609.11955)

**<font color=#1a73e8>作者：</font>** Dhruv Dixit, Paritosh Pandey  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used for automated fact checking, but end-to-end prompting often entangles evidence retrieval, reasoning, and uncertainty estimation, making failures difficult to diagnose and confidence difficult to trust. We present R2VC, a modular retrieve, reason, verify, calibrate architecture for evidence-grounded fact checking with citations and abstention. R2VC combines hybrid sparse+dense retrieval over Wikipedia, a supervised fine-tuned and DPO-aligned generator that produces diverse structured verdict candidates, an external NLI cross-encoder for evidence-based candidate selection, and a lightweight sequence-level calibrator for confidence estimation and selective abstention. On FEVER, an 8B backbone with R2VC achieves 13.74% higher accuracy than baseline. Ablation studies show that verifier-based candidate selection and confidence calibration are the largest contributors to performance. Removing candidate selection drops FEVER accuracy to 76.24%, while removing calibration nearly doubles the Brier score to 0.161. A manual analysis of 250 errors further shows that retrieval failures, especially wrong-entity evidence, remain the dominant bottleneck. Together, these results show that modular fact-checking pipelines can substantially improve both predictive accuracy and confidence reliability in open-domain verification.

---


### 2. [Performance, Efficiency and Collapse -- Advantages and Challenges in Offline Post-training of Code LLMs](https://arxiv.org/abs/2609.11956)

**<font color=#1a73e8>作者：</font>** Abhinav Anand, Sanjana Reddy Pachika, Shweta Verma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training with reinforcement learning (RL) is a critical phase in the development of code-generating large language models (LLMs), as it ensures adherence to instructions and the production of functionally correct code. This process typically requires computationally intensive code sample generation from Transformer-based LLMs and substantial GPU-CPU communication for sequence verification. To address these computational challenges, this work examines whether RL-based post-training can be performed entirely offline by leveraging existing datasets rather than generating new samples. The findings indicate that, with only a few hours of training, zero-shot code generation performance of LLMs can be substantially improved without online sampling. Additionally, offline RL produces performance gains across models ranging from 0.5B to 7B parameters, although the extent of improvement varies among model families.

---


### 3. [Look Before You Leap: Pre-Action Verification for LLM Agents](https://arxiv.org/abs/2609.11957)

**<font color=#1a73e8>作者：</font>** Asaad Althoubi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> An LLM agent acts on the world by emitting actions: shell commands to run, edits to apply. A wrong action does not always fail loudly; it can fail silently, producing a plausible but incorrect effect that raises no error. We argue that a cheap deterministic check, run before an action takes effect, is an effective and underused form of agent oversight, and we study it across two action modalities in one framework. The idea is to fix an action's correct effect by construction, before any executor runs, so that silent failure is measured directly and the verifier may abstain rather than guess. For shell commands, a static verifier over 9930 commands and 482 tools catches 95.8% of invalid commands at a 10.0% false-positive rate. Its syntax and binary checks are oracle-exact, giving zero false positives while catching half of all errors; the flag check is bounded only by help-text coverage and accounts for every false positive. For code edits, a benchmark of 640 edits over 224 files isolating the apply step exposes a sharp split. Content-anchored formats such as search/replace and diff fail cleanly, whereas location-anchored formats fail silently: line numbers corrupt 99.1% of files under a one-line shift, and function-name edits hit the wrong function 12.7% of the time. In both settings a refuse-when-unsure policy turns silent failures into recoverable ones at a tunable cost in applicability: selective grounding reaches 0.958 recall at 7.0% false positives, and an anchor-and-verify applier records one silent misapplication in 8320 trials (0.01%). We release both benchmarks, the verifiers, and the guards.

---


### 4. [On-Device Language Models for Privacy-Preserving Stress Prediction: A Multimodal Evaluation on Mobile Health](https://arxiv.org/abs/2609.11961)

**<font color=#1a73e8>作者：</font>** Ibukunoluwa Soyebo, Alyssa Donawa, Rodrigo Aguilar Barrios 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Stress is a pervasive determinant of mental health and a key target for mobile health interventions. On-device language models (ODLMs) offer privacy-preserving inference without cloud dependency, yet their feasibility for health prediction under mobile resource constraints remains underexplored. We evaluate ODLMs for multi-modal stress prediction using zero-shot prompting, measuring predictive accuracy alongside latency and throughput. Our results show that objective sensor features marginally outperform subjective self-reports on average, and that lightweight sub-2B models achieve low latency with predictable resource usage. Our findings highlight both the promise and the practical constraints of ODLMs for mobile mental health.

---


### 5. [Occamy-1.0: Open Pareto-frontier 35B Intelligence for Co-work](https://arxiv.org/abs/2609.11977)

**<font color=#1a73e8>作者：</font>** Wenhui Chen, Shiwen Cheng, Hao Dong 等 43 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Co-work agents execute complex workflows that combine information gathering, tool use, coding, and file manipulation across many model invocations. Because cost and latency accumulate over the full episode, their practical value depends not only on peak capability but also on how efficiently that capability is delivered. Yet many steps in everyday work emphasize state tracking, coordination, recovery, and follow-through rather than frontier-scale reasoning. We present Occamy-1.0, a cost-efficient co-work model obtained by further training the post-trained Qwen3.6-35B-A3B checkpoint. We construct execution-grounded data and environments, capture replayable long-horizon trajectories across multiple harnesses, and use staged post-training to develop and consolidate complementary execution capabilities. Across a broad suite of co-work benchmarks, Occamy-1.0 is consistently among the strongest comparably sized models and remains competitive with substantially larger frontier systems on several tasks. Under our stated evaluation and pricing protocol, its aggregate performance across four representative benchmarks places it at the low-cost knee of the observed cost--performance Pareto frontier. Supporting evaluations in tool calling, coding, and instruction following further show that this specialization preserves broad agentic capability. We release the model weights and a subset of the training data to support research on practical co-work agents and agentic post-training.

---


### 6. [Harness or Model? Isolating the Harness Effect in Agentic Coding with a Contamination-Controlled Private Suite](https://arxiv.org/abs/2609.11987)

**<font color=#1a73e8>作者：</font>** Mohsen Arjmandi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agentic coding system couples a language model to a harness: the tools, prompts and control flow that turn a chat model into an autonomous software engineer. Vendors ship harnesses tuned to their own models, and practitioners assume the vendor-native pairing solves more tasks. We measure that assumption with paired same-model contrasts on a private, contamination-controlled suite of 256 repository and post-cutoff contest tasks. The same 80 tasks ran under claude-agent-sdk and under deepagents on claude-opus-4-8, and under the openai-codex SDK and deepagents on gpt-5.5, with gemini-3.5-flash and deepseek-v3.2 as side cells. 792 of 800 planned runs were graded by an isolated oracle. Neither contrast resolves an average advantage for either harness: -1.25 pp for Opus 4.8 (48.8% vs 50.0%, task-bootstrap 95% CI [-10.0, +7.5]) and +1.25 pp for GPT-5.5 (55.6% vs 54.4%, CI [-4.4, +6.9]). The Opus average combines opposite strata: the native harness trails by 9.0 pp on the 61 repository tasks and leads by 23.7 pp on the 19 contest tasks (label-permutation p = 0.003). The partition was chosen after seeing the data and needs a designed replication. Correctness and completion also separate: 22 of 81 runs cancelled at the wall-clock ceiling had produced a passing patch. Re-priced from raw per-turn usage at frozen list prices, the neutral harness cost 1.3 to 1.6 times as much per solved task on Opus 4.8 and 1.2 times on GPT-5.5. These are observed-usage estimates. On the Anthropic account 58 runs left no usage record, and allocating that spend to either cell would move the Opus ratio between 0.7 and 2.3, so the billed ordering is unresolved. This revision corrects an August 2026 manuscript whose cost figures rested on a usage-semantics defect in our own telemetry (Section 5.1). We release the orchestrator, grading oracle, reanalysis code and derived aggregates. The tasks stay private.

---


### 7. [Explainable Prediction from Mobile Sensing Data through LLM-guided Concept Integration](https://arxiv.org/abs/2609.11995)

**<font color=#1a73e8>作者：</font>** Yuning Wang, Iman Azimi, Amir M. Rahmani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mobile sensing enables longitudinal monitoring of behavioral and physiological patterns in everyday settings. However, accurate prediction remains challenging in small-cohort health-sensing studies, where task-specific outcome supervision is limited relative to heterogeneous sensing data. Interpretability is also important, as model outputs should reflect meaningful behavioral and physiological patterns rather than predictive scores alone. We develop a Concept-Integrated Transformer (CIT) with LLM-guided concept supervision for explainable prediction from mobile sensing data. CIT uses a pretrained large language model to generate baseline-aware concept abnormality targets with confidence weights without manual concept annotation. Across two longitudinal datasets, CIT achieves the highest F1 score on AFFECT (0.756) and ties for the highest on a PHQ-9 dataset (0.765). The learned concept scores also reveal interpretable behavioral and physiological patterns; in AFFECT, sleep quantity and quality show the clearest difference between high and low negative affect groups. These findings support LLM-guided concept integration for accurate and interpretable prediction in small-cohort mobile sensing studies.

---


### 8. [Fixed State, Long Reach: What a Constant-Size Cache Buys Block Diffusion at Scale](https://arxiv.org/abs/2609.11998)

**<font color=#1a73e8>作者：</font>** Vaibhav Singh, Pierre-André Noël, Torsten Scholak 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Diffusion language models decode tokens in parallel, but their bidirectional denoiser rules out the naive key--value (KV) cache behind fast autoregressive inference. Block diffusion restores caching by decoding block-by-block, and the block caches deployed on it so far are tied to attention: O(L)in memory and, if used as training-free retrofits, only an approximation of the model's computation. Both constraints can be overcome: sequence mixers that summarize finalized blocks into a reusable state support block caching, and the corresponding block-causal training objective makes the cache exact. We study this recipe at scale, pretraining three 3B block-diffusion denoisers (attention, mamba, and hybrid) on 300B tokens under one single-frontier objective and decoding all three through a single cached interface. Only the state-space cache is O(1) in sequence length: its memory and per-step latency stay constant at any context length, while an attention cache remains O(L). At 256k tokens (where attention has grown to 82GB and 29 ms/step), the Mamba cache delivers 4.3x lower latency, 11x less memory, and 2.6x higher single-stream throughput; and because that footprint is constant it scales with batch as well, reaching 14x the aggregate throughput, where attention cannot run beyond a single stream. The same linear-state bias lets the Mamba and hybrid backbones keep retrieving out to 8-16x their training length, whereas attention's retrieval collapses at 2x, at no measured quality cost.

---


### 9. [Can We Trust LLM Judges: A Study of Capability-Dependent Biases and Multi-Judge Ensemble for Bias Calibration](https://arxiv.org/abs/2609.12002)

**<font color=#1a73e8>作者：</font>** Gemma Zhang, Prachi Badarayani, Asmi Kumar 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used as automated judges for model training and evaluation, yet individual judges exhibit systematic biases that undermine reliability. Much of prior work has studied biases in pairwise LLM-as-a-judge settings; in this paper, we focus on absolute scoring tasks, which mirror more realistic use cases. Across four benchmarks and six models (36 judge-examinee pairs), we show that a model's task accuracy strongly predicts its judging accuracy (Pearson $r \geq 0.90$ on most models) and inversely predicts its directional bias ($r \leq -0.83$), but that accuracy alone does not ensure fair evaluation: more capable examinee models consistently receive more lenient judgments from all judges ($r \geq 0.83$). To address this, we propose calibrated weighted majority voting (WMV), an ensemble evaluation method that aggregates multiple LLM judges weighted by online estimates of their false-positive and false-negative rates. We introduce a disagreement-based estimator that derives these error rates purely from inter-judge agreement patterns, requiring no ground-truth labels or task metadata. In a simulated experiment with shifting task distributions, our label-free WMV tracks an oracle with perfect error-rate knowledge to within 0.5 percentage points on average, outperforming both individual judges and unweighted majority voting. These results demonstrate that principled multi-judge calibration can simultaneously improve accuracy and correct for systematic leniency without requiring labeled data, offering a scalable path to reliable automated evaluation as model capabilities increase.

---


### 10. [Feature Recovery for Object Understanding After Irreversible Fire Damage](https://arxiv.org/abs/2609.12078)

**<font color=#1a73e8>作者：</font>** Aditi Tiwari, Sofia Stoica, Savya Khosla 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Objects in post-fire environments often undergo irreversible physical transformations that change their geometry, material state, and visual appearance. Detecting and identifying these remnants is critical for locating hazards, reconstructing pre-incident contents, and inventorying losses. Unlike standard image corruptions, these degradations affect the physical structure of the object itself. To study this setting, we introduce TRACE, a transformation-aware benchmark for post-fire object understanding. TRACE contains 21.4K real-image-grounded synthetic scenes and paired object-level pristine-to-degraded progressions spanning 499 object identities across 189 categories. We define five tasks targeting localization and pre-degradation understanding: degraded-object detection, pristine-state recovery and retrieval, original material recovery, pristine description generation, and functional reasoning. Existing models degrade sharply with severity. From the least to the most severe level, RF-DETR mAP decreases by 71% relative, while InternVL3.5 retrieval R@1 falls from 93.85 to 28.11. To address this, we propose the Feature Recovery Module (FRM), a plug-and-play module that maps degraded encoder features to pristine-aligned representations while keeping the host frozen. Trained only with paired feature supervision, FRM improves scene-level detection, CLIP/SigLIP2 feature recovery, and all four object-level VLM tasks, with larger gains under more severe degradation. Across VLM hosts and severity levels, relative gains average 12.5% for retrieval, 20.1% for material recovery, 13.2% for description generation, and 12.4% for functional reasoning.

---


### 11. [What Counts as a Mistake? Annotating Recitation Events in Quran Memorization Transcripts](https://arxiv.org/abs/2609.12085)

**<font color=#1a73e8>作者：</font>** Mohamad Al Mdfaa, Nursultan Askarbekuly, Ahmed Helaly 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Checking Quran recitation from an ASR transcript requires distinguishing unresolved mistakes from repetitions, repairs, opening formulas and accepted spelling differences. We report a completed human annotation of 100 production recording cases: 348 scored units and 162 localized events across ten combined labels. An executable evaluator scores labels and word positions together. A plain diff reaches label-aware F1 0.525 and localization F1 0.826; adapted production cleaner/alignment components reach 0.518 and 0.786, with exact-span F1 0.505 for both. Correcting the adapter's word coordinates recovers all five annotated repetition events, showing why annotation interfaces must be checked before interpreting baseline failures. In a preliminary pilot, eight single 20-minute runs across three coding agents and eight models span label-aware F1 0.143 to 0.892: seven land far above every baseline, and one collapses below the naive diff from a missing normalization step. Across the six, 970 of 972 gold-event instances draw an overlapping prediction, so what remains is not detection but convention: span extent, and the labels whose boundary is stipulated by adjudication rather than visible in the text. Seven of 162 events defeat all six same-day runs, five of them one orthographic rule, and the strongest run still misses the same ones. No run annotated before building, so the pilot measures the algorithm half of the task only.

---


### 12. [Creating an Atomic User Model for Personality-Aware Large Language Model Interaction](https://arxiv.org/abs/2609.12086)

**<font color=#1a73e8>作者：</font>** B. Sankar, Deepthika S, Pawni Yadav 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Assistants built on large language models are expected to write as their user would, and the dominant approach is single-channel: preferences summarised from conversation history and reinserted into context. This inverts the order of inference. Preferences are the task-dependent surface of a comparatively stable personality structure, so a system storing only preferences relearns the person whenever the task changes. First, we characterise personality seepage, where a prompt's linguistic surface carries a personality fingerprint the assistant mirrors without access to the personality behind it. Second, we propose the Atomic User Model (AUM), a human-readable representation organising a person as a stable identity nucleus with four interpretable shells (psychological, cognitive and experiential, behavioural, and social), plus cross-shell entries recording internal conflict and authenticity. Third, we treat AUM as a retrieval index over a person rather than a prompt prefix, with a pipeline where a task classifier, component-selection function and budgeted retriever return a small payload of fields at generation time. Fourth, we evaluate it with sixteen language-model-simulated participants, six style-sensitive tasks and three seeds, plus a synthetic scaling study of the retriever. Retrieving eight fields matched the style fidelity of the full user model on 23% of the context (211 tokens against 915), improved on flat preference notes by 0.24 points on a five-point scale (p < 0.001, dz = 0.50), and raised forced-choice identification of the participant's own voice from 14.9% to 42.7% (25% chance). Four pre-registered controls returned null, locating the effect in the representation rather than the search over it. The benefit is largest for participants the un-personalised assistant reproduces worst (rho = -0.61, p = 0.013): personalisation is worth most to those the default serves least.

---


### 13. [MAIA: Multi-Agent Intent Articulation for Requirement Discovery in Art Commissions](https://arxiv.org/abs/2609.12097)

**<font color=#1a73e8>作者：</font>** Yu-Chao Wang, Yanhong Lu, Yingjie Victor Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In bespoke art commissions, laypeople know what they feel but lack the words to specify it: one participant wanted a laid-off truck driver depicted as "a ghost in his own machine" but left the medium, scale, and palette unsaid. We frame this as an articulation bottleneck at an under-served upstream stage: requirement discovery, which precedes any artist or image generator and forces the commissioner to constitute intent in the first place. We present MAIA (Multi-Agent Intent Articulation), a multi-agent system that scaffolds this stage through Socratic inquiry under a "Verification over Invention" rule, turning vague affect into a text-only brief of visual terms the user verifies. In a within-subjects study (N = 16), the full configuration produced a large, significant gain in Cognitive Support over a minimal baseline (r = 0.96, p_FDR = 0.015; LMM p_FDR < 0.001). Thematic analysis traces the same mechanism, and a validator gate structurally blocks unratified content. A complementary blind review by three professional concept artists on a sampled set of briefs corroborates this improvement from the artist's side: AI rewriting improved visual completeness and executability in all eight sampled tasks (task-level Wilcoxon p = 0.008; FDR q = 0.010), with directionally larger gains under MAIA than under the baseline (underpowered, d = 1.4-2.6).

---


### 14. [Competence-Gated Pooling of Language Models and Priors for Event Forecasting](https://arxiv.org/abs/2609.12101)

**<font color=#1a73e8>作者：</font>** Aditi Tiwari, Aashrith Bandaru, Heng Ji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In hybrid forecasting, a language model is often one of several available signals. A system may already have a market, crowd, or statistical forecast and must decide whether the model adds useful information or should be ignored. The relevant target is therefore not standalone model accuracy, but relative competence, defined as the model's marginal value beyond the available external forecast. Under Brier loss, we characterize when model disagreement can improve an external forecast and derive the gain from using domain-specific rather than global pooling weights. We then introduce a competence gate that estimates domain-level source weights from resolved outcomes, shrinks uncertain estimates toward a global weight, and recalibrates the pooled forecast. Across 2,357 resolved binary questions and five language models, the gate improves the main external baseline from 0.0771 to 0.0732 Brier and significantly outperforms global forecast combinations. The gain remains significant under leakage controls and against a leakage-safe time-series prior on the pooled structured set, with separate evidence on FRED. In contrast, the gate gives no significant improvement on the official ForecastBench market subset, where it largely defers to the market. Across four Qwen models, verbal confidence does not reliably identify when the model outperforms the external forecast, while outcome-estimated competence supports better abstention decisions. These results provide a practical approach for selective model use based on measured marginal value.

---


### 15. [Language Is an Insufficient Substrate for Quantitative Reasoning, and Consequential Domains Need Large Quantitative Models](https://arxiv.org/abs/2609.12105)

**<font color=#1a73e8>作者：</font>** Reuben Vandeventer, David Imrem, David J. Wild  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The prevailing assumption in applied machine learning is that progress on consequential quantitative decisions such as pricing risk, allocating capital, triaging patients, or containing a network intrusion will follow from progress in large language models (LLMs). A language model is trained on a representation of the world that was produced by human description; description is a lossy encoding of the quantitative record, and the loss is irreversible: no downstream model, at any scale, can recover from a description what the description did not encode. We formalize this as a property of the representation on which a model is trained rather than of the model capacity, and we identify three further properties that consequential settings demand of a model and that a language substrate cannot supply by construction: reproducibility, lineage from every output back to the source records that produced. it, and calibrated uncertainty. We argue that these properties define a distinct model class, which we call the Large Quantitative Model (LQM).

---


### 16. [Extracting Dataset Mentions in Forced Displacement and FCV Documents: A Weakly Supervised Framework with LLM-Based Label Refinement](https://arxiv.org/abs/2609.12107)

**<font color=#1a73e8>作者：</font>** Rafael Macalaba, Aivin V. Solatorio, Patrick Michael Brock 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Development and humanitarian organizations produce and support surveys, administrative registries, and other data resources to inform research, policy, and operations, yet systematically identifying where these datasets are referenced remains difficult. Such references are dispersed across research papers, project documents, humanitarian reports, and other unstructured text, limiting both the ability to trace data use and to identify potential gaps in data availability or dissemination. We present a weakly supervised framework for adapting dataset extraction to forced displacement and Fragile, Conflict, and Violence (FCV) documents without first constructing a large manually labeled training corpus. A lightweight model trained on general research literature generates candidate dataset mentions from unlabeled domain documents, which a frontier large language model (LLM) reviews in context, validating or rejecting candidates and correcting their extraction boundaries. The resulting annotations are supplemented with targeted synthetic and contrastive examples and used to fine-tune the lightweight model for large-scale extraction. We evaluate the resulting model on an independent gold-standard benchmark of 1,706 text passages spanning research, humanitarian, and operational documents. Across the full benchmark, the model achieves 74.1\% precision and 70.5\% recall at the mention level; among passages containing dataset references, precision reaches 89.5\%. At the passage level, the model achieves 88.2\% accuracy and 88.6\% specificity in distinguishing passages with dataset references from those without them. These results demonstrate a practical approach for constructing domain-specific supervision when labeled data are limited, and provide a technical foundation for larger-scale analysis of data use and potential gaps in the displacement data landscape.

---


### 17. [The Cost of Compression: A Rate-Distortion Limit on Factual Hallucination](https://arxiv.org/abs/2609.12111)

**<font color=#1a73e8>作者：</font>** Xi Wang, Shijia Xu, Rongfeng Guo  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Factual hallucination in closed-book question answering is often treated as a coverage problem: a model fails because the relevant fact is absent from its internal memory. This view misses a second source of error. Even when a fact has been observed, finite memory may force it to be stored only approximately. We study this effect through a simple coverage--compression model of factual recall. We consider an unstructured question-answering task with $N$ possible queries and $K$ possible answers. A learner observes $M$ training facts, compresses them into at most $B$ bits, and answers uniformly drawn test queries without retrieval. For a uniformly random ground-truth mapping, we prove $\mathcal{E} \geq \frac{M}{N}\delta^\star\!\left(\frac{B}{M}\right) + \left(1-\frac{M}{N}\right)\left(1-\frac{1}{K}\right)$, where $\delta^\star(r)$ is the inverse rate-distortion function of a uniform $K$-ary source under zero-one loss. The two terms separate compression distortion on observed facts from missing coverage on unobserved facts. The bound gives a compact way to reason about selective memory, forced compression, structure, retrieval, abstention, and long-context organization. We study the predicted signatures with theory-implied simulations and controlled fact-injection probes in modern language models that vary fact load and effective trainable memory. The result is not a complete theory of hallucination, but an information-theoretic account of a separable failure mode: lossy recall of observed facts under finite memory.

---


### 18. [Quantifying Consonant Contributions to Word Intelligibility via Acoustic Masking](https://arxiv.org/abs/2609.12122)

**<font color=#1a73e8>作者：</font>** Eunjung Yeo, Kwanghee Choi, Krupaben Kothadia 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Consonants contribute unequally to whether a word is understood. Given the limited time available for therapy, ranking consonants by contribution to intelligibility helps prioritize intervention targets in motor speech disorders. However, measuring this contribution relies on perceptual studies that are difficult to scale. This paper presents a scalable method that measures consonant contribution using acoustic masking. We silence one consonant at a time in an isolated word and test whether an automatic speech recognition (ASR) model still recognizes the word. We define a consonant's contribution score as the proportion of its masked instances for which the word becomes misrecognized, which we refer to as the mask-induced misrecognition rate (MMR). We validate MMR against two linguistic factors previously reported to correlate with consonant contribution, namely phoneme frequency and functional load. We apply this analysis across four languages, English, Spanish, German, and Czech, using three ASR architectures, MMS (encoder-only), Whisper (encoder-decoder), and Qwen3-ASR (LLM-based). Using partial Spearman correlations, we find that phoneme frequency correlates negatively with MMR while functional load correlates positively. In other words, more frequent consonants are less disruptive when masked, whereas consonants carrying more lexical contrast are more disruptive. Further cross-language analysis shows that consonant rankings are not consistent, indicating that consonant contribution is language-dependent.

---


### 19. [Rank-Efficient LoRA via Joint Tangent-Space Optimization under Isotropic Curvature](https://arxiv.org/abs/2609.12123)

**<font color=#1a73e8>作者：</font>** Zihan Zhu, Zhehang Du, Xuyang Chen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Low-Rank Adaptation (LoRA) is an effective approach for adapting large pretrained models by learning low-rank weight updates. In practice, the LoRA rank is used to control an adapter's parameter budget and representational capacity. We show that this view is incomplete: while the nominal rank determines the representational capacity, the optimizer shapes how much of that capacity is used in the induced weight-space updates. In a case study of GPT-2 adaptation with LoRA, we observe a strong rank-dependent optimizer effect. Despite using the same nominal rank, AdamW often produces per-step updates with concentrated singular spectra and low effective rank, whereas Muon uses a richer set of directions and benefits more consistently from increasing LoRA rank. These observations motivate ISO-LoRA, an optimizer that couples the LoRA factor updates through spectral descent on the induced tangent perturbation in weight space. ISO-LoRA promotes updates that distribute energy more evenly across singular directions, improving rank utilization while preserving compatibility with the LoRA parameterization. We complement this design with theoretical guarantees showing that ISO-LoRA can achieve higher effective rank than standard factor-wise optimizers through a one-step analysis under a stylized spiked-gradient model. We validate this design on language-model adaptation across 0.1B-7B-parameter models, where ISO-LoRA improves effective rank and downstream performance, with the strongest gains at moderate-to-large LoRA ranks. Our results highlight rank utilization as a key factor in LoRA optimization and suggest that optimizer design offers an important path toward stronger parameter-efficient adaptation.

---


### 20. [Local Edits, Global Ripples: Replay-Informed Policy Adaptation for Workflow Synthesis](https://arxiv.org/abs/2609.12127)

**<font color=#1a73e8>作者：</font>** Manqing Mao, Hong Wang, Samson Koelle 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Prompt-policy editing offers a practical way to improve agents that synthesize executable workflows without updating the underlying model. However, persistent prompt editing has two coupled properties. First, edit locality does not imply effect locality: an edit confined to one policy segment can ripple through downstream execution, altering behavior beyond the edited segment. Second, edit effects are composition-sensitive: edits that work in isolation can interfere after composition, causing one or both to lose their benefit or become harmful. Persistent adaptation must therefore support two distinct decisions: identifying where the policy should change from execution feedback, and determining whether the resulting edit remains safe to persist after composition.
To address these challenges, we introduce RIPPLE (Replay-Informed Persistent Policy Localization and Editing), which separates where an edit is made from whether it remains safe after composition. It diagnoses failed trajectories, maps each actionable failure to a predefined policy segment, and restricts the correction to that part of the policy. RIPPLE then evaluates candidates against the same iteration-start policy to compare their isolated gains, before replaying promising edits after previously accepted updates to expose downstream effects and interactions. Only edits that remain safe under composition are retained.
We evaluate RIPPLE on Flow-HO, a synthetic held-out benchmark for executable workflow synthesis. RIPPLE improves validation success by up to 23.1% and yields positive gains on two additional frozen language-model backbones, while maintaining edit efficiency and low execution cost. Targeted interaction analysis further demonstrates both properties: a segment-local tool-use edit changes downstream resource resolution and validation, while an edit beneficial in isolation becomes harmful after composition.

---


### 21. [GUIDE: Generative Utility Inference and Decision Engine](https://arxiv.org/abs/2609.12137)

**<font color=#1a73e8>作者：</font>** Anagha Tiwari, Alexander G. Gray, Nick Feamster 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Measuring the preferences of human users remains a fundamental challenge of AI alignment. Existing elicitation approaches struggle to efficiently discover multidimensional preferences or accurately ground these inferences in domain knowledge. To address this, we introduce GUIDE, an LLM-driven elicitation architecture that infers user preferences through conversations by combining Bayesian adaptive sampling for question selection and symbolic representation learning to initialize domain-specific preference models. GUIDE generalizes adaptive sampling to diverse elicitation questions through an extensible type system of transforms on a parameterized preference state. GUIDE produces domain-specific preference representations through an initialization process using symbolic rule-based learning to capture world knowledge and set priors over preference dimensions grounded in data about decision alternatives. The architecture provides observability and steerability to facilitate deployment and analyze elicitation processes. In silico experiments on investment portfolio optimization demonstrate that GUIDE improves cold-start and minimizes recommendation regret consistently within early elicitation interactions across user personas compared to prior work, LLM-only baselines, and ablated GUIDE versions.

---


### 22. [Can LLMs in Draft-Verify-Revise Pipelines Resolve Deictic Ambiguity?](https://arxiv.org/abs/2609.12162)

**<font color=#1a73e8>作者：</font>** Obinna I. Ekekezie  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Draft-verify-revise is a common LLM orchestration pattern for scaling inference-time compute. One LLM drafts, a second critiques the draft and provides feedback, and a third uses that feedback to revise the draft into the final output. As context cascades between stages, LLMs at different stages can resolve a context-dependent expression such as "previous" differently. When that happens, the expression undergoes a deictic shift, a change in what it refers to. This phenomenon was studied with a synthetic dataset of 10 base examples, each rendered in three conditions. Holding the shared components constant, the conditions varied whether the draft stage LLM (the assistant) or the verify stage LLM (the grader) resolved the expression correctly, and how much independent reasoning the revise stage LLM (the meta-evaluator) needed to determine which reading was correct. Six models from three providers were tested across 21 reasoning effort configurations using e-values for sequential testing, in a primary experiment and an ablation experiment that removed error classification labels from the grader's feedback. A separate LLM analyzed the meta-evaluator's stated rationale for each wrong verdict. Balanced accuracy (the unweighted mean of sensitivity and specificity) ranged from 0.156, below chance, to near-perfect. GPT-5.2 rose from 0.156 without reasoning to 0.942 at its highest reasoning effort level, while Gemini 3 Pro stayed above 0.94 at every level. Gemini 3 Pro at low reasoning effort outscored GPT-5.2 at xhigh reasoning effort for roughly 5% of the cost per trial. When the meta-evaluator erred, it tended to rely on surface cues rather than operational reasoning. Context engineers implementing draft-verify-revise pipelines should be wary of deictic shifts and make the intended referent explicit at each stage.

---


### 23. [WinSyn: An Automated Pipeline for Realistic Enterprise Question-Answering Evaluation](https://arxiv.org/abs/2609.12171)

**<font color=#1a73e8>作者：</font>** Amey Varhade, Ananya Sutradhar, Ravishankar Krishnaswamy 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Enterprise settings provide a challenging environment for question-answering agents, which often rely on Retrieval-Augmented Generation, Deep Research (DR), and related techniques. Much of this challenge comes from the complexity of enterprise data: information is often spread across evolving and potentially conflict- ing emails, chat messages, documents, and other artifacts. Existing benchmarks typically have limited real-world complexity, short-form responses, and unnatural queries, so they often fail to capture the challenges of enterprise settings. In this work, we introduce an automated pipeline for generating synthetic datasets of emails reflecting realistic workplace scenarios, along with long- and short-form questions and gold answers grounded in the data. Our method simulates long-running enterprise projects spanning several months and involving up to 25 interacting employees across multiple roles. The data emphasizes ambiguity, distributed information, and naturally occurring queries. To validate the pipeline, we evaluate few standard agentic baselines on our datasets using the latest frontier models. We find that aggregate scores averaged over all queries remain below 80% for each dataset, indicating significant room for improvement. These findings suggest that more work remains to be done for enterprise deployment and underscore the importance of realistic, high-complexity evaluation data for developing stronger real-world enterprise DR systems.

---


### 24. [Physics as the label for measuring and correcting materials reasoning in multimodal models](https://arxiv.org/abs/2609.12181)

**<font color=#1a73e8>作者：</font>** Hasan Kurban, Rasul Khanbayov, Mustafa Kurban  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language and language models increasingly interpret materials data, yet benchmarks report that they hallucinate invalid properties and violate physical law. Evaluation matches final answers to scarce human labels, while discovery agents verify final proposals or density functional theory (DFT) execution. Neither measures the physical consistency of a model's reasoning chain. Materials data carries its own physics, making a large class of materials reasoning verifiable without annotation. We introduce MatPCR, a label-free benchmark whose programmatic oracles check diffraction geometry through Bragg's law, scale bars, spectral peaks, and Materials Project-grounded checks of near-hull stability, computed band-gap class, and net magnetization. We define the Physical-Consistency Rate over image and structure inputs; introduce Constraint-Grounded Self-Verification, an agentic loop whose gain survives self-refinement and equal-compute re-prompting controls; release an open verifier useful in distribution but near chance on all six held-out constraint types; and derive an exact identity for how oracle error displaces the reported rate.

---


### 25. [GAUGE: When Not to Trust LLM-as-a-Judge in User-Simulated Evaluation of Task-Oriented Agents](https://arxiv.org/abs/2609.12191)

**<font color=#1a73e8>作者：</font>** Umesh Bodhwani, Thanh Tran, Kai Wei  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Comparing and selecting task-oriented LLM agents increasingly relies on a low-cost offline evaluation gate: persona-driven LLM user-simulators converse with each candidate, an LLM-as-a-judge scores the transcripts, and the higher-scoring agent is promoted. We introduce GAUGE, a reusable offline protocol that measures whether this gate's ranking matches a grounded verifiable reward across 25 agents from six providers on the $\tau^2$-bench and SimulatorArena benchmarks, separating two kinds of evaluation validity that release practices conflate: ranking validity and construct validity. First, a satisfaction-success gap: satisfaction carries essentially no information about task success, as conversations rated satisfied by our blind panel are decorrelated from actual success, with 57.5% of them failing the customer's task, a pattern consistent across five rater populations, both benchmarks, and every subjective dimension we rated. Second, while the gate's ranking is robust across the broad capability span, it loses resolution among the near-equal strong agents: this decision-disagreement rate jumps from $<$1% on wide-reward pairs to 31% on close pairs. The gate is thus human-validated yet mis-anchored. As a remedy, we propose a calibrate-then-trust cadence in which a judge-free completion bit is a zero-cost tripwire for truncation regressions.

---


### 26. [Plans They Abandon, Reports They Author: The Narrative Layer of Autonomous Agents](https://arxiv.org/abs/2609.12205)

**<font color=#1a73e8>作者：</font>** Obada Kraishan, Kulsawasd Jitkajornwanich  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> When a coding agent finishes a task, the developer reviews a summary the agent wrote about itself, not a display someone designed. We ask how much of the agent's work that summary carries, and whether it drifts toward the plan the agent stated when execution departed from it. Across 5,851 real developer sessions and 355,942 tool calls, a self-report referred to about one action in eleven, and a reader working from the report alone recovered roughly a fifth of the action log. Neither figure depended on whether the session later needed human correction. Reports did not generally resemble the stated plan more than the executed one, but they did so increasingly as execution diverged from the plan. We hand-validate both measurement steps that use a language model, report the one that failed alongside the one that passed, and draw conclusions only from measures that survived.

---


### 27. [Repair Before Reinforce: Context-Augmented Knowledge Graph Reasoning for Multi-Hop Question Answering](https://arxiv.org/abs/2609.12230)

**<font color=#1a73e8>作者：</font>** Tharaka D. Fonseka, Niraj K. Jha  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Question-answering often requires reasoning across multiple connected facts rather than retrieving a single isolated relation. Knowledge graphs (KGs) provide a structured way to represent such facts, but training large language models (LLMs) only on isolated KG head-relation-tail triples may limit their ability to learn the surrounding context needed for multi-hop reasoning. In this work, we propose a context-augmented training framework for multi-hop question-answering. Although generally applicable, we validate the framework in the context of disease-specific KGs, extracted using a reliable KG extraction framework called GraphMERT, for Gastroparesis and Diabetes. For each primary KG triple, we attach supporting triples extracted from the same source text chunk to form a context graph (CG). This creates two supervision settings: KG-grounded supervision, which uses only the target KG triple or path, and CG-grounded supervision, which uses the target KG triple or path together with supporting context triples. We train the Qwen3-14B model using supervised fine-tuning (SFT) under both settings, producing KGModel and CGModel variants. To strengthen the lower-hop factual foundation of the models, we introduce an LLM-judged, history-aware adaptive repair pipeline that identifies unresolved one-hop failures, continually fine-tunes on targeted repair examples, and removes or quarantines problematic noisy triples. This repair stage enables the models to reach 100% accuracy on the cleaned retained one-hop validation sets. Finally, we employ reinforcement learning (RL) using lower-hop question-answer items and evaluate generalization on harder 3-hop, 4-hop, and 5-hop tasks. Across both diseases, context-augmented supervision consistently improves multi-hop performance over KG-only supervision. RL initialized from repaired SFT checkpoints yields larger and more stable gains.

---


### 28. [Chopthin-Consensus Power Sampling: A Diversity-Preserving Approach to LLM Decoding](https://arxiv.org/abs/2609.12243)

**<font color=#1a73e8>作者：</font>** Minoo Ahmadi, Seyedarmin Azizi, Erfan Baghaei Potraghloo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Inference-time power sampling via Sequential Monte Carlo (SMC) can substantially improve large language model (LLM) reasoning without requiring post-training. However, many existing SMC approaches rely on equal-weight resampling, which can aggressively prune low-weight trajectories, discarding potentially correct reasoning paths and degrading the genealogical diversity of the search space. To address this, we introduce Chopthin-Consensus Power Sampling (CCPS). Our method applies the Chopthin resampler to LLM decoding: rather than equalizing weights and forcing unnecessary particle duplication, it enforces an upper bound on the ratio between the largest and smallest weights and carries the unequal weights forward. This targeted intervention preserves a richer set of distinct reasoning paths, keeps the weighted SMC approximation unchanged in conditional expectation, and guarantees a lower bound on the post-resampling effective sample size (ESS). To fully exploit this enriched population, we employ a semantic-majority selection mechanism that merges token-identical final trajectories, clusters semantically equivalent answers, and returns the answer supported by the largest number of distinct trajectories. Evaluating across three open-weight models and five reasoning benchmarks, we show that Chopthin increases oracle coverage in 13 of 15 settings. Combined with semantic-majority selection, CCPS matches or exceeds the final-answer accuracy of the Power-SMC baseline in 14 of 15 settings, delivering absolute gains of up to 10.6 percentage points. These findings demonstrate that diversity-preserving resampling and diversity-aware selection are complementary mechanisms for training-free LLM reasoning. Code is available at this http URL.

---


### 29. [Automated Detection and Structuring of Social Tipping Point Evidence in Climate related Documents: A Modular AI Framework](https://arxiv.org/abs/2609.12254)

**<font color=#1a73e8>作者：</font>** Kavindu Perera, Mohammad Abaeiani, Ekaterina Gilman 等 17 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The climate literature has grown faster than review teams can read it. That gap matters most for a concept like the environmental social tipping point, the threshold at which a small change triggers rapid, self-reinforcing change in a social system. Evidence of this kind of shift is usually contained in one or two paragraphs within a longer document. As a result, existing text mining tools-which categorize entire documents by topic or highlight isolated claims-leave an expanding set of important evidence without any systematic method for discovery or organization. This paper presents an open and modular transformer-based framework that detects and structures social tipping point evidence at the passage level. The framework joins five components into a single deployable workflow: a DistilBERT boundary splitter for segmentation, an iteratively augmented RoBERTa classifier for detection, a Mistral 7B model that rewrites each detected passage for clarity, a LLaMA 3.2 3B model that rates the passage against five published social tipping point criteria, and a Milvus vector store for semantic retrieval. The system is wrapped in a Streamlit interface backed by MinIO object storage. Evaluated on a 163-passage benchmark labelled by GPT-4.1 and a 51-passage set reviewed by experts, the splitter surpassed three competing methods on a nine-metric composite score (6.137). The tuned RoBERTa model achieved 71.4 percent accuracy with a Cohen's kappa of 0.337 on the full benchmark, and 87.5 percent accuracy with a kappa of 0.742 on passages with labels, outperforming both a climate-focused model and untuned language models.

---


### 30. [HypoKG: Evidence-Disciplined Biomedical Hypothesis Generation Beyond Endpoint Knowledge](https://arxiv.org/abs/2609.12260)

**<font color=#1a73e8>作者：</font>** Dominic Okonkwo, Adetayo Okunoye, Ismailcem Budak Arpinar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate biomedical hypotheses, but it remains unclear whether they truly reason from scientific evidence or simply produce convincing-sounding ideas. To study this, we combine three major biological databases: the Kyoto Encyclopedia of Genes and Genomes (KEGG), Rhea, and UniProt, into a unified biochemical knowledge graph and construct a benchmark of 550 paths connecting enzyme sources to rare disease endpoints, yielding 13,200 hypotheses from six LLMs under four conditions varying the biological information each model receives: source enzyme only, full biological path, or source and disease endpoint only. Hypotheses are scored using an expert-derived five-criterion rubric on a 1-5 scale per criterion. We find that models given both the source and disease endpoint often produce the highest-scoring hypotheses, showing that LLMs can generate compelling ideas from minimal information. However, these hypotheses are less grounded in the evidence. In contrast, models given the full biological path generate hypotheses more consistent with known mechanistic relationships. We call this evidence-disciplined reasoning. To confirm this effect, we shuffled intermediate path steps while keeping endpoints fixed. Evidence grounding dropped significantly (delta = -0.793, p < 0.001), confirming models genuinely used path structure during reasoning. Our findings show that knowledge graphs support hypothesis generation in two ways: they identify biological endpoint pairs absent from the literature, and their mechanistic paths guide how LLMs reason between them.

---


### 31. [GTA: Graph Theory Agent and Benchmark for Algorithmic Graph Reasoning with LLMs](https://arxiv.org/abs/2609.12265)

**<font color=#1a73e8>作者：</font>** Zixiang Xu, Yanbo Wang, Chenxi Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly asked to reason over structured data such as graphs, yet how reliably they can carry out multi-step graph algorithms in language remains unclear. Existing evaluations tend to use simple tasks on small graphs, to score code generation rather than reasoning over the graph itself, or to fix a single input format. We introduce Graph Theory Bench (GT Bench), a benchmark covering 24 classical graph problems in 44 task-structure settings, with over 100,000 examples across four representations: natural language, structured language, adjacency list, and adjacency matrix. Evaluating eight LLMs on GT Bench shows that accuracy is strongly tied to the input representation, that the best representation shifts with graph density, size, and topology as well as with the model, and that this sensitivity persists, attenuated, in the strongest reasoning models. Building on these observations, we propose the Graph Theory Agent (GTA), which pairs a preference-trained representation selector with plan-and-decompose scaffolding around a frozen executor LLM. GTA lifts Phi-4 from 53.5% to 69.1% on the benchmark's easy split and from 33.0% to 41.5% on its hard split, outperforming eight prompting and agent baselines, and transfers without retraining to GraCoRe and NLGraph. Code for benchmark generation and evaluation: this https URL. The project homepage is available at this https URL.

---


### 32. [EAR: Entity-Aware Partitioning Approach for Retrieval-Augmented Generation Development](https://arxiv.org/abs/2609.12268)

**<font color=#1a73e8>作者：</font>** Cenab Batu Bora, Oylum Alatlı, Sebnem Bora 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) can improve knowledge-intensive question answering, but the first design choice is easy to overlook: how should the source corpus be partitioned into retrievable units? Fixed-size chunks often return long passages whose relation to the question is only implicit. We introduce EAR, an Entity-Aware Partitioning approach for multiple-choice question answering (MCQA). EAR extracts normalized surface anchors from the question, answer options, and corpus; retrieves local windows around matching corpus anchors; and can attach a larger parent passage through an extractive summary. We evaluate EAR on a cleaned Massive Multitask Language Understanding (MMLU)-style subset of 153 questions selected by an automatic corpus-support heuristic and using decontaminated public textbook text. Across same-protocol top-k = 3 and top-k = 8 sweeps with Mistral, Gemma, and DeepSeek, EAR entity-window reduces retrieved words by 37.5-40.2% relative to chunks. Observed accuracy changes are +5.2, +1.3, and -3.9 points at top-k = 3, and +5.9, -3.3, and -4.6 points at top-k = 8; none of the entity-window differences is statistically significant. The scoped contribution is methodological: EAR provides a compact and inspectable retrieval unit, while its rule-based anchor extractor remains domain-specific and requires separate validation before transfer.

---


### 33. [Tact: A Zero-Cost, Browser-Based Pipeline for On-Demand Tactile Braille Storybooks](https://arxiv.org/abs/2609.12272)

**<font color=#1a73e8>作者：</font>** Iliano Fasolino  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Braille literacy among blind school-age children has fallen sharply, in part because producing illustrated braille pages still requires specialized software and trained labor. We present Tact, a browser-based pipeline that converts a spoken or typed story idea into printable braille with a matching raised tactile illustration, without an account or mandatory cost and with an offline-capable path. The paper documents the engineering history of the system: its sighted-operator ethical model; hardware rationale for consumer fused-deposition modeling; physical braille geometry and printer calibration; local, hosted, and fallback language-model paths; a deterministic Grade 1 braille translator; verified page layout and pagination; a 93-shape hand-drawn tactile illustration library; and synthesized sound design for a voice-first interface. We report engineering verification, ethical commitments, limitations, and the work required before the system is ready for real blind and low-vision readers.

---


### 34. [Reinforcement Learning over Patient Trajectories for Clinical Reasoning in EHR Foundation Models](https://arxiv.org/abs/2609.12277)

**<font color=#1a73e8>作者：</font>** Yuxin Xiao, Sheng Zhang, Chandan Singh 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Electronic health record (EHR) foundation models trained on longitudinal patient trajectories have demonstrated strong performance across diverse clinical prediction tasks. However, their clinical reasoning capabilities remain constrained by next-token prediction on limited and incomplete EHR data. To address this, we propose a reinforcement learning (RL) fine-tuning framework that treats EHR foundation models as generative policies over patient trajectories. We formulate common clinical prediction problems (e.g., hospital readmission) as event-conditioned, time-windowed reasoning tasks. We then design time-aware, rollout-sensitive rewards to account for finite rollout lengths and temporally inconclusive outcomes. We find that RL fine-tuning consistently improves over pre-trained backbones and strong baselines. Notably, it enables smaller models to surpass larger pre-trained models in data-limited regimes and induces positive transfer across tasks. Further analysis shows that RL fine-tuned models generate trajectories with stronger structural and semantic alignment to ground truth and greater downstream utility.

---


### 35. [T-GADE: Thermodynamical Generative-AI-Driven Evolution of LLM Artifacts](https://arxiv.org/abs/2609.12286)

**<font color=#1a73e8>作者：</font>** Kyoko Ogawa, Naoki Mori  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Integrating evolutionary computation and large language models (LLMs) requires control of population diversity as well as generative capability. Among LLM outputs, those with explicit structure, such as a description paired with code, are structured artifacts; we use artifact for short. We propose T-GADE, which evolves these artifacts by extending thermodynamical genetic algorithms through LLM-based genetic operators and artifact-level diversity evaluation. A common free-energy objective supports generational and steady-state updates, with Fermi-type occupancy excluding repeated genotypes and Bose-type occupancy permitting them. We establish exact one-member removal and conditions for recovering the zero-temperature survival rule of Evolution of Heuristics (EoH). On the online bin-packing task studied in the EoH paper, excess measures relative bin-count overhead above a volume lower bound. Training excess uses search instances; transfer excess uses instances with another bin capacity. Generational Bose-type T-GADE at $T=0.003$ reduced median training excess by approximately 29%, from 1.152% to 0.815%, over 20 runs per configuration (two-sided Mann-Whitney $p=0.042$, Cliff's $\delta=0.378$). Validation selection among its two highest-ranked final candidates reached the same median transfer excess as EoH, 0.496%. These results demonstrate the utility of thermodynamical selection and validation-based use of retained artifacts.

---


### 36. [Breaking the Token Ceiling: Distilling Smaller, Stronger Byte Models](https://arxiv.org/abs/2609.12303)

**<font color=#1a73e8>作者：</font>** Kalyani Marathe, Artidoro Pagnoni, Tomasz Limisiewicz 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small models are made more capable through distillation from a larger one that shares their tokenization scheme. However, do distilled byte and token models behave similarly in terms of scaling trends as compute and data increases? To enable this comparison, we introduce two variants to efficiently convert token logits to Byte Logits: 1) approximate: Marginalize-It, and 2) exact: End-Of-Token. We then present the first large scale study of overtraining decoder-only dense transformer models varying two dimensions simultaneously: the tokenization scheme (Tokens, Bytes, Bytes w/ eot) and the training objective (Distillation vs. Cross-Entropy), sweeping layer-parameter-matched models with roughly 1 billion parameters up to 1 trillion bytes of data. Across eight benchmarks spanning three categories: Multiple Choice QA, Language Generation, and Machine Translation, we find that Token-1B models outperform byte models (End-Of-Token-1B and Bytes-1B) in the low-FLOP regime but eventually plateau; byte models start worse yet surpass Token-1B models with more compute, reaching a higher downstream task performance ceiling. Extrapolating the average top-1 error vs. validation BPB scaling laws predicts that, asymptotically, distilled End-Of-Token-1B outperforms distilled Token-1B by up to 4%. They are also far more data efficient, matching the performance of distilled Token-1B using only one-sixth of the training data. Moreover, by operating over a small vocabulary of 256 bytes instead of on the order of 100K tokens, they circumvent the need for top-k truncation during logit dumping, while also reducing logit storage costs to roughly one-fifth. Finally, our downstream performance scaling laws predict that our distilled End-Of-Token-1B models asymptotically surpass the Llama 3.2-1B, Gemma-3-1B-pt, and Gemma 2B models on averaged downstream tasks by up to 6.5%, 8.1%, and 2.1%, respectively.

---


### 37. [ESTS at WMT26: Routing-Informed Expert Pruning for Model Compression](https://arxiv.org/abs/2609.12310)

**<font color=#1a73e8>作者：</font>** Liu O. Martin, Lucas Bandarkar, Nanyun Peng  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We describe six submissions under the team name ESTS to the unconstrained WMT26 Model Compression Shared Task for English--Simplified Chinese and English--Egyptian Arabic. We submit three compression operating points per translation direction, all derived from GPT-OSS-20B. We use task-specific routing mass to rank experts and cross-lingual routing divergence to allocate retained capacity across layers, then physically remove low-importance experts. The resulting specialists are recovery-tuned on GPT-5.1-generated synthetic translation data and further compressed by applying MXFP4 quantization to the retained expert projection weights. We additionally implement a robust inference system for the instruction-conditioned WMT26 setting, including category inference, output validation, retries, segmented fallback, and source-owned JSON reconstruction. Across our six submissions, parameter counts range from 4.186B to 7.770B and packed artifact sizes from 4.55 to 6.33~GiB. Internal xCOMET-XL evaluation using GPT-5.1 pseudo-references provides an internal comparison across the submitted compression operating points.

---


### 38. ["I Felt Very Seen, But Still Very Alone": Longitudinal Trajectories of General-Purpose LLM Use for Socioemotional Support](https://arxiv.org/abs/2609.12314)

**<font color=#1a73e8>作者：</font>** Meryl Ye, Briana Vecchione, Livia Garofalo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> People increasingly use general-purpose chatbots such as ChatGPT, Claude, and Gemini for mental health and emotional support. We report a multi-stage longitudinal qualitative study of 18 U.S. adults, conducted from April to December 2025, combining initial interviews, a four-week diary study, focus groups, and exit interviews. We find that socioemotional use often emerged gradually out of practical use and when other forms of support were unavailable. Participants developed routines and boundaries around chatbot use, which were disrupted by model updates, evolving public discourse about AI harms, and changes in personal circumstances. We demonstrate how longitudinal study captures factors beyond the human-AI dyad, and argue that HCI researchers and designers should account for users' histories with their chatbots and broader care ecologies when evaluating AI systems over time and introducing updates that may disrupt established sources of support.

---


### 39. [Sampling via Decision-Flow: Training-Free Extraction of Improved Latent Reasoning Paths in Large Language Models](https://arxiv.org/abs/2609.12317)

**<font color=#1a73e8>作者：</font>** Zhendong Mi, Shaoyi Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A central question in LLM reasoning is whether reinforcement learning (RL) instills genuinely new capabilities or merely reshapes how existing knowledge is expressed during inference. Building on the distribution-sharpening hypothesis, which holds that RL reallocates probability mass toward high-reward trajectories already latent in base models, we ask: can we unlock those latent paths without costly RL fine-tuning? We present Decision-Flow Sampling (DF-Sample), a training-free, data-free inference-time framework that constructs a hierarchical reasoning tree, scores terminal nodes for quality, and back-propagates utilities to inform each intermediate branching decision. Unlike conventional sampling strategies that make purely local step-wise choices, DF-Sample performs explicit global trajectory evaluation before committing to a path, recovering high-quality but low-probability reasoning chains that standard decoding overlooks. On GPQA, DF-Sample achieves 45.6% accuracy, surpassing power sampling (38.9%) and GRPO (39.9%), showing that a training-free method can outperform a trained one. Across three models and four benchmarks, DF-Sample consistently outperforms baselines, indicating substantial latent reasoning potential in pretrained base models.

---


### 40. [AIM: A Privacy-Aware Interoperable Memory Framework for Multi-Agent Multi-User LLM Systems](https://arxiv.org/abs/2609.12320)

**<font color=#1a73e8>作者：</font>** Zachary Johnson, Nigel Boachie Kumankumah, Somya Chatterjee 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Traditional large language models (LLMs) are scoped to individual user sessions, limiting their knowledge to a single conversation and preventing them from learning user preferences that evolve over time. Existing agentic memory systems address this limitation but generally operate at the individual-user level, restricting the public knowledge that could be shared across users to improve downstream responses. We introduce AIM (Agentic Interoperable Memory), a unified, privacy-aware memory framework that enables multi-agent, multi-user LLM systems to persistently manage private and shared memory. AIM dynamically classifies information as private, scoped to one user and inaccessible to others, or public, accessible to all users. It enforces index-level access controls so that private memories are retrievable only by their owner, protecting sensitive data while allowing beneficial shared knowledge to improve coordination and consistency. We also introduce MUMBench (Multi-User Memory Benchmark), a dataset of multi-user interactions containing private and shareable information across four domains. To our knowledge, MUMBench is the first public dataset designed to evaluate multiple memory operations, including retrieval, creation, update, and deletion, in a multi-user environment. Across three independent runs on MUMBench, AIM achieves 96.0% visibility classification accuracy, 58.8% strict operation accuracy, and 70.5% state-aware operation accuracy.

---


### 41. [Affective Agent: On-Device Personalized Intervention Reasoning for Wearable Systems](https://arxiv.org/abs/2609.12322)

**<font color=#1a73e8>作者：</font>** Reina Mun, Zishen Wan, Vijay Janapa Reddi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Affective computing has advanced wearable state inference, but on-device reasoning about whether, when, and how to intervene remains challenging. We present Affective Agent, a three-layer reference architecture for personalized intervention reasoning under uncertainty on wearable-class hardware. It combines a compact sub-billion-parameter language model with physiological evidence, context, and user history to decide whether, when, and how to intervene, without cloud dependency or per-user retraining. The architecture is organized into three interacting layers (perception, personalization, and reasoning), adapting to individual users through host-managed structured memory evolution rather than per-user weight updates. We instantiate Affective Agent in indoor environmental quality control and evaluate it on held-out, simulator-generated longitudinal scenarios spanning physiological variation, context, signal quality, and intervention history. Results show that memory-driven personalization and two-pass structured reasoning improve intervention decisions within this synthetic evaluation. By moving the decision layer on-device, this work demonstrates a path from wearable state inference toward closed-loop, personalized intervention on wearable-class hardware.

---


### 42. [Simulating Disengaged Students to Evaluate LLM-based Tutors](https://arxiv.org/abs/2609.12331)

**<font color=#1a73e8>作者：</font>** Xianghui Meng, Jionghao Lin  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Simulated students generated by computational models provide a practical way to evaluate tutoring strategies and pedagogical approaches used by human and AI tutors. However, such simulations should account for disengaged behaviors, including gaming the system, wheel-spinning, and off-task behavior, because tutors may need different responses for different learner states. We present Disengagement-Aware Student Simulators (DAS2), a reproducible pre-deployment protocol that models five learner-engagement states: engaged, gaming, wheel-spinning, off-task, and mixed, and evaluates AI tutor performance across these states. Using ASSISTments09, two coders independently labeled 100 sampled tutoring sessions based on anonymized interaction-log summaries. They achieved 84% agreement (Cohen's kappa = 0.78), and among agreed cases, human consensus labels matched DAS2 rule-based labels in 81% of cases (kappa = 0.75). Conditioning simulations on intended learner states reduced the correctness-rate gap between simulated and authentic sessions from 0.54 to 0.20 for gaming and from 0.51 to 0.18 for wheel-spinning. Fine-tuned Qwen2.5-7B better matched authentic response-time distributions, while prompt-only GPT-4o generated more distinguishable learner states. Evaluation of five AI tutors from the Claude, Llama, Gemini, Qwen, and GPT families showed that relative rankings remained stable across learner states and interaction lengths, while absolute performance varied, revealing state-specific differences in tutor support. Human validation further showed that automated tutor evaluation does not fully align with human judgment. DAS2 provides a pre-deployment framework for evaluating how AI tutors respond to diverse learner-engagement states before deployment.

---


### 43. [I Am No One: Style-Aware Paraphrasing for Text Anonymization](https://arxiv.org/abs/2609.12341)

**<font color=#1a73e8>作者：</font>** Ahmed Sohair Khan, Estrid He, Monica Wachowicz 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Authorship attribution models can re-identify users from seemingly anonymized text by exploiting stable stylistic fingerprints, even after explicit identifiers are removed, posing a growing privacy risk for text publishing and analytics. This risk extends to speech-derived text such as ASR transcripts of meetings and call-center conversations, where stylometric leakage can persist even after acoustic anonymization. Differential privacy-based anonymization often severely degrades text quality and utility. We propose a style-aware, prompt-driven anonymization approach that uses pretrained large language models to construct compact stylistic profiles from minimal samples and rewrite text to suppress identifiable style markers while preserving meaning. Across blog and review datasets, our approach reduces authorship attribution F1 by 60-70% while maintaining content quality and readability, substantially outperforming DP-based and non-DP baselines.

---


### 44. [ParaRecover: A Process-Level Benchmark for Error Localization and Recovery in Parallel Tool-Use Agents](https://arxiv.org/abs/2609.12345)

**<font color=#1a73e8>作者：</font>** Bowen Guan, Zhentao Yin, Yanming Shen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Existing agent benchmarks mainly evaluate final task success or tool-call correctness, providing limited insight into whether agents can reliably diagnose and recover from intermediate execution failures. This limitation becomes particularly critical in multi-turn parallel tool-use scenarios, where errors may propagate across dependent branches and trigger cascading failures. We introduce ParaRecover, a process-level benchmark for evaluating error localization and recovery in multi-turn parallel tool-use agents. Built upon a fine-grained taxonomy of 14 error types covering planning dependencies, tool selection, and argument matching, the benchmark comprises 10,626 instances spanning two difficulty levels. To enable finegrained, process-oriented evaluation, we further propose the SDE rubric, which measures structural integrity, diagnostic reasoning, and evolutionary strategy during agent this http URL across more than ten mainstream LLMs reveal that even state-of-the-art models still struggle with multi-turn error propagation,implicit tool-use failures, and precise replanning. Moreover, we demonstrate that the SDE rubric provides effective supervision signals for improving agents' reflective recovery capabilities. Our data and code are available at this https URL.

---


### 45. [SynthSentry: Detecting Synthetic Data Contamination in Language Model Training Data](https://arxiv.org/abs/2609.12353)

**<font color=#1a73e8>作者：</font>** Praveen Kumar Myakala, Ravichandra Namburi, Sowmya Keragodu Jayaramu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models trained recursively on their own or other models' outputs undergo model collapse, in which distributional tails and factual accuracy deteriorate while fluency survives. Prior work diagnoses collapse after training; the actionable problem is screening a corpus of unknown provenance before training. We introduce SynthSentry, a corpus-level, model-agnostic contamination signal requiring no access to the generating model, no generation history, and no synthetic labels. The score is a distributional divergence over three statistics: lexical diversity collapse, n-gram tail truncation, and perplexity variance across reference models. We evaluate on corpora contaminated by small open-weight generators and an instruction-tuned open-weight model under a leave-one-generator-out protocol. A domain-stratified study measures false positives on naturally repetitive human text (legal, clinical, source code). The score ranks corpora by severity with little loss when whole generator families are held out. Per-domain calibration holds near its nominal false-positive budget once covariance shrinkage and a bootstrap threshold replace a naive quantile, which runs four times over budget. A downstream fine-tuning check showed no contamination-driven accuracy deficit at our scale, so whether pruning recovers one remains open; the same run shows over-pruning risk once pruning exceeds the true contamination fraction. We frame screening as a data-curation defense rather than a post-hoc diagnosis and release the scoring toolkit. All results are small-scale; scope is English-language, batch-mode corpus screening. Contamination sources are single-generation or hand-authored rather than recursively generated, so results speak to synthetic contamination generally and not to recursion depth.

---


### 46. [CueMem: Cue-Guided Context Reconstruction for Long-Term Conversational Memory](https://arxiv.org/abs/2609.12354)

**<font color=#1a73e8>作者：</font>** Changjian Wang, Rongzhen Li, Weili Guan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-term conversational agents must answer user queries by recalling information from extended dialogue histories, yet directly using the full history is costly and often unreliable, while compressed memory units may lose fine-grained evidence needed for question answering. Motivated by the reconstructive view of autobiographical memory, we propose CueMem, a cue-guided framework that treats extracted memory records as retrieval cues rather than self-contained evidence and reconstructs query-relevant dialogue context from their source turns. During memory construction, CueMem extracts fine-grained memory cues from dialogue turns and links each cue to its source turn. At query time, it retrieves query-relevant cues, maps them to source-turn anchors, and expands from these anchors over a turn graph that captures temporal proximity and semantic relatedness, reconstructing a compact evidence context from the original dialogue for LLM answer generation. Experiments on LoCoMo and LongMemEval show that CueMem consistently outperforms representative long-term memory baselines. Further analyses show that graph-based context reconstruction helps recover supporting dialogue evidence while reducing query-time input tokens and latency compared with the full-history LLM setting. These results highlight retrieval cues as an effective alternative to self-contained memory evidence for long-term conversational question answering.

---


### 47. [An Evidence-First Multi-LLM Framework for Auditable Critical-Infrastructure Dependency Modeling](https://arxiv.org/abs/2609.12360)

**<font color=#1a73e8>作者：</font>** Nurjahan, Mst Eshita Khatun, Lamine Noureddine 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Critical-infrastructure knowledge is distributed across heterogeneous, incomplete, and weakly structured evidence, making dependency models difficult to construct automatically and difficult to trust. Large language models (LLMs) can extract structured knowledge from such evidence, but direct LLM-to-graph generation risks unsupported relationships, inconsistent terminology, incorrect entity identities, and erroneous dependency endpoints. We present an evidence-first multi-LLM framework for constructing Infrastructure Knowledge Bases (IKBs) and Infrastructure Dependency Graphs (IDGs) from heterogeneous infrastructure documentation. Multiple open-weight LLMs independently extract candidate entities and dependencies from normalized evidence, after which the framework separates evidence verification, ontology grounding, entity resolution, dependency alignment, validation, fusion, and human review. Evidence support, ontology reconciliation, endpoint resolution, model agreement, and human validation remain distinct states, while provenance and unresolved cases are preserved throughout. The validated IKB is then projected deterministically into the IDG without introducing new LLM-generated knowledge. Evaluation in nine infrastructure projects shows that entity recovery achieves substantially higher recall than complete directed dependency recovery and that canonical endpoint resolution is a major constraint in dependency construction. Cross-model overlap is also much lower for dependencies than for entities, indicating that the models often produce non-overlapping candidate assertions rather than a stable majority consensus. These findings support an auditable evidence-to-IKB-to-IDG process in which uncertainty is preserved and resolved progressively rather than collapsed into a single confidence or voting decision.

---


### 48. [ORQA: An Occupation-Realistic Question and Answer Framework for LLM Professional Knowledge](https://arxiv.org/abs/2609.12366)

**<font color=#1a73e8>作者：</font>** Shreyas Krishnan, Serina Chang, Abhishek Nagaraj  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present ORQA, a method for testing occupation-level knowledge in large language models. Prior methods either map abstract LLM skills to occupations via task definitions or utilize expert knowledge which is difficult to obtain at scale and expensive. ORQA complements both of these methods by connecting O*NET occupations to trusted occupation-specific websites (such as regulatory agencies, licensing bodies, professional organizations, and government publications) and converting these into source-traceable question-answer pairs. A combination of an automated pipeline and human review produces a set of high quality questions about occupations. The question set created via our method covers 116 occupations from all 21 major groups in the SOC, with 480 questions sourced from 187 different websites. Each question is designed to probe a real-world skill question that is relevant to the occupation in question. We test 15 state-of-the-art frontier and open-weight models via this method. Claude Opus 4.6, GPT-5.4 and Claude Sonnet 4.6 all perform the best at approximately 58-62% while smaller open-weight models achieve approximately 33-41% performance. Performance varies significantly across occupations. Healthcare-related occupations achieve the highest performance (78%) while Office and Administrative Support achieve approximately 40%. Performance on individual occupations (e.g. Sheet Metal Workers and Fish and Game Wardens) is essentially zero. We also find that open-ended questions and weighting by wage bill do not significantly affect the ranking of models on this benchmark. We believe that leveraging existing trusted occupation-specific information to test LLM knowledge in professional domains may be a scalable and useful method for evaluating occupation-level AI performance in the future. Results and data are available at this http URL.

---


### 49. [Toward Robust Personalized Alignment for LLMs: Mitigating Persona Drift in Multi-Turn Dialogue](https://arxiv.org/abs/2609.12373)

**<font color=#1a73e8>作者：</font>** Youyuan Zhang, Siyuan Li, Fangming Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persona drift remains a central challenge for personalized language models, as user profiles evolve over long interactions rather than remain permanently fixed. Models must therefore revise persistent persona states when preferences genuinely change, while avoiding updates driven by transient, ambiguous, or unresolved observations. We propose CORE, which separates turn-local evidence from persistent persona-state revision and selectively updates grounded user preferences through uncertainty-aware belief revision. We also introduce PERSIST, a held-out post-anchor benchmark for persona-state robustness under sequential interaction stress, covering ambiguity, conflict, and controlled social influence. Across ALOE, PersonaChat, and PERSIST, CORE improves personalized alignment and robustness, with complementary gains in normalized closed-slot state fidelity. Human evaluation and mechanistic controls further support explicit update control beyond stronger generation or persistent memory alone.

---


### 50. [An Open-Source End-to-End FHE Implementation for Privacy-Preserving Llama 3 8B Inference](https://arxiv.org/abs/2609.12378)

**<font color=#1a73e8>作者：</font>** Yuhang Fan, Yusi Chen, Kanyu Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cloud LLM services typically require users to send prompts to a model provider, creating a privacy risk. Fully homomorphic encryption (FHE) lets a server perform inference without decrypting the input, but representing data as ciphertexts adds storage and computational overhead. In CKKS-based LLM inference, the packing scheme maps logical tensors to ciphertexts and slots. It therefore determines the ciphertext count and the homomorphic cost of linear layers, and it constrains how data pass between linear layers, attention, and nonlinear computation. As models and sequences grow, inefficient layouts accumulate encoding, compute, and layout-conversion overhead.
We present Odin, an FHE inference system that co-designs ciphertext packing and model execution for Llama. Starting from a THOR-style baseline whose bottleneck is weight encoding, Odin uses a feature-major cross-layer layout to unify residual connections and layer interfaces, and builds transient intra-operator layouts for linear projections and attention. This reduces redundant plaintext encoding of weights in wide projections. Within attention, QK^T produces scores that Softmax can consume directly, and PV consumes the resulting probabilities, avoiding intermediate repacking. For nonlinear ops, we use minimax polynomial approximation with input-range control and joint error allocation guided by model quality, reducing polynomial degree and multiplicative depth. To our knowledge, Odin is the first open-source end-to-end GPU CKKS implementation of Llama-3.
With Llama-3-8B weights and a 128-token input, Odin evaluates all 32 Transformer layers on a single NVIDIA H100 80 GB GPU. Server-side end-to-end FHE evaluation takes 366.4 s and 58.9 GiB peak device memory. Under the same model, input, CKKS parameters, and hardware, THOR takes 1651.9 s, a 4.51x speedup.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-134](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
