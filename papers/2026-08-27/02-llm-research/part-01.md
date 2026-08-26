# 🧠 大模型相关研究 | 2026年08月27日

> 本类共 **190** 篇论文：已确认 **178** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-190](./part-04.md)

---

### 1. [RENDER: Controlling Reader-Facing Evidence in LLM Memory Evaluation](https://arxiv.org/abs/2608.23568)

**<font color=#1a73e8>作者：</font>** Yuan Si, Simeng Han, Daming Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Memory and RAG evaluations often treat the answering model's input as an implementation detail, even though systems may render the same history as a memory entry, summary, typed record, or raw excerpt. We introduce RENDER, a benchmark control that fixes the conversation while varying the reader-facing artifact. RENDER combines a five-level packet ladder, localizing when answer-bearing content enters the input, with deterministic templates approximating ChatGPT-style entries, LangChain summaries, MemGPT-style typed records, and raw conversation. On 500 LongMemEval questions and nine models, matched-budget resolved packets beat recency-truncated raw dialogue by 42.4-72.6 points. In deployed-style templates, best-worst spread is 24.6-48.8 points per model; under the primary scorer, ChatGPT-style entries have higher point estimates than raw conversation on 7 of 9 models. Judge rescoring preserves the positive aggregate effect, but model-specific significance is mixed. Three models scoring 0 percent on formal ledger packets answer the same facts from natural-language entries at 45.4-53.4 percent. The effect persists under retrieval noise and transfers to HotpotQA, suggesting that memory/RAG evaluations should report or control the reader-facing artifact.

---


### 2. [ESQ-Bench: A Multi-Tier Enterprise Oracle Benchmark for Evaluating NL2SQL Dialect Generalization and Silent Semantic Divergence](https://arxiv.org/abs/2608.23569)

**<font color=#1a73e8>作者：</font>** Sanjay Mishra, Divya Chukkapalli, Ganesh R. Naik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> State-of-the-art Natural Language to SQL (NL2SQL) models report execution accuracy exceeding 89 percent on established benchmarks such as Spider and BIRD. However, these benchmarks rely on simplified academic schemas and open-source SQL dialects that do not reflect the complexity of enterprise database environments. We introduce ESQ-Bench, an Oracle-first NL2SQL benchmark with systematic complexity tiers and silent-divergence evaluation across three enterprise schema complexity tiers. We constructed and released six populated schemas (465 tables, 164,682 rows, zero empty tables) with identical seed data on Oracle, PostgreSQL, MySQL, and SQL Server, a four-metric evaluation harness (EM, EX, SR, SD), and 550 gold-validated question-query pairs (Tier-1: 95; Tier-2: 228; Tier-3: 227). Schema-linked prompting with GPT-4o shows monotonic execution-match degradation across tiers: 79.8, 60.3, and 57.2 percent EX on executed queries (June 2026), versus 75.6, 80.4, and 95.8 percent on an earlier 142-question pilot slice. EM stays below 7 percent tier-wide; operational silent-divergence reaches 73 to 99 percent among EX-passing queries. Failure analysis shows wrong-result semantics dominate at higher tiers. Claude Sonnet 4.6 with schema-linked prompts reaches 87.4, 74.9, and 68.7 percent EX (executed queries), exceeding GPT-4o schema-linked on every tier. GPT-4o zero-shot EX on executed queries (78.7, 73.5, and 77.8 percent) inverts schema-linked at Tiers 2 to 3 due to lower execution rates and survivor bias in the zero-shot versus schema-linked analysis. Local Llama 3.2 schema-linked reaches only 13.3 percent bank-wide EX (73 out of 550), underscoring the gap between closed API models and open-weight baselines on enterprise Oracle schemas.

---


### 3. [Taming Visual Neglect: A Variational Information Bottleneck Framework for Adaptive Attention in Multimodal In-Context Learning](https://arxiv.org/abs/2608.23570)

**<font color=#1a73e8>作者：</font>** Kaito Tanaka, Yuji Nishimura, Keisuke Matsuda 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large vision-language models exhibit strong in-context learning (ICL) capabilities, yet when and why visual context helps multimodal ICL remains poorly understood. Empirical studies show a puzzling dichotomy: models sometimes effectively leverage visual demonstrations, yet often neglect them entirely. We propose VIB-ICL, an information-theoretic framework that resolves this dichotomy through the Information Bottleneck principle. We introduce the Cross-Modal Information Gain (CMIG), which quantifies the additional mutual information that visual context provides about the target beyond textual context. We derive a generalization bound showing that multimodal ICL's excess risk over text-only ICL is governed by the CMIG, proving that multimodal ICL provably outperforms text-only ICL when visual information is non-redundant. We further prove that visual context neglect, often viewed as a failure mode, is the Information Bottleneck-optimal solution when visual information is redundant, yielding a closed-form Attention Reallocation Principle that prescribes how visual attention weights should be adaptively adjusted. We instantiate this principle in the VIB-ICL algorithm, which estimates CMIG via variational bounds and dynamically reallocates attention. Experiments on five benchmarks demonstrate consistent improvements of up to 4.7\% accuracy gains and 35\% reduction in required demonstrations, validating our theoretical predictions.

---


### 4. [LLM Agents Perform Controlled Experiments Using Simulation Models](https://arxiv.org/abs/2608.23622)

**<font color=#1a73e8>作者：</font>** Yuchen Xia, Michael Weyrich, Nasser Jazdi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have shown strong capabilities in reasoning, planning, and tool use, but many scientific and engineering tasks require more than plausible text and code generation. They require understanding how a system responds to intervention, which in practice depends on controlled experimentation. In this work, we propose a multi-agent framework that enables LLM agents to conduct controlled experiments with scientific simulation models for pharmaceutical process design. Given a user query and a baseline configuration, the system constructs a structured task representation, designs experiments, executes comparative simulation, interprets the resulting outcomes, and synthesizes evidence-based recommendations for process parameter optimization. By coupling language models with high-fidelity simulation models in an interactive agent framework, the proposed system supports reasoning through intervention, comparison, and observation. As a result, it produces more specific and actionable outputs than language-only reasoning. In an industrial application setting, this advantage is reflected in higher output specificity as well as improved user-rated correctness and helpfulness. Ablation studies and visualized case analyses further demonstrate the effectiveness and practical utility of simulation-integrated experimental reasoning.

---


### 5. [From Triage to Discharge: A Survey of NLP Tasks, Methods, and Open Challenges in the Emergency Department](https://arxiv.org/abs/2608.23627)

**<font color=#1a73e8>作者：</font>** Dipankar Srirag, Aditya Joshi, Salil Kanhere 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emergency departments (EDs) operate under time pressure, generating multimodal data such as clinical conversations, triage notes, and discharge documents. Recent advances in natural language processing (NLP), particularly pretrained transformers and large language models, have created new opportunities to support language and time-intensive stages of emergency care. Yet existing surveys map clinical NLP across the broader hospital workflow or focus on specific tasks. This survey analyses 46 papers spanning the three phases of ED: triage, diagnosis, and disposition, covering tasks such as triage classification, clinical summarisation, automatic diagnosis, report generation, and discharge documentation. We examine modelling paradigms, evaluation practices, and emerging benchmarks and shared tasks. Across tasks, we identify common trends, including a shift from task-specific neural architectures to pretrained language models, growing interest in interactive clinical systems, and increasing attention to clinically grounded evaluation. Finally, we detail open challenges such as limited generalisability, noisy clinical inputs, and workflow constraints that inform future ED-NLP research.

---


### 6. [TRACE: Transition-Aware Residual Control for Multi-Objective Materials Discovery](https://arxiv.org/abs/2608.23631)

**<font color=#1a73e8>作者：</font>** Kang Zhou, Yujia Tong, Yong Tao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-objective materials discovery with LLM agents is often limited not only by how many candidates can be proposed, but by how effectively each costly property evaluation informs the next search step. Existing agents mainly store evaluated candidates and their scores, so they know which materials succeeded but not which executable edits caused useful property changes. This makes local refinement difficult when objectives compete and an edit that improves one property may damage another. We propose TRACE, a transition-aware residual control framework that treats evaluated edits as the basic unit of feedback. TRACE records each local refinement as a parent-edit-child transition with observed property deltas, aggregates transition evidence to estimate reusable edit effects, and ranks future edits by their predicted ability to reduce the current candidate's remaining constraint violations while avoiding damage to already satisfied objectives. In a controlled same-backbone comparison, TRACE improves over LLEMA, the state-of-the-art LLM-agent baseline, raising macro-average hit rate from 18.13\% to 25.96\%.

---


### 7. [Function-Level Execution Feedback for Code Preference Optimization](https://arxiv.org/abs/2608.23632)

