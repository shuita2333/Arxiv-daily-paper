# 🧠 大模型相关研究 | 2026年09月22日

> 本类共 **148** 篇论文：已确认 **139** 篇，待复核 **9** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-148](./part-03.md)

---

### 1. [Do small language models know what they don't know?](https://arxiv.org/abs/2609.20824)

**<font color=#1a73e8>作者：</font>** Prashant Mudgal  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We explore whether entropy-based confidence signals can be leveraged to improve the accuracy of Small Language Models (SLMs) with fewer than 3 billion parameters, running entirely on consumer hardware. We evaluate seven distinct approaches, including token-level entropy early stopping, semantic entropy estimation, and uncertainty-aware routing to larger expert models, across 7 model pairs and 5 standard NLU benchmarks. Our key finding is that token-level entropy is effectively blind in SLMs: in 91% of dataset-model combinations, mean token entropy is near zero regardless of answer correctness, rendering token-based confidence signals unusable at this scale. We demonstrate that semantic entropy, computed by generating multiple samples, clustering answers by meaning, and measuring distributional uncertainty, recovers a viable confidence signal. Using semantic entropy to selectively route uncertain queries to a larger expert model yields accuracy improvements of up to +50 percentage points. Notably, cross-family routing (e.g., SmolLM 360M to Phi-3.5-mini) averages +22.0% improvement compared to +6.8% for same-family routing, revealing that expert model quality matters more than architectural compatibility. Our results suggest that the value proposition for entropy-based methods in SLMs is not computational savings but intelligent compute allocation: spending more tokens where they matter most.

---


### 2. [HERMES: Contrast-Aware Knowledge Graph Reasoning from Clinical Notes for Patient Outcome Prediction](https://arxiv.org/abs/2609.20825)

**<font color=#1a73e8>作者：</font>** Gia-Bach Nguyen, Hoang-Ha Nguyen, Tuan-Cuong Vuong 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical predictive models often rely on structured Electronic Health Record data, such as time-series and procedure codes. While recent approaches have begun leveraging unstructured clinical notes, they typically encode them as flat sequences, which may lose explicit relational and temporal structure present in clinical narratives. In response, we propose HERMES, a graph-based framework that operates exclusively on clinical text while preserving clinical relationships. This approach builds on two key ideas. First, personalized Knowledge Graphs (KGs) are constructed through Large-Language-Model-guided extraction from clinical notes with Contrastive Logic Modeling that explicitly captures temporal dynamics and treatment failures and changes in outcomes. Second, a Graph Attention Network synthesizes patient representations through graph-based learning over the KGs. Experiments on MIMIC-III and MIMIC-IV for in-hospital mortality and 30-day readmission prediction show that HERMES consistently outperforms strong text-only baselines. Our findings demonstrate that explicit relational modeling with Contrastive Logic Modeling significantly advances predictive performance.

---


### 3. [From Discharge Notes to Patient Understanding: Persona-Grounded, Open-Ended Simulation of LLMs as Discharge Educators](https://arxiv.org/abs/2609.20827)

**<font color=#1a73e8>作者：</font>** Won Seok Jang, Zonghai Yao, Hong Yu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Hospital discharge education is an interactive teaching task: a clinician adapts a discharge plan to a patient's literacy, recall, and personality. Existing LLM evaluations target static or artifact-generation tasks and do not measure patient understanding under open-ended dialogue. We introduce DischargeBench, a persona-grounded simulation in which a candidate LLM educator conducts a multi-turn session with a Virtual Patient, while an Education Monitor Agent regulates patient realism without modifying the educator, protecting the evaluation signal. We curate MIMIC-IV-Ext-DischargeBench, 477 cases over 24 ICD chapters with persona axes (personality, education level, health literacy, past-medical-history recall) for stratified analysis. Each simulation is scored on four axes -- Conversation Quality, Topic Checklist, Comprehension, and Factual Consistency -- by an LLM-as-a-Judge aligned against physician annotations. Across closed- and open-source LLMs, aggregate scores conceal clinically relevant variation across ICD chapters and patient personas; difficult personas expose coverage failures, comprehension gaps, and reduced source-answer agreement. LLM evaluation for discharge education should center patient understanding, not text quality or answer accuracy alone.

---


### 4. [Beyond WER: Entity and Disfluency Recall in Accented Conversational ASR](https://arxiv.org/abs/2609.20828)

**<font color=#1a73e8>作者：</font>** Fiza Husain, Ankit Pandey, Yash Singh  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> ASR systems optimised for Word Error Rate (WER) often miss named entities and filled pauses in accented conversational English, both critical for language-learning feedback. We present a three-stage pipeline for speakers from India, Indonesia, and Latin America: (1) heuristic SQL filters curating entity-rich training data at 2.8x the entity density of random sampling, (2) regional LoRA adapters fine-tuned on Qwen2.5-Omni-3B producing both verbatim and corrected transcripts in a single forward pass, and (3) a six-category error taxonomy validated by an LLM-based judge (83.8% agreement, 210 human-labelled samples). The pipeline achieves 80-85% entity recall (up from 53-55%), 76-86% filler recall (up from <5%), and 6-10% WER across 6k test utterances, outperforming Whisper and a commercial ASR on entity recall while matching a zero-shot 30B model with 10x fewer parameters. Paired bootstrap tests confirm that curation alone accounts for 2.8-4.2 pp of entity recall gain (p<0.0001).

---


### 5. [SAGE: Schema-Guided LLMs for Grant Review](https://arxiv.org/abs/2609.20829)

**<font color=#1a73e8>作者：</font>** Erik Varapaev, Andrei Chetvergov, Stepan Ukolov 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Grant reviewers must apply detailed criteria to application forms, budgets, and supporting documents while producing assessments that colleagues can inspect. We present SAGE, Schema-Guided Aspect-Based Grant Evaluation, a system that translates a grant rubric into structured checks and links its judgements to evidence from the application package. We evaluate SAGE in two stages on 35 nonprofit grant applications. A post-factum comparison with 105 reviews from the original competition shows fair ordinal agreement (kappa = 0.29). The foundation then conducted a criterion-level re-review after inspecting SAGE, producing 202 assessments. In this assisted round, SAGE reached kappa = 0.58 and outperformed a one-prompt-per-criterion baseline (kappa = 0.33 on the common subset), with higher rank correlation and lower error. A claim-level audit further identifies confirmed, disputed, and unaddressed parts of the structured draft. SAGE operationalizes the review methodology by producing a detailed, evidence-linked, and auditable draft for expert correction.

---


### 6. [Recursive Language Models Generalize Out of Domain](https://arxiv.org/abs/2609.20831)

**<font color=#1a73e8>作者：</font>** Chenxiao Yang, Zhiyuan Li, David McAllester 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study when limiting what a language model can see improves learning. We compare standard CoT, the more general learner that reads the full trace, with recursive language models, which restricts itself by solving each subtask in an isolated context. In-distribution, this generality comes for free: CoT can efficiently simulate the recursive rule, so the IID generalization guarantee changes only by a constant factor, and recursion does not offer much. But out of domain, CoT can fit training by relying on context outside the current subtask, i.e. a shortcut that breaks once those tokens change; recursive context isolation rules out this failure mode. Even though CoT's class still covers the recursive rule, simplicity bias picks the shortcut over the truth. Thus, to go beyond distributional accuracy and truly reason, covering the right rule is not enough; this contrasts with classical learning theory.

---


### 7. [TatBLiMP: A Benchmark of Linguistic Minimal Pairs for Tatar](https://arxiv.org/abs/2609.20832)

