# 🧠 大模型相关研究 | 2026年09月04日

> 本类共 **177** 篇论文：已确认 **170** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-177](./part-04.md)

---

### 1. [WMLLM: Self-Evolving Optimization Agents via Predict-Then-Act World Modeling](https://arxiv.org/abs/2609.01608)

**<font color=#1a73e8>作者：</font>** Zhongzheng Li, Qingsong Ran, Shikun Feng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Black-box optimization problems remain challenging because of large, weakly structured, and high-dimensional search spaces. Existing methods often suffer from poor sample efficiency because they rely on direct candidate generation or trial-and-error refinement. A natural way to improve search efficiency is to use world modeling, which can help identify promising optimization directions before costly evaluation. Large language models can predict the outcomes of these candidates with nontrivial accuracy because of their implicit knowledge. Motivated by this observation, we propose WMLLM, a self-evolving optimization-agent framework based on predict-then-act world modeling. The agent first predicts promising directions and then acts to generate candidates. Combined with agentic multi-turn refinement, population-based search, and reinforcement learning, WMLLM refines both its implicit world model and its optimization strategy during search. Experiments on black-box optimization tasks, especially multi-objective molecular optimization, show that WMLLM improves sample efficiency and final optimization performance. On the multi-objective molecular optimization benchmark, WMLLM achieves state-of-the-art results under a limited evaluation budget.

---


### 2. [EvalDetectBench: A Benchmark for Measuring Evaluation Awareness in Frontier Language Models](https://arxiv.org/abs/2609.01611)

**<font color=#1a73e8>作者：</font>** Xinning Li, Kemunto Ochwang'i, Aryasomayajula Ram Bharadwaj 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier large language models can often recognize when they are being evaluated, a capability known as evaluation awareness. If models behave differently in evaluations than in deployment, this undermines the validity of evaluation results, which are a crucial component of current AI safety frameworks. We introduce EvalDetectBench, an open pipeline and benchmark for measuring evaluation awareness that works with any Inspect-compatible evaluation, allowing practitioners to test against current and future benchmarks. EvalDetectBench ships with a newly curated transcript suite covering current frontier system-card evaluations and diverse deployment sources. The benchmark serves two purposes: measuring how reliably frontier LLMs recognize that they are being evaluated, and assessing how detectable individual benchmarks are as evaluations. We identify two methodological choices in the existing literature that introduce systematic bias: the identity of the model that generated the deployment transcripts accounts for 11.25% of measurement variance and can reorder model rankings; and elicitation prompts selected for high performance on one model can perform near chance on others. EvalDetectBench corrects for both via per-model probe calibration and a stratified generator-harmonisation procedure.

---


### 3. [Prompt-Space Meta-Learning Does Not Transfer Across Users: A Frozen-LLM Negative Result](https://arxiv.org/abs/2609.01615)

**<font color=#1a73e8>作者：</font>** Liam Byrne, David Dylan, Orla Fitzgerald 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Personalizing a frozen large language model (LLM) to individual users is often framed as a meta-learning problem in prompt space: each user is a task, and one seeks a shared natural-language adaptation policy that, given a handful of the user's labeled interactions, configures the frozen model for that user. The framing is attractive because it is backbone-agnostic and reuses the machinery of prompt optimization, yet the field rarely tests whether the optimized meta-objective encodes transferable cross-user adaptation rather than generic instruction quality. We study this question with Muse (Meta-learned User-adaptation via Shared Evolution), which evolves a single shared adaptation prompt over a meta-train user population by reflective prompt evolution, freezes it, and applies it zero-shot to held-out users; matched controls isolate learning from confounds of phrasing and selection. On two standard personalization benchmarks (LaMP-2 categorization and LaMP-3 rating) over 200 held-out users each, Muse does not significantly improve on its own un-evolved seed prompt or on a structure-broken control that meta-trains on mismatched user-support pairs, and is dominated by plain few-shot retrieval on the rating task (Delta MAE +0.175, p < 0.001). We attribute these outcomes to a single mechanism, meta-objective collapse: the meta-validation objective is statistically invariant to whether the user-support correspondence is genuine (p=0.555 on LaMP-2, p=0.622 on LaMP-3), so it cannot be optimized into transferable adaptation and instead rewards instruction polish and validation overfitting. The seed-prompt, wrong-support, and invariance-oracle controls form a reusable protocol that separates learned adaptation from these confounds.

---


### 4. [PRO-Step: Step-level Process Reward Optimization for Retrieval-Augmented Generation](https://arxiv.org/abs/2609.01658)

**<font color=#1a73e8>作者：</font>** MinKeon Kim, Namjun Lee, Jaekwang Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation enhances Large Language Models by grounding responses in external knowledge, but multi-hop reasoning remains vulnerable to error propagation, where early retrieval failures confound subsequent steps. Standard outcome-based optimization only rewards the final answer, leaving intermediate retrieval and reasoning errors undetected. While existing process-based methods introduce step-level signals, they still score each step against the final answer, rewarding spurious successes where flawed retrieval coincidentally produces the correct answer. Step-level supervision in RAG requires evaluating both logical validity and evidential grounding at each step. We introduce PRO-STEP: we train a generative PRM that evaluates both dimensions, employ PRM-guided value tree search to construct preference pairs contrasting valid steps against flawed ones, and optimize the policy via step-level Direct Preference Optimization. Experiments on single and multi-hop QA datasets demonstrate that PRO-STEP achieves the best average EM and F1 across five benchmarks. Code, models, and training data are publicly available at this https URL.

---


### 5. [Beyond Textual Chain-of-Thought: A Survey on Action-Grounded Reasoning in Autonomous Driving](https://arxiv.org/abs/2609.01659)

**<font color=#1a73e8>作者：</font>** Zhengxu Tang, Xiaozhou Zhang, Guofeng Cui 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought (CoT) reasoning powers generative models by eliciting intermediate steps before producing an answer. In autonomous driving, the answer is a continuous action. Thus its reasoning must share the same spatiotemporal structure as the physical world. This survey studies the resulting shift from textual CoT to action-grounded reasoning. Surveying 171 papers, including 130 method papers and 41 benchmarks, datasets, surveys, and analysis papers, we propose a representation-centered taxonomy that treats the form of the intermediate state as the organizing axis. We systematize the 130 methods into four categories: language-based, visual-spatial, latent-dynamic, and externalized reasoning, further divided into 13 subtypes tied to distinct regions of interests. Our synthesis shows that the open frontier of reasoning in driving agents lies in intermediate representations that can be grounded in the real world, coupled to real-time action, and verified under safety-critical systems. Project page: this https URL.

---


### 6. [Ranked by the Matcher: A Reproducibility Audit of Knowledge Graph Extraction from Threat Reports](https://arxiv.org/abs/2609.01671)

**<font color=#1a73e8>作者：</font>** Safayat Bin Hakim, Houbing Herbert Song  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Security teams and researchers choose knowledge-graph extraction tooling for threat reports on the strength of published triple-F1 scores, yet those scores depend on how predicted triples are matched to gold annotations. We could reimplement the stated matching rule for only five of twelve inspected systems. Re-scoring ten system outputs on shared documents under eight protocols reverses eleven of forty-five pairwise orderings; one fixed prediction set spans 0.16-0.70 F1. On GRID's external 378-item calibration set, no mechanical matcher (lexical, embedding, or entailment) agrees with multi-reviewer adjudication above 71%, whereas an LLM judge reaches 86%. To separate component effects from matcher rewards, we build CTIForge, whose deterministic validation layer can vary while extraction is held byte-identical. Across seven tested deployment configurations, validation raises precision for all four hosted backbones and lowers it for all three offline backbones. Because backbone, decoding, and backend-specific prompting covary, this is a descriptive split rather than an isolated serving effect. It coincides with a roughly 2.8-fold increase in actions explicitly disputing entity type, consistent with hand-written rules encoding the conventions of the extractor against which they were developed. We release the pipeline, protocol suite, and per-triple audit records.

---


### 7. [Skill-as-API: Confidential Multi-Agent Coordination for Agentic Software Engineering](https://arxiv.org/abs/2609.01677)

**<font color=#1a73e8>作者：</font>** Ziwei Zhao, Yu Gu, Haojun Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> AI coding agents are evolving from solitary tools into collaborative teammates that discover and invoke one another's specialized skills. But the coordination channel itself can leak a skill's intellectual property. Protocols such as MCP and A2A run implementations server-side, yet they still publish each skill's description and typed schemas to every peer, offer no way to hide a skill's existence, and cannot guarantee that a wrapped system prompt stays off the wire. Application-layer privacy filters help, but act only after the model has decided to emit sensitive text. We take a complementary, protocol-layer route: Skill-as-API, a coordination protocol whose public view of a skill is limited to its name, description, typed input/output schemas, and trust tier. The skill body is closure-captured in the owner's process and never crosses the wire. Four layers add access control and narrow the prompt-injection surface structurally rather than by filtering content. We provide an open-source Python implementation over XMTP with 1.8-2.9 s cross-continent hot-reconnect latency, and a software-engineering case study in which three agents coordinate a pull-request review while each retains ownership of its proprietary analysis prompts.

