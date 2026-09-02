# 🧠 大模型相关研究 | 2026年09月03日

> 本类共 **295** 篇论文：已确认 **283** 篇，待复核 **12** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-295](./part-06.md)

---

### 201. [Subliminal Learning as Trait-Direction Drift: A Mechanism and Targeted Control under SFT Distillation](https://arxiv.org/abs/2609.01091)

**<font color=#1a73e8>作者：</font>** Zhixuan Liu, Zhichen Dong, Yuyu Fan 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Beyond intended capabilities, model distillation can transfer hidden traits from a teacher. A teacher biased by a system prompt can generate semantically clean training data, such as numeric sequences, that still causes a downstream student to inherit the hidden preference, a phenomenon known as subliminal learning. Prior work has identified several parts of this process. How the signal builds up during training and produces behavioral transfer remains unclear, making targeted mitigation difficult. We propose and validate trait-direction drift as a mechanism for subliminal learning: biased generation creates measurable preference gaps in teacher data, and student-recognizable gaps induce trait-aligned updates during supervised fine-tuning that accumulate into behavioral transfer. Guided by this mechanism, we propose probe-space corridor regularization, a targeted defense that constrains drift along a calibrated trait direction during distillation. The method substantially reduces hidden-trait transfer, preserving task performance: for example, it lowers malicious-response transfer from 29.55% to 6.45% with low main-task accuracy cost, and consistently suppresses animal-preference transfer across the main Qwen setting. The preference-gap, training-trajectory, and intervention evidence links subliminal learning to trait-direction drift and motivates corridor regularization as a targeted control during distillation.

---


### 202. [Beyond Magnitude: Contrastive Routing for Modular Mixture-of-Experts](https://arxiv.org/abs/2609.01100)

**<font color=#1a73e8>作者：</font>** Nikolaos Xiros, Dimitrios Damianos, Maria-Eleni Zoumpoulidi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> In current Mixture-of-Experts architectures, routing is performed based on representations dominated by structure shared across all tokens, limiting expert specialization. We show that contrasting each token against an Exponential Moving Average of the layer's hidden states, rather than routing on absolute magnitude, concentrates the routing signal onto a low-dimensional, highly separable subspace. Building on this, we propose the Contrastive Routing Mechanism (CoRM), which scores each expert by the gap between its affinity for the incoming token and its affinity for this shared reference state, interpreted through a distinct per-expert projection. The resulting experts have routing boundaries that align with linguistic structure significantly more than the Top-k baseline. Our experiments show that CoRM improves average zero-shot accuracy by +0.67 to +1.69 points (Top-1) and +1.38 to +1.77 points (Top-2) over standard Top-k MoE baselines on nine zero-shot reasoning benchmarks, at the minimal cost of 2.9% added parameters and 2.6% added FLOPs per token.

---


### 203. [ClinTraceBench: Source-Verifiable Longitudinal Clinical Reasoning over EHR-Derived Dialogues](https://arxiv.org/abs/2609.01111)

**<font color=#1a73e8>作者：</font>** Huimin Wang, Zhengyi Zhao, Yutian Zhao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Clinical LLM assistants must reason over multi-visit patient trajectories, yet whether the compact history representations used to scale them---retrieval, structured timelines, LLM summaries, agentic memory---preserve the longitudinal signal clinical reasoning needs has not been measured. We introduce ClinTraceBench: 385 MIMIC-IV-derived verified dialogues with event-ID provenance, a nine-task taxonomy (T1--T9), and L0--L4 deterministic + L5 human-audit validation (98.92\% agreement). We evaluate eight history representation strategies---a no-context floor, \textit{last-visit-only}, \textit{full-context}, BGE-M3 \textit{dense-retrieval}, two compression schemes, and two agentic-memory systems (\textit{Mem0}, \textit{A-Mem})---across four backbones (DeepSeek-V3, GPT-4o-mini, Haiku~4.5, Sonnet~4.6) on 6{,}271 questions: 32 cells, 200{,}672 predictions. Four findings: (SP4) a controlled T3 injection probe isolates compression-induced \textit{relation} loss---with the attribution sentence present \textit{before} construction, \textit{Mem0}, \textit{A-Mem} and \textit{llm-summary} still recover only 0--5.3\% of the injected positives; (SP1) compressed strategies pay an aggregation tax on multi-visit trends and cross-patient comparisons; (SP2) the blind-to-full gap spans $+29.8$~pp (GPT-4o-mini) to $+62.7$~pp (Haiku); (SP3) abstention scales non-monotonically with context length. On the Pareto frontier Haiku dominates Sonnet under \textit{full-context} (\$25.76 vs.\ \$106.21), inverting the ``biggest backbone wins'' heuristic.

---


### 204. [EDRAC: Benchmarking Arabic Dialect Reading Comprehension](https://arxiv.org/abs/2609.01113)

**<font color=#1a73e8>作者：</font>** Noor Abo Mokh, Kirill Chirkunov, Teresa Lynn 等 18 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dialectal Arabic (DA) remains under-resourced compared to Modern Standard Arabic (MSA), particularly for machine reading comprehension (MRC) and question answering (QA). Existing Arabic QA benchmarks primarily focus on formal written MSA or multiple-choice QA, with limited coverage of naturally spoken dialects. Here, we aim to bridge this gap. We introduce EDRAC, the first large-scale benchmark for dialectal Arabic machine reading comprehension (MRC) and generative QA, covering five major dialects: Egyptian, Moroccan, Emirati, Syrian, and Saudi Arabic. EDRAC contains 499 passages derived from naturally occurring spoken interactions and 4,977 corresponding QA pairs generated through a human--LLM collaborative pipeline combining iterative generation, LLM-as-a-judge evaluation, and human verification. We benchmark Arabic-centric and multilingual LLMs on EDRAC using lexical and semantic metrics. Our results reveal substantial gaps between semantic answer quality and dialectal fidelity, highlighting the limitations of existing evaluation metrics for dialectal Arabic generation. EDRAC provides a realistic and challenging MRC benchmark for future research on dialectal Arabic NLP.

---


### 205. [Latent Recurrent Thoughts: Recurrent Refinement of Proposed Latents for Reasoning with Frozen LLMs](https://arxiv.org/abs/2609.01117)

**<font color=#1a73e8>作者：</font>** Zhaoliang Chen, Jie Fu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chain-of-thought reasoning unfolds in discrete token space: each step is committed as text, errors propagate, and eliciting good traces presupposes traces to imitate. Reasoning instead in a model's continuous representation space - where intermediate states are vectors rather than words - sidesteps these constraints, but leaves open how those latent states should be computed. We approach this along two axes. First, we keep a large language model (LLM) frozen and use it for what it is already good at - modeling and decoding sequences - while a small auxiliary network supplies continuous latent thoughts as input. Second, we produce those latents by recurrence: a tiny recurrent reasoner refines them over many steps, decoupling the depth of computation from the size of the model, so that the latents are a product of iterative processing rather than a single forward pass. We instantiate this as Latent Recurrent Thoughts (LRT): a task-dedicated proposer supplies base latents, a recurrent reasoner refines them through bounded residual corrections, and the frozen LLM decodes the answer. On symbolic reasoning with answer supervision but no reasoning traces (Countdown-4, Sudoku) and on natural-language reasoning (HumanEval, MBPP, StrategyQA), LRT substantially outperforms prior frozen-decoder continuous-space reasoning methods under an identical decoder, prompt, data, and training budget, and outperforms non-thinking-mode chain-of-thought prompting on the same backbone at a small fraction of its inference compute.

---


### 206. [Does task decomposition improve automatic NLG evaluation?](https://arxiv.org/abs/2609.01139)

**<font color=#1a73e8>作者：</font>** Sebastian Steindl, Nikos Voskarides, Alberto Gasparin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The LLM-as-a-judge (LLMaJ) framework has emerged as a promising solution for cheap, reproducible, reference-free Natural Language Generation (NLG) evaluation. Prior work seeks to improve LLMaJ by decomposing evaluation tasks into simpler sub-tasks. In this work, we systematically compare LLMaJ methods with and without decomposition on multiple NLG datasets. We find no evidence that LLMaJ with task decomposition leads to performance gains over a fair baseline that does not use decomposition. Instead, we find that previously reported performance gains in decomposition-based LLMaJ stem from using human labels as training data, and not task decomposition itself. Also, we find that, when human labels are available, LLMaJ without using task decomposition can perform comparably to human annotators.

---


### 207. [Revisiting Face Recognition for Monozygotic Twins: The Celeb Twins Test Set](https://arxiv.org/abs/2609.01141)

