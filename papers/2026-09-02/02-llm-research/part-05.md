# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

---

### 201. [POLYFLOW: A Neuro-Symbolic Framework for Static Cross-Language Information Flow Analysis](https://arxiv.org/abs/2608.29808)

**<font color=#1a73e8>作者：</font>** Haoran Yang, Zhixuan Zhong, Jiawei Guo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern software systems are commonly constructed in multiple, interacting programming languages. This construction leads to additional, often stealthy vulnerabilities buried in complex information flow due to language interactions. Existing static analyzers are impeded by the heterogeneous semantics of different languages, whereas dynamic approaches suffer from the limited coverage of (available and/or generated) test inputs. In this paper, we develop PolyFlow, a neural-symbolic framework for statically reasoning about information flow across language boundaries, combining large language models (LLMs) and static analysis synergistically. Governed by the control-flow representation of a given multi-language system, PolyFlow leverages LLMs to identify implicit flow facts due to challenging language features, hence augmenting the base representation and then propagating data flow through the system. It tackles inherent barriers (e.g., token limit and hallucination) of LLMs by putting them under careful guidance (e.g., static-analysis-guided scoping, context management, and fact checking), along with a multi-LLM expert panel for negotiated validation. Our experiments on real-world Python-C and Java-C systems show that PolyFlow is cost-effective and superior to various kinds of state-of-the-art baselines, revealing previously unknown cross-language vulnerabilities that are missed by all the baselines.

---


### 202. [FRAMEWORKERS: A Dynamic Multi-Agent Framework for AI-Generated Video Production](https://arxiv.org/abs/2608.29814)

**<font color=#1a73e8>作者：</font>** Zhendong Li, Lei Sun, Letian Shi 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Modern video generators excel at synthesizing individual clips, but complete video production requires coordinating a long sequence of interdependent creative steps, including scripting, storyboarding, generation, and editing. It further demands persistent asset management and dynamic task orchestration as intermediate outputs, dependencies, and execution states evolve over time. Existing automated systems typically rely on rigid pipelines that are difficult to adapt to diverse inputs and changing workflows, while general-purpose large language models (LLMs) remain unreliable for long-horizon orchestration and multimodal asset routing. We introduce FRAMEWORKERS, a task-centric and workspace-grounded multi-agent framework for open-ended video production. A central Director formulates video creation as dynamic task management, continuously editing a Task Stack to determine which subtask to execute next and which sub-agent to invoke. An Assistant serves as the execution layer, grounding each selected task in a shared Workspace, retrieving the required assets and context, invoking the assigned sub-agent, and persisting the resulting artifacts. Execution capabilities are exposed through modular sub-agents with registered descriptors, allowing new sub-agents to be integrated without redesigning the orchestration workflow. To improve orchestration reliability, we fine-tune the Director via supervised fine-tuning (SFT) followed by Group Relative Policy Optimization (GRPO) for descriptor-conditioned task routing. Experiments show that FRAMEWORKERS outperforms strong LLM planners in routing accuracy, recovers reliably from runtime failures, generalizes to unseen sub-agents without retraining, and achieves higher end-to-end video quality and broader task coverage than fixed pipelines, single-agent systems, and prior multi-agent approaches.

---


### 203. [Structure Aware Neural Architecture Search for Mixture of Experts](https://arxiv.org/abs/2608.29817)

**<font color=#1a73e8>作者：</font>** Petr Babkin, Oleg Bakhteev  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Neural Architecture Search (NAS) has so far rarely been applied to Mixture-of-Experts (MoE) models, and existing MoE designs leave the alignment between experts and the structure of the data to emerge on its own. We propose an architecture search framework that makes this alignment an explicit search variable: the assignment of data clusters to experts is optimised jointly with the per-expert architectures. We cast the joint problem as a cluster-aware likelihood maximisation, show that it coincides with the incomplete-data maximum likelihood of a latent-variable mixture, and solve it by a generalised Expectation-Maximisation procedure whose otherwise intractable expert-quality term is supplied by an adaptively refined surrogate. We prove that the iterates converge whenever the surrogate errors are summable, and that at every limit point no candidate the search produces improves the true objective. On a heterogeneous image-classification mixture the method recovers the underlying domain partition on 95% of clusters without ever observing domain labels, and on that benchmark and a four-domain time-series forecasting one alike it outperforms the MoE and NAS baselines that likewise use no label information.

---


### 204. [EVAR: Evidence-Validated Hypothesis Admission for Budget-Aware Narrative Reasoning](https://arxiv.org/abs/2608.29835)

**<font color=#1a73e8>作者：</font>** Peilin Liu, Zhiquan Ji, Jinglong Ping  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often produce fluent but weakly grounded conclusions when reasoning over non-interactive, long-form narratives. A central failure mode is that unsupported intermediate hypotheses can enter the reasoning trajectory and contaminate subsequent inference, especially when evidence is scattered across distant parts of the story. To address this problem, we propose EVAR, an evidence-validated hypothesis admission framework for budget-aware narrative reasoning. EVAR first compiles the narrative into an immutable evidence store of source-linked atomic claims and assigns an instance-specific inference budget from unresolved gaps and uncertainty signals. During refinement, EVAR directly proposes candidate hypotheses for unresolved gaps, constructs hypothesis-conditioned validation challenges, and verifies each candidate against the locked store before admission: supported hypotheses enter the answer-supporting state, unverifiable ones are quarantined, and contradictory ones are discarded. A sufficiency-based stopping mechanism further avoids unnecessary refinement. Experiments on NarraCrime and multiple public reasoning benchmarks show that EVAR improves both task performance and evidence faithfulness while maintaining controllable inference cost.

---


### 205. [Influence-Directed Distillation: Solving the Diversity Bottleneck in Sampled-Token On-Policy Distillation](https://arxiv.org/abs/2608.29846)

**<font color=#1a73e8>作者：</font>** Run Yang, Runpeng Dai, Jie Sun 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Sampled-token on-policy distillation (OPD) efficiently transfers capabilities from teacher to student using student-generated tokens, requiring teacher probabilities only for sampled tokens. Yet it frequently suffers from diversity distillation failure: the student's pass@1 improves while its pass@$k$ plateaus, failing to inherit the teacher's diversity. To explain this, we introduce First-Order Local Entropy Influence, a signed first-order proxy that decouples each update's entropy effect into the teacher--student log-probability gap and the student's local probability structure, and empirically links entropy contraction to negative-influence positions. Motivated by this, we propose Influence-Directed Adaptive On-Policy Distillation (IDA-OPD): rather than relying on costly full-vocabulary Forward-KL objectives, it preserves entropy-expanding updates while replacing entropy-contracting ones with divergence-adaptive advantage shrinkage, using only the teacher's sampled-token log-probability. Experiments on reasoning-oriented distillation show IDA-OPD consistently improves pass@$k$, inheriting the teacher's diversity through distillation, matches the strongest teacher-informed methods at strictly lower cost, and broadly maintains vanilla OPD's pass@1, all without full-vocabulary teacher information.

---


### 206. [GenRubric: Self-Evolving Rubric Generation for Scalable LLM Evaluation](https://arxiv.org/abs/2608.29856)

**<font color=#1a73e8>作者：</font>** Yifan Chen, Haitao Li, Qingyao Ai 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as scalable evaluators for open-ended tasks. However, many LLM judges derive query-specific criteria during scoring, leaving the evaluation requirements insufficiently specified and their coverage difficult to audit. Query-specific rubrics make these requirements explicit, but expert-written rubrics are costly to construct, while existing automatic methods typically rely on inference-time refinement or external supervision. We introduce GenRubric, a self-evolving framework that improves rubric generation from unlabeled queries without requiring additional human annotations during self-evolution. Our approach is based on rubric-induced self-consistency: independently sampled rubrics for the same query provide partial views of its latent evaluation requirements, and a comprehensive rubric should induce a response that generalizes across these complementary evaluation views. We implement this principle through reinforcement learning, combining a cross-rubric comprehensiveness signal with group-level and criterion-level rewards for rubric quality. We train GenRubric models at 4B, 8B, and 14B scales across multiple domains. Experiments on human-annotated rubric benchmarks show that self-evolution improves the agreement between evaluations induced by generated rubrics and those induced by expert-written rubrics. The improvements further generalize to held-out domains, demonstrating the potential of self-evolving rubric generation for scalable and query-specific LLM evaluation. Code and models are publicly available at this https URL.

