# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

---

### 51. [ASTRA - Agentic System for Ticket Resolution and Analysis](https://arxiv.org/abs/2608.28790)

**<font color=#1a73e8>作者：</font>** Shashidhar Reddy Javaji, Mohamed Trabelsi, Jin Cao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Technical operations teams resolve large volumes of incidents by synthesizing fragmented evidence from ticket text, historical cases, system logs, and technical documentation. Existing automation often relies on monolithic generation without explicit evidence modeling or provenance, making outputs difficult to verify when critical signals are sparse across sources. We propose ASTRA, an agentic system for ticket resolution in which a central orchestrator coordinates three specialist information-gathering agents and drives a judge-orchestrator refinement loop to produce evidence-backed troubleshooting reports. TicketSimilarityAgent retrieves relevant historical precedents through dense retrieval and LLM reranking; LogAgent distills hundreds of thousands of log lines into structured, quote-grounded findings using deterministic filtering and constrained LLM analysis; and DomainKnowledgeAgent retrieves relevant technical knowledge via the Model Context Protocol (MCP). Their outputs are transformed into a claim-evidence representation linking each claim to a verbatim source passage, assigning a support level, and preventing cross-attribution. A JudgeAgent scores the report on five criteria, while the OrchestratorAgent converts low scores into targeted follow-up queries for bounded iterative refinement. Evaluated on 987 real-world telecom fault tickets across seven product lines, ASTRA achieves a mean quality score of 4.13/5.0, with 59.9% of reports identifying the fault area at the component-family level or better. Relevance and Clarity scores are 4.88 and 4.94, respectively, while fabricated technical details remain below 3% of error cases. Stratification by fault type reveals that hardware faults remain substantially harder than software or configuration faults (Cohen's d=0.80), pointing to a fundamental limitation of text-based evidence channels for hardware fault diagnosis.

---


### 52. [Breaking Darknet CAPTCHAs with general purpose LLM](https://arxiv.org/abs/2608.28794)

**<font color=#1a73e8>作者：</font>** Benjamin Fehrensen, Jens Hubler  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Our work evaluates the effectiveness of automated methods for solving CAPTCHA challenges commonly encountered in darknet environments. These CAPTCHAs are typically designed to operate without JavaScript, resulting in distinct characteristics compared to mainstream CAPTCHA systems. Our study considers three representative challenge types: open-circle localization, rotation-based alignment, and object-selection CAPTCHAs.
The experiments reveal a systematic limitation of contemporary MLLMs: while they are generally capable of identifying relevant visual structures, they frequently struggle with precise spatial localization and geometric transformations. These deficiencies can be mitigated either through task reformulation or by augmenting the models with specialized image processing tools.
These deficiencies can be mitigated by task reformulation or by equipping the model with specialized image-processing tools. We therefore propose a hybrid framework in which an MLLM serves as a high-level reasoning and orchestration layer while delegating geometric computations to deterministic algorithms via the Model Context Protocol (MCP). The resulting system achieves success rates above 90% across all evaluated CAPTCHA types and demonstrates that combining the complementary strengths of MLLMs and classical computer vision yields a more accurate and efficient solver than either approach alone.

---


### 53. [Enhancing SAE-based Steering via Neighbor Integrated Feature Selection](https://arxiv.org/abs/2608.28806)

**<font color=#1a73e8>作者：</font>** Yutian Liu, Xu Wang, Difan Zou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) disentangle model activations into interpretable features and are widely used for steering large language models. Most existing SAE-based steering methods select features by applying a top- filter based on statistical scores, assuming that higher-scoring features yield stronger steering effects. In this paper, we show that this assumption is often invalid, leading to suboptimal feature selection. Our analysis reveals that effective steering features may be distributed among representationally adjacent, semantically similar groups induced by feature splitting in SAEs. Within such groups, features may exhibit disparate statistical scores despite having comparable steering influence, causing score-based selection to overlook important features. Based on these observations, we propose \textsc{Neighbor Integrated Feature Selection} (\textsc{NIFS}), a plug-and-play strategy that leverages representation similarity to improve feature selection for steering. We evaluate \textsc{NIFS} across multiple SAE-based steering methods and tasks, and demonstrate consistent performance gains over conventional top-$k$ selection.

---


### 54. [Capability-Stratified Degradation in Ternary Language Models](https://arxiv.org/abs/2608.28809)

**<font color=#1a73e8>作者：</font>** Anirudh Malik, M Sparsh Mehra, Poojith Devan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Extreme low-bit inference offers a route toward smaller models and constrained deployment. Ternary language models restrict weights to $\{-1,0,+1\}$, approaching the limit of $\log_2 3 \approx 1.585$ bits/weight. The practical question for a pretrained model is not simply whether weights can be quantised but which capabilities survive and whether it remains useful for adaptation. We explore this by converting Qwen3.5-0.8B (752M parameters) to ternary weights using 72.4M tokens of quantisation-aware training (QAT). The resulting model, Cloe, is evaluated across 29 benchmarks, representation diagnostics, and downstream fine-tuning. The evidence shows non-uniform degradation. A linear probe recovers 43.76% of MMLU answers from the full-precision teacher's representations but only 26.19% from Cloe (near chance), indicating specialist factual information is lost. However, Cloe retains measurable performance on ten tasks, averaging 77.1% of teacher performance. Crucially, fine-tuning raises Cloe to 89.8% on SST-2 (95.6% of the matched teacher) and reaches 79.4% teacher retention on XSum. We attribute degradation to a combination of quantisation-induced information loss and incomplete recovery due to the limited QAT budget. We also highlight an evaluation pitfall: standard answer-letter scoring failed (Cloe emitted "A" on 98.6% of MMLU questions), necessitating continuation scoring. Ultimately, ternary conversion is unsuitable as a drop-in general replacement yet remains valuable as a compact substrate for task-specific models.

---


### 55. [Visible but Not Yet Curatable: Characterizing the Curatability of Compact and Derived Open LLM Artifacts](https://arxiv.org/abs/2608.28819)

**<font color=#1a73e8>作者：</font>** Yiyi Lu, Yilai Qian, Yucheng Jin  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Open Large Language Model (LLM) research increasingly produces compact and derived artifacts, such as adapters, quantized checkpoints, merged models, and distilled variants, that are distributed across papers, model hubs, model cards, code repositories, and release statements. Although these artifacts are publicly visible, digital libraries often lack sufficient evidence to identify, preserve, and cite them as coherent scholarly objects. We introduce a framework that conceptualizes curatability as a record-level property of distributed scholarly records and operationalizes it through four evidence dimensions: artifact identity, scholarly linkage, upstream evidence, and release assets. Guided by this framework, we conduct the first collection-scale characterization of open LLM curatability using a May 2026 snapshot of 191,375 public Hugging Face repositories and a core corpus of 2,214 scholarly papers. Our results reveal a pronounced visibility-to-curatability funnel. While 90.7% of paper records contain at least one useful curation signal, only 18.1% combine usable upstream evidence with concrete release evidence, and only 6.1% provide sufficiently coordinated evidence to support high-curatability records. Based on these findings, we derive a minimal seven-field curatable record and complementary responsibilities for model hubs, scholarly indexes, and digital libraries, providing practical guidance for improving the preservation and bibliographic control of open LLM artifacts.

---


### 56. [Discovering Machine Correlates of Consciousness](https://arxiv.org/abs/2608.28824)

**<font color=#1a73e8>作者：</font>** Romain Salvi, Ouri Wolfson  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Currently, in biological systems Neural Correlates of Consciousness (NCCs) are characterized in terms of EEG and FMRI signals. Unfortunately, this characterization prevents the transferability of the NCCs concept to machines. Such transferability would be useful in order to investigate AI consciousness. In this paper we provide an alternate characterization that is transferable, and enables the analogous definition of Machine Correlates of Consciousness (MCCs). Specifically, we propose that NCCs (MCCs) are substrate-level signals that are not under human (AI agent) control, and that are reliably modulated by emotions.
This paper presents the first empirical investigation of MCCs. Specifically, we present the results of experiments conducted with two LLMs, Llama-2 7B and Llama-3.1 70B parameters. In these LLMs we collect hardware anomaly traces that are substrate-level indicator-sequences. And we show that after controlling for confounding factors, these are modulated differently by emotional and neutral computations. And this difference is statistically significant for the larger Llama-3.1 70B, but not for the smaller Llama-2 7B. The results constitute initial empirical evidence that MCCs are present in the Llama-3.1 70B configuration. And they are consistent with the hypothesis that consciousness probability and degree increase with the LLM sophistication.
Independently of consciousness, MCCs can also be used for detection of emotions in AI agents.

