# 🧠 大模型相关研究 | 2026年10月21日

> 本类共 **548** 篇论文：已确认 **507** 篇，待复核 **41** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

---

### 151. [Native Probability Outputs for Clinical Triage: An Evaluation of Calibration and Decision Accuracy](https://arxiv.org/abs/2610.24692)

**<font color=#1a73e8>作者：</font>** Liang You, Zhiyin Zhou, Dawei Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Patient-facing triage requires an appropriate care recommendation and recognition of when information is insufficient. We evaluate whether Jev, a decision model that returns probabilities over predefined actions, supports both judgments. Using CARE-Bench, we compare Jev with four general-purpose language models and three input-independent baselines across 925 decision points from 439 public cases. On the public test subset, Jev ranks fourth of five models by macro-F1 (0.461) but has the lowest observed multiclass Brier score (0.610), an 18.7\% improvement over uniform prediction (case-bootstrap 95\% interval, 4.9--31.1\%). Noul has lower binary Brier than Choice (0.215 versus 0.276). A evaluation of 453 HealthBench conversations again gives Jev the lowest observed Brier score (0.299), but measures a distinct emergency-referral judgment. Jev combines lower probability error with missed clarification needs in the four-action task. Asking about information sufficiency separately increases recall but also produces frequent unnecessary clarification assignments.

---


### 152. [When Do Repetition Loops Lock? Truncation Sampling, Bounded Penalties, and a Blind Spot in DRY](https://arxiv.org/abs/2610.24715)

**<font color=#1a73e8>作者：</font>** Yichuan Chen, Xin Wang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models sometimes repeat verbatim until the generation limit. We study the exit rather than the entrance: given that a span has already been repeated $n$ times, when is escape still possible? Along the loop the context is deterministic, so loop survival under any sampler can be computed exactly from one forward pass. Pure sampling leaves a positive escape probability at every step; top-$p$ with threshold $\pi>1/2$ locks a position exactly when the continuation probability reaches $\pi$. A bounded penalty can leave a position locked; a penalty that outgrows the model's preference for the loop over unseen tokens guarantees escape under top-$p$. The same analysis predicts a blind spot in the widely deployed DRY sampler: its sequence breakers cap the penalty at $\lambda b^{g-1-a}$ for loops whose longest breaker-free run has $g$ tokens. On eleven open models, 66\% of locked units with $g=6$ stay locked under DRY and 1\% with $g=8$. In free generation with this http URL, all 109 loops that survive DRY have $g\le 7$. We propose DRY-C, which adds a term that grows exponentially with the number of verbatim recurrences, up to its look-back window. With it, none of 720 structured-output generations looped to the length limit, and task completion stayed close to DRY's.

---


### 153. [DiffuPlan: Editable Planning State for Diffusion Language Model Agents](https://arxiv.org/abs/2610.24717)

**<font color=#1a73e8>作者：</font>** Qisheng Zhou, Zhen Xiong, Qiaoyu Tan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (dLLMs) are emerging as an alternative to autoregressive (AR) language models, yet dLLM agents largely inherit an interaction protocol designed for AR generation: once intermediate state is written, later observations can only be incorporated by appending more text. This is a poor match to a defining capability of dLLMs -- reconstructing earlier text conditioned on context that appears both before and after it. We ask whether this capability can support a different agent-state paradigm in which intermediate planning state is directly revisable as evidence arrives. We introduce DiffuPlan, a diffusion search agent that maintains a single editable planning state and reconstructs only the affected steps when later evidence resolves an entity or changes the search route. To support variable-length revisions, we introduce Expansion-Partition Marginalization (EPM), which marginalizes over equivalent expansion paths. We further adapt diffusion trajectory RL to multi-turn search. Across four multi-hop QA benchmarks, DiffuPlan achieves 50.24 average F1, outperforming strong AR search agents. More importantly, under identical data and training, editable planning state improves the diffusion agent by 2.44 F1 versus only 0.47 for its AR source model. These results show that dLLMs need not imitate append-only AR agents: revising committed state is a distinct agentic advantage.

---


### 154. [PV-Decoding: Progressive Verification Decoding with Decode Gating for Diffusion Language Models](https://arxiv.org/abs/2610.24722)

**<font color=#1a73e8>作者：</font>** Renxi Liu, Yiming Li, Shengyin Sun 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Discrete diffusion language models (dLLMs) offer an attractive alternative to autoregressive generation by updating multiple tokens in parallel, but their inference efficiency is still limited by the cost of safely committing tentative predictions. In particular, speculative decoding for dLLMs is challenging because speculative tokens within the same diffusion block may depend on one another, making aggressive acceptance prone to error propagation and strict verification computationally expensive. We present PV-Decoding, a confidence-driven speculative decoding framework with progressive verification for block diffusion inference. PV-Decoding partitions masked positions into directly decoded tokens, speculative tokens, and unresolved tokens using two confidence thresholds, and then verifies speculative tokens with progressively stronger policies, including single-batch, dual-batch, and multi-batch verification. This design exposes a practical accuracy--efficiency trade-off: weaker verification minimizes overhead, whereas stronger verification improves acceptance precision and robustness. Experiments on three diffusion language models across GSM8K, MBPP, and HumanEval show that PV-Decoding reduces sequential model forward passes (MFPs) by 8%--37% relative to confidence-based decoding, while keeping the largest observed accuracy drop to 1.3%. On Dream-7B-Instruct/GSM8K, PV-Decoding (1-batch) and PV-Decoding (2-batch) improve throughput by 7.0%--13.6% under the same hardware budget, whereas PV-Decoding (multi-batch) is slower under the current runtime. These results suggest that confidence-guided speculation with structured verification is a practical path toward efficient and reliable dLLM inference.

---


### 155. [Where Natural Language Ends in Agents: Executable Skill Composition with MetaSkill](https://arxiv.org/abs/2610.24723)

**<font color=#1a73e8>作者：</font>** Meng Shu, Wei He, Hang Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent Skills express open-ended task knowledge in natural language, but composing them requires persistent execution order and upstream-output handoffs. We propose selective formalization at Skill boundaries: coordination relations with stable references and machine-checkable constraints become executable, while substantive task judgments remain within Skills. We introduce MetaSkill, a hybrid representation that preserves complete Skill packages and local instructions while making invocation dependencies and predecessor-text bindings executable through a directed acyclic graph (DAG) runtime. This interface supports explicit coordination without prescribing how each Skill performs its local task. Across 20 multi-Skill artifact tasks and two LLMs, we compare natural-language procedures, prompt-visible graphs, and MetaSkill derived from a common frozen plan per task, using the same designated Skill packages. Additional comparisons evaluate AgentSkillOS with the same available Skill packages as MetaSkill, as well as agent systems using their configured tools. Blinded artifact judgments yield favorable preference point estimates across all reported comparisons, with 95% task-bootstrap intervals excluding parity against Prompt Graph under DeepSeek-V4-Flash and OpenClaw under GLM-5.2. In audited GLM-5.2 execution traces, all planned nodes complete and all declared precedence constraints are satisfied. Together, these findings support MetaSkill as a practical interface for composing open-ended Skills, combining local linguistic flexibility with executable dependencies, explicit predecessor-text bindings, and auditable coordination. Code is available at: this https URL

---


### 156. [fxBench: Evaluating and Understanding Formula Suggestions in Spreadsheets](https://arxiv.org/abs/2610.24729)

**<font color=#1a73e8>作者：</font>** Sanket Mhatre, Sumit Gulwani, Vu Le 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spreadsheets are among the most widely used tools for computations, and formulas are their core building blocks. Besides agentic spreadsheet tools, proactive formula suggestions enable significant productivity gains and are now available in popular spreadsheet software (Microsoft Excel and Google Sheets). Such suggestions pose interesting challenges: the right context must be collected and represented for a machine learning model, which must then be able to write a correct formula, in a way that is fast and cheap enough to trigger on every = (or subsequent keystrokes for auto-completion) without taking users out of their editing flow. Surprisingly, there is no public benchmark for formula suggestions on real spreadsheets. In this paper, we therefore (1) introduce fxBench as a manually curated benchmark of 503 formula suggestion tasks based on Sheetpedia, (2) break down the formula suggestion problem into four capabilities (gather context, understand context, understand intent, write formula) that a formula suggestion system requires, and (3) evaluate existing and new approaches to understand bottlenecks in these capabilities that pose interesting research directions. Specifically, we annotate each benchmark with the cells that describe intent to determine the theoretical performance limit of a given context selection strategy, we evaluate performance of small and large models on different representations of context, including a dense format with high theoretical coverage at low token counts, and we fine-tune smaller language models to show that we can learn to understand such dense formats. Additionally, we perform quantitative and qualitative analysis on failure modes to understand bottlenecks in the formula writing capability; the best configuration only achieved 58.8% correct suggestions.