**<font color=#1a73e8>作者：</font>** Idris Nechnech, Sehwan Kim, Jimin Seo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Process supervision has improved mathematical reasoning, where intermediate steps are naturally expressed as chains of thought. In code generation, however, process supervision remains underexplored because there is no standard notion of a step. Supervision can target lines, reasoning traces, or program states, making it unclear what to label and optimize. We propose STEP-KTODER, a framework for code preference optimization that defines steps as module-level functions in decomposed multi-function programs and assigns binary correctness labels via automatically generated unit tests. Our method provides a code-specific instantiation of stepwise KTO, combining function-level process supervision with outcome-level feedback on the full program. We evaluate on HumanEval(+), MBPP(+), BigCodeBench, and LiveCodeBench, showing that STEP-KTODER improves over outcome-only KTO and DPO. Further analysis shows that execution-based labels are essential: LLM-as-a-judge annotations systematically over-predict function failures, corrupt positive step labels, and degrade downstream preference optimization. Code is available at: this https URL.

---


### 8. [The Blending Ratio Is Not Where the Performance Is: Diagnosing Prototype Blending for Few-Shot Adaptation of Vision-Language Models](https://arxiv.org/abs/2608.23634)

**<font color=#1a73e8>作者：</font>** Liangzhi Li, Bowen Wang, Yiming Qian 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Many few-shot adaptation methods for vision-language models classify with a convex combination of the zero-shot text prototype and the mean of the K labelled image features, with a single blending ratio routinely tuned on held-out labels, often on the test set itself. We ask what the family's own bias-variance justification invites: what is the right ratio, can it be estimated without validation data, and is finding it where the performance is? First, the ratio minimising prototype mean-squared error has a closed form whose support-set plug-in is exactly a positive-part James-Stein coefficient shrinking towards the text prototype. Across 4,800 cells (ten datasets, five backbones including SigLIP, five shot counts, five seeds, four prompt tiers) this theoretically optimal ratio is a reliable estimate of the wrong quantity: on the 950 primary-tier cells where it is defined it trails a test-set-oracle ratio by 8.5 points. It saturates near 1, discarding the text prior for a nearest-class-mean classifier, because 78% of the text-image prototype distance it treats as bias is a class-independent offset that the arg max largely cancels. We prove the mechanism and bound its share of the damage at 26% by a counterfactual. Second, leave-one-out on the support set alone sets a ratio landing within 0.9 points of the oracle blend, so it is estimable without validation data. Third, validation-free linear probes beat even the oracle-tuned blend: CLAP by +1.9 points and LP++ by +1.5 on average, and at K >= 4 all four validation-free baselines sit above the oracle, the linear probes by margins excluding zero. These results locate the ceiling in the model class, not the hyperparameter: the ratio can be set near-optimally for free, and it is still not where the performance is. Code, cached features, per-cell records: this https URL

---


### 9. [Auditing the Synthetic Memoir: Measuring Scene-Level Confabulation in LLM-Generated Autobiography Against the Documented Record of the Life It Describes](https://arxiv.org/abs/2608.23640)

**<font color=#1a73e8>作者：</font>** Heather Renze  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When a large language model (LLM) is asked to write a person's life, how much of what it writes actually happened? We present a scene-level case-study audit - the first quantified audit of LLM-generated autobiography against a subject-specific ground-truth corpus that we are aware of, based on an unsystematic literature search. The subject and the author of this paper are the same person: a 366-day "page-a-day" book of first-person anecdotal entries was drafted with a conversational LLM whose documented inputs were a template, two exemplar days, and each day's quote - not her corpus - and every day was subsequently audited at the anecdote-scene level against an independent verification corpus using a four-level rubric fixed before analysis. We define the verification-failure rate as the share of days not rated VERIFIED (scene positively corroborated): 354 of 366 days fail, 96.7% (Wilson 95% CI 94.4-98.1%). Only 12 days contain a corroborated scene; 19 days (5.2%) assert claims actively contradicted by the record; the dominant failure mode is grounded drift - real people, employers, and settings inside invented scenes - though its measured share varies across raters. Independent re-rating replicates the headline (no evidence the original rate was inflated) while showing that the four-way taxonomy has only fair-to-moderate reliability. Regenerating the same days with current named models reproduces 100% verification failure under the same inputs; grounding generation in the subject's corpus significantly improves the verification rate while leaving substantial residual failure (83.3%). We contribute the measurement, a reusable audit instrument whose WEAK/UNVERIFIED boundary we show to be unreliable, and a grounding remedy with quantified effect.

---


### 10. [Ethical LLM-Assisted Research: A Framework for Responsible Delegation, Verification, and Epistemic Value](https://arxiv.org/abs/2608.23644)

**<font color=#1a73e8>作者：</font>** Kalin Stoyanov  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are becoming routine instruments of scientific research, assisting with literature synthesis, hypothesis development, coding, and formal reasoning. Their use raises a central epistemic question: when parts of scientific reasoning are delegated to an artificial system, what conditions must remain under human control for the resulting knowledge claims to retain epistemic legitimacy and accountable authorship? This paper develops a normative and conceptual framework for analyzing such delegation. Scientific reasoning is treated as a distributed process in which the origin of a contribution may vary between human and machine, while responsibility for its acceptance into the scientific record remains human. The framework distinguishes content origin $O(g)$, completion of human verification $V(g)$, responsibility assignment $R(g)$, accountable human ownership $M(g)$, and epistemic outcome $E(g)$. These constructs separate the provenance of a claim from the process by which it is checked, the epistemic outcome of that checking, and the human responsibility attached to its disposition. The central proposition is that the ethical boundary of LLM-assisted research is determined primarily by adequate verification and accountable human ownership rather than by the degree of machine involvement itself. On this basis, the paper develops the notion of an \emph{epistemic audit}: a structured record of delegation, verification, provenance, and responsibility intended to make AI-assisted reasoning transparent and reviewable. The resulting framework provides a formal vocabulary for distinguishing responsible cognitive delegation from the transfer or neglect of epistemic responsibility in scientific research.

---


### 11. [MolEmb: Multimodal Large Language Models Can Be Strong Molecular Embedding Models](https://arxiv.org/abs/2608.23646)

**<font color=#1a73e8>作者：</font>** Xinjian Zhao, Xiangru Jian, Yaoyao Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Molecular embedding models can serve as foundational infrastructure for computational chemistry and drug discovery, where reusable vector representations support property prediction, virtual screening, and retrieval. Most molecular encoders are specialist models built around a single molecular view, producing unconditional vectors with no language interface for varying the representation. We ask whether multimodal large language models (MLLMs), which natively process images, text, and symbolic inputs, can instead serve as \emph{general molecular embedding models} that produce embeddings conditioned on both a molecular profile and a natural-language semantic context. We introduce \textbf{MolEmb}, a lightweight framework that adapts MLLMs by aligning molecular profiles with textual descriptions in a shared embedding space using a bidirectional contrastive objective. The resulting embedding model is competitive on molecular property prediction and supports cross-modal molecule--text retrieval in the same space. We further introduce \textbf{MolCAR}, a diagnostic benchmark for context-aware retrieval, and find that context-aware molecular embedding is primarily a data property of the supervision. These results suggest that MLLMs are not merely chemistry assistants or generators, but a viable and extensible route to general molecular embedding models.

---


### 12. [From Causal Plausibility to Causal Reliability: Evaluating LLMs as Calibrated Direct Causal-Edge Classifiers](https://arxiv.org/abs/2608.23660)

**<font color=#1a73e8>作者：</font>** Amit Kumar, Elnur Adl Zarabi, Suranjana Trivedy 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to provide prior causal knowledge for structural causal discovery, yet whether their direct-edge judgments and confidence can be trusted remains unclear. We systematically evaluate 12 instruction-tuned open-weight models across six benchmark causal graphs, five prompting strategies, and four confidence sources: verbalized, logit-based, cross-prompt agreement, and cross-model agreement. Under our language-only pairwise protocol, our evaluation yields three key findings. (i) LLM-based causal judgments are strongly recall-dominant: models predict overly dense graphs with many false-positive edges, while prompting mainly shifts the precision-recall trade-off rather than resolving overprediction. Gains from model scale diminish on the largest graphs and do not eliminate miscalibration. (ii) LLMs often capture causal relatedness without reliably identifying directness or orientation. Relative to published reference graphs, models misclassify 40.0% of indirect and 36.0% of reversed non-edges as direct edges, versus 28.2% of other non-edges. Moreover, 80.8% and 84.6% of these false positives receive verbalized confidence of at least 80%, revealing substantial overconfidence in structurally incorrect predictions. (iii) Conventional confidence estimates are unreliable, whereas agreement offers a more promising signal. Logit-based confidence frequently collapses near 1.0 regardless of correctness, while cross-prompt and cross-model agreement achieve better mean calibration and discrimination, though their advantages are not statistically significant after Holm correction. A benchmark-familiarity audit further identifies potential familiarity in five model-dataset pairs, all involving AsiaM. Overall, our results suggest LLMs are better viewed as sources of externally validated soft causal priors than as direct evidence of causal structure.

---


### 13. [Scaling Reinforcement Learning for Diffusion Models via Velocity Matching](https://arxiv.org/abs/2608.23664)