---


### 207. [Perceive to Hypothesize, Verify to Ground: An Agentic Reasoning Framework for Open-World Geo-Localization](https://arxiv.org/abs/2608.29880)

**<font color=#1a73e8>作者：</font>** Yutian Jiang, Ruijie Li, Sisuo Lyu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Open-world geo-localization requires models to reason over ambiguous visual cues through multi-step reasoning and external knowledge grounding. While recent large vision-language models exhibit strong multimodal reasoning capabilities, existing approaches still suffer from perceptual hallucination and context drift due to the lack of explicit evidence-grounded verification. In this work, we reformulate geo-localization as a human-like perceive-then-verify reasoning problem and propose GeoPAVE (Geo-localization Perception-and-Verification-Engine), a bi-level agentic framework that contains perception-based hypothesis generation via single-pass rollouts and verification-based evidence grounding for decision actions: support, refute, and refine. To support rigorous evaluation, we further introduce PAVED, a novel dataset derived from real-world user check-in data, equipped with comprehensive reasoning trajectories featuring multi-hop queries, multi-round tool invocations, and structured perception-verification traces. The dataset and code are available at this https URL.

---


### 208. [Improving Argument Saliency Coverage in Small LLMs for Long Legal Opinion Summarization via Sequence-Level Distillation](https://arxiv.org/abs/2608.29884)

**<font color=#1a73e8>作者：</font>** Mohamed Elaraby, Ahmed Elhady, Diane Litman  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We show that sequence-level distillation from a capable long-context teacher model is a simple, annotation-free, and data-efficient strategy for improving argument saliency coverage in long legal opinion summarization, where small LLMs often struggle to retain the most salient argumentative content. Across student model sizes, distillation consistently surpasses tuning on expert-written summaries in our legal-opinion setting. We further demonstrate that most gains are achieved with as few as ~10 training summaries, highlighting the strong data efficiency of teacher-generated supervision. Finally, we find that summary distillation is sufficient for improvements: reasoning-chain distillation remains competitive with summary-only distillation, but provides marginal benefit when combined with summary supervision.

---


### 209. [Check The Scoreboard: An Analysis of Scoring Schemes on Multiple-Choice Evaluation](https://arxiv.org/abs/2608.29887)

**<font color=#1a73e8>作者：</font>** Nishant Balepur, Paiheng Xu, Wei Ai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multiple-choice question answering (MCQA) benchmarks in NLP use number-right scoring (accuracy), but in educational testing, the scoring scheme, the combination of the response mode models follow and the rule for grading responses, is a key design choice that dictates which abilities to reward. We examine how alternatives to number right change what MCQA measures with six education-inspired schemes that assess abilities beyond accuracy: distractor elimination, abstention, confidence calibration, and self-correction. On LLM benchmarks, these schemes: 1) shift rankings of 31 LLMs beyond rephrased number right prompts; 2) better predict the LLMs users prefer in LLM Arena; and 3) reveal distinct model capabilities, like that GPT-5 rarely abstains and readily self-corrects, while weaker open-weight models often abstain and hesitate to eliminate choices. Given the benefits of alternative scoring schemes, we discuss ways to extend them to tasks beyond MCQA.

---


### 210. [VibeJam: A User Study Platform for Web Development with Agents](https://arxiv.org/abs/2608.29889)

**<font color=#1a73e8>作者：</font>** Nishant Balepur, Connor Baumler, Valerie Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Programming with AI is increasingly agentic, users prompt LLMs to directly edit their code and review the changes, with adoption growing especially for web development tasks. Despite this growth, most NLP work uses offline evaluation and lacks support for online studies, losing insights into how programmers truly use coding agents. We release VibeJam, a browser-based user study platform for users to collaborate with AI agents to develop websites. VibeJam enables agent customization and uses the open-source Aider agent by default, and to mirror downstream use, we add diff review, chat and plan modes, and live website previews. In a pilot study with 55 released, game-based website creation tasks, five experienced AI programmers rate our system as fun, simple, and resembling commercial tools, while 13 junior students use VibeJam to make websites of higher quality than agents in the same task. We open-source VibeJam to spur extensions and support studies on how coding agents can help users.

---


### 211. [En-ViMedNER: An English-Vietnamese Parallel Biomedical Corpus with UMLS Semantic Type Annotations](https://arxiv.org/abs/2608.29890)

**<font color=#1a73e8>作者：</font>** Nhu Vo, Phuong Nguyen, Nu Uyen Phuong Le 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Biomedical Named Entity Recognition (NER) is fundamental to healthcare AI applications, including clinical decision support and medical information extraction. While corpora with Unified Medical Language System (UMLS) annotations, such as MedMentions, have driven progress in English biomedical NER, no comparable resource exists for Vietnamese. This paper presents En-ViMedNER, the first English-Vietnamese parallel biomedical NER corpus annotated with UMLS semantic types, which are language-neutral codes providing a shared cross-lingual label space and ensuring direct comparability with existing UMLS-based resources. The corpus contains 4,392 PubMed abstract pairs, 44,892 English-Vietnamese sentence pairs, and 202,949 aligned entity-mention pairs across 21 semantic types adapted from the MedMentions ST21pv dataset. To balance quality and scalability, we have constructed the corpus through automatic translation, expert post-editing, LLM-assisted label projection, and human verification and adjudication. We characterize En-ViMedNER as a large-scale silver-standard corpus with a human-audited and consensus-corrected mini-test subset. We evaluate En-ViMedNER in two settings: (i) Vietnamese-input/Vietnamese-output biomedical NER and (ii) English-input/Vietnamese-output cross-lingual NER. For Vietnamese NER, we benchmark Vietnamese-supervised encoder models, English-supervised multilingual encoder models, and prompt-based LLMs. The best model achieves an F1 score of 52.70 on the test set and 53.78 on the mini-test set. For cross-lingual NER, we benchmark encoder-decoder models and prompt-based LLMs. The best model achieves an F1 score of 45.44 on the mini-test set. We publicly release our corpus, corpus construction pipeline, and baseline models to facilitate future Vietnamese biomedical NLP research.

---


### 212. [REIGN: Refurbished Embeddings with Integrated Guidance Networks for Efficient Context-Length Scaling](https://arxiv.org/abs/2608.29899)

**<font color=#1a73e8>作者：</font>** Devrim Çavuşoğlu, Emre Akbaş  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dense retrieval over long documents is expensive. Token-level encoders scale quadratically in sequence length, and most long-context embedding models reach 32K tokens only through architectural workarounds or by stretching billion-parameter LLMs. We propose REIGN (Refurbished Embeddings with Integrated Guidance Networks), a contrastively trained bi-encoder that operates on sequences of contextualised chunk embeddings from a frozen Guidance Network (GN) rather than on raw tokens. REIGN targets multi-chunk inputs, primarily for document-to-document retrieval; single-chunk inputs stay with the GN. Decoupling token-level processing from document-level reasoning, and caching the GN embeddings to disk, cuts per-document training cost by roughly four orders of magnitude relative to chunked Transformer fine-tuning. We also release a synthetic long-document retrieval benchmark for contrastive training and evaluation at long context lengths. Across an in-distribution Wikipedia benchmark, the LoCo out-of-distribution suite, and a real-world patent retrieval case study, REIGN matches dense long-context retrievers at smaller parameter budgets in each regime. A paired significance test puts it on par with models 1.6-4.3x larger on the patent task, and it stays within 0.65 nDCG@10 of a 20x-larger model on LoCo.

---


### 213. [When Less is More: Understanding When Token Filtering Helps and Fails in AI-generated Text Detection](https://arxiv.org/abs/2608.29903)

**<font color=#1a73e8>作者：</font>** Xiaoyang Han, Lvxiaowei Xu, Ming Cai  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid advancement of large language models (LLMs) has made AI-generated text detection increasingly critical. Existing zero-shot detectors assume that more token-level evidence leads to more reliable detection. However, our empirical study challenges this consensus: fewer tokens sometimes work better, retaining only 40% can yield optimal performance, yet this benefit is not universal. Using the Entropy Gap Score (EGS), we introduce top-$k$ cumulative probability filtering as a diagnostic probe. Across three representative settings, filtering exhibits strikingly different behaviors. We analyze EGS via typical set theory and quantify its dynamics through entropy calibration and distribution analysis. We find that filtering helps for weak source LMs, where low-entropy tokens are harmful, but fails for strong source LMs, where they are not notably harmful. Our work provides the first systematic analysis showing that some tokens are not merely uninformative but systematically harmful due to entropy miscalibration, revealing a two-sided trade-off in token-level detection.

