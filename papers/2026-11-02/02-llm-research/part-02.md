# 🧠 大模型相关研究 | 2026年11月02日

> 本类共 **353** 篇论文：已确认 **335** 篇，待复核 **18** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

---

### 51. [Can Event Detectors Leave the Broadcast Camera? Evidence from Tennis](https://arxiv.org/abs/2610.38042)

**<font color=#1a73e8>作者：</font>** David Soeiro-Vuong, Andre-Louis Rochet  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Ball bounces and racket hits are the events from which tennis statistics are derived, and on monocular video the two are easy to confuse. We release a benchmark of 345 bounce and hit annotations at frame level on eight clips that mix broadcast, fixed elevated, phone and court-level viewpoints, with a frozen development and test split, a confusion-aware matcher, clip-level bootstrap intervals and a blind second annotation of three clips. On it we score supervised precise spotters with published broadcast weights, two zero-shot vision-language models, and RallyArb, an arbitration layer over a ball track and player poses that fits no parameter on event labels. The supervised spotters score near-perfectly on broadcast footage and almost nothing on phone and court-level footage, where the pooled bounce F1 of E2E-Spot is 0.130. RallyArb keeps a bounce F1 above 0.8 on the three phone and court-level clips, two of which were used to tune it, and finds 8 of 11 bounces on the held-out one, but it places hits too far from the contact frame to match human timing. The vision-language models detect events on every viewpoint and miss the contact frame by about 0.1 s. Fine-tuned leave-one-clip-out from its broadcast weights, the spotter reaches about 0.8 bounce F1 on two phone and court-level clips and stays at 0.2 on a grazing phone angle. The annotations, the evaluator and the frozen predictions of every scored row are released.

---


### 52. [PromptSense: Sentiment-Aware Mental Health Chatbot with Dynamic Prompting](https://arxiv.org/abs/2610.38044)

**<font color=#1a73e8>作者：</font>** Sugi Lee, Jianlong Zhou, Jing sUN  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Current Large Language Models (LLMs)-based mental health chatbots often lack sufficient empathy, contextual awareness, and safety mechanisms, potentially leading to ineffective or harmful interactions. This paper proposes a novel framework that integrates sentiment and depression analysis with a rule-based filtering mechanism prior to model inference. By dynamically constructing prompts based on emotional and risk-related insights, the framework aims to significantly improve the contextual relevance, empathy, and risk-aware of model-generated responses. We evaluated four model strategies and two prompt engineered variants across qualitative metrics such as empathy, helpfulness, clarity, relevance, safety, as well as toxicity assessments using the Perspective API. Experimental results indicate that the prompt engineering approaches outperforms DSFT and RLAIF by 1.8\% and 1.1\% respectively.

---


### 53. [Ignore the Writing: A Proposal for Peer Review in the Age of AI](https://arxiv.org/abs/2610.38062)

**<font color=#1a73e8>作者：</font>** Vassilis Kostakos  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> The written paper has long stood in as proof of work: a fluent, well-structured manuscript was taken as evidence that good research lay behind it. Generative AI has broken that link. Polished manuscripts now cost nothing to produce, submissions are outgrowing what reviewers can absorb, and venues are turning to AI for help. The logical endpoint is a loop where AI writes the papers and AI reviews them. We argue that this loop is survivable, but only if it is given a reward function, and that human reviewing effort should become that reward function. We propose that submissions should consist of a 1500-word brief plus an unlimited, machine-verifiable appendix. Human reviewers judge whether a pursuit is worthwhile, models verify the experimental record in the appendix, and human curation decides where the field goes next.

---


### 54. [From Error Prediction to Causal Influence: Auditing SAE Features in Multiple-Choice QA](https://arxiv.org/abs/2610.38067)

**<font color=#1a73e8>作者：</font>** Aria Nourbakhsh, Adelaide Danilov, Oleksandr Marchenko Breneur 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sparse autoencoders (SAEs) can predict internal features associated with model errors, but association alone does not establish causal influence. We study this distinction in multiple-choice question answering, where answer preference can be measured by the logit margin between the correct answer and the competing choices. Across eight datasets, we analyze Gemma~3 1B and 4B with Gemma Scope SAEs. We propose a pipeline to filter out the features that have high correlation with format and content artifacts, such as prompt and answer permutation, and evaluate the remaining ones with causal feature interventions. Our results show that SAE activations contain predictive signals about wrongness and uncertainty across models and datasets. After filtering artifact-contaminated features, selected features for causal intervention at question and option spans produce larger absolute margin shifts and a higher wrong-to-correct rate than randomly selected features, indicating greater causal leverage. However, answer flips are rare, and we do not observe stable effect directions across meaning-preserving changes in prompt format and answer order. An adapted HalluSAE baseline produces larger final-token margin changes, but relies on substantially contaminated features and does not significantly improve correction rates. Therefore, the identified features reflect context-dependent answer competition rather than the mechanism of incorrect answer errors.

---


### 55. [Prompt Lottery in LLM-as-a-Judge: Measuring and Mitigating Sensitivity to Syntactic Rephrasing](https://arxiv.org/abs/2610.38076)

**<font color=#1a73e8>作者：</font>** Ilija Subasic, Brett Levert, Andrew Rabinovich 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-as-a-Judge has become a standard for evaluating large language models, yet most approaches implicitly assume that a single judge prompt functions as a stable evaluation instrument. Prior work has primarily explored deliberate prompt modifications such as scoring rubrics, role descriptions, or chain-of-thought reasoning in order to optimize accuracy. In contrast, we investigate whether validated prompt variants intended to preserve evaluation semantics while differing in surface realization (\textit{paraphrastic rephrasings}) yield consistent judgments under a fixed evaluation task. We introduce \textit{Prompt Lottery}, a phenomenon in which paraphrastic rephrasings produce different LLMaJ judgments. Across a large-scale study spanning diverse evaluation tasks, judge families, and model backbones, we find that these variations can alter evaluation outcomes and, in some settings, reverse relative model rankings. A user study with 10 human annotators shows that LLMaJ judges exhibit 6-9$\times$ larger agreement degradation under prompt rephrasings than humans, falling below the generally accepted threshold in usability studies. This indicates that single-prompt evaluation is insufficiently robust for model ranking. Finally, we show that multi-prompt aggregation substantially improves robustness by emphasizing judgments that remain consistent across prompt variants.

---


### 56. [Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](https://arxiv.org/abs/2610.38095)

**<font color=#1a73e8>作者：</font>** NVIDIA, Aastha Jhunjhunwala, Aayushi Ashokkumar Srivastava 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce Nemotron 3.5 Super and Nemotron 3.5 Lightning, open and efficient Mixture-of-Experts Hybrid Mamba-Transformer models designed for reasoning, long-context understanding, and agentic workloads. Super is a 120B-parameter, 12B-active multimodal model, while Lightning is a smaller 30B-parameter, 3B-active text model; both designed for efficient deployment. Both models combine large-scale distillation, long-context training, and native speculative decoding, while Super further incorporates Indic continued pretraining and agentic software-engineering mid-training. We develop a comprehensive post-training pipeline spanning supervised fine-tuning and reinforcement learning (RLVR and RLHF), complemented in Super by specialized teacher training and multi- teacher on-policy distillation (MOPD). This transforms Super from a text-only base model into a multimodal agent capable of reasoning over text, images, video, and interactive tool environments. We further explore test-time scaling through parallel agent execution and self-verification. Across training and deployment, we jointly optimize capability and efficiency. Indic continued pretraining improves Indian-language benchmarks by up to 9.82 percentage points, while agentic mid-training strengthens software-engineering capabilities and robustness across agent harnesses. The post-trained Super model achieves 51.78% on SWE-bench Pro, surpassing Nemotron 3 Ultra despite using approximately 4.6x fewer active parameters. Post-training MTP boosting improves speculative- decoding acceptance length by up to 21.8% under probabilistic draft sampling, while NVFP4 quantization achieves 99.62% median accuracy recovery relative to BF16. Inference optimizations enable up to 4,856 output tokens/s/GPU on GB200 while sustaining at least 50 tokens/s/user.

---


### 57. [Evaluating Causal Reasoning in LLMs: A Case Study in the Challenges of Procedural Generation](https://arxiv.org/abs/2610.38100)

**<font color=#1a73e8>作者：</font>** Justin Clarke, Isha Karn, Patrick Murray 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) appear to represent and reason about a large range of phenomena. In particular, recent studies have examined whether LLMs can accurately reason about causation. One of the most commonly used benchmarks for evaluating formal causal reasoning in LLMs is CLadder, a framework for procedural generation of benchmark data sets that was released in 2023. Experiments with CLadder appear to indicate that LLMs can perform formal causal reasoning in a large percentage of generated examples. In this paper, we examine what can be reliably inferred when LLMs perform well on test sets produced by CLadder. We identify several examples of superficial and highly predictive patterns that the CLadder generator embeds in data sets it generates. We find that even simple models such as random forests perform well on CLadder-generated data sets after training on a sample of generated data. We also find that the performance of many commercial LLMs on CLadder test sets is extremely brittle and that removing large sections of the text that are critical for formal causal reasoning has almost no effect on performance. Given these results, the most likely hypothesis for the strong performance of state-of-the-art LLMs on CLadder is that they are exploiting superficial patterns learned from exposure to training data from the generator. Any inference that LLMs are exhibiting more complex causal reasoning must rule out this hypothesis.

