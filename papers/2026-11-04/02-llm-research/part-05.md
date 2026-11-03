# 🧠 大模型相关研究 | 2026年11月04日

> 本类共 **515** 篇论文：已确认 **481** 篇，待复核 **34** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

---

### 201. [\textsc{ChatDify}: Automating End-to-End Dify Workflow Synthesis from Natural Language via Multi-Agent Collaboration](https://arxiv.org/abs/2611.01563)

**<font color=#1a73e8>作者：</font>** Tao Fan, Guoqiang Ma  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The proliferation of Large Language Models has catalyzed powerful application development platforms like Dify, which enable users to build sophisticated LLM-powered workflows through modular node orchestration. However, manually configuring these workflows requires deep platform expertise and remains time-consuming and error-prone, creating a significant barrier for non-expert users. To address this challenge, we propose \textsc{ChatDify}, a novel multi-agent framework that automates end-to-end Dify workflow synthesis from natural language descriptions. \textsc{ChatDify} employs an Actor-Critic architecture comprising three specialized agents: the \textit{Planner Agent} that decomposes user requests into structured execution plans, the \textit{Executor Agent} that performs context-aware parameter synthesis and schema-augmented DSL compilation, and the \textit{Reviewer Agent} that ensures reliability through hybrid verification with closed-loop refinement. We evaluate \textsc{ChatDify} on a curated benchmark of 100 production-inspired tasks across three state-of-the-art LLM backends, achieving 0.96, 0.91, and 0.75 success rates with Qwen-3.7, GLM-5.1, and DeepSeek-v4, respectively. These results demonstrate its robustness and practical applicability for lowering the technical barrier to creating sophisticated LLM applications.

---


### 202. [StateGate: A Behavioral-Fidelity Prompt Optimization Method for Long-Chain LLM Agents](https://arxiv.org/abs/2611.01585)

**<font color=#1a73e8>作者：</font>** Shicheng Huang, Cai Fu, Jianqiang Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Currently, long-chain LLM agents commonly suffer from behavioral degradation in complex tasks, where prompts are written in full but steps are not executed in full. To address this issue, existing approaches face three major challenges. First, constraints are strongly bound to their textual carriers; once natural-language constraint sentences are removed, their binding force vanishes. Second, the execution process lacks independent verification, as the evidence for judgment is often supplied by the executing party itself, leading to the failure of self-referential validation. Third, existing remediation schemes are difficult to generalize, and hard-coded mechanisms cannot be transferred across tasks. In this paper, we propose StateGate, a novel prompt-optimization scheme that transforms semantic constraints into symbolic gates enforced by an external deterministic runtime. By decoupling the content of a constraint from its carrier of efficacy, StateGate achieves behavioral fidelity in long-chain tasks without losing the binding force of the prompt. Specifically, we first propose four independent compression strategies (deduplication, generalization, externalization, and text-to-gating) together with their corresponding decision chains, enabling principled prompt symbolization. Second, we design a three-component architecture consisting of a state file, a validator, and an orchestrator, which thoroughly separates judgment authority from execution authority. Third, we formally prove that the compliance of symbolic constraints is independent of context size. Finally, we validate the framework on a vulnerability-discovery task in the security domain; the results show that StateGate achieves 100% execution closure and accurate vulnerability detection.

---


### 203. [LLM-Enhanced Multimodal House Price Prediction using Structured, Textual, and Visual Features](https://arxiv.org/abs/2611.01615)

**<font color=#1a73e8>作者：</font>** Khandokar Md. Rahat Hossain, Souvik Das, Tahsina Hashem 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate house price prediction is essential for real estate buyers, sellers, agents, and financial institutions. Traditional methods rely primarily on structured data, e.g., number of bedrooms, bathrooms, parkings, but they overlook rich contextual information embedded in textual descriptions and property photos. Previous deep learning approaches for house price prediction have fused multimodal data but they fall short to extract structured spatio-temporal and contextual features from texts and semantic visual information from images. In this paper, we introduce a novel multimodal framework that addresses these limitations by systematically integrating structured attributes, textual descriptions, and visual images of properties to achieve higher prediction accuracy while maintaining interpretability. We use a large language model to derive domain-specific spatio-temporal and contextual features from text, and an unsupervised vision-language approach to automatically group photos into meaningful classes like indoor, outdoor, mixed, or floorplan, that are commonly present in real-world house listings. These categories are created without manual labeling by aligning image clusters with carefully designed pseudo text prompts. We fuse all features into a unified representation and use an optimized regressor to predict prices. Experiments on a large real-world property dataset demonstrate that our method outperforms traditional methods and existing multimodal baselines. Ablation studies confirm that the novel textual feature extraction and categorized visual embeddings substantially contribute to more accurate and reliable price predictions.

---


### 204. [Seeing What Matters, Verifying What Pays: Load-Adaptive Speculative Decoding for Vision-Language Models](https://arxiv.org/abs/2611.01617)

**<font color=#1a73e8>作者：</font>** Hong Nie, Zhangchi Gao, Yuqian Liang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Speculative decoding accelerates vision-language model (VLM) inference without altering the output distribution, yet two factors limit its gains. Existing drafters either lack the image evidence required for visually grounded tokens or pay to condition on every visual token, although a short draft block typically depends on only a few image regions. Moreover, the value of verifying additional candidates varies with GPU load, so no fixed verification structure is efficient across serving conditions. We present Uni-LaSpec, a block-parallel speculative decoding framework that addresses both factors. To improve draft quality, Uni-LaSpec reuses the verifier's own attention: the query retained from the preceding verification ranks the cached, int8-quantized visual keys, and a cross-layer vote selects a few visual tokens that the drafter fuses through gated cross-attention. Acceptance-aware training further weights each draft position by its contribution to the accepted prefix. To allocate verification, a marginal-cost criterion selects the structure per request and per round: draft trees exploit idle verifier capacity under light load, whereas a dynamic head truncates linear drafts under heavy load. Across six VLMs from three model families and 17 text and multimodal benchmarks, selecting eight visual tokens retains at least 98.6% of the acceptance obtained from the full image at sub-millisecond selection cost. With greedy decoding at concurrency one, Uni-LaSpec achieves up to 5.11x text and 3.24x multimodal throughput over autoregressive decoding. Across six load levels and three GPU types, it outperforms autoregressive decoding in every setting and matches or exceeds the best fixed verification strategy in 123 of 144 settings; under bursty arrivals, it reduces mean end-to-end latency by 47.6% relative to linear verification.

---


### 205. [Chain-of-Thought Oversight Requires Separate Evidence for Faithfulness and Monitorability](https://arxiv.org/abs/2611.01620)

**<font color=#1a73e8>作者：</font>** Sichao Li, Sai Ma, Xiyang Hu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A common assumption in chain-of-thought (CoT) oversight is that a visible reasoning trace makes model behavior easier to monitor. We argue that this assumption can conflate distinct properties along a chain linking a model's internal computation, reasoning artifacts, outputs, and monitor judgments. We identify four properties along this chain: reasoning visibility (whether a trace is accessible), mechanistic faithfulness (whether a trace reflects internal computation), mechanistic localizability (whether a compact causal mechanism can be isolated), and behavioral monitorability (whether a monitor can detect the target behavior). Two complementary case studies across three open-weight reasoning models show why these distinctions matter. In the security vulnerability reasoning study, probes and activation ablations provide evidence of internal representation and causal influence, but a monitor with access to the reference answer does not outperform the majority-class baseline in a held-out test. In authority-hint factual reasoning study, a monitor correctly distinguishes changed from unchanged answers, but seven mechanistic analyses do not isolate a compact causal mechanism. These results show that evidence for one claim does not establish the others. We therefore propose an evidential-chain reporting standard. Each claim carries a licensing statement that specifies its target property, access tier, and artifact, and labels each required link as supported, unsupported, or assumed. These assessments determine whether the conclusion is licensed, conditionally licensed, or not licensed.

---


### 206. [Zero-shot evaluation of open vision-language models as System 1 decision models on radiology tasks](https://arxiv.org/abs/2611.01631)