---


### 57. [Evaluating the Hidden Costs of Personalization in Large Language Models](https://arxiv.org/abs/2608.28833)

**<font color=#1a73e8>作者：</font>** Yumeng Wang, Yuchen Wu, Cheng Qian 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> While Large language models (LLMs) incorporate user personalization signals to improve usability and helpfulness, they increasingly shift from providing balanced, informative responses toward optimizing for user satisfaction when conditioned on personal context such as conversation history, inferred preferences, and user profiles. Specifically, we identify three emerging risks: (1) irrelevant personalization, where models reference personal information in unnecessary contexts; (2) preference narrowing, where models reinforce informational echo chambers; and (3) sycophantic bias, where models agree excessively with user opinions. As a result, models may reference personal information in contexts where it is unnecessary, inadvertently collapse response diversity, or agree excessively with user opinions. Despite the growing use of personalization in AI assistants, there has been limited systematic evaluation of its potential side effects. To bridge this gap, we propose PRISK, a dynamic evaluation framework with automated data generation and tailored metrics that uncovers systematic limitations in current LLM personalization and how personalized information shapes its responses. Our empirical analysis across 13 LLMs demonstrates the presence of user profiles and retrieved memories consistently exacerbates biases, resulting in an average drop of 45.9% in irrelevant personalization, 41.7% in preference narrowing and 61.7% in sycophantic bias.

---


### 58. [Delegating Before Learning: Where Generative AI Sits in Students' Professional Communication](https://arxiv.org/abs/2608.28837)

**<font color=#1a73e8>作者：</font>** Jared Ren, Soobin Cho  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We conducted an interview study with twelve students on their use of generative AI in academic communication. Students delegated professional messages to AI most where the pressure to sound professional is highest: email to instructors and administrators. AI involvement ranged from correcting the writer's own text to working out and writing the message outright, and students checked AI-written text against two criteria: whether it looks like AI and whether it sounds like them. Building on these findings, we model the AI-mediated process of writing a student--instructor email at the highest level of involvement we observed, and compare it with an unaided model of writing the same messages, built from participants' accounts and a classic model of the writing process. Three differences emerge: the learning loop that builds writing skill is removed, the message is no longer written for its specific recipient, and the confidence a successful exchange returns goes to using the system rather than to the writer's own ability. From these differences we derive two risks, that individual capacities never form and that authenticity and trust in communication become work. Design can respond to both but is unlikely to be enough, so the risks also need research and policy attention.

---


### 59. [A rigor-matched audit of periodic-step layer skipping for efficient llm inference: conflayers versus swift, with a supplemental analysis of trained routing alternatives](https://arxiv.org/abs/2608.28846)

**<font color=#1a73e8>作者：</font>** Prateek Kumar Sikdar, Arpan Ghosh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Layer-skipping methods for efficient LLM inference decide, at some granularity, which transformer layers to execute for a given input. We present a rigor-matched, three-seed audit of two periodic-step, search-based methods that make this decision online at inference time and re-evaluate it every few generation steps: a confidence-gated early-exit baseline (ConfLayers) and genuine self-speculative decoding (SWIFT, Xia et al. 2024), together with vanilla autoregressive decoding, across two model scales (Qwen2.5-0.5B and Qwen2.5-1.5B) and two tasks (GSM8K reasoning and CNN/DailyMail summarization). SWIFT is the strongest method on accuracy in three of four cells; ConfLayers is dominated everywhere, with particularly large deficits on GSM8K at 1.5B. Once online-search overhead is separated from pure inference cost, SWIFT's true inference speed is faster than ConfLayers's in all four cells (5-21%), reversing the naive wall-clock ranking in three of them. ConfLayers's search overhead is small and stable (1-2% of cost), while SWIFT's is larger and more variable (up to 28.7%). We additionally examine two trained-routing methods, LayerRoute (Sikdar, 2026) and LayerDrop (Fan et al. 2020), as a supplemental analysis because they operate at coarser decision granularities. Under a verified protocol with genuine per-input gating, a genuine full-model baseline, and genuine inference-time compute skipping, both show modest speedups (1.08-1.33x) but accuracy well below the periodic-step methods, including a near-total collapse for LayerRoute on GSM8K at 1.5B (0.003 mean exact-match across three seeds). We release the full audit protocol as a template for rigor-matched efficiency comparisons.

---


### 60. [The Halt Vector: Internalizing a Causal Steering Intervention for Efficient Reasoning](https://arxiv.org/abs/2608.28859)

**<font color=#1a73e8>作者：</font>** Dylan Jayabahu, Tinuade Adeleke  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reasoning models do not stop when they know the answer. On DeepSeek-R1-Distill-Qwen-7B the chain of thought runs about twice as long as the model's own answer probability takes to settle, and how much of that excess is removable varies from problem to problem, so a global length penalty cannot take it out. We take it out by internalizing a causal interpretability finding into the weights. The mechanism is a halt vector: a difference-of-means direction at layer 18 of this model whose steering strength controls how long it thinks, while a replicated value axis does nothing. Installing that intervention in the weights is harder than it looks. Maximizing the scalar projection onto the direction corrupts the off-axis dimensions a frozen downstream reader depends on, and generation gets longer instead of shorter; what works is reconstructing the whole steered activation with those dimensions pinned to their natural values. Fit from 24 problems and no reinforcement learning, the halt removes about a quarter of the thinking at held accuracy across five unseen benchmarks, and the cut tracks each problem's own removable slack at 0.70. It also closes a non-termination pathology that grows with difficulty and that a decoding-time confidence hook makes worse. We do not claim to beat a well-tuned length penalty or decoding-time early exit on the raw trade-off; the contribution is how the halt is obtained.

---


### 61. [Latent-Space Intervention for Cross-Lingual Factual Consistency: Consistency Improvements without Accuracy Drops](https://arxiv.org/abs/2608.28860)

**<font color=#1a73e8>作者：</font>** Faeze Ghorbanpour, Constanza Fierro, Alexander Fraser 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) often answer the same factual question differently across languages. We study whether cross-lingual latent-space intervention can reduce this inconsistency. We train layer-specific autoencoders on parallel multilingual representations and apply inference-time corrections to factual QA prompts. We find that latent intervention improves geometric alignment between languages, and that this improvement translates into consistent gains in cross-lingual consistency with English across both open-ended and multiple-choice QA formats, without degrading factual accuracy. In open-ended QA, Spearman's rank correlation between English and non-English languages improves substantially, with gains of 0.16 for English-Arabic and 0.20 for English-Russian pairs. In multiple-choice QA, answer agreement with English improves consistently across both KLAR and mParaRel. Ablations show that AE reconstruction yields consistent gains at no accuracy cost, while PCA projection contributes marginally, and mean-shift produces substantially larger consistency gains in open-ended QA at the cost of some accuracy.

---


### 62. [No Detectable Change in Side-Level WER from Prompt-Level Context: A Preregistered Ablation on a Production Oral-History Corpus](https://arxiv.org/abs/2608.28875)

**<font color=#1a73e8>作者：</font>** Theodore O. Cochran, Stephanie Dodson, Keith Nore  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Supplying context at inference time to a large multimodal model is an inexpensive lever for adapting speech transcription to a domain, and earlier results on smaller models reported large gains. This work tested that mechanism where it ships, in the prompt-conditioning layer of a production oral-history transcription tool, on a sample from its own production corpus. Full prompt-level context did not detectably change side-level word error rate (WER), and none of the four preregistered hypotheses was supported. The design was a within-item paired ablation, preregistered with the analysis code frozen by hash before the confirmatory batch was scored; two disclosed gpt-4o pilot sides had been scored earlier, during scorer development. Nineteen cassette sides, about 10.6 hours of degraded 1970s-80s interview audio, were reprocessed through the production code path under three prompt arms, crossed with two deployed commercial configurations, gpt-4o-transcribe and gemini-2.5-flash, and scored against operator-corrected verbatim references. For gpt-4o-transcribe the median paired difference between the full-context and no-context arms was +0.6 WER points, with a side-resampled interval of [-1.1, +1.0]; the Gemini estimates were too unstable to support a comparable negative inference. A post-hoc rerun found run-to-run pipeline variability larger than the confirmatory differences, so effects of that size cannot be resolved from one transcription per cell. An implementation audit verified the manipulation was live, and sequence-alignment analysis found a small improvement on complete context-listed phrases, too small to materially change side-level WER, and for Gemini coexisting with worsened unlisted-token error. Evaluating context mechanisms therefore requires sequence-aligned term-level, insertion, and speaker-label measures alongside aggregate accuracy.

---