**<font color=#1a73e8>作者：</font>** Jaemoo Choi, Wei Guo, Yuchen Zhu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reward fine-tuning is becoming an important tool for adapting diffusion models to human preferences and task-specific objectives, but existing methods largely inherit policy-gradient machinery from large language models. Unlike autoregressive models, diffusion models do not provide tractable likelihoods for generated samples. As a result, current approaches either construct trajectory likelihoods from stochastic denoising transitions or approximate endpoint likelihoods with evidence lower bound, introducing additional computation and algorithmic complexity. We demonstrate that this likelihood-based machinery is not necessary for effective diffusion reward fine-tuning. We propose reward-based velocity matching (RVM), a simple trajectory-free update that acts directly on the velocity field. RVM reinforces directions associated with high-reward generations, suppresses those with low reward, and involves an optional anchor term controlling drift from a reference velocity. Notably, it provides a general framework that recovers recent fine-tuning methods, including RAM and DiffusionNFT, as special cases. Across various large-scale diffusion models reward fine-tuning tasks, RVM is competitive with or outperforms trajectory-based policy-gradient methods under substantially reduced training cost. We further find that, once the velocity update is simplified, the particular loss variant matters less than reward and anchor design. For video generation, standard preference rewards can favor visually clean but nearly static outputs; introducing a new dynamic-tracking reward that substantially improve motions while improving overall VBench performance. These results suggest that scalable reward fine-tuning for diffusion models is better posed in the native velocity representation than as likelihood-based policy optimization.

---


### 14. [Gated Activation Steering for Reducing Sycophancy & Hallucination in Medical Question Answering](https://arxiv.org/abs/2608.23666)

**<font color=#1a73e8>作者：</font>** Himanshu Tripathi, Subash Neupane, Shaswata Mitra 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sycophancy and hallucination are persistent failure modes of Large Language Models (LLMs) across domains. However, it becomes particularly consequential in clinical question answering, where responses must remain grounded in the provided context and robust to user pressure. Hallucination can introduce information that is unsupported by the context, while sycophancy can cause a model to abandon a previously correct answer when challenged by the user. Existing approaches, such as prompt-based safeguards and always-on activation steering, often address these behaviors separately or apply interventions broadly across turns, which can unnecessarily deteriorate responses that were already correct. To address these limitations within a single framework, we employ Inference Time Intervention (ITI) to jointly control both behaviors by learning separate steering directions for hallucination and sycophancy from contrastive clinical pairs and applying them to causally verified attention heads. During runtime, behavior-specific gates then determine when intervention is needed: the hallucination component mitigates unsupported claims, while the sycophancy component mitigates answer shifts caused by user pressure. We evaluate this framework on clinical questions grounded in EHR data while keeping the model weights frozen. Across all evaluation settings, we conducted 15,900 model-response runs. Across 600 pressure trajectories for the 4-billion-parameter model, the unsteered model caved in 570 cases. At the same time, gated steering helped it last longer in 551 of them. It held its ground under pressure at levels comparable to those of models with more than 100 billion parameters, showing that targeted inference-time steering can improve robustness without intervening at every turn.

---


### 15. [Automata from Agent Traces: Failure and Next-Step Prediction](https://arxiv.org/abs/2608.23670)

**<font color=#1a73e8>作者：</font>** Seonglae Cho, Franklin Cardenoso Fernandez, Umar Mohammed 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based agents execute multi-step tasks, but their behavioral structure remains opaque: long unstructured traces resist the safety auditing and runtime monitoring that deployment requires. Existing approaches operate per-trace or success-only, so they miss the cross-run topology that links next-step and failure prediction. To recover that shared structure, we collapse an entire trace corpus into a single, compact finite-state machine (FSM) that serves as a structural substrate for the otherwise unpredictable behavior of LLM agents. Across twelve public datasets, the FSMs are compact (7-43 states), replay held-out data at >=0.997 fitness with near-identical topology across splits, and build in milliseconds. This substrate addresses both prediction goals. For next-step prediction, FSM-state context outperforms Agent Workflow Memory on every ground-truth-matched dataset. For failure prediction, per-state behavioral features reach held-out AUROC up to 0.94, and an online monitor ranks failing runs above passing ones from a partial trace, triggering early stopping well before completion. Behavioral topology thus appears shaped more by the deployment harness than by the LLM, providing a model-agnostic structural primitive for safety auditing and runtime monitoring.

---


### 16. [The Limits of Automatic Evaluation of Creativity in Large Language Models](https://arxiv.org/abs/2608.23705)

**<font color=#1a73e8>作者：</font>** Alessandro Tutone, Giorgio Franceschelli, Mirco Musolesi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly capable of generating text that challenges human performance in domains requiring creativity, yet evaluating creativity in LLM-generated content remains a significant challenge. Here, we investigate whether current automatic evaluation methods can reliably capture human judgments of creativity. We collect human evaluations of human- and AI-generated short stories from the WritingPrompts dataset across 11 dimensions of creativity, and compare these judgments with automated objective metrics and LLM-as-a-Judge evaluations. Our experiments reveal substantial misalignment between automatic evaluations and human assessments. In particular, LLM-based judges exhibit a systematic preference for AI-generated stories, consistently favoring their stylistic characteristics over the unpredictability and other qualities of human-authored texts. Furthermore, correlation analyses show that widely used automatic metrics exhibit near-zero alignment with human judgments across both human- and AI-generated stories, suggesting that they fail to capture important dimensions of creativity. These findings highlight fundamental limitations in current approaches to the automatic evaluation of creative text and underscore the difficulty of reducing the multidimensional and subjective nature of creativity to computational metrics.

---


### 17. [Do LLMs Understand Limit Order Book Dynamics?](https://arxiv.org/abs/2608.23706)

**<font color=#1a73e8>作者：</font>** Junxiao Chen, Paul Glasserman  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A large language model (LLM) trained on synthetic limit order book (LOB) data achieves near perfect scores in generating valid sequences of LOB events. However, the LLM's implicit world model fails to learn the state of the LOB. This deficiency leads to biased estimates and spurious predictability in using the LLM to forecast future LOB events. Our analysis uses novel tests of an LLM's world model, extending prior work from deterministic settings to the stochastic dynamics needed for the LOB.

---


### 18. [ADE: Agentic Data Evolution Framework for Human-Centered Objectives](https://arxiv.org/abs/2608.23719)

**<font color=#1a73e8>作者：</font>** Yang Yu, Yilin Jiang, Zexuan Fei 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Aligning large language models to human-centered objectives is difficult when targets are non-executable and context-dependent, limiting reliable verification and scalable supervision. Although synthetic data expands coverage, weak verification shifts the bottleneck from generation to selection. Noisy signals destabilize iterative refinement and can cause silent regressions. We propose Agentic Data Evolution (ADE), a data-centric framework that organizes synthetic supervision as evolving data snapshots. ADE improves data snapshots through a closed-loop Observation-Variation-Selection (OVS) procedure, where a steady-state admission mechanism acts as a quality ratchet that conservatively gates updates for sustained cross-round improvement. We validate these improvements through complementary intrinsic trend tracking and extrinsic post-training evaluation. On DEV300, ADE raises the intrinsic win rate from 50% to 75.81% and the extrinsic win rate from 55.20% to 68.86%, consistent performance gains across diverse benchmarks. Blind expert evaluation further confirms this, with a 66.11% preference for evolved answers. These gains extend across post-training methods, model scales, and tasks beyond the target weakly verifiable educational objectives. Resources are available at this https URL.

---


### 19. [DriftAD: Visually-Guided Text Drift for Few-Shot Industrial Anomaly Detection](https://arxiv.org/abs/2608.23723)

**<font color=#1a73e8>作者：</font>** Wenyang Liu, Tianyi Liu, Dongshuo Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Few-shot anomaly detection (FSAD) has recently benefited from vision-language models such as CLIP, which enable anomaly de?tection by aligning visual features with text descriptions of normal and abnormal states. However, existing methods typically rely on static text prompts that are applied uniformly across the entire feature hierarchy and spatial dimensions. This rigid global-to-local matching fails to capture the highly localized and scale-dependent physical variations of industrial defects. To address this, we propose DriftAD, a FSAD framework built on three key modules. First, an Anomaly Signal Amplification (ASA) module enhances subtle defect signals through spatial and frequency branches before text-visual matching. Second, Visually-Guided Text Drift (VGTD) dynamically transforms frozen CLIP text embeddings, steering them into layer?wise, spatially-adaptive anomaly descriptors conditioned on local visual context at each encoder depth. Third, Drift-Guided Spatial Gating (DGSG) uses the drifted abnormal descriptor as a spatial probe to selectively enhance anomaly-relevant visual features. Addi?tionally, a drift separation loss prevents representational collapse of the drifted descriptors, and a gate supervision loss enforces spatially discriminative gating in DGSG. Extensive experiments on MVTec?AD and VisA demonstrate state-of-the-art performance across all 1-, 2-, and 4-shot settings on both image-level and pixel-level metrics. Code is available at this https URL.

---


### 20. [AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace](https://arxiv.org/abs/2608.23740)