---


### 214. [IndicDetect: Evaluating Cross-Lingual LLM-Generated Text Detection for Hindi, Telugu, and Tamil](https://arxiv.org/abs/2608.29919)

**<font color=#1a73e8>作者：</font>** Bhaskar Ganesh Devalla, Junchao Wu, Nilesh Dokuparthi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid proliferation of LLMs has further heightened the need to develop dependable AI-generated text detection, especially beyond English. Nevertheless, current benchmarks pay little attention to Indic languages and test detectors in idealized settings that do not represent the real world. We present a generalized benchmark for AI-generated text detection in Hindi, Telugu, and Tamil, which we call IndicDetect, designed to assess the robustness of detectors under realistic distribution shifts. IndicDetect comprises highly curated human-written texts matched with LLM-generated counterparts across various domains and generators, and systematically evaluates detectors in the presence of domain shift, generator shift, and adversarial perturbation. Using a single and repeatable evaluation scheme, we evaluate a wide range of statistical and neural detectors. We find substantial robustness failures: supervised neural detectors perform well in-distribution, while training-free methods degrade considerably under unseen generators and adversarial attacks. The severity of these failures varies across languages, with Hindi exhibiting the largest overall degradation under adversarial perturbations. These results highlight that the primary weakness of existing detectors in Indic settings lies in their robustness, not in their peak accuracy. IndicDetect provides standard data splits, an evaluation protocol, and baselines to establish a robust, language-aware foundation for AI-generated text detection in Indic scripts.

---


### 215. [Sleight of Word Benchmark: Can Language Models Notice If Their Own Output Was Tampered With?](https://arxiv.org/abs/2608.29921)

**<font color=#1a73e8>作者：</font>** Alberto Cetoli  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The output of a Language Model can be tampered with \emph{while} the model is writing it. A simple test can thus be constructed by evaluating the model's perception of this external perturbation. In this spirit, a simple benchmark is built in which a single word is consistently substituted with another in the generation process. We call this method \emph{Sleight of Word}. Two distinct axes are measured: metrics that relate to the model's surprise, as well as an evaluation of the textual reaction for 19 different open-weight language models.

---


### 216. [Towards Continual Test-Time Adaptation of Vision-Language Models in Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2608.29923)

**<font color=#1a73e8>作者：</font>** Chandler Timm C. Doloriel, Yunbei Zhang, Sarthak Kumar Maharana 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Open-vocabulary semantic segmentation (OVSS) relies on vision-language alignment to recognize arbitrary text-defined categories, yet this alignment is fragile under continual test-time distribution shift. Our diagnostic analysis reveals that entropy minimization drives patch-level class collapse, continual updates erode vision-language alignment, and redundant gradients from low-shift samples waste computation. We propose Diversify, Anchor, and Filter (DAF), a stabilization framework that augments entropy-based adaptation with a marginal diversity loss that resists collapse, a cross-modal anchor consistency loss that constrains feature drift relative to a frozen source model, and feature salience filtering that skips low-value backward passes to offset part of the source-anchor overhead. We evaluate on five datasets spanning natural scenes, autonomous driving, underwater imagery, and remote sensing with their corrupted variants. Across the evaluated continual shifts, DAF remains stable where entropy minimization collapses, improving mIoU by over 8 points on Pascal VOC20-C, over 9 points on LoveDA, and over 3 points on Foggy Cityscapes compared to the source model, and is robust to aggressive adaptation and learning rate choices.

---


### 217. [Hallucination Mitigation for Large Vision-Language Models via Implicit Feature Stabilization](https://arxiv.org/abs/2608.29924)

**<font color=#1a73e8>作者：</font>** Aditi Sarker, Rafi Ibn Sultan, Hui Zhu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) are prone to hallucinations: they fluently describe objects, attributes, and scenes that are not in the image. We connect part of this failure to a measurable property of their representations, feature instability, where mild semantics-preserving perturbations of the input cause large changes in the learned embeddings; hallucination rates rise together with this variability. Existing stability-motivated remedies are explicit, in the sense that they intervene at inference time through latent steering or constrained decoding, and pay for it on every query. We propose implicit stabilization instead: perturbation-invariance is built into the model weights during fine-tuning, and nothing extra runs at deployment. Our framework, INFUSE, first stabilizes visual and textual representations around perturbation-averaged and ground-truth anchors, then aligns the stabilized representations across modalities with bidirectional contrastive objectives. We prove that the anchor's root-mean-square deviation from the perturbation-mean representation shrinks at rate $1/\sqrt{K}$ in the number of views, and that under a Lipschitz decoder, this bounds how much any perturbation can change the model's hallucination behavior. On LLaVA-1.5, LLaVA-1.6, and Qwen3-VL-8B-Instruct, INFUSE reduces AMBER CHAIR by 46-63% relative to each base model, improves ObjHal, MMHal, HallusionBench, and POPE, and preserves VQA-v2 and TextVQA, all with no inference-time overhead.

---


### 218. [Token Counts Are Not Model Lineage: A Frozen-Threshold Holdout Study of Black-Box LLM API Fingerprinting](https://arxiv.org/abs/2608.29930)

**<font color=#1a73e8>作者：</font>** Bo Chen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Black-box model attribution is increasingly relevant when large language models (LLMs) are served through relay and reseller APIs. A tempting low-cost signal is the prompt-token count returned by an OpenAI-compatible endpoint: two models that share a tokenizer and chat template may produce the same count sequence up to a fixed offset. Yet the validity of this signal for broader \emph{model-family} attribution has received little direct holdout testing. We conduct a frozen-threshold study over 24 labeled endpoint pairs, split evenly into a development set and an untouched holdout set, with three temporal repeats and 30 controlled texts per pair. We introduce a validity-gated result contract that distinguishes an observed dissimilarity from an uninformative measurement caused by missing usage data, rate limits, or endpoint policy. The resulting shift-invariant exact-match score perfectly separates the 12 development pairs, yielding a frozen threshold of 0.725. On holdout, however, only 6 of 12 pairs are eligible under the pre-specified three-repeat rule. Among eligible pairs, balanced accuracy is 0.75, sensitivity is 0.50 (95\% Wilson interval 0.15--0.85), and specificity is 1.00 (0.342--1.00). Two same-family pairs---Qwen 3.8 and DeepSeek V4 variants---fall below the frozen threshold. Across 4,320 formal API calls, every log is replayable, while holdout contains 189 non-200 responses and 157 successful responses without prompt-token usage. The study therefore validates token-count consistency as a fingerprint of a shared \emph{tokenization stack}, but rejects its use as a standalone necessary test for model-family lineage.

---


### 219. [Compression-Aware Abstention: Teaching LLMs to Refuse When KV-Compression Masks Remove Answer Evidence](https://arxiv.org/abs/2608.29934)

**<font color=#1a73e8>作者：</font>** Mohammadali Khodabandehlou, Bhaskar Krishnamachari  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> KV-cache compression reduces LLM inference memory by evicting context tokens, but when the evicted tokens contain answer-bearing evidence, the model may hallucinate instead of recognizing that the compressed context is insufficient. We address this failure from a behavioral perspective: to our knowledge, this is the first work to formulate compression-aware abstention as a learning problem, in which a model learns to answer when supporting evidence survives compression and abstain when it does not. We construct supervision from compressor survival masks and tight answer-bearing spans, labeling examples as Confident when evidence survives and Abstain when it is removed. A 10.1M-parameter LoRA adapter trained on ~2.6K MuSiQue 2-hop QA examples reduces base-model hallucinations by 97% under prompt-style truncation while preserving correct answering on evidence-retaining examples. Unlike prompt-only abstention baselines, which over-abstain on many answerable high-retention examples, the trained adapter learns a conditional policy. We also evaluate the method under actual compressed-cache decoding, where multi-compressor training yields a 6-22x relative lift over the unaided base on evidence-retaining examples. Controlled-deletion experiments show that the learned behavior is driven by evidence content rather than input length alone.

---


### 220. [When Safety Speaks a Language: A Mechanistic Analysis of Safety-Language Identity Entanglement in LLMs](https://arxiv.org/abs/2608.29936)