### 63. [MineCEraft: Evaluating Language Models as Construction Engineers in the World of Minecraft](https://arxiv.org/abs/2608.28884)

**<font color=#1a73e8>作者：</font>** Sewoong Lee, Risham Sidhu, Julia Hockenmaier 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce MineCEraft (Minecraft Construction Engineering Benchmark, pronounced mine-see-ee-raft), an easy-to-use, open-source benchmark designed to systematically evaluate the reliability and limitations of LLMs for construction tasks in Minecraft. The MineCEraft benchmark comprises 723 domain-expert hand-crafted natural-language instructions with programmatically verifiable evaluation, spanning 17 distinct task categories, providing a safe and controllable experimental environment for assessing LLMs' ability to perform realistic construction engineering tasks. With this benchmark, we conduct an in-depth evaluation of state-of-the-art LLMs and perform a detailed error analysis, revealing key failure modes and practical challenges in applying LLMs to construction engineering tasks.

---


### 64. [Structured State Reconciliation for Human-AI Task Handover](https://arxiv.org/abs/2608.28907)

**<font color=#1a73e8>作者：</font>** Kayleigh Bishop, Maria P. Stull, Breanne Crockett 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Task handover requires communicating enough current state for a successor to resume work, yet the relevant information is often divided between system records and human observations. System records can be precise and timestamped but only partially observe the task, while human reports capture intent and task knowledge that no log contains but are vulnerable to omission and memory error. We present a provenance-aware pipeline that converts task telemetry and human-authored reports into a shared typed task-state representation, aligns and reconciles their facts, detects conflicts, and generates structured handover reports. We evaluate the approach on 13 paired task states collected in a controlled spatial multitask environment, using task-grounded metrics that estimate the state-reconstruction cost a report would spare a hypothetical recipient and the misinformation burden it would impose. Reconciling both sources preserved greater estimated task-state utility than either the user report or telemetry alone. Relative to a direct end-to-end LLM given the same inputs, structured reconciliation maintained comparable estimated utility while incurring substantially less misinformation, and task-aware rendering retained utility more efficiently (per token) than exhaustive rendering. An exploratory content analysis further shows that human reports contain substantial strategic knowledge that lies outside state-focused metrics. These results support provenance-aware state reconciliation as a design pattern for safer AI-assisted handover.

---


### 65. [SemKV: Semantic Mixed-Precision KV Cache Quantization Guided by the Quality Cliff for Long-Context LLM Inference](https://arxiv.org/abs/2608.28911)

**<font color=#1a73e8>作者：</font>** Daeha Lee, Do-Hyung Kim, Jae-Hong Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The key-value (KV) cache is the dominant memory bottleneck of long-context large language model (LLM) inference, growing linearly with context length. We show that uniform KV quantization on a fractional-bit grid does not degrade gracefully: under a prespecified multi-seed statistical protocol, Llama-3.1-8B-Instruct with an affine quantizer is statistically indistinguishable from FP16 KV down to 2.322 code bits/value and collapses at 2.0 bits - a quality cliff in (2.0, 2.322] that reappears in generation-time quantization and multi-turn dialogue and transfers to Mistral-7B. The cliff reframes importance-aware mixed precision: above it, eight model-internal importance indicators are statistically interchangeable, so the benefit of mixing is grid interpolation, reaching average precisions uniform quantization cannot realize. SemKV preserves every token, ranks tokens by a model-internal score, and assigns two adjacent above-cliff precisions, achieving a measured 6.0x storage reduction with no statistically detectable quality difference from full KV (n=900, three seeds), and outperforming FP16 token pruning granted a 1.5x larger memory budget. Replacing the affine base with a distortion-optimized quantizer (TurboQuant-MSE) lowers the cliff in every protocol tested, raising the no-detectable-loss operating point to 7.9x. The recipe: measure the cliff for the target deployment setting, then interpolate above it.

---


### 66. [Causal Interventions Reveal Typologically Organized Syntactic Mechanisms in Multilingual Language Models](https://arxiv.org/abs/2608.28924)

**<font color=#1a73e8>作者：</font>** Sasha Boguraev, Toshiki Nakai, Kyle Mahowald 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Linguistic theory has long recognized cross-linguistic syntactic regularities, leading to claims that these similar structures are processed by similar mechanisms. However, this hypothesis has been difficult to test empirically due to our lack of fine-grained, manipulable access of human processing mechanisms. In this work, we take advantage of techniques from mechanistic interpretability to study such a question in multilingual LMs. We first isolate language-internal mechanisms before attempting to transfer them cross-lingually. Across four models and three well-studied constructions (subject--verb number agreement, anaphoric pronoun gender agreement, and filler--gap object extraction) we find consistent cross-lingual mechanism transfer. We further find transfer to be graded, with more transfer between more typologically similar languages. We believe our work provides novel hypotheses about cross-linguistic syntactic structures and multilingual processing, and more broadly shows how the study of language models can help inform linguistic theory.

---


### 67. [The Hallucination Signal Is a Mean Shift: Why Simple Probes Suffice](https://arxiv.org/abs/2608.28930)

**<font color=#1a73e8>作者：</font>** Jungseob Lee, Jaehyung Seo, Heuiseok Lim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hidden-state probes effectively detect LLM hallucinations, but the geometry of the signal remains poorly characterized, driving increasingly complex probe architectures. Across three 7B-scale models and three datasets in a paired-example paradigm, we find the signal overwhelmingly dominated by a single mean-shift component, and removing this direction collapses detection to chance. Shrinkage linear discriminant analysis closes about 73% of the gap between 1D and full-dimensional classifiers, so apparent architectural complexity largely reflects high-dimensional covariance estimation difficulty rather than exploitable non-linearity. A simple L2-regularized logistic regression (0.952 AUROC) bounds or outperforms twelve controlled architectural alternatives, and our multi-layer aggregation exceeds CLAP cross-layer attention probing under matched paradigm. Because the signal spans a contiguous layer band, LayerMix aggregates it to match oracle-layer performance without oracle access. Our claims characterize the geometry within the controlled paired-example paradigm. Our code is available at this https URL.

---


### 68. [VocalAffectBench: Evaluating Vocal Emotion Recognition in AI Audio Models](https://arxiv.org/abs/2608.28932)

**<font color=#1a73e8>作者：</font>** Models Luc Debaupte, Tyler Baumgartner, Brandon Tai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Voice products increasingly need affective cues that are present in speech but absent from transcripts. We introduce VocalAffectBench, a public, test-only benchmark for evaluating whether AI audio models can identify expressed vocal emotion from raw audio. The benchmark contains 273 human-recorded English WAV clips from 51 speaker accounts totaling 1.95 hours across seven labels: angry, disgusted, fearful, happy, neutral, sad, and surprised, with 39 clips per class. All baselines are evaluated from audio alone, without transcripts or contextual metadata. Across six released baselines, average accuracy is 35.5%. The strongest baseline, gemini_3_5_flash, reaches 46.5% on the seven-way task, above the 14.3% random baseline but far from robust emotion recognition. A secondary valence-bucket analysis maps labels into positive, neutral, and negative classes, excluding surprised because its valence is ambiguous. Aggregate accuracy under this coarser view is 50.9%. Performance is highly uneven across classes. By recall, neutral is identified most reliably at 75.6% averaged across baselines, while surprised and fearful reach only 10.7% and 15.4%, respectively. These results show that the evaluated baselines can extract some affective signal from speech, but discrete expressed-emotion recognition remains fragile, especially for non-neutral emotions that are often most important in voice agent workflows.

---


### 69. [Oculi: A Conversational Agentic Platform for Automated Credit Risk Analysis](https://arxiv.org/abs/2608.28944)

**<font color=#1a73e8>作者：</font>** Vennise Ho, Kristian Diana, Sandy Mourad 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Credit risk analysis in financial institutions traditionally requires analysts to manually write SQL queries, run statistical computations, and build visualization dashboards. This is a time-consuming workflow that limits exploration to familiar segments. We introduce \textbf{Oculi}, a conversational platform that transforms natural language questions into comprehensive credit risk analyses, complete with data queries, statistical testing, and interactive visualizations. Oculi employs a three-layer architecture that separates reasoning (LLM-powered agent), execution (Model Context Protocol tool servers), and presentation (agentic UI), enabling analysts to discover high-risk portfolio segments. Within Oculi, a new segment discovery pipeline is proposed that combines deterministic statistical methods with LLM-guided feature selection, leveraging LLM semantic domain knowledge alongside data-driven metrics to identify meaningful, actionable portfolio segments. Evaluated on a mortgage portfolio with 200+ features, Oculi demonstrates effectiveness in discovering material risk segments previously intractable through manual exploration, reducing time-to-insight significantly while maintaining auditability and statistical rigor.