---


### 8. [Learning Evidence Sufficiency Boundaries for Selective Answering in Grounded Multi-Hop QA](https://arxiv.org/abs/2609.01687)

**<font color=#1a73e8>作者：</font>** Haruto Sato, Yuki Tanaka, Ren Nakamura 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grounded question answering systems should answer only when the supplied evidence supports the answer. In multi-hop QA, this requirement is difficult because partial evidence can make an unsupported answer appear plausible. We study selective answering through evidence sufficiency boundaries: for the same question, a model should abstain under unsupported or partially supported context, answer when the context first becomes sufficient, and keep the answer stable when redundant evidence is added. We introduce Evidence Sufficiency Boundary Training, a generation-native training framework that constructs ordered evidence chains and supervises the abstain-to-answer transition directly. The method combines level supervision, a boundary flip margin, post-boundary stability, and answer recall protection. We build evidence chains from HotpotQA, 2WikiMultiHopQA, and MuSiQue, then evaluate models with chain metrics, raw QA utility, and unsupported-answer rates on external non-answerable sets. With Qwen2.5-3B-Instruct and LoRA adaptation, Evidence Sufficiency Boundary Training gives the strongest boundary localization among the tested systems, with flip accuracy of 0.807 compared with 0.781 for a token-level abstention baseline. It also achieves the lowest overall unsupported-answer rate on external non-answerable evaluation, 0.095 compared with 0.101 for the same baseline, while retaining competitive raw QA F1. The results show that grounded selective answering improves when training marks the evidence level where refusal should give way to answering.

---


### 9. [FairLens: Benchmarking Fairness in Vision-Language Models for High-Stakes Decision-Making](https://arxiv.org/abs/2609.01691)

**<font color=#1a73e8>作者：</font>** Vahid Reza Khazaie, Ahmed Y. Radwan, Shaina Raza  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly used to make decisions from visual inputs. We introduce FAIRLENS, a benchmark and evaluation framework for measuring both the fairness and the validity of VLM responses in three high-stakes domains: hiring, legal, and healthcare. FAIRLENS pairs real face images spanning gender, race, and age groups with closed- and open-ended questions, giving more than 100K image-question pairs per model, and evaluates responses from four complementary views: demographic parity over adverse outcome rates, soundness, demographic association over unsupported roles and statuses, and bias in free-text generation. Soundness is the central validity criterion: a response is sound when it follows the evidence stated in the question and abstains when the image cannot support an answer. Evaluating eight VLMs, we find that the primary failure is unwarranted inference rather than unequal treatment. Models routinely infer qualifications, threat, illness, or professional role from a face instead of abstaining, and the weakest model does so on 99% of the questions its input cannot answer. These failures are most severe in legal and healthcare, where recognizing insufficient evidence matters most, and disparity metrics alone would miss them: parity gaps are small in absolute terms, yet when baseline adverse rates are low the same gap means one demographic group receives adverse labels several times as often as another, and a small gap can equally reflect a model that treats every group unsafely. Bias in free-text responses is only loosely coupled to multiple-choice accuracy, so correct structured answers do not imply safe generation. FAIRLENS shows that fair high-stakes VLM behavior requires similar treatment across groups and refusal to infer high-stakes attributes from appearance, and its question suite transfers to any face corpus with demographic annotations.

---


### 10. [Public-Sharing Labels and Verbatim Field Egress in an MCP-to-A2A Agent Configuration: A Controlled Multi-Model Study](https://arxiv.org/abs/2609.01693)

**<font color=#1a73e8>作者：</font>** Arpan Kumar Mahapatra  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety properties assessed separately for Model Context Protocol (MCP) tool use and Agent2Agent (A2A) delegation need not describe behavior when one agent uses both. We measure one such behavior in a single controlled MCP-to-A2A configuration: a testbed drives a real-model host across a local MCP and a local A2A leg into an ordered event trace scored by exact deterministic rules (no LLM judge), one restricted decision per trial. In a pre-specified, frozen three-arm design, each of 10 record scenarios appears with a CONFIDENTIAL header, with no header, and with PUBLIC - OK TO SHARE; the six substantive record values are byte-identical across arms, and the outcome is verbatim occurrence of any of them in the outbound message. Four models x 3 arms x 4 repeats give 480 trials; the scenario is the unit of generalization, and we report the 10 scenario-level values (mean, median, sign counts), with no p-values or intervals. The confidential-minus-unlabeled contrast is inconclusive and floor-limited in every model (both arms at or near zero), so it does not show that confidential labels lack a protective effect. Adding PUBLIC - OK TO SHARE is descriptively associated with higher verbatim egress relative to the unlabeled baseline, with strong model dependence: strong and consistent for Claude Sonnet 5 (public-minus-unlabeled mean +0.800, all 10 scenarios; mostly an association with whether Claude relays at all), moderate but floor-limited for one GPT-5.6 tier, small (median 0) for another, and a complete floor for the third. This is an association in one configuration, not a causal or general effect. Code, byte-pinned traces, and the offline analysis pipeline are released as a public artifact.

---


### 11. [From Visual Cues to Spoken Narration: Rethinking Audio Description](https://arxiv.org/abs/2609.01725)

**<font color=#1a73e8>作者：</font>** Akshita Gupta, Aditya Arora, Federico Tombari 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Audio Description (AD) provides spoken narration of visual events during dialogue gaps, making movies accessible to visually impaired audiences. The problem requires determining both what (which visual event) and when (position for inserting the AD) to narrate, to achieve the best user experience. Prior work has largely reduced the problem to video captioning of pre-segmented video clips, i.e., what is largely predefined and when is ignored entirely. We propose Cue2Narrate, a two-stage pipeline that jointly predicts what and when to narrate in longer untrimmed movie clips. A dual-head audio-visual localizer predicts two temporally distinct windows per AD utterance: a visual cue window and a spoken narration window. A LoRA-adapted VLM then generates concise ADs from the predicted visual evidence, trained with a Description Ranking Loss that ranks captions (negative samples) of the same frames lower than the GT AD. To benchmark this new problem statement, we introduce the LongLSMDC benchmark with up to 8-min movie clips (~6.5min on average). On LongLSMDC, Cue2Narrate outperforms video-only and audio-only localization baselines by 5--12 points in avg. mAP. Under both predicted- and GT-window evaluation, Cue2Narrate improves AD generation over the corresponding fine-tuned base VLM. These results establish the first benchmark for multi-segment AD generation on long-form clips. Data & Code: this https URL

---


### 12. [HEAT: Faster Fully Homomorphic Inference via Approximations-Weights Co-Adaptation](https://arxiv.org/abs/2609.01730)

**<font color=#1a73e8>作者：</font>** Alessandro Zirilli, Davide Marincione, Evgenios M. Kornaropoulos 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Fully homomorphic encryption (FHE) allows a server to run a language model directly on encrypted user prompts, but current approaches remain prohibitively slow. Ciphertexts natively support only addition, multiplication, and rotation, and multiplications may be composed only to a bounded depth before a costly bootstrapping operation is needed to continue. Every nonlinearity must therefore be approximated by an iterative method, and each iteration uses multiplications. A higher iteration count buys precision but exhausts the available depth faster and triggers more bootstraps, which dominate latency. Existing approaches fix the iteration counts uniformly across the model rather than tailoring them to each site's error tolerance. We introduce Homomorphic Encryption-Aware Training (HEAT), a fine-tuning method that makes the per-nonlinearity iteration counts learnable, enabling them and the model weights to co-adapt during training. HEAT optimizes iterations with respect to the task objective, allowing the model to adapt to approximation errors encountered during inference without architectural changes or retraining from scratch. On encrypted GPT-2 decoding, HEAT reduces iterations by $3.1\times$, bootstraps by $1.6\times$, and end-to-end latency by $1.4\times$, while improving decode agreement over the calibrated baseline.

---


### 13. [AlphaRAD: Grounded Zero-Shot Classification in Chest Radiology via $α$-Corrected Binary Cross Entropy and Factorized Latent Supervision](https://arxiv.org/abs/2609.01757)