**<font color=#1a73e8>作者：</font>** Apoorva Upadhyaya, Sandipan Sikdar  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Safety alignment of large language models (LLMs) degrades across languages, yet the internal mechanism driving this asymmetry remains poorly understood. Our work, therefore, presents a systematic mechanistic analysis of multilingual safety using sparse autoencoder (SAE) features, sparse interpretable directions in the residual stream associated with harmful and harmless model behavior across three instruction-tuned LLMs, eight languages, and all model layers. We observe that safety-relevant features are architecture-dependent in terms of where they are located and how they are distributed across layers. Additionally, they are geometrically entangled with language identity and exhibit cross-lingual sharing patterns, i.e., languages share safety features to varying degrees across model depths and architectures. This safety-language entanglement has direct consequences such that ablating safety features impacts not only harmful response rates but also target language, with the degree of intervention predicted by the relationship between safety and language features. Our findings qualify the language-universality of safety alignment as architecture-dependent and offer a mechanistic account of multilingual safety interventions.

---


### 221. [AcrossWAM1.0:A Modular Latent World-Action Stack for Compact Robot Policies](https://arxiv.org/abs/2608.29937)

**<font color=#1a73e8>作者：</font>** Yafei Zhang, Nan Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Latent world-action models avoid rendering future pixels by predicting an action-relevant visual subgoal in feature space. LaWAM established this formulation, but its original presentation left the world model, multimodal backbone, and deployment checkpoint tightly coupled. We introduce AcrossWAM1.0, a modularization and scaling study of this latent world-action stack. Rather than presenting latent subgoals as a new algorithm, we make the module boundary explicit: a policy adapter produces latent-action and action-generation contexts; a retained latent world decoder grounds the predicted transition in the current scene;and a flow-matching expert generates continuous action chunks. We further separate training-only teachers from the inference graph and provide a verifiable deployment export. On 2,000 paired LIBERO episodes, replacing a Qwen3-VL-2B backbone with Qwen3.5-0.8B yields 97.45% success versus 98.00% for the 2B model (a-0.55percentage-point difference; exact McNemarp=0.266). This does not prove equivalence, but it meets a prespecified two-point retention criterion. The compact, inference-reachable checkpoint contains 1,472.6M unique parameters, 42.4% fewer than the original 2B policy, while all retained tensors are bitwise identical to the source checkpoint. Cross-family execution is additionally checked with a MiniCPM-V adapter smoke test; closed-loop cross-family transfer remains an open evaluation. AcrossWAM1.0 therefore contributes an auditable software and evaluation boundary for compact latent world-action policies, distinct from LaWAM's original latent-subgoal contribution.

---


### 222. [On the Recoverability of Private Information Unlearning in Large Language Models](https://arxiv.org/abs/2608.29943)

**<font color=#1a73e8>作者：</font>** Shicheng Hu, Runzhi Tian, Ziqiao Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can memorize sensitive information, raising serious privacy concerns. Machine unlearning offers a potential solution to remove such information, but it remains unclear whether existing methods truly erase it or merely hide it within the model. A key challenge is quantifying the persistence of sensitive data under a unified evaluation framework. To address this, we construct a synthetic dataset containing fake private information and propose a white-box auditing framework to systematically assess whether claimed-forgotten information is genuinely removed. Using this framework, we evaluate five existing unlearning methods and find that a simple "inverse greedy" decoding -- selecting the least likely token at each step -- can recover supposedly forgotten private information. Our results reveal that current unlearning approaches often fail to fully eliminate sensitive information, highlighting the need for more reliable methods to ensure privacy in deployed LLMs.

---


### 223. [XQDT: eXplainable and Quantitative Data-Text Alignment Metric with Feedback Signals](https://arxiv.org/abs/2608.29948)

**<font color=#1a73e8>作者：</font>** Kun Efimov-Zhang, Yifei Song, Claire Gardent  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating data-text alignment remains challenging: existing metrics often provide limited explanations for the scores, while prompt-based LLM-as-Judge methods can be expensive and unreliable. We present an end-to-end explainable evaluation metric that fine-tunes a language model to identify omitted, extra, incorrect, and correct data units in a data-text pair. These local judgements are aggregated into precision, recall, and F1 scores, providing both fine-grained diagnostic feedback and an interpretable measure of alignment quality. Across benchmarks, our fine-tuned models outperform LLM-as-Judge methods in error prediction and achieve competitive precision, recall, and F1 scores, while maintaining strong correlation with human judgements. Beyond evaluation, our verifier outputs also provide useful feedback signals for downstream correction and refinement, supporting alignment-oriented improvement of data-to-text and text-to-data. Code and resources are available at this https URL.

---


### 224. [SearchWiki: Learning to Build and Navigate Knowledge Wikis for Active Information Seeking](https://arxiv.org/abs/2608.29953)

**<font color=#1a73e8>作者：</font>** Guransh Singh, Vishwajeet Kumar, Arkadeep Acharya 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Flat retrieval-augmented generation treats a corpus as a bag of chunks, discarding document hierarchy and cross document structure. We introduce SearchWiki, a harness framework that synthesizes a corpus into a hierarchical, typed, navigable wiki and trains an agent, WikiResearcher-9B, to retrieve information through multi-turn tool use. The wiki organizes knowledge into three layers - document overviews, cross- document topic pages, and page-level source records; enabling progressive refinement of retrieval when initial lookup misses. We optimize the agent's navigation policy with on-policy reinforcement learning with a multi-component reward function balancing answer correctness, retrieval quality and trajectory efficiency. Evaluation on ViDoRe-V3 (8 domains), FinanceBench, and memory benchmarks (LoCoMo, LongMemEval, PersonaMem-v2) shows that WikiResearcher- 9B which is our RL-tuned Qwen 9B model, significantly outperforms same-size untrained baselines and exceeds or matches larger external models. SearchWiki paired with WikiResearcher-9B demonstrates that learned navigation over structured corpora is a superior alternative to flat retrieval.

---


### 225. [Detecting Hidden Chain-of-Thought in Large Language Models with Linguistic, Behavioral, and Mechanistic Indicators](https://arxiv.org/abs/2608.29956)

**<font color=#1a73e8>作者：</font>** Armaan Singh, Ryan Trinh Le, Jasmine Kaur 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models often answer complex reasoning questions without revealing intermediate steps, raising whether they reason latently or complete patterns. We propose the Hidden CoT Detection Score (HCDS), a comparative behavioral and mechanistic signal measuring whether neutral-prompt behavior aligns more closely with explicit CoT or explicit no- CoT. Here, hidden CoT operationally denotes this neutral-prompt CoT-like alignment; HCDS does not directly observe or prove an unexposed reasoning trace. On GSM8K, HCDS is significantly positive for both Qwen3-4B variants (Thinking $+1.87$, $p = 1.2 \times 10^{-7}$; Instruct $+1.41$, $p = 1.9 \times 10^{-4}$), replicates across a different inference stack and quantization within $0.08$ ($+1.80$ and $+1.45$), and is not significantly positive in seven of eight length-adjusted calibration-control cells. The unadjusted score produces large positive scores on single-step arithmetic and numeric factual lookup. The variants also respond differently to no-CoT instructions: Instruct complies from the prompt alone, whereas Thinking continues reasoning and requires intervention. These findings show stronger, less prompt-conditional CoT-like behavior in the reasoning-tuned model, consistent with but not proof of latent reasoning. HCDS thus investigates latent reasoning without relying on models' self-reported traces.

---


### 226. [RIDGE: Region-Informed Derivative-Guided Evidence Selection for Long Video Understanding](https://arxiv.org/abs/2608.29958)

**<font color=#1a73e8>作者：</font>** Shanqing Xu, Meng Luo, Mengchen Qian 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Long videos contain far more visual content than Large Vision-Language Models (LVLMs) can process under a fixed visual-token budget, making frame selection essential. Existing query-aware selectors usually estimate frame-query relevance and build a compact subset from high-scoring frames. Although their mechanisms differ, the similarity sequence is still often treated primarily as values to rank or sample from, rather than as an ordered signal whose shape reflects how query-relevant evidence emerges, peaks, and fades over time. This can obscure frames that explain, contextualize, or follow an event, because such evidence may lie on the rising or falling sides of a nearby relevance peak and receive lower absolute scores. We propose RIDGE, a frame selection framework that reads the frame-query similarity curve as a temporal signal. By using local changes and curvature, RIDGE partitions the timeline into structural regions and applies region-specific selection to preserve event cores, transitions, buildup, aftermath, and contextual frames under a fixed budget. It is a lightweight post-processing step on precomputed frame-query scores and requires neither training nor iterative LVLM calls. Across four long-video benchmarks and three backbones, RIDGE achieves the best performance in most settings and remains competitive in the others.