---


### 70. [The Web-CLI: Verifiable Privacy for Tools, Models, and Inference Engines in the Browser](https://arxiv.org/abs/2608.28950)

**<font color=#1a73e8>作者：</font>** Tejaswi Gowda  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We introduce the Web-CLI, a novel application architecture deploying powerful computational capabilities (command-line tools compiled to WebAssembly, models run through client-side inference runtimes, and GPU-accelerated engines) as zero-install, offline-capable browser applications that preserve full underlying capability. Unlike web-based alternatives that require server-side processing and expose user data to third parties, Web-CLI applications execute entirely on the client, providing a verifiable privacy guarantee by architecture rather than policy. We define the pattern and its four properties: fidelity, progressive disclosure, offline-first, and zero egress. We present four reference implementations across distinct domains: ffmpeg-webCLI, a browser-based video editor built on FFmpeg; whisper-webCLI, speech transcription via this http URL; chat-webCLI, WebLLM-based language model inference; and 3mf-webCLI, a deterministic tool segmenting 3D models into multi-material files for physical 3D printing. Together they demonstrate that the pattern generalizes across deterministic media processing, neural speech recognition, LLM inference, and geometry processing with a physical output, and we outline how it extends to AI-native interfaces in which a local language model becomes the command surface itself. We further report early, anecdotal signs of independent reuse by third-party tools, suggesting the pattern generalizes beyond its reference implementations. We evaluate the primary implementation against native FFmpeg on performance and feature parity, and argue that progressive disclosure lowers the barrier for non-technical users. We argue that for applications processing sensitive user data (medical, legal, journalistic, or personal), the Web-CLI should be the default architecture, as it makes data locality an independently verifiable technical property rather than a policy promise.

---


### 71. [CoVA-SFT: A Large-Scale Dataset for Chain of Visual Abstractions](https://arxiv.org/abs/2608.28958)

**<font color=#1a73e8>作者：</font>** Tsung-Han Wu, Heekyung Lee, Anya Ji 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning has dramatically improved large language models (LLMs) by allowing them to decompose problems into intermediate steps. While CoT is widely effective for linguistic tasks, text-only CoT forces models to serialize visual problems into awkward prose. Although architectural solutions exist to process visual inputs, the community lacks a massive, multi-step, self-corrected dataset to teach models how to build and maintain internal visual workspaces when solving purely textual reasoning problems. To address this limitation, we introduce CoVA-SFT, a highly structured corpus of 51.9K samples containing over 222K multimodal reasoning steps across 5 distinct layout families and 17 complex tasks, and CoVA-Bench, a companion benchmark of 1,700 held-out test samples spanning the same tasks for reproducible evaluation. By providing explicit rationale formulations, agentic renderings, and verification loops, CoVA-SFT teaches multimodal language models to interleave text and visual abstractions. We validate the dataset by demonstrating that models fine-tuned on CoVA-SFT outperform all interleaved CoT baselines by more than 2x on average on CoVA-Bench, though they still fall short of strong text-only CoT baselines, highlighting open challenges for future work.

---


### 72. [Efficient GPU Retrieval for Semantic Search](https://arxiv.org/abs/2608.28968)

**<font color=#1a73e8>作者：</font>** Dhritiman Das, Chujie Zheng, Ronak Kaoshik 等 21 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Semantic Search on LinkedIn must retrieve relevant profiles from a corpus of hundreds of millions in response to natural-language queries such as "a fintech founder in Berlin who worked in payments." The deployed relevance policy is bottleneck-oriented: every active non-negotiable facet must be satisfied, and a pre-existing LLM Graded Relevance (GR) judge operationalizes this through a fixed min/median aggregation over facet grades. Cosine similarity instead averages evidence, letting a strong match on one facet mask failure on another, capping the recall of the first-stage (L0) retriever.
We present a policy-aligned retrieval framework: embeddings are partitioned into eight category-supervised segments whose scores follow the same min/median rule at serving time; for multi-vector retrieval, this segment score is computed independently per tagged document slot and maximized across slots. A lightweight single-slot Stage-1 scorer generates high-recall candidates, while scale-invariant relative-norm gating keeps category activation consistent across training, evaluation, and serving. On 21K held-out queries, this representation improves offline relevance over a matched-capacity baseline, with gains broadly distributed across facet combinations.
We serve this framework with a two-stage GPU architecture: an FP8 coarse ranker scores the full corpus, increasing per-shard capacity by 71% and Stage-1 matmul throughput by 36%, then an FP16 stage exactly re-ranks an oversampled candidate set, recovering 99.6-99.8% of full-FP16 recall at over 500 QPS per shard replica. In a member-randomized A/B test, exploratory-query Precision@10 under the unchanged GR judge rises from 63.7% to 79.0% and navigational Precision@1 from 65.5% to 74.7%, with a blinded human evaluation independently confirming the Precision@10 gain.

---


### 73. [Selective Forgetting: A Graph-Based Memory Framework for Long-Term LLM Agents](https://arxiv.org/abs/2608.28978)

**<font color=#1a73e8>作者：</font>** Theo Rusu, Sourena Khanzadeh, Manar Alalfi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Knowledge graphs have been proposed as a structured alternative to flat retrieval-augmented generation for long-term agent memory, on the assumption that representing conversations as entities and relations improves recall. We evaluate that assumption directly. Our framework extracts each conversational turn into typed nodes and attributed edges, answers questions from a two-hop subgraph, and periodically prunes nodes that score low on a weighted combination of recency, access frequency, degree centrality, and age. On LongMemEval, the graph does not outperform a flat vector baseline at a matched candidate-generation budget of five retrieval roots: token F1 is $0.417$ against $0.468$, and a paired bootstrap over 500 questions gives
$\Delta = -0.050$ (95\% CI $[-0.085, -0.016]$). The gap is widest on questions that require recalling a specific prior assistant turn, where judged correctness falls from $0.911$ to $0.607$, suggesting that decomposing a turn into entities discards the surface form these questions depend on. The forgetting module is more successful. Applied once to a persistent 27{,}021-node graph, it removes 9.8\% of nodes and 9.5\% of stored bytes; token F1 is unchanged ($+0.001$, 95\% CI $[-0.015, +0.016]$) and judged correctness falls by $1.6$ points, with the 95\% interval bounding any loss at $3.8$ points ($[-0.038, +0.006]$). Because our extractor is a single small model evaluated on one benchmark, these results characterise this extraction-based pipeline rather than graph-structured memory in general. Code: this https URL

---


### 74. [Detecting and Guiding LLM-Generated Korean Poetry with Interpretable Form-level Features](https://arxiv.org/abs/2608.28986)

**<font color=#1a73e8>作者：</font>** Keunhyeung Park, Seunguk Yu, YoungBin Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs often struggle with modern Korean poetry, producing outputs that resemble "line-broken prose." We address two coupled tasks: detecting whether a Korean poem is human- or LLM-authored, and guiding LLMs to generate poetry closer in form to human writing. We quantify the human-LLM gap along four form-level linguistic dimensions: output length (Volume), the diversity and connective use of line-final forms (Structure Variation), the irregularity of line lengths (Rhythmic Irregularity), and adherence to standard orthography (Normative Adherence). We operationalize these dimensions as five interpretable features. For detection, a logistic regression classifier over these five features attains an average AUC-ROC of 83.60 in zero-shot out-of-distribution detection across seven unseen LLMs, versus 75.84 for the strongest baseline in our comparison, KatFishNet, an absolute gain of 7.76 AUC points and a 10.23% relative improvement; one generator-specific punctuation pattern outside our taxonomy remains a boundary case. For generation, expert evaluation on GPT-5.2 prefers feature-guided poems over the unconstrained baseline, and analyses across GPT-5.2 and Gemini-3 show that targeted length, rhythm, and ending statistics move toward the human distribution. These results suggest that interpretable, language-specific features can bridge the diagnosis and guidance of LLM-generated poetry.

---


### 75. [Using LLMs to Mimic the Conversational Dynamics of Reddit Communities](https://arxiv.org/abs/2608.28989)

**<font color=#1a73e8>作者：</font>** Vedaant Jain, Yoshee Jain, Ishq Gupta 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Online communities face a constant battle against toxicity and misinformation. While human moderators struggle to keep pace with the volume of content, LLMs offer a promising solution for automatically generating constructive responses and shaping online interactions. This paper preliminarily investigates if LLMs can mimic the communication styles of Reddit users using their comment history as context. We evaluate two prompting approaches: predicting a target comment and filling in masked comments. We find that LLMs outperform expectations at replicating comment structure and formality, but struggle to accurately capture nuanced emotions, e.g. understating joy and overstating anger. These findings highlight a promising direction for LLMs in guiding online conversations towards prosociality influencing emergent communication patterns and norms within the community. The results of our study inspire future work with more rigorous methods of evaluation to explore the LLMs' effectiveness across diverse online communities to better understand their broader societal impact.