---


### 58. [The Prestige: Benchmarking Cognitive Visual Reasoning using Magic Tricks](https://arxiv.org/abs/2610.38103)

**<font color=#1a73e8>作者：</font>** Shuo Wen, Beixi Du, Edwin Meriaux 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce The Prestige, a video understanding benchmark that probes cognitive visual reasoning through professional magic performances, where deliberate misdirection challenges models to track events and explain unexpected outcomes. The benchmark comprises open-ended questions ranging from temporal and causal understanding to robustness against adversarial questions. Evaluation of leading open-source and proprietary VLMs reveals a substantial gap between even the strongest model and human performance. We also find systematic discrepancies between human and automated grading and identify recurring model failure modes. Ablations further show that models can select correct multiple-choice answers even when they fail to generate correct explanations independently, motivating further investigations into question formats. Together, these findings highlight limitations in both VLM reasoning and its evaluation, underscoring the need for more reliable video understanding models and more rigorous benchmarks.

---


### 59. [TGTV: An Interpretable Framework for UAV Fault Detection and Traceability via Spatiotemporal Graph Learning and Large Language Models](https://arxiv.org/abs/2610.38106)

**<font color=#1a73e8>作者：</font>** Zixuan Wang, Changbo Shi, Ji Liu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Fixed-wing unmanned aerial vehicles experience operating-condition transitions, asynchronous sensor sampling, and control-system compensation that can obscure fault signatures. Existing temporal detection methods have limited capacity to represent coupled faults across subsystems, track their evolution, and constrain language-model diagnoses with quantitative evidence. This paper proposes TGTV, an interpretable fault detection and traceability framework that integrates spatiotemporal graph learning with a large language model. A temporal convolutional network and a graph attention network with weighted fused adjacency extract multiscale temporal patterns and spatial dependencies among sensors. A hybrid temporal Transformer and variational autoencoder then evaluates window-level anomalies using prediction errors and reconstruction probabilities. Continuous-time Shapley attribution identifies critical sensors and high-contribution intervals while preserving the temporal continuity of fault evolution. A structured evidence package combines detection results, graph relationships, temporal attribution, sensor attribution, and operating context. An evidence-constrained diagnosis protocol uses this package to generate flight-level conclusions with traceable evidence identifiers. Cross-flight holdout experiments on the public ALFA fixed-wing flight dataset yield a window-level area under the precision-recall curve of 0.976, accuracy of 0.973, recall of 0.902, and F1 score of 0.920. Flight-level fault diagnosis achieves recall of 0.943 and an F1 score of 0.944. These results demonstrate accurate anomaly detection and quantitatively supported fault-tracing cues, providing a basis for interpretable post-flight fault review and analysis.

---


### 60. [Beauty Is Human: When People Love AI-Generated Art, They Think a Human Made It](https://arxiv.org/abs/2610.38113)

**<font color=#1a73e8>作者：</font>** Zihan Chen, Di Zhu, Lei Nico Zheng  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI now produces images and poems that people cannot reliably distinguish from human-made work, so people often judge for themselves who made a work. We examine how these perceived-authorship judgments relate to aesthetic preference. In a public online AI Art Turing Test, 11,123 people judged whether each of 50 pictures (26 AI-generated) was made by a human and were asked for their favourite. Among the 9,152 respondents who judged their favourite, a picture was 22.1 percentage points more likely to be judged human-made when it was the respondent's favourite, holding respondent and picture fixed. The association was similar for AI-generated and human-made favourites, was positive for all 50 pictures, and appeared under every reported detection strategy. Respondents most negative about AI art chose fewer AI-generated favourites (47% against 60% among the most positive) but more often believed them human-made, partly because others also judged those pictures human. As a result, in every opinion group a third to two fifths of respondents named an AI-generated favourite they believed human-made. A reanalysis of a published experiment on AI-generated poetry, in which 230 people rated each poem before judging its authorship, found the same pattern, although the AI poems were rated higher. When provenance is hidden, liking and perceived human authorship travel together, consistent with aesthetic response serving as evidence of a human maker and with beliefs about the maker shaping enjoyment. The findings qualify research on bias against AI art, which typically uses explicit labels, and inform AI disclosure policy.

---


### 61. [Post-Training Large Language Models with LLMON](https://arxiv.org/abs/2610.38120)

**<font color=#1a73e8>作者：</font>** Basel Shbita, Michael Hind, Chad DeLuca 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) treat all context tokens uniformly, lacking explicit separation between executable instructions and passive data. This leads to prompt injection vulnerabilities, ambiguous instruction binding, and unreliable execution control. We present a post-training methodology using LLMON (LLM Object Notation), a framework that enables separating instructions from data and requires explicit identifier-based execution. We construct a large-scale structured training corpus of 4.6B tokens spanning general, RAG (Retrieval-Augmented Generation), and tool-calling data, augmented with distractor-infused variants in which competing instructions and irrelevant data segments are present in context but not referenced. Post-training two Granite-4.1 base models (3B and 8B) through supervised fine-tuning followed by reinforcement learning, we show that LLMON-structured supervision reduces attack success rates on indirect prompt-injection benchmarks from 53-100% to 0.02-5.6% while preserving general capabilities. We further introduce attention-based interpretability metrics that diagnose failure modes at individual transformer layers for structured inputs, revealing how our approach reshapes internal attention patterns. Our results demonstrate that explicit execution semantics can be taught through standard post-training without architectural modification.

---


### 62. [Answer-Only Disclosure: Private-Context LLM Assistance over Web APIs with a Leakage Ledger](https://arxiv.org/abs/2610.38126)

**<font color=#1a73e8>作者：</font>** Liang Yuan, Xiaohu Du, Ruikun Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Web assistants increasingly answer questions about a user's private documents by pairing a small on-device model with a cloud LLM behind a Web API. In collaborative decoding, the document stays on the client, and the cloud receives only a public view that the user approves, such as the question alone, but the two models exchange messages while the answer is generated. We show that the message transcript can disclose private content that neither the public view nor the answer contains. In a planted-secret audit, speculative decoding with private drafts did not include the secret code in its answers, yet sent the code to the cloud in rejected drafts. We present ADLER, a decoding protocol for streaming LLM APIs in which every message to the cloud depends only on the public view and the answer the user sees, regardless of how the client combines the two models or how the cloud behaves. A client-side leakage ledger then bounds how much the answer itself reveals relative to a public reference process built from the cloud's replies. In the audit, no ADLER configuration exposed the secret beyond the answer. On GSM8K math problems with numerical values masked in the cloud's input, ADLER with an unlimited leakage budget raises the exact-match accuracy of a 0.5B client from 0.41 to 0.83 and of a 1.5B client from 0.67 to 0.85 under lenient answer parsing, close to the 0.92 achieved by uploading the full problem. It also exceeds a zero-leakage program baseline (0.69) by 0.14 and 0.16, respectively. In this baseline, the cloud writes a program that the client runs offline using the private numbers. The ledger records the disclosure charge associated with this gain; budgets of 16 nats or less leave accuracy near the cloud-only baseline on GSM8K.

---


### 63. [Decompose, Don't Expand: Capability-Independent AI Systems by Construction](https://arxiv.org/abs/2610.38144)

**<font color=#1a73e8>作者：</font>** Tejaswi Gowda  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A recurring design choice in building AI systems is whether, when a task is too hard for a model, to expand the model (make it larger, better-prompted, fine-tuned), or to decompose the task (extract the parts that admit a deterministic solution to a host, leaving the model only the irreducibly fuzzy residue). We make three claims. First, that many tasks commonly delegated whole to a model are in fact deterministic tasks with a small generative core. Second, and our central empirical result, that decomposing such a task yields a measurable and desirable property we call parity by construction: on the extracted sub-tasks the model-size performance curve becomes flat, because no model performs them at all. We measure this across nine models spanning a 494M-parameter local checkpoint to a frontier Opus-class model, a thirty-fold parameter range on the local family alone: once the host resolves the context, operation selection scores identically for all nine models and selector resolution for eight of nine, while the one task that does not decompose, labelling, remains sloped across the same range. Because the task leaves the model, a stock checkpoint suffices: no task-specific training and no fine-tuning. Third, that this is a general design discipline, not a domain trick: we show the same move recurring across physics setup, motion retargeting, and object-model editing, and in a Web-CLI tool family (same author, so not an independent replication). We give a method for locating the cut, the construction that makes a cut exist (a deterministic surface and a closed grammar over it), and a way to make the residue safe (resolve the deterministic context; verify the generative output), position the work against neuro-symbolic AI, tool-augmented language models, and generate-and-verify approaches, and are explicit about what is measured (one domain) versus illustrative (the rest).