---


### 227. [Generative vs. Encoder Models for Multilingual NER: A Comprehensive Empirical Study on Naamapadam](https://arxiv.org/abs/2608.29959)

**<font color=#1a73e8>作者：</font>** Jakkala Mahesh, Jatavath Shravan Kumar, Komalla Shivani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language is humanity's most consequential technology, yet for over a billion speakers across India's twenty-two constitutionally recognised languages, its digital layer remains structurally incomplete. Named Entity Recognition (NER), the foundational step in transforming raw text into machine-interpretable knowledge, has been studied exhaustively for English but remains largely unsolved across most Indic languages. This paper presents a rigorous comparative study of generative and encoder-based neural architectures for NER on all eleven languages of the Naamapadam benchmark. We evaluate five classic model families spanning sequence-to-sequence transformers and multilingual encoders; four decoder-only large language models (LLMs) fine-tuned with LoRA and 4-bit NF4 quantisation; and nine generative models in zero-to-5-shot inference. Under strict CoNLL span-level evaluation, encoder-based models (mBERT and XLM-R, both F1=0.675 on Hindi) substantially outperform every generative architecture in ten of eleven languages, with gaps of 7.5-40 percentage points against the strongest competitor (Gemma-2-2B: avg F1=0.427). The best few-shot result reaches only 28% of the encoder baseline. We identify three language clusters--encoder-dominant, partial-coverage, and failure-zone; and provide actionable deployment guidelines grounded in transfer learning and low-resource NLP principles.

---


### 228. [Review Before Trust: Source-Grounded Integrity Gates for AI-Assisted Personal Health Records](https://arxiv.org/abs/2608.29965)

**<font color=#1a73e8>作者：</font>** Nora Girda, Adrian Groza  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can convert medical documents into structured data, but plausible output may still be unsupported by the source. Persisting such output in a longitudinal health record, a record that accumulates patient information over time, therefore creates an integrity risk: unverified data may influence later summaries, trends, or preventive-care computations. We introduce an evidence-gated trust-promotion model that keeps generated data provisional until a deterministic monitor verifies it against the source document. The monitor admits a candidate for a specified downstream use only when the source contains a unique supporting quotation, the relevant fields occur within the same laboratory row, and the required provenance is preserved. The generator cannot approve its own output, missing or ambiguous evidence causes refusal, and refused candidates remain available for human review rather than being silently discarded. We implement the model in Medical DataCloud, a personal health-record application, and evaluate it through automated tests and a replay of saved extraction outputs. All 22 conformance and mutation tests pass. The replay covers nine historical laboratory PDF reports containing 102 manually labelled rows. The reports produce 97 numeric candidates: schema validation accepts all 97, an earlier packet-level evidence check accepts 94, and the hardened quotation- and row-level policy admits 72 while retaining 25 for review. The study evaluates system integrity rather than clinical correctness or clinical safety. The results demonstrate the technical feasibility of an enforceable boundary that prevents generated claims from authorizing their own reuse in a longitudinal health record.

---


### 229. [DataFoundry: Evolving Data Preparators via Recursive Self-Improvement](https://arxiv.org/abs/2608.29966)

**<font color=#1a73e8>作者：</font>** Cehao Yang, Xiaojun Wu, Xueyuan Lin 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Domain adaptation of large language models increasingly depends on constructing high-quality training data, yet existing data-preparation pipelines typically address quality only after generation through post-hoc filtering. This creates a fundamental mismatch: data-quality issues often originate from the construction process itself, while quality control is applied only to its outputs. We introduce \textsc{DataFoundry}, a framework for \textbf{evolving data preparators through recursive self-improvement} before large-scale data production. \textsc{DataFoundry} represents a data preparator as an evolvable runtime specification and instantiates its evolution with a \textsc{Skills-as-Modules} architecture, in which a central \textsc{Controller} orchestrates modular skills to compile executable runtimes, diagnose deficiencies on small pilot sets using domain-appropriate criteria, and translate diagnostic feedback into adapters that revise individual preparation components while preserving stable interfaces. We evaluate \textsc{DataFoundry} on DataPrep-Bench across mathematics, finance, law, and medicine, and find that recursively evolved preparators produce training data with higher downstream utility than baselines. Experiments across different backbones further demonstrate that these improvements are not tied to a particular model, while analyses and case studies further reveal the framework's optimization dynamics and illustrate how its evolution unfolds in practice.

---


### 230. [An Open-Source, Event-Driven Pipeline for Cryptocurrency Market Data: Ingestion, Forecasting, and On-Chain Fraud Detection](https://arxiv.org/abs/2608.29973)

**<font color=#1a73e8>作者：</font>** Basil Sajid Shaikh, Melrick Mascarenhas, Nuzhat Faiz Shaikh  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Cryptocurrency markets generate high-frequency, multi-source data that is expensive to work with unless a team already has commercial-grade streaming and warehousing infrastructure in place. This paper describes a fully open-source pipeline that reproduces the behavior of a cloud-native, event-driven system -- file arrival triggering a message, a message triggering compute -- entirely on commodity hardware, using Apache Kafka and a filesystem-watching poller in place of managed cloud triggers. The pipeline partitions historical Gemini exchange data into hourly and minutely files, ingests them asynchronously through two independently grouped Kafka consumers (one for audit logging, one for Spark-triggered ETL), and lands cleaned output in a PostgreSQL warehouse with historical and aggregated schemas plus asset-specific data marts. We use the resulting Bitcoin data mart to compare a seasonal ARIMA model against a single-layer LSTM network for price forecasting, and separately apply Random Forest and Gradient Boosting classifiers, with additional engineered features, to the public Ethereum fraud detection benchmark introduced by Farrugia et al. We report the architecture, the modeling methodology, and the resulting metrics, and we are explicit about the limitations of comparing forecasts issued at different horizons and of evaluating fraud detection on a static, already-labeled dataset.

---


### 231. [SpanCalib-VLM: Calibrated Hallucination Span Detection in Vision-Language Models](https://arxiv.org/abs/2608.29974)

**<font color=#1a73e8>作者：</font>** Amanuel Gizachew Abebe, Yasmin Moslem  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Detecting hallucinations in Large Vision-Language Models (LVLMs) requires both accurate span localization and well-calibrated confidence scores. Fine-tuned generative VLMs excel at identifying hallucinated text spans but suffer from overconfidence and high inference latency. Discriminative sequence taggers offer deterministic speed and superior calibration but exhibit conservative span recall. We present SpanCalib-VLM, a hybrid dual-system for the SHROOM-Visions Shared Task that combines a multimodal sequence tagger, consisting of XLM-RoBERTa-Large fused with a SigLIP vision encoder via cross-attention, with our fine-tuned generative VLM (Qwen3.5-4B-SHROOM-SFT). Through a Union-Calibrated Fusion strategy, candidate spans from the generative model are re-scored with calibrated probabilities from the sequence tagger. On the SHROOM-Visions English evaluation split, our ensemble achieves a Pearson calibration correlation of 0.41 and an overall IoU of 0.39, with a clean-response IoU of 0.91} and overall detection accuracy of 70.7%. We make our model weights and code publicly available.

---


### 232. [Evolutionary Soups: Evolving Mixture-of-Experts for Multi-Objective LLM Alignment](https://arxiv.org/abs/2608.29978)

**<font color=#1a73e8>作者：</font>** Lingxiao Kong, Steffen Staab, Cong Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly required to generate responses that satisfy multiple competing objectives. Since optimal trade-offs depend on both user preferences and input prompts, controllable multi-objective generation must dynamically adapt models at inference time without retraining. To address this, we propose Evolutionary Soups, a mixture-of-experts framework for fine-grained generation control, with gating networks trained via an evolutionary algorithm. The per-layer gating networks dynamically produce expert-merging coefficients from hidden-state representations, while the evolutionary algorithm incorporates greedy hypervolume contribution for effective evolution of these gating networks, achieving consistent improvements on large and noisy training datasets and broader coverage of the non-convex Pareto front. Experiments across three tasks demonstrate the effectiveness of Evolutionary Soups over baselines: it achieves the best hypervolume, linear utility, and Tchebyshev utility (~20% improvement) among controllable methods on all tasks.