---


### 157. [Can LLM Agents Resolve Service Failures? Simulating Multi-Turn Complaint Handling under Information Asymmetry](https://arxiv.org/abs/2610.24733)

**<font color=#1a73e8>作者：</font>** Wailing Ng, Mengze Hong, Chen Jason Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents are widely adopted in service chatbots for rule-guided support and information access, yet emotionally demanding complaint handling still relies heavily on human agents. We introduce ServiceBench, to our knowledge the first benchmark dedicated to complaint handling, with 2,500 scenarios spanning 184 complaint categories and five service industries. We propose Asymmetric Progressive Complaint Simulation (APCS) to simulate realistic complaint handling, together with a justice-based evaluation framework. Our experiments reveal that even capable LLM agents struggle to handle complaints effectively. They lack the ability to proactively gather information and strategically guide conversations toward resolution, often resorting to premature compensation. We further show that targeted post-training with SFT and DPO substantially improves these capabilities, enabling a smaller model to match or surpass much larger models on several outcomes.

---


### 158. [Are We Evaluating VLM Token Pruning Right? Looking Beyond Accuracy and Token Count](https://arxiv.org/abs/2610.24740)

**<font color=#1a73e8>作者：</font>** Geng Li, Guohao Chen, Shilin Shan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Visual token pruning aims to reduce inference cost while preserving the capabilities of the original VLM. Yet existing evaluations rely on aggregate task accuracy and retained token count as proxies for pruning quality and actual efficiency. We reveal two limitations: 1) Aggregate accuracy can obscure whether a pruning method truly identifies critical visual tokens; many examples remain solvable under arbitrary token removal and models can exploit textual shortcuts when visual evidence is degraded. 2) Retained token count is an unreliable proxy for efficiency, as identical token budgets can incur different end-to-end costs depending on where and how pruning is performed. Consequently, comparisons based on aggregate accuracy and retained token counts fail to recover the global performance-efficiency Pareto frontier across methods. We introduce PAA-Bench, a plug-and-play evaluation framework for existing benchmarks, to evaluate whether pruning succeeds through meaningful token selection and whether this success translates into real speedup. To determine when token choice actually matters, we propose Random-Pass@k to measure how often an example remains correct under random pruning, enabling comprehensive evaluation across different levels of selection difficulty. To compare efficiency fairly, we introduce Preservation-Constrained Speedup (PCS) to report the maximum end-to-end speedup each method achieves under a shared preservation target. Experiments across 8 methods, 3 VLM backbones, and 9 benchmarks show that stronger token compression does not necessarily yield greater speedup, method differences widen on examples where token selection matters, and efficiency rankings change with the preservation target.

---


### 159. [ReTRACE: Feedback-Guided LLM Agent in a Chemistry Harness for Retrosynthesis Planning](https://arxiv.org/abs/2610.24744)

**<font color=#1a73e8>作者：</font>** Jinxiang Xie, Yijian Zhang, Qingyuan Yi 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-aided retrosynthesis has advanced through single-step prediction, tree search and route scoring, but complex targets still require judgement over the whole route, where stereochemistry, functional-group compatibility, cost and greenness interact. Here we present \textbf{\mbox{ReTRACE}} (\textbf{RE}trosynthesis with \textbf{T}ool-orchestrated \textbf{R}easoning \textbf{A}nd \textbf{C}ontext-aware \textbf{E}vidence), an agent that places a large language model (LLM) in a chemistry harness that integrates molecular tools, complementary single-step prediction engines, a purchasable starting-material library, a route memory and a multi-criterion route evaluator. Routes are judged by a new metric that combines programmatic checks with adversarial LLM review, and its verdicts are compared with a synthetic chemist's. The agent learns continually from evaluator feedback during search, diagnosing weak routes and backtracking to revise them. With Claude Opus 4.8, at least one of the top 10 routes proposed by ReTRACE passed the audit for 87.4\%, 95.0\% and 86.7\% of targets on the three benchmarks. Two prospective wet-lab syntheses show that ReTRACE route proposals can be converted into executable procedures after expert revision.

---


### 160. [BanglaBBQ: A Bias Benchmark for Question Answering in the Bangladeshi Context](https://arxiv.org/abs/2610.24764)

**<font color=#1a73e8>作者：</font>** Sumit Anthony Gomes, Yasin Rahman, Taeeba Tasnia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper introduces BanglaBBQ, a question-answering bias benchmark designed to capture stereotypes grounded in the Bangladeshi context, in both Bangla and English. Following KoBBQ and PakBBQ, BanglaBBQ adapts the original Bias Benchmark for Question Answering (BBQ) by classifying its templates into three groups: directly translated (DT), modified to align target groups or contexts with Bangladesh (TM), and removed when deemed unsuitable for the Bangladeshi context (SR). This process retains 140 templates across six categories, comprising 76 DT and 64 TM templates. Five newly authored (NA) categories, based on stereotypes common in Bangladeshi society, are then added: marital status, age and political perception, regional origin, educational background, and mental-health status. Native Bangladeshi annotators judged all 466 newly authored templates, and 372 were retained because a strict majority of English annotators identified the intended target and rated the attitude as common enough. Each newly authored template is linked to a documented source and a verbatim quote from it. Each evaluated template also has a counter-stereotypical version of its disambiguated context. The dataset was evaluated using two open-weight models (Qwen3-4B and Qwen3-8B) and two closed models (GPT-4.1-mini and Gemini 2.5 Flash). All four lean towards the stereotyped person when the context is ambiguous, in both languages, and the effect of language differs by model, so English results do not predict behaviour in Bangla. On the adapted BBQ templates, both Qwen3 models are also less accurate when the context contradicts a stereotype than when it confirms it. On the newly authored templates, the closed models follow counter-stereotypical evidence almost perfectly, and all four models are more biased on the templates that annotators validated than on those they rejected.

---


### 161. [Design Anything, Design at Scale](https://arxiv.org/abs/2610.24771)

**<font color=#1a73e8>作者：</font>** Xuchao Ren, Siyuan Feng, Jing Huang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As multimodal resources are transformed into media outputs, agentic AI is expected to stay aligned with design intent over long horizons. Designers follow briefs specifying goals, constraints, and deliverables, with later work building on earlier decisions. Recent work reuses design experience across tasks, yet alignment among artifacts within one project remains challenging. Agents therefore need to preserve and apply this intent across domains and as projects grow. We introduce Design Anything, a graph-based harness that preserves design intent outside the model and binds deliverables to the workflow steps that produce them through an intent-execution graph. A task contract retains constraints and decisions, selected designs become explicit inputs to later generations, and a deterministic controller uses bindings and execution records to check output types and counts, identify outstanding deliverables, and guide subsequent turns. We also introduce DesignAnything-Bench, with 228 tasks across 19 design domains, including 38 project families at scales of 6, 14, and 24 artifacts. With the LLM held fixed, Design Anything satisfies 85.0% and 92.5% of the brief's factual constraints with DeepSeek V4.1 Flash High and GPT-5.6 Sol High, respectively, exceeding the strongest same-model baselines by 15.4% and 14.4%. These gains reach 25.1% and 23.0% on 24-artifact tasks. Under each model, Design Anything leads or ties in constraint satisfaction in 18 of 19 domains. Professional designers also prefer its complete deliverable sets over those of same-model baselines in a blind evaluation.

---


### 162. [ATLAS: Learning to Adapt LVLM Attention for Reasoning Video Segmentation](https://arxiv.org/abs/2610.24783)

**<font color=#1a73e8>作者：</font>** Hamidreza Dastmalchi, Ali Cheraghian, Aijun An 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning Video Object Segmentation (RVOS) aims to localize and segment objects referred to by natural-language expressions throughout a video. Although large vision-language models (LVLMs) implicitly encode localization cues in their attention maps, these attentions are often noisy, diffuse, and scattered across layers, heads, and modalities, limiting their direct use for segmentation. Existing methods typically rely on handcrafted attention-selection heuristics or computationally expensive attention refinement. We propose ATLAS, an attention adaptation framework that learns to transform raw LVLM attentions into object-centric localization cues. ATLAS treats attentions from all layers, heads, and modalities as structured features, combining high-resolution frame-level attentions that capture spatial information with low-resolution video-level attentions that encode temporal context. A lightweight U-Net equipped with temporal attention and FiLM-based modulation fuses these complementary representations to generate coarse segmentation heatmaps, which are propagated across the video using SAM2. Extensive experiments on challenging referring and reasoning video segmentation benchmarks show that ATLAS outperforms existing frozen-backbone methods. Code and models are available at \url{this https URL}.

---


### 163. [LLM Trojans that Increase Response Lengths and Cost](https://arxiv.org/abs/2610.24784)