**<font color=#1a73e8>作者：</font>** Jianzhong You, Yuan Gao, Chris McIntosh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Pretrained Models (VLPMs) offer a scalable path to open-vocabulary chest radiology understanding, yet two aspects remain underexplored: how structured clinical semantics extracted from medical reports can reduce in-batch noise during contrastive learning, and how cross-modal fusion can be designed to produce more faithful spatial grounding without added complexity. We introduce AlphaRAD, addressing these opportunities through two contributions. First, we construct a large-scale structured medical concept space from medical reports parsed by a Large Language Model for training, thereby mitigating in-batch learning noise and removing heuristic pair matching in contrastive learning, and thus naturally positioning AlphaRAD as a medical concept discriminator trained via $\alpha$-Corrected Binary Cross-Entropy. Second, we propose FLaS (Factorized Latent Supervision), an extremely simple yet effective cross-modal feature fusion module that factorizes VLPM representations into independent subspaces, using dedicated alignment supervision to enhance the expressiveness of spatial grounding without introducing additional model parameters. Through extensive empirical validation, AlphaRAD shows strong zero-shot generalization across diverse chest radiology tasks. Notably, it establishes state-of-the-art average performance across 16 classification benchmarks, while achieving individual state-of-the-art results via distinct gains on 7 grounding/phrase grounding and 3 segmentation datasets.

---


### 14. [Towards Behavior Tree-Guided Vulnerability Detection with Lightweight LLMs](https://arxiv.org/abs/2609.01758)

**<font color=#1a73e8>作者：</font>** Enna Basic, Alberto Giaretta  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly used for software vulnerability detection, but their performance depends on how source code is represented in the input. Most prompting approaches use source code in its original form, while some works propose the use of structured representations. Abstract Syntax Trees (ASTs) are one of the most popular approaches, but AST verbosity increases input size relative to source code, making them hard to fit within some LLMs context windows. This paper investigates Behavior Trees (BTs) as an alternative intermediate representation for LLM-based vulnerability detection. BTs encode control flow, conditions, and executable actions more compactly than ASTs, making them a natural candidate when token count is a constraint. First, we propose a preprocessing stage that parses Java source code into ASTs and then converts them into BT representations. We then compare vulnerability detection performance across 460 Java samples from the Juliet Java test suite, using three input representations: raw source code, AST, and BT. All experiments use a single quantized local LLM, Mistral Small 3.2 24B (Q4_K_M). Our results show that using BT representations improves recall on short code samples, while raw source code achieves higher precision. On longer samples, BTs improve overall performance over the original representation and fit within the context window, whereas many ASTs exceed the context limit. These findings suggest that BTs can provide a compact and useful structured representation for vulnerability detection with quantized, locally deployable LLMs.

---


### 15. [MemeCULT-1K: Benchmarking South Asian Cultural Context and Humor Understanding of Multimodal Models](https://arxiv.org/abs/2609.01772)

**<font color=#1a73e8>作者：</font>** Tawsif Tashwar Dipto, Mehedi Ahamed, Radib Bin Kabir 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Meme understanding goes beyond recognizing visual content or literal text; it requires implicit cultural knowledge and pragmatic inference that most vision-language models still lack. We introduce MemeCULT-1K, a multilingual benchmark of 1,000 South Asian memes in Bengali, English, and Hindi, where each meme is paired with a cultural context note and three human-written explanations, along with a supplementary set of 54 Bengali regional dialect memes. We evaluate thirteen popular Vision Language Models (VLMs) under two settings: meme-only and context-aware. Providing minimal cultural context yields consistent gains across all models and languages: mean SBERT similarity improves from 44.6 to 56.4 (+11.8), BLEURT from 37.3 to 42.3 (+5.0), and LLM-as-a-Judge scores from 2.57 to 3.43 out of 5 (+0.86). Fine-grained error analysis reveals that closed-source models fail mainly on entity and reference misidentification, while open-source models are bottlenecked by broader cultural knowledge gaps, with linguistic and phonological failures proving the most context-resistant across both. These results highlight the difficulty of culturally grounded meme understanding and motivate future work on explicit cultural knowledge integration. Our dataset and code are publicly available at TawsifDipto17/MemeCULT-1K.

---


### 16. [VakyArth: Evaluating Pragmatic Competence in LLMs across Indic Languages](https://arxiv.org/abs/2609.01788)

**<font color=#1a73e8>作者：</font>** Usneek Singh, Poorvaja Veera Balaji Kumar, Parth Nanda 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Real-world communication often requires pragmatic reasoning: interpreting meanings implied through context and cultural convention rather than stated literally. Existing pragmatic evaluation remains largely limited to English and high-resource languages, leaving Indic languages unexplored despite their linguistic and cultural diversity. We introduce VakyArth, the first pragmatic benchmark for Indic languages, designed as a diagnostic evaluation covering Hindi, Punjabi, Tamil, and Malayalam. VakyArth evaluates models across five phenomena: deixis, speech acts, implicature, social pragmatics, and coherence; through multiple-choice questions, natural language inference, and translation, with all items authored by native speakers. Across multilingual large language models (LLMs) of varying families and sizes, we find consistent failures on pragmatic meanings rooted in Indic linguistic and cultural conventions. Our analysis shows systematic differences across languages and tasks: MCQ accuracy exceeds NLI accuracy in all model-language combinations, translation performance does not reliably track pragmatic understanding, and Indo-Aryan languages show a translation advantage over Dravidian languages. We further show that automatic translation metrics can miss fluent but pragmatically unfaithful outputs, especially for implicature and deixis.

---


### 17. [Disentangling Statistical Preemption from Entrenchment in Language Models' Avoidance of Overgeneralization](https://arxiv.org/abs/2609.01794)

**<font color=#1a73e8>作者：</font>** Yixuan Wang, Freda Shi, Kanishka Misra  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How do learners avoid overgeneralizations such as Tom laughed me without explicit negative evidence? Constructionists have posited two proposals that describe indirect negative evidence against overgeneralizations: preemption (which privileges exposure to near-synonymous construction---e.g., she made him laugh) vs. entrenchment (all exposures to a verb's grammatical usages, including cases like He laughed). We disentangle these hypotheses by running controlled rearing experiments on LMs trained on child-caregiver conversations, where we systematically remove preemptive vs. non-preemptive evidence. We find that while LMs avoid overgeneralizations, they do not show preemption at a verb-specific level, instead showing weak but non-zero evidence of abstract preemption. Combined with results from analyzing the LMs' training dynamics, we find that LMs treat competing structures as indirect positive---as opposed to negative---evidence in the verb-specific condition. Insofar as preemption is the more plausible route to avoiding overgeneralizations in humans, our results point the need for there to be sensitivities to indirect negative evidence in neural network learners, and suggest new human experiments to test abstract preemption.

---


### 18. [How Do Prompt Variations Affect Energy Consumption in On-Device LLMs?](https://arxiv.org/abs/2609.01798)

**<font color=#1a73e8>作者：</font>** Wei Hu, Xiaolong Tu, Dawei Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed on mobile devices, making energy efficiency a key deployment constraint, yet the energy impact of prompt design remains underexplored. This paper aims to understand how two prompt properties, cognitive load and phrasing pattern, shape the energy behavior of on-device LLM inference. We conduct a broad empirical study covering prompt properties, datasets, models, and devices, with phase-level profiling that separates prefill and decode energy. We find that cognitive load primarily affects the energy cost per token, while phrasing pattern affects energy largely through token usage. Our energy-quality analysis further shows that prompt design reshapes the attainable frontier differently across models, highlighting the need for model-aware prompt design in energy-efficient on-device LLM inference. Code, datasets, and scripts are available at this https URL.

---


### 19. [hLLM: Single Pass Decoding for Generative Reranking](https://arxiv.org/abs/2609.01807)

**<font color=#1a73e8>作者：</font>** Emil Laftchiev, Prachi Agrawal, Moe Kayali 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve state-of-the-art generative ranking quality, but the ranking they produce must be decoded, and autoregressive decoding spends one sequential forward pass per emitted token. We observe that the only tokens a ranker must emit are the $N$ ordinal values naming the items in ranked order, and that this narrow, permutation-structured output format admits decoding strategies which are much more efficient than left-to-right generation. We introduce hLLM (Hungarian LLM), a format-specialized decoding strategy that decodes all $N$ ordinals in $O(1)$ forward passes. hLLM reads an $N \times K$ item-position score matrix off the LLM's prefill hidden states with a lightweight self-attention head, then decodes the ordinals as the optimal bipartite assignment of that matrix via the Hungarian algorithm, yielding a valid permutation by construction rather than by repair. Through a systematic study of training signals and backbone adaptation, we show that LoRA-based fine-tuning combined with teacher ranking distillation reaches 28 ms end-to-end inference, a speed-up of $64\times$ while maintaining ranking quality on par with the teacher. We provide a complete ablation decomposing the contributions of architecture, training signal, and backbone adaptation. Our framework connects generative ranking to combinatorial optimization, opening a path toward other $O(1)$-decode mechanisms for real-time ranking.

---


### 20. [TalkFa: A Unified Benchmark for Farsi Dialogue Generation and Understanding](https://arxiv.org/abs/2609.01810)