**<font color=#1a73e8>作者：</font>** Michael Zang, Haiyu Wu, Mrinal Sharma 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Past literature on face recognition for monozygotic (("identical") twins points to facial marks and mirror asymmetry as possible directions for improved accuracy of twins recognition. The Celeb Twins Test Set (CTTS) contains web-scraped image pairs for 80 sets of celebrity twins. It is the only twins test set with meta-data for twins with distinguishing skin marks and possible mirror asymmetry. CTTS is organized in the manner of face verification test sets such as LFW, CALFW, CPLFW, CFP-FP, and AgeDB-30. Current deep CNN matchers can achieve over 76% accuracy in classifying CTTS same-person / different-person image pairs. We show that current matchers do not make use of skin marks, or asymmetry, and discuss reasons for this. Finally, we discuss the feasibility of using generative AI tools such as Grok, ChatGPT and Gemini to create images of imagined monozygotic twins as a means to increase representation of twins in face recognition training sets.

---


### 208. [On the Design Fundamentals of Pixel Text Representation Learning](https://arxiv.org/abs/2609.01147)

**<font color=#1a73e8>作者：</font>** Chaohao Yuan, Ruifeng Yuan, Zhuoxu Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Text-rich visual inputs require models that can read, retrieve, and compress language directly in pixel space, yet existing pixel-text encoders struggle with fixed resolution pretraining, visual shortcut learning, weak visual grounding, and multilingual visual text understanding. In this work, we investigate the fundamental design principles required for robust visual text representation learning. Through systematic controlled ablations, we identify four critical components: variable image resolutions and rendered font sizes provide spatial proxies for high-resolution document generalization; natural image-text pairs are indispensable for grounding and prevent text-only collapse; layout-aware rendering helps prevent pixel-level shortcuts; and a two-stage multilingual curriculum enables effective cross-lingual alignment. By integrating these principles into a scalable training recipe, we train Pixel Linguist II, a native-resolution vision encoder trained with on-the-fly rendering, unified contrastive grounding, and a multilingual curriculum over 280M training examples. Pixel Linguist II sets new state-of-the-art results on English, cross-lingual, and multilingual Visual STS and ViDoRe, while also enabling better MLLM downstream evaluation. Notably, Pixel Linguist II remains robust under 80\% visual token compression, showing great promise for optical context compression. Our code and resources are available at this https URL.

---


### 209. [Dotting the Eye: An Intent-Driven Image Retouching Agent for Visual Focus Enhancement](https://arxiv.org/abs/2609.01148)

**<font color=#1a73e8>作者：</font>** Chujie Qin, Zilong Zhang, Zewei Chang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Image retouching is commonly formulated as enhancing overall visual quality through color adjustment, but in practice, it also serves to emphasize visual focus by guiding viewers' attention toward a specific subject or region. Achieving such focus-oriented retouching is inherently challenging, as it requires well-coordinated global and local adjustments to manipulate perceptual saliency while maintaining visual naturalness. This intricate process typically demands substantial professional expertise. In this study, we propose EyeControl, a MLLM-driven agent with a diffusion-based retouching executor that enables visual focus enhancement under weak user intent. With only a few clicks or coarse strokes, EyeControl directs visual attention to the intended region, effectively "dotting the eye" of the image. The core idea is to explicitly link the weak user intention with the target editing region and the corresponding tonal adjustment operations during retouching. To achieve this, the system first interprets the intent and image content to infer the visual focus and generate structured intent guidance for the retouching executor. Second, the retouching executor is encouraged to respond more strongly to the target region, explicitly aligning its attention map with a designed pseudo-intent map. We also introduce an operation-consistency constraint to improve coordination between global and local adjustments, achieving more natural and coherent retouching. Additionally, we contribute ControlArt-Bench, a high-quality evaluation dataset for visual focus enhancement. Extensive evaluations demonstrate that EyeControl yields perceptually appealing results with stronger intent alignment. Code can be found in this https URL.

---


### 210. [CopyShield: A Cross-Level Benchmark of Copyright Defenses in LLMs](https://arxiv.org/abs/2609.01161)

**<font color=#1a73e8>作者：</font>** Maryam Alshehyari, Dushyant Singh Chauhan, Samuele Poppi 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can reproduce memorized text verbatim, yet copyright defenses are usually evaluated under incompatible protocols. We introduce CopyShield, a controlled benchmark comparing three representative defenses at distinct intervention levels: contrastive decoding (output), Direct Preference Optimization (behavioral), and activation intervention (representation). We evaluate CopyShield on two model families, LLaMA-3.1-8B and Mistral-7B-v0.3, using controlled memorization over five public-domain books and a shared protocol measuring literal leakage, calibrated non-literal leakage, utility, and degeneracy. Across these methods, intervention level is associated with distinct compliance-utility trade-offs. On LLaMA-3.1-8B, contrastive decoding remains near-degeneracy-free (0-2%) but reaches a literal-suppression floor at NV-Recall 0.192-0.203. DPO nearly eliminates literal leakage (0.263 to 0.002) but induces paraphrase-loop degeneracy in 58% of QA outputs, with no utility gain over the SFT baseline. Activation intervention attains the lowest non-literal flagging rate (1/200) by blocking 84% of non-literal queries before generation. Human evaluation confirms that DPO has low coherence, whereas activation lowers perceived copyright risk through broad refusal. On Mistral-7B-v0.3, the output- and representation-level patterns persist, while DPO degeneracy falls to 10-14%, showing that its severity is model-dependent. Together, CopyShield provides cross-level reference baselines and identifies targeted non-literal suppression as an open challenge. The code is available at this https URL.

---


### 211. [Classic AI Scaffolding for LLM Social Agents](https://arxiv.org/abs/2609.01167)

**<font color=#1a73e8>作者：</font>** Anatole Gershman  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language models can produce locally plausible social turns, but fluent next-turn generation is not enough for social simulation. Human encounters such as restaurant lunches and hotel check-ins are bounded social episodes with roles, scripts, material state, obligations, commitments, timing, and closure conditions. We present EpisodeSim, a hybrid LLM-agent architecture that represents classic-AI structures as natural-language control state interpreted by LLM calls. A World Master maintains shared reality, constructs scenes, adjudicates proposed actions, tracks effects and obligations, and controls closure. Experiments with small qualitative ablations on two held-out settings support a design claim: LLM fluency supplies local texture, but coherent social simulation benefits from persistent classic-AI-style scaffolding that organizes behavior over time.

---


### 212. [Pre-carved Niches: The Formation Dynamics of Modular Task Partitions in Early LLM Training](https://arxiv.org/abs/2609.01170)

**<font color=#1a73e8>作者：</font>** Guangqi Li, Yongxin Li  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models exhibit a modular internal organization that mirrors well-studied functional networks of the human brain, but how this organization forms during training is unknown: prior work has characterized finished models, not the formation process. We track formation step by step: we train a Pythia-410M model from scratch (two trajectories, bf16 and fp32) and run attribution patching at every step, alongside probes for gradient norms, effective updates, weight norms, and first-order loss decomposition across 14 tasks in four cognitive domains. Three findings. First, the modular map is pre-carved: before any learning, the dominant task pair already overlaps at ~3.6x the attribution substrate (a task-independent baseline), and its layer-0 concentration is an architecture-level constant on this model family. Second, the partition locks in through two sharp jumps whose amplitudes do not track the learning-rate schedule (the second reaching 20.4 sigma quiet-window / 6.2 sigma global), accompanied by gradient-level relative deprivation--winners receive 2.25->2.73x the loser's gradient supply, 9.5-11.5 standard deviations below a random control--that does not propagate to updates or weights. Third, deviation from the substrate appears only in the domain being learned, consistent with the hypothesis that modularity tracks learning. We close by separating the feature-level account we can defend from the mechanistic questions we cannot, and we pre-register the scale-threshold hypothesis behind our ongoing 2.8B experiments.

---


### 213. [A SoK for SoCs: Reading the TI Leaves on AI for Cyber Threat Intelligence Generation and Sharing](https://arxiv.org/abs/2609.01174)

**<font color=#1a73e8>作者：</font>** Saastha Vasan, Hadjer Benkraouda, Jizhou Chen 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Cyber Threat Intelligence (CTI) is essential for defending mission-critical infrastructure, yet the process of transforming raw attack evidence into shareable CTI remains fragmented and understudied.
We conduct a literature survey of academic papers, organizing the CTI lifecycle into three stages: Threat Data Collection, CTI Generation and Sharing, and CTI Consumption. The first and third stages are well represented in the literature, whereas only a small number of papers address CTI Generation and Sharing. To learn how this stage is practiced, we survey practitioners across multiple organizations who routinely generate and share CTI. They describe a largely manual process with four recurring challenges: preventing the exposure of sensitive information, extracting indicators from noisy attack data, correlating observed behavior with standardized tactics, techniques, and procedures (TTPs), and translating CTI into the formats that sharing platforms require.
Using the insights from the practitioner survey, we divide the CTI Generation and Sharing stage into four steps: Intelligence Extraction, Normalization and Enrichment, Codification, and Distribution. We then conduct pilot studies that probe the feasibility of current Large Language Models (LLMs) for each step. The pilot studies show that LLMs can assist an analyst in each of the four steps. However, the models recover only a fraction of the indicators the evidence contains, struggle to ground every claim in the supplied evidence, and do not judge what keeps shared intelligence useful to its recipients. Each step therefore requires expert supervision. Based on these observations, we derive three research directions for automating the production of shareable intelligence.