**<font color=#1a73e8>作者：</font>** Ilshat Saetov, Dmitry Gaynullin  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We introduce TatBLiMP, the first benchmark of linguistic minimal pairs for Tatar (tt, ISO 639-3 tat), a Qypchaq Turkic language written in Cyrillic. To our knowledge it is the first grammaticality evaluation for Tatar language models of any kind, since even the 101-language MultiBLiMP does not include Tatar. TatBLiMP covers 16 morphosyntactic phenomena in 1248 sentence pairs. Each pair differs by a single morpheme, one grammatical and one ungrammatical. A model passes a pair when it assigns higher probability to the grammatical member. Scoring compares probabilities the model already assigns, so the benchmark needs no text generation and no parser, and it runs on base models and on mid-training checkpoints. TatBLiMP adapts the phenomenon inventory and single-morpheme breaking operations of TurBLiMP to Tatar and adds one phenomenon specific to Tatar, bare-noun number after numerals and quantifiers. The grammatical member of every pair is an attested sentence from Tatar literary prose. The ungrammatical member is produced by a deterministic single-morpheme perturbation with the apertium-tat transducer. Every pair is ratified by a native speaker. A plausibility principle governs construction, so the ungrammatical member is a plausible real-world error rather than an arbitrary corruption. Across from-scratch Tatar models, cross-lingual adaptations, and frontier multilingual LLMs, the benchmark tracks focused Tatar training rather than parameter scale. A 478M from-scratch model and a 125M monolingual model lead near 0.97, a 7B adaptation trails, frontier LLMs of 30-120B parameters fall to 0.80-0.92, and a lightly tuned multilingual model is weakest. We close with the benchmark's main limitation. Its inherited taxonomy omits the morphophonology, vowel harmony and consonant assimilation, that is most salient to native speakers, and we sketch a native second layer that would add it.

---


### 8. [Transsion's Speaker-Attributed Multilingual ASR System for the MLC-SLM 2026 Challenge](https://arxiv.org/abs/2609.20833)

**<font color=#1a73e8>作者：</font>** Zhecheng Ren, Xuanji He, Xiaoxiao Li 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents the Transsion Speech Team submission to Task 1 of the MLC-SLM 2026 Challenge, which focuses on speaker-attributed transcription for multilingual conversational speech. We propose a cascaded framework consisting of three components: a speaker diarization module, a long-form multilingual ASR module, and a speaker-transcription fusion module. The diarization module is built upon DiariZen and produces speaker-homogeneous segments through local speaker activity estimation and global speaker clustering. The ASR module is based on Qwen3-Omni and generates multilingual transcriptions, while an external CTC-based alignment model provides precise word- and character-level timestamps. Finally, the fusion module combines diarization outputs with timestamped transcriptions to generate speaker-attributed STM outputs. Experimental results on the official evaluation set demonstrate the effectiveness of the proposed framework. The submitted system achieves a tcpMER of 15.41% and ranks second among all participating teams.

---


### 9. [Towards Secure Cloud-Native Computing: Unveiling Kubernetes Misconfigurations with Large Language Models](https://arxiv.org/abs/2609.20834)

**<font color=#1a73e8>作者：</font>** Mostafa Anouar Ghorab, Mohamed Aymen Saied  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In the rapidly evolving landscape of cloud-native computing, Organizations are increasingly adopting infrastructure models that emphasize scalability, flexibility, and efficiency. Kubernetes has become the de facto standard for orchestrating containerized applications in these environments. However, the inherent complexity of cloud-native ecosystems introduces significant challenges, particularly in the form of misconfigurations that can compromise both security and performance. This study explores the potential of Large Language Models (LLMs) in identifying Kubernetes misconfigurations. We introduce a comprehensive taxonomy of common misconfiguration types, offering a structured framework to better understand and categorize these issues. Additionally, we conduct an empirical evaluation of state-of-the-art detection tools to benchmark their effectiveness. Furthermore, we analyze the Kubernetes objects most prone to misconfiguration and evaluate the severity of the identified issues. By leveraging advanced machine learning techniques, including LLMs, we provide novel insights into enhancing misconfiguration detection methodologies.

---


### 10. [A Generative Grammar Underlying the Voynich Manuscript, the Pastiche Hypothesis: Evidence from Large Language Models](https://arxiv.org/abs/2609.20835)

**<font color=#1a73e8>作者：</font>** Nicolas Turenne  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Background: The Voynich Manuscript is a fifteenth-century codex written in an unknown script whose content remains undeciphered. Previous studies suggest that its statistical properties resemble those of natural languages, while its illustrations - primarily plants - recall medieval herbals.
Methods: We present a multidisciplinary analysis combining probabilistic modeling, phonetic decomposition, rare-event detection, and multimodal image analysis, based on a newly transliterated corpus. Word- and letter-level distributions are modeled using position-dependent probabilistic grammars, while phonetic patterns are compared across Indo-European, Semitic, and Asian languages. Image-text alignment methods based on large language models are applied to identify potential botanical correspondences.
Results: The results indicate that Voynich symbols behave as letters rather than syllabic units, while word-length distributions resemble syllabic structures. Phonetic analyses show closer alignment with consonant-heavy languages such as Hebrew or Arabic than with Indo-European languages. Probabilistic modeling reproduces Zipf-like distributions and reveals extremely low probabilities for repeated initial-letter sequences, indicating a structured imitation of natural language. Image analysis suggests strong correspondences between Voynich plant illustrations and those found in Pseudo-Apuleius herbals from the Mediterranean tradition, consistent with an imitation of medieval medicinal books.
Perspectives: These findings support the hypothesis that the Voynich Manuscript follows a structured generative system combining linguistic regularities and herbal knowledge, and demonstrate the value of integrating probabilistic and AI-assisted approaches in the analysis of historical manuscripts.

---


### 11. [PhysioBench: A Unified Benchmark for Physiological Signal Question Answering](https://arxiv.org/abs/2609.20836)

**<font color=#1a73e8>作者：</font>** Mengxuan Li, Junfa Chen, Jinze Xia 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Physiological signals support diverse clinical and monitoring tasks, yet existing physiological signal foundation models typically require task-specific adaptation for each task. Natural language provides a common interface for specifying different prediction objectives, but the ability of current models to follow such instructions across physiological signal modalities remains insufficiently evaluated. To address this gap, we introduce PhysioBench, a unified benchmark for physiological signal question answering. PhysioBench harmonizes annotations from 22 public datasets into 61.4 million questions across 30 tasks. Each question-answer pair is grounded in a signal segment and traceable to its source annotation. We evaluate 21 representative models, including large language models, vision-language models, time-series language models, and physiological signal foundation models under three complementary settings. The results show that none of the evaluated models achieves consistently strong performance across physiological signal modalities and tasks. The incorporation of natural language supports unified prediction across tasks, although performance remains sensitive to question formulation. Beyond these findings, PhysioBench offers an extensible platform for fine-grained analysis and future research on physiological signal understanding. Our codes are available at this https URL.

---


### 12. [From Generation to Detection: Exploration of Discourse Driven Scenario based LLM Generated Fake News](https://arxiv.org/abs/2609.20838)

**<font color=#1a73e8>作者：</font>** Zeynep Özdemir, Murat Osmanoğlu, Sevgi Yiğit-Sert 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In this study, we examine how modern LLMs generate and detect fake news under controlled settings across four manipulation scenarios. These are open-ended generation, rewriting, manipulation prompts and attribute based prompts grounded in the journalistic discourse framework. Firstly, using seven widely adapted models, we created a synthetic fake news corpus with 14000 generated articles across these four scenarios. Then we analyzed its linguistic properties to assess how closely model-generated news resembles real news structurally and semantically. Finally, to evaluate detection performance, we conducted experiments where each model judges generated fake news, starting with a basic detection prompt and improved prompts developed through an iterative refinement process that extracts misleading patterns from real-fake pairs. Our results revealed substantial variation across models in both generating and detecting misinformation, demonstrated that the generation strategy strongly influences detectability, and show that the refined prompt does not improve and often harms detection performance. Therefore, the study provides a systematic assessment of LLMs detection capability of LLMs generated fake news across typical generation scenarios.

---


### 13. [COAL-SQL: Coverage-Guided Augmentation and Failure-Driven Learning for Text-to-SQL Post-Training](https://arxiv.org/abs/2609.20842)

**<font color=#1a73e8>作者：</font>** Qifeng Cai, Xuanguang Pan, Hao Liang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-to-SQL translates natural-language questions into executable SQL queries, but open-source large language models still require task-specific post-training for complex, real-world SQL generation. Effective post-training requires both training data that cover the capabilities demanded by the target task and a learning strategy that enables the model to acquire them. Existing datasets provide valuable supervision but incompletely cover SQL structures, while augmentation methods typically expand data without identifying structural gaps. Moreover, supervised fine-tuning (SFT) or reinforcement learning (RL) alone cannot dynamically address weaknesses exposed during training. We propose COAL-SQL, a unified framework combining Coverage-Guided Augmentation (CGA) and Failure-Driven Learning (FDL). CGA uses greedy selection to identify SQL structures missing from the original dataset and constructs complementary examples, improving structural coverage. FDL retains GRPO as the main optimization objective while supplying targeted supervision for unsolved examples. At the step level, it applies SFT to verified reasoning traces generated by a strong LLM for accumulated failures. At the epoch level, it retrieves structurally related examples based on accumulated failures to create targeted practice, helping the model acquire the corresponding SQL capabilities. With only 12,600 distinct post-training examples, COAL-SQL achieves 64.9% execution accuracy on the BIRD development set and outperforms baselines trained at comparable scale. The code is available at this https URL.