**<font color=#1a73e8>作者：</font>** Bradley J Erickson, Sara Salehi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Purpose: We compared two multimodal System 1 decision models, Clef 27B and d1 3B, with a traditional LLM (Qwen 3.8-27B) on seven radiology tasks covering text, radiographs, CT and MRI. Methods: Three models were compared: Clef, Qwen3.8-27B and d1. Three tasks were interpretation of text and 4 were detection of finding in images. The tasks were: 1. finding presence of finding in CT-RATE chest CT reports; 2. Presence of finding in PadChest chest radiograph reports; 3. the same 18 findings on CT-RATE chest CT but 3D volumes; 4. MR safety status of devices from AccessGUDID device records; 5. line and tube position on RANZCR CLiP chest radiographs; 6. motion-artifact severity on MR-ART T1-weighted brain MRI and 7. sequence identification on BraTS 2021 brain MRI. The primary endpoint was AUROC. There was no fine-tuning of the models on the tasks. Results: All models completed all tests without a failed request. All retrieved findings from reports almost perfectly (AUROC >0.95). Clef ranked higher than its Qwen backbone on CT-RATE volumes and RANZCR lower on MR-ART. The two did not differ on BraTS, GUDID or PadChest, and differed by 0.002 on CT-RATE reports. On BraTS, Clef correctly identified 90 of 100 FLAIR volumes while Qwen never chose it. d1 ranked lower than Clef on six of seven tasks. No model performed well on motion severity. Clef was faster per request than Qwen on tasks with many questions per input. d1 used 3 to 9 times less energy per request than Clef. Conclusions: System 1 models can perform important tasks in radiology with high accuracy, at lower compute cost than LLMs used in the usual way. When an LLM is constrained to a single answer token, its cost and performance is similar to System 1 models unless multiple questions are asked. A 3B System 1 model was close to the 27B models on report text but not on images. No model performed well on motion severity.

---


### 207. [BanglishDepYT: Depression Detection in Native Bengali Social Media with Emotion-Preserving Preprocessing and Domain-Adaptive Pretraining](https://arxiv.org/abs/2611.01633)

**<font color=#1a73e8>作者：</font>** Ayon Roy, Sadman Sharif, Syed Shams Islam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Depression affects millions of Bengali speakers across South Asia, yet automated detection systems have relied almost entirely on datasets translated from English. Such datasets cannot capture the emoticons, romanized Bengali words, and elongated spellings that characterize real expressions of distress. We introduce BanglishDepYT, a Bengali depression dataset collected natively from YouTube, comprising 191,000 unlabeled comments and 1,000 samples verified through dual bilingual annotation. We propose EPH (Emotion-Preserving Hybrid preprocessing), which converts emoticons to semantic tags, preserves Banglish tokens, protects negation words, and normalizes emotional elongation. A key finding is that preprocessing choice substantially affects performance on informal text: standard cleaning reduces the Banglish Survival Rate to zero (SVM F1: 0.7062), while EPH preserves signals (CESS: 0.9996 vs. 0.6694) and raises SVM F1 to 0.8570, an improvement of 0.1508. We further apply domain-adaptive pretraining (DAPT), continuing SahajBERT pretraining on unlabeled in-domain comments. DAPT-SahajBERT achieves the highest mean F1 (0.8161) and MCC (0.6272), significantly outperforming the baseline (F1: 0.7805, p = 0.0013, d = 1.450) and matching MuRIL (p = 0.589). These results suggest that targeted domain pretraining is a competitive alternative to large-scale multilingual pretraining. LLM-assisted annotation using Qwen2.5-7B achieves substantial human agreement (kappa = 0.611), enabling pseudo-labeling of 96,071 comments. Semi-supervised training improves AUC from 0.8499 to 0.8731 (p = 0.044), offering a scalable path to expanding annotation. All code, models, and datasets are publicly released to support reproducible research.

---


### 208. [Benchmarking Vision-Language Models for Urdu Nastaliq Handwriting Recognition](https://arxiv.org/abs/2611.01635)

**<font color=#1a73e8>作者：</font>** Haseeb Yaqoob, Fatima Azfar, Emaan Arif Khan  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Handwritten Urdu is hard to recognize because the cursive Nastaliq script has no fixed baseline and no clear character boundaries. We benchmark six systems on the Urdu Nastaliq Handwritten Dataset (UNHD): Tesseract (default configuration), a script-specific recognizer trained on printed Urdu (UTRNet-Large), two open-source vision-language models (VLMs), and two commercial VLMs. All six systems are evaluated without fine-tuning on 2,465 single-line images (Part A), and the four VLMs receive the same fixed prompt (decoding uses temperature 0 where configurable, except for Claude Sonnet 5, whose decoding cannot be configured). Both commercial VLMs reach lower error than the printed-Urdu recognizer and the open-source VLMs. We do not compare against handwriting-trained recognizers, which would likely do better in-domain; we characterize zero-shot behavior, not state of the art. We also describe three distinct failure modes among the ranked systems. In one of them, a commercial model explicitly declines to transcribe a few very hard-to-read images instead of guessing. In a second study (Part B), VLMs correct the output of a separate OCR system using both the source image and the noisy text. Once separated from each model's own reading ability, the benefit is small on Tesseract's output (0.7% to 7.4%) and larger (17.9% and 21.9%) only for the two commercial correctors given UTRNet's text. It appears to depend on how legible the supplied text already is, and a weaker corrector can make a more legible text worse.

---


### 209. [Local or Escalate? Post-Training Expert Routing for Real-Time Duplex Speech Models](https://arxiv.org/abs/2611.01639)

**<font color=#1a73e8>作者：</font>** Ruoyu He, Jisen Li, Anthony Ji 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A full-duplex model should answer easy questions immediately, but hard questions often need stronger reasoning, which may require waiting. The challenge is to choose between these paths at the moment the model begins to speak. Recent systems learn related mode decisions through special-token generation inside the dialogue model, coupling routing to turn-taking and temporally annotated full-duplex training. We study a post-training alternative. We freeze MiniCPM-o 4.5, using only its speech input and output, and fit a logistic failure readout on hidden states already available at its native listen-to-speak transition. The resulting gate requires no additional model generation and exposes thresholds that can be retuned without changing the duplex policy. A probe fitted on text-input states also reads the states of spoken questions, including unseen human recordings. On the internal benchmark, selective handoff improves answer accuracy by 27.1 points. Compared with always using the expert, it reduces mean server time to first answer audio by 31.5 percent. It also outperforms matched random routing across external speech question-answering pools, as well as a zero-shot GPT-5.4 mini router that rates the transcribed question. The training recipe also transfers to a second duplex model family. These results show that an existing duplex model can be equipped to answer easy turns immediately and wait for stronger reasoning or fresher knowledge on the turns that need it, without further duplex training.

---


### 210. [CREDO: Evidence-Conditioned Credit Assignment for Temporal Reasoning Agents](https://arxiv.org/abs/2611.01643)

**<font color=#1a73e8>作者：</font>** Yue Leng, Shengtao Wen, Xiang Chen 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Temporal Knowledge Graph Question Answering (TKGQA) requires language model agents to retrieve evidence, select relevant facts, and perform multi-step temporal reasoning. However, the trajectory-level outcome signal in GRPO does not explicitly distinguish the quality of intermediate decisions: downstream failures can penalize useful evidence acquisition, while identical rewards in all-failed groups eliminate the relative outcome signal despite differences in intermediate progress. We propose Credit Redistribution with Evidence-Driven Opportunities (CREDO), which uses intermediate evidence to recover local supervision, including in all-failed groups, and determine where outcome supervision acts. CREDO assigns positive stage-level credit through comparisons among rollouts of the same question and uses retained answer overlap as an opportunity proxy to shift part of the outcome-policy weight toward reasoning and answering. The framework preserves terminal rewards and trajectory-level advantages, while redistribution conserves total outcome-policy weight per trajectory. Following the public evaluation protocol of prior work, CREDO raises Overall accuracy from 78.0% to 82.4% and Multiple accuracy from 55.0% to 65.6% on MultiTQ relative to the strongest published baseline in our comparison. On TimelineKGQA, it raises cross-KG accuracy from 30.9% to 36.4% relative to our reproduced baseline via direct transfer to ICEWS Actor under matched training and evaluation settings.

---


### 211. [dKV Forcing: Separating Generation and Memory Representations through a Differentiable KV Cache](https://arxiv.org/abs/2611.01648)

**<font color=#1a73e8>作者：</font>** Zhiqi Li, Bo Zhu  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A causal video generator produces two key--value (KV) states for every segment: the KV it uses while denoising that segment, and the KV it writes into the cache for later segments to read. In a pretrained generator the two already differ substantially, later segments attend to them differently, and replacing the written KV with the generation KV degrades the continuation. We propose dKV Forcing (dKV denotes differentiable KV) to learn a dedicated memory representation from its future use: a writer-specific low-rank residual on the shared backbone separates memory writing from generation and is trained through the future reads of what it writes. Learning a write from its future use needs gradients through the cache, which the mutable cache in common use cannot provide. dKV Forcing replaces the training-time cache by persistent differentiable pages with local rematerialization and, in one temporal traversal, computes exactly the gradient that a two-pass reconstruction of the same objective computes. One traversal computes the full memory gradient at $7\%$ generator-update overhead over detached-write training, with $28\%$ less resident memory and $20.8\%$ shorter training cycles than the two-pass reconstruction. Over Self Gradient Forcing (SGF), the same objective trained with the same traversal, writer adaptation raises VBench-Long aesthetic quality by $6.6$ points at 60\,s and $8.5$ points at 240\,s with the highest subject and background consistency, and rollout dropout of the residual keeps most of this gain while restoring the motion of training without write gradients.