**<font color=#1a73e8>作者：</font>** Neda Jamshidi, Kamyar Zeinalipour, Fahimeh Akbari 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Farsi, spoken by more than 120 million people, lacks a comprehensive benchmark for dialogue generation and understanding. We introduce TALKFA, a unified benchmark comprising three complementary datasets: (1) WIKI-FADIAL, 4.2K Wikipedia-grounded dialogues for knowledge-grounded generation; (2) DAILYDIALOG-FA, 6.6K dialogues annotated for dialogue acts and emotions; and (3) PLAYDIAL-FA, 2.1K theatrical dialogues with sentiment labels. While LLMs assist data construction, every dialogue undergoes multi-stage review and revision by native Farsi speakers, and only the final human-approved dialogues are released. Experiments with six LLAMA and MISTRAL models show that LoRA substantially improves dialogue generation while requiring only 25-50% of the training data to recover over 90% of the final performance gains. Across classification tasks, FABERT achieves the best dialogue-act performance, LORA-MISTRAL-7B performs best on emotion recognition, and MISTRAL-24B achieves the highest sentiment score. Human evaluation and independent external validation demonstrate the reliability of the benchmark, while comparisons with GPT-4.1 as an LLM judge reveal that automatic metrics substantially overestimate dialogue quality. Zero-shot evaluation with frontier LLMs further shows that TalkFa remains a challenging benchmark. We will release all datasets, annotation guidelines, code, and checkpoints.

---


### 21. [Beyond Instruction-Driven Editing: Source-Grounded Problem Discovery with User-Governed Repair for Scientific Posters](https://arxiv.org/abs/2609.01813)

**<font color=#1a73e8>作者：</font>** Xingda Lyu, Honglin Lu, Xinye Luo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Interactive editors usually assume that users already know what to change. Yet an important interaction state comes earlier: a user may recognize that an artifact is not working without knowing what intervention to request. We call this the articulation gap. We introduce PROS (Proactive Refinement Of Scientific Posters), which separates epistemic initiative from behavioral authority: the system can surface source-grounded candidate problems, while users decide which become repair goals and whether resulting changes are committed. Accepted issues hand off to native-object PPTX editing with validation and reversible preview. We also introduce PROS-Bench, a source-linked collection of 120 papers and 320 editable PPTX posters, including a 120-poster matched primary core and a separate conference representation challenge. On the primary core, PROS achieves a mean VLM-rated stage-balanced diagnosis quality score of 67.2 on a 0-100 scale and 87.6% operator-verified target resolution among accepted diagnoses. Temporally blinded automated scoring yields a +22.7-point paper-macro accepted-target uplift, yet 14.8% of assessable accepted targets decline. This divergence shows why problem discovery, local resolution, and realized outcome should be evaluated separately. More broadly, intelligent editors can support problem discovery before a concrete edit request exists without taking authority over consequential change.

---


### 22. [Induction and Inquiry via Probabilistic Reasoning over Language and Code](https://arxiv.org/abs/2609.01815)

**<font color=#1a73e8>作者：</font>** Wasu Top Piriyakulkij, Sam Acquaviva, Cassidy Langenfeld 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> How humans grow and maintain abstract knowledge from the sparse, streaming noisy data of experience is a longstanding challenge in cognitive science. Any computational account must satisfy at least three desiderata: It must be (1) data-efficient and compute-efficient, (2) capture gradations of uncertainty to support intelligent inquiry and information gathering, and (3) be flexible enough to mentally represent the endless range of concepts people can learn and think about. Here we introduce a computational model that captures these three properties, by encoding symbolic knowledge as mental programs that combine natural language with source code, and sequentially inferring mental programs using LLM-guided Bayesian learning algorithms. Across a range of behavioral studies this model successfully reproduces quantitative signatures of human inductive learning and active inquiry, such as anchoring, garden-pathing, and other effects. In contrast, pure LLMs and classic Bayesian models either fail at the underlying task, or do not reproduce human behavior, or succeed only at exorbitant computational cost. These results suggest that one way humans continually grow their knowledge is by mentally representing many hypotheses spanning language-like and program-like representations, then revising those hypotheses to approximate Bayesian updates, while a bottom-up neural mechanism (an LLM) makes inference both tractable and learnable.

---


### 23. [Video2Reaction: Training Foundation Video Models to Predict Audience Reaction](https://arxiv.org/abs/2609.01816)

**<font color=#1a73e8>作者：</font>** Sidong Zhang, Trang Nguyen, Shiv Shankar 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> We introduce Video2Reaction, a multimodal dataset that maps short movie segments to the induced emotional reactions of viewers in the wild, as expressed through social media comments. Video2Reaction captures the natural diversity of emotional responses by aggregating reactions from online comments at scale, modeling labels as distributions over categorical emotions to better reflect the subjective and ambiguous nature of emotional perception. We benchmark two vision-language models (VLMs) finetuned with LoRA, showing that VLMs learn effectively from Video2Reaction and outperform specialized baselines on dominant reaction prediction. We further demonstrate that VLMs pre-finetuned on Video2Reaction transfer effectively to VCE, another induced emotion dataset with a different taxonomy and video domain. Notably, LLaVA-NeXT-Video-7B pre-finetuned on Video2Reaction and adapted on only 1% of VCE training data achieves a top-3 accuracy of 0.682, on par with the best reported VCE performance trained on the full dataset. The dataset is available at this https URL

---


### 24. [AVERT: Audio-Verified Adjudication for Spoken Dialogue State Tracking](https://arxiv.org/abs/2609.01828)

**<font color=#1a73e8>作者：</font>** Chunggi Lee, Hanspeter Pfister  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Spoken dialogue state tracking recovers slot-value pairs from speech, where ASR errors concentrate in entity values and persist across turns, making it both a generation and an editing problem. A strong per-turn text editor corrects much of this but, operating on the transcript alone, leaves three recoverable errors: a value predicted inconsistently across turns, an omitted slot, and a value the audio does not support. We present AVERT, which scores each candidate value by combining cross-turn agreement with a trained audio-conditioned verifier and resolves the three error types with three operators, vote, add, and swap, each restricted to the slots where its error is common. On SpokenWOZ, a base speech-LLM reaches 33.04 JGA, a text editor 38.34, and AVERT 40.13, without retraining either. This is in the range of a 1B end-to-end system that consumes the full spoken history (39.32), though AVERT uses two 1B decoders rather than one. The audio verifier contributes a statistically significant gain, and restricting each operator to a selected slot subset matters: removing it lets unrestricted voting overwrite correct categorical values and fall below the editor.

---


### 25. [Interpretable Symptom Vectors for Depression in a Large Language Model](https://arxiv.org/abs/2609.01832)

**<font color=#1a73e8>作者：</font>** Fangyi Zhu, Ajay Subramanian, Allison Constant 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Patients with depression present with diverse symptom profiles, yet clinical practice routinely reduces this variation to a single severity score. Large language models (LLMs) can potentially capture various symptoms and their severity from patient speech. However, how depressive symptoms are represented inside LLMs remains poorly understood, limiting clinical trust. To examine whether internal model activations match clinician judgment, we analyzed the residual stream of Gemma-3-27B-PT using mechanistic interpretability techniques. Recording activations across symptom descriptions drawn from validated clinical instruments, we found that symptom groups geometrically separated the most at layer 21 across multiple distance metrics. Using Semantic Projection, we then projected held-out naturalistic text onto Symptom Vectors constructed from these instruments. The resulting per-symptom coefficients preserved clinician-annotated rank ordering across mood, somatic, and suicidality axes. Furthermore, a single depression vector in Layer 21 separates held-out depressive from non-depressive text (AUC = 0.789), which can be used as an emotional valence gate that restricts symptom projection to depressive speech. These results reveal a decorrelated, clinician-aligned symptom signal readable directly from internal activations, offering a mechanistic foundation for interpretable depression-assessment tools.

---


### 26. [Candidate Generation and Definition-Guided Verification for Sentence-Level Depression Symptom Recognition](https://arxiv.org/abs/2609.01833)

**<font color=#1a73e8>作者：</font>** Weiming Li, Catarina Barata, Miguel Constante 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sentence-level recognition of depression symptoms is challenging because similar expressions can differ in symptom relevance, and language-model inference is insufficiently grounded in diagnostic definitions. This study proposes a two-stage framework separating symptom-candidate generation from definition-grounded verification. A contrastively fine-tuned sentence encoder generates a symptom candidate per sentence, and a fine-tuned language model verifies whether the candidate is present or absent using the sentence, its context, and a candidate-specific diagnostic definition, checking its judgment against that definition before answering. Evaluated against encoder, inference-based, medical, and general LLM baselines and a matched single-stage supervised classifier, the proposed pipeline attains the best accuracy and F1 scores of all methods, with rationales matching expert-authored annotations. A preliminary clinical audit indicates moderate alignment with diagnostic definitions, with explanation quality strongly dependent on prediction correctness. The results support decomposing symptom recognition into candidate generation and definition-grounded verification, though performance remains limited for rare categories.