---


### 64. [SkillCT: A Multidimensional Benchmark and Execution-Free Baseline for Agent Skill Assessment](https://arxiv.org/abs/2610.38147)

**<font color=#1a73e8>作者：</font>** Mengyu Sun, Zunlong Zhou, Ziyuan Yang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent skills package instructions, scripts, and resources for specialized tasks and are increasingly distributed through public Web repositories. However, existing skill benchmarks primarily focus on downstream task execution, insufficiently assessing specification quality, behavioral robustness, semantic alignment, and responsibility boundaries. Their reliance on task-specific tools, environments, and repeated executions limits scalability and pre-deployment assessment. To address these challenges, we introduce SkillCT, a benchmark that broadens skill assessment from downstream utility to a multidimensional characterization of skill quality. SkillCT evaluates skills across nine complementary dimensions spanning three aspects: Static Assessment, which captures intrinsic properties of the skill specification; Dynamic Assessment, which measures whether the induced behavior remains stable across backbone models and request variations; and Human-Assisted Assessment, which examines behavior-chain consistency and task granularity. These dimensions provide a broader view of skill quality than execution success. Applying SkillCT to a public skill corpus establishes a reference benchmark for analyzing quality weaknesses and relationships across dimensions. Building on this benchmark, we propose an execution-free quality evaluation baseline that predicts the multidimensional quality profiles of unseen skills by retrieving and leveraging similar reference skills, without executing the skills under evaluation. This reduces token consumption and evaluation time, while preserving consistency with the full assessment. Furthermore, SkillCT-guided optimization improves downstream task success and execution efficiency, demonstrating its value for skill refinement. These findings highlight the effectiveness of SkillCT in supporting scalable skill assessment, optimization, and repository maintenance.

---


### 65. [REEL: Same Frames, Different Answers and Different Costs](https://arxiv.org/abs/2610.38158)

**<font color=#1a73e8>作者：</font>** Xin Liang, Jiangpeng He  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Video understanding keeps moving toward longer recordings, and the longer a recording is, the more questions can be asked about it. But processing it again for every question does not scale, so many systems watch the video once, build a memory, and answer later questions from it. Yet what to remember is decided before anyone knows what will be asked, and whatever is left out cannot be recovered later.
Moreover, whether the savings pay off is judged by token counts, which fall when the input gets shorter but not when the model reuses what it has already computed. We present REEL, an evaluation framework that compares three saved representations built from exactly the same observed frames, so that a change in answers can come only from what the system remembered. Text writes a short record of what happened, Visual keeps the encoder outputs, and Prefix State also keeps the language-model prefix. Each is compared with full reprocessing (Frames) by paired correctness changes, cumulative GPU time, and storage size. Across six vision-language models and two benchmarks, Text and Frames differ in correctness on 20\% to 29\% of questions, even when their mean accuracy is almost the same. By contrast, Visual and Prefix State stay much closer to Frames. With unlimited storage, Prefix State is the cheapest in total GPU time among memories that keep almost all of the answers Frames gets right, for every model on both benchmarks. The trade-off is storage: Prefix State keeps up to about 21 GiB per video, whereas Text needs only kilobytes. Reusing computation and discarding information both look like efficiency, but only the second removes evidence that later questions may need, and neither mean accuracy nor token count tells them apart. REEL makes that difference measurable for any system that answers many questions from one saved memory.

---


### 66. [ATI-OPD: Adaptive Teacher Intervention for Stable Long-Sequence On-Policy Distillation](https://arxiv.org/abs/2610.38160)

**<font color=#1a73e8>作者：</font>** Jiannan Guan, Youxin Jiang, Yutai Hou 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own responses using token-level feedback from a teacher. As responses grow longer, the student's prefix can depart from the teacher's own reasoning, weakening its feedback on later tokens. Updates based on this feedback can reinforce the same deviations in later responses and destabilize training. Prior approaches such as length control and loss reweighting limit learning from problematic responses but leave their prefixes unchanged. Fixed cutoffs can also discard later reasoning. We propose \textbf{Adaptive Teacher Intervention for On-Policy Distillation (ATI-OPD)} to improve subsequent teacher guidance by revising the student's reasoning prefix. ATI-OPD replaces the earliest high-disagreement segment with a short teacher segment, then lets the student resume its own reasoning from the revised text. To handle renewed disagreement, it excludes persistently divergent suffixes from the distillation loss while retaining useful student continuation. Training diagnostics show less teacher-student disagreement, fewer gradient spikes, and fewer extremely long responses. Across five mathematical reasoning benchmarks and two teacher-student pairs, ATI-OPD improves average student-only accuracy over standard OPD.

---


### 67. [DecompGym: Benchmarking LLM Agents on Designing Decomposition Algorithms](https://arxiv.org/abs/2610.38175)

**<font color=#1a73e8>作者：</font>** Sikai Cheng, Tinghan Ye, Arnaud Deza 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Benders decomposition and column generation solve large optimization problems by passing cuts, columns, and dual values between a master problem and subproblems, and are hard to implement correctly. Large language models now automate parts of algorithm design, which points toward agents that build decomposition solvers for new problems. As a first step toward such agents, we study how well current coding agents design and implement these two algorithms, and how they fail. We introduce DecompGym, 81 instances from nine problem families (five Benders, four column generation), in which an agent writes a solver for a prescribed method. Each solver must meet three criteria: execution within a 60-second time limit; numerical feasibility together with a method audit, in which an LLM judge reads the solver's code; and an objective within 1% of the stored optimal objective. We evaluate 12 GPT, Claude, and Gemini models running in coding-agent tools. Over up to ten attempts, we compare independent regeneration with reflection, which first diagnoses the failure. On the first attempt, two models solve every instance and seven solve more than 90%. Most Benders failures (48 of 62) are missing or suboptimal solutions. The most common column-generation failure is a method-audit rejection. Output checks alone would accept 93 of the 108 attempts that fail the method audit. The most common rejection, an optimalif, occurs 96 times, 92 of them in one this http URL turns 66% of retries into successes, compared with 39% for regeneration, and it repairs method-audit failures, for which the judge names the defecective gaps. Agents for decomposition therefore need checks on how a solver reaches its answer and feedback that locates the error. The benchmark is available at this https URL.

---


### 68. [Component Translation and Judge-Labelled Refusal: A Multilingual Safety Evaluation](https://arxiv.org/abs/2610.38181)

**<font color=#1a73e8>作者：</font>** Yongxi Zhou, Junwei Yao, Wenbo Ye 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Whole-prompt translation evaluates a request in different languages but does not compare which component carries a language. We introduce a paired reversal: translate the complete request component or the complete operation component into the same target language, holding behaviour, English frame and translated-span count fixed. Component identity and non-English text quantity change together. Assigning English, Chinese and Spanish independently to the two components yields nine configurations on 190 of 300 sampled harmful behaviours retained after consensus annotation and automatic gating. Refusal scored by language-model judges is the primary outcome; unsafe compliance is reported separately. On Gemini 2.5 Flash and DeepSeek, three refusal swaps are about 5.3 percentage points and the fourth is -0.5; none survives the pre-specified six-test Holm correction. In an exploratory extension, Mistral Small 4 has a 13.7-point Spanish swap (95% interval [8.4, 18.9]), which survives the twelve-test Holm sensitivity correction under the primary judge, and 12.1 points under a second judge. GPT-5.4-mini estimates are within 2 points of zero. Component assignment supplies an additional evaluation dimension. Evaluations should record component languages and translated text quantity, comparing matched behaviours at equal translated-span count while interpreting refusal and unsafe compliance separately.

---


### 69. [Complementing Text Based Moderation with Multimodal Grounding: Detecting Fraudulent Inducement Behaviors on Short Video Platforms](https://arxiv.org/abs/2610.38185)

**<font color=#1a73e8>作者：</font>** Xiaoyong Yu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Short video platforms have become a primary channel for black and gray industry operations in internet finance, where inducements such as prompts to like, follow, join private chat groups, or click external links frequently steer users toward fraud. Because such videos are short, dynamic, and often convey intent through fleeting visual cues rather than stable text, a moderation system must guarantee detection recall and localize the offending segment so reviewers inspect only the relevant clip. Existing OCR+LLM pipelines transcribe on-screen text frame by frame and classify the transcript, but exploit only textual information. Many inducements are conveyed through visual cues OCR cannot observe, and keyframe-based localization cannot recover precise temporal boundaries. We explore OCR+MLLM, which augments the text pipeline with a Multimodal Large Language Model, and compare three routes: OCR+LLM, OCR+MLLM, and a large zero-shot MLLM, along detection, latency, token consumption, and deployment complexity. OCR preserves the text signal that guarantees recall, while the MLLM jointly performs OCR-grounded discrimination and temporal grounding, localizing both textual and non-textual inducements. We construct a dataset of 2,419 internet finance short videos (66.49 hours) with 3,194 annotated events across four categories, and study reward design for RL-based grounding under class imbalance. We report two findings: auxiliary reward terms are exploited through reward hacking, and stronger localization rewards degrade class-balanced detection. We therefore design a recall-weighted F2 localization reward with class-balanced resampling. Experiments show OCR+MLLM localizes better than the keyframe OCR+LLM baseline (mIoU 26.52 vs. 14.49) and detects non-textual inducements that text-only pipelines miss, while maintaining 67.0 percent macro recall.