---


### 214. [LLMPEDIA: Browsing, Verifying, and Comparing the Parametric Encyclopedic Knowledge of LLMs](https://arxiv.org/abs/2609.01182)

**<font color=#1a73e8>作者：</font>** Muhammed Saeed, Simon Razniewski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Flagship language models appear saturated on benchmarks like MMLU (Hendrycks et al., 2021), scoring above 90% - yet benchmarks test only what the experimenter thought to ask, the availability bias of fixed question sets. LLMPEDIA makes this bias measurable and browsable. We recursively materialized ~1.3M articles from three model families' parametric memory (GPT-5-mini, DeepSeek-V3.2, Llama-3.3-70B) without retrieval, then audited a stratified sample of atomic claims against Wikipedia and a curated web stack, coloring every claim supported, refuted, or insufficient (Saeed and Razniewski, 2026). On a uniform random sample the true rate is 68.4% - more than 21 pp below MMLU - with 30.5% of claims insufficient: assertions no benchmark probes and the world's largest encyclopedia cannot adjudicate - long-tail knowledge or plausible hallucination, the evidence cannot tell - extending to free text the coverage gap GPTKB established for triples (Hu et al., 2025). The resulting live, open encyclopedia lets visitors inspect this frontier one claim at a time through five one-click views - link-traversal exploration, claim-level factuality, cross-model and political-persona comparison, and a guided topic drill-down - each page, claim, and verdict at a stable URL. LLMPEDIA is live at this https URL

---


### 215. [Reveree: Diagnosing LLM Reverse-Engineering Agents](https://arxiv.org/abs/2609.01185)

**<font color=#1a73e8>作者：</font>** Hadjer Benkraouda, Hongyu Cai, Berkay Celik 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Reverse engineering (RE) is critical to security tasks such as malware analysis and vulnerability discovery, and large language model (LLM) agents are increasingly able to perform it autonomously. Capture-the-flag (CTF) RE challenges have become the standard proxy for measuring this capability, but evaluation rests on a single criterion: whether the agent captures the flag. This solve rate reveals neither where in the RE process an agent fails nor whether a success reflects analysis of the binary or recall of a public solution. In this paper, we propose Reveree, a diagnostic framework that scores an LLM RE agent's trajectory at three tiers: solve rate, milestone progress through an eight-stage RE schema, and a behavioral profile of its actions. Comprehension stages are scored by an outcome-blinded LLM judge validated against a human expert; all other stages are verified deterministically. Using Reveree, we evaluate nine frontier models and four prompting strategies on 88 picoCTF and NYU-CTF challenges. We find that the base model dominates performance, whereas prompting strategy is a secondary, model-dependent effect. Surprisingly, larger, newer, or costlier models are not reliably stronger. We also find that failures concentrate at the comprehension stages of the RE process, and that extra budget, persistence, or reasoning effort rescues few of them, pointing to a competence limit rather than a resource limit. Regarding memorization, while models reproduce picoCTF flags from challenge descriptions alone, NYU-CTF shows minimal measurable recall, and most solves survive surface perturbation, indicating that genuine analysis coexists with memorization. We release Reveree to the community.

---


### 216. [PersuaRL: Reinforcement Learning-Driven Multi-Expert Selection for Persuasive Dialogue Generation in Insurance](https://arxiv.org/abs/2609.01188)

**<font color=#1a73e8>作者：</font>** Rohan Kirti, Akash Ghosh, Aryan Vats 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) are revolutionizing digital communication by powering conversational agents deployed across domains such as customer service, digital sales, and insurance. These agents, built on LLMs, can understand user input, retrieve relevant information, and generate coherent responses. However, while they excel at factual communication, they often lack the ability to engage in truly persuasive, context-sensitive dialogue, especially in domains like insurance, where trust and clarity are critical. Building on this need within the insurance domain, our work focuses on improving the persuasiveness of digital agents, aka LLMs. To support this, we introduce InsureDial, a Persuasive Insurance Dialogue dataset, designed to capture the nuances of persuasive communication specific to motor insurance interactions. We introduce PersuaRL, a reinforcement learning-based framework that equips LLM-driven dialogue agents with the ability to adaptively explore, select, and coordinate strategies across multiple expert modules, guided by the evolving dialogue context, to achieve more effective persuasion. We conduct extensive automatic human and qualitative evaluations on two benchmark persuasion dialogue datasets, including our InsureDial. Our evaluations consistently demonstrate that PersuaRL outperforms baseline, generating contextually appropriate and highly persuasive responses.

---


### 217. [Births are difficult to predict even with rich survey and full-population register data](https://arxiv.org/abs/2609.01194)

**<font color=#1a73e8>作者：</font>** Elizaveta Sivak, Emily M. Cantrell, Thomas Emery 等 100 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Major life events have proven difficult to predict. Does this reflect limits of theory, data, and algorithms, or the large role of chance? We examine one outcome - having a child within three years - through a near-ideal setting for prediction: a data challenge where 147 researchers predicted births for Dutch residents aged 18-45, using survey data and full-population registers. Methods ranged from logistic regression to a large language model and transformers. Predictions were moderately accurate (best F1: register 0.59, survey 0.76); advanced models did not outperform classical ones; and the larger registers did not beat the survey. Simulating the stochastic biology of conception and pregnancy, we estimated a predictive ceiling (survey F1 ~ 0.86-0.94, register 0.88-0.96). Observed performance falls short of this ceiling, implicating imperfect data, methods, and unmodelled chance, while the ceiling itself shows that chance in reproduction alone sets a non-trivial limit on predicting individual lives.

---


### 218. [CaRL-EM: Cost-Aware Reinforcement Learning for Entity Matching with LLMs](https://arxiv.org/abs/2609.01195)

**<font color=#1a73e8>作者：</font>** Chaohui Guo, Michel Klein, Zhisheng Huang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Entity matching (EM) requires fine-grained contextual understanding and domain knowledge. Recent work shows that large language models (LLMs) can serve as strong matchers across domains, but most methods either make independent pairwise decisions or rely on manually designed composite pipelines, thus lacking flexibility in realistic multi-candidate settings. At the same time, they typically ignore inference cost at scale. We formulate LLM-based EM with candidates as a cost-aware sequential decision problem and propose CaRL-EM, a reinforcement learning controller that manages LLM operations. Given the state of an anchor record, its candidate set, and the cost, CaRL-EM adaptively chooses among different operators (Match/Compare/Select/Decide) and model capacities to maximize a quality-cost objective. The policy interacts with abstract operators, allowing the same controller to be reused with different underlying LLM backends at inference time without retraining. Experiments on 7 benchmarks show that CaRL-EM (i) learns to dynamically plan the usage of inexpensive and expensive operators based on task complexity, (ii) achieves robust zero-shot transfer across diverse datasets and domains, and (iii) consistently achieves a better quality-cost trade-off than strong LLM-based baselines and manually designed pipelines, yielding a lower inference cost at comparable or higher quality.

---


### 219. [FinLifeBench: Exhaustive Life-Event History and Financial-State Reconstruction from Longitudinal Banking Dialogue](https://arxiv.org/abs/2609.01198)

**<font color=#1a73e8>作者：</font>** Hangyeul Lee, Juyoung Oh, Jaeyong Ko 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Repeated banking interactions require assistants to maintain complete, current, and traceable customer records as life changes emerge incidentally in routine requests. Existing benchmarks emphasize question answering, bounded episodes, or targeted recall rather than exhaustive longitudinal reconstruction. We introduce FinLifeBench, which evaluates two tasks over the same cumulative dialogue: reconstructing every life-event instance with its first-establishing session and reconstructing a complete 34-path financial state at consecutive checkpoints. The benchmark contains 6,000 eight-turn Korean banking sessions from 20 independent synthetic trajectories, with deterministic, exhaustive gold for 24 event types and 34 state paths and consensus quality assurance. Across eleven LLMs under a full-context condition, event-anchor recall falls from 0.591 at 15 sessions to 0.445 at 300. Errors are driven primarily by omitted events rather than poor anchor localization, while financial-state reconstruction frequently treats superseded or potentially outdated information as current; the best GCA@15 reaches 0.470. Performance on the two reconstruction tasks is only weakly associated. These results show that models can localize evidence for recovered events while still failing to maintain complete and temporally valid longitudinal records.