---


### 233. [AutoCRAT: Within-trajectory Joint Control of Stochasticity and Compute for LLM Reasoning](https://arxiv.org/abs/2608.29988)

**<font color=#1a73e8>作者：</font>** Hanjun Luo, Qiushi Liu, Jingya Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) achieve strong reasoning performance, which depends critically on inference-time decisions. Yet these decisions are commonly handled by static, one-size-fits-all policies, limiting adaptation to diverse tasks and reasoning stages. Recent adaptive methods partially address this limitation, but they primarily adapt either decoding stochasticity (how the model explores) or reasoning compute (how long the model reasons) in isolation, leaving their interaction within a single reasoning trajectory unmodeled. To address this challenge, we shift toward a within-trajectory joint control view, and instantiate it in AutoCRAT, a decoder-side controller for frozen backbones. Using only signals available during decoding, AutoCRAT jointly adjusts sampling stochasticity and reasoning budget during generation. AutoCRAT operates over a discrete action space and updates control decisions only at semantic boundaries, improving stability while remaining responsive to the evolving reasoning process. Comprehensive evaluation across 6 benchmarks demonstrates that AutoCRAT (I) uses 13.8-52.7% fewer inference tokens on average than recommended static configurations, (II) surpasses recommended static and adaptive baselines by 1.5-4.5% in relative accuracy, and (III) enjoys strong cross-backbone transferability.

---


### 234. [Beyond Fluency: A Rubric-Based Benchmark for Evaluating Saudi Dialect and Cultural Competence in Large Language Models](https://arxiv.org/abs/2608.29990)

**<font color=#1a73e8>作者：</font>** Ghassan Al-Sumaidaee, Sajjad Abdoli, Ahmed Rashad 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly deployed in Arabic-speaking markets, yet standard benchmarks overwhelmingly reward Modern Standard Arabic (MSA) fluency while leaving dialectal and culturally grounded competence unmeasured. This gap is consequential: everyday Arabic is largely dialectal, and dialect encodes social meaning that MSA-centric evaluation cannot capture. We present a rubric-based benchmark for the Saudi dialect, comprising 31 expert-authored prompts spanning idiomatic, pragmatic, lexical, and culturally-embedded phenomena, each paired with an expert-established ground truth. Our methodology separates evaluation into a model-agnostic phase, in which atomic, MECE positive criteria are derived solely from the ground truth, and a model-specific phase, in which four state-of-the-art systems -- Claude Opus 5, Gemini 3.7, GPT-5.6, and Kimi K3 -- are scored against those criteria and penalised for errors they actively introduce. Across 124 model-prompt evaluations we catalogue 466 error instances under a nine-category taxonomy. The four systems cluster within a narrow macro-average band (42.7%-53.1%), with no model exceeding 55% and every model recording at least one negative-scoring prompt, confirming that Saudi dialectal competence remains broadly unsolved. Notably, Ambiguous Framing is the dominant failure mode (37.3% of errors) while outright Hallucination accounts for only 11.2%, indicating that models fail less by stating falsehoods than by distorting register and flattening pragmatic nuance. We further observe a consistency-versus-ceiling trade-off and model-distinctive error signatures. We release the full prompt set, ground truths, and scored rubrics to support reproducible dialectal evaluation.

---


### 235. [Generating Clinical Vignettes that Preserve Cognitive Formulations](https://arxiv.org/abs/2608.29995)

**<font color=#1a73e8>作者：</font>** Amit Oren, Nimrod Hertz-Palmor, Dean Ariel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models can generate fluent clinical case vignettes, but fluency alone does not ensure fidelity to a specifiable clinical structure. We introduce FORMA, a theory-grounded framework that compiles a cognitive model of a disorder into a directed weighted graph, samples a person-specific configuration of that graph, and validates whether the generated vignette preserves the specified components and causal links. We instantiate FORMA on Posttraumatic Stress Disorder using the Ehlers and Clark cognitive model, generating 16,500 vignettes across 500 personas, 11 generation models, and three ablation conditions. Evaluation combines an external edge-recovery probe, two clinical experts, a scaled LLM judge, and a clinician user study with 100 licensed practitioners. The cognitive graph is recoverable from full-condition vignettes (MCC = +0.41, AUC = 0.70) but not from zero-shot generation (MCC = +0.01, AUC = 0.50). Experts rate full vignettes substantially higher than zero-shot alternatives, and clinicians perceive them to be human-written 85% of the time, compared with 22% for zero-shot. FORMA also reduces demographic disparity in perceived quality by 1.5-7x. These results show that cognitive formulation can serve as an auditable specification for scalable synthetic clinical text generation. A repository with the data and code is available online: this https URL.

---


### 236. [Partition-Aware Unlearning for Removing Spurious Correlations in Large Vision-Language Models](https://arxiv.org/abs/2608.29996)

**<font color=#1a73e8>作者：</font>** Aditi Sarker, Nazreen Shah, Rafi Ibn Sultan 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) achieve strong performance across many multimodal tasks; however, they often exploit spurious object-background correlations, resulting in predictions driven by contextual shortcuts rather than object-relevant visual evidence. Despite growing interest in hallucination and robustness evaluation, existing benchmarks provide limited control over whether model predictions are grounded in the target object or induced by correlated background cues. In this work, we introduce PURGE (\underline{P}artition-aware \underline{U}nlearning for \underline{R}emoving spurious-correlation \underline{G}enerated \underline{E}rrors), a framework for constructing, benchmarking, and mitigating spurious-correlation-induced failures in LVLMs. The framework consists of: -- (1) Structured dataset construction wherein we develop three complementary structured data construction strategies that partition examples by object-relevant evidence and spurious background cues, enabling controlled diagnosis of shortcut reliance; and -- (2) Partition-aware unlearning, which uses these partitions to selectively remove spurious object-background associations while preserving object-based reasoning. We evaluate the \algo~framework across multiple LVLMs, including LLaVA-1.6-7B, Qwen3-VL-8B-Instruct, and Qwen3.5-9B, together with CLIP as a vision-language encoder, on a diverse suite of benchmarks, including CHAIR, POPE, Causal-HalBench, MM-SpuBench, AMBER, MMHal, and Waterbirds. Our results show that PURGE consistently reduces hallucinations and spurious-correlation-driven errors while maintaining or improving overall performance in most evaluated settings, providing both a reusable evaluation protocol and an effective mitigation framework for more reliable LVLMs.

---


### 237. [Small Language Models as Judges for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2608.30005)

**<font color=#1a73e8>作者：</font>** Fengyu Xie, Yilun Zhao, Bingsen Chen 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Rubric-based reinforcement learning extends RL beyond tasks with exact answers or rule-based verifiers by scoring responses against instance-specific criteria. However, this makes reward computation expensive: training requires repeated rubric judging, often with proprietary APIs or local generative LLM judges with 7B parameters or more. We study whether smaller language models can serve as efficient and reliable rubric-based judges. To make this question measurable, we construct PointRubric and RaR-Science-Static, two pointwise rubric-based evaluation datasets with instance-specific criteria and itemwise satisfaction labels. We compare three ways of extracting criterion-level judgments from small models: Generative verdicts, Yes/No Logprob margins, and Probe judges. Across both datasets, the Qwen3-1.7B Probe judge achieves the strongest criterion-level agreement among these methods, outperforming Generative and Logprob judges. Used as a GRPO reward model, it trains a policy from 0.232 to 0.643 on RaR-Science rubric score, compared with 0.594 for an 8B Generative judge baseline, while the baseline requires 10.7$\times$ more reward-judge time. Task and domain transfer experiments further suggest that Probe judges preserve criterion-level reward structure across settings.

---


### 238. [Error Detection for PET/CT Radiology Reports: Domain-Specific vs Large Language Models](https://arxiv.org/abs/2608.30021)