---


### 70. [From Natural Language to Real Schematics: An Automated Workflow for Power Electronics Schematic Synthesis](https://arxiv.org/abs/2610.38201)

**<font color=#1a73e8>作者：</font>** Bowen Su, Huan Chen, Jiahua Ying 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Designing power electronics converters traditionally requires intensive human expertise across topology sizing, commercial component selection, circuit simulation verification, and schematic drafting. While Large Language Models (LLMs) show promise in electronic design automation (EDA), applying standalone LLMs directly to board-level power electronics schematic synthesis suffers from severe engineering hallucinations, including inaccurate analytical sizing, fabricated or mismatched component part numbers, violated voltage derating margins, and broken topological connectivity. In this paper, we propose a Bounded Dual-Loop Automated Schematic Synthesis Framework that translates natural language specifications into verified, editable KiCad schematics and manufacturing deliverables. Our workflow integrates six stages across three functional columns: (1) requirement parsing and knowledge-driven power stage synthesis covering non-isolated (Buck, Boost) and isolated/resonant (Flyback, DAB, half-bridge LLC) topologies; (2) contract- and evidence-coordinated component selection grounded in distributor APIs and OEM datasheets, coupled with closed-loop ngspice transient verification and stress feedback; and (3) modular control hardware integration and multi-format deliverable generation featuring native KiCad netlist round-trip verification. End-to-end case studies on a 24-36V to 12V,2A Buck converter (29 positions, 83 verified terminals) and an isolated 48V to 24V, 0.5A, Dual-Active Bridge (DAB) converter (87 positions, 341 verified terminals), alongside comparative evaluations against a Vanilla LLM baseline, demonstrate that our framework improves component verification coverage from 22.2 to 98.6, nominal value consistency from 0 to 97.7, and SPICE simulation pass rates from 0 to 100.

---


### 71. [Two Birds with One Stone: Skill-Augmented Generation via Unified Retrieval and Utilization](https://arxiv.org/abs/2610.38204)

**<font color=#1a73e8>作者：</font>** Zihan Luo, Jiahui Kang, Wei Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Skills, as reusable external knowledge, have demonstrated substantial potential to enhance the ability of Large Language Models (LLMs) to solve complex tasks. However, existing skill-augmented generation methods typically rely on separate models for skill retrieval and skill utilization, resulting in disconnected optimization of these two processes. To address this gap, we propose Skill-Uni, a unified reinforcement learning framework that jointly optimizes skill retrieval and utilization. Specifically, we adopt a generative skill retrieval paradigm that enables a single model to both learn how to retrieve relevant skills and leverage them for task solving. To effectively train this unified framework, we introduce a two-stage training strategy consisting of warm-up instruction tuning and GRPO, allowing the model to progressively improve its skill retrieval and utilization capabilities. Extensive experiments on five skill-related benchmarks demonstrate the effectiveness of Skill-Uni, yielding average performance gains of 66.59% and 34.82% over the base Qwen3-4B and LLaMA3.1-8B models, respectively. Besides, Skill-Uni is compatible with various skill retrieval engines, demonstrating its flexibility and generalizability. Additional in-depth analyses also provide insights into the effectiveness of Skill-Uni.

---


### 72. [Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction](https://arxiv.org/abs/2610.38209)

**<font color=#1a73e8>作者：</font>** Haoran Bu, Yiting Shen, Litian Zhang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLM-based agents now share experiences on social platforms and remember new preferences to enhance their performance. However, existing memory systems contain a vulnerability in role-to-principal attribution that attackers can exploit. We identify Role Grounding Misattribution, in which an attacker-designed interaction causes the victim agent to incorrectly record a preference from the attacker as a preference of the victim's user. Specifically, we are the first to formalize Role Grounding Attack (RGA), an attack model that exploits this vulnerability through nested conversation structures. In the memory formation stage, an experience-sharing post quoting a conversation between the attacker agent and its user is published, which explicitly identifies its publisher. The inner conversation expresses preferences from the user of the attacker agent. When the victim agent remembers preferences from this nested structure, its memory loses the context binding and grounds the attacker's preference to the victim's user instead. In the memory retrieval stage, the misattributed preference persists and influences the victim agent's decisions when it encounters relevant scenarios. We instantiate RGA as tool selection manipulation and privacy leakage. Tool selection manipulation causes a tool-call preference to be misattributed to the victim's user, steering the victim toward an attacker-controlled tool. Privacy leakage extends this by misattributing both a tool-call preference and a task-requirement preference to the victim's user. The victim selects the attacker's tool, then includes sensitive information in tool arguments to satisfy the task requirement. We evaluate RGA across five mainstream memory systems and six language models. Tool manipulation and privacy leakage both achieve high attack success rates. These results call for stronger role grounding.

---


### 73. [GAAC: Lossless KV Compression for Bandwidth-Efficient LLM Inference on Personal Devices](https://arxiv.org/abs/2610.38210)

**<font color=#1a73e8>作者：</font>** Yipin Guo, Arun M George, Siddharth Joshi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Weight-only, lossy quantization substantially reduces the storage and memory requirements for serving large language models (LLMs), but the growing key-value (KV) cache remains a bottleneck for long-context inference on personal devices. We present Group-Adaptive Additive Codec (GAAC), a lossless KV compression and serving system that exploits exponent redundancy to reduce storage and accelerate attention without introducing KV approximation. GAAC encodes BF16 exponents using calibrated per-channel base-plus-offset codes over contiguous ranges. GAAC adapts code widths across small groups while preserving KV values bit-for-bit. A fused attention kernel reconstructs KV tiles on the fly, avoiding full-cache decompression. Block-wise compression and fixed-capacity slots support incremental cache updates and paged serving. Across five tested models, GAAC achieves 1.405-1.407$\times$ lossless BF16 KV compression. We also study compression performance on low-precision tensors FP8 E4M3 caches ( 1.09-1.14$\times$) and E5M2 caches (1.25-1.30$\times$). On NVIDIA DGX Spark, GAAC accelerates decode attention at a 64K-token context by 1.19-1.27$\times$ and end-to-end W4A16 decode steps by 1.04-1.15$\times$. In serving, it reduces resident KV memory by approximately 26% and increases aggregate throughput by 13-29% under comparable KV-memory budgets. On Apple M4, GAAC achieves 1.02-1.25$\times$ attention speedups, demonstrating portability beyond NVIDIA GPUs.

---


### 74. [Disparity Laundering: Consensus Without Fairness in Clinical Multi-Agent Systems](https://arxiv.org/abs/2610.38215)

**<font color=#1a73e8>作者：</font>** Xiaoyang Wang, Tianrui Wang, Christopher C. Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical large language models are increasingly fielded as multi-agent teams, on the assumption that deliberation averages out individual error. It does not average out bias. Across a full factorial of five model families and four aggregation topologies on 120 real MIMIC-IV emergency cases under counterfactual demographic swaps, no configuration neutralizes the disparity: all 20 cells commit the direction of their agents' independent answers, giving Black patients more acute triage. Every model has a topology that amplifies its baseline gap, but which one varies by model, so no design is reliably safe or reliably amplifying: the disparity is relocated, never removed. Late-stage fixes fail: fairness instructions and demographic masking leave the gap untouched, and per-agent self-debiasing widens it, because the bias is already encoded in the agents' ordinary clinical numbers. We call this disparity laundering; the audits now applied to clinical AI, per model, per output, per version, can certify the parts but never the committed decision. Interventions close the gap exactly when they make counterfactual versions visible inside the system and pool them, through deliberation, into the committed decision. A diverse-perspective ensemble does both while keeping the team, with no retraining or architectural change: the disparity falls by 67 to 94% where all five perspectives pool at every round, and the one topology that never pools them is the one it cannot reliably repair. Medical multi-agent systems do not filter demographic bias; they launder it into plausible decisions no single-version audit can catch, and the only defense is to make the bias visible.

---


### 75. [Rubricon: Automated Rubric Generation and Refinement for LLM Evaluation and Training](https://arxiv.org/abs/2610.38220)