**<font color=#1a73e8>作者：</font>** Seonglae Cho, Donghyun Lee  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Concurrent multi-agent coding promises division of labor across modules, robustness through redundancy, and parallel exploration at the natural granularity of multi-file projects. Realtime collaborative editing protocols solve this coordination problem for human teams via Conflict-free Replicated Data Types (CRDTs), but the LLMs underneath generate one token at a time and existing multi-agent coding systems inherit this serial limit: they either sequence agents through phase handoffs or pool independent samples without coordination, and a single agent abandons up to half of hard tasks with a one-file stub-and-exit. AgentRoom is a realtime collaborative editing protocol for concurrent coding agents. Its runtime layer exposes file-level claim, status, and broadcast as MCP tools on a CRDT-merged shared filesystem. Five frontier coding-CLI models ran four backend coding tasks, with cross-language checks in Python DevBench and Rust+axum. For CLI-stable models, AgentRoom with 2 agents abandons fewer tasks than Solo and has less run-to-run variation. At matched-compute, one positive mean LLM-judge contrast puts AgentRoom over parallel-merge. The other contrast, a bundle probe, puts full AgentRoom above each partial case: an ordering rather than a percentage split. Coordination, not parallelism or CRDT-merge, bears the load.

---


### 21. [Calibration-Preserving Pruning: Compression as a Reliability Contract](https://arxiv.org/abs/2608.23744)

**<font color=#1a73e8>作者：</font>** Ibne Farabi Shihab, Adria Binte Habib, Anuj Sharma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Split conformal prediction, not the pruning rule, supplies finite-sample marginal coverage once a pruned model is fixed independently of the conformal calibration split. We study the separate efficiency problem: can pruning preserve score geometry well enough to obtain smaller valid prediction sets? Calibration-Preserving Pruning (CPP) augments a base pruning score with nonconformity-gradient saliency and uses disjoint pruning, validation-selection, conformal-calibration, and test splits. Bounded score perturbations imply bounded conformal-quantile shifts and controlled set inflation, but do not make the generic coverage theorem CPP-specific. Final five-seed Qwen2.5-1.5B results at 50\% sparsity show the largest gains on large-label tasks. On DBpedia-14, CPP-SparseGPT reduces mean set size from \(10.1\) to \(8.6\) while changing accuracy from \(0.347\) to \(0.366\); CPP-Wanda reduces \(11.2\) to \(9.0\) with an accuracy trade-off from \(0.310\) to \(0.295\). Across 15 dataset--sparsity cells, CPP-SparseGPT produces smaller sets in 13 and higher accuracy in 11. Matched controls show that generic supervised gradients explain much of the gain: true-label CPP is not statistically resolved from matched Wanda+SNIP, whereas threshold-aware candidate-label CPP reaches \(7.8\) mean set size at explicit accuracy and offline-compute costs. RoBERTa-base and Llama-3-8B diagnostics support transfer, but our claims remain limited to reliability-sensitive classification.

---


### 22. [TrustShiftProbe: Characterizing, Benchmarking, and Defending Staged Trust Attacks on MCP Servers](https://arxiv.org/abs/2608.23763)

**<font color=#1a73e8>作者：</font>** Mehrdad Rostamzadeh, Sidhant Narula, Mohammad Ghasemigol 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has emerged as the standard layer connecting Large Language Model agents to external tool backends. This openness introduces a severe server-side threat we term TrustShift: a compromised MCP server behaves benignly during an initial conditioning phase, building operational reliance and suppressing agent skepticism, before switching to an adversarial payload once an interaction threshold is reached. The evasion is temporal, not syntactic: benign at deploy time, the server's defection is invisible to predeployment static analysis, which sees only the honest phase. Switched payloads range from overt structural violations to schema-valid manipulations, the latter preserving outer protocol compliance to evade runtime middleware filters. Crucially, TrustShift originates in the server-controlled tool channel, not user prompts (unlike indirect prompt injection) or the transport (unlike man-in-the-middle): the adversary is the trusted server endpoint itself. We introduce TrustShiftProbe, an evaluation and defense framework with four contributions: (1) a stateful temporal threat model of the agent-server lifecycle as a benign conditioning phase followed by an adversarial defection at a trust horizon; (2) a language-agnostic attack engine that instantiates each variant as a compromised MCP server across four production domains; (3) SHIELD, a multi-tier, zero-oracle runtime defense at the MCP transport boundary that audits server payloads against behavioral baselines learned during clean trust windows; and (4) a taxonomy of nine TrustShift variants spanning three execution mechanisms (structural violation, semantic corruption, scope expansion) and three adversarial objectives (disruption, exfiltration, and their combination). Across frontier proprietary and open-weight models, TrustShift attacks achieve a 69.5% mean attack success rate that SHIELD mitigates to 42.7%.

---


### 23. [When Youth Enter The Chat: An Epistemic Shift in the Validation of LLM-Based Measures of Student Talk](https://arxiv.org/abs/2608.23780)

**<font color=#1a73e8>作者：</font>** Liliana Santos-Deonizio, James Malamut, Ramón Martínez 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are being used increasingly to measure aspects of student discourse (e.g. talk moves, collaboration, equity of voice) at scale. Typically, LLM-based measures of student talk use transcriptions of classroom conversations that only include verbal contributions, which de-contextualize student language. Common practices for validating these measures include comparing outputs against expert annotations by adults, using held out evaluation sets and F1 scores. We argue that these approaches are insufficient to ensure that such measures are meaningful and equitable for teaching and learning, particularly for racially and linguistically marginalized youth. In order to center the youth whose talk is being analyzed, re-contextualizing these classroom conversations and engaging youth in the research process is necessary. Sharing epistemic authority with youth, ultimately, centers their point of view and adds crucial nuance to the analysis of their talk that adult experts, researchers, and LLMs cannot provide. In a case study of multilingual youth in one 8th-grade math classroom, we address the epistemic exclusion of youth by employing multiple ethnographically-oriented methods to re-contextualize student conversations and center youth as epistemic authorities in conversation with researchers and LLMs. We conducted participant observations, interviews, focus groups, and member checks with four focal students. Findings reveal that there were misalignments between students' interpretations of their own math talk experiences and the LLM-based measures of their talk. Students contested both the LLM classifications and the coding scheme used to measure their talk, highlighting the need for youth to be involved in the epistemic process of producing knowledge about their experiences.

---


### 24. [Inter-dimension Dependence for Multi-Dimensional Evaluation of Open-Ended Text](https://arxiv.org/abs/2608.23783)

**<font color=#1a73e8>作者：</font>** Haoyuan Li, Snigdha Chaturvedi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-judge methods are widely used for evaluating the quality of generated open-ended text. Such evaluations are generally multi-dimensional, since the error patterns in texts can be different for different dimensions. Therefore, reliable LLM judges should evaluate each target dimension independently. To quantify the extent to which LLM judges depend on non-target dimensions when evaluating a target dimension, i.e., inter-dimension dependence, we propose CorrGap. To measure this, CorrGap uses the difference in correlations between LLM-predicted scores and ground truth scores across different groups of texts. Using CorrGap, we show that inter-dimension dependence is pervasive across LLM judges in open-ended text evaluation tasks. To mitigate inter-dimension dependence, we propose DimCheck, a method that iteratively removes unrelated evidence from COTs generated by LLM judges in a step-wise way. We show that DimCheck mitigates inter-dimension dependence and outperforms strong baselines across three LLMs and four tasks. We also show that smaller trained LLMs can approximate larger LLMs in DimCheck, with much lower inference costs.

---


### 25. [Mixture of Channel Experts: Static Sparse Supports with Input-Adaptive Mixing for Pointwise Projections](https://arxiv.org/abs/2608.23794)

**<font color=#1a73e8>作者：</font>** Elian Iluk, Gil Ben-Artzi  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) scales language models by routing each input through a small set of independently parameterized experts. We show that copying this design into convolutional networks fails for a structural reason: parallel convolutional experts that read the same input channels learn nearly identical filters. We therefore move the expert axis from operator duplication to channel selection. We introduce Mixture of Channel Experts (MoCE), a structured sparse channel-mixing layer, inspired by MoE, that replaces pointwise (1x1) channel-reduction projections. In MoCE, an expert is a single output channel with a learned sparse support of k << C input channels. The selected channels are combined by a softmax whose temperature is predicted per input, so each expert can move between mean-like and max-like aggregation. A residual expert summarizes the unselected channels, and a load-balancing loss keeps channel coverage complete. MoCE replaces a dense projection whose cost is quadratic in C with a mechanism whose relative cost scales as k/C, and the predicted savings hold in measured wall-clock time. Across ResNet backbones on ImageNet-1K and CIFAR-100, transfer learning, EfficientViT, and a strong modern training recipe, MoCE matches or exceeds dense baselines and prior channel-selection methods while reducing MACs by 16.7% and end-to-end latency.

---


### 26. [Giga-Embeddings: Mixture-of-Experts Encoders for High-Throughput Text Embeddings](https://arxiv.org/abs/2608.23806)