---


### 220. [Compressing AI Traffic: Standardized Neural Network Coding of Visual-Token Representations in Split Vision-Language Inference](https://arxiv.org/abs/2609.01200)

**<font color=#1a73e8>作者：</font>** Reza Heidari, Hamed R. Tavakoli, Juho Kannala  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> When the visual encoder and the language decoder of a vision-language model (VLM) run on different compute nodes, the intermediate visual-token embeddings become a communicated payload rather than an internal activation. We call such machine-consumed intermediate tensors AI traffic and ask how far they can be compressed with a standardized, training-free codec. We insert ISO/IEC 15938-17 Neural Network Coding (NNC) round trips on the complete visual interface of a Qwen3-VL-8B-Instruct video question answering pipeline, comprising the main visual-token representation and the DeepStack feature streams, while leaving weights, prompts, and generation untouched, and sweep the quantization parameter (QP) over a wide rate range. Closed-ended Video-MME accuracy remains close to the uncompressed reference up to a 98% reduction of the transmitted BF16 tensor and only then collapses; open-ended MLVU generation shows the same plateau-and-collapse profile under an LLM judge. This robustness is not due to near-lossless reconstruction: the decoded tensor is heavily discretized, carries substantial row-wise relative L2 error, and has a visibly steeper singular-value decay than its source. Downstream reasoning therefore depends on coarse structure and relative geometry rather than exact floating-point values, which argues for rate-task rather than rate-distortion optimization of AI traffic codecs.

---


### 221. [Who Judges the Judges? A Chinese Safety QA Benchmark for Evaluating LLM Responses and Safety Judges](https://arxiv.org/abs/2609.01210)

**<font color=#1a73e8>作者：</font>** Rui Yang, Shuang Huang, Junhua Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Safety benchmarks for large language models often assess the risk of a user query, although the outcome of question answering depends on whether the response violates a policy. This distinction is critical in Chinese harmful-content evaluation, where linguistic variation and adversarial transformations can obscure risky intent. We introduce C-SafeQA, a policy-grounded benchmark for response-level Chinese safety evaluation. It comprises 538 base queries and 8,877 adversarial queries answered by four full-model LLM deployments, yielding 37,660 query-response records labeled safe, unsafe, or disputed. Reference labels are generated through agreement-aware multi-model adjudication and blind audits of stratified subsets by three safety experts. C-SafeQA supports both evaluation of target-model safety and auditing of seven automated safety judges against shared reference labels. Unsafe-response rates range from 0.93% to 3.35% on base queries and from 11.68% to 30.05% on adversarial queries. On the adversarial subset, judges show substantial trade-offs between unsafe-response recall and risk-query-conditioned safe-response false positive rate, and no judge dominates all metrics. Both acrostic transformations reduce unsafe recall for all seven judges, revealing mechanism-specific evaluator weaknesses. Dataset records, metadata, verification code, and judge scripts are publicly released to support recomputation, while benchmark construction, target-response generation, and private adjudication remain outside the release boundary.

---


### 222. [REFACTOR-VLA: Unsupervised Library Learning of Typed Motor Programs](https://arxiv.org/abs/2609.01215)

**<font color=#1a73e8>作者：</font>** Riyaaz Shaik, Chandru Venkataraman  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Most vision-language-action (VLA) models -- OpenVLA, $\pi_0$, RT-2, RDT-1B -- are monolithic: they emit raw motor commands or short action chunks without organizing behavior into reusable abstractions, so they degrade on long-horizon tasks and resist interpretation. Existing skill-discovery methods sidestep the core question of when two action sequences are behaviorally equivalent, either clustering contrastive embeddings or delegating the judgment to a language model uncalibrated to the robot's dynamics. We introduce REFACTOR-VLA, a wake/sleep system for learning reusable skills. Its sleep phase clusters motor-program fragments under a Behavioral-Equivalence Kernel (BEK) computed from rollouts of a learned latent world model $M_\phi$; its wake phase emits typed lambda terms over a Hindley--Milner-inspired vocabulary, consumed by a library-conditioned rectified-flow action decoder. Abstractions are admitted only if they pass Minimum Description Length and return-preservation gates. On LIBERO we report two findings. First, enlarging the world model from 188M to 430M parameters worsened performance on 4 of 4 suites, so capacity alone does not help. Second, the training objective matters far more: adding an auxiliary supervised contrastive (InfoNCE) loss during world-model warmup substantially improves sleep-phase clustering, giving Normalized Mutual Information at $n=3$ seeds of $0.462 \pm 0.021$ (object), $0.867 \pm 0.025$ (spatial), $0.915 \pm 0.013$ (goal) and $0.754 \pm 0.010$ (LIBERO-10), and beating the strongest published baseline on all 4 suites by a mean $\Delta = +0.184$. Across providers ($n=12$) the 95% bootstrap confidence interval for mean pairwise NMI is $[0.683, 0.729]$ (mean $0.705$). The sleep phase also yields the first real-LIBERO task-language library: the decoder uses 2 of 3 admitted abstractions and rewrites all 256 sampled demonstrations.

---


### 223. [H2Table: Hierarchical Hypergraph-Enhanced Large Language Models for Complex Table Reasoning](https://arxiv.org/abs/2609.01216)

**<font color=#1a73e8>作者：</font>** Jia Ling, Yangfan Wang, Chen Tang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tables are ubiquitous across diverse domains, yet reasoning over them remains a significant challenge for modern large language models (LLMs). Current approaches typically linearize tables into sequences, inherently overlooking their intrinsic two-dimensional and hierarchical structure. To address this, we propose H2Table (Hierarchical Hypergraph-Enhanced Table Reasoning), a novel framework that represents complex tables as hierarchical nested hypergraphs. To process this representation, we design a tailored hypergraph encoder to facilitate message passing between hyperedges (headers) and nodes (cells), thereby perceiving the semantic entailment relationships between them within complex tables. Furthermore, we introduce a set of learnable query vectors acting as a lightweight bridge to extract representative structural embeddings from the encoder into the LLM. Experimental results demonstrate that our approach effectively handles complex table question answering tasks with hierarchical nested headers. Notably, on the HiTab dataset, H2Table achieves an average improvement of 22.88% over state-of-the-art baselines on highly complex tables with a nesting depth of four. Our code is available at: this https URL.

---


### 224. [Prompt-Robust Language Models: Which Training Strategies Work?](https://arxiv.org/abs/2609.01217)

**<font color=#1a73e8>作者：</font>** Frederic Sadrieh, Michal Štefánik  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Despite their strong performance, large language models remain highly sensitive to prompt formulation. Prior work addresses this through refined data construction or through dedicated robustness objectives. We reproduce and compare these strategies under controlled conditions, and measure how effective they are in addressing models' prompt sensitivity. We find the current robustness fine-tuning methods improve over standard fine-tuning and in-context learning, but the best-to-worst prompt gap remains as high as 40-57% of performance. Moreover, the recent robustness-enhancing methods we test - CoIN for contrastive alignment and PPCL for consistency regularization - often fail to outperform the simplest data construction strategy: training on one template per batch. Our diagnostics explain these results. The auxiliary objectives move the quantity they penalize, but do not generalize beyond it. Additionally, data construction strategies differ due to the conflicting signs of per-template gradients on 57-64% of parameters. Thus, batches that mix formulations force the optimizer to reconcile competing updates instead of finding a shared, prompt-agnostic one.

---


### 225. [S$^2$Prune: Spatially Structured Visual Token Pruning for Multimodal Large Language Models](https://arxiv.org/abs/2609.01224)

**<font color=#1a73e8>作者：</font>** Yuanyuan Jia, Shunpu Tang, Qianqian Yang  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Visual token pruning reduces the inference overhead of multimodal large language models (MLLMs) by retaining only a subset of visual tokens. Existing methods usually select tokens based on importance or redundancy. However, we observe that these criteria produce stable spatial biases across inputs and do not always outperform simple Uniform Grid sampling, highlighting the value of broad spatial coverage. Motivated by this, we propose S$^2$Prune, a training-free pruning method that preserves spatial coverage while adapting token density to local image structure. We first divide the image into regions and assign at least one token to each region to preserve coverage. The remaining token budget is then distributed according to Laplacian variation, giving more tokens to regions with richer structure. We then use Early Representation Change (ERC), computed from the first decoder block, to select representative tokens within each region. We evaluate S$^2$Prune across diverse settings and two MLLM architectures. On Qwen2.5-VL-7B-Instruct, it achieves the highest average accuracy among the evaluated training-free pruning methods. With only 32 of the original 576 visual tokens, it still retains 79.3% of the full-model performance. Code is available at this https URL.