**<font color=#1a73e8>作者：</font>** Hermione Warr, Harry Anthony, Lilli J Freischem 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Errors in radiology reports can adversely affect patient treatment, yet automated report quality assurance remains challenging because errors are often subtle and require domain expertise to detect. Although large language models (LLMs) have recently been proposed for radiology report verification, their ability to detect clinically meaningful errors beyond chest X-ray datasets remains under-explored. To this end, we present the first systematic evaluation of language models for PET/CT report error detection, comparing compact domain-specific models with SOTA open-weight LLMs. We collected 30,633 oncology FDG PET/CT reports from 23 radiologists over 10 years. We trained domain-specific BERT models to detect clinically motivated synthetic reporting errors and evaluated alongside zero-/few-shot Qwen3-32B, Gemma-3-27B and Llama-3.3-70B on a held-out benchmark of 11,500 reports. A 15M-parameter model achieved 94.4% balanced accuracy with a 5.8% false-positive rate, compared with 84.0% for the strongest prompted LLM. Task-specific adaptation of Llama-3.3-70B closed this performance gap (94.4%) but retained substantially greater computational requirements. Our results suggest that domain-specific training matters more than model scale for PET/CT report error detection, supporting compact models as an accurate and computationally efficient approach to automated radiology report quality assurance.

---


### 239. [Automatic Conversion of NICE Guidelines to an Executable Computational Model Using Large Language Models](https://arxiv.org/abs/2608.30022)

**<font color=#1a73e8>作者：</font>** Ashvin Gupta, Denys Prociuk, Alessandra Russo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Introduction: NICE guidelines provide evidence-based recommendations for clinical care but remain largely in unstructured natural language. Existing approaches to converting them into computable representations often focus on individual diseases, require substantial manual encoding, and do not scale. Large language models (LLMs) may enable much of this translation to be automated. Methods: We present an end-to-end approach that converts textual clinical guidelines into executable models capable of generating explainable, patient-specific recommendations. A stepwise LLM-based transformation with in-context examples produces human-inspectable intermediate artifacts. We apply the approach to NICE pancreatic and lung cancer guidelines, use expert review to assess rule alignment, and evaluate the executable pancreatic cancer model on 20 patient vignettes. Results: Expert review showed strong alignment between the source guidelines and generated executable models. Most discrepancies were partial omissions rather than incorrect logic, while hallucinated or fundamentally incorrect rules were rare. On the patient vignettes, the executable model achieved an F1 score of 82.5%. Conclusion: LLMs can transform natural-language NICE guidelines into interpretable, executable models that preserve guideline structure, support transparent inspection and modification, and generate patient-specific recommendations. These findings demonstrate the feasibility of scalable automated generation of computable clinical guidelines.

---


### 240. [Interpreting and Steering for Safe and Correct Code Generation](https://arxiv.org/abs/2608.30025)

**<font color=#1a73e8>作者：</font>** Hao Yan, Ziyu Yao  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) frequently generate source code containing vulnerabilities, yet little work studies the internal mechanisms that distinguish safe from vulnerable generation in them. In this work, we systematically perform a mechanistic interpretation of LLMs, aiming at both understanding how code safety-vs-vulnerability is represented or driven by components in an LM and turning the insights into actionable steering strategies to encourage safer code generation. To this end, we introduce CodeSec-Pairs, a dataset of 9,342 Python safe-and-vulnerable contrastive code pairs, sampled from Llama-3.1-8B-Instruct. Utilizing the dataset, we explore approaches to localize layers and attention heads that relate to code safety, and further experiment with different steering strategies for inference-time vulnerability reduction. In particular, we propose DuoSteer, a double-steering approach that simultaneously applies safety and code-correctness steering to attention heads. In experiments over five vulnerability types, DuoSteer leads to an average of -26.9% vulnerability rate reduction and +7.5% functional correctness improvement, which outperforms not only other steering variants but also prompting and supervised fine-tuning baselines. The advantage also replicates on Qwen-2.5-Coder-7B-Instruct with another 2,500 contrastive pairs sampled from that model.

---


### 241. ["Act Like a 5th Grader" is Not Enough: Bounding Knowledge in LLM-Based User Simulators](https://arxiv.org/abs/2608.30033)

**<font color=#1a73e8>作者：</font>** Krisztian Balog, Arild Michel Bakken  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to simulate human behavior but frequently fail to exhibit realistic cognitive constraints, suffering from a "superhuman bias." Using a dataset of over 71,000 reading comprehension responses from 2,359 primary-school students (grades 4--6), we demonstrate that standard persona prompting yields near-perfect, deterministic performance, failing to capture the natural variance of developing readers. To address this, we introduce the Cognitively Bounded User Simulator (CBUS), an architectural framework that explicitly models the restricted working memory of young readers through an episodic bottleneck. Within this framework, we formalize two distinct test-taking strategies to emulate different reading behaviors. Our evaluation shows that explicitly modeling cognitive bounds significantly narrows the simulation gap across multiple LLM backbones, demonstrating that enforcing architectural constraints is more effective for high-fidelity simulation than simply scaling raw model capabilities.

---


### 242. [Beyond Uncertainty: Multi-Solver Disagreement Rewards for Self-Evolving Reasoning Curricula](https://arxiv.org/abs/2608.30035)

**<font color=#1a73e8>作者：</font>** Vinoth Selvendran, Zhanming Zhang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving reasoning frameworks train a Challenger to generate questions exposing a Solver's weaknesses, creating adaptive curricula without human data. However, existing approaches use a single solver's sampling uncertainty as the Challenger's reward. This creates a fundamental bottleneck: as the solver grows confident on the Challenger's question distribution, all sampled answers converge identically, collapsing the reward to zero and starving the Challenger of learning signal. Critically, this single-model reward cannot distinguish genuinely easy questions from those that merely align with one solver's learned biases. We propose a multi-solver disagreement reward using a heterogeneous ensemble varying in model capacity and sampling temperature. A normalized Shannon entropy over the ensemble's per-question plurality answers explicitly rewards questions where solvers produce conflicting solutions---capturing difficulty as inter-model divergence rather than intra-model sampling variance. This richer gradient enables the Challenger to discover questions targeting true capability boundaries, producing a curriculum that forces downstream Solvers to develop robust reasoning strategies generalizing across problem types. Our approach is a drop-in reward function replacement requiring no framework modifications or additional data. Experiments with Qwen3-4B show that Solvers trained on disagreement-Challenger questions achieve +1.34 points average improvement on competition-math benchmarks (MATH-500, AMC, Olympiad), suggesting that multi-solver disagreement provides a complementary and scalable signal for curriculum generation in self-play reasoning systems.

---


### 243. [Balance of Benchmarks: Semantic Density Reweighting for Benchmark Multiplicity and Task-Conditioned Evaluation](https://arxiv.org/abs/2608.30044)

**<font color=#1a73e8>作者：</font>** Jhen-Ke Lin  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Language models are commonly compared by averaging scores across a benchmark list with equal weight. Such lists grow through publication outside an explicit measurement design, so equal weighting turns the density of published benchmarks into an implicit capability weight: densely benchmarked regions count repeatedly. We introduce Balance of Benchmarks (BoB), which embeds benchmark descriptions and assigns each benchmark an inverse-density semantic weight. Nearby entries share aggregate influence at a disclosed density scale. After equating heterogeneous scores onto a common latent scale, a residual field uses the same geometry to condition model rankings on a task query. The two components serve distinct empirical roles. On a snapshot of 586 models and 14 benchmarks, BoB predicts which models are unusually strong on a held-out task beyond their general ability, reaching a profile correlation of 0.462 compared with 0.049 under equal weighting. It also limits the influence of densely repeated benchmarks on the aggregate. After adding four copies of each benchmark in turn, the resulting rankings retain a Kendall tau of 0.995, compared with 0.936 under equal weighting. The residual field therefore provides task-conditioned prediction, and inverse-density weighting provides robustness to benchmark multiplicity. Together, they turn benchmark-list composition from an incidental property of evaluation suites into an explicit, controllable part of measurement design, providing a principled foundation for task-aware and multiplicity-robust model evaluation.

---


### 244. [Can LLM Agents Discover? Evaluating Creativity on ML Engineering Tasks](https://arxiv.org/abs/2608.30047)

**<font color=#1a73e8>作者：</font>** Shitanshu Bhushan, Yunxiang Zhang, Lu Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent AI systems promise autonomous scientific discovery, claiming to discover algorithms and produce research papers, yet understanding whether they exhibit creativity, the capacity to produce solutions that are both novel and useful, remains an open question. We present a framework for evaluating multi-turn LLM research agents' creativity using ML engineering tasks as a testbed, through three dimensions: P-Creativity (psychological novelty: novel relative to the agent's own prior solutions within a run), H-Creativity (historical novelty: novel relative to the corpus of human solutions), and Usefulness (task performance). Evaluating two agent frameworks, AIDE and AIRA-Dojo, on 10 Kaggle-style machine learning tasks from MLE-Bench, we develop an LLM-as-a-Judge pipeline and verify its strong correlation with human creativity judgments, providing a reliable automated metric for P-Creativity evaluation at scale. Applying this pipeline to agent trajectories, we find: (1) all agents exhibit declining P-Creativity as they transition from exploration to exploitation; (2) LLMs exhibit greater H-Creativity than medal-winning humans, yet achieve lower performance. Our findings reveal that current agents can explore novel regions of the solution space but lack the capacity to convert this novelty into improved task performance.