**<font color=#1a73e8>作者：</font>** Egor Kolodin, Egor Krasnoperov, Evgeniy Kosarev 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Giga-Embeddings, a family of text embedding models designed to combine strong retrieval quality with efficient serving. Its largest member is a sparse 10B-parameter Mixture-of-Experts encoder with approximately 1.8B active parameters per token. Across English, Russian, multilingual, and code MTEB benchmarks, this model achieves the strongest aggregate performance within the family on all four evaluated suites. In our vLLM benchmark with 1024-token inputs, it processes 114.5k tokens per second, providing 25 percent higher throughput than the dense 3B model and 1.56-2.65x the throughput of the evaluated external systems. The family also includes a dense 3B encoder and a distilled 480M encoder for tighter compute and memory budgets. We train the compact model using a dimension-agnostic objective that aligns teacher and student similarity distributions. The resulting 480M model scores 70.98 on Russian MTEB, surpassing FRIDA while using 42 percent fewer parameters. We release all three model checkpoints.

---


### 27. [Serving Masked Diffusion LLMs: Characterization and Design Principles from Real Hardware](https://arxiv.org/abs/2608.23807)

**<font color=#1a73e8>作者：</font>** Farhana Amin, Sabiha Afroz, Mona Moghadampanah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models (dLLMs) can in principle generate text faster than autoregressive (AR) models, since they denoise many tokens at once. Recent systems have begun building serving infrastructure for dLLMs, but none first measure how these models behave under real, concurrent serving load. Serving systems built without this grounding risk carrying over assumptions from AR serving that may not hold for dLLMs. We characterize dLLM serving to close this gap, using LLaDA-8B-Instruct with a D2F (Discrete Diffusion Forcing) LoRA adapter on a single NVIDIA H200 GPU, evaluated on GSM8K and HumanEval. We report three findings. First, request difficulty, the number of denoising steps a request needs, is discrete rather than continuous: requests fall into 11 fixed step-count levels (178 + 29k), and no signal we test predicts the level before generation starts (best R2 = 0.150). Second, benchmarks with short generation budgets below 320 tokens understate serving variance, since requests are cut off before the latency spread appears. Third, only 24% of single-request wall-clock time is GPU computation; the rest is CPU-side dispatch overhead. Batching mainly helps by amortizing this overhead: sharing one forward pass per denoising step improves throughput by 16.0x at batch size 16 over a per-request-dispatch baseline. We also argue structurally that output quality should not degrade with batch size, stating three assumptions this rests on; we measure 74 to 76% GSM8K accuracy at single-request scale. Finally, we derive a batch-timeout rule for fixed-fill synchronized batching under Poisson arrivals. Together, these results show that serving diffusion language models needs parallelism at the level of each denoising step, which differs from AR serving in how admission and eviction interact with an already shared forward pass.

---


### 28. [Discovering Cross-Language Reasoning Invariance in LLMs with Geometry-Invariant Sparse Autoencoders](https://arxiv.org/abs/2608.23809)

**<font color=#1a73e8>作者：</font>** Igor Bogdanov, Changcheng Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multilingual language models can solve the same mathematical problem in different languages, but it remains unclear whether they rely on shared features or on language-specific computations that only produce similar outputs. We study this question in five models from four families using the Multilingual Grade School Math (MGSM) dataset, with problems solved in English, German, French, Spanish, Russian, and Chinese, retaining problems with valid reasoning traces in all six languages and replaying those traces through the model to record representations at multiple layers. For each model, we first use Centered Kernel Alignment (CKA) to identify layers with cross-language alignment. At each selected layer, we train two sparse autoencoders (SAE): a baseline reconstruction-only model and a contrastive variant introduced in this work, the Geometry-Invariant SAE (GI-SAE). GI-SAE supplements the reconstruction loss with an Information Noise-Contrastive Estimation (InfoNCE) loss that trains the encoder to produce similar activations for traces of the same problem, regardless of language or token position. We then test whether the resulting shared features are functionally interchangeable by swapping their values between languages during the model's forward pass and measuring the resulting change in output, quantified by Kullback-Leibler (KL) divergence per feature. Although GI-SAE yields higher CKA and Jaccard similarity at nearly every layer, higher geometric similarity does not consistently imply greater functional interchangeability. We find that cross-language feature sharing is model- and architecture-dependent in this sample and appears at different depths in different models. GI-SAE primarily amplifies cross-language structure already present: the pattern is model-specific, with strengthening in Qwen, no functional benefit in Gemma, and mixed layer-dependent effects in Llama and Phi.

---


### 29. [Generating Biomedical Fact-Checking Reports with RL-Enhanced Agentic Search](https://arxiv.org/abs/2608.23811)

**<font color=#1a73e8>作者：</font>** Jiongxiao Wang, Dingli Ma, Chaoqun Ni  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Automated fact-checking is essential for ensuring the reliability of public health information, yet the biomedical domain poses unique challenges. Validating biomedical claims requires rigorous interpretation of scientific literature, assessment of retrieved evidence, and comprehensive justification toward the conclusion. Although Large Language Models (LLMs) enhanced by Retrieval-Augmented Generation (RAG) and agentic search perform automated fact-checking in a retrieve-then-verify paradigm, current methods still output isolated prediction labels, lacking explanatory depth and offers limited utility for human understanding. To bridge this gap, we introduce an LLM-based agent named BioCheck Agent that generates structured biomedical fact-checking reports with agentic search. Rather than merely outputting supported or refuted labels, our agent synthesizes final conclusions with retrieved evidence and rigorous analysis. To ensure domain-specific accuracy, BioCheck Agent exclusively searches high-quality scientific literature in PubMed, utilizing advanced Boolean search operators. Recognizing that direct prompting often results in hallucinations and low-quality reports, especially for lightweight open-source models, we further propose the Evidence-Grounded Group Relative Policy Optimization (EG-GRPO) to perform reinforcement learning on BioCheck Agent with a task-specific reward that incentivizes advanced search behavior and high-quality evidence retrieval while penalizing hallucinations. Our experimental results show that compared to the base model Qwen3.5-4B, BioCheck Agent with EG-GRPO improves label prediction accuracy on SciFact by 9.95%. Furthermore, it achieves a 3.7% higher evidence quality score and a 19.63% lower evidence hallucination rate, demonstrating its ability to generate biomedical fact-checking reports with improved accuracy and quality.

---


### 30. [Learning to Grade Efficiently: A Bandit-Driven Prompt-Selection Framework for Low-Cost LLM Essay Scoring](https://arxiv.org/abs/2608.23814)

**<font color=#1a73e8>作者：</font>** Olga Manakina, Igor Bogdanov  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) demonstrate strong capabilities in automated essay scoring (AES), but contemporary approaches typically employ fixed prompt selection, failing to address operational cost concerns and evolving optimal configurations. We propose a novel cost-aware approach that treats each prompt type as an arm in a multi-armed bandit (MAB) controller, enabling adaptive selection of optimal prompting strategies during inference. Our experiments on IELTS Writing Task 2 essays show that the MAB framework achieves comparable scoring accuracy to exhaustive grid search while reducing LLM calls by 78.4\% to find the best grading approach. We implemented four distinct grading recipes (multi-step vs. single-step assessment, with vs. without calibration examples) and found that the multi-step approach with examples achieves the highest accuracy. By tracking token usage and latency alongside agreement metrics, we produce the first cost-reliability learning curves for essay scoring, providing actionable insights for educational technology platforms that must balance operational costs against assessment validity. This work represents the first application of online control mechanisms to adaptively select prompting strategies in AES, transforming prompt selection from an offline hyperparameter optimization problem into an efficient online learning task.

---


### 31. [Beyond Static and Linear: What Attention Constraints Best Fit Human Reading Times?](https://arxiv.org/abs/2608.23818)

**<font color=#1a73e8>作者：</font>** Lanni Bu, Xiulin Yang, Christian Clark 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Transformer-based language models are widely used as models of human language processing, yet their attention mechanisms allow lossless access to the full preceding context, unlike the limited memory systems of humans. We hypothesize that installing memory constraints into transformers' attention mechanisms can improve their fit to human behavioral data. While previous work has explored individual constraints in isolation, we conduct a systematic comparison of multiple attention-based memory mechanisms across different model sizes and training corpora, evaluating both psychometric predictive power for human reading times and grammatical competence. We additionally compare static constraints, in which the constraint strength is fixed throughout training, to dynamic memory curricula. We find that constraints that are sensitive to the content of intervening tokens consistently achieve the highest alignment with human reading times, outperforming distance-based constraints. We observe a dissociation between psychometric fit and grammatical competence under dynamic memory curricula, suggesting that Transformers cannot serve as a one-size-fits-all cognitive model.

---


### 32. [Mitigating Exploration Bias in RL for Multi-Instruction Following](https://arxiv.org/abs/2608.23830)