---


### 14. [VISPATH: Visual-Intent-Guided Path Reasoning for Multimodal Knowledge Graph Question Answering](https://arxiv.org/abs/2609.20843)

**<font color=#1a73e8>作者：</font>** Jinke Wu, Zhengpin Li, Mengzhe Jia 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Knowledge graph question answering (KGQA) enables models to answer natural-language questions through structured graph reasoning and has achieved substantial progress across many benchmarks and applications. Recently, multimodal KGQA (MM-KGQA) has attracted increasing attention because many questions require jointly using multimodal inputs and KG evidence. However, existing MM-KGQA methods typically use multimodal information only for starting entity grounding or evidence retrieval, after which multi-hop reasoning degenerates into text-only graph search. As a result, they cannot exploit multimodal cues that become important at intermediate hops. To address this limitation, we propose VISPATH, a visual-intent-guided path reasoning framework for MM-KGQA. VISPATH first identifies a reliable starting entity by combining multimodal grounding with graph-structural cues. It then performs intent-guided path discovery by recomputing hop-specific multimodal intent from the input, question, and current partial paths, so that each expansion is guided by the current reasoning state. The discovered paths are further refined through reasoning-chain pruning, which evaluates candidate paths as complete evidence chains based on their consistency with the question, reasoning sketch, and hop-specific intent. Finally, VISPATH checks whether the selected evidence is sufficient for answer generation. We further construct VISPATH-Bench, a benchmark for evaluating multimodal multi-hop reasoning over KGs, covering questions that require two to four hops over KG paths. Extensive experiments on VISPATH-Bench and three additional multimodal QA benchmarks show that VISPATH consistently outperforms strong baselines. Notably, with GPT-4o as the backbone, VISPATH surpasses GPT-5.4 on VISPATH-Bench, achieving a 10.6% relative improvement in average accuracy and a 13.1% improvement at 2-hop reasoning.

---


### 15. [Boosting Deepresearch and LongContext Ability with Self-Generated Deepresearch Rollouts Traces](https://arxiv.org/abs/2609.20844)

**<font color=#1a73e8>作者：</font>** Zihan Wang, Hao Wang, Boyuan Jiang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deepresearch (DR) agents interact with real-world web environments through multi-turn search and visit, causing their contexts to grow rapidly over time. We observe that, even after DR Agentic Reinforcement Learning (DR-RL), 61.6% of the model's remaining prediction errors can still be attributed to insufficient long-context understanding, including longcontext hallucination and failures in cross-document evidence integration. It motivates us to further break the bottleneck of DR-RL by strengthening the model's long-context ability. However, effective LongContext training requires more than simply increasing context length. To bridge the data gap, we propose `DR Rollouts to LongContext-QA (DR-to-Long)'. The method repurposes DR-RL trajectories, which naturally contain search histories, visited webpages, evidence snippets, and final-answer supervision. It then replaces the compact snippets and webpage summaries in each trajectory with the full contents of their corresponding URLs, producing substantially longer multi-document contexts while preserving the original evidence relationships. Building on DR-to-Long, we introduce DLD (DR -> LongQA -> DR)-RL. DLD-RL first performs a short DR-RL stage to collect rollout trajectories, which are then converted into LongQA instances at zero annotation cost. The model is subsequently optimized with LongQA-RL to strengthen LongContext ability, followed by full DR-RL to continue improving its DR capability. Experiments show that DLD-RL outperforms standard DR-RL by 7.3% on three Deepresearch benchmarks and improves performance by 13.5% on three long-context benchmarks.

---


### 16. [Rewarding Efficient Reasoning Improves Abstention on Underspecified Tasks in Reasoning Models](https://arxiv.org/abs/2609.20846)

**<font color=#1a73e8>作者：</font>** Polina Tsvilodub, Max Höth, Michael Franke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While modern large reasoning models (LRMs) excel at providing correct answers in many tasks, we provide additional evidence for the observation that they often struggle with a critical capability: knowing when to abstain from answering. We analyze this gap by comparing LRM behavior to results from a human study, revealing that human reasoning effort on unanswerable tasks is upper-bounded by answerable tasks, whereas LRMs waste computational resources by generating longer Chains of Thought (CoTs) on unanswerable than on answerable prompts. To overcome this inefficiency, we take inspiration from a resource-rational perspective on human cognition and introduce a novel GRPO reward that encourages efficient reasoning about whether the task contains all the information needed to solve it. Fine-tuning several 4B LRMs with this reward leads to human-like abstention performance gains (+12.8% on average) while retaining answering capabilities and boosting the models' efficiency (44% shorter CoTs on average).

---


### 17. [Enhancing Audio Reasoning via Semantic Summary Prediction](https://arxiv.org/abs/2609.20849)

**<font color=#1a73e8>作者：</font>** Francesco Bonzi, Pooneh Mousavi, Cem Subakan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Audio Language Models (LALMs) perform well on complex question answering but often show a reasoning gap, where explicit Chain-of-Thought (CoT) reduces accuracy compared to direct answers. We hypothesize that long reasoning sequences shift attention away from the audio input. To address this, we propose SPARE (Semantic Prediction for Audio REasoning), which introduces a register token aligned with the final conclusion using a cosine similarity loss with a Sentence-BERT embedding. This conditions the model's latent space with the target semantic goal before reasoning begins. Experiments on MMAU and MMAR with SALMONN show improved zero-shot reasoning and stronger early attention to audio without additional inference cost.

---


### 18. [MME-Safety: A Fine-grained Benchmark for Safety Evaluation of MLLMs](https://arxiv.org/abs/2609.20850)

**<font color=#1a73e8>作者：</font>** Yueming Lyu, Yilian Shi, Haoxiang Tan 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) show remarkable advancements, their cross-modal capabilities introduce complex vulnerabilities that easily bypass unimodal filters. Existing benchmarks lack fine-grained intent-related annotations and rely on unidimensional metrics, hindering comprehensive robustness evaluation. To address this, we propose MME-Safety, a rigorously verified benchmark featuring a unique four-dimensional annotation schema that categorizes risk scenarios, harm severity, and modality-specific stealth levels. Furthermore, we introduce a hierarchical evaluation framework to assess fundamental response reliability, actual risk exposure, and the structural integrity of defensive behaviors. Extensive zero-shot evaluations across 17 state-of-the-art MLLMs provide a comprehensive safety profile of current multimodal systems. Our analysis systematically investigates cross-modal input configurations and uncovers safety implications associated with Chain-of-Thought (CoT) reasoning. These multifaceted findings underscore the urgent need for robust, reasoning-aware safety alignment in the multimodal landscape.

---


### 19. [Sparse Priors for Efficient Distribution Learning](https://arxiv.org/abs/2609.20883)

**<font color=#1a73e8>作者：</font>** Saumya Goyal, Barnabás Póczos  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Despite the widespread use and success of generative AI techniques today, theoretical guarantees on learning a distribution supported in $d$ dimensions from $n$ samples degrade as $O(n^{-1/\Theta(d)})$, though shown to be minimax optimal. We hypothesize that present bounds are too pessimistic because smoothness assumptions are not enough to capture the structure of distributions that often appear in real applications. Consequently, we introduce the class of sparse priors and define the "Sparse Dimension" as a measure of sparsity of a prior over the space of all distributions. We show that distribution learning under a $k$-sparse prior achieves a Bayesian risk lower bound of $\Omega(\sqrt{k/n})$ under common distance metrics, and show a matching (up to logarithmic terms asymptotically in $n,k$) upper bound for the TV distance under mild additional assumptions. We show the statistical equivalence of distribution learning and learning to sample in the Bayesian setting so that our results apply to learning to sample as well. While $k$ can still depend on the dimension $d$, or a notion of intrinsic dimension, our results show that learning under an appropriate prior overcomes the curse of dimensionality with respect to the dependence on $n$.

---