---


### 212. [EEG-HealthLLM: Hierarchical Adaptation of Large Language Models for Unified Heterogeneous EEG Health Assessment](https://arxiv.org/abs/2611.01652)

**<font color=#1a73e8>作者：</font>** Ruidong Ma, Jisheng Dang, Ronghao Lin 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Electroencephalography (EEG) provides a non-invasive means for neurological and mental health assessment, yet existing EEG models are typically developed for individual tasks and are difficult to unify across heterogeneous signal configurations and assessment objectives. Large language models (LLMs) offer a common interface for multiple tasks, but adapting heterogeneous EEG signals to a shared LLM raises a key challenge: how to preserve task-specific signal characteristics while enabling effective language-side parameter sharing. To address this problem, we propose EEG-HealthLLM, a unified and parameter-efficient framework for heterogeneous EEG health assessment. We introduce an Asymmetric Hierarchical Adaptation Strategy: task-specific EEG adapters preserve heterogeneous spatio-temporal dynamics, while a unified shared LoRA is injected into the LLM backbone (e.g., Phi-3) to capture shared high-level assessment semantics across tasks. We further establish EEG-HealthBench by reorganizing five existing EEG resources into paradigms covering epileptic seizure detection, major depressive disorder assessment, anxiety risk assessment, depressive symptom risk assessment, and emotional state assessment under a unified subject-independent protocol. Extensive experiments show that EEG-HealthLLM achieves an average balanced accuracy (BAC) of 69.58%, ranking first among the evaluated methods in both average BAC and macro-F1. Compared with independent single-task LoRA adaptation, it improves average BAC from 67.70% to 69.58% while reducing the aggregate language-side adapter footprint by 80.0%. Further analyses reveal task-dependent cross-task interactions and trade-offs, supporting the proposed hierarchical adaptation strategy. The implementation is publicly available at this https URL.

---


### 213. [GatedVLA with Camera-Based Emergency Braking: AlpaSim E2E Closed Loop Challenge Technical Report](https://arxiv.org/abs/2611.01663)

**<font color=#1a73e8>作者：</font>** Kaneyoshi Hiratsuka, Naoki Takada, Makoto Kawano  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> This report presents GatedVLA, our entry for the Physical AI AV (PAI-AV) track. Our learned vision-language-action (VLA) policy pairs the driving-pretrained Qwen-Drive-1.0-4B vision-language model with a layer-wise flow-matching action expert that outputs a 2.5 s horizon of acceleration and curvature controls, augmented with a soft visual mask applied to the expert's cross-attention. Compared to an identically trained baseline, the masked policy achieves comparable overall open-loop error while reducing error on left turns. In local closed-loop evaluation across the same 150 scenes (two rollouts per scene), the visual mask increases the mean scene score from 0.479 to 0.517 (paired difference +0.038, 95% bootstrap CI [-0.018, +0.093], wins/losses 37/26, sign test p = 0.21). Incorporating a rule-based automatic emergency braking (AEB) module at deployment further increases the mean score to 0.599 (+0.082, CI [+0.023, +0.143]) and reduces the mean number of scenes with at-fault collisions from 34.0 to 11.0.

---


### 214. [MMCoT$^3$: Empowering 3D Scene Understanding with 3D-Text Interleaved Multi-Modal Chain-of-Thought Reasoning](https://arxiv.org/abs/2611.01676)

**<font color=#1a73e8>作者：</font>** Yongqi Shan, Yifan Wang, Yunzhi Zhuge 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding and reasoning over 3D scenes from point clouds is essential for a broad range of AI applications. Recent 3D large language models have shown promising results, yet they still face two fundamental limitations: (i) insufficient capability for grounded multi-step reasoning in complex 3D scenes, and (ii) a text-centric inference paradigm that lacks effective interaction between textual reasoning and visual evidence. As a result, these models often fail to verify intermediate inferences, disambiguate similar object instances, and avoid hallucinations. To address these limitations, we propose MMCoT$^3$, the first 3D-Text Interleaved Chain-of-Thought (CoT) framework for 3D scene understanding. The core idea is to explicitly interleave textual reasoning with task-relevant 3D evidence, enabling the model to consult scene observations throughout the reasoning process. In addition, since a textual mention in 3D scenes may correspond to multiple candidate objects, naive object-mention alignment can inject incorrect evidence and mislead subsequent reasoning. To mitigate this multi-instance ambiguity, we design an ambiguity-aware evidence aggregation mechanism that uses query-guided cross-attention to fuse candidate object tokens and inject both evidence and ambiguity cues into the reasoning process. To better equip the model with multi-step reasoning capability, we further develop PointCoT, a large-scale 3D-specific CoT instruction tuning dataset with approximately 176.2K instances spanning captioning, question answering, dialogue, and planning tasks. Extensive experiments on six benchmarks show that our method consistently improves performance and achieves state-of-the-art results, validating the effectiveness of our proposed ambiguity-aware 3D-text interleaved reasoning for 3D scene understanding.

---


### 215. [SPAR: Experience-Driven Strategy Evolution in Multi-Session B2B Sales](https://arxiv.org/abs/2611.01695)

**<font color=#1a73e8>作者：</font>** Hangming Zhang, Yao Zhao, Haotian Kuang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> B2B outbound sales involves high transaction values and relationship-based trust, so closing a deal typically requires multiple rounds of outreach building on prior context. Existing LLM-based sales agents operate within single sessions and cannot carry forward context or refine strategies from experience. Methods that do learn from experience store lessons as unstructured text and treat all outcomes as equally informative, with no mechanism to distinguish a flawed strategy from an external factor. We propose SPAR, a self-evolving framework that models selling strategies as testable hypotheses and refines them without parameter updates. A double-loop architecture lets an inner loop adapt to individual merchants through episodic memory while an outer loop evolves a shared strategy playbook through causal attribution and hypothesis-driven evolution. In a live A/B test on the 1688 platform with over 200,000 merchants, SPAR achieves +15.8% conversion lift and +35.8% high-intent merchant growth. Human evaluation by domain experts rates SPAR at 4.62 out of 5 on overall sales quality, the highest among all methods.

---


### 216. [Just-in-Time Skill Retrieval via Long-Horizon State Tracking](https://arxiv.org/abs/2611.01701)

**<font color=#1a73e8>作者：</font>** Xin Lin, Ziheng Wang, Zerui Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents increasingly rely on external skill libraries to support complex task execution. However, determining which skills are needed remains challenging in long-horizon tasks. Existing methods typically select a fixed skill set before execution, implicitly assuming that a task's procedural requirements can be determined from its initial description. This assumption is restrictive for long-horizon interaction, where new requirements emerge from intermediate observations, execution outcomes, and newly revealed constraints. This motivates just-in-time skill retrieval, which dynamically selects skills as execution unfolds. Just-in-time skill retrieval is promising but challenging: the utility of a skill depends not only on the current context, but also on the evolving task state shaped by prior steps. To this end, we propose JitSkill, a state-grounded framework that addresses this challenge through continuous task-state tracking. By connecting emerging requirements with accumulated task progress, JitSkill provides procedural support throughout execution without treating each retrieval decision independently. Experiments across three agent benchmarks demonstrate its effectiveness in improving long-horizon task completion. Our code is available at this https URL.

---


### 217. [MatMoE: Matryoshka Mixture-of-Experts with Dynamic Mixed-Precision Quantization for Efficient Inference](https://arxiv.org/abs/2611.01704)

**<font color=#1a73e8>作者：</font>** Renjie Wei, Haochen Huang, Chuyu Qiu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architecture has been widely adopted in large language models (LLMs) since it reduces the computational cost through sparse expert activation. However, the massive parameter scale of MoE models hinders their deployment on resource-constrained edge devices. Although existing mixed-precision quantization reduces the model size, they are inherently static, fixing the bit-width of each expert across decoding steps. Such static schemes yield suboptimal performance as they overlook the dynamic variation in expert importance during decoding. Furthermore, they fail to adapt to the dynamic latency constraint driven by the fluctuating system utilization. To address these challenges, we propose MatMoE, a dynamic mixed-precision quantization framework for efficient MoE inference. MatMoE features: (1) a Matryoshka MoE PTQ algorithm that enables experts to operate flexibly at multiple precisions within a stringent memory budget; (2) a floor-and-compensation quantization method that eliminates redundant memory accesses in the Matryoshka representation; and (3) a dynamic bit-width allocation strategy that determines the precision for each expert based on their routing scores to satisfy the dynamic latency requirement. We implement our MatMoE system atop this http URL for both CPU and GPU platforms. Extensive evaluations across three modern MoE models and challenging benchmarks demonstrate that MatMoE achieves $4.0\% \sim 18.3\%$ higher accuracy than state-of-the-art static mixed-precision method. Compared to this http URL, MatMoE delivers $1.3\times \sim 3.7\times$ speedup on Raspberry Pi 5, and $1.2\times \sim 1.3\times$ speedup on NVIDIA RTX 4090 and Jetson AGX Orin.