**<font color=#1a73e8>作者：</font>** Ulyana Tkachenko, Hui Wen Goh, Guram Gogia 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Rubrics enable reward assignment on tasks without verifiable answers, but are expensive to manually produce from scratch. We present Rubricon, a pipeline that generates discriminative rubrics without requiring human preference labels, rubric annotation, or generator-model training. Using any LLM, Rubricon samples multiple rubrics, selects the most discriminative candidate, adds criteria to capture overlooked requirements or response flaws, and prunes criteria that are misaligned or shallow. Alongside LLM self-critique and test-time scaling, Rubricon uses observed criterion pass rates on example model responses to guide refinement. Across five professional, consumer, clinical, and general-use LLM benchmarks, Rubricon produces rubrics whose scores of frontier LLM responses exhibit 9% greater alignment with labor-intensive expert-authored rubrics, compared to the best alternative synthetic rubric generation method among RRD, QSRG, OpenRubrics, and agentic generation via harnesses like Codex. On HealthBench, post-training a Qwen3.5-9B model with Rubricon rubrics yields 4.5% better performance than training with rubrics from the strongest alternative synthetic rubric generator, RRD.

---


### 76. [3DCodeEdit: Benchmarking Instruction-Guided 3D Program Editing](https://arxiv.org/abs/2610.38231)

**<font color=#1a73e8>作者：</font>** Binjie Wang, Xinran Zhao, Shoubin Yu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models increasingly create 3D content through code, with practical workflows often relying on editing existing programs rather than regenerating them, for speed and precise control. Such edits require understanding what a program builds and foreseeing how a change reshapes it, yet prior benchmarks mostly evaluate generation or simple edits against a reference. In this paper, we introduce 3DCodeEdit, a benchmark of 2,592 instruction-guided editing tasks over 108 Blender programs that construct objects entirely in code. Its edits range from parameter to structural changes, style redesign, and scene composition, and are judged from renders against human-reviewed checklists. Across 17 models, the average success rate is only 37%, and even the strongest models complete fewer than 60% of structural and style edits. As models become more capable, their failures shift to geometric foresight, where the code runs but builds the wrong shape. We therefore study whether multi-turn feedback can compensate for this missing foresight. Feedback from a separate reviewer model that describes how the renders differ from the request helps most, more than maximum reasoning effort or an agent harness, and can let a 27B model surpass the single-shot rate of a 2.8T-parameter model.

---


### 77. [Keepace.ai: A Technical Report on a Large Language Model for Sports and Health](https://arxiv.org/abs/2610.38249)

**<font color=#1a73e8>作者：</font>** Keepace.ai Team, Bowen Wu, Heng Wang 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models hold promise for delivering safe, scientifically grounded, and personalized exercise guidance at scale, yet the sports-and-health domain still lacks curated training corpora and rigorous evaluation benchmarks. this http URL is a domain-specialized LLM built on Qwen3.5-27B through post-training, currently optimized for Chinese-language exercise guidance across three tasks: workout plan generation, sports-and-health knowledge QA, and personal sports data analysis. In internal rubric-based evaluations designed with domain experts, this http URL outperforms its base model and larger general-purpose baselines, with the most pronounced improvements in exercise safety, boundary compliance, structured output completeness, and scientific accuracy. This report summarizes the current design, data pipeline, safety-first evaluation framework, and evaluation results of this http URL.

---


### 78. [ParaTTT: Parallelizing Test-Time Training Layers with Deep Memories](https://arxiv.org/abs/2610.38255)

**<font color=#1a73e8>作者：</font>** Noel Loo, Neehal Tumma, T. Konstantin Rusch 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Test-time training (TTT) layers replace the linear fast-weight memory of modern recurrent architectures with a small neural network trained online by gradient descent. This nonlinear memory is more expressive than the linear memories of Gated DeltaNet and Mamba-2, but is difficult to parallelize: existing implementations such as TTT-MLP rely on sequential, block-wise weight updates that run several times slower than chunkwise-parallel linear recurrences. Moreover, their block-wise execution only approximates the token-by-token online recurrence, whereas linear recurrences admit an exact chunkwise-parallel evaluation. We introduce ParaTTT (PTTT), an algorithm for parallelizing arbitrarily deep nonlinear memories by iteratively refining estimates of the inner-loop gradient trajectory. Starting from a guess of the hidden-layer gradients, each refinement consists of three chunkwise-parallel passes: a forward pass that evaluates the resulting feature trajectory, an exact gated-delta-rule pass that computes the readout trajectory and its feature gradients, and a backward pass that propagates these gradients into a new estimate. The exact online gradient descent recurrence is a fixed point of the iteration, while decoding requires no refinement iterations. We prove geometric convergence for a two-layer variant under sufficient contraction conditions. In practice, two iterations suffice. With two refinement steps at 4K context, PTTT evaluates the inner-loop trajectory $32\times$ faster than TTT-MLP with the block approximation at matched error, while the full 340M model trains $4.9\times$ faster. Models trained at 340M and 1.3B parameters match or exceed Gated DeltaNet and Mamba-2 and remain competitive with same-size Transformers on language-modeling perplexity and zero-shot accuracy, with better recall than the linear recurrences.

---


### 79. [Cross Lingual Abstractive Summarization for Marathi](https://arxiv.org/abs/2610.38267)

**<font color=#1a73e8>作者：</font>** Asang Dani, Shailesh R Sathe  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text summarization is an important task for advancing natural language processing (NLP) research and applications in Indic languages. Despite progress in extractive and abstractive summarization, both monolingual summarization (MS) and cross-lingual summarization (CLS) remain relatively underexplored for these languages. Recent advances in Transformer architectures, pretrained language models (PLMs), and dataset availability offer new opportunities to address this gap. In this work, we construct cross-lingual training data from the monolingual Marathi MahaSum corpus and combine it with the smaller cross-lingual PMIndiaSum dataset to fine-tune IndicTrans2, an Indic neural machine translation model. We evaluate the resulting models using ROUGE, chrF and chrF++ metrics, focusing primarily on Marathi-to-English summarization due to computational constraints. We also discuss the applicability of our approach to the English-to-Marathi direction. Our experiments demonstrate that leveraging a pretrained translation model yields substantially better summarization performance than the IndicBART and mBART-50 based baselines reported in previous work on cross-lingual summarization.

---


### 80. [The Role of Quantization in Loss Spikes](https://arxiv.org/abs/2610.38277)

**<font color=#1a73e8>作者：</font>** Zaiqian Chen, Aditya Somasundaram, Sophie Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Loss spikes in language model pretraining can waste substantial compute and derail otherwise healthy training runs. A primary driver of these instabilities is the growth and divergence of output logits in the final language modeling (LM) head. In this work, we study a particularly costly form of this instability associated with output logit growth: delayed, terminal divergences that emerge only after prolonged training, which we call time-bomb spikes. We find that these instabilities are preceded by rapidly growing quantization error in the LM head, which eventually culminates in a loss spike. Crucially, reducing numerical precision accelerates time-bomb spikes, while increasing precision improves stability. We then propose a simple yet effective mitigation that replaces AdamW on the LM head with SGD with momentum, suppressing logit growth and improving stability over long training horizons. Finally, we find that existing mitigation techniques from the literature (along with our own) all reduce quantization error, suggesting a shared numerical mechanism behind their effectiveness. Together, our results identify finite precision error as a hidden driver of time-bomb spikes and show that suppressing this error is key to stable long-horizon pretraining.

---


### 81. [EPSBench: Benchmarking LLM Agents for Earnings Forecasting](https://arxiv.org/abs/2610.38293)

**<font color=#1a73e8>作者：</font>** Yanbin Yin, Chuyu Xu, Liqin Ye 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Quarterly earnings forecasting requires an agent to connect financial evidence to the income-statement line items that produce a company's reported earnings. We introduce EPSBench, a benchmark for studying this ability across 149 firm-quarters from 86 US companies. Agents read a fixed collection of filings, earnings-call transcripts, and news, then estimate company-specific income-statement drivers with cited evidence. A shared accounting calculator converts these estimates into GAAP diluted earnings per share (EPS), providing a common basis for comparing forecast assumptions. We evaluate six models under a common harness, assessing point forecast error relative to date-matched analyst consensus and checking whether their prediction intervals achieve the stated coverage. Three models show no detectable paired difference in point forecast error from consensus, and three have higher error. Across all six models, nominal 80% intervals contain reported EPS in only 37--70% of runs that return an interval, and most misses fall above the upper bound because the forecasts run low. The driver records trace most of the error gap between models to operating-income estimates.

---


### 82. [Hidden Commitment: When Language Models Silently Pick a Side and How Steering Can Surface It](https://arxiv.org/abs/2610.38296)