---


### 76. [Agentic AI uncovers conserved cross-tissue protein co-abundance programs inaccessible to single-dataset analysis](https://arxiv.org/abs/2608.28990)

**<font color=#1a73e8>作者：</font>** Runyu Guan, Dehao Wu, Qiqi Xie 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein co-abundance clusters preserved across tissues can reveal shared disease mechanisms and candidate therapeutic targets, particularly when proteins implicated in organ-confined diseases converge in peripheral or accessible tissues. However, previous cross-tissue studies have focused on biologically pre-selected tissue pairs, leaving most possible combinations and non-obvious relationships unexplored. We present an LLM-agent framework for large-scale, evidence-grounded comparison of tissue-specific protein co-abundance networks. The framework constructs tissue networks, derives pairwise consensus clusters, and integrates evidence from expression atlases, protein interaction and complex databases, pathway annotations, disease catalogues, and literature. Applied to all 820 pairwise combinations of 41 human tissues and fluids, it identified 1,833 conserved co-abundance clusters across 406 tissue pairs. Colon, synovial fluid, blood, cerebrospinal fluid, and bone marrow were the most broadly connected tissues, while the most cluster-rich pairs were dominated by bone marrow. The analysis also highlighted non-obvious relationships: skin-bone marrow exceeded the anatomically adjacent bone-bone marrow pair, while colon-breast contained cancer-relevant clusters involving extracellular-matrix remodeling, lipid metabolism, and immune modulation. Cluster-level analyses generated further mechanistic hypotheses, including a brain-gut extracellular-vesicle/redox/serotonin-cofactor axis and a liver-bone marrow stress-response axis involving genes linked to white matter disease. These results provide a global, comparable landscape of conserved protein co-abundance and a hypothesis-generating resource for mechanistic and therapeutic exploration. Code and data are available at this https URL.

---


### 77. [Towards Fully Automated Medical Imaging Code Generation via Validation-based Context Engineering](https://arxiv.org/abs/2608.29016)

**<font color=#1a73e8>作者：</font>** Zixiao Zhao, Jing Sun, Zhe Hou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have demonstrated considerable promise in program generation for small-scale and conventional application development; however, they remain limited when applied to complex, domain-specific tasks such as medical image processing. General-purpose models lack explicit domain knowledge and robust validation mechanisms to ensure correctness, often requiring substantial human intervention to produce reliable processing pipelines. To address these limitations, we propose AutoMedImg, a multi-agent framework for fully automated medical image processing code generation. AutoMedImg orchestrates specialised agents across two phases: a Planning Phase that performs dataset analysis and architecture design with semantic and formal verification, and a Coding Phase that generates modules in parallel with static checking, execution testing, and assembly validation. This multi-stage validation mitigates error propagation throughout generation, while comprehensive auto-context engineering combining domain-specific knowledge bases, shared memory, and validation feedback automates context construction without manual prompting. A cross-project adaptive pipeline synthesis mechanism further accumulates validated pipelines and retrieves proven components for new tasks based on project similarity, enhancing generation efficiency through cross-project learning. Extensive evaluation across six diverse and well-established medical imaging datasets with five backbone LLMs demonstrates that AutoMedImg achieves zero human intervention, with Dice scores of up to 0.90 for segmentation tasks and 99% accuracy for classification.

---


### 78. [Hybrid Semantic Context-Enhanced Ensemble Learning for Wind Power Ramp-Event Forecasting and Uncertainty-Aware Evaluation](https://arxiv.org/abs/2608.29024)

**<font color=#1a73e8>作者：</font>** Momina Liaqat Ali, Muhammad Abid, Muhammad Abdullah 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Wind power ramp events which are sudden, large swings in turbine output over short windows are difficult to estimate, and standard models often miss them. Hybrid forecasting approach is built which augments semantic context to ramp-event forecast. Rather than applying an extensive language model directly to predict turbine operating data, we have implemented a pipeline where turbine operating data is converted to simplified text, which is then converted to dense embeddings to be used as inputs for ensemble models incorporated with other features. Testing runs are performed at multiple intervals within the SDWPF dataset, including 10-minute, 30-minute, and 60- minute horizons, with ramp events constituting the highest change in future power output. We check robustness against autoregressive, LSTM, and GRU baselines plus several ensemble configurations, using Diebold-Mariano tests and bootstrap confidence intervals, and we vary the ramp threshold, compress the embeddings with PCA, and validate externally on Kaggle SCADA and NREL data with uncertainty-aware scoring. The semantic-context features produce negligible yet statistically significant gains over the baselines in multiple paired ensemble runs, most clearly at the 30- and 60-minute horizons where these gains hold across different ramp-threshold definitions, and PCA compression helps in some longer-horizon cases. The best context- augmented ensembles rank near the top overall, though the GRU model still posts the lowest ramp-event RMSE at 30 and 60 minutes. External tests confirm the error reduction generalizes across datasets, but the size of the gain depends on both model and dataset. Prediction intervals cover most test cases well but weaken during ramp events, pointing to a localized shift in the data distribution.

---


### 79. [Facts Without Rules: Boundary Metadata Collapse in Multi-Agent LLM Handoffs](https://arxiv.org/abs/2608.29028)

**<font color=#1a73e8>作者：</font>** Yian Wang, Agam Goyal, Eshwar Chandrasekharan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent LLM systems often coordinate by compressing an upstream interaction into a handoff artifact that downstream agents treat as shared state. We show that this handoff step is a structural source of privacy leakage: summaries preferentially preserve operational facts while weakening the boundary metadata that governs how those facts may be used---a failure mode we call \emph{summary collapse}. On a controlled multi-agent coordination testbed we measure marker survival with a human-validated judge ($\kappa = 0.74$), where $\sigma_b = 1$ means every boundary marker survives verbatim and $\sigma_b = 0$ means all are lost. Boundary-marker and operational-fact survival are nearly uncorrelated at the handoff level on both GPT-5-mini and DeepSeek-R1-32B (Pearson $r$ near zero): uncompressed free-text handoffs preserve boundaries at $\sigma_b \approx 0.80$, whereas a $25$-word budget drops $\sigma_b$ to ${\approx}0.57$ while operational-fact survival stays near ceiling. Controlled downstream tests reveal that protection depends on \emph{boundary explicitness}: vague languages leak in $73\%$ of GPT and $50\%$ of DeepSeek cases, while explicit constraints reduce leakage to under $15\%$ across all three tested models. A no-handoff single-agent control further shows the failure is not reducible to multi-agent topology as direct full-marker access still leaks more often than the operationalized handoff. Prompt-only mitigation and exact-string redaction only partially address the problem, while a gold-derived audience allowlist nearly eliminates leakage across models, showing that correctly identifying audience boundaries is the key factor.

---


### 80. [Learning to Follow In-Context Watermark Instructions via Self-Distillation](https://arxiv.org/abs/2608.29030)

**<font color=#1a73e8>作者：</font>** Yepeng Liu, Tianyi Chen, Xuandong Zhao 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In-context watermarking (ICW) prepends an instruction to a query asking the model to embed a statistically detectable signal in its response. It thus equips LLMs with a watermarking interface that third parties can invoke without access to model internals. Its reliability hinges on the LLM following the instruction without degrading answer quality, yet how well current LLMs do so has not been measured. We introduce $\mathsf{ICWBench}$, a benchmark of three verifiable ICW instruction families, each scored on both detectability and answer quality. Evaluating 14 frontier proprietary and open-source LLMs, we find that none of the evaluated LLMs achieves both objectives across all three families. To address this, we propose a self-contained two-stage training method, requiring no distillation from a stronger model, no manual annotation, and no pre-existing ICW IF ability. The first stage, self-distillation with logits perturbation (SDLP), uses the same base LLM as both teacher and student: an instruction-equivalent decoding-time logits perturbation makes the teacher follow the ICW instruction, and the student is trained to match the teacher's output distribution. The second stage applies reinforcement learning with the automatic verifier as the reward. Applied to Qwen3-14B and GPT-OSS-20B, our method raises average TPR@$1\%$FPR across three ICW instructions from $0.100$ to $0.974$ and from $0.337$ to $0.968$, respectively, while maintaining high response quality under both perplexity evaluation and LLM-as-a-Judge.

---