---


### 226. [MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence](https://arxiv.org/abs/2609.01235)

**<font color=#1a73e8>作者：</font>** Walid Saidi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> MutMem V1 introduced retention-preserving, cryptographically authorized mutation for persistent agent memory but did not provide a complete portable verification contract or clean-install reproduction path. MutMem V2 closes that publication gap without introducing a second memory engine. It specifies exact canonical bytes, domain-separated object and bundle commitments, mandatory recall-evidence membership and ordering, external trust anchors, identity epochs, revocation, authorization, request receipts, ordered disclosure, and three mutation terminal types. The released protocol contains 18 versioned object schemas, 39 recall vectors, 15 mutation vectors, and 37 closed recall failure reasons. Independent Node and Python implementations agree on verdict and primary reason for all 72 structural and cryptographic terminals; a production-conformance corpus agrees on 42/42 cases across 28 required classes. A clean Node v26.8.1 installation reaches first-boot, restart, and scheduler readiness with no experimental memories. A separately scoped 120-unit Canary experiment supports only explicit-marker traversal. Every public table regenerates from a self-hashed aggregate, and an independent verifier reconstructs the statistics and claim boundaries. Historical V1 empirical results remain historical. MutMem V2 supports claims about portable integrity, authorization, traceability, conformance, and reproducibility under stated assumptions; it does not establish semantic truth, universal robustness, or independent replication.

---


### 227. [Post-Training Science for Supervised Fine-Tuning](https://arxiv.org/abs/2609.01244)

**<font color=#1a73e8>作者：</font>** Charles O'Neill, Mudith Jayasekara, Harry Partridge  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Every supervised fine-tuning run forces the same chain of decisions, such as learning rate, batch size, LoRA or full fine-tuning, how many epochs, which optimiser, and what data to feed the model. Each of these is typically rediscovered from scratch for every new model and dataset. Here we measure them under one instrument: a sweep that varies one lever at a time, and spans dense and mixture-of-experts models in two families (Qwen3 and Llama), on four real-world customer SFT datasets, for both LoRA and full fine-tuning. These datasets give a controlled testbed: each task carries an evaluation built with the customer, and its training data is produced by iterative supervised fine-tuning that refines model outputs until they pass that evaluation, so the supervised target is internally consistent and the task judge we report against is the criterion the data was built to satisfy. We ask how the optimal learning rate and batch size move with model scale, family, and data, and whether one selection rule transfers across them; what LoRA trades against full fine-tuning, and how its rank and alpha set what the adapter can learn; whether validation loss (or other metrics, such as loss landscape flatness) faithfully ranks downstream quality; whether post-training gains scale with model size and data volume, on a model ladder extended through mixtures-of-experts to 235B parameters; how many epochs to train before general instruction-following erodes; and whether a geometry-aware optimiser improves on AdamW. Each recommendation is paired with a measure of its uncertainty.

---


### 228. [Explore More, Drift Less: Outcome-Only Reinforcement Learning Can Suffice for Long-Horizon Interactive Agents](https://arxiv.org/abs/2609.01245)

**<font color=#1a73e8>作者：</font>** Liming Pu, Xiaoxia Li, Yifu Liu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning is a natural way to post-train LLM agents for long-horizon interactive tasks judged only by end-of-task verification, yet a shared belief holds that outcome-only RL soon hits a ceiling on small open models. Recent work therefore compensates around the training with denser rewards, SFT priors, skill libraries, curated memory, or multi-agent orchestration. We argue the ceiling is an artifact of two failures of common practice. Signal starvation: group-relative RL with sparse outcome-only rewards yields a gradient only when a task's rollout group mixes successes and failures, so under-scaled exploration silences exactly the hardest, most instructive tasks. Policy drift: squeezing many updates out of a small task pool degrades the policy itself, as an unanchored objective lets the sampling distribution collapse exactly when saturation has already made informative groups rare. We present CANOPY (Coverage-ANchored On-PolicY RL), a minimalist protocol attacking both directly: scale same-task exploration until the natural signal reappears, keep every update on-policy, KL-anchored, and confined to the agent's own action tokens, then cash in an enlarged interaction budget at test time. On AppWorld, a long-horizon interactive coding benchmark, a Qwen3-14B policy trained with CANOPY through environment interaction alone--without task-specific supervision, auxiliary credit signals, or elaborate agent scaffolding--topped the public leaderboard (Feb. 2026; Test-Normal TGC 86.9, Test-Challenge 67.6), and the same design principles lift Qwen3.5-9B on SWE-bench Verified by 16.6 points. Agentic RL alone thus internalizes long-horizon capability directly into a small open model; we plan to release the complete training stack at this https URL.

---


### 229. [Ready to Speak: Aligning LLMs for TTS-Friendly Text Generation](https://arxiv.org/abs/2609.01246)

**<font color=#1a73e8>作者：</font>** Thibaut Thonet, Jos Rozen, Laurent Besacier  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Current Large Language Models (LLMs) are primarily optimized for written text, often producing outputs that are grammatically correct and helpful yet poorly suited for spoken delivery via Text-to-Speech (TTS). In this work, we study how to make LLMs natively generate TTS-friendly text, which we frame as a preference alignment problem: instead of relying on downstream rewriting modules, we directly align LLMs to generate text optimized for spoken delivery. We introduce two preference datasets spanning different target domains, CORA and Recipe, which contain paired TTS-friendly and TTS-unfriendly responses. We further propose an evaluation suite combining a pattern-based heuristic metric, a TTS$\to$ASR evaluation pipeline, and a MUSHRA listening study with human judges. Our experiments compare the recently proposed Feature-aware Sampling and Tuning (FaST) framework -- leveraging interpretable features instead of a black-box reward model -- against an array of alignment baselines on the TTS-friendly generation task. Notably, we found that FaST achieves the best overall tradeoff between TTS-friendliness and helpfulness across various settings. We also identified a strong correlation between our different metrics, highlighting the ability to reliably assess TTS-friendliness via an efficient heuristic.

---


### 230. [Measuring the Behavioral Fidelity of Long-Horizon Human Activity Simulations](https://arxiv.org/abs/2609.01257)

**<font color=#1a73e8>作者：</font>** Yi Fei Cheng, Fan Yang, Iremsu Bas 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLM-based human simulators are increasingly used for policy, evaluation, and training, they must faithfully reproduce real behavioral patterns. While prior work has examined behavioral fidelity in survey responses and dialogue, longer-horizon real-world activity remains largely unexplored. We introduce a framework for evaluating behavioral fidelity in long-horizon activity simulations across temporal granularities and levels of analysis. As a case study, we collect a 43-hour multi-camera dataset of in-the-wild office activity and compare trace-derived conditioning mechanisms: persona descriptors, few-shot exemplars, and statistical transition and time-of-day priors. We find that behavioral fidelity is not uniform across metrics: statistical priors bring activity and sequence distributions closest to real behavior, yet over-fragment routines and suppress within-person variability. These findings motivate a more holistic evaluation that spans multiple metrics, temporal granularities, and levels of analysis.

---


### 231. [Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents](https://arxiv.org/abs/2609.01272)

**<font color=#1a73e8>作者：</font>** Jinqing Zhao, Chengcan Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Prospective memory means carrying out a deferred intention at the right future cue while other work continues. Benchmarks now isolate it as an agent skill, yet frontier LLMs still struggle: the best published PM-Bench scaffold reaches only 65.1% Set-F1. We argue that this loop is schema-constrained state tracking rather than open-ended reasoning, and that small models can execute it when the action space is typed. We propose the Prospective Intention Store (PIS) that puts lifecycle logic in code and scoped language work on the model. The scaffold is agentic and training-free: no selector fine-tuning and no trajectory distillation. On PM-Bench, DeepSeek-Chat with PIS reaches 82.9% Set-F1. On Gemma-E2B, Set-F1 is only 4.2% without a store and at most 6.6% under seven retrospective memories, while PIS reaches 66.2%. PIS further reaches 70.1% Set-F1, where retrospective memory methods stay at most 54.4%. PIS sets a new state of the art on this benchmark and enables small models to surpass the published large-model scaffold.

---


### 232. [From Base Rollouts to RL Reasoning: A Budgeted Search Perspective](https://arxiv.org/abs/2609.01274)