### 20. [BI-Agent and BI-Bench: Towards Automating End-to-End Business Intelligence](https://arxiv.org/abs/2609.20886)

**<font color=#1a73e8>作者：</font>** Chuxuan Hu, Yeye He, Penny Zhou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Business intelligence (BI) is a cornerstone of enterprise decision-making and is widely used by enterprise users in software such as Power BI and Tableau. In traditional BI workflows, users need to prepare data by (1) identifying relevant tables, (2) performing data transformations, and (3) building join relationships, before they can (4) answer their business questions. These steps can be complex and time-consuming, making BI challenging.
Given the strong capabilities of large language models (LLMs) in working with data, we study their ability to answer BI questions end-to-end, without requiring users to manually perform the tedious preparation steps. To do this, we harvest a large collection of real-world BI projects from public sources, and manually extract pairs of (questions, ground-truth answers) from real user dashboards. The resulting benchmark, BI-Bench, is the first benchmark to systematically study LLMs' ability on end-to-end BI.
We find that even frontier LLMs perform poorly on BI-Bench, with less than 50% accuracy. To address their limitations, we design a tool-augmented BI-Agent that decomposes BI workflows into subtasks on structured data, such as search, join, and transform, and orchestrates specialized data management methods across BI stages. Furthermore, we develop a post-training framework that synthesizes training trajectories from real BI projects, enabling BI-Agent to be further post-trained using both supervised fine-tuning (SFT) and reinforcement learning (RL). BI-Agent achieves substantial accuracy gains of up to 40 percentage points with vanilla LLMs, and post-trained BI-Agent yields gains of up to 30 points. Our results highlight the importance of combining tool-augmented reasoning with domain-specific post-training in complex BI workflows, and point to promising directions for future research.

---


### 21. [BirdsongChat: A Hybrid Multi-Agent Framework for Multimodal Embodied Behavior Simulation](https://arxiv.org/abs/2609.20887)

**<font color=#1a73e8>作者：</font>** Callie C. Liao, Duoduo Liao, Ellie L. Zhang  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Multimodal embodied systems require translating human intentions into interpretable and coordinated behaviors across heterogeneous modalities. However, existing multimodal agents often rely on implicit representations, limiting controllability and cross-modal consistency. We present a hybrid multi-agent framework for interactive multimodal behavior simulation that bridges semantic reasoning and physical execution through a Unified Parameter Representation (UPR). LLM-based reasoning agents transform multimodal inputs into UPR, which encodes behavioral states and interpretable control parameters for simulation agents generating synchronized 3D motion, spatialized soundscapes, and environmental behaviors. We develop BirdsongChat as a prototype implementation of the proposed framework, using interactive avian behavior simulation as a testbed that tightly couples motion, vocalization, and environmental context. BirdsongChat is evaluated on text- and image-guided scenarios involving species, behaviors, affective states, environments, and multi-bird interactions. The system achieves normalized scores of 94.4\% for cross-modal coherence, 100% for affective consistency, and 92.6% for generation consistency. These results demonstrate that an explicit intermediate representation effectively bridges semantic reasoning and physical execution, improving controllability and multimodal synchronization. The proposed framework thus offers a generalizable design principle for embodied AI systems requiring interpretable semantic-to-physical coordination across modalities, with potential applications in bio-inspired ecoacoustics, swarm robotics, virtual environments, and creative multimedia.

---


### 22. [Proxifield: Decentralized Multi-Agent Communication through Semantic Proximity](https://arxiv.org/abs/2609.20889)

**<font color=#1a73e8>作者：</font>** Pradyumna Tambwekar, Yenchia Feng, Deep Patel 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> As LLM capabilities have expanded, multi-agent communication has emerged as an increasingly active area of research. Prevailing protocols often adopt rigid structures that introduce coordination bottlenecks and can degrade as the number of agents increases. We introduce Proxifield, a round-adaptive multi-agent protocol with decentralized agent decision-making that constructs sparse communication graphs from the evolving semantic proximity of agents. Without model training or a centralized planner, Proxifield connects agents using four routing signals derived at inference time: direct address, information needs, plan alignment, and information complementarity. We compare Proxifield with two representative coordination baselines, a centralized Star protocol and a decentralized Shared Context protocol, across two domains: Drone Search and Rescue and the collective-reasoning benchmark HiddenBench. We first ablate base-model capability and find that, in both domains, the performance of Proxifield improves with model size (35B -> 397B parameter model) and Proxifield outperforms all baselines at the largest scale. As team size increases, Proxifield's task-reward advantage over Star widens from 5.4% at (N=5) to 53.0% at (N=25) and 59.5% at (N=50), while Shared Context consistently underperforms both protocols. Proxifield is also substantially more robust to permanent agent failure, retaining 73.6% of its no-failure task reward under the most severe condition, compared with 58.3% for Shared Context and 38.8% for Star. These results demonstrate that decentralized, semantically adaptive routing can improve the scalability and fault tolerance of multi-agent systems.

---


### 23. [Generative Artificial Intelligence Chatbots for Motivational Interviewing: A Scoping Review From System Design to Intervention Outcomes](https://arxiv.org/abs/2609.20902)

**<font color=#1a73e8>作者：</font>** Runze Hu, Jingqi Kong, Yang Yang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Motivational interviewing (MI) is a collaborative approach to elicit autonomous motivation for health behavior change. Generative AI (GenAI) offers new ways to deliver MI via conversational systems, but evidence on their design, assessment, and translation into interventions remains fragmented. This scoping review characterized evidence on GenAI-MI chatbots across system design, safety, MI quality, user perceptions, and intervention outcomes. We conducted a PRISMA-ScR scoping review. Nine datasets were searched for studies published or publicly available from January 1, 2015 to June 2, 2026 that used GenAI to generate MI chatbot responses or counselor utterances. Data were extracted using a predefined framework and synthesized descriptively. Forty-seven reports (48 studies) were included. Twenty (41.7%) focused on system design without direct participant use; 28 (58.3%) involved direct interaction. Most systems were text based and disembodied; 23 (47.9%) incorporated dynamic adaptation. Safety measures were unevenly reported. Among studies with direct use, 21/28 (75.0%) reported informed consent or user education. Thirty (62.5%) assessed MI quality, generally suggesting MI-consistent interactions. User perceptions were favorable, especially empathy, usability, helpfulness, and intention to use, though measures were heterogeneous. Eighteen (37.5%) reported intervention outcomes, mostly after a single session. Positive findings were more consistent for short-term motivation than sustained behavioral or functional change. GenAI-MI chatbots can deliver MI-consistent interactions perceived favorably, but evidence for sustained behavioral or functional change is limited. Future research should strengthen runtime safety monitoring, standardize MI quality assessment, and use longer-term comparative designs with behavioral and functional outcomes.

---


### 24. [Do Quantum Models Scale Like LLMs?](https://arxiv.org/abs/2609.20912)

**<font color=#1a73e8>作者：</font>** David S. Berman, Ying-Jer Kao, Roger G. Melko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> In this work, we study the neural scaling laws of RydbergGPT, an autoregressive transformer model trained on qubit projective measurement data gathered from interacting Rydberg atom arrays. The quantum system is known to exhibit a finite-size remnant of a critical point as the laser detuning parameter is varied. We find that near the critical point the transformer loss as a function of training dataset size is well described by a power-law with a loss floor correction. However, away from criticality the quality of the power-law description is substantially reduced. We then compare the statistical structure of both Rydberg measurements and natural-language corpora using an entropy-normalised, finite sample corrected mutual information "two-point" function. We find that near-critical statistics of the two point functions are closest to those observed in natural-language, whilst other qubit configurations far from the critical point have two-point functions that decay more rapidly. This supports the hypothesis that multi-scale dependence contributes to stable neural scaling, and that scaling behaviour should be viewed as a property of the model-data pair.

---


### 25. [When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation](https://arxiv.org/abs/2609.20942)