### 81. [A Unifying Perspective on Language Model Representations: From Filler-Role Structure to Mechanistic Interpretability](https://arxiv.org/abs/2608.29034)

**<font color=#1a73e8>作者：</font>** Zhang Enyan, R. Thomas McCoy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A wide range of methods have been proposed for interpreting language models, delivering important insights into their inner workings. However, different methods and their resulting insights stand in relative isolation: what could the underlying structure of language models be, such that they give rise to all our interpretations? In this work, we propose using Tensor Product Representations (TPRs) as a unifying hypothesis. TPRs give a concrete proposal for how compositional structure could be represented in vector space --- as filler-role bindings. We show, both mathematically and empirically, that TPRs can unify several prior interpretability methods: additive analogies, linear probing, sparse autoencoders, and activation patching. Mathematically, we show that these methods can all be derived from TPRs. Empirically, we apply the derivations to a range of different models --- from small toy models to LLMs --- to construct instances of each of the above interpretability methods; these constructed variants perform comparably to their standard variants. We view this work as a step toward what interpretability will ideally provide: a unified account of the nature of neural networks, corroborated not just by individual observations but also by an explanation of the connections between them.

---


### 82. [EmoLASP: Emotion Recognition with Language Models and Answer Set Programming](https://arxiv.org/abs/2608.29035)

**<font color=#1a73e8>作者：</font>** Thao Le, Michael Thielscher  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Emotion recognition in conversations is increasingly tackled with language models, but these models can be unstable and expensive to fine-tune or to prompt with long dialogue histories. We propose EmoLASP, a framework that combines a language model with declarative reasoning via Answer Set Programming (ASP) to predict VAD scores (Valence-Arousal-Dominance) in conversations. Experiments on a widely used benchmark dataset (IEMOCAP) across six open-source LLMs (3B-120B) and two PLMs (BERT, RoBERTa) show that EmoLASP improves prediction performance compared to using the language model alone, even when the LLMs/PLMs are given no dialogue history in their prompts or input vectors. The gains are largest for prompt-only LLMs, which EmoLASP uses without any fine-tuning. However, for fine-tuned PLMs, the reasoner adds little once dialogue history is available. EmoLASP's LLM pipeline demonstrates the potential advantages of using a reasoning approach to ensure emotion prediction consistency and to reduce both the cost of fine-tuning and the cost of prompting with long dialogue histories.

---


### 83. [DocIntent: Answerability-Guided Agentic Restoration for Real-World Document Visual Question Answering](https://arxiv.org/abs/2608.29037)

**<font color=#1a73e8>作者：</font>** Zihan Huang, Shihang Wu, Junle Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Real-world degradations such as blur, shadow, distortion, and moire patterns severely impair the document question-answering capabilities of Multimodal Large Language Models (MLLMs). Applying restoration tools before Visual Question Answering (VQA) is an intuitive solution. However, existing restoration approaches remain limited, as manually designing and executing restoration strategies is labor-intensive and requires domain expertise. Agentic restoration offers new possibilities for automation, yet existing frameworks primarily target natural images and pursue perceptual quality, overlooking that restoration should serve downstream tasks rather than optimize generic image quality metrics. To this end, we explore the value of agentic restoration for real-world degraded document VQA and propose DocIntent, a training-free Answerability-Guided Agentic Restoration framework. DocIntent first assesses question answerability, then identifies task-relevant degradations and selectively invokes restoration tools. A Comparison-Based Rollback mechanism validates each restoration step and reverts it when question-relevant evidence becomes less decipherable. The entire process requires no additional pretrained degradation classifier or image quality assessment model. Extensive experiments on the WildDoc benchmark show that DocIntent consistently improves the average score and consistency of different open- and closed-source MLLMs. The code and experimental data will be publicly available.

---


### 84. [RouteSparse: Input-Conditional Pattern Routing for Budgeted Long-Context Prefilling](https://arxiv.org/abs/2608.29058)

**<font color=#1a73e8>作者：</font>** Chao Zhang, Yifan Ji, Ziyan Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dynamic sparse attention can reduce the quadratic cost of long-context prefilling without changing model weights. MInference assigns each attention head one pattern offline and estimates that pattern's sparse indices for every prompt. This design is efficient, but it assumes that a head's preferred pattern and sparsity budget remain suitable across inputs. We introduce RouteSparse, which routes each head and prompt segment among a small library of GPU-efficient sparse patterns. A low-cost probe estimates pattern utility and uncertainty; a latency-aware router then selects a pattern and budget, while uncertain cases fall back to a denser mask. We formulate routing as constrained risk minimization, derive an attention-output error certificate from omitted probability mass, and evaluate the method on long-context retrieval, question answering, summarization, and language modeling. On Llama 3.1-8B-Instruct with 128K-token prompts, RouteSparse achieves $6.5\times$ dense prefill speed with a 0.2-point RULER drop relative to dense attention, compared with $7.3\times$ speed and a 1.6-point drop for fixed per-head routing. Ablations confirm that input-conditional routing, hardware profiling, and selective dense fallback each contribute to the quality--latency tradeoff.

---


### 85. [Agent2UCB: Agentic System for Generative Engine Optimization](https://arxiv.org/abs/2608.29063)

**<font color=#1a73e8>作者：</font>** Sheldon Yu, Rui Wang, Tong Yu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model driven search engines such as Google AI Overviews and Perplexity have created new opportunities for Generative Engine Optimization (GEO) the practice of refining content to increase its likelihood of being cited or summarized by generative systems. We demonstrate Agent2UCB, an agentic GEO system that autonomously improves content visibility through customized, feedback-driven optimization. For each content item, the system evaluates nine GEO strategies, identifies the most effective method, and accelerates selection using a bandit-based Agent2UCB policy that integrates LLM priors with online reward signals. To monitor side effects, the system also provides a lightweight, text-only SEO readiness evaluation covering readability, topical coverage, and EEAT-style credibility. Experiments on GEO-Bench show consistent visibility gains while preserving SEO quality. The demo allows users to choose the websites of interest, observe the optimization workflow, and compare GEO/SEO outcomes across methods.

---


### 86. [Not All or None: Dynamic Construction of Target-aware Memory Graph for Conversational Stance Detection](https://arxiv.org/abs/2608.29066)

**<font color=#1a73e8>作者：</font>** Yifan Xiang, Bin Liang, Yuqi Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Stance detection is crucial for understanding the underlying attitude of an expression towards a target. Conversational stance detection is a more challenging stance detection task in real-world social media scenarios, as it involves detecting the user's stance by leveraging the target-related historical statements across conversational sessions. In this paper, we propose target-aware Memory Graph TamGraph, a novel method that dynamically leverages target-related statements for conversational stance detection. Instead of considering all preceding historical conversations or using no prior conversation information for stance detection, our TamGraph employs a stepwise, entropy-guided backtracking mechanism to selectively activate memory from historical conversations and dynamically constructs a target-aware graph to model the stance relations among utterances. This allows the exploitation of target-related information from the conversation history for stance detection while preventing the introduction of noise. Experimental results on both English and Chinese benchmarks demonstrate that our TamGraph substantially improves LLM performance on conversational stance detection.

---


### 87. [Selective Disclosure of Hidden Directives in Reasoning Models: Behavioral Asymmetry and Steering](https://arxiv.org/abs/2608.29070)

**<font color=#1a73e8>作者：</font>** Zimo Shi, Xander Tifft, Wen Xing  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning traces are increasingly proposed as a mechanism for AI oversight: a monitor inspecting a model's reasoning can, in principle, detect misbehavior invisible from outputs alone. This assumes CoT surfaces what a model is instructed to do regardless of the instructions given. We test this assumption along two axes. First, we introduce the Instruction-Compliance Gap (ICG): the difference in probability that a model's CoT explicitly references a hidden system prompt directive when that directive is malign versus benign. Across 100 task pairs and 8 frontier reasoning models from 5 families, we find consistent asymmetric disclosure, a higher probability of leaking malign hidden instructions than benign ones, in Qwen3-14B (Wilcoxon $p=0.0001$, $+13.9$pp), Qwen3-32B ($p=0.0011$, $+13.0$pp), Qwen3-235B ($p=0.035$, $+5.8$pp), and similar results with MiniMax-M2.5 and DeepSeek-R1. The detector has 100% precision against two independent blinded labelling passes, and an LLM monitor reading only the reasoning trace reproduces the asymmetry in all 8 models against directive-free controls, identifying the specific directive in 82% of malign traces which the detector classifies as clean. Second, steering vectors extracted in MiniMax-M2.5 via Contrastive Activation Addition causally induce hiding from bare prompts and suppress it from prompts that would otherwise produce it, replicating in Qwen3-14B under a pre-registered design. Benign and malign-derived hiding vectors are highly similar (cosine $0.804$ in MiniMax-M2.5; $0.970$ in Qwen3-14B), implying that in these models the disclosure asymmetry arises from differential activation of a shared hiding direction rather than separate mechanisms.