---


### 245. [Spec2Twin-Chain: Orchestrating Bi-Level Optimization with LLMs for Blockchain Digital Twin Construction](https://arxiv.org/abs/2608.30050)

**<font color=#1a73e8>作者：</font>** Haoting Zhang, Haoxian Chen, Jiayuan Sheng 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building a blockchain digital twin largely requires translating domain knowledge and specific system descriptions into a simulator architecture, calibrating its parameters against behavioral evidence, and validating the constructed twin. These steps are commonly performed through application-specific modeling efforts that can be difficult to reuse across systems and downstream decision problems. We consider automating this process through Spec2Twin-Chain, a framework that formulates blockchain digital-twin construction as a bi-level optimization problem. At the upper level, a large language model proposes and revises structurally admissible architectures using system specifications, behavioral evidence, and feedback from evaluated designs. At the lower level, a simulation-based optimizer calibrates the architecture-conditioned parameters under explicit objectives and guardrail constraints. The two levels iterate. The evaluated candidates at lower levels are retained in a global archive and used to guide subsequent proposals at upper levels. We conduct controlled experiments involving twin calibration, feedback-driven recovery, stress analysis, downstream policy optimization, and policy updating. The results demonstrate that the framework can construct behaviorally accurate twins, improve initial designs through iterative feedback, and reuse calibrated twins to support downstream decisions.

---


### 246. [Pak3H: Evaluating the Cost of Cultural Mismatch in LLM Alignment with a Human-Contextualized Urdu Benchmark](https://arxiv.org/abs/2608.30065)

**<font color=#1a73e8>作者：</font>** Abdullah Hashmat, Usman Naseem, Agha Ali Raza  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) demonstrate strong Helpfulness, Harmlessness, and Honesty (3H) alignment in English-centric settings, but these gains transfer poorly to low-resource languages due to cultural mismatches. Existing multilingual 3H benchmarks rely predominantly on automated translation or LLM based synthesis, propagating source-language biases while sacrificing local relevance. To address this gap, we introduce Pak3H1, the first human-validated, culturally contextualized Urdu benchmark suite for 3H alignment, comprising PakAlpaca (helpfulness), PakBeaverTails (harmlessness), and PakTruthfulQA (honesty). Our multi-stage pipeline integrates manual cultural adaptation and dictionary-guided post editing to prioritize native speaker judgment, ensuring both semantic fidelity and contextual authenticity. Zero-shot evaluations across multiple open and proprietary LLM architectures reveal systematic cross-lingual alignment gaps: helpfulness win rates decline under localized contexts, harmlessness guardrails break down against regional safety risks, and composite honesty metrics degrade substantially due to localized factual constraints. These findings expose structural limitations in current alignment approaches, underscoring the necessity of human-guided localization for equitable multilingual evaluation.

---


### 247. [How do World Models and Policies Compose in LLM Agents? A Joint Spectral and Behavioral Account](https://arxiv.org/abs/2608.30067)

**<font color=#1a73e8>作者：</font>** Ruize Xu, Xiao Yu, Yujin Tang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> How do LLM agents come to both understand environments they act in and master tasks set within them? Through controlled experiments combining world-model training (next-state prediction) and policy training (reward maximization), we investigate this question. We dissect the resulting models through their additive parameter updates. Geometrically, we find effective world-model updates are low-rank and share an input-feature subspace with policy updates while writing to nearly orthogonal output directions, whether trained separately or sequentially. However, we find that, in projection interventions, the sequential update induces more robustness than separate policy RL when removing the world model's leading input directions, suggesting that it has learned alternative input pathways. Behaviorally, we find the sequentially trained agent explores a wider range of states and actions. Based on this, we ask: does policy training preserve world knowledge as well as it could? We probe this with training-free merging built on the geometrically motivated input basis plus an online world-model loss during policy RL, and show both improve over the untreated baseline. Our findings suggest world knowledge and task-directed ability can be learned in geometrically complementary forms, and that future post-training pipelines should consider how best to engineer the interface between them.

---


### 248. [TAKE 85: Testing Audiovisual filmmaKer's intEnt across 85 Hours of Film](https://arxiv.org/abs/2608.30068)

**<font color=#1a73e8>作者：</font>** Kaishuu Shinozaki-Conefrey, Olivier Pascaud, Robin Courant 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Films communicate through deliberate creative choices, including lighting, color, composition, editing, dialogue, music, and sound. Humans naturally interpret these signals as directorial intent, yet current multimodal large language models (MLLMs) are evaluated almost exclusively on understanding what happens rather than why it is presented that way. We introduce TAKE 85, the first benchmark for directorial-intent understanding, comprising 398 short films (85 hours) with expert-verified question-answer pairs spanning global and fine-grained visual and audio intent. Through controlled modality ablations, TAKE 85 enables systematic evaluation of multimodal reasoning. Experiments on state-of-the-art MLLMs reveal a substantial gap between perceptual recognition and intentional understanding: while models accurately describe events and narratives, they consistently fail to infer the communicative role of filmmaking decisions. Our results establish directorial intent as a previously overlooked dimension of multimodal understanding: even the strongest model reaches only 58 out of 100, and our ablations show that no input modality is sufficient on its own. All code, Q&As, and models are publicly available from this https URL

---


### 249. [Budget-Aware Compression Pipeline for Single-GPU LLM Inference: Methods, Trade-offs, and Coupling Effects](https://arxiv.org/abs/2608.30076)

**<font color=#1a73e8>作者：</font>** Hongyu Yu, Yifei Shen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Single-GPU deployment of 70B-parameter language models on an NVIDIA GPU is constrained by device memory, long-context throughput, and engineering integration cost. We cast single-GPU inference as a budget-aware design problem over these three axes and study how pruning, quantization, and KV-cache compression interact under realistic execution. Controlled ablations show that layer-wise pruning makes weight quantization more robust. KV-cache sparsification complements INT8 KV quantization by reducing memory without hurting decoding speed, while static vector quantizers often conflict with dynamic caching. Guided by these coupling results and explicit budget tracking, we assembled a practical pipeline and compressed a 70B model to about 33 GB, sustained about 57 tokens/s on 10k token prompts on a single A40, and kept absolute accuracy within 5% on common and reasoning benchmarks. We contribute design rules and a reproducible evaluation protocol that jointly report quality, memory, and end-to-end speed, and we provide a foundation for automated pipeline search under realistic single-GPU constraints.

---


### 250. [When Does a Classifier Help an LLM? Classifier-Guided Prompting and Hybrid Classifier-LLM Models for Credit-Default Prediction](https://arxiv.org/abs/2608.30086)

**<font color=#1a73e8>作者：</font>** Rishi Datta, Lavanya Prahallad  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Credit-default prediction is an important task in financial decision making. Traditional methods use fitted classifiers such as logistic regression and random forests on tabular features. Large language models (LLMs) have recently been applied to this task through prompting. In this work we study how a fitted classifier and an LLM can be combined for credit-default prediction. We distinguish telling the LLM to imitate a classifier from using the classifier to build the prompt. We hypothesize that a fitted classifier can supply the ranking ability that an LLM prompt lacks. We experiment on the Default of Credit Card Clients dataset, and report recall, F1, and the area under the ROC and precision-recall curves, with bootstrap confidence intervals. We observe that a few-shot LLM has the highest recall (0.47) and F1 (0.50) of any single model but ranks worse than a random forest (AUC-ROC 0.72 against 0.79). Instructing the LLM to imitate a classifier gives no significant change. Pruning the prompt to the classifier's eight most important features raises recall by 0.071 and F1 by 0.032. Adding the classifier's predicted probability to the prompt raises the LLM's AUC-ROC from 0.72 to 0.78, matching the random forest, while keeping 0.118 higher recall than it. The reverse composition, and the use of several classifiers, do not help. We thus recommend a simple classifier-guided prompt for LLM-based credit prediction.

---


> [!TIP]
> 当前位于：**201-250**（第 5/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-452](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