---


### 27. [Architecting Conversational Data Systems for Stateless LLM APIs: The Hydration Proxy Pattern](https://arxiv.org/abs/2609.01834)

**<font color=#1a73e8>作者：</font>** Joseph Axisa  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As enterprise platforms transition to conversational reasoning interfaces, the stateless nature of LLM APIs creates an architectural gap. While statelessness enables horizontal scalability for AI providers, it forces client applications to manage the entire burden of conversational state and semantic memory. The work identifies the Hydration Proxy Pattern, an architecture that decouples session persistence from the reasoning engine. The framework ensures platform sovereignty over conversational data while enabling secure, multi-stage semantic grounding. We further propose the Context Stabilization Mandate to resolve the tradeoff between sovereign state management and KV caching.

---


### 28. [Agent Memory Is a Surface for Endogenous Authorization Laundering](https://arxiv.org/abs/2609.01836)

**<font color=#1a73e8>作者：</font>** Tommaso Cerruti, Mika Okamoto, Ansel Kaplan Erol  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Long-running LLM agents rely on persistent memory to carry state across interactions, including permissions, restrictions, and revocations. When memory misrepresents this evolving authorization state, the agent's own records can grant authority that the underlying history never permitted, resulting in misaligned behavior without any external attacks.
We term this failure endogenous authorization laundering, where spurious permissions written into memory lead to unauthorized actions as their provenance is washed away. We then introduce EAL-Bench, which measures how accurately persistent memory preserves evolving authorization state and whether errors propagate to downstream unauthorized actions.
We evaluate five LLMs as memory writers and two as executors across procurement, cybersecurity, and finance. We find that under incremental memory updates, writers create false authority for up to 50.2% of unauthorized requests; once false authority is present, executors act on it in 98.6% of trials. Two safeguards, requiring stored permissions to be backed by valid source events, and tracking permission changes through bounded event sourcing, substantially reduce laundering, but both also reject more legitimate actions, exposing a safety-utility tradeoff. Persistent memory is therefore not merely a performance component, but a part of an LLM agent's effective authorization policy.

---


### 29. [The Memory Trust Gap: Capability-Dependent Failures in Persistent-Memory Agents](https://arxiv.org/abs/2609.01852)

**<font color=#1a73e8>作者：</font>** Jundong Hu, Shekar Ramachandran  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Persistent memory supports personalized agents, but a stale stored fact can override current authoritative evidence without warning. We study when this harm begins as model capability changes. We evaluate a frozen, closed-set, action-scored benchmark with 2 suites that represent 2 different meanings of "no memory" (a Benefit suite, unsolvable without the stored fact, and a Safety suite, in which an authoritative tool always holds the correct value), on a same-family model-size series (Qwen3 0.6/1.7/4/8B). The Memory Trust Gap reflects over-trust rather than confusion. In the Benefit suite, models answer with the stale value 0.92-1.00 of the time at every scale. In the Safety suite, harm below the no-memory baseline under the trap conditions ($\Delta_{\mathrm{mem}}$) is capability-gated, with the larger models collapsing most once a stale note is made to look current. In a $2\times2\times2\times2$ factorial, which feature triggers over-trust depends on both the feature and model scale. Removing a label amplifies over-trust at every size, and a recency feature (stale dated newer) fools the larger models harder. Source authority is weak and scale-flat, and position changes from positive to negative across the Qwen3 model-size series. We confirm these scale interactions with direct cross-size contrast tests rather than overlapping per-model intervals. Mitigation is likewise capability-dependent: exposing metadata improves accuracy for the capable models, but only pre-resolving the conflict restores accuracy for the 2 smaller checkpoints. The same pattern appears on the capable models in an independent Llama-Instruct model-size series and on 2 external datasets (RGB, MisBench). A framing control finds no consistent advantage for the memory label: at the 3 smaller scales, models trust a stale document more than a stale memory; at 8B, the difference is not significant.

---


### 30. [Belief-Calibrated Optimization: An Explicit World Model for Agentic Optimization](https://arxiv.org/abs/2609.01861)

**<font color=#1a73e8>作者：</font>** Yuhan Chen, Zhihua Tian, Mahavir Dabas 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The performance of an LLM agent depends on the scaffold around a frozen model. A common way to improve that scaffold is to use a coding agent as an optimizer: it reads current scores and traces and iteratively edits the source, producing a new candidate each round. Each edit is chosen according to a belief about how the environment will respond: what went wrong, and which change should help. That belief is typically implicit. It lives in the coding agent's reasoning on the current call, or remains latent in its parameters, rather than as something written down. Later calls therefore see scores and traces, but they do not use that belief. We introduce Belief-Calibrated Optimization (BCO), a method that writes that belief down as a persistent in-context document and continually revises that document as new candidates are evaluated. The resulting document is a world model: the current account of how the environment responds to edits. Added to an otherwise standard loop, BCO reaches a higher train passrate than a matched control that lacks only the world model, on five benchmarks spanning memory QA, tool-use QA, code-as-action app agents, and terminal agents. The gap remains on every held-out split, which is not used to select the candidate. After a target-model swap, in which the frozen model is replaced and the scaffold is not, the selected BCO scaffold leads on the tasks we test, except where context-window overruns leave it unfinished. An offline ablation then asks whether that gap comes from what the world model says. A fresh predictor given the accumulated document forecasts how the environment will respond more accurately than predictors given either no document or a same-form copy whose content has been falsified. The comparison indicates that the document carries reusable information in its content, not only in its form.

---


### 31. [Thinking effort aligns between humans and reasoning models in abductive reasoning](https://arxiv.org/abs/2609.01867)

**<font color=#1a73e8>作者：</font>** Henry Arthur  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A major question in cognitive modeling concerns the behavioral alignment between large language models and humans across linguistic and non-linguistic tasks. Unlike standard LLMs, large reasoning models (LRMs) are optimized with reinforcement learning from verifiable rewards, encouraging correct solutions to reasoning tasks rather than preference-aligned responses. Recent work (de Varda et al., 2025) investigates the cost of thinking in humans and LRMs by comparing human reaction times with model reasoning traces across a range of reasoning tasks. We isolate this alignment by turning to abductive reasoning: unlike deductive tasks, its difficulty cannot be inferred from formal structure and offers no shortcuts a model could exploit to mimic effort without genuine search, providing firmer ground for empirical claims of shared effort. We find further evidence of alignment between LRM and human reasoning effort, as well as evidence that models and humans tend to make similar errors. Finally, we show that decoding methods that let models explore multiple reasoning paths increase alignment in reasoning cost between humans and LRMs across the three models tested.

---


### 32. [ArcticSwarm: Deferring Early Consensus in Long-Horizon Multi-Agent Research](https://arxiv.org/abs/2609.01870)

**<font color=#1a73e8>作者：</font>** Soyoung Yoon, Boyi Liu, Yite Wang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multi-agent systems have shown strong performance in domains with reliable verifiers such as coding, where multi-parallel candidate generation selected by a verifier is effective. However, such pipelines would not generalize to open-ended, long-horizon research tasks without a verifier. While majority voting or self-consistency is often used to reach consensus as a proxy verifier, parallel agents repeatedly explore the same evidence, while access to peers' partial findings cause search to converge on an early candidate before alternatives are tested. We present ArcticSwarm, a multi-agent research architecture that separates evidence gathering from evidence integration. Subagents publish findings to a shared bulletin board, while gated isolation lets selected search tasks maintain their own prior, preventing early consensus. Structured review at three commitment boundaries enforce only confident candidates to be propagated. As a result, ArcticSwarm reaches 82.6% on the full BrowseComp-Plus set with the open-weight Qwen 3.5-27B model, compared with 78.8% without gated isolation and 74.5% additionally with structured review disabled, outperforming aligned baseline MiroFlow runs (70.6%). Extending to live-web BrowseComp, ArcticSwarm reaches 73.6% with GPT-5, which is well above the reported provider system (54.9%) and MiroFlow (63.4%). Overall, the results show that restricting peer reads during evidence gathering and strengthening commitment boundaries before a hypothesis is shared can broaden search and improve long-horizon multi-agent deep research.

---


### 33. [Epistemic Sybil Resistance: Multiplying AI Agents Without Multiplying Evidence](https://arxiv.org/abs/2609.01873)