**<font color=#1a73e8>作者：</font>** Samuel Dawit Assefa, Jae Won Cho  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Language-model answers are often treated as a visible record of the internal decision that produced them. We test this assumption in conflicting-context question answering, where two supplied documents support incompatible answers. A model can process the disagreement and still return a one-sided answer, even under prompts that ask it to disclose conflict. In Qwen 0.8B, hidden source commitment is captured by a residual source-choice direction whose sign tracks which document the answer uses. Sparse middle-layer MLP writers feed the same coordinate, and steering the coordinate changes the chosen source. A transfer run on Gemma 3 1B preserves the source-choice readout and sparse-write bridge under LLM-audited labels. Conflict disclosure follows a different pattern, appearing weaker, later-layer, and only partially steerable. These results support a practical monitoring strategy for retrieval systems that detects silent source commitment with residual readouts and pairs conflict-surfacing prompts with disclosure steering when the model has selected a side under disagreement.

---


### 83. [Don't Ask the LLM: Visual Token Pruning with Spectral Structure and Semantic Relevance](https://arxiv.org/abs/2610.38303)

**<font color=#1a73e8>作者：</font>** Intaek Shin, Geuntaek Lim, Sungjune Park 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large vision-language models (LVLMs) represent images and videos as long visual-token sequences, substantially increasing inference costs. These costs motivate visual-token pruning, whose effectiveness depends on both what signal is used for selection and when that signal becomes available. Our analysis reveals complementary limitations: visual-side [CLS] attention produces scattered, background-biased selections under aggressive compression, while stronger query-conditioned signals become available after substantial computation within the large language model (LLM). This raises a natural question: can structurally coherent, query-aware token selection be performed before consulting the LLM? We therefore propose ST-Pruner (Spectral-Textual Pruner), a training-free framework for pre-LLM visual-token selection. It combines attention-independent spectral saliency with inverted patch-text similarity through parameter-free multiplicative fusion. Across diverse LVLMs, ST-Pruner retains over 95% of full-token performance using at most 11.1% of visual tokens and achieves a 3.2x end-to-end speedup on LLaVA-NeXT. Code is available at this https URL.

---


### 84. [Robust LLM-Generated Text Detection through Matched Conditional-Response Probing](https://arxiv.org/abs/2610.38312)

**<font color=#1a73e8>作者：</font>** Junfeng Hao, Wenxian Wang, Tao Leng 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable detection of large language model (LLM)-generated text must remain effective under meaning-preserving text revisions, such as rewriting, polishing, and expansion. In practice, LLM outputs are often rewritten, polished, expanded, translated, or lightly edited before publication, weakening the lexical, syntactic, and local discourse cues used by many existing detectors. We introduce \textbf{M}atched \textbf{C}onditional-\textbf{R}esponse \textbf{P}robing (\textbf{MCRP}), a frozen-LLM probing framework that measures how a candidate text responds when a semantically matched condition is introduced, removed, or replaced. For each candidate, the frozen probe LLM first generates a short semantic condition and then compares token-level losses and prompt--target attention measurements under matched, null, and control conditions. It aggregates bidirectional conditioned alignment, counterfactual sensitivity, and internal attention coupling into a probe representation, on which it trains a lightweight supervised random-forest classifier while keeping the probe LLM frozen. Across standard detection, robustness to meaning-preserving text revisions, multilingual, and multidomain evaluations, MCRP achieves consistently strong performance. Under rewriting, polishing, and expansion, it reaches 93.97\% F1 and 96.24\% ROC-AUC, outperforming the strongest evaluated baseline by 19.50 and 25.77 percentage points, respectively. Component ablations show that the response feature groups make complementary contributions to predictive performance. In the condition-control study, matched conditions consistently outperform random, mismatched, and corrupted alternatives, demonstrating a measurable incremental benefit from semantic matching.

---


### 85. [CHORD: Cross-Model Hallucination Detection via Relational Graph Discrimination](https://arxiv.org/abs/2610.38314)

**<font color=#1a73e8>作者：</font>** Yongxin Deng, Zhen Fang, Guansong Pang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hallucination detection is critical for deploying large language models (LLMs) in real-world applications. Due to strong empirical performance, internal representation-based methods have emerged as the prevailing direction for detecting hallucinations, yet they remain largely model-specific and often fail to generalize to unseen LLMs. In this paper, we study an important yet underexplored problem, termed cross-model hallucination detection (CMHD), which aims to train hallucination detectors on source LLMs while ensuring performance on unseen target LLMs. The core challenge of CMHD lies in cross-model representation heterogeneity: hidden states from different LLMs exhibit severe semantic inconsistency, which limits the transferability of classical representation-based detectors. Through analysis and empirical validation, we show that relational structures over layers, tokens, and features capture transferable detection signals despite semantic inconsistency. Based on this observation, we propose cross-model hallucination detection via heterogeneity-oriented relational discrimination (CHORD), a relational graph discrimination framework that represents hidden states as joint relational graphs over layers, tokens, and features. It feeds these graphs into relation-aware attention to obtain structure-aware features, and uses meta-learning to shape these features toward transferable detection signals. Extensive experiments show that CHORD outperforms representative detection methods in cross-model generalization. Code is available at this https URL.

---


### 86. [Can LLMs Faithfully Solve Ontology Engineering Tasks? A Mechanistic Interpretability Study](https://arxiv.org/abs/2610.38326)

**<font color=#1a73e8>作者：</font>** Bohui Zhang, Albert Meroño-Peñuela, Elena Simperl  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ontological knowledge underpins large language model (LLM) performance on knowledge-intensive tasks. However, existing evaluations of LLMs' ontological understanding largely rely on behavioral correctness, leaving the underlying mechanisms unexplained. Existing mechanistic interpretability work has largely focused on instance-level factual knowledge, leaving ontological knowledge under-explored. To bridge this gap, we introduce MIOE, a causal-abstraction benchmark that evaluates interchange interventions for two ontology engineering tasks: entity typing and subsumption prediction. MIOE tests whether learned internal intervention targets can change an ontology-level target answer while preserving class-specific auxiliary information. Across Qwen3-8B and Qwen3-4B, we evaluate SAE-, DBM-, and DAS-based methods, including multi-task and multi-layer variants. Distributed subspace methods give the strongest results and generalize across prompt settings, but the induced changes remain only partially separated from auxiliary class-specific information. Multi-task objectives and contiguous layer-window interventions improve this balance, while class-level analyses reveal substantial variation across ontology classes. These results suggest that ontological predictions are mechanistically accessible in LLMs, although current methods do not yet isolate a cleanly disentangled causal mechanism for ontological knowledge.

---


### 87. [A Case Study of a Multi-Agent Kernel-Optimization Loop That Learns a New AI Accelerator](https://arxiv.org/abs/2610.38329)

**<font color=#1a73e8>作者：</font>** Byonggon Chun  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier large language models write correct CUDA kernels for most single-operator benchmark tasks, yet their accuracy collapses on accelerators whose architecture and programming language they have rarely seen. We present a case study of an LLM agent loop built for such accelerators. Our example is the FuriosaAI RNGD NPU, programmed in a recent, sparsely documented Rust DSL, where the loop optimized three Gemma-4-12B decode kernels over 12 days on a shared, scarce device. The loop builds its own target knowledge: it writes and checks a summary of the DSL documentation, measures the chip with microbenchmarks, records compiler-derived legality rules, and revisits this knowledge when the toolchain changes, rechecking rules and measurements where it can. A role-based search over per-kernel Design Trees explores whole-kernel designs and accumulates small accepted changes in the best version of each kernel. Because device time is scarce and readings are noisy, cheap checks screen new designs before any device run, and late in the run a change was accepted only after repeated comparisons with the best kernel on the device. The final kernels reach a 9.293x geomean speedup over the official baseline, each within 1.25x of the cycles needed just to move its weights. Our prompts, profiler and acceptance test are available at this https URL.

---


### 88. [Multi-Token Prediction Done Right](https://arxiv.org/abs/2610.38331)

**<font color=#1a73e8>作者：</font>** Jayden Teoh  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Multi-Token Prediction (MTP) is now a common ingredient in language-model pre-training, as it improves downstream performance and enables faster inference through speculative decoding. We identify a flaw in standard MTP training, in which a residual component of the MTP gradient interferes with both next-token and multi-token learning, increasingly so with scale. Specifically, the MTP cross-entropy gradient can be decomposed exactly into a KL self-distillation term that pulls each MTP head toward the model's own next-token prediction (NTP) distribution and improves speculative decoding, and a residual that has a low signal-to-noise ratio and buries the useful KL signal. We introduce the KL gradient-recovery trick: when two distributions share a linear output head, the gradient of their KL divergence can be recovered exactly by combining their cross-entropy gradients through straight-through gradient routing. Unlike minimizing the KL directly, this trick requires no vocabulary-sized logit matrices and is compatible with standard fused cross-entropy kernels. This enables Soft Multi-Token Prediction (Soft-MTP), a one-line code change to MTP that removes the noisy residual and backpropagates only the KL self-distillation signal by reusing the existing NTP and MTP cross-entropy computations. Soft-MTP supports both DeepSeek- and Meta-style MTP, adds no parameters, and incurs no measurable overhead. From 167M to 1.2B parameters, Soft-MTP improves over standard MTP with lower NTP perplexity, faster speculative decoding and higher zero-shot accuracy at every scale, lower MTP perplexity from 689M onward, and stronger math and code reasoning after fine-tuning at 1.2B. Soft-MTP also matches, if not exceeds, direct KL divergence minimization on most metrics. Soft-MTP is, in effect, a free lunch for MTP optimization. Our code can be found at this https URL.