**<font color=#1a73e8>作者：</font>** Sy-Tuyen Ho, Minghui Liu, Furong Huang  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly participate in scientific evaluation, both as automated reviewers and as assistants to human reviewers. As model-generated reviews enter public data and future training corpora, AI peer review can become recursive: later reviewers learn from judgments produced by earlier models. We study one step of this feedback loop in a controlled setting. Starting from Llama 3.1 8B, we first fine-tune a reviewer on official ICLR reviews from 2018--2023 and then train four successor models on ICLR 2024 data with systematically varied mixtures of official and model-generated reviews. Our study shows that introducing synthetic reviews compresses rating distributions and reduces both same-paper and corpus-level semantic diversity. We call this pattern $\textbf{scientific-judgment collapse}$.
To mitigate this failure mode, we introduce $\textbf{TrustReviewer}$, an open-source LLM-based system for generating peer reviews of AI and machine learning papers. TrustReviewer intervenes at two complementary stages. For training-time prevention, we train the core reviewer in a single stage on a curated corpus designed to reduce low-quality and semantically degenerate supervision. For test-time correction, paired activation steering aims to further mitigate residual tendencies toward collapsed judgments without further training or additional expert annotation. Together, these results characterize a concrete risk of recursive reviewer training and provide practical interventions for preserving judgment diversity and improving recommendation alignment in AI-assisted scientific evaluation.

---


### 26. [MemeTAG: Keyword-Driven Meme Classification through Tag Embedding Reconstruction](https://arxiv.org/abs/2609.20962)

**<font color=#1a73e8>作者：</font>** Akshit Sharma, Prashant W. Patil  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> The proliferation of harmful internet memes poses a significant societal threat, yet their automated classification remains a formidable algorithmic challenge due to the nuanced, multimodal nature of their content. To address this, we introduce MemeTAG, a novel dual-objective framework that pioneers a keyword-aware approach to meme classification. Our core innovation is a two-part semantic guidance mechanism: first, we leverage a pretrained Vision-Language Model to generate a set of descriptive keywords, that capture the high-level semantics. Second, we introduce the Aggregated Tag Inference Network (ATIN), an attention-based module that distills these keywords into a single, rich semantic embedding. This embedding serves as a target for a novel auxiliary reconstruction loss, which compels the model to learn deeply aligned visual and textual features. This approach, combined with an efficient three-stage training strategy, establishes a new state-of-the-art on the HarMeme, Hateful Memes Challenge (HMC), and PrideMM datasets, decisively outperforming existing state-of-the-art methods.

---


### 27. [RBS-Attention: Radius-Bounded Sparse Prefill for Long-Context Large Language Models](https://arxiv.org/abs/2609.20971)

**<font color=#1a73e8>作者：</font>** Chuxu Song, Jiuqi Wei, Zhencan Peng  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-context large language model inference is increasingly limited by prefill, where dense self-attention processes the entire prompt before generation begins. Sparse block selection can reduce this cost, but a block centroid may hide a highly relevant token among many irrelevant ones. We call this failure mode mean dilution and propose RBS-Attention, a training-free sparse-prefill method with two complementary selection branches. A centroid base branch captures average relevance, while a rescue branch uses the maximum key-block radius and its prompt-, layer-, and head-dependent distribution to identify blocks at risk of underestimation. Independently thresholding the two branches and combining their masks controls the contribution of rescue blocks while preserving regular block-sparse FlashAttention execution. On H100 GPUs, RBS-Attention achieves 20.65$\times$ standalone prefill-attention speedup, 11.92$\times$ vLLM prefill-attention speedup, and 5.97$\times$ end-to-end time-to-first-token speedup at 128K on Qwen3-30B-A3B-Instruct-2507-FP8. On the dense Qwen3-32B model, it obtains 88.65 overall RULER accuracy versus 89.52 for dense attention; LongBench-v2, InfiniteBench, and Video-MME provide additional quality evaluation. Supporting experiments measure actual retention, compare selectors at matched density, and characterize block-size, threshold, and memory behavior. Together, these results support radius-adaptive dual-branch selection as an effective approach to long-context prefill.

---


### 28. [Attention-Aware Routing: Coupling Routing and Attention in MoEs](https://arxiv.org/abs/2609.20974)

**<font color=#1a73e8>作者：</font>** Despoina Kosmopoulou, Anastasios Tsetsilas, Efthymios Georgiou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In Mixture-of-Experts language models, the router typically selects and weights experts based on the token's hidden state, utilizing limited contextual information. We propose Attention-Aware Routing (AAR), which augments the router with temporal and spectral features extracted from a sliding window of attention weights that represent a summary of the model's contextual state, disentangled from the hidden state. Keeping the base transformer entirely frozen, we train only the routing parameters, isolating routing as the sole variable. AAR improves GSM8K by +3.37 pp over a routing-only SFT baseline on OLMoE. Beyond performance, we show that routing and attention form a coupled circuit: routing changes at layer l propagate through the residual stream to amplify attention sinks at layer l+1, reshaping attention without any direct update to the attention mechanism itself. Further, AAR reduces long diverging generation, with incorrect answers getting shorter, while correct answers remain unchanged in length. Finally, AAR is strongly depth-sensitive: applying it indiscriminately across layers can degrade factual retrieval, whereas mathematical reasoning gains persist when it is introduced deeper in the network. This sensitivity exposes a retrieval--reasoning tension across depth and makes layer-selective AAR a controlled probe of the routing-relevant information carried by attention at different layers.

---


### 29. [CaLR: Causal Latent Revision for Robust Diffusion Reasoning](https://arxiv.org/abs/2609.20981)

**<font color=#1a73e8>作者：</font>** Wei Cai, Jian Zhao, Yuchen Yuan 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Autoregressive (AR) models suffer from local greediness, while diffusion language models (DLMs) often lack the strict causal structure required for reasoning. To combine the advantages and overcome the drawbacks of the dual, we propose Causal Latent Revision (CaLR), a framework that reformulates reasoning as constrained latent optimization. By adopting a causal topology matrix (CTM) from an expert model and implicit differentiation, CaLR performs gradient-guided ``thought revision" to enforce logical consistency, enabling dynamic self-correction of intermediate steps during parallel generation. Empirically, CaLR achieves SOTA DLM performance on complex benchmarks, surpassing strong AR baselines and demonstrating superior robustness in constrained tasks like Sudoku.

---


### 30. [Trustworthy FinAInce: Unpacking How AI-Mediated Financial Advice is Judged](https://arxiv.org/abs/2609.20989)

**<font color=#1a73e8>作者：</font>** Aryan Ramchandra Kapadia, Eshwar Chandrasekharan, Koustuv Saha  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As generative AI is increasingly used as a source of personal financial guidance, understanding how people appraise such advice is important for supporting appropriate reliance. We conducted a randomized vignette experiment with 285 U.S. adults across eight financial decisions, independently varying three advice styles---AI, expert, and online community---and displayed source labels while holding the underlying recommendation consistent. Advice style most strongly shaped message and safety appraisals, Expert labels selectively increased perceived source knowledge, and decision context primarily shaped risk and safety appraisals. These appraisals were associated with downstream judgments, with models explaining 69.2% of overall quality, 75.9% of trust, and 82.9% of intended reliance. Expert-style advice also remained most preferred when shown without source labels. Our findings have implications for understanding financial advice evaluation, distinguishing the roles of advice style and source labels, and designing financial AI that supports grounded evaluation rather than simply maximizing trust.

---


### 31. [Understanding How Educators Configure GenAI Support for Open-Ended Learning -- An Exploratory Study of K-12 Career Exploration](https://arxiv.org/abs/2609.21019)

**<font color=#1a73e8>作者：</font>** Si Chen, Xinyue Chen, Artur Mullagaliyev 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI (GenAI) can support open-ended learning through generation, personalization, and learner modeling, yet educators need ways to shape these capabilities around educational goals. Through interviews and design activities with 15 U.S. educators, we examined educator configuration of GenAI using K-12 career exploration as an exploratory context. Educators configured not only AI-generated experiences, but also when student activity became an inference, whether learner information persisted, who could access it, and how it informed subsequent human action. They also faced challenges translating teaching needs into configurations: recognizing possibilities for control beyond familiar uses of GenAI, decomposing general-purpose AI into understandable functions and responsibilities, and identifying useful information through intended teaching actions. We discuss how GenAI systems can support educators in expressing and testing configurations, while establishing boundaries around personalization, inference, persistence, disclosure, and action to keep AI-supported learning aligned with evolving learner needs.

---


### 32. [Stiefel-AdamW: Geometry-Aware AdamW for Linear Factorization Blocks](https://arxiv.org/abs/2609.21039)