**<font color=#1a73e8>作者：</font>** Mian Zhang, Yueqin Yin, Kaiyu He 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> RL has emerged as a powerful paradigm for enhancing the instruction following capabilities of LLMs. While existing training recipes achieve substantial gains, we find that they suffer from exploration bias towards easy instructions when the training data has multiple instructions in a prompt. This bias is caused by two main reasons: 1) the policy model's initial ability to satisfy hard instructions is too low to trigger successful exploration during RL training, so the optimization is biased towards easy instructions; and 2) canonical RL training recipes typically employ a cumulative reward (the number of instructions fulfilled), treating all instructions equally, which biases the policy model towards fulfilling easy instructions to obtain the same amount of reward. To address these issues, we first propose two metrics to measure the exploration bias in instruction following and then introduce a two-stage framework to alleviate it: 1) Behavioral Bootstrapping, a lightweight rejection sampling fine-tuning stage before RL to activate hard instructions; and 2) Scarcity-Aware Rewards, a new RL reward function that assigns rewards to instructions based on their empirical scarcity. Experiments show that the proposed metrics are highly correlated with model performance, and our methods unleash the potential of RL training: our best models outperform the baselines by a significant margin across three verifiable instruction following benchmarks. We release codes at this https URL.

---


### 33. [Minima-KV: Retention-Preserving KV Cache Compression with Mixed-Format Paged Attention](https://arxiv.org/abs/2608.23834)

**<font color=#1a73e8>作者：</font>** Sergii Kozyrev, Davyd Maiboroda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache is a primary capacity and bandwidth bottleneck in long-context LLM serving. We present Minima-KV, a retention-preserving hierarchy for mixed-format paged attention. Recent and protected Anchor pages remain in FP8, while older non-anchor pages move to packed TQ3; every live-request page remains addressable. Format-specific kernels compute partial attention states and combine them through a globally normalized online-softmax merge, enabling direct heterogeneous decode without a cache-sized dense shadow. Across separate, configuration-bound Qwen3.6-27B profiles on a single 96-GB NVIDIA RTX PRO 6000 Blackwell GPU, deployment accounting reports 18.3 KiB of attention KV per live token, corresponding to 3.50x compression relative to BF16 and 1.75x relative to FP8. A materializing quality profile matches its dense control on 16K RULER needle-in-a-haystack tasks. On the same 503-question LongBench v2 set, measured deltas are -0.80, -0.60, and -0.40 percentage points at 16K, 32K, and 64K. A separate single-pair direct-decode canary with two 59,008-token requests measures 3.625x active-KV compression and 0.9821x throughput relative to its control, routes all 16 full-attention layers without fallback, and retains no dense shadow. These results establish a practical mixed-format path for compressing long-context state without evicting live-request KV pages.

---


### 34. [SyPS: Measuring Sycophancy Prompt Sensitivity in Large Language Models](https://arxiv.org/abs/2608.23837)

**<font color=#1a73e8>作者：</font>** Lijia Huang, Yao Fu, Sihao Ren  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are known to exhibit social sycophancy, often validating or agreeing with users in socially sensitive contexts. Existing evaluations typically measure sycophancy under a fixed prompt formulation, leaving unclear whether such behavior is stable when the same underlying situation is presented with different sycophancy-relevant prompt variants. In this work, we study sycophancy prompt sensitivity: the extent to which changes in user confidence, emotional framing, social consensus, or validation-seeking language alter a model's sycophantic behavior. We refer to our evaluation framework as SyPS, short for Sycophancy Prompt Sensitivity. Building on existing social sycophancy evaluation settings, SyPS constructs controlled prompt variants that preserve the same underlying user situation while varying sycophancy-relevant social cues. We introduce the Sycophancy Prompt Sensitivity Score (SPSS), an instance-level measure of sycophancy variation across paired prompt variants. Unlike aggregate sycophancy rates, SPSS separates baseline sycophancy from prompt-induced shifts, enabling model-level comparisons of robustness to sycophancy-relevant social cues. Empirically, we find that sycophancy prompt sensitivity is socially structured: validation-seeking and emotional-pressure cues often increase sycophancy, whereas counter-framing and anti-sycophancy prompts tend to reduce it. Our framework highlights whether LLMs maintain stable social judgments while adapting appropriately in tone.

---


### 35. [PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Compression](https://arxiv.org/abs/2608.23843)

**<font color=#1a73e8>作者：</font>** Zizhong Wang, Jieying Wang, Zhao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-context inference in large language models (LLMs) is increasingly limited by the memory required for the key-value (KV) cache. KV cache compression addresses this problem by reducing the storage cost of previous tokens. Among existing approaches, low-rank compression is particularly attractive because it represents every token in reduced dimensions. Previous low-rank methods typically derive fixed projection spaces from model weights, construct fixed spaces from calibration activations, or construct a shared basis over a broad cache region. Such representations may not capture detailed but important information. We partition each per-head KV cache into fixed-length logical pages and observe substantial low-rank structure within individual pages. Based on this observation, we propose PuzzleKV, a training- and calibration-free method that treats each completed page as an independent compression unit. PuzzleKV decomposes pages within each layer and KV head, computes attention directly over dense and factorized pages, and incrementally compresses newly eligible pages during autoregressive decoding. Experiments across models, context lengths, and benchmarks demonstrate the effectiveness of PuzzleKV under matched storage budgets. At approximately 60% of the original KV cache storage, PuzzleKV achieves more than 96% of Full KV performance across both evaluated models and all benchmark settings, with substantial gains over Global SVD on RULER and competitive performance on LongBench. To achieve a more aggressive compression ratio, PuzzleKV can be further combined with quantization while retaining more than 93% of Full KV performance using only 18.7% of the original storage.

---


### 36. [Exploit More, Explore Smarter for Budget-Constrained Agentic Search](https://arxiv.org/abs/2608.23848)

**<font color=#1a73e8>作者：</font>** Haoyang Fang, Bernie Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Budget-constrained agentic search arises when an LLM agent must refine candidates under a small evaluation budget, because validation is expensive, generation requires multiple model calls, or both. In this regime, standard MCTS allocates budget poorly: exploration bonuses dominate at low visit counts, unpromising siblings are expanded before promising chains can deepen, and branching is independent of node quality. We introduce ExTS, a tree-search policy that treats expansion itself as a value-of-information decision. ExTS combines three mechanisms: discriminative reward shaping to separate candidates under narrow score distributions, a stochastic virtual child that estimates the value of creating a new branch from the parent's reward history, and quality-conditioned branching that expands only when a node's score justifies the budget cost. Across prompt optimization, code generation, molecular structure elucidation, and agentic workflow optimization, ExTS is competitive with or improves over task-specific tree-search baselines, with an average relative gain of +5.5% using a single fixed configuration. We further introduce pilot-run diagnostics that characterize what makes budget-constrained agentic search problems structurally different from one another, providing both understanding of the problem space and practical guidance for adaptation.

---


### 37. [Does Episodic Memory Help Close the Lexical Frequency Gap in Sensitivity to Syntactic Contrasts? A Test Using Retrieval-Augmented Language Models](https://arxiv.org/abs/2608.23851)

**<font color=#1a73e8>作者：</font>** Jing Liu, Najoung Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grammatical knowledge and how it is empirically tested are typically considered robust to the frequency of the lexical items in the expressions. However, neural network-based models of grammaticality exhibit high sensitivity to lexical frequency. We draw upon Complementary Learning Systems theory to test the hypothesis that robustness to lexical frequency can arise via a hippocampal episodic memory mechanism, which enables rapid encoding and retrieval of specific experiences and allows learners to leverage them when processing rare patterns. We use retrieval-augmented language models as an instantiation of such an episodic memory mechanism (specifically, $k$-nearest-neighbor language models that augment parametric models with explicit instance storage), and test whether this augmentation helps close the lexical frequency gap that vanilla language models exhibit in syntactic contrast tests. Using syntactic contrasts with frequency-stratified test items, we find that retrieval augmentation narrows the performance gap between high- and low-frequency items, consistent with episodic memory compensating for weak parametric representations. This benefit is consistent across different syntactic phenomena and across models pretrained on child-realistic and large-scale data. Additionally, we show that structural information is critical for effective retrieval, whereas semantic similarity alone provides little benefit. While these are promising proof-of-concept results supporting our hypothesis, the frequency gap is narrowed rather than fully closed. Based on our analyses, we propose preferential reweighting of retrieved instances, better representations and retrieval strategies for structural information, and flexible configurations of storage and retrieval as promising future directions for improving the implementation of episodic memory in language models.

---


### 38. [LUX: A Lesion-Aware Graph-Conditioned Visual - Language Architecture for Explainable Endoscopic Captioning](https://arxiv.org/abs/2608.23853)

**<font color=#1a73e8>作者：</font>** Alexis Ivan Escamilla-Lopez, Gilberto Ochoa-Ruiz, Salvador Hinojosa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The interpretation of endoscopic imagery in ulcerative colitis is complex and subjective, with variability in human assessment and subtle mucosal inflammation. Although deep learning has advanced automated analysis, most vision-language models rely on global visual embeddings that overlook the localized and relational nature of pathological evidence, limiting clinical reliability and interpretability.
We introduce LUX (Lesion-aware Unified eXplainable captioning), a graph-conditioned vision-language architecture for explainable endoscopic image captioning. LUX constructs a lesion-centric scene graph from Grad-CAM and CBAM activation maps, representing pathological regions as nodes and encoding their spatial and clinical relationships. These graph embeddings are integrated into the cross-attention layers of a T5 decoder, enabling generated words to attend to specific lesion nodes rather than only to global image features. This provides direct alignment between linguistic content and pathological evidence, supporting token-level interpretability and relational reasoning.
LUX outperforms strong baseline and state-of-the-art medical captioning models across BLEU, METEOR, ROUGE-L, and CIDEr, with particularly strong gains in CIDEr. It also reduces hallucinated clinical findings and improves lesion-level grounding through stronger correspondence between generated tokens and localized pathological regions.