**<font color=#1a73e8>作者：</font>** Zhengxing Li, Guangmingmei Yang, Nader Alfares 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Management of the token-based costs of using LLMs has emerged as a significant problem. Some frontier-model providers charge five times per response token than per prompt token, while others offer prefilling discounts for prompt tokens. In this paper, we devise a defense against a new data-poisoning attack that plants a Trojan which increases the length of the response (and hence the cost to the user) when its trigger is present in the prompt. In particular, we demonstrate how a subtle Trojan may trigger on semantically similar instructions of an instruction fine-tuned LLM.

---


### 164. [Video-Language Entailment for Video Similarity Estimation](https://arxiv.org/abs/2610.24786)

**<font color=#1a73e8>作者：</font>** Benedetta Liberatori, Lorenzo Vaquero, Elisa Ricci 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Comparing videos to assess their semantic similarity remains a challenging task for current Large Multimodal Models (LMMs), which are primarily trained with single-video objectives. While most prior works have focused on computing global similarity, recent studies have introduced the more challenging problem of concept-based similarity, which measures how similar two videos are with respect to specific concepts (e.g., activity, location). However, no dedicated approaches have yet leveraged LMMs to explicitly address this task. In this paper, we aim to fill this gap introducing Video Caption Entailment for video similarity estimation (VICE): a dual-branch design that leverages LMMs for cross-video reasoning. Each branch jointly processes one video and the caption of the other, measuring their alignment for a specific concept via video-language entailment. The outputs from both branches are fused to produce a final similarity score, along with a textual explanation of the model reasoning. This approach leverages the model's native single-video understanding while enabling fine-grained comparative reasoning between video and text. Experiments on ConViS-Bench and StepDiff show that VICE outperforms models that process both videos simultaneously, highlighting the promise of single-video reasoning for concept-based similarity estimation.

---


### 165. [Who Gets Unmasked? Sampler-Induced Bias in Diffusion Language Models](https://arxiv.org/abs/2610.24795)

**<font color=#1a73e8>作者：</font>** Xujun Che, Farsheed Haque, Depeng Xu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Diffusion language models (dLLMs) generate by gradually unmasking a canvas, so their samplers decide not only which token to write but also when to commit it. We show that this second decision changes who appears in generated text, a sampler-induced bias on top of the model's own. Common commit rules, including LLaDA's default, commit the positions whose sampled tokens are most probable; this peeking favors majority options. To separate the sampler from the model, we read the model's belief about a fork, such as a protagonist's gender, in one forward pass, and show that this belief matches exact sampling from the model. Measured against it, peeking samplers on LLaDA and Dream amplify occupational gender stereotypes and collapse opinion distributions, and confidence-based ordering shifts gender-balanced occupations toward men, more so under faster parallel decoding. We propose Fork-First Sampling, which decides the fork before anything else is written: it follows the belief or any target distribution, improves fluency, and avoids the stories that remark on the protagonist's gender, which prompt-based fixes produce, at the cost of one forward pass. Fairness evaluations of dLLMs should report the commit rule.

---


### 166. [Table Serialization Determines Which Relations Language Models Preserve](https://arxiv.org/abs/2610.24798)

**<font color=#1a73e8>作者：</font>** Junwei Ma, Arun Kumar Chithanar, Palash Goyal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study how text serialization affects table lookup in instruction-tuned language models. Our diagnostic asks the model to find the row containing a specified value under one named column, then return the value under another named column in that same row. We render the same synthetic 256-cell tables in row-major form and in column-major form with each header placed beside its values, while varying the table aspect ratio across five shapes. Across three models, the better format changes with table shape: row-major performs better on tall tables, whereas column-major performs better on wide tables. At 64 x 4, row-major leads by 42.3-54.0 percentage points; at 4 x 64, column-major leads by 35.0-59.0 points. Mapping wrong answers back to their source cells reveals a complementary error pattern: row-major tends to preserve the correct row but lose the target column, while column-major tends to preserve the correct column but lose the row. We use the term relational locality to describe this pattern: serialization keeps one relation locally available while making the other depend on positional alignment. A separate non-tabular ordering experiment supports this interpretation. Thus, apparent width-related failures in text-serialized tables depend on linearization, not table shape alone.

---


### 167. [Medical Fine-Tuning Reshapes, Not Reduces, Patient-Facing AI Risk: A Rubric-Based, LLM-Judge Evaluation Framework](https://arxiv.org/abs/2610.24807)

**<font color=#1a73e8>作者：</font>** Savan Doshi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Patient-facing medical question answering with large language models (LLMs) is moving from research demonstrations to production deployments, yet evaluation remains anchored on factual correctness. Factuality is necessary but not sufficient: a response can be factually grounded and still issue a directive that, if acted on, would harm the patient. We introduce a risk-sensitive evaluation framework that scores responses by the presence and severity of six categories of risk-bearing language (treatment directives, contraindications, dosage expressions, urgency-triage cues, high-alert medication mentions, and overconfident assertions), anchored on published clinical harm taxonomies. Severity is classified by a three-judge LLM ensemble. We apply this framework to six 7-9B instruction-tuned models, three general (Mistral-7B, Phi-3.5-mini, Llama-3.1-8B) and three medically adapted (BioMistral-7B, OpenBioLLM-Llama3-8B, Med42-Llama3-8B), on 200 real patient questions from the K-QA benchmark. Two findings emerge. First, ensemble risk-bearing language is statistically independent of factual hallucination rate (pooled Spearman $\rho = -0.065$, $n = 300$, 95% CI $[-0.18, +0.05]$; distance correlation $= 0.10$, independence test $p = 0.24$). Second, medical fine-tuning does not reduce aggregate risk but reshapes it: continued-pretraining adaptations (BioMistral, OpenBioLLM) consistently suppress high-alert medication mentions while amplifying overconfident assertions, whereas clinical instruction-tuning (Med42) suppresses dosing only, without amplifying overconfidence. Per-category Krippendorff $\alpha$ is fair to good for the four linguistically anchored categories (0.53-0.71) and low for the two clinical-judgment-dependent categories (0.19, 0.31), indicating where automatic safety evaluation is and is not yet reliable. We release the rubric, judge prompts, and evaluation code.

---


### 168. [Ask, Don't Guess: Targeted Clarification for Speech Recognition Errors](https://arxiv.org/abs/2610.24809)

**<font color=#1a73e8>作者：</font>** Sankalp Parashar, Preethi Jyothi, Sunita Sarawagi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech recognition in real time in far-field conversational settings still incurs significant errors. Identifying potential error spans during streaming ASR permits a recourse mechanism where the speaker can be asked to repeat the affected content under cleaner acoustic conditions. We propose \sysname, a new framework for online error localization, that identifies spans likely to benefit from this intervention. Our supervision uses clean audio to estimate how the recognizer's output might change under improved acoustic conditions. We probabilistically align noisy and clean decodes using a pair-HMM to obtain soft supervision. These soft targets train a counterfactual gain scorer by combining a suite of acoustic and language features to produce token-level scores, that are further grouped into spans for targeted recourse. An LLM uses the ASR transcript of the repetition to revise only the selected span. At a precision of $70\%$, \sysname achieves the highest recall by identifying up to 52\% more erroneous tokens compared to the strongest baseline. Targeted repetition yields relative WER reductions of up to 24\% under a budget that accounts for both interruption frequency and the lengths of re-uttered spans.

---


### 169. [First-Order LoRA Training with Phone NPUs](https://arxiv.org/abs/2610.24816)

**<font color=#1a73e8>作者：</font>** Xu Zheng, Wei Cheng, Zhuomin Chen 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device fine-tuning lets a large language model (LLM) learn from its user's private data without uploading it. Low-rank adaptation (LoRA) reduces the trainable parameters, but each first-order training step still multiplies by the frozen base-model weights during the forward pass, activation recomputation, and input-gradient computation. A phone's neural processing unit (NPU) already holds these weights for inference; using it for training also requires computing input gradients, which its inference interface does not support. We present a system that runs all three frozen-weight products on the NPU while keeping the training graph, adapters, and optimizer on the CPU. Its input-gradient kernels reuse the resident weight tiles and the forward dequantizer, avoiding a transposed weight copy and ensuring forward and backward use the same effective weights. To preserve usable gradients, the system selects precision by gradient sensitivity and applies a per-row range guard for half-precision (FP16) outputs. Its runtime fuses the remaining CPU operators and overlaps NPU execution with adapter computation, while resumable execution and thermal pacing let training proceed as a background job. We evaluate it on two Qualcomm Snapdragon platforms using four LLMs from the Qwen and Llama families. Our workloads cover nightly personalization with labels supplied on the phone and the public LaMP-2 benchmark; comparisons include an optimized CPU trainer, a phone-GPU trainer, forward-only training, and GPU-trained references.

---


### 170. [Efficiency Measured in English: Tokeniser Coverage Bounds Small Language Models on Indic Scripts](https://arxiv.org/abs/2610.24818)