---


### 218. [Route-Guided CBF-QP Repair for Safe Vision-Language-Action Models](https://arxiv.org/abs/2611.01713)

**<font color=#1a73e8>作者：</font>** Chan Park, Sunwoo Hong, Kirak Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) models can generate task-oriented robot actions, but they do not guarantee safe execution in obstacle-rich manipulation scenes. Although CBF-QP safety filters can locally project unsafe actions into a safe set, such correction may push the robot away from the learned task trajectory and leave the VLA policy without a reliable recovery direction. We propose Route-Guided CBF-QP Repair, a post-hoc repair module that uses the short-horizon action chunk predicted by the VLA to detect blocked nominal trajectories and generate entry-exit-rejoin guidance around obstacles. The selected route is added to the CBF-QP objective as a soft guidance term, while the CBF safety constraint remains hard. On SafeLIBERO, our method improves collision avoidance, task success, and SafeSuccess compared with AEGIS. Our project page is available at GitHub.

---


### 219. [EarlySelectKV: Anticipatory KV Selection via Cross-Layer Query Proxies](https://arxiv.org/abs/2611.01715)

**<font color=#1a73e8>作者：</font>** Yuhao Liu, Yuehao Li, Linghe Zhang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Query-conditioned sparse KV selection reduces long-context inference cost by attending to a subset of historical KV entries at each decoding step. Existing selectors must wait for the target-layer query before scoring candidates and generating indices, placing routing on the immediate pre-attention path. We introduce EarlySelectKV, a training-free transformation that uses proxy queries from earlier hidden states to precompute selected KV indices while retaining the real target-layer query for final attention. Tests with RocketKV, Quest, and Loki show no consistent pattern of quality degradation across the evaluated settings. In the primary RocketKV evaluation, ES-RocketKV differs by +0.018 points on LongBench, approximately -0.01 points on RULER, and +0.25 percentage points on representative NIAH/Passkey settings. In a TensorRT-LLM deployment with CPU-offloaded routing, ES-RocketKV improves end-to-end output throughput by up to 12.4% and reduces GPU-resident memory by 11.1% of the combined KV/K-summary pool. This makes routing timing an explicit optimization target alongside KV subset selection in sparse long-context decoding. Code is available at this https URL.

---


### 220. [Delivered, Not Used: Evaluating Agent Memory at Its Point of Use](https://arxiv.org/abs/2611.01718)

**<font color=#1a73e8>作者：</font>** Changran Xu, Zeju Li, Qiang Xu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Task success, retrieval quality, and cost do not show whether an LLM agent used a delivered memory or what followed from that use. We introduce MemUse, which evaluates memory at its point of use in recorded trajectories: each memory delivery is compared with what the agent could already see and followed through the agent's later actions and their consequences. An agentic judge rates each delivered entry's relevance, accuracy, novelty, influence, and observed effect; programmatic checks enforce complete reading of cited evidence, and fixed rules aggregate the ratings into verdicts linked to memory histories and delivery cost. On 8,000 SWE-bench Verified episodes from three memory systems, resolve rates stay within 0.4 percentage points of a no-memory baseline, yet MemUse shows that most delivered entries were irrelevant, most relevant entries went unused, and in two systems most deliveries restated content the agent could still see. It also surfaces effects that outcomes hide: 23.2\% of episodes with beneficial memory use still failed, and 5 of 16 with harmful use still succeeded.

---


### 221. [MAC-Bench: Benchmarking Multi-Agent Collaboration via Interconnected Tasks](https://arxiv.org/abs/2611.01728)

**<font color=#1a73e8>作者：</font>** Zerui Chen, Qinggang Zhang, Qichuan Liu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based multi-agent systems (MAS) tackle challenging tasks by dividing work among agents and coordinating their contributions toward shared objectives. Evaluating these systems therefore requires benchmarks that assess not only task-solving performance but also the ability to handle interdependent work. However, existing benchmarks often emphasize task difficulty without substantial collaboration requirements or evaluate only a limited range of predefined collaboration patterns. In this paper, we introduce MAC-Bench, a comprehensive benchmark for evaluating multi-agent collaboration through interconnected tasks. Rather than imposing predefined agent roles or communication protocols, MAC-Bench embeds collaboration requirements directly into task dependencies and shared-resource constraints. Specifically, we mine reusable collaboration structures from selected benchmark tasks at two levels. Local collaboration patterns capture recurring interactions among subtasks, while global task structures characterize how these interactions contribute to complete workflows. Through coarse-to-fine composition, these structures are recombined into task graphs combining different collaboration requirements. Tasks are instantiated in executable environments with automated verification of partial progress and complete task resolution.

---


### 222. [Less but Sufficient: Relation Knowledge Selects Compact Knowledge-Graph Contexts, and What External Checks Can and Cannot Catch](https://arxiv.org/abs/2611.01733)

**<font color=#1a73e8>作者：</font>** Seunghui Jwa, Minsu Oh, Sangwoo Hong 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) read knowledge-graph facts ranked by relevance, leaving open whether they suffice or conflict. Our checks use relation knowledge, written by hand or learned from training questions labelled with their relation paths. It selects a compact context of facts yielding an answer, and derives it; a derivability check tests whether an answer follows, a consistency check whether facts conflict, and a validation-chosen routing gate decides where the derived answer replaces the LLM's. Seven open LLMs read the compact context better in exact match than relevance-ranked facts; on ComplexWebQuestions (CWQ) they match SubgraphRAG's facts at a quarter of the prompt tokens, and stronger LLMs read SubgraphRAG's better. Where the routing gate passes, ours leads SubgraphRAG's in exact match in all 53 LLM, benchmark and prompt settings. A precision gate, returning the derived answer only when the check passes with exactly one derived entity, answered 18 and 5 percent of held-out WebQSP and CWQ questions in a pre-specified test, right for 90 and 96 percent. The consistency check judges facts by path evidence only where another path joins their entities, true of 2.5 percent of named-entity facts in our compact WebQSP and CWQ contexts.

---


### 223. [RSI-Env: An Open-Ended Environment for Recursive Self-Improvement of Agents](https://arxiv.org/abs/2611.01736)

**<font color=#1a73e8>作者：</font>** Wanying Qu, Zhiyuan Fan, Jiyao Liu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recursive self-improvement (RSI) envisions agent systems that autonomously improve their own models and harnesses, with each updated system continuing to improve itself. Existing approaches typically restrict optimization objectives, editable components, or evaluation procedures, limiting open-ended exploration and continuity across generations. We introduce RSI-Env, a persistent environment for coordinated model-harness improvement, supporting autonomous training, harness modification, and retention of research state. An independent Host Controller manages services, evaluation, and versioning. Under Self, each accepted model-harness version takes over the next improvement round. We define three settings that vary goal specificity and access to benchmark feedback: Open-General, Capability-Directed, and Benchmark-Guided. Across these three settings, we compare Self with two fixed external Teachers on seven tasks, starting from Qwen3.8-27B with a minimal harness. Without benchmark feedback, Open-General Self raises GPQA Diamond accuracy from 65.2% to 73.2% and AIME 2026 accuracy from 53.3% to 56.7%. All three Capability-Directed Self runs achieve target-aligned gains. Knowledge Self demonstrates continued improvement across system updates, with SimpleQA accuracy rising from 82.0% to 85.0% and then 88.0%. Benchmark guidance and Teacher benefits vary by task. These results demonstrate RSI-Env's support for open-ended exploration and sustained recursive improvement within the studied runs, while highlighting challenges in preserving gains across capabilities.

---


### 224. [How Does Chain-of-Thought Supervision Teach Models to Reason? A Theoretical Analysis](https://arxiv.org/abs/2611.01740)

**<font color=#1a73e8>作者：</font>** Kaito Takanami, Cengiz Pehlevan  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Training with chain-of-thought (CoT) supervision is an effective approach for teaching models multi-step reasoning procedures. At inference time, however, models may need to continue reasoning beyond the finite teacher CoT sequences observed during training, and longer reasoning can instead degrade performance, a phenomenon known as overthinking. How the amount and structure of training-time CoT give rise to such failures remains theoretically poorly understood. To study this problem, we introduce an in-context weight prediction model trained on finite gradient descent trajectories for linear regression. Using high-dimensional asymptotic analysis, we show that the success and failure modes of long-horizon reasoning undergo phase transitions depending on the context length and the total amount of training CoT. We further distinguish two mechanisms of overthinking, error accumulation and error amplification, and show that with short training contexts, increasing the training CoT budget can worsen long-horizon error before eventually stabilizing reasoning. Experiments with fully trained linear and multi-head softmax attention further show that these qualitative behaviors persist. Our results provide a theoretical account linking properties of training-time CoT to inference-time failures and offer guidance for designing teacher CoT that supports stable reasoning.