**<font color=#1a73e8>作者：</font>** Emanuele Zangrando, Marco Sutti, Francesco Tudisco  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> A pervasive structural pattern in modern deep learning is the linear factorization block: a submodule of the form $W = BA$ in which two parameter matrices are multiplied directly, with no intervening nonlinearity. Such blocks appear in LoRA adapters, low-rank compressed layers, query-key products of self-attention, and share a common pathology: the factorization is non-unique, which can destabilize training and limit usable learning rates. Despite this, factorization blocks are typically optimized with standard Euclidean methods that ignore the underlying geometry. We introduce Stiefel-AdamW, a near drop-in replacement for AdamW for use wherever such blocks appear. By constraining one factor on the Stiefel manifold while leaving the other Euclidean, Stiefel-AdamW relaxes the full $\mathrm{GL}(\mathbb{R}^r)$ gauge symmetry to a compact orthogonal symmetry, ruling out factor blow-up while retaining the coordinate-wise diagonal preconditioning that gives AdamW its practical strength. Moment estimation is performed in the ambient Euclidean space, with geometry entering only through a tangent-space projection and a manifold retraction. The implementation overhead over AdamW is minimal, and we show that the resulting optimizer inherits both the stability benefits of Riemannian methods and standard convergence guarantees. We validate Stiefel-AdamW on LoRA-style fine-tuning of GPT2, ViT, and Mistral 7B and on full pretraining of GPT2 on OpenWebText, showing consistent improvements over strong baselines at essentially no additional cost over AdamW.

---


### 33. [Aligning with Lived Experience: Heterogeneous Benefits of Fine Tuning in Mental Health Support Generation](https://arxiv.org/abs/2609.21075)

**<font color=#1a73e8>作者：</font>** Mohit Chandra, Nabin Kim, Eli Min 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> As access to professional mental healthcare remains limited, many individuals turn to online platforms such as Reddit to seek peer support situated within human lived experience. However, a significant portion of such queries go unanswered, presenting an opportunity for using Large Language Models (LLMs) to fill this gap. While LLMs have demonstrated strong performance on clinical benchmarks, their ability to generate lived-experience informed and community-aligned peer support is underexplored. Addressing this gap, we introduce the COmmunity-centered Peer Engaged Support (COPES) dataset and a three-axis evaluation framework to assess LLM alignment with community perspectives to mental health support seeking queries. Evaluating zero-shot and post-trained (SFT and DPO) models, we show that post-training on COPES significantly improves Strategy Alignment (>50% for general-purpose models) and alignment in Emotion & Tone. However, we also observe that such improvements are heterogeneous and alignment improvements vary significantly across subreddits and requested coping strategies. Furthermore, post-training induces distributional shifts, heavily favoring problem-focused recommendations while suppressing emotion-focused strategies. Together, this work shows that while curating community-driven data improves the alignment of LLM responses, model performance remains disparate across distinct sub-communities and specific mental health needs.

---


### 34. [Geometry of Values: Task Vector Composition for Ethical Preference Alignment in Language Models](https://arxiv.org/abs/2609.21094)

**<font color=#1a73e8>作者：</font>** Utkarsh Agarwal, Monojit Choudhury  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are increasingly deployed in applications that must weigh clashing moral values, yet even strong models exhibit hidden biases and brittle instruction-following across languages. We introduce a 12,000-instance dataset of two-option dilemmas covering pairwise three value conflicts: Honesty vs. Justice, Justice vs. Autonomy, and Autonomy vs. Honesty, along with their translations into Hindi, Arabic, Spanish, and Chinese, to probe cross-lingual behavior. Benchmarking on GPT-5-mini reveals that it consistently favors Honesty over Autonomy across all five languages when no policy is given. The Llama-3.2-1/3B models exhibit strong first-option bias; however, both plain fine-tuning and Direct Preference Optimization fine-tuning effectively remove this bias, increasing accuracy to greater than 98%. In order to decouple the effect of learning correlations in the dataset from abstract values, we propose a task vector transfer based experiment where after computing the task vectors for a direction of value preference we orthogonalize it with respect to the general instruction following vector. Our experiment shows that this method is effective in isolating the direction of the specific value preference that can successfully be used to conduct task arithmetic to obtain a model with the opposite stance.

---


### 35. [Detecting Hallucination in LLMs: Tracing the Topological Signatures of Impaired Context Sharing](https://arxiv.org/abs/2609.21096)

**<font color=#1a73e8>作者：</font>** Amir Jalilifard, Anderson Rocha, Eric Wong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> In this work, we examine the topology of information flow patterns within attention graphs to effectively distinguish hallucinated from non-hallucinated responses. We analyze the Forman-Ricci curvature to identify structural patterns indicating information bottlenecks in attention graphs. We then introduce a method that captures both semi-local and global information-flow characteristics of attention heads associated with hallucinated responses. We evaluate our approach extensively across several LLMs and established benchmarks. Empirical results demonstrate that our proposed single-pass approach provides consistent improvements over existing attention-based and multi-response baselines across two hallucination-detection benchmarks, while achieving competitive performance across diverse LLM architectures. Further analysis reveals that impaired context sharing among tokens during causal generation is strongly associated with hallucination occurrences in LLMs. In particular, hallucinated responses are consistently characterized by an over-reliance on self-attention, diffused context retrieval from earlier tokens, or information over-squashing, especially in the final transformer layer.

---


### 36. [NetInspector: Measuring and Improving LLM Capabilities for Reliable Intent-Based Networking Policy Generation](https://arxiv.org/abs/2609.21103)

**<font color=#1a73e8>作者：</font>** Yuxuan Zhang, Hongxin Hu, Guofei Gu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern networks are large in scale and heterogeneous in configuration, making manual policy management increasingly impractical. Intent-Based Networking (IBN) addresses this by automating the translation of high-level operator goals into low-level network configurations. Yet existing IBN systems rely on static heuristics and fixed-feature classifiers that generalize poorly to distribution shifts such as new service definitions or evolving phrasing in operator requests. Large Language Models (LLMs), with strong reasoning and translation capabilities demonstrated across many domains, are a natural candidate for IBN policy generation. However, it is unclear whether LLMs can be reliably applied to this task, nor whether their use mitigates or worsens the underlying security risk.
In this work, we show that while fine-tuned LLMs excel at intent translation, they exhibit false negative rates when checking whether a proposed intent violates an existing security policy. The root cause is not a lack of logical reasoning capability, but LLMs lack of persistent grounding in network topology and group hierarchy. Motivated by this finding, we introduce NetInspector, a three-layer agentic framework that enforces a verify-then-act protocol, decoupling information retrieval from reasoning so that the LLM focuses on symbolic reasoning while every policy decision is grounded in verifiable network facts retrieved from a live Environment Layer before approval. On NetInspector-Bench, a 2,224-sample synthetic benchmark spanning campus, enterprise, and WAN topologies, NetInspector reduces FNR by over 30\% relative to ungrounded baselines and remains robust under linguistic distribution shifts.

---


### 37. [Talk to Me, Jarvis: An Open-Source Edge-Deployable Voice Assistant Framework for Autonomous Racecars](https://arxiv.org/abs/2609.21109)

**<font color=#1a73e8>作者：</font>** Daniel Henel, Frederik Werner, Alexander Langmann 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models have improved their effectiveness as back-end components for voice assistants, particularly in intent understanding and context-aware input classification. However, online-hosted models introduce network dependency and variable inference latency, limiting their suitability for time-critical autonomous driving applications. In this work, we address these issues by developing Jarvis, an offline voice assistant for high-level behavioral commands of autonomous vehicles. Its architecture integrates speech recognition and synthesis with natural language command classification into a lightweight, local framework. Jarvis core component is a text-to-command classifier, built using a domain-specific fine-tuning of the Mistral 7B model, demonstrating low-latency inference. Our experimental evaluation demonstrates that our solution outperforms larger online-hosted models, achieving 97.63 % intent recognition accuracy with an average processing latency of 1.39 s, making it well-suited for operations requiring quick response times. To support further research and fine-tuning, we provide an open-source implementation.

---


### 38. [Decoupling Internal Representational Changes and Causal Importance in Fine-Tuned Large Language Models](https://arxiv.org/abs/2609.21113)