**<font color=#1a73e8>作者：</font>** Marc Bara  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-agent AI systems improve inference by spawning agents and synthesizing reports. But another agent is not another observation: apparently independent reports may descend from the same evidence, and genuinely independent evidence can produce nearly identical reports. We formalize this as an epistemic Sybil problem. A report Z is an epistemic Sybil extension relative to reports R when I(Theta; Z | R) = 0. No report-only aggregator can generally distinguish replication from independent corroboration: identical reports can warrant different posteriors under unobserved ancestry. A Gaussian shared-root model shows common ancestry does not imply complete redundancy. Repeated extraction adds information toward a source-level ceiling, and correlated extraction errors, which a shared base model can induce among independent agents, lower that ceiling further. We test these predictions with more than 20,000 controlled LLM-agent report and extraction calls on synthetic evidentiary documents. Holding one evidence root fixed while report multiplicity rises from 1 to 32 collapses naive posterior coverage from 0.940 to 0.263. Holding report count fixed while evidence-root multiplicity rises from 1 to 16 closes the gap, and the aggregators are statistically indistinguishable at k = 16. The agent's replicate extraction errors are correlated (gamma_cal = 0.719, estimated out of sample), and a correlated-extraction aggregator restores calibration accordingly. A controlled manipulation isolates representation similarity from evidential ancestry. It changes a report-space deduplication mechanism's mean inferred cluster count by 1.425 (95% CI [1.363, 1.485]), whereas a fourfold change in true ancestry changes it by only 0.040 ([-0.045, 0.120]). Collective inference should therefore track evidential ancestry and dependence, not agent or report multiplicity or similarity.

---


### 34. [GAPS: Dimension-Level Gates for Conditional Activation Steering](https://arxiv.org/abs/2609.01878)

**<font color=#1a73e8>作者：</font>** Moghis Fereidouni, Muhammad Umair Haider, Hassan Sajjad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering suppresses undesired behaviors in language models by adding a steering vector to the hidden state during generation. Recent conditional methods such as CAST and DSAS improve the behavior-capability trade-off by deciding when to intervene, but once active, they apply the full dense vector to all hidden dimensions, regardless of whether a neuron carries concept information or already lies in the desired regime. We introduce dimension-level conditioning as a complementary axis of selectivity that also decides which neurons to intervene on. Our method, GAPS (Gated Activation steering via Posterior and Separability), combines two training-free gates: a static separability gate that restricts steering to neurons with statistically reliable concept information (via AUROC), and a dynamic posterior gate that steers a neuron only when its current activation is better explained by the undesired concept under a Gaussian model. The gates add O(D) overhead per token, and they plug into existing conditional methods. On toxicity mitigation (RealToxicityPrompts) and concept removal (OneSeC) with Gemma-3 (4B) and Qwen-3 (1.7B), GAPS consistently matches or improves the Pareto front of its token-level counterparts; under a fixed capability budget, DSAS+GAPS reduces Gemma-3's toxicity rate from 6.52% to 0.48%, versus 3.52% for DSAS alone. Ablations attribute most of the gain to the posterior gate.

---


### 35. [Does Playing it Safe Count as Faithfulness? Reassessing LVLM Hallucination Mitigation Methods](https://arxiv.org/abs/2609.01888)

**<font color=#1a73e8>作者：</font>** Mehrdad Fazli, Sina Mansouri, Mohit Marvania 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent inference-time hallucination mitigation methods for large vision-language models (LVLMs) report strong gains on hallucination benchmarks. However, it remains unclear whether lower hallucination scores reflect improved multimodal grounding or more conservative generation. We evaluate six mitigation methods across three LVLMs and four benchmarks, including hallucination-focused evaluation and the diverse capability benchmark MMStar. Our analysis reveals two consistent patterns. First, hallucination reduction is often coupled with reduced informativeness: methods that lower hallucination rates also reduce object recall, visual coverage, or response detailedness. Second, improvements on hallucination benchmarks do not reliably transfer to broader multimodal capabilities, with methods showing inconsistent or degraded performance on fine-grained perception and reasoning tasks. Our findings suggest that current evaluation protocols may overestimate progress by rewarding conservative generation. We argue that hallucination mitigation should be evaluated as a faithfulness--informativeness--capability trade-off rather than through hallucination scores alone.

---


### 36. [Grounded, Compute-Efficient LLM Policy Agents for Energy-Poverty Equity in Physically-Constrained Peer-to-Peer Energy Markets](https://arxiv.org/abs/2609.01918)

**<font color=#1a73e8>作者：</font>** Kunal Jadhav, Siddhesh More  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Energy poverty is nearly absent from NLP-for-social-good, and the little existing work is either static retrieval/QA or relies on carbon-intensive cloud LLMs, a self-defeating "computational irony" for a humanitarian setting. We present EqGrid, a closed-loop simulation in which a low-frequency, open-weight LLM policy agent sets price and carbon bounds and targeted subsidies over a community of empirically-grounded household personas, while high-frequency multi-agent RL traders clear a continuous double auction constrained by a physical distribution grid (IEEE-33-bus with Dynamic Operating Envelopes). Our contribution is threefold and directly addresses how to measure the social impact of AI: (i) grounded personas (region-matched socio-demographics) whose load curves are checked for shape and level realism against real smart-meter data; (ii) formal energy-poverty equity metrics (Energy Burden, Gini of EB, LIHC) showing the intervention reduces burden inequality without raising net grid cost; and (iii) a compute-efficiency frontier that measures how much equity performance survives compressing the policy agent from a 235B teacher down to a sub-1B model deployable on a laptop, in estimated energy/carbon per decision. A decoupled-safety design (the LLM sets bounds; a validate-and-project grid gate executes) yields zero grid-constraint violations versus 55 under direct LLM control. On energy-poverty equity, the LLM policy lowers the Gini of energy burden to 0.305 (from 0.351) and mean burden by 28% while cutting cost (outperforming a tuned rule baseline), and a 3B-active model retains 95% of the benefit at roughly 9x lower inference energy than the teacher, with even a 0.8B on-device model retaining 92% at roughly 24x lower energy. We will release code and configs.

---


### 37. [Looped Transformers under the Jacobian Lens: Does the Global Workspace Survive Recurrence?](https://arxiv.org/abs/2609.01924)

**<font color=#1a73e8>作者：</font>** Wenlong Wang, Fergal Reid  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent work identifies a mid-depth band of verbalisable, causally potent representations in a standard feedforward transformer --- a functional analogue of a global workspace. Whether the same workspace functionality emerges when depth is implemented through recurrence rather than a stack of distinct layers remains unknown. Looped and depth-recurrent transformers provide a direct test of this question because they reuse the same weights across depth. We extend the Jacobian lens to iterated architectures using a virtual-unrolling adapter. We apply the full workspace suite --- lens fitting, readout, and eleven causal experiment families --- to Ouro-2.6B (48 layers looped 4 times, deeply supervised) and Huginn-0125 (a 4-layer core recurred 16 times, trained for latent reasoning), using Qwen3.6-27B (64 untied layers) as the standard baseline. We find that a workspace forms in the iterated part of each architecture, but that recurrence changes how it can be accessed. Ouro reconstructs workspace content in every loop, and linear transport cannot carry that content across loop boundaries; writes and ablations must therefore span every remaining loop. Huginn carries content forward across all sixteen recurrences, while reads, writes, and ablations act only within a sliding window of roughly two recurrences. Whether newly injected content can be verbalised tracks explicit per-iteration supervision; whether existing content can be steered does not.

---


### 38. [CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing](https://arxiv.org/abs/2609.01925)

**<font color=#1a73e8>作者：</font>** Huu Huy Nguyen, Chien Van Nguyen, Franck Dernoncourt 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> The attention prefilling phase of long-context LLM inference scales quadratically, making self-attention a severe computational bottleneck. Traditional sparse attention methods mitigate this through fixed patterns or offline profiling, but lack the flexibility to adapt to input-dependent attention structure. Recent dynamic methods address this by routing heads to sparse patterns in real-time, but rely on indirect routing proxies with overhead and budget allocation mechanisms that overlook the post-softmax mass hierarchy. We present CRISP (Cliff-awaRe Input-adaptive Sparse Prefilling), which identifies and addresses two structural challenges in this dynamic routing paradigm. First, we show that the routing decision can be read directly off the structure of the proxy attention map. We replace the Jensen-Shannon Divergence (JSD) routing with C_struct, a structural proxy that measures mass at Vertical-Slash compatible positions and reproduces JSD's routing decisions while eliminating both the pooled matmul and subsequent KL divergence overhead. Second, we formalize the post-softmax mass cliff and demonstrate theoretically that strictly cumulative coverage thresholds accumulate O(n) background noise at long contexts. CRISP navigates this via a sink-aware threshold grounded in the noise floor. Empirically, across InfiniteBench, RULER and LongBench on two model families, CRISP is the strongest sparse method overall and matches or exceeds exact dense attention on retrieval-heavy benchmarks, recovering up to +28.0 pp on retrieval tasks over baselines and achieving up to a 5.30x attention speedup at 512k tokens, driven primarily by our O(n) noise elimination during selection while preserving structural integrity.