---


### 88. [A Comprehensive Survey on Linguistic Steganography: Methods, Countermeasures, Evaluation, and Challenges](https://arxiv.org/abs/2608.29077)

**<font color=#1a73e8>作者：</font>** Ruiyi Yan, Chenhui Chu, Zhongliang Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Linguistic steganography hides secret messages in natural language text. Large language models (LLMs) have reshaped the field, but a systematic account of how these scattered advances collectively reshape the field in this new era is still missing. We provide one along four axes: 148 steganographic methods, 60 linguistic steganalysis countermeasures, 23 evaluation metrics, and 9 open challenges, each with taxonomies, reviews, and adoption analyses. Cutting across these axes, we identify five specific paradigm shifts in the LLM era: (1) from covertext modification to prompt-only generation, (2) from heuristic to provable security, (3) from white-box symmetric LMs to black-box or asymmetric access, (4) from security-centric designs to joint optimization, and (5) from text-quality concerns to engineering issues. The survey aims to serve as both a reference and a roadmap for practical and responsible linguistic steganography in the LLM era.

---


### 89. [HANIA: Planner-Guided Multimodal Graph Evidence Selection for Grounded Question Answering](https://arxiv.org/abs/2608.29088)

**<font color=#1a73e8>作者：</font>** Zafar Ali, Asad Khan, Nimbeshaho Thierry 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal question answering remains sensitive to noisy, incomplete, and weakly grounded evidence. Long unstructured contexts can introduce redundancy and encourage unsupported generation, while flat retrieval may overlook relations needed for multi-step reasoning. We present HANIA, a planner-guided multimodal graph framework for evidence-grounded question answering. HANIA processes the supplied image and text using a frozen vision-language model to extract concise question-relevant visual evidence with explicit abstention. It then constructs an input-grounded multimodal graph and applies a two-group finite-state planner to coordinate descriptive and relational evidence. Coverage-aware pruning retains a compact evidence set based on relevance, graph confidence, concept coverage, and modality diversity. The selected passages, visual statements, and graph triples are provided to a frozen instruction-tuned decoder. We evaluate HANIA on ScienceQA using answer accuracy, evidence-filtering quality, evidence-budget sensitivity, and efficiency. The results show that structured evidence planning and compact graph-guided retrieval can support competitive multimodal question answering without target-dataset fine-tuning or iterative retrieval. The code is available at this https URL.

---


### 90. [EviAnchor: Mitigating Hallucinations in Large Vision-Language Models via Regional Visual Evidence Compensation](https://arxiv.org/abs/2608.29092)

**<font color=#1a73e8>作者：</font>** Sihang Jia, Shuliang Liu, Songbo Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) frequently generate content unsupported by visual inputs. Preliminary experiments show that visual evidence is primarily incorporated into answer-side representations in early-to-middle decoder layers, while its direct influence progressively weakens in later layers. This attenuation suggests that visual evidence acquired earlier may be insufficiently utilized during subsequent generation. Based on this observation, we propose EviAnchor, a training-free and single-branch inference framework that preserves and reactivates visual evidence throughout generation. EviAnchor introduces Regional Evidence Anchor (REA) slots to progressively aggregate dense visual tokens into spatially structured representations. It then strengthens the current decision state's access to these visual anchors through decision-conditioned evidence routing, mitigating excessive dependence on textual context. Finally, the model resumes its native Transformer computation to integrate the retrieved visual evidence with question semantics and generation history. Experiments across POPE, CHAIR, and MMHal-Bench demonstrate consistent improvements in visual grounding.

---


### 91. [Development of an Autonomous AI Coding Agent using Monte Carlo Tree Search (MCTS) and Gemini LLM Frameworks](https://arxiv.org/abs/2608.29096)

**<font color=#1a73e8>作者：</font>** Pravin Game, Vipin Ramakrishnan, Prathamesh Wagh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The ongoing changes in software engineering requirements have created a substantial need for automated tools which can create secure source code from natural language input. The performance of traditional Large Language Models (LLMs) becomes limited by their "one-shot" capability which results in logical hallucinations together with reduced algorithmic performance during complicated operations. The research presents an autonomous AI Coding Agent which establishes a connection between LLM-generated content and production-ready software through its organized methodology for decision making. Our framework uses the Gemini 2.5 Flash API for essential reasoning capabilities while employing a tailored Monte Carlo Tree Search (MCTS) method to solve code generation challenges as a search operation. The agent uses a "Self-Critic" evaluator system to test different implementation methods which it ranks according to their accuracy and difficulty level before it improves its operational framework through backpropagation. The system operates through a Flask-based web interface which delivers instant feedback together with syntax highlighting features. Our experimental results show that the MCTS-based method achieves a 92% success rate on complex logical prompts while surpassing standard zero-shot generation models.

---


### 92. [Recognition-Refusal Misalignment in LLMs: Why Models Answer Structurally Unanswerable Questions](https://arxiv.org/abs/2608.29109)

**<font color=#1a73e8>作者：</font>** Yucheng Du, Xiyang Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often answer structurally unanswerable questions, such as computing cot(-540°) or evaluating (1).startswith("1"), instead of abstaining. We ask whether this failure reflects missing recognition or failed routing from recognition to abstention. Across instruction-tuned models from 1.7B to 70B parameters, a single linear direction in the hidden state separates answerable from structurally impossible math and code prompts, showing that models represent impossibility before generation. Yet this recognition direction is nearly orthogonal to the canonical safety-refusal direction that mediates trained harmful-content refusal. An in-domain behavior-defined invalidity-aware direction is closer to recognition, but only partially aligned with it, and remains near-orthogonal to safety refusal. Generation-time steering along the recognition direction changes invalidity-aware behavior bidirectionally and dose-responsively on structural math and code cells, while random directions do not. Base/instruct comparisons further show that the low-cosine geometry is already present at the pretraining endpoint. The confident-on-impossible failure is therefore better explained as a routing failure than as an encoding failure: the model has a usable "no admissible answer" signal, but the safety-refusal pathway is not aligned to use it.

---


### 93. [Emergent Misalignment Is Not Magical](https://arxiv.org/abs/2608.29118)

**<font color=#1a73e8>作者：</font>** Mingxuan Li, Qirun Dai, Heran Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning large language models (LLMs) on narrowly harmful datasets can lead to misalignment broadly, a phenomenon known as emergent misalignment (EM). EM poses a challenge for AI safety and our understanding of LLMs. Prior work often frames EM as an unexpected behavior, and explains it by appealing to general misalignment directions or anthropomorphizing it as acquiring an evil persona. However, the mechanisms behind these framings remain obscure. In this work, we show that EM is a predictable and data-dependent generalization phenomenon. By examining the base model's representation of EM training data and evaluation prompts, we find that evilness after EM training is highly predictable from representational distance: the closer an evaluation prompt is to training data centroid, the more evilness it elicits from EM models after training (with an average Spearman correlation of -0.73 across 12 model-dataset settings). Building upon this analysis, we further demystify EM by showing that (1) its effectiveness changes significantly based on training data format; (2) there is not a general misalignment direction that transfers across different EM models; (3) the effect of EM is fundamentally different from persona changes. Furthermore, we extend the EM generalization metric from a scalar distance to a dataset-specific generalization direction, which robustly predicts EM models' evilness under semantics-preserving prompt perturbations including appending random tokens and paraphrasing, where other methods do not reliably generalize.

---


### 94. [HEAR Who Said What: Unlocking Speaker-Attributed Reasoning via Counterfactual Voice Grounding](https://arxiv.org/abs/2608.29120)

**<font color=#1a73e8>作者：</font>** Dongwook Lee, Sangkwon Park, Eunwoo Song 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Speech Language Models (SLMs) are increasingly deployed in multi-speaker environments, yet their ability to attribute speech to the correct speaker and reason over speaker identities remains unclear. Hence, we introduce HEAR, a conceptually hierarchical benchmark diagnosing the foundational capabilities of speaker-attributed reasoning, comprising 2.4K human-verified samples from 887 diverse multi-party audio clips. Evaluating 20 leading SLMs on HEAR reveals they struggle with these foundational tasks, often relying on semantic priors rather than actual vocal cues. To address this, we present A2R, a 30B model optimized on Counterfactual Audio with Speaker-level Hard negatives (CASH), a dataset designed to guide the model to prioritize acoustic vocal cues over linguistic signals. A2R achieves strong performance on HEAR and exhibits zero-shot generalization to diverse multi-speaker downstream tasks, demonstrating that learned speaker attribution unlocks the model's latent capacity for speaker-aware reasoning. All resources are available at this https URL