**<font color=#1a73e8>作者：</font>** Lingfang Li, Procheta Sen, Shubham Das 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning has emerged as a widely adopted approach for adapting LLMs to a variety of downstream tasks. However, how it reshapes their internal mechanisms remains poorly understood. To address this, we investigate how fine-tuning alters internal representations in LLMs, including attention patterns and layer-wise activations, and examine whether these changes are linked to task-relevant components identified by EAP (e.g., attention heads and logit-level activations) that drive task performance. We find that EAP-identified components are concentrated within specific layers, indicating a degree of functional localisation in how models internalise task-specific behavior. Notably, the distribution of these components across layers is largely uncorrelated with the layers undergoing the most substantial representational changes during fine-tuning. Furthermore, we observe that overlap in EAP-identified components across tasks does not translate into cross-task performance transfer if the tasks are different in nature (e.g. classification vs. generative tasks). More specifically, fine-tuning on one task can lead to a degradation of performance on another when the two tasks exhibit a high degree of overlap in their EAP-identified components.

---


### 39. [TinyCeNN-LM: Quality-Gated Conversion of Pretrained Attention with CeNN-Inspired Cellular-Recurrent Layers](https://arxiv.org/abs/2609.21139)

**<font color=#1a73e8>作者：</font>** Kabeh Mohsenzadegan, Vahid Tavakkoli, Kyandoghere Kyamakya  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Replacing attention in a pretrained language model is a compatibility problem: a plausible substitute may alter representations expected by later layers. TinyCeNN-LM introduces a \emph{quality-gated post-training conversion} framework using CeNN-inspired cellular-recurrent layers with bounded local processing, compact recurrent memory, routing, fusion, and accept-or-rollback validation. Three implementations are studied: Integrated Memory, MemoryFusion, and PDelta3-GDN2-CLVR+Local32. Strict PDelta3 conversion accepts a layer only when representation and NLL criteria pass fixed thresholds. On SmolLM2-135M, layers 0-2 are accepted with cumulative $\Delta\mathrm{NLL}=+0.01209$, while layer 3 is rejected despite acceptable NLL because representation fidelity fails. On Qwen3.5-0.8B, full-attention layers 3, 7, and 11 are accepted with final $\Delta\mathrm{NLL}=+0.02073$. Integrated Memory keeps perplexity within $-0.07\%$ to $+0.93\%$ while reducing total cache by up to $6.01\%$. A sampled 200-item downstream sanity check gives $28.5\%$--$32.0\%$ overall accuracy for converted Qwen releases. The results support conservative, quality-gated structural conversion rather than universal attention replacement or speedup.

---


### 40. [Exploring Text Classification Models with Sparse Autoencoders](https://arxiv.org/abs/2609.21142)

**<font color=#1a73e8>作者：</font>** Daniel Kerrigan, Brian Barr, Enrico Bertini  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As language models (LMs) rise in prominence, there is interest in making them more transparent in order to better understand their internal behavior. Recent interpretability work has focused on using sparse autoencoders (SAEs) to break down neuron activations at a given layer in the LM into human-understandable features, where each feature represents a concept that the model has learned. In this paper, we share work on using SAEs to analyze the behavior of text classification LMs. We present techniques for exploring the relationships between the SAE's features and the model's predictions and errors. We integrate these techniques into SAEfarer, a tool for analyzing concepts learned by text classification LMs. We assess SAEfarer in an expert pilot evaluation with five Ph.D. students.

---


### 41. [Clinician-Grounded Quality Assurance for AI-Assisted Psychiatric Intake](https://arxiv.org/abs/2609.21149)

**<font color=#1a73e8>作者：</font>** King Shi, Amanda Li, Jonathan Ivey 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Before patients can use AI-assisted psychiatric intake systems, health systems need practical ways to routinely evaluate these tools against their clinical standards for quality assurance. Because clinicians may use different intake styles, evaluation for this task must (1) support comparison across interviewing approaches, (2) minimize clinician burden, and (3) measure clinically relevant performance for health systems deploying these technologies. We present a clinician-grounded evaluation platform built around a memory-augmented patient simulator for open-ended AI interviewing, InterviewPlayground. We created interactive patients using InterviewPlayground with our expert-authored vignettes, constructed a simulated intake platform for the interviews, and designed evaluation modalities relevant to intake. In a pilot of 6 clinicians in a 25-minute assessment compared to a GPT-based LLM intake interviewer, the LLM recovered more of the clinically relevant items embedded in the patient vignettes (88.0% vs. 38.9%), but made more clinical inferences not based on the interview (56.8% vs. 27.8%), and characterized identified safety concerns less often (33.3% vs. 66.7%), setting the stage for deployed quality assurance for this task.

---


### 42. [CoLearn: An Agentic Tutor that Learns its Learner in a Human--AI Co-Learning Loop](https://arxiv.org/abs/2609.21154)

**<font color=#1a73e8>作者：</font>** Kailai He, Zhihao Wu, Linhai Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Good tutoring adapts to the individual: it tracks what a learner knows, notices why they go wrong, and asks the next question that will help most. Most deployed tutoring tools instead serve fixed item banks and treat a wrong answer as a single bit of signal. We present CoLearn, an interactive, agentic tutor that supports an iterative tutoring loop: the learner practises, and the system builds an evidence-grounded memory of the learner's mastery and misconceptions. This memory is updated as evidence accumulates and is used to generate the next personalised question. CoLearn has three components: (i) a persistent learner-state memory that updates per-topic mastery with a soft-evidence variant of Bayesian Knowledge Tracing, where a large language model acts as a continuous observation function; (ii) adaptive question generation that targets the learner's weakest topic and recurring misconceptions; and (iii) an evidence view that makes personalisation visible and testable through live progress visualisation and blind A/B comparison. In blind A/B evaluation, questions conditioned on this memory are preferred over non-personalised ones 68-69% of the time, and in persona simulations with hidden ground-truth mastery the agent's belief converges toward the learner's true mastery.

---


### 43. [Can Agents Design Better Chips with a Higher Level Abstraction?](https://arxiv.org/abs/2609.21157)

**<font color=#1a73e8>作者：</font>** Zijian Ding, Yang Zou, Yizhou Sun 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) agents are increasingly being explored for chip design, but most existing approaches operate directly at RTL. We ask whether agents can design better chips by leveraging higher-level abstractions. We compare Direct RTL Design, Agent-based HLS Design, Post-Compiler HLS Refinement, and Post-HLS RTL Refinement, and combine Agent-based HLS Design with Post-HLS RTL Refinement as Agent-based HLS with RTL Refinement (AHRR). We use FPGAs as a practical, easy-to-deploy platform for end-to-end evaluation, but note that the design-flow tradeoffs we study are largely independent of the target technology. Across a diverse 11-tasks benchmark suite, AHRR achieves a 2.6$\times$ geometric-mean speedup over Direct RTL Design across our benchmark suite. Case studies show that HLS distills design knowledge into abstractions that agents can leverage, while RTL refinement recovers lower-level optimization opportunities. Together, these results make AHRR a promising workflow for agentic chip design. The code and evaluation artifacts are available at this https URL.

---


### 44. [M2G-LLM: Enhancing Clinical Prediction via Multimodal Graph Reasoning and LLM Context Injection](https://arxiv.org/abs/2609.21164)

**<font color=#1a73e8>作者：</font>** Inyoung Choi, Sukwon Yun, Jiayi Xin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Integrating diverse data modalities --- such as clinical notes, laboratory results, and medical imaging --- is essential for advancing clinical decision-making. While Large Language Models (LLMs) have shown remarkable performance in processing unstructured clinical text, their limited capacity to incorporate non-text modalities hinders their broader utility in healthcare applications. Here, we introduce M2G-LLM (Multimodal MedGraph-LLM), a novel framework that enhances LLMs with multimodal integration and alignment via Graph Neural Networks (GNNs). Our approach models temporal relationships between patient visits, propagates information across clinically similar patients, and aligns heterogeneous data sources to construct enriched multimodal context vectors. These vectors are injected into the intermediate layers of the LLM, enabling joint reasoning over textual and non-textual modalities. We evaluate M2G-LLM on the MIMIC-IV and MIMIC-CXR datasets, demonstrating improvements in clinical prediction tasks over strong baseline models. Our results highlight the promise of combining the language understanding of LLMs with the relational reasoning capabilities of GNNs for comprehensive, multimodal healthcare analysis.

---


### 45. [SpecOpt: Contact-Diff Reasoning for Agentic Molecule Optimization Toward Binding Specificity](https://arxiv.org/abs/2609.21165)