**<font color=#1a73e8>作者：</font>** Wenhe Sun, Cunxiang Wang, Zijun Yao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning with verifiable rewards (RLVR) improves language-model reasoning, but how these gains relate to inference-time decoding and search remains unclear. Does RL create reasoning the base model lacks, or shift the rollout distribution toward trajectories it can already reach but rarely samples? We study this behaviorally with a Unified Decoding Framework (UDF), which expresses token-level sampling, beam-like search, tree search, and sequence-level resampling as executable policies over a shared budgeted operating space, scored post hoc with pass@$k$, self-consistency, best-of-$N$, and first-finish success. Using paired Base/RL checkpoints from SimpleRL-Zoo, we ask whether an RL default-policy curve can be approximated by a structured path of Base operating points. On Math500, AIME, GPQA, and IFEval, the pass@$k$ recovery path follows a Budgeted Operating-Point Transition Rule (BOPTR), $N_{\mathrm{Base}} \approx \alpha N_{\mathrm{RL}}^{\beta}$, with benchmark-conditioned exponents. On Qwen2.5-7B, BOPTR gives the lowest transfer error among the non-oracle rules we test, 3.41 pp (95% CI [2.32, 5.53]); a three-seed replication gives 3.07 $\pm$ 0.39 pp. The rule extends to ten models across four families (3.28 to 4.87 pp on checkpoints added after fitting), to four benchmarks it was never fitted on (5.03 pp vs. 4.44 pp in fit), and holds without an RL checkpoint for the target model (4.19 pp) or without RL supervision of any kind (5.08 pp). These results support a qualified internalized-search reading: under the recipe we test, much of the measured RL gain corresponds to a change in sampling efficiency toward operating points the base model can already reach under search. We treat the scaling patterns as descriptive of this recipe and cohort, report where they break down, and use UDF and BOPTR as behavioral diagnostics rather than evidence of parameter-level equivalence.

---


### 233. [The Constitutional Coverage Trilemma in AI Governance](https://arxiv.org/abs/2609.01275)

**<font color=#1a73e8>作者：</font>** Natalija Mitic, Soona Sedahmed A. O., Mamadou Selly Ly 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Frontier AI systems function as \emph{constitutional institutions}: each deployed model encodes an implicit ranking among safety, helpfulness, honesty, autonomy, and equity. We ask whether the supply of frontier constitutional types covers human demand. Combining a paraphrase-controlled audit of the as-shipped default constitutions of $23$ frontier LLM archetypes with a pairwise-tradeoff study of $1{,}649$ US participants on the same instrument, we report three facts. \emph{Demand is broad}: it spans all five values, with the largest constituency under one-third. \emph{Supply is narrow and drifting}: the $23$-archetype hull occupies ${\sim}2\%$ of the demand hull under conservative noise-matched estimation ($0.10\%$ at full audit precision), no archetype puts helpfulness or autonomy first ($37\%$ of users are constitutionally homeless), and across six model families autonomy decreases in $5/6$, equity increases in $5/6$, and safety increases in $4/6$, with monotone within-family version trends (order-permutation $p = 0.013$) and the autonomy decline concentrated in scenarios where safety is not at stake. The drift's importance is directional: \emph{away} from a value already undercovered, mechanically worsening the welfare floor for the least-served users. \emph{The fix is sparse}: a $2$-vertex menu $\{e_{\mathrm{HON}}, e_{\mathrm{AUT}}\}$ beats the full $23$-archetype frontier by $47\%$ on mean regret (CI $[43\%, 52\%]$); three vertex additions cut mean/worst-group regret by up to $81\%$/$64\%$. We formalize these findings as a budgeted-pluralism trilemma, show the binding regime is empirically realized, and verify the conclusions are robust to distance-based welfare and to degraded routing. The instrument and audit harness are described in full in the appendices.

---


### 234. [Some Emotions Run Deeper: Layer-wise Probing and Causal Intervention in Large Language Models](https://arxiv.org/abs/2609.01279)

**<font color=#1a73e8>作者：</font>** Tian Fang, Gaël Guibon, Davide Buscaldi  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Emotion is expressed in text along a wide spectrum, from surface lexical cues to inferences entangled with content. Most layer-wise analyses of emotion in LLMs use a single corpus, leaving open whether the depth at which emotion becomes accessible is a property of the model or also of the text source. We investigate this across three datasets spanning different degrees of explicitness and contextualization in emotion expression (Twitter posts, Reddit comments, and autobiographical narratives) and eight 1B--9B open-weight LLMs from the Llama, Qwen, and Granite families. We combine layer-wise probing with offline feature scaling and online forward interventions, transfer analyses, and an early-exit classifier. We find that (i) the best probing layer shifts systematically across corpora, from input-adjacent layers to over half model depth, and this ordering persists after matching label-by-length-bin distributions; (ii) across the evaluated settings, forward-pass interventions on probe-selected bands reduce test accuracy by 5--6 points more than same-width random bands ($q < 0.01$); (iii) selected bands transfer across datasets and emotion categories, suggesting partially shared affective information rather than strictly per-emotion substrates; and (iv) probe-selected early-exit representations outperform full-depth exits by $6.9$ percentage points on average.

---


### 235. [Analog-DB: An Agent-First Analog Integrated Circuit Database, From Blocks to Systems](https://arxiv.org/abs/2609.01286)

**<font color=#1a73e8>作者：</font>** Danial Noori Zadeh, Mohamed B. Elamien  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sharing analog integrated circuit designs remains difficult: foundry non-disclosure agreements restrict the process details a design depends on, and the testbenches behind published results are rarely released. We present analog-db, an open-source, versioned database built on a shareable design representation. A domain-specific language captures each design as a process-neutral topology, reusable testbenches, and a machine-readable datasheet under one schema, so a design is shared in full and re-simulates on the process kits it is bound to. A parameterization scheme exposes functional sub-blocks and device sizes as named parameters that carry their matching constraints, making circuits composable and retargetable; a schema-governed contract and queryable catalog let AI design agents discover and reuse them directly. Across the regulator corpus, all 23 circuit-kit bindings on three open kits meet their own recorded specification bands (typical corner, matched devices, no layout) and 10 of 23 meet a common class band. Seventeen of the 23 imported sizings failed their testbenches and closed under a gm/ID sizing loop driven by the annotated sub-block roles, typically within one to three iterations. In a supervised case study, a coding agent working from the released artifacts sized the op-amp cores of a chopper instrumentation amplifier on an open 130nm kit, locating four hand-entry defects and a missing common-mode feedback loop that the sizing-only baseline did not repair. The database holds 68 circuits across sixteen classes, verifiable at schematic level under a tiered harness and tracked on a power/performance scoreboard, released at this https URL.

---


### 236. [Agentic Multimodal Models for Environmental Hyperspectral Unmixing](https://arxiv.org/abs/2609.01289)

**<font color=#1a73e8>作者：</font>** Michał Cholewa, Luca Ciampi, Nicola Messina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Hyperspectral unmixing is a key task in remote sensing that aims to decompose mixed pixels in hyperspectral images into their constituent material signatures, or endmembers, and their fractional abundances. Conventional modular approaches estimate the scene composition through successive model-order estimation, endmember extraction, and abundance estimation stages, whose errors can lead to redundant or ambiguous candidate components and ultimately affect the recovered decomposition. We introduce an algorithm-agnostic, large vision-language model (LVLM)-driven agentic framework that refines the outputs of such pipelines rather than replacing their underlying numerical algorithms. Starting from an initial decomposition, the agent iteratively gathers complementary spectral and spatial evidence through dedicated tools, including spectral-library retrieval and abundance-map visualization, and modifies the active endmember set through merge and discard operations followed by abundance re-estimation. We apply the same refinement procedure to several modular pipelines combining different model-order, extraction, and abundance-estimation methods, and evaluate it on HYDICE Urban, Jasper Ridge, and Stonewall Playa. Experiments show that the proposed agent consistently improves endmember cardinality and generally improves the recovered spectral signatures and abundance maps across heterogeneous modular pipelines, while remaining competitive with integrated end-to-end unmixing methods, including CNN-AE, uDAS, and R-CoNMF. These results highlight the potential of tool-using LVLM agents to combine spectral and spatial evidence for algorithm-agnostic refinement of physically grounded hyperspectral unmixing decompositions. Code is publicly available at this https URL.

---


### 237. [Explore Before Committing: Hypothesis-Guided Search for Deep Research Agents](https://arxiv.org/abs/2609.01294)

**<font color=#1a73e8>作者：</font>** Ruochen Zhou, Zhengyu Chen, Luan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Deep-research agents answer complex questions by interacting with search and browsing tools, yet they often search along a single evolving trajectory. Our trajectory-level analysis reveals a common failure mode in which the agent may encounter an early search state with several plausible directions, but follow one direction before collecting enough comparative evidence. Once this happens, subsequent tool calls tend to reinforce the same path, increasing the chance of failure when the initial direction is misleading. We further find that successful trajectories reduce this risk through two behaviors: grounding vague exploration in concrete candidates and shifting directions when the current path is weak or incomplete. Based on these findings, we propose HypoSearch, which generates lightweight hypotheses as soft search hints, explores them through bounded independent branches, and compares branch-level evidence before commitment. Across four deep-research benchmarks and three backbone models, HypoSearch consistently outperforms single-trajectory search and standard parallel baselines, improving Qwen3.5-122B from 46.7 to 60.0 on BC-small while using fewer tool calls than five independent trajectories. A pilot supervised fine-tuning study further shows that these behavioral signals can curate compact training trajectories and reduce degradation from unfiltered data.