---


### 225. [Evolving Memory, Learning to Meta-Control: Test-Time Adaptation for Experience-augmented LLM Agents](https://arxiv.org/abs/2611.01747)

**<font color=#1a73e8>作者：</font>** Zeyuan Zhao, Yuanyuan Shi, Peng Yu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Self-evolving agents accumulate experience from task streams, but existing frameworks typically rely on fixed pipelines to retrieve and utilize this experience, neglecting when and how to deploy it. We introduce Online Meta-Control of Experience (OMCE), a framework that updates experience memory and learns a meta-control policy from task feedback during test-time adaptation. OMCE employs a lightweight contextual-bandit meta-controller that uses compact retrieval signals to select among four cognitive actions: DIRECT, EPISODE, GUIDE, and DISTILL. This routing mechanism operationalizes three coupled decisions: whether to invoke experience, which memory format to utilize, and when to consolidate new guidance. OMCE evolves online, leveraging task feedback to update the memory bank and refine the routing policy via contextual bandit updates. Experiments on four online adaptation benchmarks across four backbones show that OMCE improves first-attempt success by up to 20.5 percentage points over the strongest compared baseline, while reducing per-task token use by a factor of 5.7 to 62.5 relative to ACE with GPT-5.2. Controlled ablations further support the benefits of learned routing and continued routing policy adaptation.

---


### 226. [FinishStrong: Learning to End Well after Imperfect Start in Video Temporal Grounding](https://arxiv.org/abs/2611.01765)

**<font color=#1a73e8>作者：</font>** Yuda Zou, Boxiang Zhou, Xin Zhou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> A poor start lowers the ceiling, but does not negate the value of finishing well. In autoregressive video temporal grounding, models systematically exhibit an endpoint performance asymmetry, predicting ends significantly worse than starts. A committed flawed start acts as an immutable physical constraint, irreversibly capping the attainable overlap as a sunk loss. While models should minimize the remaining conditional regret, standard post-training paradigms fail to teach this adaptation. Specifically, teacher-forced SFT suffers from strict prefix exposure bias, and holistic trajectory evaluation in standard GRPO inadvertently penalizes conditionally optimal ends if they follow a poor start. To address this, we introduce FinishStrong, a novel two-stage post-training framework explicitly designed to teach optimal continuations. First, Online-start SFT exposes the end prediction to the model's own generated contexts. Second, Conditional-tree GRPO restructures the sampling topology, centering end rewards exclusively within the same-start branch to mathematically isolate the conditional end quality from the inherited start penalty. FinishStrong-9B achieves a state-of-the-art 61.7\% overall IoU on TimeLens-Bench, remarkably outperforming flagship closed-source models like Gemini-3.8-Flash and Qwen3.8-Max. Crucially, when forced to continue from imperfect starts, it reduces the subsequent end prediction error by 36.5\%, proving its exceptional ability to end well after flawed starts. Code will be open.

---


### 227. [MemRole: From Memories to Decisions for Long-Horizon Reasoning in Role-Playing Agents](https://arxiv.org/abs/2611.01778)

**<font color=#1a73e8>作者：</font>** Mengting Li, Xilong Cheng, Zhihao Xiao 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based role-playing agents are fluent at imitating a character's style, yet struggle to make role-consistent decisions over long narrative horizons. Such decisions are shaped by experiences spanning many prior scenes, which are often partial and may point in different directions. Existing methods inject cross-scene memories as context, but do not reason about how past events shape a character's current motivations and behavior. We propose MemRole, a framework that makes this memory-to-decision process explicit. It introduces Long-Horizon Memory Thinking (LHMT), a reasoning schema that decomposes hidden reasoning into context understanding, memory activation, and response strategy planning, trained on a novel-derived dataset whose character-grounded, timeline-constrained memory pools limit each character to what it could plausibly know at the current narrative point. Beyond supervised fine-tuning, we propose Self-Refining On-Policy Self-Distillation (SR-OPSD): the model critiques its own rollouts against the reference under a data-driven rubric, and a critique-conditioned teacher view of the same model distills token-level guidance back into the policy. MemRole-32B improves over its backbone by 15.2 points on memory-grounded role-playing, performs on par with frontier LLMs such as GPT-5.4, and achieves the best character-motivation recognition accuracy on CroSS-MR.

---


### 228. [MaterialVellum: Steering Generative AI by Leveraging Expressive Material Affordances to Form Design Constraints](https://arxiv.org/abs/2611.01800)

**<font color=#1a73e8>作者：</font>** Chu Li, Nicolai Marquardt, Hugo Romat 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present MaterialVellum, an interaction approach for steering generative AI through material-inspired manipulation of design constraints. In urban design, for instance, zoning bounds can be defined by the stretch of elastic bands, building density redistributed by molding clay, and functional relationships organized by the pull of magnets. MaterialVellum departs from current interfaces that rely on natural language prompts, and instead leverages users' existing knowledge of physical materials to represent and manipulate design constraints. We introduce a framework that maps material affordances---such as elasticity, malleability, or attraction---to spatial, relational, and proportional constraints that underpin design. These mappings are operationalized in user interfaces through familiar direct manipulation multi-touch gestures, including stretching, sculpting, and clustering, whose effects feed as control parameters into generative AI pipelines. We demonstrate this approach through technology probes, including an urban design, a flower arrangement design, and a graphical design scenario.A qualitative study (N=10) shows that material-based interactions improve accessibility of constraint expression, support exploratory workflows, and lower barriers for non-experts, while effectiveness depends on alignment with users' mental models.

---


### 229. [Shared relations, specific choices: conditional sensitivity and competing pathways in language models](https://arxiv.org/abs/2611.01809)

**<font color=#1a73e8>作者：</font>** Kaixiang Shu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> How does a relational representation shared across queries drive a query-specific choice? Controlled entity-binding experiments with GPT-2 Small, Qwen2.5-1.5B and Llama-3.2-1B reveal a low-dimensional relational background that is predominantly shared across query roles and transfers to new names. Same-domain interactions persist when another attribute domain is queried. After removing this component, restoring independently trained relation directions brings output contrasts closer to their original values than sign-reversed or equal-norm random controls in all three models. Yet a transferable relational representation need not have a transferable functional sign. In Qwen2.5, fixing model weights, the training-mean relation vector and edit dose yields opposite selection effects across binary and lexical-mapping prompts with different answer vocabularies. A factorial contrast of downstream sensitivities across attribute-query combinations determines the shared direction's local signed selection gain. In a separate eight-condition protocol, mean local gain is positive in Qwen2.5 and negative in Llama3.2. Late-component clamps resolve opposing pathway contributions: in Llama3.2, negative transmission through selected attention-only paths is partially offset by positive transmission through paths traversing both selected attention and MLP sets. Source-coordinate analyses establish distributed factor coverage, hidden-receiver readouts reveal layout-dependent combination, and instance-geometry interventions separate response direction from amplitude. These findings show how conditional sensitivity and competing pathways give shared relational structure its effect on specific choices.

---


### 230. [LegoEnv: Self-Evolving Agentic Environments via Modular Recombination](https://arxiv.org/abs/2611.01834)

**<font color=#1a73e8>作者：</font>** Zhuosong Jiang, Chengxu Wu, Junqi Liu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM agents learn by interacting with environments, yet existing environments are designed for specific tasks and fail to generalize to new ones. Recent methods automate environment construction with LLMs. However, they generate each environment from scratch, neither reusing parts shared across environments nor carrying a fix from one environment to the rest. To address this, we propose a new paradigm of evolving environment atoms, which composes environments from reusable atoms (intent, rule, data and server) and evolves the atoms when an environment fails to give reliable feedback (e.g., an application lacks a tool the task requires). To instantiate this paradigm, we introduce LegoEnv, which builds 5,465 verified environments over 223 applications, and one round of evolution raises the share of solvable environments from 71.6% to 88.3%. On AutomationBench, SFT on these environments lifts Qwen3.6-27B from 16.0% to 32.0%, and RL with their verifiers lifts Qwen3.8-27B from 37.6% to 40.3%. Further analyses show steady gains with corpus size, transfer to unseen applications, and failures concentrated in a few shared root causes.

---


### 231. [ReFrame: Silence-Aware Compute Reclamation for Full-Duplex Speech Models](https://arxiv.org/abs/2611.01835)