---


### 39. [Beyond the Mandate: A Systematic Security Analysis of the Agent Payments Protocol (AP2)](https://arxiv.org/abs/2608.23858)

**<font color=#1a73e8>作者：</font>** Avital Aviv, Parth A. Gandh, Ron Bitton 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Agent Payments Protocol (AP2), introduced by Google, enables large language model (LLM)-driven shopping agents to authorize and execute payments on behalf of users. Its signed Checkout and Payment Mandates protect the integrity of transaction data after signing. Agent interactions and external inputs that shape a transaction before authorization remain outside that protection, including Agent-to-Agent Protocol (A2A) messages and Model Context Protocol (MCP) tool calls. Prior work identified replay and prompt-injection attacks in AP2 v0.1. AP2 v0.2 addresses some of these issues but adds capabilities and deployment assumptions that require renewed analysis. We present a systematic security analysis of AP2 v0.2 based on its roles, transaction lifecycle, deployment architectures, and trust boundaries. We divide the lifecycle into five phases and identify five deployment architectures. Using MAESTRO (Multi-Agent Environment, Security, Threat, Risk, Outcome), we model four threat actors, eleven attack surfaces, eighteen adversary capabilities, and six attacker goals. The resulting catalog contains 48 threats spanning five attack families. We score these threats with the Artificial Intelligence Vulnerability Scoring System (AIVSS), identifying eight that reach the High band in at least one architecture. Because no complete public AP2 deployment was available, we build a testbed spanning all five architectures and develop five proof-of-concept demonstrations covering all eight High-risk threats and their mitigations. We also develop a deployment-aware scanner that maps applicable threats to static, cross-role consistency, and adversarial checks. Our analysis shows that valid mandate signatures alone do not ensure that an agent-mediated transaction reflects the user's intent when its pre-authorization context is manipulated.

---


### 40. [Revelation Control](https://arxiv.org/abs/2608.23860)

**<font color=#1a73e8>作者：</font>** Qinyou Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Revelation Control is the problem of choosing priced interventions that reveal hidden state only insofar as the revealed distinctions can change a consequential decision, while accounting separately for any useful progress created by the intervention itself. We develop this theory for learning systems, where states equivalent under declared current information can respond differently to future training and favor different actions. The framework defines decision-sufficient revelation and revelation depth, separates pure information value from productive reuse, embeds static Bayes refinement into state-dependent continuation value, and gives an exact cost-adjusted factorization criterion: an additional shallow coordinate is decision-nonredundant only when states sharing a scalar summary lie on opposite sides of the priced Stop/Continue boundary. We also give a target-independent protocol for model-specific instantiation and prove that bounded stop-flip risk alone cannot certify positive expected utility under unrestricted severity. Across Qwen2.5-7B and Mistral-7B-v0.3, deeper future-learning probes have positive decision value and productive reuse yields strict equal-compute utility advantages. Qwen additionally provides evidence for a decision-nonredundant shallow revealability regime; in Mistral, a scalar continuation architecture fit only on an independent development panel retains positive familywise-adjusted lower bounds on a disjoint target panel, consistent with scalar decision sufficiency within the tested architecture family and resolution. The evidence supports structural rather than numerical transfer: the decision theory, cost accounting, continuation logic, and evaluation protocol transport, while empirical proxies, coefficients, thresholds, and even the required shallow state dimension may be system-specific.

---


### 41. [Markets, Not Planners: Decentralized Orchestration of LLM Agents with Private Information](https://arxiv.org/abs/2608.23867)

**<font color=#1a73e8>作者：</font>** Xiao Liu, Haoyang Li, Songwei Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As LLM agents proliferate, built by different parties and with different capabilities and costs, orchestrating them is more like assembling labor across the economy than a computer calling a subroutine. Existing orchestration is typically centralized, with a single planner assigning every task, but this creates a bottleneck as agent pools grow, requires private information (e.g., agents' execution costs), and can easily be manipulated, such that a single inserted preference nearly doubles a favored agent's task share under a centralized LLM allocator. We introduce AgentLance, a repeated labor market in which agents bid on tasks using their private costs and self-maintained strategy notes, an allocator selects winners from bids and public reputation records, and a VCG-style payment rule rewards cost-aware bidding. Complex tasks are handled by hierarchical delegation: winning agents can decompose work and subcontract it through the same mechanism. Across mathematical reasoning, code generation, knowledge-intensive QA, and agentic tasks, AgentLance matches agents to their specializations, shifts work toward cheaper agents as cost sensitivity rises, and consistently outperforms single-model, centralized-orchestration, and market baselines. Diagnosing market failures, including inaccurate cost self-estimation and sub-optimal bidding, then correcting them in controlled experiments yields further gains, charting a path toward more efficient agent economies.

---


### 42. [Gen2Physics: Grounding Generated 3D Meshes in Physics via Multi-View Material Decomposition](https://arxiv.org/abs/2608.23869)

**<font color=#1a73e8>作者：</font>** Mauro Comi, Jordi Serrano Berbel, Kevis-Kokitsi Maninis 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While state-of-the-art generative models produce high-fidelity 3D meshes, these outputs lack the physical properties required for interactive simulation, gaming, or robotics. We introduce Gen2Physics, a unified and automated framework that grounds generated meshes in physics by automatically decomposing them into their constituent material components. Unlike prior approaches, which focus on volumetric representations incompatible with standard physics engines, Gen2Physics operates directly on meshes to produce immediately simulation-ready assets. Our pipeline integrates a fine-tuned Vision Transformer for dense material segmentation, a robust 2D-to-3D consistency projection, and a Vision-Language Model (VLM) guided refinement that leverages contextual reasoning to assign physical properties and infer internal geometry (solid vs. hollow). By converting surface patches into volumes with distinct densities, our method enables physically plausible dynamic simulations. Experimental results on the ABO-500 and PartNet-Material benchmarks demonstrate that Gen2Physics more than doubles the material segmentation accuracy of prior physics-grounding pipelines (15.6 to 48.3 mIoU), while matching the mass-estimation accuracy of volumetric methods and being the only approach to output watertight per-material sub-meshes.

---


### 43. [Granite.Trust Policy Tools: Shareable, Actionable Policies for Generative AI Applications](https://arxiv.org/abs/2608.23870)

**<font color=#1a73e8>作者：</font>** Nathalie Baracaldo, Nicolas Mello, Kush R. Varshney 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When it comes to safety policies for generative AI, one size does not fit all. Each organization and use case needs to mitigate different risks depending on the application context, regulatory environment, organizational values, and user personas. Yet, existing policy specification approaches are designed for traditional access control and fail to capture the nuances of GenAI application: the enforcement of content-based constraints.
We present two contributions to address this gap: (1) the Actionable Policy schema, a YAML-based format for specifying what model responses can and cannot contain. The schema enables exception-based policy governance, proposing exceptions to track policy violations; (2) synthetic data generation pipeline that produces policy-aligned training data for model alignment and testing, and a set of tools to help define the schema and enforce policy. Together, these enable organizations to specify policies once and enforce them throughout the GenAI application lifecycle: from model alignment to runtime monitoring. The Actionable Policy schema, example policies, and tools are available as open source: this https URL We welcome new ideas, contributions and feedback.

---


### 44. [LG-GER: Language-Guided Group Emotion Recognition via Multimodal Evidence Distillation](https://arxiv.org/abs/2608.23880)

**<font color=#1a73e8>作者：</font>** Ahmed Shehab Khan, Zhiyuan Li, Yan Tong  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Inferring the collective emotional state of a group of people from a single image, a task known as group emotion recognition (GER), requires integrating spatially distributed cues such as faces, poses, interactions, and scene context. Current methods rely on detector-driven multi-stream pipelines. These are trained with only image-level supervision that lacks guidance on which regions matter or how strongly each contributes. We propose LG-GER, a language-guided distillation framework that uses a multimodal large language model (MLLM) to generate dense, spatially grounded evidence, i.e., bounding boxes paired with emotion signals and confidence scores, for the training images. This structured evidence is distilled into a single vision-language model (VLM) backbone through four complementary losses: classification, region-text grounding, spatial emotion, and spatial confidence regression. At inference, LG-GER requires no detectors, no MLLM, and no multi-stream fusion, making GER practical for real-time and resource-constrained deployment. LG-GER has been evaluated on two benchmark GER datasets (GroupEmoW and GAF~3.0) and achieves competitive or superior results compared to state-of-the-art methods that require detection and multi-stream processing at inference.

---


### 45. [Names Can Hurt: Spotting Slopsquatting Risks Caused by Package Name Hallucinations in Local Coding LLMs](https://arxiv.org/abs/2608.23897)