**<font color=#1a73e8>作者：</font>** Anna Pramod  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Small Language Models with quantisation and parameter-efficient adaptation are widely offered as the route to multilingual AI under compute constraints, and their efficiency is almost always reported as a single memory figure. We show that this figure is measured in English and does not transfer. Across a 131k-sentence corpus spanning eleven Indic scripts, TinyLlama-1.1B's tokeniser emits 1.34 subword tokens per Latin-script word and 22.60 per Kannada word. This is not inefficiency; it is absence. Its vocabulary contains 0% of Odia's codepoints, 1% of Telugu's and 2% of Kannada's, and for five of eleven scripts the measured fertility sits at the UTF-8 byte-fallback ceiling, on Odia at 99.6% of it, with 93.6% of emitted tokens being raw bytes. Because SentencePiece byte fallback never raises an unknown-token marker, this failure is entirely silent: TinyLlama's UNK rate is 0.0% on every script, including the one it reads as bytes. We further show that low fertility can indicate the opposite of efficiency: mBERT posts its best score anywhere (1.10 tokens/word, on Odia) while discarding 87.9% of the text as UNK. MuRIL, an Indic-vocabulary encoder with a fifth of TinyLlama's parameters, reads every script at 1.23-2.26 tokens/word with zero UNK and zero byte fallback. The binding constraint is the vocabulary, not the parameter count. The consequence is concrete: on a 2048-token context window, the same model gives an English user 1,528 words of usable context and a Kannada user 91.

---


### 171. [Pair-Aware Optimization: Coordinating Exploration and Refinement for Jailbreaking LLM Agents](https://arxiv.org/abs/2610.24823)

**<font color=#1a73e8>作者：</font>** Juanyang Xu, Zheng Wang, Xingyu Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are vulnerable to adversarial inputs that induce attacker-specified malicious behaviors, commonly referred to as jailbreaking. Existing optimization-based jailbreak attacks primarily employ first-order (FO) methods that leverage gradient information or zeroth-order (ZO) methods that rely on function-value feedback. However, their complementarity and optimization ordering remain underexplored. We systematically investigate four strategies: pure ZO, pure FO, ZO->FO, and FO->ZO, and develop a ZO-FO framework that explores adversarial prefixes through ZO optimization and refines their corresponding suffixes through FO optimization. To coordinate the two processes, we introduce Pair-aware optimization, which retains multiple prefix candidates, conditionally refines their suffixes and selects among the resulting prefix-suffix pairs. We further investigate agent jailbreaking from a more general stochastic-generation perspective, where the same adversarial input can induce diverse reasoning trajectories and actions that a single greedy output cannot capture. Accordingly, we adopt consistent stochastic decoding during both optimization and evaluation. Experiments across malicious-instruction and malicious-environment benchmarks demonstrate that hybrid optimization improves attack effectiveness over single-optimizer methods, while optimization order substantially influences performance.

---


### 172. [Teaching Code Agents to Ask Without Leaking Private Code](https://arxiv.org/abs/2610.24824)

**<font color=#1a73e8>作者：</font>** Wenjia Jiang, Jieke Shi, Zhensu Sun 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Local coding agents can extend their reach by consulting a stronger cloud model. Such consultations, however, often expose the repository's private identifiers, file paths, and source code. Host-side masking hides recognized identifiers but leaves the surrounding code and the agent's phrasing unchanged, while training for less disclosure risks suppressing consultation or producing questions too vague to answer. We propose utility-verified abstraction (UVA), which teaches the agent to describe private entities by their role and type while retaining the technical details an expert needs. From solved repair trajectories, we rewrite each question into this form and keep the rewrite only if it discloses fewer private entities and the repair, replayed from the same execution state with the repair trajectories. Across two benchmarks, the trained agent consults more often than before training. On repository-level issue repair, it solves 37.6% of issues, against 25.3% for the same model working alone, a gain from the training as a whole rather than from consultation alone. Its questions disclose 3.7-fold fewer private entities and 1.4-fold less verbatim code than the untrained agent's questions to the same expert.

---


### 173. [Pattern-Driven Evaluation of LLM Code Optimization: Isolating Compiler-Transcendent Semantic Reasoning](https://arxiv.org/abs/2610.24835)

**<font color=#1a73e8>作者：</font>** Wesley Lu, Runzhou Liu, Hongru Du 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Existing evaluations of LLM-based code optimization primarily measure end-to-end speedup, obscuring whether a model actually performs the intended optimization. For compiled languages, this is especially problematic: observed gains may reflect transformations already recoverable by modern optimizing compilers rather than optimization behavior attributable to the model itself. We present PatternBench, a benchmark for studying compiler-transcendent optimization, i.e., performance improvements that remain after aggressive compiler optimization. PatternBench targets residual optimization opportunities across seven classes of transformations and pairs runtime evaluation with an AST-based optimization faithfulness analysis that verifies whether the intended optimization is realized in the generated program. Experiments with frontier, open-weight, and fine-tuned models show that runtime speedup alone provides an incomplete account of optimization capability. Optimization faithfulness is strongly associated with realized speedup, and fine-tuning improves both faithfulness and optimization effectiveness. These results suggest that evaluation of LLM-based code optimization should measure not only performance outcomes, but also whether the target transformation was successfully executed.

---


### 174. [A Statistical Viewpoint on Adam, Shampoo and Muon](https://arxiv.org/abs/2610.24839)

**<font color=#1a73e8>作者：</font>** Tetiana Parshakova, Robert M. Gower, Paulo Orenstein  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We provide new statistical insights into designing stochastic optimization methods. By modeling the gradient via a normal distribution, we argue that the stochastic gradient should be whitened using its covariance. We give an online method for estimating the mean and variance of the gradients based on regularized likelihood or, equivalently, through a maximum a posteriori estimate. We then show how to use structured approximations to the covariance within this same framework, which includes diagonal and Kronecker-factored approximations. The diagonal approximation results in a method that is very closely related to Adam and performs as well in practice. The Kronecker approximation results in the new MN method, which is a variant of Shampoo and KL-Shampoo. We also recover Muon by applying this same statistical framework to the gradient direction rather than the full gradient. By combining this with a whitening step, we arrive at MN-Muon, a novel preconditioned version of Muon. Our experiments on GPT-2-type models at Chinchilla scale indicate that MND, the diagonal implementation of MN, outperforms both the Distributed Shampoo and the KL-Shampoo implementations in terms of stability, final validation loss and time taken. MND-Muon, the diagonal implementation of MN-Muon, improves on Muon in 21 of 24 paired GPT-small runs and achieves a lower best validation loss on GPT-medium, where it remains stable over the six tested learning rates. However, we found that NorMuon was comparable to MND-Muon and achieved a slightly lower validation loss on GPT-medium and at GPT-small batch 512 on FineWeb.

---


### 175. [AgentSoV: Virtual Sensing for LLM Multi-Agent Systems via Stream of Variation](https://arxiv.org/abs/2610.24845)

**<font color=#1a73e8>作者：</font>** Congjing Zhang, Siyuan Xu, Yunfei Bai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) multi-agent systems (MASs) solve complex tasks through interacting agents, yet their reliability is difficult to analyze because failures depend on both individual agents and how information and errors propagate across the system. Existing approaches largely treat this as post-hoc failure attribution, but do not provide a common model across heterogeneous MAS architectures or support broader analysis of information influence and observability. We introduce AgentSoV, a virtual-sensing framework that models MAS execution as a stochastic dynamic system through Stream of Variation (SoV). AgentSoV maps heterogeneous trajectories into diagnostic stages, constructs virtual measurements from observable outputs, and learns cross-stage variation propagation with a state-space model. Its representation is architecture-aware in stage dependencies yet architecture-agnostic in analytical language, supporting chain-structured, orchestration-based, and directed acyclic graph (DAG)-structured MASs. Without re-executing the MAS, AgentSoV supports three system-level analyses: failure attribution identifies where abnormal variation enters; stage-input influence quantifies how strongly intermediate inputs affect downstream outcomes; and virtual-sensor placement selects complementary observations under a monitoring budget. Experiments across multiple MAS architectures demonstrate a unified approach to fault localization, information influence, and observability. AgentSoV reframes agentic execution as a dynamic system to model rather than merely text to inspect, providing insights for MAS structure and component design.

---


### 176. [MisleadQA: Diagnosing LLM Failures under Misleading Context](https://arxiv.org/abs/2610.24851)