**<font color=#1a73e8>作者：</font>** Zheng Zhou, Guanyi Chen, Jing Wei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Full-duplex speech models execute dense model inference for every audio frame throughout a live interaction. This uniform framewise schedule creates sustained GPU load across dialogue states whose computation has strong, reusable temporal structure. ReFrame formulates full-duplex inference as a silence-aware computation problem. Mutual Silence Speculation (MSS) operates when both participants are silent: it evaluates multi-frame Temporal continuations, verifies text and hidden-state stability, and applies batched Mimi audio-token correction. Listening Frame Folding (LFF) operates while the user speaks and the agent listens: it processes already-arrived user frames through parallel Temporal execution and frame-batched audio-token generation while accepting only the verified prefix. Frame-Budget Reinvestment (FBR) assigns the released frame intervals to resumable external retrieval and language-model workers, then injects timely references through Moshi's conditioning interface. We instantiate ReFrame on five full-duplex models spanning Moshi-family, phase-structured, and flattened autoregressive generation. Across the complete 1,225-conversation FDBench, ReFrame reduces measured GPU execution time by 18.80-31.01% and retains 96.92-100% non-PAD text agreement on five different models. On HaluEval tests, FBR increases the number of correct generated spoken answers from 86 to 205 under the same auxiliary-service budget. ReFrame turns recurring dialogue structure into lower inference cost and higher end-to-end service capability.

---


### 232. [NEIGHBOR: Aligning Service Behaviour and Evidence Use in an LLM Agent for Community Resident Services](https://arxiv.org/abs/2611.01836)

**<font color=#1a73e8>作者：</font>** Zongyou Yang, Yinghan Hou, Xiaokun Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Residents who contact a community service desk about a repair or a service charge need answers they can act on, with facts that hold for their case and commitments the desk can keep. In tool-augmented LLM agents, such facts come from documents and records, and the conduct of a service answer is usually specified in a system prompt. We present NEIGHBOR, an LLM agent for community resident services that trains this conduct into the model that drives its tools. NEIGHBOR is deployed on a live resident-service platform for a district of an East Asian city of more than ten million people. It adapts Qwen3-235B-A22B with LoRA on 7,824 supervised fine-tuning examples built from public community-service materials around six service-behaviour targets, among them commitment control and human referral, and the adapted model plans document retrieval and read-only text-to-SQL over the resident's own records. In an offline evaluation with seven configurations, an independent domain expert rated all 350 answers to 50 stratified held-out queries. NEIGHBOR scores 7.74/10 against 5.86 for the same agent running the un-tuned model (+1.88; paired Wilcoxon $p<10^{-8}$; higher on 46 of 50 queries) and improves all six rated dimensions. No tool-augmented answer received a red-line flag (standalone models: 8-14% of answers). An LLM judge ranks the seven configurations much as the expert does (Spearman $\rho=0.93$). Its rubric counts specifics absent from the reference answer as fabricated, so it scores tool-grounded answers 1-2 points lower, enough to change which configuration ranks first. For resident-facing agents, service behaviour is a practical fine-tuning target that raises expert-rated answer quality with the tools held fixed.

---


### 233. [Self-Evolving Agentic Workflows via Semantic Decomposition of Complex Tasks](https://arxiv.org/abs/2611.01840)

**<font color=#1a73e8>作者：</font>** Zichuan Fu, Junjia Qi, Xian Wu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic workflows organize complex tasks into reusable procedures. However, invoking an LLM at every step incurs repeated inference costs and delays. We propose a framework for self-evolving agentic workflows through semantic task decomposition. Each subtask has explicit applicability conditions and a procedure that executes code or invokes a model as needed. An agent uses execution feedback to refine the decomposition and update these procedures. Experiments in the GLEE competition show the framework on bargaining, negotiation and persuasion. Most observed final-decision procedures are implemented in code. Code is available at this https URL.

---


### 234. [Advances in Agentic Computer Graphics](https://arxiv.org/abs/2611.01860)

**<font color=#1a73e8>作者：</font>** Hengyu Liu, Jihyeon Je, Ruiqi Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Computer graphics is built on code. Large language model (LLM) agents can now generate graphics code and iteratively refine it through various feedback. This capability opens the door to a potentially new paradigm of computer graphics, with graphics algorithms increasingly built around agentic systems to automate progressively complex tasks. Over the past years, research on agentic graphics has expanded rapidly across a diverse range of tasks. This rapid growth makes it increasingly difficult for manual literature reviews to keep pace with new developments. At the same time, similar ideas are often described using different terminology across these tasks, further complicating efforts to develop a systematic understanding of the field. In this report, we address these challenges through two contributions. First, we introduce a unified taxonomy for characterizing agentic systems across diverse computer graphics tasks. Second, we develop an agentic literature system that can assist human researchers in analyzing existing and newly published papers at scale. Building on these contributions, we analyze emerging research trends and discuss open challenges in coordinating agents and tools across graphics tasks, designing interfaces and representations for human-agent collaboration, sustaining long-horizon planning and refinement, and reliably evaluating interactive graphics systems.

---


### 235. [Quantizing Recurrent Language Models Is Easier Than You Think](https://arxiv.org/abs/2611.01864)

**<font color=#1a73e8>作者：</font>** Philipp Nazari, Neehal Tumma, Daniela Rus 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear recurrences are becoming an increasingly common building block in large language models, replacing the growing KV cache of softmax attention with a fixed-size recurrent state that enables efficient decoding. However, the quantization stack has largely been developed around softmax Transformers, whose numerical properties and inference state differ from those of recurrent models. Our goal is to understand these differences and study the design space of quantization methods for recurrent models. In our analysis, we differentiate between two targets. First, extra-state quantization concerns weights and activations outside the recurrent state, whose distributions are shaped indirectly by the sequence mixer during training. In controlled 1.3B parameter models, we find that decayed recurrences develop weaker residual outlier channels than softmax attention and are therefore easier to quantize without incoherence processing. Second, intra-state quantization concerns the recurrent state itself during decode, where repeated updates create a different numerical problem from KV cache quantization. We instantiate our findings as LoReS, a state quantization pipeline combining value-axis scale grouping to match output channel magnitude, decay-based mixed-precision to protect slowly decaying heads or channels, and stochastic rounding to limit error accumulation under repeated requantization. Across Qwen-3.5 9B, Nemotron-H 8B, and Kimi-Linear 48B-A3B, LoReS supports robust 8-bit state quantization and lower effective precision on shorter decode horizons. We implement LoReS in vLLM and demonstrate end-to-end decode speedups.

---


### 236. [Don't Guess, Ask Wisely: Benchmarking and Training Proactive Elicitation in Open-Domain LLM Conversations](https://arxiv.org/abs/2611.01878)

**<font color=#1a73e8>作者：</font>** Rongyu Zhang, Mutian Bao, Jinjian Zhang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When user queries are incomplete, large language models should ask targeted questions before committing to an answer, a capability we call proactive elicitation, yet evaluation on real user-assistant queries across seven LLMs (8B to frontier) shows that fewer than 11% of underspecified queries trigger a follow-up question. To benchmark and train this capability, we introduce VagueBench, where each seed query is annotated with structured intent and detail units then degraded into intent-vague and fully-vague variants via controlled removal of linguistic cues, yielding known hidden information sets for evaluating both when and what to ask. We propose DialogGRPO, an offline reinforcement learning method that organizes multi-turn elicitation as a dialogue-state directed acyclic graph, where candidate questions at each node receive dense turn-level rewards combining immediate information gain with lookahead value through group-relative comparison, enabling fine-grained credit assignment without runtime simulation. DialogGRPO elicits missing information on over 88% of vague queries with substantial gains in both recovery efficiency and answer coverage, without over-asking on complete queries, outperforms prompting and test-time-scaling baselines, and generalizes zero-shot to MultiWOZ 2.4 and AmbigQA.

---


### 237. [Interface Quilt: Modifying Applications with Computer Use Agents and Generative UI](https://arxiv.org/abs/2611.01891)

**<font color=#1a73e8>作者：</font>** Leping Qiu, Jo Vermeulen, Tim Zindulka 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Modifying an existing application is difficult when it does not provide programmatic access for that change. Recent advances in computer-use agents (CUAs) enable richer understanding and operation of existing interfaces, while generative UI (GenUI) makes it practical to generate new ones. We examine how these advances expand software modification through a design space of what can be changed and a framework for how modifications can be implemented. We then introduce Interface Quilt, a system that combines CUAs and GenUI to generate interface patches, which are new interfaces displayed over an existing application to modify its presentation, interaction, and capabilities. Through demonstrations across a variety of applications, we show that interface patches support a range of modifications without source code, APIs, or accessibility data.

---


### 238. [Does reflective LLM feedback survive a wet-lab-scale label budget?](https://arxiv.org/abs/2611.01908)