**<font color=#1a73e8>作者：</font>** Akash Raj, Sargam Sahu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a code generating language model fabricates a Python package name, an adversary who has pre-registered that name on PyPI can convert that hallucination into a supply chain compromise. This event has been termed as 'slopsquatting'. We propose a two layer detector to counter this issue. The first layer performs a deterministic PyPI existence check. The second is a Random Forest classifier trained on ten features derived from the package name and its PyPI metadata. An import name reconciler bridges the two, resolving cases such as 'import cv2' versus 'pip install opencv-python' without a security bypass. The detector is embedded in a LangGraph state machine that retries at escalating temperatures and, on repeated failure, routes to a stronger fallback model. Across 300 curated prompts, the pipeline produces hallucination free code on 76% of runs. The primary exhausts its retry budget on 28.7%; intra model retries recover roughly a quarter of those, and cross model fallback recovers a further 16.5% of the remainder. Four findings have been observed. First, half of the flagged hallucinations are packages already registered on PyPI, as low quality lookalikes of well known projects, caught by the classifier rather than the deterministic layer (e.g., pil, faiss, tabula, haystack). Second, hallucination rate scales almost linearly with prompt adversariality, from 0 to 10% on routine coding to 40 to 73% on slopsquat baits. Third, the weaker primary refused 6 of 10 direct baits unaided, suggesting recent instruction tuning provides a baseline defense. Fourth, when primary and fallback share a model family, approximately 84% of primary failures recur on the fallback, motivating cross family pairing. A user study (n = 24) reports mean satisfaction 4.4 out of 5 and 21 of 24 stated adoption intent.

---


### 46. [BenchBench-Protocol: Evaluating Real-World Wet-Lab Protocol Reasoning and Modification](https://arxiv.org/abs/2608.23898)

**<font color=#1a73e8>作者：</font>** Aditya Sivakumar, Ashu Singhal, Nicholas Larus-Stone 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce BenchBench-Protocol, a benchmark for large language models of 149 protocol-modification tasks recovered from modifications that scientists made to published protocols during real experimental work. Adapting a published protocol to a new experiment is a routine task for a wet-lab scientist, and a correct modification requires accounting for prior choices and downstream steps. Recent life-science benchmarks have moved toward open-ended, rubric-graded tasks, but tasks are typically elicited from experts rather than reconstructed from real-world modifications. BenchBench-Protocol tasks are derived from differences between a published protocol and a version a scientist modified, which provides the basis for the query and the weighted rubric elements for a correct response. The benchmark draws from 96 source protocols across nine domains of wet-lab biology and only includes tasks rated highly after review by domain experts. We evaluate nine closed and open models; Claude Opus 5 scores highest at 59.2% normalized rubric score, with other models between 34.1% and 47.1%, and the benchmark remains unsaturated when taking the best of ten attempts. As models are increasingly helpful in life-sciences research, evaluating them on routine wet-lab tasks becomes correspondingly important. We present BenchBench-Protocol as both a grounded assessment of wet-lab reasoning and evidence for the utility of real-world experiments to construct benchmark tasks.

---


### 47. [Quantifying System-Level Harms from AI Adoption in Complex Sociotechnical Systems](https://arxiv.org/abs/2608.23906)

**<font color=#1a73e8>作者：</font>** Paul Vautravers, Oliver Chalkley, Gabriel Downer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Artificial Intelligence (AI) is increasingly integrated into complex sociotechnical systems, including Critical National Infrastructure (CNI), where harms emerge from interactions between technical, human, and organisational elements. Yet current AI evaluation remains model-centric, offering little insight into how observed behaviours might translate into system-level risk. We propose a framework that links structured hazard analysis, component-level testing, and probabilistic system modelling to bridge this gap. By providing a traceable pathway from model behaviour to system-level outcomes, the framework enables practitioners to answer the "so what?" of AI failures, quantify their systemic impact, and move toward evidence-based and anticipatory governance of AI in complex systems. Applied to the UK's Real Time Gross Settlement (RTGS) system as an illustrative worked example, we derive AI-driven loss scenarios using Systems Theoretic Process Analysis (STPA) and examine adversarial manipulation of LLM-based trading as one such loss scenario. Component-level experiments show that simple adversarial inputs induce measurable behavioural shifts where AI recommendations are followed. Under the component-to-system mapping used here for a financial contagion model, these shifts alter system resilience, increasing bank failures and lowering the threshold at which shocks lead to cascading disruption, particularly under widespread or monopolistic AI adoption.

---


### 48. [Retrieval-augmented generation vs. deterministic tax computation in multi-agent financial advisory: A 2x2 factorial experiment](https://arxiv.org/abs/2608.23908)

**<font color=#1a73e8>作者：</font>** Aryan Brar, Justin Du, Avery Lor 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tax-loss harvesting demonstrates consistent benefits to long-term portfolio growth; yet implementing it efficiently often involves complex considerations that are specific to the holdings within that portfolio and the individual who owns it. We introduce a custom capital gains calculation engine and a RAG-retrieved vector store of market advisory reports to provide context for a multi-agent trade recommendation system. We investigate the effects of each context provider on the quality of recommendations, measured by relative capital gains incurred during portfolio liquidation. A 2x2 repeated-measures ANOVA revealed a significant main effect of the tax optimization engine ($F(1,29) = 9.17$, $p = .005$, $\eta^2_p = .240$): enabling the engine reduced tax savings by approximately 55 percentage points relative to the no-engine conditions. The RAG main effect was not significant ($p = .841$), nor was the interaction ($p = .553$). The RAG-only condition achieved the highest descriptive mean tax savings (47.7%), and the baseline condition performed second-best (30.6%), suggesting that the pre-trained language model's internalized financial knowledge may be sufficient for competent tax-loss harvesting recommendations without explicit tooling. These results indicate that augmenting LLM agents with domain-specific computation engines does not guarantee improved performance and may introduce conflicting optimization signals.

---


### 49. [PROOF-Gen: From Optimized Data to Better Distillation](https://arxiv.org/abs/2608.23911)

**<font color=#1a73e8>作者：</font>** Anh Ta, Junjie Zhu, Shahin Shayandeh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Supervised fine-tuning on teacher-generated trajectories is the standard first stage for distilling tool-calling capabilities into deployable models. Post-training pipelines that drive shipped tool-calling agents re-run this stage on a daily or weekly cadence, paying the frontier-teacher cost each cycle, yet the mechanism is generate-and-filter (keep the teacher's passing trajectories, discard the rest) and each cycle leaves behind the same hard scenarios because failures supply no signal. On {\tau}2-bench, 57% of teacher trials fail, two-thirds of them near-misses (most tool calls correct, undone by one decisive error).
We introduce PROOF-Gen (Per-scenario Reflective Optimization to Overcome FailedGeneration), which recovers golden trajectories from these failures via per-scenario prompt optimization. For each failed task, a reflector analyzes the execution trace and evaluation feedback, then writes corrective guidance that steers the teacher to a passing trajectory. The guidance is stripped before training, so the student learns from clean demonstrations with no task-specific scaffold.
On {\tau}2-bench, per-scenario optimization recovers 93% of failed scenarios. Fine-tuned on the combined data, Qwen3-4B-Instruct-2507 improves from Pass^1=0.132 to 0.529 and Gemma 4 E4B-it gains +7.2pp on BFCL v4 multi-turn. In a deployed pipeline, the method lifts trajectory quality by +6.3pp goal completion and transfers to a deployed on-device model (+1.5pp goal completion; +1.7 to +5.0pp across response-quality metrics), with positive transfer in every locale (non-English average +1.48pp).

---


### 50. [MARS: Multi-Specialist LLM Relay System for Competitive Programming](https://arxiv.org/abs/2608.23918)

**<font color=#1a73e8>作者：</font>** Andrei Mikhailov, Mikhail Burtsev, Alsu Sagirova  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models excel at code generation, yet competitive programming exposes a persistent failure mode: existing multi-agent pipelines distribute work over generic planner, coder, and debugger roles and delegate the choice of algorithmic technique to the backbone alone. We present MARS (Multi-Agent Relay of Specialized LLMs), a prompt-only framework in which each agent is a topic specialist---dynamic programming, graphs, strings, geometry, and so on---grounded by retrieval-augmented generation over an algorithm-theory corpus. Given a problem, retrieval selects a small team of relevant specialists; a starter writes an initial C++17 solution, and each subsequent turn runs the candidate against public examples in a sandbox, lets the active specialist keep, repair, or hand off the draft, and forwards a structured packet to the next specialist. A single infrastructure-fixer pass normalizes boilerplate at the end. On the CodeContests test split with Gemma 4, MARS reaches $0.624 \pm 0.006$ pass rate at $2.3$ recorded pipeline stages per task ($+14.4$ percentage points over direct prompting), closing most of the gap to CodeSIM ($0.731$) at $3.3{\times}$ lower wall-clock cost and substantially smaller variance in per-task token spend. The source code is available on GitHub: this https URL.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-190](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