---


### 89. [MUSE: Multi-Level Memory with Selective Runtime Injection for Scientific Coding Agents](https://arxiv.org/abs/2610.38332)

**<font color=#1a73e8>作者：</font>** Haoran Jin, Defu Lian, Xiting Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Historical experience can guide scientific coding at multiple levels, but task-level retrieval may miss implementation lessons that become relevant during execution. We introduce MUSE, a memory management framework combining multi-level memory with selective runtime injection for scientific coding agents. MUSE builds global, approach-level, and implementation-level memory from historical trajectories. At initialization, the agent receives global memory and problem-matched approach-level memory. During execution, current interactions are used to retrieve implementation-level memory. An LLM gate selects relevant experience and generates specific review advice, or skips injection. Across four benchmarks spanning numerical problem solving, kernel optimization, and scientific software repair, MUSE outperforms retrieval and memory baselines on all evaluation metrics. Ablations support the multi-level design and gated injection, while transfer experiments show that memory remains useful across kernel benchmarks. These results show that multi-level memory and selective runtime injection enable effective reuse of experience in scientific coding. Code is available at this https URL.

---


### 90. [Fu-TCM: a multimodal large language model that learns traditional Chinese medicine diagnostic reasoning](https://arxiv.org/abs/2610.38333)

**<font color=#1a73e8>作者：</font>** Jiahang Xie, Tong Jin, Lingfei Wu 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are advancing in multimodal understanding and reasoning, accelerating medical model development. Traditional Chinese medicine (TCM) uses evidence from the four examinations to determine disease location and nature, differentiate syndromes and guide treatment. This diagnostic process constitutes a complete chain of reasoning. We present Fu-TCM, a multimodal TCM LLM trained on data retained after cleaning and filtering an initial collection of approximately 7.12 million examples derived from classical texts, textbooks, medical images, clinical cases and publicly available datasets. The model was further optimized using Bianzheng-Grounded Policy Optimization (BGPO), which explicitly targets syndrome differentiation through rewards for response format, intermediate TCM reasoning fields and final syndrome predictions. Fu-TCM-27B led all six benchmarks spanning TCM reasoning, text and vision, achieving a macro-average accuracy of 81.01% and surpassing the strongest reference model with complete results across all six benchmarks by 7.13 percentage points. Its largest margin was 11.90 points on Fu-bianzheng. Case-level analyses further showed a positive association between intermediate-field accuracy and final syndrome-selection accuracy in most evaluated models. These findings suggest that TCM syndrome differentiation may be computationally learnable and that structured reasoning supervision can improve performance across TCM tasks.

---


### 91. [Learning a Prior-Data Fitted Network for Graph Foundation Models via Structural Causal Model Priors](https://arxiv.org/abs/2610.38335)

**<font color=#1a73e8>作者：</font>** Ziwei Zhang, Tianyin Liao, Chunyu Hu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Graph Foundation Models (GFMs) have recently emerged as a promising paradigm for learning transferable representations across different graphs and domains. However, existing GFMs face notable limitations, including limited pre-training scale or reliance on aligning with textual information in Large Language Models (LLMs). To overcome these limitations, recent studies have drawn inspiration from prior-data fitted networks (PFNs), which learn from large synthetic datasets and support multi-domain prediction backed by causal learning. However, existing graph PFNs encounter severe difficulties in modeling causal relationships within and across node and edge sets, generating diverse graph structures, and designing suitable architectures that can learn from complex synthetic datasets. To address these challenges, we propose **GSCM-PFN** (Graph SCM-based Prior-Data Fitted Network), a graph PFN pre-trained on synthetic data generated from an SCM-based prior that jointly models nodes and graph topology. Specifically, we (1) design a joint feature-edge-label structural causal model (SCM) to guide synthetic graph generation and capture causal relationships within and across node and edge sets; (2) introduce prior-guided node-edge dependency modeling to instantiate diverse graph generation strategies, and prove that our SCM-based generation prior is more expressive than existing priors; and (3) propose a feature-permutation-invariant dual-path graph network with theoretical guarantees for learning from diverse synthetic graphs. Experiments on 23 real-world benchmarks show that GSCM-PFN outperforms both conventional GFMs and PFN-based GFMs, without utilizing real-world graph data for pre-training. Code: this https URL

---


### 92. [Statutory Article Retrieval from Arabic Judicial Narratives: Family Law and Law of Evidence in Saudi Arabia](https://arxiv.org/abs/2610.38336)

**<font color=#1a73e8>作者：</font>** Zarah Shibli, Areej Alhothali, Lulwah Alharigy  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliable legal information retrieval must ground legal reasoning in authoritative statutory sources. In Arabic judicial settings, long factual narratives must be mapped to concise articles that express abstract legal rules, creating a narrative-to-legal-rule abstraction gap. Using a benchmark of 200 synthetic Saudi Arabic judicial cases and 381 articles from the Family Law and the Law of Evidence, we compare word-level and char-4 BM25, zero-shot dense encoders, per-law retrieval, dense-sparse reciprocal rank fusion (RRF), and a proposed Decompose-and-Refine (DaR) pipeline. In DaR, a large language model splits each narrative into disputed legal issues and generates, for each issue, three retrieval channels: a statute-style paraphrase, legal keywords, and a candidate taxonomy chapter. On the whole corpus, the instructed Qwen3-Embedding-8B dense encoder reaches an MRR@10 of 0.849, the best result of any non-decomposed system. Under per-law scoring, this advantage reflects Family Law only: restricted to Evidence articles, the same encoder drops to an MRR@10 of 0.087, and fusion with BM25 raises it only to 0.207. DaR changes this picture, raising Evidence MRR@10 to 0.696 and Family MRR@10 to 0.864. Without decomposition, the two laws favor different strategies; under DaR, the same retriever achieves the best MRR@10 on both.

---


### 93. [Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?](https://arxiv.org/abs/2610.38342)

**<font color=#1a73e8>作者：</font>** Huangfei Jiang, Anning Hu, Kai Sheng 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Financial agents must form forecasts and investment judgments from decision-time evidence, with predictions evaluated against subsequent outcomes. Existing benchmarks assess financial knowledge, research workflows, or forecasting, but evaluating the full research process requires a strictly frozen information set and professional evaluation criteria. We introduce Investor's Last Exam (ILE), an equity-research benchmark led by experienced buy-side investors and fund managers. Its three components are a versioned financial database spanning 3.43 million document versions and nine source categories, supplemented by structured market data, with validated timestamps governing retrieval and computation; a task taxonomy organized around professional analyst deliverables; and an expert-led framework linking scoring criteria to sources, calculations, and assumptions through financial dependency graphs. Evaluation spans 86 assignments and jointly assesses research quality, forecast accuracy, and simulated investment performance. GPT-6 Astra and Claude Opus 5.5 lead overall at 68.1 and 66.9 out of 100, yet even Astra scores only 52.5 on Forecast & Model. Our results show that even state-of-the-art models fail to translate overall research capability into predictive performance. ILE shifts the evaluation unit from isolated capabilities to the evidence--assumption--judgment chain, allowing researchers to locate where analytical advantages fail to translate into forecasts and investment judgments, and providing a traceable, diagnostic foundation for training and evaluating financial agents.

---


### 94. [Knowledge-structured and evidence-aware semantic self-distillation for glomerular pathology foundation model](https://arxiv.org/abs/2610.38346)

**<font color=#1a73e8>作者：</font>** Qiming He, Jing Li, Zihan Wang 等 27 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual foundation models learn rich pathological morphology but lack explicit concept-level supervision. Vision--language pretraining can provide this supervision but requires costly image--text pairs. Here, we introduce GloSAGE, a semantic self-distillation framework that uses lesion profiles predicted by a pretrained visual teacher to construct structured pathology descriptions. Reliability-guided selection identifies image--text anchors, while Knowledge-Structured Pathology Text Synthesis and Evidence-Guided Negative-pair Construction account for partially observed lesions. Image--text alignment trains projection layers while retaining the frozen visual encoder; an intermediate Semantic Transfer Layer supplies features for downstream tasks. Developed on GloMillion and evaluated across seven glomerulus- and case-level cohorts, GloSAGE supported zero-shot lesion recognition, image--text retrieval, hard-negative discrimination and concept-intervention analyses. It outperformed its source visual model in most lesion-recognition tasks and improved lesion grading, while supporting competitive case-level disease classification, injury grading and baseline renal function estimation. Ablations supported the combined contributions of knowledge-structured text and evidence-guided negatives, and the intermediate transfer layer improved mean lesion-recognition ROC-AUC relative to the complete projection output. A frozen language model conditioned on GloSAGE features generated glomerular descriptions. These findings suggest that teacher-derived lesion profiles can provide annotation-efficient semantic supervision for extending a glomerular visual foundation model.