**<font color=#1a73e8>作者：</font>** Haoxuan Zeng, Xin Luo  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Can reflective language-model feedback improve a biological predictor when each cycle buys only one plate of labels? We separate three possible sources of benefit: proposing model edits, choosing measurements, and revising decisions through repeated feedback. We replay $36$ ProteinGym assays, starting with $96$ labels and acquiring $96$ per round for six rounds, with a sealed test set and a shared edit schema. The pre-specified comparison of full LLM control against random edits detects no advantage in test rank correlation ($\Delta z=-0.008$, $95\%$ CI $[-0.034,+0.018]$); equivalence is also unestablished. Exploratory ablations nevertheless identify useful model editing. With random acquisition fixed, LLM edits improve Fisher-transformed test Spearman by $0.043$ over no edits; with acquisition fixed to upper confidence bound, they improve normalized top-variant recovery by $0.023$. LLM acquisition alone does not detectably outperform fixed adaptive rules, and repeated feedback does not detectably outperform one initial recommendation under full control. Thus, the observed gains support constrained specialist editing, while the incremental value of recursive reflection remains unestablished at this label budget.

---


### 239. [Who Asks, Who Answers: Linear Attention Builds the Query in Hybrid Language Models](https://arxiv.org/abs/2611.01909)

**<font color=#1a73e8>作者：</font>** Wenqi Zeng, Chen Feng, YuAng Chen  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Hybrid language models interleave linear-attention layers with a small number of softmax-attention layers. Prior work largely attributes in-context retrieval to softmax attention, treating linear attention primarily as a mechanism for compressing past context. We revisit this division of labor and show that linear attention plays a direct role in retrieval by constructing the query used by softmax attention. Studying Qwen3.5 (Gated DeltaNet) and Granite4.0 (Mamba-2), we identify an Encode--Address circuit. An early Encode block preserves token identity, while an Address block constructs the final-position representation from which a softmax \emph{reader} forms its attention query. Transplanting this representation between prompts with different queried keys redirects retrieval in 0.97--0.99 of cases. The Address block's recurrent state carries the retrieval target, and its computation transfers across architectures: replacing Granite's Address block with Qwen's restores retrieval accuracy to 0.92--0.94 without updating either model's weights. Across six Qwen3.5 models, Address computation becomes distributed at larger scales over a chain of blocks, each guiding a successive reader, as the query no longer passes from one reader to the next through attention. These findings reveal a division of labor in hybrid retrieval: linear attention constructs the query, while softmax attention performs the lookup. Code is available at this https URL

---


### 240. [SurgQ-VLM: Question-Conditioned Dual-Stream Compression and Answer-Type-Aware Reinforcement for Surgical Video Question Answering](https://arxiv.org/abs/2611.01913)

**<font color=#1a73e8>作者：</font>** Dhruv Makwana, Ananya Mantravadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reasoning about surgical video -- which phase is underway, which instruments act, and when events occur -- underpins operative documentation, workflow analysis, and skill assessment. Yet surgical visual question answering is still largely built on single frames and closed labels that cannot express a duration, an ordering, or a count, and the video models that lift the frame limit typically compress every clip the same way regardless of the question, discarding the temporal evidence the answer needs. Worse, the answers are structurally heterogeneous, spanning five incompatible structures -- binary, classification, multi-label, counting, and sentence-temporal -- that no single training signal scores uniformly well. We propose SurgQ-VLM, a two-stage model for surgical video question answering. Stage 1 trains a question-conditioned dual-stream (slow/fast) compressor for a LoRA-adapted Qwen2.5-VL-7B: cross-attention conditions both streams on the question, and each clip's visual tokens shrink 49x from the raw ViT patches (11x vs. post-merge backbone tokens). Stage 2 post-trains with GRPO under an answer-type-aware reward that scores each question on the metric matching its answer structure (micro-F1 for label sets, normalised error for counts, a content-timing blend for temporal windows). On a sealed 21,840-question test split over Cholec80 and CholecT50, SurgQ-VLM reaches 0.779 keyword accuracy and a 10x BLEU-4 gain over zero-shot; GRPO adds 2.5 pp K-Acc (2.0 pp attributable to the answer-type-aware reward), concentrated in the structurally hard types, with answer format unchanged (ROUGE-L). Code is available at this https URL.

---


### 241. [AgenticMobility: An Open-Source Platform for Multi-AI-Agent Mobility Dynamics](https://arxiv.org/abs/2611.01918)

**<font color=#1a73e8>作者：</font>** Jiaheng Xiao, Jiangtao Han, Jiachen Wang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Understanding mobility dynamics and the effects of urban transportation management policies requires examining how individual travel decisions, traffic conditions, and policy interventions influence one another over time. We present AgenticMobility, an open-source experimental platform for studying how mobility AI agents and other AI agents interact, adapt through repeated experience, and collectively shape mobility outcomes. Persistent agents retain identities and relevant states across rounds, with explicit interfaces defining information access, admissible actions, and decision schedules; linked records trace decisions, execution, and feedback.
In the current implementation, large language model (LLM) agents act as travelers choosing routes and departure times and as a manager periodically adjusting link charges within MATSim. A preliminary demonstration spans 100 simulated days in each of five configurations, with one run per configuration and a shared simulation seed. In the joint traveler--manager run, all 1,179,300 finalized target decisions satisfied action constraints; execution checks verified implementation of accepted choices and preservation of personal memories across days. Trajectories show stable route choices alongside departure-time adjustments and differences between controlled-trip and population-wide outcomes.
The platform supports experiments on individual adaptation, collective outcomes, and management interventions by varying information access, retained experience, and management feedback. Source code is available at this https URL

---


### 242. [Vision-language classification of Torsades de Pointes risk from pseudo-coloured ECG images: do T-wave morphology and colour context help or hinder?](https://arxiv.org/abs/2611.01921)

**<font color=#1a73e8>作者：</font>** Dario Labrador Alonso, Alaa Alahmadi  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Contextual prompting is widely presented as a cheap route to better performance from vision models, but the evidence comes largely from benchmarks in which an attribute named in a prompt is also present in the image, confounding the two channels. We investigate the significance of context for a semantically complex biomedical signal classification task using a domain-adapted vision-language model, BiomedCLIP. Building on our previous work that renders electrocardiogram (ECG) signals as colour-enhanced images to flag Torsades de Pointes risk using the QT-nomogram and pseudo-colouring technique, we cross four context strategies with four T-wave morphology label sets, evaluated zero-shot and with a class-balanced linear probe, under five-fold stratified cross-validation on 9,789 images. Zero-shot inference is unusable. Once trained, the colour-enhanced images outperform the colourless ones on every metric: balanced accuracy 0.903 versus 0.825, sensitivity 0.914 versus 0.827, specificity 0.892 versus 0.823, ROC-AUC 0.955 versus 0.888 and Matthews correlation coefficient (MCC) 0.437 versus 0.311. Crossing colour-in-image with colour-in-prompt separates the confounded channels: the image contributes +0.126 MCC (+0.078 balanced accuracy, +0.067 ROC-AUC) whether or not the prompt names colour, whereas naming it changes nothing under any metric. Context is two-sided: the best prompt set gains 0.008 MCC where colour is present and 0.016 where it is not, while the worst loses 0.017 and 0.013. For a signal rendered as an image, the leverage lies in how the signal is drawn rather than in how it is described - and where the endpoint is an interval measurement, prompts naming T-wave morphology describe the wrong quantity.

---


### 243. [TAC-CoT: Tool-Empowered Implicit Chain-of-Thought via Interleaving Explicit Tokens](https://arxiv.org/abs/2611.01926)

**<font color=#1a73e8>作者：</font>** Juseon Do, Sangmin Bae, Jeesu Jung 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based agentic systems are increasingly combined with CoT reasoning to solve tasks that require accurate reasoning, external knowledge, and multi-step deliberation. Yet, explicit CoT incurs substantial generation overhead, while implicit CoT, which replaces textual rationales with compact continuous tokens, does not naturally support the explicit communication interface required for agentic tool-use. We propose TAC-CoT, a tool-empowered adaptive implicit CoT framework that replaces explicit reasoning traces with compact latent reasoning segments while retaining textual tokens only for tool calls, observations, and final answers. This interleaved design enables agentic tool-use without verbalizing every intermediate reasoning step. Experiments on agentic math and QA benchmarks show that TAC-CoT improves accuracy by up to 8.8 points while reducing model forward passes by up to 6.8x. Furthermore, analyses show that TAC-CoT improves tool-use quality in both single- and multi-tool settings.

---


### 244. [Is Your Long-Horizon Benchmark Really Deep? Measuring and Synthesizing Depth in Terminal Tasks](https://arxiv.org/abs/2611.01927)