**<font color=#1a73e8>作者：</font>** Hui Wang, Bohao Chu, Qianli Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are widely used to answer questions from retrieved or user-provided context. However, provided context can be factually true yet out-of-scope, describing a different entity, time, or location from the one the question targets, and still lead models to a wrong answer. Prior work has mainly studied factually false or irrelevant context. It remains unclear whether such out-of-scope context misleads models as much as false context, and whether adding gold context prevents models from being misled by either. We introduce **MisleadQA**, a diagnostic dataset of multiple-choice questions with an abstention option. Each question pairs gold context (G) with true but out-of-scope context (S) and false but in-scope context (F) supporting the same wrong answer. We evaluate six open-weight LLMs. On questions they answer correctly without context, providing S alone leads them to switch to this wrong answer in 29.3% of cases, and providing F alone does so in 75.4%. Adding G nearly removes the effect of S, but F still misleads models in 21.0% of cases, especially when F comes first. A context-faithful instruction reduces these errors mainly through abstention and lowers accuracy even with G. These findings suggest that evaluations should check whether context applies to the question, not only whether it is true, and should report correct, misled, and abstention rates together. Data and code are available at [this https URL](this https URL).

---


### 177. [Learning to Program Retrievals: Composing Search Primitives via Reinforcement Learning](https://arxiv.org/abs/2610.24854)

**<font color=#1a73e8>作者：</font>** Kyuyoung Kim, Zilin Xiao, Zhiyuan Wang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented language models increasingly use multi-step search to solve knowledge-intensive tasks, yet existing systems typically expose retrieval through fixed pipelines or collections of atomic tools. We introduce Retrieval Program Learning (RPL), a programmable search framework that allows a policy to compose search primitives into executable programs with local state and control flow. This enables adaptive search that can retrieve broadly, process intermediate results, and selectively construct model context without tying retrieval breadth to context consumption. However, the resulting flexibility creates a difficult exploration problem: useful programs may require several coordinated decisions, while reinforcement learning often supplies only sparse feedback. To address this challenge, we propose program mutation, a grammar-constrained and execution-verified procedure that generates local variants of suboptimal programs sampled during RL, converts them into training trajectories, and distills them back into the policy. We evaluate RPL on open-domain question answering and corpus-level reasoning tasks, comparing it with a range of retrieval and reasoning baselines. RPL consistently improves open-domain QA performance across model sizes and in- and out-of-domain benchmarks, with particularly large gains on multi-hop tasks. Notably, a 4B model trained with RPL outperforms all 8B model baselines. On corpus-level reasoning, RPL achieves the highest answer F1 and document-coverage F1 for both model sizes while substantially reducing context consumption and retrieval turns. Our results show that programmable search expands the retrieval strategies that agents can learn, while program mutation provides an effective mechanism for exploring useful program structures beyond direct on-policy sampling.

---


### 178. [LLM-Based Evaluation Planning for Heterogeneous Optimization](https://arxiv.org/abs/2610.24855)

**<font color=#1a73e8>作者：</font>** Nian Ran, Sebastian Brulin, Markus Olhofer 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous optimization problems require an optimizer to decide not only which candidate solutions to evaluate, but also which objectives and constraints should be evaluated under different costs and fidelities. Existing SOTA methods such as MFE-NSGA-III address this setting with manually designed selection metrics, but their behavior is largely determined by predefined heuristic rules and hyperparameters. In this work, we propose REP-HO, a reasoning-based evaluation planner that replaces the rule-based mixed-fidelity selection step with a large language model (LLM) planner. The LLM receives the same primitive optimization-state information as the heuristic planner, such as surrogate predictions, uncertainties, evaluation costs, and budget status. We first show that REP-HO achieves competitive performance compared to the human-designed metric-based method (MFE-NSGA-III). We then further enhance each decision with an adaptive nearest-neighbor summary, leading to better and more stable results. We evaluate REP-HO across five heterogeneous regimes covering cost imbalance, constraint difficulty, surrogate fidelity, budget level, and objective conflict. Across these regimes, one of the two variants obtains the best mean ranking score in every regime, REP-HO(Deepseek) is first or second throughout, and the planner shows adaptive allocation behavior, such as prioritizing constraint evaluations under tighter budgets and reallocating constraint evaluation budget when surrogate reliability changes. These results suggest that LLMs can serve as flexible evaluation planners for heterogeneous optimization, offering a general alternative to fixed hand-designed metrics.

---


### 179. [FlowMaker: From Tasks to Cost-Efficient Generative AI Workflow Deployments](https://arxiv.org/abs/2610.24861)

**<font color=#1a73e8>作者：</font>** Dimitrios Liakopoulos, Prasoon Sinha, Neeraja J. Yadwadkar  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Generative AI workflows execute user tasks by composing sequences of LLM calls, where each call performs a sub-task (e.g., summarization or translation), forming a workflow. Executing such workflows requires decisions over workflow structure, model assignments, and deployment configurations, which jointly determine latency, cost, and accuracy under dynamic workloads and resource constraints. Existing systems optimize these decisions in isolation or fix them early, leading to suboptimal cost and goodput. We make two key observations. First, efficient serving requires jointly exploring all combinations of workflows, model choices, and deployment configurations under dynamic cluster state. Second, reuse of deployed LLMs is critical for reducing cost, but must be performed on-the-fly, as reuse depends on current load and resource availability. Together, these make selecting a workflow-variant-a combination of workflow, models, and deployment configuration-a time-critical problem. We present FlowMaker, which exposes a task-level interface and selects workflow-variants on behalf of users. To realize this, we design a constraint-guided load-aware pruning algorithm for fast, on-the-fly decisions. FlowMaker improves goodput by up to 10.14$\times$ and reduces cost by up to 2.77$\times$ compared to state-of-the-art baselines, including Murakkab.

---


### 180. [Bellman Language Models: Solving the Recurring Decisions of LLM Agents](https://arxiv.org/abs/2610.24871)

**<font color=#1a73e8>作者：</font>** Adarsh Vatsa, William Eiers  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A general observation in agentic workflows, especially bounded ones, is that the decision space of the LLM, when we separate a decision from generation, starts approaching saturation: the agent meets the same states again and again, and after enough conversations it stops meeting new ones. LLMs generally don't treat these decisions as an optimization problem and instead re-derive them from their context/prompt on every turn. We show that treating decision making within reasonable bounds as an optimization problem, solving it once, and reusing the solved decisions can often make an agent faster, cheaper and more reliable. Our approach, which we call Discretize, Then Decide, starts from data such as the workflow's own logs or, when none exists, runs of the LLM agent itself. It reads each conversation into discrete states and estimates the probability of each outcome and the cost of each move, until no new states appear and the probabilities stop changing. It then solves the resulting Markov decision process. The solution runs as a controller around the model, sending moves whose content is fixed in the state, such as a tool call or a templated reply, and any state it hasn't seen is sent back to the LLM. We call an LLM run this way a Bellman language model (BLM), after Richard Bellman's equation for the best move in each state.
On $\tau^2$-bench telecom, the controller with no model solves 79% of tasks. As a BLM, Qwen3.8-27B, an open model, goes from 29% to 96% with 93% fewer model calls. For Claude Opus 5.5, which solves 96% of tasks on its own, running it as a BLM cuts model calls and cost per task by about 98% and lets it solve 2 more tasks. On InventoryBench, the solved policy with no model beats every published method. Where the hard part is writing content rather than choosing moves, such as resolving SymPy issues, few decisions can be solved in advance, and a BLM helps little.

---


### 181. [The One-Pixel of Reasoning: One Truthful Relation Is Enough to Mislead LLM Agents](https://arxiv.org/abs/2610.24873)

**<font color=#1a73e8>作者：</font>** Jinwei Hu, Youcheng Sun, Yi Dong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can one sentence manipulate an agent's belief by targeting a single implicit warrant linking evidence to a conclusion? In this paper, we introduce the one-relation attack (ORA), a novel cognitive attack on this inferential relation. ORA localizes a critical implicit warrant and performs a one-relation intervention using a single source-grounded sentence that qualifies this warrant and steers the agent toward an incorrect belief. Across eighteen models on biomedical inference and vulnerability detection, best-of-$10 attacks overturn initially correct answers at mean rates of 54.9% for proprietary and 80.0% for open-weight models. Attacks also transfer without victim feedback, and paired controls support the roles of targeting and qualification. Moreover, successful sentences can pass source-support checks and evade identification, and multi-agent debate raises team error from 50.0% to 59.5% in our balanced stress test. These findings establish implicit warrants as a cognitive attack surface for manipulating agents' beliefs.

---


### 182. [Goal Images Are Control Targets: Spatially-Grounded Goal-Image Synthesis for Robotic Manipulation](https://arxiv.org/abs/2610.24885)