**<font color=#1a73e8>作者：</font>** Thao Nguyen, Heng Ji  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Off-target protein binding is a major source of adverse effects for small-molecule drugs, yet most structure-based molecular design methods focus on generating selective compounds de novo rather than improving the selectivity of existing, well- characterized drugs. We introduce specificity optimization (SpecOpt), a molecular design task that seeks constrained structural modifications to an existing compound that increase its binding preference for an intended target over known off-targets while preserving its structural identity and drug-like properties. To enable systematic evaluation, we construct a ChEMBL-derived benchmark from compound-target interaction data, identifying intended targets through curated drug-mechanism annotations and off- targets through measured activities. We then develop an agentic framework that docks each compound against its intended target and off-targets, compares the resulting poses through residue-aware atom-protein contacts, and provides these differential interactions to a large language model to propose targeted structural modifications. Candidates are retained only if they satisfy molecular similarity, ADMET, and target-off-target docking selectivity criteria. On 915 compounds, the agent improves the target- off-target binding gap for 84.8% of compounds, shifting the mean gap from -0.72 to +0.47 kcal/mol while maintaining a mean Tanimoto similarity of 0.72 to the starting compounds. Ablation studies identify residue-specific contact information as the critical optimization signal: replacing residue identities with binary contact indicators eliminates improvement on all 29 ablation compounds. These results establish SpecOpt as a distinct molecular design problem and demonstrate residue-aware differential interactions as an effective signal for improving the specificity of existing compounds.

---


### 46. [TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching](https://arxiv.org/abs/2609.21172)

**<font color=#1a73e8>作者：</font>** Zhihao Shu, Md Musfiqur Rahman Sanim, Jie Hu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are moving onto mobile devices for increasingly diverse workloads over text, images, video, and audio. These applications often require long contexts, making the Key-Value (KV) cache a dominant memory bottleneck because it grows linearly with sequence length and is accessed at every decoding step. Prior work reduces KV-cache footprint through low-rank compression, token eviction, or flash offloading, but the resulting reconstruction overhead, irreversible token loss, or I/O stalls can offset the benefit of saving memory. We present TierKV, a mobile LLM inference framework built on Predictive Multi-Tier Cache Optimization (PMCO). Before decoding starts, PMCO predicts future cache demand from prefill hidden states and jointly assigns tokens to exact, low-rank, and flash-offloaded tiers under the device memory and accuracy budgets. This formulation retains access to the full context, removes the circular dependency of reactive eviction, and admits a closed-form solver that selects tier boundaries and per-layer ranks at runtime. Across eight text, vision, and audio models on three mobile SoCs, TierKV improves prefill throughput by up to 17.6x over existing mobile LLM frameworks, reduces RAM-resident KV cache by 12.5-34%, thereby enabling substantially longer contexts under the same memory budget, while incurring only minor accuracy degradation.

---


### 47. [Not All Irregularity Is Equal: Causally Isolating a Rare Failure Mode in Japanese Morphological Inflection](https://arxiv.org/abs/2609.21179)

**<font color=#1a73e8>作者：</font>** Wen Zhang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Neural morphological generation systems often achieve high aggregate accuracy on benchmark datasets, yet such performance can conceal systematic errors clustered in rare morphological subclasses. We present an orthography-aware diagnosis of Japanese past-tense verb inflection, treating hiragana not merely as a transcriptional medium but as a representational system that encodes morphophonological structure. Using two character-level Transformer architectures evaluated across five random seeds, we show that although both systems exceed 97% aggregate accuracy, a single structurally specific irregular subtype, verbs whose stems end in /e/ and require gemination before the past-tense suffix and make up fewer than 1% of the data, accounts for a disproportionate 30-43% share of residual errors and contributes roughly 34-48x its prevalence to total errors. We then move from diagnosis to causal isolation: controlled ablation experiments show that removing this subtype alone produces larger accuracy gains than removing all irregular verbs combined. These findings indicate that error concentration in neural morphological learning is not driven by irregularity per se, but by the interaction between extreme low-frequency morphological patterns and specific orthographic processes. We argue that morphological evaluation should incorporate fine-grained subclass analysis, and discuss implications for data-efficient, developmentally plausible language model pretraining.

---


### 48. [When Better Turns Do Not Make Better Agents: Diagnosing the Gap Between Next-Turn Metrics and Workflow Success](https://arxiv.org/abs/2609.21187)

**<font color=#1a73e8>作者：</font>** Md Tahmid Rahman Laskar, Xue-Yong Fu, Gundeep Singh 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Agent models are frequently evaluated one decision at a time, where the model predicts the next action based on the gold interaction history, which is scored against a reference. We investigate whether improvement under this protocol is predictive of improved autonomous workflow execution. We study pre-SFT and supervised fine-tuned (SFT) Qwen3 models at 4B and 14B parameters and Gemma 3 models at 4B and 12B parameters on multi-turn customer-support workflows. We find that SFT consistently improves text-turn success, and that overall next-turn success increases for every model under gold-history evaluation. However, these improvements do not transfer to autonomous workflow execution. Tool-specific gains also vary across metrics and models. None of the four SFT models succeeds under holistic workflow evaluation, with strict trajectory completion reaching at most 10.4% workflow success. Our results show that next-turn evaluation is not a reliable proxy for workflow success, motivating separate reporting of text quality, local action correctness, tool execution, and end-to-end task completion.

---


### 49. [SWE-Proof: Can Language Models Resolve Real-World Issues with Machine-Checked Proofs?](https://arxiv.org/abs/2609.21190)

**<font color=#1a73e8>作者：</font>** George Ma, Benjamin Mikek, Haoyu Li 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Ensuring the correctness of LLM-generated code is a core challenge for modern software engineering. Benchmarks for agentic code generation check correctness with held-out test suites, which are inherently incomplete and increasingly susceptible to memorization. Formal verification avoids both problems, but existing work covers only standalone tasks whose specifications are given as input, not real issues, which touch large repositories and state intent in vague natural language. We present Benchproofer, a pipeline that turns a coding task with a known correct patch into a formally verified one: it writes a specification for the new code, summarizes the existing functions that code calls with axioms, and admits an instance only after mechanical and adversarial gates agree. Applying it to SWE-bench Verified yields SWE-Proof, 500 real issues whose correctness is formally verified rather than tested, and it extends to SWE-bench Pro. Across two frontier models, verification catches what tests miss: a quarter to a half of test-passing patches admit counterexamples, which a structured natural-language specification does not fix, while a correct formal one lifts resolution from 85% to 95% for Opus 4.8. Writing that specification is the hard part: models that must write their own gain nothing over an unaided baseline, and only 62% of their specifications pass our audit. The usual failure is faithfulness, a specification that constrains part of the required behavior and leaves the rest free. Specification quality still tracks the outcome, failing on 89% of unresolved instances against 47% of resolved ones, making faithful specification synthesis a concrete open problem.

---


### 50. [Information-Gain Rewards over Diversity-Pruned Tests: GT-Anchored Verifier Co-Training for Reliable Code Generation](https://arxiv.org/abs/2609.21208)

**<font color=#1a73e8>作者：</font>** Ana Nunez, Peyman Najafirad  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-play methods that co-train a single language model as both coder and test author promise to move code-generation RL beyond fixed test suites, but they suffer from two coupled pathologies: permissiveness collapse, where pass-rate rewards are maximised by trivial, non-discriminative tests, and concentration bias, where i.i.d. sampled tests cluster on modal inputs and inflate estimator variance. We introduce CoVer (Co-trained Coder and Verifier), a single-policy GRPO framework that addresses both failure modes. First, an information-gain (IG) reward scores each self-generated test by the mutual information between its pass/fail vector and a graded, ground-truth-anchored correctness signal y [0, 1] m, gated by the sign of their covariance so that only positively discriminative tests receive reward. Second, a three-stage diversity-aware selection step prunes a candidate pool to a behaviourally non-redundant suite (invalidity, input-string, execution-profile filtering), raising the effective sample size of the IG estimator at fixed execution budget. On five benchmarks (LiveBench, MBPP, LiveCodeBench, CodeContests, Code-Forces), CoVer raises one-shot pass@1 by +5.8 points at 7B and +7.1 points at 14B over the Qwen2.5-Instruct backbone, and achieves the highest macro-average among all compared methods at both scales. As a drop-in backbone inside the CodeT ranking pipeline, CoVer-7B adds +3.5 points, demonstrating the dual benefit of co-training for both generation and selection.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-148](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