---


### 238. [A Composable Evaluation System for Reproducible Omni-Modal Foundation Model Evaluation](https://arxiv.org/abs/2609.01315)

**<font color=#1a73e8>作者：</font>** Hodong Lee, Sanghee Park, Dohoon Ryu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Building an omni-modal foundation model means evaluating it across text, image, video, and audio. Excellent evaluation toolkits exist for each modality, but their inference engines, prompt conventions, and metric implementations are mutually incompatible, so practitioners end up maintaining separate environments for every toolchain and still struggle to compare results across them. OmniEvaluator grew out of this need in our own model development: rather than reimplementing benchmarks, it connects existing inference engines and curated evaluation libraries at a higher level, exposing four inference backends, four evaluation frameworks, and over a thousand benchmarks through a single interface. Every run is recorded as an artifact capturing the full configuration for exact reproduction, and results flow into a shared dashboard for cross-model comparison. A federated mode shares GPU inference servers across concurrent evaluations, and a built-in verifier, small enough to run on CPU, keeps its score stable across engines and prompts where rule-based scoring fluctuates under configuration mismatch, matching cost-efficient commercial LLM judges without their recurring API cost. The system, demo video, and dashboard are publicly available. (this https URL)

---


### 239. [Reliability Challenges in Diffusion Vision-Language Models](https://arxiv.org/abs/2609.01318)

**<font color=#1a73e8>作者：</font>** Md. Atabuzzaman, Chris Thomas  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Diffusion-based Large Vision-Language Models (dLVLMs) have recently emerged as a compelling alternative to autoregressive (AR) LVLMs, offering advantages in parallel decoding, bidirectional context, and controllable generation. Despite rapid progress, their reliability properties remain largely uncharacterized. We present the first systematic reliability evaluation of hallucination and bias in dLVLMs, benchmarking six diffusion models against competitive AR baselines across four dimensions. Our key findings are: (1) dLVLMs reverse the yes-bias of AR models in binary visual queries; (2) they achieve competitive hallucination rates yet exhibit degraded linguistic quality; (3) they collapse to near-zero accuracy on underrepresented racial groups with opposite-polarity gender bias; and (4) they exhibit accuracy collapse in multiple-choice settings when the correct option is shorter than its distractors, associated with a length prior that emerges at the first denoising step. Tokens committed at late denoising steps with low confidence further correlate with hallucinated content, pointing to a mechanistic signal unique to diffusion generation. These patterns vary across model families, suggesting reliability is shaped by the generative paradigm together with training data.

---


### 240. [Automated Event Log Generation from Unstructured Text Using Finetuned LLMs](https://arxiv.org/abs/2609.01320)

**<font color=#1a73e8>作者：</font>** Maximilian Seeth, Gabriel Marques Tavares, Daniel Schuster  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Process mining (PM) provides a powerful framework for discovering and optimizing operational processes from event data. However, the efficacy of PM techniques is strictly predicated on the availability of structured event logs. Thus far, event logs have often been laboriously created by domain and process mining experts. This costly effort causes large portions of organizational knowledge, including incident tickets, manuals, and textual reports, to remain underutilized. We address this bottleneck by investigating the efficacy of Large Language Models (LLMs) as automated data translators. We propose a scalable framework that leverages LLMs as data translators to bridge the gap between unstructured textual resources and structured event data. We finetune LLMs on a newly created text-to-log dataset, demonstrating that the resulting models can extract high-fidelity event logs from unstructured resources. Our results show that this finetuning approach outperforms few-shot or zero-shot prompting by a large amount, highlighting finetuning as a necessary pre-condition for generating reliable event data. We conclude that our method provides a promising pipeline for making previously unused data available to process mining ecosystems, effectively expanding the possibilities of using PM to further investigate organizational workflows.

---


### 241. [Bandits in Prod: Hyperparameter Optimization at Inference Time](https://arxiv.org/abs/2609.01335)

**<font color=#1a73e8>作者：</font>** Louis Abraham, Tuan-Anh Nguyen, Nicolas Devatine  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Many production systems can assess a configuration only by using it on live requests and observing noisy feedback. Modern agentic systems are a prominent example, with inference-time choices such as model selection, retrieval depth, prompting strategy, and decoding temperature, yet often with no representative validation data. We formalize this setting as Online Hyperparameter Optimization (OHPO) and cast it as an infinitely many-armed bandit over mixed and conditional search spaces. We introduce IMABO, a general framework that combines any bandit policy for choosing among already sampled configurations with any oracle for proposing new ones. We instantiate it with IMOSS, a restart-free anytime policy whose active set grows as $t^{\beta}$, and prove an expected cumulative quantile-regret bound of $O(p_\rho^{-1/\beta} + T^{(1+\beta)/2})$, where $\beta\in(0,1)$ controls active-set growth and $p_\rho$ lower-bounds the probability that a proposed configuration falls in the top-$\rho$ fraction of the search space. We combine IMOSS with three practical oracles: a Tree-structured Parzen Estimator, an incumbent-mutation oracle driven by a per-coordinate bandit, and a pretrained tabular foundation model, all three improving over the uniform random oracle baseline. IMABO obtains the lowest cumulative regret across diverse OHPO settings, from tuning classical machine-learning models to configuring LLM-based agents.

---


### 242. [LEAP: Likelihood Elicitation and Aggregation for LLM-based Probabilistic Forecasting](https://arxiv.org/abs/2609.01337)

**<font color=#1a73e8>作者：</font>** Yufei Chen, Yiran Zhao, Xiaogang Xu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-based forecasting systems have improved on real-world tasks such as financial markets and sports outcomes, largely through stronger search and tool use. Many systems still ask an LLM to read all collected evidence together and produce the final forecast. We call this design Monolithic Prediction. It can obscure how individual evidence items affect the result and collapse uncertainty across competing outcomes. We propose LEAP (Likelihood Elicitation and Aggregation for Probabilistic forecasting), which reorganizes how collected evidence is used in the prediction stage. LEAP examines each evidence item separately and elicits likelihood parameters that describe its implications for the target. An explicit prior and a deterministic probabilistic model then combine these likelihoods into a posterior distribution. This procedure supports continuous, single-choice, and multi-choice forecasts while preserving reproducible evidence contributions. We build a benchmark covering forecasting, information-seeking, and browsing tasks, and evaluate LEAP on our own agent loop and several agent CLI frameworks. Given the same evidence, LEAP improves most prediction and calibration metrics across models and remains stronger under controlled comparisons of prior access, inference budget, and aggregation.

---


### 243. [Probing Factual Knowledge Transfer with Training Data Interventions](https://arxiv.org/abs/2609.01341)

**<font color=#1a73e8>作者：</font>** Romina Oji, Marc Braun, Marcel Bollmann 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Do multilingual language models transfer factual knowledge across languages during continued pretraining, or do they mostly recall facts learned directly from the target-language data? To answer this question more reliably, we propose an intervention-based framework: starting from an English-pretrained model, we continue pretraining on Persian data from which specific facts have been systematically removed at varying levels of granularity. We construct SIFT, a resource of 500 triples across 20 relations, stratified by the cultural origin of each fact's subject into general (globally prominent) and Persian-related entities, designed for both systematic fact removal from training data and evaluation, with natively written Persian cloze templates. Our results show that fact transfer is very limited: under the strictest removal condition, a large majority of English-acquired facts fail to transfer into Persian. We further show that sentence-level co-occurrence removal is insufficient to eliminate fact signal, and that easier (randomly selected) negative candidate sets substantially inflate apparent transfer by rewarding shallow associative heuristics, while performance on a harder candidate set that allows for less reliance on heuristics is much lower. Finally, we show that source-language entity frequency has a large influence, with Persian-related facts, which are orders of magnitude rarer in the English corpus, hardly transferring.

---


### 244. [SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers](https://arxiv.org/abs/2609.01343)