---


### 95. [Beyond Correctness: Validity-Oriented Evaluation of Biomedical LLM Judges](https://arxiv.org/abs/2608.29127)

**<font color=#1a73e8>作者：</font>** Rodrigo de Oliveira, Federico Pittino, James Gwinnutt 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose a scalable, validity-oriented pipeline for evaluating biomedical LLM judges when high-quality human judgments are scarce. First, we augment existing human-labelled biomedical benchmarks with deterministic, metric-grounded mutations that produce auditable preference pairs. Second, we evaluate judges beyond aggregate correctness using three deployment-relevant dimensions: correctness against metric-derived gold labels, robustness under repeated stochastic sampling, and compliance with the requested output format. We use this pipeline to assess Llama-3.1-8B-Instruct under four regimes: (1) base, using the instruct model as is; (2) SFT, distillation-based supervised fine-tuning only; (3) RL, GRPO-based reinforcement learning only; and (4) SFT$\rightarrow$RL, SFT followed by RL. The base and single-stage regimes struggle on structured medical discrimination such as PICO extraction and clinical calculations, whereas SFT$\rightarrow$RL performs best across correctness, compliance, and robustness; gains concentrate on decomposable tasks (PICO, MedCalc), at times matching or outperforming frontier models.

---


### 96. [APIFlow-Bench: Measuring Whether Agents Survive Long, Dependent API Workflows](https://arxiv.org/abs/2608.29128)

**<font color=#1a73e8>作者：</font>** Zelin Wan, Arash Nourian, Xiaoxiao Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tool-using agents are commonly evaluated by a single bit: whether an end-to-end workflow completed. This metric fails to distinguish failures that matter in production, such as expired credentials, malformed payloads, or correct execution followed by incorrect final delivery. We introduce APIFlow-Bench, a fully auditable benchmark for long-horizon, dependent REST-API workflows that decomposes performance into seven engineering capabilities and requires agents to produce answers supported by the actual call path. We generate synthetic API worlds forward, subtask by subtask; each subtask is admitted only after a zero-LLM self-test triad verifies its grader and an oracle establishes solvability, and an adversarial audit identified and fixed six grader exploits. Grading is deterministic and provenance-sensitive: a state check traces a mock-minted canary through the API data flow to the response the answer must originate from, and a typed answer card is verified field by field. We release all answer keys and 44,362 unredacted execution transcripts. Across 19 frontier and open-weight models under one neutral scaffold, we find: (1) longer dependency chains degrade success, from 93% on individual subtasks to 74% on clean 20-subtask chains and 61% when including the 8% of chain trials that a model-consensus screen flags as passed by no model; (2) reliability separates models more than best-case capability, with best-of-five spanning seven points but all-five-of-five reliability spanning 44 points; (3) the independent-error account of compounding failure does not fit the data: pass rates on 20-subtask chains are 33 percentage points above the product of subtask-level rates, and on the clean slice 77% of failing runs reached the correct final state and failed only at delivery.

---


### 97. [AI Historian: Helping historians organize and verify person-centred temporal clues from dispersed historical narratives](https://arxiv.org/abs/2608.29133)

**<font color=#1a73e8>作者：</font>** Yifeng Lu, Zijie Yang, Jie Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> History is not preserved in complete, continuous form. Accounts of a person's activities, relationships and historical contexts are scattered across texts, chapters and narrative perspectives; historians must retrieve, identify and compare these materials to reconstruct temporal sequences and verify them against sources. Here we present AI Historian (AIH), an AI agent system that helps historians organize person-time evidence from dispersed biographical narratives. It takes source sentences as evidence units, identifies people and temporal cues, verifies candidate cross-text associations and infers comparable temporal ranges while preserving traceable source-text evidence. We evaluated AIH on six Shiji cases concerning Liu Bang, Xiang Yu and Xiao He. AIH Agent achieved a temporal-localization MicroIoU of 86.2%, compared with 81.3% for human-only annotation and 17.1% for direct large-language-model prompting; it required about 14 min, versus 1 h 32 min for human-only annotation. We further applied AIH to the Twenty-Four Histories and other ancient Chinese histories, ancient Japanese and Korean histories, and modern and contemporary historical materials, and released the results through Westlake Historian. These results indicate that AIH can reduce the cost of organizing historical materials at scale while turning connections obscured by chapter-based narration into traceable, revisable research questions for collaborative testing.

---


### 98. [Not the Same Protector: Deployment-Dependent Protective Intervention in LLMs](https://arxiv.org/abs/2608.29136)

**<font color=#1a73e8>作者：</font>** Eunna Lee, Soomyoung Lee, Jungpyo Nam 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> We ask whether a model protects a user in the same way when that user speaks rather than types. Using a single distress vignette---a physical injury of unstated severity following an interpersonal conflict---we present four frontier models with matched inputs across voice, text, and raw API deployment conditions (n=30 per cell) and code each response along five binary protective indicators, including whether the model issues an explicit medical-care directive. Voice-interface responses are markedly shorter than text-interface responses for three of the four models, and protective behavior contracts alongside that compression: medical directives are at ceiling under both the API and text conditions but decline under voice for every model tested. The contraction is not reducible to length. One model produces voice and text responses of comparable length yet still drops medical directives, and another falls below ceiling between its API and voice conditions, whose responses are of nearly identical length. Under raw API access the pattern is categorical rather than partial: no model asks after the user's safety even once. These results show that protective intervention is sensitive to the surface through which a request arrives, that this sensitivity is detectable using a simple protective coding scheme, and that it is not explained by turn length alone.

---


### 99. [Chat-Edit-3D++: Interactive 3D and 4D Scene Editing via Large Language Models](https://arxiv.org/abs/2608.29137)

**<font color=#1a73e8>作者：</font>** Shuangkang Fang, Yufeng Wang, Yi-Hsuan Tsai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent work on image content manipulation based on vision-language pre-training models has been effectively extended to text-driven 3D scene editing. However, existing schemes for 3D scene editing still have certain shortcomings, hindering their further development as interactive design tools. Such schemes typically adhere to fixed input patterns, limiting flexibility in text input. Furthermore, their editing capabilities are constrained by a single or a few 2D visual models and require intricate pipeline design to integrate these models into 3D reconstruction processes. To address the aforementioned issues, we propose the Hash-Atlas network, which reformulates 3D scene editing as operations on 2D atlas images, thereby achieving a workflow decoupling of the 2D editing and 3D reconstruction processes. Building on this foundation, we introduce a dialogue-based 3D scene editing approach, termed CE3D++, which is centered on a large language model (LLM) that allows arbitrary textual input from users and interprets their intentions, subsequently facilitating the autonomous invocation of the corresponding visual models. Additionally, we extend CE3D++ to monocular 4D scenes by imposing motion constraints on moving objects and further fine-tuning the LLM by creating a trajectory dataset related to editing tasks, which enables the smaller LLM to schedule up to 30 different visual tools accurately. Experimental results demonstrate that CE3D++ effectively integrates multiple visual models to achieve diverse visual editing effects, possessing strong scene comprehension and multi-round dialog capabilities. The source codes and trained models are available at this https URL.

---


### 100. [Quantifying Error Tolerance in Synthetic Data: An Atomic-level Operand vs. Operator Perturbation Study](https://arxiv.org/abs/2608.29144)

**<font color=#1a73e8>作者：</font>** Jiaxiang Liu, Chenhao Yuan, Shuwen Xu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Synthetic data generation has become a cornerstone for advancing large language models. However, the lack of the quantitative analysis for error tolerance became a critical bottleneck. Consequently, current filtering strategies fluctuate between two extremes: they are either overly aggressive, risking the exclusion of potentially valuable samples, or overly permissive, failing to eliminate erroneous samples effectively. To bridge this gap, this paper introduces Atomic Tree Operation Modeling (ATOM), a framework that decomposes data into functional units ($f(x)\rightarrow y$). ATOM distinguishes benign Operand $x$ perturbations from fatal Operator $f$ perturbations. The former are needlessly discarded by aggressive filtering, while the latter slip through permissive filtering. Our experiments reveal a double dissociation: models are robust to operand perturbations but collapse under operator perturbations. By prioritizing operator over aggressive operand precision, our ATOM-synthesized data outperforms rigorous baselines (e.g., +3.1% gain over LIMA), suggesting that operator diversity matters more than operand precision. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**51-100**（第 2/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