**<font color=#1a73e8>作者：</font>** Riddhi Chatterjee, Ritish Shrirao, Kushagra Mehrotra 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Goal-conditioned manipulation policies are steered by a goal image, a picture of the desired post-manipulation scene synthesized from the current observation and a language instruction. The prevailing assumption is that better image-editing quality yields better goals, so goal generators are built and compared using general image-editing metrics. We show this assumption is false. Across two independent goal-conditioned policies on CALVIN, the image editors that top aggregate editing-quality leaderboards (Gemini 3 Pro Image and GPT Image 1.5) produce worse control targets than our proposed far smaller finetuned open models, and the gap widens sharply for the multi-step (long-horizon) tasks robots actually face. A per-dimension analysis explains why. Downstream policy success is governed almost entirely by manipulation adherence (selecting the right object and the right final state; Spearman $\rho \approx 0.9$ with success), while photorealism and aesthetic fidelity, precisely where large proprietary editors excel, are uncorrelated with success ($\rho \approx 0$). This dissociation holds on both CALVIN and the real-world-aligned SIMPLER-Bridge benchmark. We then present SGE-Goal, a spatially-grounded decomposed editing framework that predicts initial and final 2D edit-region masks before goal-image synthesis. SGE-Goal turns open base models (FLUX.1 Kontext, FLUX.2 klein) into the strongest goal generators we evaluate on CALVIN, and second only to Gemini 3 Pro Image on SIMPLER-Bridge. Base models fine-tuned with SGE-Goal also hold up under chaining far better than the best proprietary editor, sustaining roughly seven times the success rate at the longest (five-step) chains. We release code, datasets, checkpoints, and a human-aligned diagnostic evaluator. Our results argue that goal generators must be selected by downstream utility, not by editing-quality leaderboards.

---


### 183. [LastWords: Boring Problems Revisited](https://arxiv.org/abs/2610.24894)

**<font color=#1a73e8>作者：</font>** Huayang Li, Richard Sproat  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In 2022, the second author published a Last Words piece in Computational Linguistics in which he pointed out that, despite the advances in AI up to that point, there were still some problems in natural language processing that on the one hand seemed trivial and perhaps boring, but on the other were hard to solve using purely neural methods. One such problem discussed in that context was text normalization, and a particular subproblem of that, namely number name reading. The piece came out just a few months before the first release of ChatGPT, and needless to say, a lot has happened since then. Indeed, as we document here, the problem (of number name reading) has practically been solved, at least by one of the latest frontier models. However, we believe that there are still open issues for such limited domain, constrained and limited resource problems, and that in some future machine learning approach, the massive resources of the latest frontier models would not be needed to solve them.

---


### 184. [Peer Pressure: Execution-Verified Co-Evolution of Attacker and Defender Populations for Code Security](https://arxiv.org/abs/2610.24896)

**<font color=#1a73e8>作者：</font>** Khushbu Pahwa, Yubin Ge, Daniele Bonadiman 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM code agents increasingly ship code with little oversight, yet defenders trained on static vulnerability datasets fall behind adapting adversaries. We co-train attacker and defender instead, and let execution decide every reward: an attacker (Red) edits a real repository and earns nothing unless its patch applies, builds, passes the tests, completes its development task and reproduces a real exploit in an isolated container, whose path also labels the entry point, the critical operation and the trace between them.
Peer-Relative Policy Optimization (PRPO) makes both sides populations of LoRA adapters over one frozen base and credits each against same-role peers that faced an identical condition, placing the population inside the policy-gradient baseline rather than the opponent pool, with a tournament preserving diversity. Matching cancels the condition's difficulty: at equal coverage it is worth 2.3 points of balanced accuracy over a baseline computed on other conditions, and it matches a within-policy control at half the verifier spend.
PRPO's 7B diff reviewer reaches 64.8% balanced accuracy on four unseen applications in three untrained languages, 5.5 points above supervised security fine-tuning and 4.4 above a frozen frontier reviewer (Claude Opus 4.8), which it leads by 15.8 on the application it trains on. Its 9B repository agent recovers 23 of 172 held-out VulnGym advisories, against 10 after supervised fine-tuning and 7 for the same backbone untrained under the same scaffold, and locates 17 of 43 reachable entry points against 13 for mini-swe-agent with GLM-5.2. Run unchanged on jailbreak defense, the same algorithm matches or exceeds WildGuard's static F1 at equal corpus and model size. Under a judge distinct from its training oracle it cuts attack success from 36.0% to 4.6%, against WildGuard's 8.9%.

---


### 185. [HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents](https://arxiv.org/abs/2610.24899)

**<font color=#1a73e8>作者：</font>** Soyoung Yoon, Peiran Xu, Han Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While LLM agents are increasingly capable of gathering and synthesizing evidence from a single homogeneous source, such as structured tables or unstructured data, real-world analytical questions frequently span heterogeneous sources. For example, answering one enterprise question may require both a result computed over an internal database and evidence found on the web. Recent evaluations on benchmarks like HybridDeepResearch show that even frontier agents struggle when evidence must cross this boundary. While these benchmarks have exposed the limitation, methodologies to explicitly teach cross-source reasoning remain absent. To address this, we introduce HybridResearcher, a 4B agent trained to bridge evidence across the structured and unstructured boundary. To build it, we synthesize cross-source bridge trajectories by starting with validated single-source tasks-such as existing text-to-SQL or web search queries-and fabricating the missing source around a bridge entity drawn from the seed's own output. We retain a sample only when strict construction gates confirm that neither side alone suffices, ensuring the data requires true cross-source interdependence. Finally, we train on this curated dataset using supervised fine-tuning followed by reinforcement learning. Evaluated on the existing HybridDeepResearch benchmark, HybridResearcher improves over our base model, Qwen3.5-4B, by 30.0 points pass@8 and surpasses the far larger Qwen3.5-397B-A17B by 8.3 points, while also improving over its base model on established, held-out single-source benchmarks (BrowseComp and BrowseComp-Plus), demonstrating that this complex cross-source reasoning can be taught directly to small models without triggering catastrophic forgetting.

---


### 186. [Leveraging Mental Models for Human-Centered Explanations: A Systematic Design Approach Illustrated by Explainable Fake Review Identification](https://arxiv.org/abs/2610.24903)

**<font color=#1a73e8>作者：</font>** Sidra Naveed, Md Shajalal, Gunnar Stevens 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Explainable AI (XAI) often prioritizes model fidelity over user intelligibility, yielding explanations that satisfy technical transparency yet fail to support human sense-making. We propose a human-centered approach, MIND-X (Mental-model INtegrated Design for eXplainability), which aligns explanations with users' mental models, commonsense concepts, and judgment heuristics. Using fake review detection as a case study, we contribute: (1) a qualitative study (n=10) that elicits how people assess review credibility and produces an actionable, design-guiding taxonomy of perceptual cues; (2) a set of design principles that link those cues to explanation strategies and prompt LLMs to generate adaptive, language-based explanations; and (3) a quantitative evaluation (n=166) showing that these explanations offer distinct advantages over token-level transparency methods widely used in explainable text classification in terms of understandability, satisfaction, perceived trust, persuasiveness, and decision-making support. Rather than claiming general superiority, our evaluation illustrates how grounding explanations in users' everyday reasoning practices can produce more intelligible and context-sensitive accounts. Our findings advance human-centered explanation design beyond a mere "gloss of transparency," demonstrating that a mental-model-aligned design process can improve intelligibility and support accountability across user-centered explanation tasks.

---


### 187. [Compositional Activation Steering Across Languages and Behaviors with Contextual Gates](https://arxiv.org/abs/2610.24906)

**<font color=#1a73e8>作者：</font>** Daniil Gurgurov, Akansh Maurya, Josef van Genabith 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering has emerged as an effective and precise way to influence the behaviours of language models. However, composing multiple steering directions to control several behaviours simultaneously remains challenging, particularly in multilingual settings and with training-free steering vectors. We address this challenge with contextual steering, jointly training gates that adapt the strength of fixed steering directions to the current hidden state and interactions between interventions. Across a broad range of languages, behavioural attributes, and models, our approach outperforms constant-strength steering and four strong baselines, including prompting. It also better preserves general knowledge and keeps the model's internal computation closer to that of the prompted model. Our analysis further shows how jointly trained gates adapt their contributions during composition, explaining the mechanisms underlying effective compositional steering.

---


### 188. [CAT-RAG: Improving Secure Code Generation with Category-Aware Agentic Retrieval](https://arxiv.org/abs/2610.24907)

**<font color=#1a73e8>作者：</font>** Mahdieh Abazar, Lorenzo De Carli, Benjamin Tan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Despite rapid progress in LLM-based code generation, security vulnerabilities remain widespread, and retrieval-augmented code generation (RACG) can further amplify risk when retrieved knowledge is verbose or vulnerable to poisoning. Existing secure RACG approaches inject security knowledge at a fine-grained vulnerability level, causing prompt overhead and diluted model attention when a query implicates multiple related weaknesses. We propose CAT-RAG, an agentic security category-aware retrieval-augmented code generation framework. CAT-RAG performs adaptive category selection via an LLM as a categorizer agent and operates either as a standalone security layer or as a drop-in add-on to RACG pipelines, requiring no modification to the underlying model. We replace CWE-level retrieval with compact, language-specific security categories. These categories provide a higher-level abstraction over individual CWE weaknesses, organizing them by the security concern they share, such as Input Validation and Injection Attacks, rather than merely grouping related entries. Each category consolidates best practices and secure code examples into a single, prompt-efficient representation. We perform a comprehensive evaluation across CyberSecEval, CodeGuard+, and HumanEval. On CyberSecEval, CAT-RAG nearly doubles the secure code generation improvement over the state of the art (23.57% vs. 12.11%) while reducing token overhead by 41.71%.