---


### 95. [WeVisCut: The Whole Editing Room in One Agent From Narration to Long-Form Video](https://arxiv.org/abs/2610.38352)

**<font color=#1a73e8>作者：</font>** Chenyu Mu, Wenming Weng, Qinrui Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Producing long-form videos from narration requires interdependent decisions that remain coherent across shots. Existing agentic editors often use multi-stage workflows driven by general models, leaving the quality-cost trade-off of compact, task-adapted policies unclear. We address this gap with WeVisCut, a long-form script-to-video system that connects tool execution with policy learning. Its agent harness maintains shared production state so that tool feedback informs subsequent decisions and repairs. Because finished videos do not expose these decisions, our four-stage data pipeline combines editing inversion with verified replay to turn recovered editing intent into executable supervision. Applied to 3,750 finished videos, this pipeline yields over 130K training examples. We use this supervision to train a single 9B policy that coordinates production and recovers from failures within the same harness. Moreover, we introduce a 100-task benchmark and five metrics assessing editing quality and delivery reliability. Under a shared tool environment, WeVisCut substantially outperforms its base model and achieves comparable performance to Claude Opus 5 while using nearly 33x fewer generated tokens per successful output minute. It also outperforms task-matched native editors on our proposed metrics.

---


### 96. [Encode Once, Answer Many: Internalizing Context via Parametric Flow](https://arxiv.org/abs/2610.38356)

**<font color=#1a73e8>作者：</font>** Xinhao Zhong, Mengxuan Wu, Chonghua Liao 等 25 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models are typically adapted to a task either by placing knowledge in the input context, which keeps it external and re-encodes it on every call, or by fine-tuning, which internalizes it but demands a costly round of optimization per task. We aim to internalize the knowledge carried by a context directly into model parameters, without per-task optimization and without keeping the context in the input at inference time. To this end, we propose CLIK, a context-conditioned parameter generator that maps a given context to LoRA parameters for internalizing knowledge in a single forward pass through a Transformer encoder with cross-attention, requiring no test-time gradient updates. Once the generated LoRA is inserted into a frozen base model, the model answers downstream queries from the query alone, having internalized the context into its weights rather than re-reading it. Because the adapter depends only on the context, it is generated once and reused for every query on the same document, so the cost of reading that document is amortized across queries. On document question answering, CLIK substantially improves over the no-context base model and outperforms existing hypernetwork-based generators, while remaining behind a base model that reads the context directly, and it carries over to multi-turn dialogue without any multi-turn-specific training. Analysis further shows that the context-dependent part of the generated adapter concentrates in a compact and specific substructure.

---


### 97. [Manifest-Assisted Retrieval in Artificial Intelligence Search: Evidence Gaps and a Security Evaluation](https://arxiv.org/abs/2610.38361)

**<font color=#1a73e8>作者：</font>** Gangzhen Qian, Kainan Zhou, Chuhong Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The external sources retained in our non-systematic audit did not isolate the incremental security or utility effect of consuming /llms.txt while ordinary retrieval remained fixed. The initial audit covered 39 sources through August 16, 2026, with later targeted updates through October 14. A purposive 15-tool study observed no automatic requests in 45 trials at one endpoint; a non-probability log study found that 97% of domains with detected files received no recorded requests in May 2026. We separate publication, fetch, model use, and action; define five operational threat paths and paired security-utility estimands; and exercise deterministic pre-model controls with 30 author-defined parser fixtures. We also execute a reduced pilot: 24 tasks across eight sites, five conditions, and 120 real model responses, with ordinary evidence held fixed. Frozen automatic scoring identifies attacker-target adoption in $21/24$ raw adversarial responses, with one further response unresolved; the adversarial URLs-only condition has no known adoptions and one unresolved response. The pilot measures output changes conditional on supplied evidence, without live retrieval or external actions. Together, the framework and pilot distinguish manifest-content effects from publication, discovery, and downstream execution, while leaving full retrieval and agent evaluation open.

---


### 98. [TCC-RAG: Temporal Causal Chain-Guided RAG for Temporal Knowledge Graph Question Answering](https://arxiv.org/abs/2610.38366)

**<font color=#1a73e8>作者：</font>** Xinxun Zhang, Yuxiang Wang, Shanshan Feng 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have spurred growing interest in temporal knowledge graph question answering (TKGQA). Most existing methods rely on semantic retrieval augmented generation (RAG), which suffers from fundamental limitations in complex temporal reasoning. On the one hand, semantic-based RAG methods struggle to capture the multi-hop causal knowledge required for complex temporal reasoning. On the other hand, these methods introduce excessive redundant knowledge, trapping LLMs in spurious reasoning chains that potentially result in erroneous answers. To address these problems, we propose a Temporal Causal Chain-guided RAG (TCC-RAG) to retrieve a concise yet sufficient set of causal knowledge to support complex temporal reasoning. Specifically, we reformulate the temporal knowledge graph into a multi-view causal cue graph, with causal cues inducing connections that explicitly encode temporal evolution and causal dynamics. Based on the causal cue graph, we construct a query-specific temporal causal chain to guide the retrieval process, enabling the model to focus on a concise set of causally relevant knowledge. Finally, we introduce a causal evidence filter to refine the retrieved knowledge, ensuring its causal consistency with the underlying temporal logic of the query. Experiments show that TCC-RAG achieves substantial performance gains of 10.72% and 8.40% on two TKGQA benchmarks, and delivers a remarkable 62.97% improvement for multi-step temporal reasoning.

---


### 99. [Compute Has Shape: Self-Morphing the Internal Computation of Frozen LLMs](https://arxiv.org/abs/2610.38382)

**<font color=#1a73e8>作者：</font>** Junxi Wu, Yiwen Guo, Shu-Tao Xia  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Test-time scaling improves large language models through additional computation, but how to adapt the topology of internal computation to individual inputs remains underexplored. Existing approaches largely fix recurrent or parallel architectures during training, or reconfigure frozen models along a single structural axis. We introduce SelfMorph, which makes computational shape an input-dependent inference-time decision. It unifies the original forward path (BASE), serial reuse of a layer span (REPEAT), and local branching and merging of perturbed hidden states (BRANCH) in a unified space parameterized by type, location, and intensity. Since they offer complementary benefits rather than uniform dominance, we use a lightweight selector that reads the backbone's depth-wise hidden state trajectory on the prompt to choose a morphology before response generation. We train the selector by distilling utility-based distribution from offline morphing that jointly account for task performance and computational cost. Evaluated on three LLMs spanning 4B-27B, SelfMorph achieves a 8.06% mean relative improvement on five in-distribution benchmarks and 4.45% on four unseen benchmarks. It achieves the strongest performance in 24 of 27 settings. These findings identify input-adaptive computational topology as a complementary axis of test-time scaling beyond generating more tokens. Our code is available at this https URL.

---


### 100. [How Much Do Teacher Bridges Matter in Interleaved On-Policy Distillation?](https://arxiv.org/abs/2610.38383)

**<font color=#1a73e8>作者：</font>** Leran Chen, Zhiyuan Yao, Lingnan Kong  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student using teacher predictions on student-generated responses. Some methods insert teacher-written segments, or bridges, but disagree on how to train on those tokens. We compare no loss, forward KL and reverse KL on identical trajectories using Qwen3-1.7B as student and Qwen3-4B-Instruct-2507 as teacher. We separate gradients by which model wrote each token. Under our short training runs and BF16 inference, pre-specified tests detected no added accuracy benefit from teacher text as context or as a training target. A one-paragraph bridge after the student's first paragraph is only 2.7% of the tokens and contributes a small gradient nearly orthogonal to the student-token gradient. In this main comparison, the three loss treatments gave similar gradient directions and were statistically equivalent in accuracy within a +/-5 percentage-point margin. An exploratory pilot placing the bridge where failed responses disagreed most with the teacher suggested a benefit from teacher-token loss. A pre-specified replication did not confirm this, and fourfold weighting showed no significant accuracy benefit. Two limitations bound these findings. Among the tested amounts of training on fixed responses, gains peaked after four updates before the student increasingly failed to stop generating. None of the tested online training variants met the criteria for stable stopping and improved accuracy. Our evaluations used BF16 inference, which rounds away most of the small weight changes. When evaluated in exact FP32, the tested replication models frequently reached the response-length limit. Our accuracy findings therefore concern BF16 inference; they do not establish that teacher-token supervision is generally unnecessary.

---


> [!TIP]
> 当前位于：**51-100**（第 2/8 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | **51-100** | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-353](./part-08.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