**<font color=#1a73e8>作者：</font>** Yu Jiang, Yue Huang, Hang Hua 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Long-horizon terminal tasks are used to evaluate and train agents. Human-curated datasets are scarce, so many synthesis methods have emerged. They usually measure the length of a task by the turns a model needs to pass it, and its difficulty by labels the LLM sets during generation. We find, however, that the turn count largely reflects the habits of the model, not only the demands of the task, and that the labels barely track how often models pass. We describe a terminal task by its work, the number of operations it requires, and its depth, the number of turns that must happen in sequence because the commands of each turn can only be chosen after reading the output of the previous one. Estimating depth as the smallest turn cap, stated to the agent, under which the task passes, we audit 734 tasks from six existing datasets. Synthesis has mostly added work, not depth: 94% of the solved synthetic tasks pass within three turns, yet depth, unlike the turn count, predicts difficulty beyond work. We propose DEPTH, in which a generation agent writes each task one segment at a time in a real software environment, carrying out each segment before writing it and starting the next from the state it leaves. Our 105 tasks exceed every audited dataset in depth and work, and none of six current models passes half of them. Fine-tuning Qwen3-8B on runs from these tasks improves it on two terminal benchmarks.

---


### 245. [TriPhysBench: Evaluating Physical Intelligence for Embodied Agents](https://arxiv.org/abs/2611.01934)

**<font color=#1a73e8>作者：</font>** Zhongxiang Sun, Chenghao Yang, Haojie Ding 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Embodied agents need physical intelligence to understand their surroundings through physical perception, physical knowledge retrieval, and physical reasoning. These capabilities must work together to interpret events and make quantitative judgments. Existing benchmarks advance physical understanding and general-purpose tool use, yet the coordination of these capabilities in physical scenarios remains insufficiently characterized. Inspired by Popper's Three Worlds, we introduce TriPhysBench, a benchmark of 410 questions from 200 videos that brings physical perception, physical knowledge retrieval, and physical reasoning into a shared evaluation setting. Its measurement-grounded and knowledge-grounded subtasks impose complementary demands on obtaining observations and acquiring external specifications, then applying them to quantitative problems. Among six representative vision-language models, the best achieves an answer accuracy of only 50.38%, revealing limited performance on tasks that require these capabilities to work together. We further introduce TriPhys, a framework that learns a unified policy for physical perception, knowledge retrieval, and quantitative reasoning from complete tool-integrated trajectories. The policy uses intermediate reasoning to guide retrieval and computation, then incorporates tool feedback into subsequent physical inference. On 110 questions from videos excluded from training, TriPhys improves answer and solution scores across three Qwen configurations, with a 17.7% relative gain in answer accuracy for TriPhys-27B over its Qwen3.6-27B backbone. This work provides a benchmark and a learning pathway toward embodied agents that move beyond recognizing events to understanding and reasoning about the physical processes behind them.

---


### 246. [VLSplat: Vision-Language Guided Object-Centric 3D Gaussian Splatting via Scene Graph](https://arxiv.org/abs/2611.01939)

**<font color=#1a73e8>作者：</font>** Yuntae Jeon, Younho Jeon, Sujin Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learning semantic representations for 3D Gaussian Splatting has recently emerged as a promising direction for 3D scene understanding. However, existing 2D-to-3D semantic lifting approaches rely primarily on 2D segmentation supervision and lack object-level priors, causing the learned representation to be driven by local mask evidence rather than holistic object structure. In this paper, we present VLSplat, a vision-language guided approach for object-centric semantic lifting in 3D Gaussian Splatting. Our method augments mask-based lifting with object-level semantic priors derived from vision-language models and refines Gaussian representations using an object-group scene graph. The refinement is performed through two language-guided modules: intra-group refinement suppresses semantic noise within object groups, while inter-group acquisition expands object support regions by incorporating structurally relevant candidates from neighboring groups. Extensive experiments on indoor scene datasets demonstrate that VLSplat improves the semantic consistency and structural completeness of object-level categories. Our code and models are available at this https URL.

---


### 247. [ReWY: Faster Gradient Computation for Delta-Rule Attention Family](https://arxiv.org/abs/2611.01940)

**<font color=#1a73e8>作者：</font>** Yi Zhang, Zhixin Zhao, Weiwei Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Delta-rule linear attention underlies language models such as Kimi Linear and Qwen3-Next. Chunkwise implementations expose matrix parallelism, but their backward passes compute unnecessary auxiliary adjoints. We present ReWY, an algebraic reformulation that reduces this work before optimizing accelerator execution. Differentiating the chunk correction as one triangular residual system eliminates the inverse adjoint and reduces seven local WY matrix products to three. Two complementary transformations expose further reuse: centered matrix contractions replace pairwise vector-gate processing, and scalar-gate reductions reuse key-gradient products instead of forming a key Gram matrix. These identities simplify backward computation for DeltaNet, GDN, KDA, and GDN2 while preserving the recurrence and gradients in exact arithmetic, without changing the architecture or training objective.
We implement the reduced graph on GPUs and Ascend NPUs. Under matched recomputation and full-saving policies, precision-qualified six-shape comparisons with frozen FLA references yield 1.15-1.81$\times$ geometric-mean complete low-level backward speedups on NVIDIA GPUs. All four operators achieve 1.18-1.70$\times$ on H100 and H200 while retaining original FP32 working matrices. A separate public-autograd evaluation on Ascend 950DT, including gradient conversions, yields 1.09-2.89$\times$ under available matched policies. Paired ablations establish further ReWY gains after optimizing the complementary contractions. Complete-gradient checks validate the recorded operator cases; supplementary full-model backward measurements assess integration into community FLA models and a GDN2 layer port. Code and reproduction materials: this https URL.

---


### 248. [Beyond Multimodal Emotion Conflict: Temporal Context-Aware Hidden Emotion Detection with Multimodal Large Language Models](https://arxiv.org/abs/2611.01943)

**<font color=#1a73e8>作者：</font>** Yonghao Wang, Jiaxin Zhou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal emotion recognition commonly combines textual, acoustic, and visual signals to infer affective states. Recent work has begun to study conflicts among modalities, but a conflict does not necessarily indicate that a person is concealing an emotion. It may also result from mixed emotions, individual expressive styles, or contextual factors. This proposal aims to distinguish ordinary emotional inconsistency from emotion concealment and to infer the underlying emotion when supported by evidence. We plan to construct a multimodal benchmark with explicit annotations of expressed emotion, internal emotion, and concealment conditions, and to develop an MLLM-based framework that integrates fine-grained facial Action Units (AUs), cross-modal features, and temporal context.

---


### 249. [Tracing How Language Models Integrate Temporal Anchors into Factual Recall](https://arxiv.org/abs/2611.01945)

**<font color=#1a73e8>作者：</font>** Ayana Niwa, Masahiro Kaneko, Kentaro Inui  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Factual recall in language models is typically framed as retrieving a factual association: a subject--relation pair maps to a single object. However, many facts are context-dependent: the same pair maps to different objects depending on a condition such as time. We introduce anchored factual recall, in which the model receives an explicit conditioning expression, an anchor, and must select the object valid under it. This raises questions that single-object recall does not: where the anchor enters the computation, what it changes, and how that change selects the answer. Focusing on temporal anchors, we answer them with causal interventions on four open-weight models on English prompts and identify two routes. In a subject-mediated route, the anchor resolves the final subject-token representation to the queried year, and the relation redistributes the readout of this state across attention heads. In a direct route] the final position attends to the anchor, and upper-layer MLPs turn this signal into a preference for the time-appropriate object. The two routes are parallel channels: their contributions add up, most queries use both, and their balance depends on the query, e.g., on the relation, consistently across models. This reframes mechanistic accounts of factual recall from retrieving a single stored object to selecting among context-dependent alternatives.

---


### 250. [CertClaim: Towards Certified Model-Claim Verification for Coding-Agent Services](https://arxiv.org/abs/2611.01950)

**<font color=#1a73e8>作者：</font>** Jiacheng Lu, Qixuan Yang, Tao Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Coding-agent services are priced by the model they claim, making the verification of such model claims crucial for their users. In this paper, we reveal that existing model auditing methods rely on a latent assumption that the deployment is static, i.e., the claimed model is always served in one reference configuration. This assumption does not hold for coding-agent services, whose providers may legitimately change the sampling preset, the reasoning mode or the system prompt without changing the model. As a result, existing methods either falsely accuse honest providers or miss cheap derivatives of the claimed model. To address this problem, we propose a certified model-claim verification method (dubbed CertClaim). Instead of testing the service against one reference deployment, we make the authorized deployments part of the claim and test whether some authorized deployment explains all the evidence of the service, by calibrating multiple evidence channels in every authorized deployment and fusing them within each deployment. We provide theoretical analyses of its false-accusation rate and detection condition. Extensive experiments on eight claims, two agent harnesses and three task suites verify the effectiveness of CertClaim, which is valid in every setting while separating substitutes far better than existing methods, as well as its resistance to potential adaptive attacks.

---


> [!TIP]
> 当前位于：**201-250**（第 5/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | **201-250** | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-515](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