---


### 189. [A Symmetry-Matching Approach to Blind-Spot Reduction in Sparse Autoencoders](https://arxiv.org/abs/2610.24908)

**<font color=#1a73e8>作者：</font>** Csaba Balogh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Language models can treat semantically distinct inputs as interchangeable at the representation level, creating blind spots that standard sparse autoencoder (SAE) objectives do not target. In safety-critical settings such as clinical dosage extraction, legal clause interpretation, or financial amount verification, such failures can propagate silently into downstream decisions. We study this problem as one of feature-basis orientation. Building on a symmetry-matching view from algebraic error-detection theory, we add a differentiable $V_{\mathrm{Gini}}$ regularisation term to SAE training that penalises uneven perturbation response within a specified family. Across GPT-2, Gemma 2, and Qwen 2.5, a frozen multi-seed evaluation shows that $V$-regularisation raises both relative and absolute lower-tail responses while reducing response-profile imbalance, with no material general-text reconstruction degradation. JumpReLU and minimum description length (MDL) objectives remain close to the Standard SAE profile under the same protocol. Family-geometry controls show that the effect is not explained by template duplication or a single dominant perturbation family, and held-out probes plus null-calibrated separation tests evaluate how far the representation-level change carries to downstream discriminability. A zero-shot audit on out-of-distribution clinical radiology minimal pairs finds the relative weak-tail lift in all evaluated model-by-family cells, not perfectly rank-aligned with the trained statistic, and a held-out family audit finds it on family kinds never used in training. Together, the results show that perturbation-aware SAE training can reorient feature bases toward safety-relevant input changes while leaving downstream validation as a separate empirical step.

---


### 190. [A Cross-Domain Evaluation of Prompting Techniques for Large Language Models](https://arxiv.org/abs/2610.24913)

**<font color=#1a73e8>作者：</font>** Kevin Krazius, Tim Schlippe, Paul Libbrecht  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prompt engineering has become a central mechanism for guiding the behavior of Large Language Models (LLMs) across a wide range of reasoning and language understanding tasks [1], [2]. However, existing studies frequently evaluate prompting techniques using different LLMs, datasets, or task settings, making direct comparisons across methods and domains difficult [3]. Consequently, in this paper we present a controlled cross-domain evaluation of Zero-Shot prompting, Few-Shot prompting, Retrieval-Augmented Generation (RAG), and automatic prompt optimization based on a PE2-inspired optimization pipeline [4]-[6]. All experiments were conducted with the same LLM and evaluated on six benchmark datasets covering arithmetic reasoning, logical reasoning, commonsense reasoning, and factual verification. The results show that no prompting strategy consistently outperforms the others across all domains, and pairwise statistical comparisons of the highest-performing configurations revealed no significant differences. RAG achieves the highest overall average accuracy of 78.33% when 300 examples are available for retrieval, while Few-Shot Prompting achieves comparatively high accuracies across several structured reasoning tasks. Zero-Shot Prompting remains competitive on tasks with self-contained inputs, whereas the PE2-inspired optimization approach produces stable but not systematically superior results compared to the other evaluated prompting techniques. Furthermore, increasing the number of task-specific examples does not consistently improve performance across prompting techniques, indicating strong domain and task dependency. These findings suggest that prompting techniques should be selected adaptively based on task characteristics rather than treated as universally applicable optimization strategies.

---


### 191. [Arctic-SWE: Revisiting the Long Horizon Agent Training by Modeling-System Co-Design](https://arxiv.org/abs/2610.24914)

**<font color=#1a73e8>作者：</font>** Boyi Liu, Yite Wang, Xinyu Lian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agent training, including software engineering, is advancing rapidly, but the recipe and infrastructure needed for a strong reinforcement-learning baseline remain difficult to reproduce. This makes gains from new algorithms or data hard to distinguish from improvements to an under-tuned baseline. We present Arctic-SWE, a fully asynchronous RL framework that establishes such a baseline through model-system co-design, using overfitting on a small task pool as the testbed. This testbed exposes failures that early reward gains conceal and guides the integration of established components: gated reward, importance-weight control, aligned training and inference engines, and consistent state across policy updates. No single component is new, yet together they form the missing foundation. On raw R2E-Gym data, without new algorithms or data work, Arctic-SWE trains Qwen3.5-4B to 62.0% pass@1 on SWE-bench Verified. This is comparable to concurrent FrogNano (61.5%), which relies on online task synthesis, after about one-sixth as many training rollouts. Building on this foundation, we further filter and refine R2E-Gym, SWE-rebench V2, and Scale-SWE. With this curated subset, the 4B model improves from 47.4%/25.0%/37.9% to 65.0%/38.3%/59.7% on SWE-bench Verified/Pro-v1/Pro-v2, and the recipe also improves Qwen3.5-9B from 56.2%/31.9%/48.8% to 65.7%/39.6%/70.2% on Verified/Pro-v1/Pro-v2. Controlled comparisons show that both curation and test strengthening improve held-out performance, although stronger tests reduce apparent training-task mastery. Arctic-SWE provides a documented starting point for studying better algorithms, data and environments for asynchronous agent RL.

---


### 192. [How Well Can LLMs Verbalize Mathematical Formulas? A Multi-Domain Evaluation](https://arxiv.org/abs/2610.24917)

**<font color=#1a73e8>作者：</font>** Peter Volbach, Tim Schlippe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) have shown strong capabilities across natural language tasks. But their ability to generate accurate written verbalizations of mathematical formulas has not been systematically evaluated. Such verbalization is important for text-to-speech systems supporting audio-based learning and visually impaired users. We evaluated five state-of-the-art LLMs across six scientific domains and constructed Read-Aloud Math, a balanced multi-domain corpus with LaTeX formulas, manually validated simple and extended transcriptions, multiple variants, textual context, domain labels, and formula complexity levels. Using multi-reference BLEU, GPT-5.2 achieved the highest score for simple transcriptions (75.9% without context, 64.9% with context), although without context it did not significantly outperform Grok 4.1 Fast or Claude Sonnet 4.5. Claude Sonnet 4.5 achieved the highest score for extended transcriptions without context (36.5%), and Grok 4.1 Fast with context (48.8%). For extended transcriptions, Statistics and Mathematics scored highest across the two context settings, while Physics scored lowest. Formula length was significantly negatively associated with BLEU for simple transcriptions without context, but not with context, whereas BLEU increased significantly with formula length for extended transcriptions in both settings. Grouping symbols were most frequently involved in transcription differences, while variable names, capitalization, and Greek letters were associated with lower BLEU scores. Overall, LLM-based formula verbalization is promising but remains sensitive to transcription type, textual context, and formula characteristics.

---


### 193. [Means-Ends Analysis Helps LLMs Plan in Continuous-State Domains](https://arxiv.org/abs/2610.24928)

**<font color=#1a73e8>作者：</font>** Jiayi Li, Carl Kingsford  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM planning research has traditionally focused on discrete-state domains, where actions form a finite, enumerable set. Existing LLM planning frameworks largely assume actions are enumerable, modeling planning as a search process over candidate actions. However, in continuous-state domains, where actions form a continuum and cannot be enumerated, this assumption breaks down. We find a remedy in Newell and Simon's Means-Ends Analysis (MEA), a general problem-solving technique rooted in heuristics from human psychology. We develop Medaka, an MEA-inspired structured prompting framework that encourages recursive goal decomposition, algebraic derivation, and per-step state tracking. To evaluate native LLM planning abilities in continuous-state domains, we develop Liquidworld, a systematic testbed on liquid mixing. On Liquidworld, Medaka can improve performance across model families, suggesting that classical means-ends analysis elicits LLM-native reasoning abilities that are helpful for continuous-state planning.

---


### 194. [What Can't Jev Decide? Probing the Limits of One-Pass Decision Models](https://arxiv.org/abs/2610.24929)