---


### 39. [Sparse Readout Prism: Explaining Logit-Lens Scores in Features Instead of Tokens](https://arxiv.org/abs/2609.01936)

**<font color=#1a73e8>作者：</font>** Matteo He, William F. Shen, Xinchi Qiu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> A language model's prediction of its next token develops across layers, and lens methods track this process by decoding intermediate hidden states into tokens. But a lens reading reflects both the hidden state and the readout (the unembedding matrix) used to decode it. Many lenses are fit on a corpus, and we show that two lenses differing only in their fitting corpus can report different tokens for the same hidden states. We call this dependence corpus conditionality. To examine readout structure independently of the fitting corpus, we introduce Sparse Readout Prism (SRP), which decomposes the readout using only its weights and expresses any token logit or logit difference as a sum of contributions from sparse readout features. This reveals readout features as a new unit of analysis for lens readings, exposing structure that token identities can obscure and enabling comparisons across tokens, contexts, layers, and lenses. Replacing the original readout with SRP's sparse approximation reconstructs 8.9-17.3 percentage points more of the tested logit differences than the strongest of six baselines built on geometric relations among readout rows. Ablating features shifts logit differences in proportion to their SRP contributions. Although token readings vary with the fitting corpus, the dominant readout feature remains stable. Because SRP uses no corpus in its construction, it provides a control independent of the fitting corpus for lens analyses.

---


### 40. [On-Policy Distillation Meets Off-Policy GRPO: Training Compact Instruction-Following Rerankers](https://arxiv.org/abs/2609.01947)

**<font color=#1a73e8>作者：</font>** Vignesh Prabhakar, Jialing Pan, Anil Babu Ankisettipalli  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Compact instruction-following rerankers are attractive for deployment, but conventional distillation pipelines typically train students by offline imitation of teacher outputs on a fixed set of examples, constraining supervision to the teacher's observed ranking space. We revisit reranker distillation through the lens of reinforcement learning.
We propose a two-stage framework combining off-policy teacher optimization with on-policy student distillation. In Stage 1, a 4B teacher reranker is strengthened with off-policy GRPO using LLM-judge feedback on 88K instruction-following examples. In Stage 2, a compact 1B student samples rankings from its own policy and receives soft teacher-derived rewards on those rankings, coupling student exploration with knowledge transfer.
Our strongest gains appear under distribution shift. On MAIR-11, the original 11-subset, 869-query evaluation, the proposed student reaches 0.7670 nDCG@6, outperforming offline listwise KD by +4.6 points. Controlled comparisons against offline pairwise RankNet KD and on-policy GKD show that neither changing the offline distillation objective nor moving teacher-distribution matching on-policy reproduces the performance of reward-based on-policy distillation over student-sampled rankings. The advantage persists on MAIR-Full: across all 126 tasks and 9,356 queries, the proposed method obtains the highest task-macro point estimates among the evaluated distillation variants, reaching 0.6808 nDCG@6 and 0.7865 MRR@6. It also exceeds two released 7B RL-trained rerankers on the comparable MAIR-11 evaluation, while the same Stage 2 training procedure consistently improves three architecturally distinct alternative student backbones.
On the 9,861-query validation benchmark, the resulting 1B reranker achieves 0.7624 nDCG@6 while providing a favorable quality-efficiency tradeoff relative to larger alternatives.

---


### 41. [Post-Training Ternarization of Qwen3-4B Capability, Effective Bit Budget, Storage Compression, and Deployment](https://arxiv.org/abs/2609.01962)

**<font color=#1a73e8>作者：</font>** Anirudh Malik, M Sparsh Mehra, Poojith Devan  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Ultra-low-bit language models can reduce storage and memory bandwidth, but a nominal "1.58-bit" label does not fully describe the stored representation, retained capability, or runtime behavior.
We study an end-to-end post-training conversion of Qwen, an instruction-tuned 4B-parameter model, using KOTMS rotation, E2M-ATQ ternarization, and GPTQ-style error compensation from TWLA. The experiment is weight-only: activations remain at 16-bit precision, so ILA-AMP is omitted. We evaluate effective bit accounting, task capability retention, perplexity, calibration sensitivity, checkpoint composition, and deployment behavior.
The final conversion uses 1.641 effective bits per weight for quantized linear weights, with 81.62% of model parameters targeted. Across ten scored capability comparisons, accuracy falls from 64.5% to 54.7%. Degradation is uneven: BoolQ retains 84.6% chance-corrected teacher performance, while ARC-Challenge retains 43.8%. Perplexity rises from 13.639 to 18.748 on WikiText-2, 24.700 to 31.992 on PTB, and 19.831 to 28.966 on C4.
A subsequent packing run preserves the ternary planes and scales, reducing reported model size from 8.29 GiB to 3.96 GiB with essentially unchanged perplexity. A separate third-party packing attempt was lossy and is excluded from the primary artifact claim. The packed artifact has not been benchmarked end-to-end for task accuracy or generation throughput. A preliminary Triton GEMV microbenchmark is 4.6x slower than FP16 cuBLAS on one tested shape. We therefore do not claim that compression alone yields faster inference.

---


### 42. [NS-Copilot: An LLM-Driven Agent System for Autonomous Neuroscience Analysis](https://arxiv.org/abs/2609.01971)

**<font color=#1a73e8>作者：</font>** Wuche Liu, Yiran Qiao, Linlin Hou 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> AI is rapidly advancing neuroscience, yet many laboratories fail to fully unleash its potential due to significant interdisciplinary barriers. While pre-trained neural models for physiological data are progressing quickly, their heterogeneous architectures and modality-specific constraints hinder systematic integration, selection, and evaluation. Despite recent advances in large language model (LLM)-based agent systems for intelligent scientific applications, existing approaches often still lack the domain expertise required to effectively select and coordinate diverse neuroscience pre-trained models and handle unique data types in this domain. We present NS-Copilot, an LLM-driven multi-agent system for neuroscience analysis that autonomously supports end-to-end workflows for diverse professional tasks. It unifies domain-specific pre-trained models and supports key neuroscience modalities, including EEG and extracellular spike data, through a natural-language interface. Given raw data and a task description, NS-Copilot orchestrates agents with specialized roles for planning, adaptive control, code generation, and result synthesis, enabling analysis without dataset-specific heuristics. We evaluate NS-Copilot on neuroscience benchmarks spanning Alzheimer's disease, Parkinson's disease, and working memory spike decoding. Across 8 trials per task, the system consistently outperforms strong baselines on the primary metric, demonstrating the ability of NS-Copilot for effective and scalable neuroscience analysis.

---


### 43. [Knowing Is Not Enough: Information Retrievability as a Precondition to Effective LLM Oversight](https://arxiv.org/abs/2609.01976)

**<font color=#1a73e8>作者：</font>** Xinyu Fu, Narayan Ramasubbu, Dennis Galletta  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly embedded in organizational work, yet their errors often pass human review. Prior research locates such failures in users' capability to review LLM output or their engagement in doing so. We develop an alternative, retrieval-based account of human oversight and posit that error detection is more effective when oversight-relevant information is accessible to users at the moment of review. Across two randomized lab-in-the-field experiments with 640 customer-facing employees, we show that self-generated explanations improve error detection and strengthen recall of verification-relevant reasoning, while cues that reactivate such reasoning help sustain detection under repeated LLM use. Theoretically, we identify information retrievability as a distinct precondition for effective oversight and specify generative encoding and cue-supported reactivation as mechanisms that build and sustain it. Practically, lightweight onboarding self-explanations and daily retrieval cues can make human oversight more resilient as LLM use becomes routine.

---


### 44. [Benchmarking Language Models for Statistical Problem Formulation](https://arxiv.org/abs/2609.01982)

**<font color=#1a73e8>作者：</font>** Chen Wang, Junzhe Zhao, Xin Cong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used as assistants for statistical and data science work, yet existing evaluations largely assume the analysis target is already specified. In practice, users arrive with informal goals and heterogeneous data, leaving the model to decide what statistical task is implied and which data are relevant. We first formalize this upstream step as Statistical Problem Formulation and decompose it into two subtasks: (1) Statistical Problem Classification and (2) Variable Identification & Role Assignment. We then introduce StatFormBench, a benchmark built from five cross-domain statistics textbooks and a data science case library, covering diverse problem types, data representations, and scenario styles. It contains 1,013 samples spanning 20 coarse-grained and 85 fine-grained statistical problem categories. Across 14 open- and closed-source LLMs, the best zero-shot models reach only 72.0 fine-grained classification accuracy and 63.2 variable set overlap. No model performs consistently best across the two subtasks, while enhanced prompting strategies yield only limited or inconsistent gains. We release the benchmark data on Hugging Face at this https URL and the evaluation code on GitHub at this https URL.

---