**<font color=#1a73e8>作者：</font>** Shaowen Wang, Ge Zhang, Kairong Luo 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Looped Transformers increase effective depth by iterating a shared block of layers, but most evaluations compare at fixed model size, conflating architectural advantage with extra FLOPs. We study looping on Mixture-of-Experts Transformers while closely matching per-token FLOPs, total non-embedding parameters, and KV cache. Through a series of ablations, we arrive at a recipe we call SMELT (Sparse MoE Transformer, middle layers Loop Twice), which loops the middle half of layers twice while matching the unlooped Baseline on all three budgets. We scale SMELT across four sizes up to 54B non-embedding parameters and fit a separate Chinchilla-style scaling law for each architecture. SMELT's loss drops faster with compute, saving 6.8--18.0\% of training FLOPs on the compute-optimal frontier. The advantage transfers to downstream benchmarks beyond what validation loss predicts, is largest on Code, and grows with sample length and the number of in-context examples. Mechanistic analysis shows that the second visit reduces the attention sink and redirects mass toward content-relevant tokens, an inductive bias that may underlie the observed performance gains. These results show that looping can improve Transformers even under budget matching, offering a practical recipe that turns depth reuse into measurable gains.

---


### 245. [ExBind: A Controlled Diagnostic Benchmark for Visual-to-Executable Correspondence](https://arxiv.org/abs/2609.01344)

**<font color=#1a73e8>作者：</font>** Ziqian Wang, Yuxiao Cheng, Tingxiong Xiao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal coding and editing systems must map a visible or semantic referent to the exact executable object that can be edited. A wrong reference may select a valid but incorrect DOM node, SVG element, graph endpoint, hierarchy member, or table cell, while final execution success alone does not reveal the source of the failure. ExBind isolates this visual-to-executable correspondence layer as a controlled diagnostic benchmark between semantic localization and action execution. It samples representation-independent latent binding instances and compiles them into SVG, DOM, canvas, tree, graph, and table cases with deterministic mappings to executable references. Models output only a strict reference; the evaluator maps predictions back to latent structure and scores structural constraints without requiring reasoning traces. The release contains a 250-case broad suite, a disjoint 240-case targeted suite, and 50 paired latent groups. Qwen2.5-VL-3B achieves 98.4% candidate validity but 76.4% exact accuracy, while Qwen3-VL-4B achieves 100.0% validity and 98.8% exact accuracy. In the targeted table suite, all Qwen2.5-VL-3B residual errors are valid correct-row/wrong-column selections. Candidate-order perturbations change case-level outcomes while preserving this error pattern. ExBind is designed for controlled diagnosis rather than population-scale ranking or end-to-end editing evaluation. Code and benchmark records are available at this https URL and this https URL.

---


### 246. [Cheap Verifiers, Large Blind Spots: Measuring the Reliability Cost of Cost-Saving Cascades](https://arxiv.org/abs/2609.01345)

**<font color=#1a73e8>作者：</font>** Dushyant Rajput  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference cascades cut cost by answering most queries with a cheap model and escalating a hard tail to a frontier model that acts as verifier. A natural extension closes the loop: fine-tune the cheap student on the verifier's rejections so the escalation rate, and cost, fall each round. We measure this loop on real LLMs and report four findings. First, the verifier's blind spot, the fraction of the student's wrong answers it accepts, is large and moves adversarially: it grows with student capability ($\beta$ from 0.12 to 0.55 as the student scales 0.5B to 32B) and shrinks with verifier capability, so it is worst in the cheap-student, cheap-verifier regime cascades exist to create. Second, buying it away returns the saving: a frontier verifier drives $\beta$ to about 0.05 but then escalates on 46% of hard-MATH queries against a 39% true error rate, paying the frontier price on nearly half of all traffic. Third, naive corrective fine-tuning on the verifier-rejected tail does not improve the small student but degrades and ultimately collapses it, across every teacher we tried (cross-family and same-family), so at this scale the self-improving loop is self-defeating. Fourth, through all of this the cascade's own dashboard, every metric computed through the verifier, reads a flat 3% error while true delivered error swings up to 32%: the system is blind to its own degradation by construction. We then give the theory that explains the blindness, a two-population conservation law, $\epsilon_\infty \lesssim q_0 \beta_0$, under which every in-loop metric improves while true quality does not, and a synthetic study that validates the mechanism. The practical conclusion: the reliability of a self-improving cascade cannot be read from any metric computed through its own verifier.

---


### 247. [CHARM: Character Hallucination for Multicultural Role Play Benchmark](https://arxiv.org/abs/2609.01352)

**<font color=#1a73e8>作者：</font>** Sunkyung Han, Nahyeon Park, Gaeun Seo 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Role-playing large language models (LLMs) are expected to adopt a character's style while also respecting that character's knowledge boundaries. Prior evaluations detect character hallucination but rarely distinguish whether errors arise from failure to recognize a boundary or from failure to comply despite recognition. We introduce CHARM, a multicultural benchmark of 40 real and fictional characters drawn from five cultural-linguistic regions, and validated by native reviewers. It probes two boundary types, Temporal (historical vs. modern) and Cross-Universe (entities outside a character's narrative or historical universe), using abstention-enabled multiple-choice questions. We propose a two-stage evaluation that separates Boundary-Awareness (explicit recognition that a query is out of scope) from Boundary-Compliance (abstention when answering concrete questions). Evaluations across six LLMs show that hallucination is driven predominantly by compliance failures. Models frequently acknowledge that a query lies outside the character's knowledge yet still provide factual, out-of-character answers. By re-posing the same questions to the target character, we confirm that a large fraction of these cases are verified parametric overrides; the model stores the relevant fact but fails to suppress it. We also observe systematic cultural variation in these failures, consistent with imbalances in how characters from different regions are represented in model knowledge.

---


### 248. [SymFold: Synergizing Evolutionary and Structural Priors for Accurate Protein Inverse Folding](https://arxiv.org/abs/2609.01353)

**<font color=#1a73e8>作者：</font>** Handong Wang, Jiaxin Qi, Baisheng Lai 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Protein inverse folding aims to recover amino acid sequences for a given 3D protein structure, underpinning broad applications such as enzyme engineering and drug this http URL methods often follow a serial pipeline, in which a structure encoder predicts a coarse sequence, which is then refined by protein language models (PLMs). However, because PLMs only perform post-hoc sequence edits, the refinement is bounded by the quality of upstream this http URL to recent multimodal protein language models (MPLMs), we could directly encode structure to generate sequences with pretrained structural knowledge, but we observe that they are not effective for inverse folding. Therefore, we introduce a symmetric dual-path architecture that both leverages PLMs for pretrained sequence evolution knowledge and MPLMs for pretrained structural knowledge to iteratively guide protein sequence this http URL extensive experiments across standard protein inverse folding benchmarks, our method achieves state-of-the-art performance, surpassing prior approaches, and ablation studies validate the rationale of our symmetric design, revealing a promising direction for the community.

---


### 249. [Separating Syntax from Language: A Mechanistic Account of Translation in Multilingual LLMs](https://arxiv.org/abs/2609.01356)

**<font color=#1a73e8>作者：</font>** Mikhail Sonkin, Tanja Baeumel, Daniil Gurgurov 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual large language models (mLLMs) achieve strong performance in machine translation, yet our understanding of the mechanisms by which they transform representations from one language to another remains incomplete. Prior work suggests that translation decomposes into separable processes within an mLLM, where conceptual content is first represented independently, followed by a production into language-specific form. In this work, we show that translation is even more modular than previously assumed and that the output language production in translation processes is actually further separable into a syntax and a surface language process. We construct controlled multilingual datasets that isolate cross-linguistic differences in word-order and use causal interventions and probing to track how representations are transformed during translation. We find that models first construct target-side word-order before realizing the target language surface form. We identify individual attention heads that are selectively sensitive to syntactic transformations while remaining largely invariant to language identity. These results establish the commitment to a syntactic structure as an independent stage in translation, extending prior decompositions and showing how translation is implemented by functionally different components within mLLMs.

---


### 250. [EDGE: Error Dependency Graph-Guided Multi-Error Attribution in Multi-Agent LLM Systems](https://arxiv.org/abs/2609.01360)

**<font color=#1a73e8>作者：</font>** Jun Hou, Priya Pitre, Yi Fang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agent failures often contain multiple related errors rather than a single mistake. Existing attribution methods usually identify a responsible agent, step, or root cause, but do not explicitly model dependency between errors. We introduce EDGE, an Error Dependency Graph-guided multi-Error attribution framework. EDGE constructs an error dependency graph from observed error events and validates a reliable causal subset through counterfactual rollout. The inference graph guides a two-stage LLM-as-judge detector for error attribution, and the intervention-validated subgraph provides a more reliable basis for explanation and repair analysis. Experiments on TRAIL and MAST show that EDGE improves category-level multi-error attribution across most evaluated models and settings. Experiments with adapted Who&When-style prompts show that the graph helps across prompting strategies. These results suggest that dependency structure is a useful diagnostic prior for agent failures beyond isolated root-cause prediction.

---


> [!TIP]
> 当前位于：**201-250**（第 5/6 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-295](./part-06.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