**<font color=#1a73e8>作者：</font>** Wang Yang, Xinpeng Li, Yanyan Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jev and its open replicas choose among the options a caller supplies with a single forward pass, fast enough to decide inside an agent loop. We ask what such a model cannot decide, and find a simple limit: Jev cannot make a decision that an LLM makes only by writing out intermediate steps. On a benchmark that varies one factor at a time, Jev finds and selects records without error up to 20k tokens and 64 options, but once the answer depends on two or more updates of one user, accuracy falls, to 53-80% at sixteen updates, because similar records interfere. Given a stale summary of the state, Jev follows it. On real decision items graded by how many thinking tokens a reference LLM needs, Jev answers 97.5% of the items that one forward pass of that LLM solves, but only 74% of the others. Jev also does not know its limit: its confidence flags the errors it makes itself but not those it inherits from a stale input, and neither an explicit nor a trained hand-off option catches the latter. The open models we evaluate share these limits. Checking the state such models rely on requires a model that reasons.

---


### 195. [TrustAgent-RFF: Agentic Diagnostic Planning for Reliable RF Fingerprinting under Domain Shift](https://arxiv.org/abs/2610.24930)

**<font color=#1a73e8>作者：</font>** Chuan Liu, Tianya Zhao, Xuyu Wang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Radio frequency fingerprinting (RFF) models can achieve accuracy under source domain conditions but become unreliable when the receiver, distance, collection day, or environment changes. Incorrect predictions in unseen domains may receive high softmax confidence, making confidence thresholding insufficient for trustworthy deployment. We propose TrustAgent-RFF, a prediction level reliability framework for RFF that operates with a frozen in-phase and quadrature (I/Q) classifier without target domain labels. For each device prediction, the framework acquires radio frequency evidence: counterfactual stability, prototype consistency, acquisition domain similarity, and signal quality. A source calibrated trust estimator combines these diagnostics with classifier confidence, prediction margin, and evidence availability indicators. Source derived lower tail penalties and cross module interactions reduce trust when diagnostic signals indicate weak support. A large language model (LLM) based planner adaptively selects the next diagnostic action based on evidence, trust state, action costs, and remaining budget. A deterministic source calibrated decision layer updates the prediction state as Accept, Reject, or Defer. Experiments across five RFF datasets and classifier backbones reveal an average source to target accuracy drop of 38.7% and show that many incorrect target domain predictions remain highly confident.

---


### 196. [T-MUON: Tensorizing Muon via t-SVD for Large Language Model Pre-training](https://arxiv.org/abs/2610.24938)

**<font color=#1a73e8>作者：</font>** Dongyang Li, Mingsong Yan, Zheng Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Muon has recently emerged as a strong optimizer for large language model pretraining by exploiting matrix structure through polar orthogonalization. However, it processes each parameter matrix independently, whereas recent tensor-aware extensions of Muon jointly update groups of eligible matrix parameters through matrix unfoldings. In contrast, we propose T-MUON, a t-SVD-based generalization that groups structurally related Transformer gradients into third-order tensors and defines the corresponding Muon-style update directly through the $M$-transform. We show that the exact T-MUON update is a steepest-descent direction under the $\star_M$-spectral norm and establish a convergence guarantee. Across GPT-2-style and LLaMA-style models from 51M to 1.3B parameters trained on FineWeb and FineWeb-Edu, head-wise T-MUON with the identity transform consistently achieves lower validation perplexity than AdamW, Muon, and variants using DFT, DCT, or DST transforms. These gains persist in additional experiments with longer context lengths and larger token budgets, although the preferred tensorization mode varies across settings.

---


### 197. [Over-Defense in Coding Agents Begins at Silent Forks](https://arxiv.org/abs/2610.24949)

**<font color=#1a73e8>作者：</font>** Hanjun Luo, Xuecheng Liu, Xiucheng Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models behind coding agents are post-trained with outcome rewards, and recent methods concentrate credit on the turns that decide the outcome. We find that defensive actions beyond what a task requires escape both. They begin at silent forks, the turns where every next action leads to the same outcome. Such actions leave the success rate unchanged, and frontier models take the disproportionate branch there in up to 91% of decisive actions under implicit budgets. The most direct fix, a checker in the trajectory reward, reaches these forks only through fully proportionate trajectories, leaving 74% of GRPO groups with identical rewards and behavior unchanged. This motivates a rethink of where learning signals belong, namely where behavior diverges, which a behavioral checker can locate and the outcome cannot. Our method, ForkDPO, contrasts a proportionate and a disproportionate action at the same prefix, at silent forks on both sides of the required behavior. On a test set of unseen repositories, it lowers a 4B model's disproportionate behavior from 70.3% to 58.9%, against 67.7% for DPO at randomly chosen turns, establishing behavioral divergence as a learning signal for how agents act beyond whether they finish. The code is publicly available at this https URL.

---


### 198. [ControlJEPA: Principled Trajectory Regularization via Lyapunov Tube Loss](https://arxiv.org/abs/2610.24951)

**<font color=#1a73e8>作者：</font>** Thai-Khanh Nguyen, Nhi Y. Pham, Uyen N.B. Vo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Next-token prediction leaves hidden-state trajectories largely unconstrained, while existing geometric regularizers primarily control the direction rather than the magnitude of trajectory deviations. We introduce \emph{ControlJEPA}, a trajectory regularization framework based on a discrete-time Lyapunov contraction condition from practical Input-to-State Stability theory. Its Lyapunov Tube Loss penalizes violations of this condition on a normalized, scale-invariant measure of transversal deviation. When the contraction condition holds at every step, the hidden-state trajectory remains within an explicit tube around the reference secant. In the partial-ISS regime, we bound mean transversal energy, temporal variance, and average tube width using the Lyapunov loss and contraction parameters, with horizon-independent variance bounds under uniformly bounded violations. ControlJEPA requires no architectural modifications. Across six benchmarks and six model families, it consistently improves accuracy and data efficiency over standard fine-tuning and prior trajectory regularizers. The resulting smoother transversal profile also persists empirically during inference, when the regularizer is inactive. The code is publicly available at: \url{this https URL}

---


### 199. [CasePlay: Self-Play Reinforcement Learning from Case Reports for Medical Reasoning](https://arxiv.org/abs/2610.24952)

**<font color=#1a73e8>作者：</font>** Hao Wang, Zihan Wang, Kai Wu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) is a promising way to improve the clinical reasoning abilities of large language models (LLMs), but current pipelines often rely on expert-labeled questions or costly synthetic-data generation. Meanwhile, the medical literature offers a wealth of high-quality unlabeled documents, including clinical case reports that trace the full clinical course from initial presentation to final treatment decisions. We study whether document-grounded self-play can convert these reports into effective RL training signals. We identify two challenges that limit existing self-play methods in this setting: knowledge-point fixation}, where the proposer repeatedly asks about a narrow set of salient clues in a source report, and difficulty-quality mismatch, where appropriately difficult questions may still be poorly formed or shallow, limiting their value for reasoner training. To address these challenges, we propose CasePlay, a self-play framework with two key components: (a) a Knowledge-Conditioned Proposer, which anchors question generation to case-specific knowledge points so that questions draw on a broader range of evidence from the source report; and (b) a Rubric-Judge Reasoner, which augments answer-accuracy feedback with rubric-based quality feedback on clue integration, reasoning depth, and option quality, guiding the proposer toward reasoning-intensive questions that better support reasoner training. Extensive experiments across seven medically related benchmarks demonstrate that CasePlay outperforms existing self-play baselines and improves the SFT warm-start model by 3.1 points on average, highlighted by a 6.3-point gain on LiveClin. This approach offers an effective path toward continually improving medical reasoning ability through self-play RL.

---


### 200. [MemPrice: Online Memory Allocation via Adaptive Pricing for Long-Horizon Agents](https://arxiv.org/abs/2610.24955)

**<font color=#1a73e8>作者：</font>** Yiming Zong, Shiyuan Piao, Jiashuo Jiang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon LLM agents face a fundamental allocation problem as interaction histories grow: which information to retain, how much context to devote to it, and at what granularity. Existing memory mechanisms largely focus on relevance, retrieval, or compression, leaving this allocation trade-off implicit. We introduce MemPrice, which treats active context as a shared resource and dynamically allocates it across memories and representation levels. MemPrice turns accumulated memory pressure into an adaptive price on context, encouraging detail only when its estimated retention value justifies the additional footprint. This pressure persists across memory refreshes, allowing the contents of memory to evolve while preserving long-run control over context usage. We show that irreversible compression can force linear worst-case regret against hindsight following its own memory trajectory, and introduce a same-state benchmark to evaluate allocation on MemPrice's realized memory states. MemPrice enforces the hard context budget at every round and regulates long-run occupancy through adaptive pricing, without prior knowledge of the interaction horizon. Under priced-frontier regularity, its average allocation-regret bound against this benchmark vanishes when accumulated estimation error is sublinear. We evaluate the framework under matched memory budgets on LongMemEval, LoCoMo, AppWorld, and WebShop across three foundation models, spanning both query-blind memory construction and goal-directed agent context management.

---


> [!TIP]
> 当前位于：**151-200**（第 4/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-200** | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-548](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