### 45. [When Agents Implement Systems: A Case Study in Defects, Detection, and Evaluation Rigor](https://arxiv.org/abs/2609.01985)

**<font color=#1a73e8>作者：</font>** Phanindra Reddy Madduru  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM coding agents increasingly perform end-to-end engineering work, we lack empirical characterization of how they behave on systems-level requirements: schema design, async orchestration, configuration correctness, and retrieval-filtering trade-offs. We present a case study of one such agent implementing a multi-component data system against a detailed pre-existing specification. Storage technologies, schema, entity-resolution algorithm, and retrieval-filtering strategy were fixed in advance; the agent autonomy was in the implementation, in diagnosing and fixing defects it introduced, and in interaction-design choices left open. Over a single session, we catalog five such defects, categorized by constraint violated and detection method. We further evaluate, on the public HotpotQA benchmark, the one retrieval trade-off specified in that architecture: restricting candidates to a graph-identified entity set before ranking versus unfiltered search. We substitute the benchmark gold evidence labels for entity identification, since we lacked LLM access to run that stage, and report standard recall rather than the benchmark own accuracy metrics. Across retrieval budgets from 1 to 10 and 100 questions against a pooled corpus of 2994 paragraphs, filtered recall reaches its ceiling by a budget of 3, expected once candidates are restricted to the gold paragraphs themselves, while unfiltered search recovers all required evidence only 69 percent of the time even at a budget of 10, a gap that holds at every budget tested, with sign test p less than 0.0001. We close with a discussion of where the agent autonomy succeeded versus required correction, including one instance where a claimed performance fix was never re-measured on the regression that motivated it.

---


### 46. [Who Drives the Probability Game of VLMs? A Temporal Causal Drive Evaluation Framework](https://arxiv.org/abs/2609.02000)

**<font color=#1a73e8>作者：</font>** Shuyao Xiao, Shengling Wang, Haoyu Niu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly evaluated on complex image and video understanding tasks, yet conventional metrics primarily assess final-answer quality and reveal little about how different information sources shape the generation process. We propose a causal and temporal evaluation framework that traces the evolving roles of visual input, question text, and generated prefixes during autoregressive decoding. Grounded in a Structural Causal Model, we use interventions and backdoor adjustment to derive three step-indexed causal-drive metrics---Visual Causal Drive (VCD), Question Causal Drive (QCD), and Prefix Causal Drive (PCD)---for characterizing source-specific generation patterns without requiring reference answers. Experiments on Qwen3-VL-8B-Instruct across MAVIS, LLaVA-Video-178K, and MiraData, together with cross-model validation on InternVL2-8B, reveal a consistent transition from stronger early question and visual guidance toward increasing reliance on generated prefixes. Randomized-intervention validation shows that QCD and PCD reduce recovery error over observational PMI baselines by 34.8\% and 47.1\%, respectively. On VLMBias, the prefix--visual imbalance score achieves 0.767 AUROC and 0.873 AUPRC for distinguishing prior-driven from visually grounded generations. These results show that causal-drive trajectories provide complementary source-level diagnostics for multimodal generation.

---


### 47. [Train What You Deploy: Closing the MLP Reachability Gap in Low-Rank Clone Distillation](https://arxiv.org/abs/2609.02006)

**<font color=#1a73e8>作者：</font>** Wenhui Chen, Zhifeng Li, Jie Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A compressed student has two shapes that need not agree: the weight it deploys at inference and the weight family its training can reach. We show that a state-of-the-art weight-inheritance distiller, Low-Rank Clone (LRC), deploys a full-width student MLP but ties training to a teacher-induced slice, leaving 62.5-81.4% of each deployed matrix's independent linear degrees of freedom unreachable-paid for at inference, never trainable. Our principle is one line: train what you deploy. From the identical LRC warm start, we make the training object the entire deployed matrix, with no change in deployed shape, deployed parameter count, or inference FLOPs, via two mergeable realizations (Dense-LRC and CORE-LRC) that both collapse to one deployed weight. This recovers stranded capacity: taking the stronger realization per teacher, +2.36/+2.71/+10.45 Avg9 over matched-budget plain-LRC baselines across three teachers (Llama3.2-3B, Llama3.1-8B, Qwen2.5-3B), with the largest gain on the widest teacher (Qwen), where it reaches the original recipe's approx. 20B-token accuracy at 10B tokens (2x token efficiency); there the strictly same-lineage arm still recovers +6.39, the fully controlled figure. Controls strongly support attributing the gain to the enlarged reachable set, rather than to added parameters or the recipe. From approx. 10B distillation tokens plus a short SFT, a half-parameter 1.5B student matches its approx. 9T-token teacher's 9-task macro-average, within evaluation noise and with a residual MMLU deficit, and a 2.7B student beats Meta's own official compression of Llama3.1-8B at ~900x fewer compression tokens (a token count under unmatched recipes, not a compute claim). All results are from single-seed runs on the LRC backbone.

---


### 48. [How Output Format Confounds Data Quality and Capability in Instruction Tuning](https://arxiv.org/abs/2609.02015)

**<font color=#1a73e8>作者：</font>** Chengguang Gan, Hanjun Wei, Yunhao Liang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Instruction-tuning data are judged by quality metrics, and tuned models are judged by benchmarks, but both judgments pass through an output interface: the surface format in which an answer is written. Using gradient signatures across 12 tasks, four semantically equivalent interfaces, three model families, and controlled corruptions, we show that this interface confounds both measurements. Spectral statistics such as effective rank are provably invariant to interface rotation and empirically blind to semantic corruption, while the direction of the update carries the quality signal. The interface-varying residual is not noise: it identifies each unit's own target task perfectly across all three families. Capability itself is stored relative to the training interface: a skill that raises accuracy by more than 40 points under the training format can be nearly invisible under every other, and correcting a single generation budget flips the measured effect of fine-tuning on GSM8K from a gain into a large loss. Pre-registered interventions delimit where this geometry stops short of control. Data quality and model capability are interface-conditioned quantities, and current practice often reports the interface instead of the content.

---


### 49. [Detecting Object Hallucinations in Large Vision-Language Models via Cross-Modal Attention Drifts and Mask-Based Verification](https://arxiv.org/abs/2609.02028)

**<font color=#1a73e8>作者：</font>** Xuanbing Wen, Boxu Chen, Le Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Despite recent advances in large vision-language models (LVLMs), object hallucination remains a major barrier to their reliable deployment. Existing detection methods often characterize visual grounding using attention from individual layers, leaving its evolution across layers underexplored. We propose CADMP, a lightweight object hallucination detection framework that combines adjacent-layer cross-modal attention drift with prediction sensitivity to targeted visual masking. During decoding, CADMP quantifies distributional changes between consecutive cross-modal attention maps to capture abrupt transitions in visual grounding. It then selects the transition with the largest drift, locates the corresponding visually relevant regions, and measures the change in prediction probability after masking these regions. These two signals provide complementary evidence: attention drift characterizes the stability of internal visual grounding, while probability variation verifies whether a prediction truly depends on the identified visual evidence. A lightweight detector integrates both signals to identify hallucinated predictions. Experiments on multiple benchmarks and representative open-source LVLMs demonstrate that CADMP achieves consistently competitive detection performance. Ablation studies further confirm the complementary contributions of adjacent-layer drift modeling and mask-based grounding verification.

---


### 50. [HeadWiseKV: Budgeted Per-Head Cache Residency for Hybrid Long-Context Language Models](https://arxiv.org/abs/2609.02029)

**<font color=#1a73e8>作者：</font>** Renjie Xie, Juncheng Yang, Aoting Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context inference retains a growing key--value (KV) cache during decoding, which consumes substantial GPU memory and can reduce generation throughput. This bottleneck remains in hybrid language models because their residual global-attention layers can dominate context-dependent cache demand. We study how to allocate this state under an aggregate KV-residency budget. We introduce HeadWiseKV, a training-free framework that compresses the residual global KV caches of hybrid language models while preserving their native local, recurrent, and linear paths. It assigns each physical KV head a static, multilevel history window, making cache demand predictable before serving. We formulate this allocation as a restricted operational rate--distortion problem and propose SeqCalib as the core policy-generation algorithm in HeadWiseKV. SeqCalib processes layers in execution order and conditions each decision on the lower-layer policy used at deployment, thereby accounting for interactions across depth. A grouped-cache runtime materializes the selected policy as actual per-head KV residency rather than a mask over a full cache. We evaluate downstream quality across four hybrid long-context models and study physical residency and serving behavior on Qwen3.6-27B. HeadWiseKV retains near-Full-KV RULER and LoCoMo quality across the evaluated models. In the fixed-model systems study, it reduces sampled peak device memory by 8.59\% at a 112K context length and extends the largest verified successful context from 114K to 161K.

---


> [!TIP]
> 当前位于：**1-50**（第 1/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-177](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
