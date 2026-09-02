# 🧠 大模型相关研究 | 2026年09月02日

> 本类共 **452** 篇论文：已确认 **431** 篇，待复核 **21** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-452](./part-10.md)

---

### 351. [Geometry of Divergence: Tracking Hidden-State Trajectories for Adaptive Multi-Turn Reasoning](https://arxiv.org/abs/2608.30650)

**<font color=#1a73e8>作者：</font>** Jie Liang, Zhengxin Yu, Hamid Nasiri 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents need to sustain goal-consistent reasoning across long multi-turn interactions under strict resource constraints. However, as the multi-turn context accumulates, it can destabilize the underlying LLM's internal representation of task-relevant information from earlier turns, blurring the boundary between constructive reasoning and representation drift. We formulate multi-turn reasoning as a hidden-state trajectory of the underlying LLM that is characterized via two complementary signals: temporal curvature that captures the directional consistency of turn-to-turn updates, and variance slope which measures the expansion or contraction of the exploration space. Across four tasks and three underlying LLMs, we observed that these geometric signals distinguish between correct and incorrect episodes prior to completion. We further decompose each episode into three-action chains formed from four actions (Read, Write, Respond, Transfer) and show that separability is action-dependent, with different signals distinguishing various chain patterns. Our experiments demonstrate that trajectory geometry can identify critical turns in the reasoning process, increasing task success rates on $\tau$-Bench from 24.1% to 39.6% while reducing token cost by 11.2%.

---


### 352. [Fine-Grained Multi Image Object Hallucination Benchmark](https://arxiv.org/abs/2608.30653)

**<font color=#1a73e8>作者：</font>** Joonki Min, Chaeyun Kim, Hyungwook Choi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal Large Language Models (MLLMs) are increasingly deployed in multi-image scenarios requiring complex reasoning across visual contexts. However, current MLLMs remain fundamentally limited by object hallucination-generating plausible yet factually inconsistent descriptions about objects. Existing benchmarks, designed primarily for single-image settings or providing only high-level multi-image assessments, cannot systematically diagnose how visual complexity and reasoning demands trigger hallucination. To address this gap, we introduce MIOH, a fine-grained multi-image object hallucination benchmark that systematically evaluates object hallucination across four foundational tasks (existence, counting, attribute, position) through three multi-image reasoning patterns (comprehensive, comparative, selective) under three controlled adversarial pressures (visual context scale, perceptual difficulty, contextual bias). Through evaluation of 29 models, we reveal that even state-of-the-art systems like GPT-5 and Gemini-2.5-Pro exhibit distinct failure patterns across different reasoning patterns and tasks. Our evaluation reveals that hallucination stems not merely from perceptual failures but from integration-stage limitations when maintaining object representations across multiple images. MIOH provides a controlled framework for analyzing multi-image object hallucination and serves as a critical evaluation tool for developing more reliable multimodal AI systems.

---


### 353. [SwarmBench: Can Large Language Models Act as Agent Swarm Orchestrators?](https://arxiv.org/abs/2608.30661)

**<font color=#1a73e8>作者：</font>** Jinshan Gao, Zhuoran Jin, Tianyi Men 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model-based multi-agent systems are evolving from fixed interaction topologies toward dynamically orchestrated Agent Swarms. However, existing benchmarks are still largely based on single-agent or general-purpose agent tasks, making it difficult to systematically evaluate key orchestration capabilities. We propose SwarmBench, a benchmark that evaluates model performance from multiple perspectives, including accuracy, efficiency, cost, and process quality. Experimental results show that current models exhibit substantial differences in orchestration capability. These differences are reflected not only in final accuracy, efficiency, and cost, but also in the overall quality of the orchestration process itself. Based on these findings, we further propose SwarmExp, a simple yet effective method based on experience extraction and experience replay, which consistently improves the orchestration performance of large language models.

---


### 354. [MURANO: Design, Run, and Reproduce Mechanistic Interpretability Experiments as Composable Pipelines](https://arxiv.org/abs/2608.30662)

**<font color=#1a73e8>作者：</font>** Alireza Bayat Makou, Emirhan Böge, Phu Gia Hoang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper presents Murano, an open source framework for designing, running, and reproducing mechanistic interpretability studies of large language models, intended for researchers across disciplines. These studies often combine loading, recording, attribution, intervention, and evaluation, while existing libraries tend to focus on different parts of this workflow. As a result, researchers using several libraries may need to adapt outputs from one for use by another. To bridge this gap, Murano represents operations from these five areas as composable steps. Steps exchange named result artifacts and declare the inputs they require and the outputs they produce. A pipeline executes its steps in the order supplied, and Murano uses canonical addresses when component identities pass between operations. Murano builds on existing interpretability and machine learning libraries. We demonstrate Murano through two reproductions of established interpretability studies and one illustrative sparse autoencoder case study.

---


### 355. [HiRS-Agent: A Hierarchical Multi-Agent System for Reliable Long-Horizon Remote Sensing Task Solving](https://arxiv.org/abs/2608.30672)

**<font color=#1a73e8>作者：</font>** Boyang Mu, Zhiwei Wei, Mugen Peng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models and multimodal models have pushed remote sensing (RS) processing from simple perception models to agentic systems designed to tackle complex, long-horizon RS tasks. However, existing systems often rely on monolithic decision-making frameworks, which fail to accommodate the multi-stage, interdependent nature of RS tasks. This centralized approach leads to challenges such as unstable task execution, incorrect tool usage, and error propagation across stages. To address these issues, we propose HiRS-Agent, a hierarchical multi-agent system for long-horizon RS task solving. HiRS-Agent adopts a two-level collaborative architecture: the Manager Layer handles dynamic routing, step-level verification, replanning, and termination control, while the Specialist Layer organizes domain-specific tools according to the RS workflow and is responsible for subtask reasoning and tool execution. To further enhance the system's capability, we introduce a two-stage supervised tuning strategy and a verification-guided hierarchical reinforcement learning stage to jointly optimize coordination and tool-use policies. Experiments on Earth-Agent Benchmark and ThinkGeo show that HiRS-Agent substantially improves long-horizon tool-use capability and final-task correctness, demonstrating the effectiveness of structured multi-agent collaboration for reliable RS agents. The code is publicly available at this https URL.

---


### 356. [CoMPASS: Collaborative Molecular Property Prediction via Adaptive Small-Large Model Synergy](https://arxiv.org/abs/2608.30674)

**<font color=#1a73e8>作者：</font>** Wentao Li, Jiangjie Qiu, Yijun Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Accurate molecular property prediction requires both statistical reliability and chemical reasoning. Graph neural networks can be calibrated directly on labeled assays but remain limited by the coverage of their training data. Large language models (LLMs) can compare molecular evidence and articulate chemical rationales, yet are unreliable as standalone quantitative predictors. The central challenge is therefore to determine when an LLM should influence a calibrated model and by how much. Here we present CoMPASS, a retrieval-calibrated framework for small-large model collaboration. CoMPASS retains a graph attention network (GAT) as the predictive anchor, retrieves locally relevant training molecules, provides attention-grounded evidence to an LLM, and converts its proposal into a bounded correction through an agreement-aware gate. Across six classification and two regression benchmarks, CoMPASS improves the GAT anchor in regions of correctable uncertainty while limiting LLM intervention in high-confidence regimes. Ablations show that the gains arise from validation-calibrated retrieval and bounded fusion rather than prompting alone. These results suggest that generative reasoning should augment calibrated prediction through evidence-grounded, controlled corrections rather than direct output replacement. Code is available at this https URL.

---


### 357. [MedAgent-R1: Faithfulness-Aware Reinforcement Learning for Evidence-Grounded Medical Reasoning](https://arxiv.org/abs/2608.30676)

**<font color=#1a73e8>作者：</font>** Jiangwang Chen, Chenghao Zhang, Hengxing Cai  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> When medical AI systems hallucinate clinical reasoning, the consequences extend beyond incorrect answers: fabricated justifications that superficially reference retrieved evidence can mislead clinicians into unsafe treatment decisions. Medical reasoning agents must therefore produce not only correct answers but also faithful justifications that clinicians can verify against cited evidence. We identify a systematic failure mode in RL-trained retrieval agents: outcome-only rewards improve accuracy while degrading faithfulness, a phenomenon we term confident hallucination. The agent learns to answer from parametric memory and backfill plausible but unsupported justifications; citation fabrication rates rise from 16.5% to 31.8% even as accuracy improves by 5 points over the supervised baseline. We address this with a faithfulness-gated reward design: accuracy credit is conditioned on evidence grounding via a hard gate, complemented by retrieval validity and conciseness signals that close exploitation paths unique to agentic retrieval. The resulting system, MedAgent-R1, reduces citation fabrication from 31.8% to 4.7% and raises evidence completeness from 58.7 to 82.6 while maintaining 75.1% accuracy, with 13.2-point gains on HealthBench Safety. Under the same agentic retrieval setup, MedAgent-R1 outscores GPT-4o on faithfulness-specific dimensions (Factual Support 4.55 vs. 4.25; Overclaiming 4.40 vs. 4.15) while remaining below GPT-4o in overall accuracy, suggesting that explicit faithfulness training yields evidence-grounding gains not achieved by scaling alone.

---


### 358. [OCR-MetaReasoning Benchmark: Evaluating the Meta-Reasoning Ability of MLLMs in Text-Rich Image Understanding](https://arxiv.org/abs/2608.30678)

**<font color=#1a73e8>作者：</font>** Gengxu Li, Yuan Wu, Yi Chang  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Text-rich image understanding requires multimodal large language models (MLLMs) to organize OCR (Optical Character Recognition)-grounded evidence across words, layout, fields, charts, and visual correspondences. Existing evaluations often conflate extraction with reasoning and rarely test whether models follow the required reasoning direction: applying visible rules, abstracting hidden regularities, or recovering missing premises. We introduce OCR-MetaReasoning, a controlled single-image benchmark that treats deduction, induction, and abduction as distinct directions and separates final-answer correctness from reasoning-process compliance. The benchmark contains 1,500 verified samples in a balanced \(3\times5\) taxonomy crossing three reasoning types with five OCR-object categories, along with reference reasoning steps, automatic answer scoring, the Meta-Reasoning Macro Score (MRMS), and the Reasoning Process Compliance Score (RPCS). Experiments with representative closed-source and open-source MLLMs show that OCR-grounded meta-reasoning remains far from saturated: models struggle with visible-rule application and layout-sensitive inference, while process-compliant rationales can accompany incorrect final answers under exact-match evaluation. The code is available at this https URL.

---


### 359. [LCoT-GV: Graph Attention Networks for Verifying Long Reasoning Chains in Large Language Models](https://arxiv.org/abs/2608.30679)

**<font color=#1a73e8>作者：</font>** Bérénice Jaulmes, Mehwish Alam  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models produce Long Chains-of-Thought (LCoTs) which involve breaking down the problem into smaller reasoning steps before reaching the conclusion. However, these steps often contain contradictions, unsupported inferences, or irrelevant steps, even when the final answer is correct. We propose Long Chain-of-Thought Graph Verifier (LCoT-GV), a graph-based framework that represents LCoTs as reasoning graphs. Each node in the graph represents a reasoning step and the edges encode semantic and logical relations. A Graph Attention Network is then trained to predict chain-of-thought correctness from the reasoning graph. We construct a new graph-oriented verification dataset from multiple reasoning benchmarks for question answering in various domains. The results show that our method is competitive with the most similar approaches.

---


### 360. [WildSEEK: Evaluating Language Models for Information-Seeking](https://arxiv.org/abs/2608.30683)

**<font color=#1a73e8>作者：</font>** Tanise Ceron, Joachim Baumann, Elisa Bassignana 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Language models are increasingly mediating information access to end users, urging a systematic evaluation of their responses for a fair and reliable information ecosystem. Existing evaluations, however, are often topic-specific or synthetic, limiting their ability to capture the complexity of "in the wild" information-seeking queries and the risks present in model responses. To address this gap, we introduce WildSEEK, a manually annotated dataset of 3k information-seeking queries from real user interactions, and an evaluation framework for LLM-generated responses. WildSEEK includes annotations for risk-sensitive domains (e.g. health and financial information), and distinguishes factoid queries from analytical queries which seek responses beyond facts. We train classifiers on WildSEEK to analyze more than 1.8M realistic user queries. We find that over a third of information-seeking queries are high-risk and more often analytical. Our findings show that LLM responses fail more often in four criteria: sycophantic behavior, overreliance, a default US-centric perspective, and poor handling of vulnerable populations -- with failure rates being mostly higher for analytical queries. By providing methods to monitor the reliability, safety, and fairness of LLM behavior, our dataset and evaluation framework offer an empirical foundation for the broader question of how these systems should behave as they take on a growing role in information access.

---


### 361. [ATLAS: Dual-Horizon Diagnostic Evaluation for Industrial Tool-Use Agents](https://arxiv.org/abs/2608.30685)

**<font color=#1a73e8>作者：</font>** Wei Chen, Peilun Zhou, Zhaoyu Hu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly deployed in user-facing services that require iterative tool use under dynamic business conditions. Reliable evaluation is essential for sustained improvement: it must reveal capability deficiencies, inform priorities, and assess interventions. Yet industrial agent service unfolds both through the iterative trajectory of a current request and through continued user interaction. Final-outcome assessment can therefore obscure where deficiencies arise and whether later service remains aligned with context from earlier exchanges. We propose ATLAS, a dual-horizon diagnostic evaluation framework for industrial tool-use agents. At the request horizon, trajectory-wise diagnostic signals relate deficiencies to execution locations and capability concerns. At the interaction horizon, user-wise signals assess whether service remains responsive across continued interaction. Together, these views provide structured diagnostic evidence for analyzing execution deficiencies and sustained service behavior. ATLAS instantiates them as executable signals with explicit evidence scopes and decision boundaries. LLM judge interfaces are calibrated against high-confidence references from real business logs; when needed, their decision behavior is distilled into efficient diagnostic models for lower-latency, lower-cost evaluation. The resulting feedback supports policy optimization. We evaluate ATLAS on Meituan Xiaotuan production traffic. Offline experiments assess diagnostic-signal fidelity and replay-based policy improvement, while online A/B experiments show concurrent gains in user engagement, downstream business outcomes, and sampled human-audit quality.

---


### 362. [Inferring Value Criteria from Ordinal Preferences: An Iterative In-Context Learning Framework for Music Generation](https://arxiv.org/abs/2608.30694)

**<font color=#1a73e8>作者：</font>** Futa Hidaka, Naomi Imasato, Kazuki Miyazawa 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Adapting a generative music system to an individual's taste requires learning what that listener values. Listeners can rank pieces, but their underlying criteria may be tacit and difficult to articulate. We ask whether and under what conditions a large language model (LLM) can adapt symbolic music generation from rankings alone and construct transferable natural-language descriptions of value criteria. In our iterative in-context learning framework, the LLM formulates hypotheses, generates candidate pieces in ABC notation, receives a ranking, and periodically infers and verbalizes value criteria from history to guide later generation. We evaluate the framework against 16 simulated raters in 480 adaptation runs using mixed-effects modeling, an ablation, and transfer tests on unseen music. Overall, the framework did not outperform a feedback-free diverse-generation baseline, but did so for two value functions with targets difficult to reach through simple sampling. How atypical the target was relative to the LLM's feedback-free generation tendencies predicted adaptation difficulty. Moreover, higher value during adaptation did not imply identification of the criterion as a general rule. On unseen music, acquired descriptions and histories improved generation for more value functions than they improved preference prediction, which remained near chance. Some gains were associated with acoustic proximity to music in the context, but others were not. These findings show that rankings alone can guide generation under limited conditions, while transferable criterion inference remains constrained by the foundation model's ability to recognize, reason about, and verbalize musical attributes.

---


### 363. [An Agentic Retrobiosynthesis Framework with Learned Frontier Selection](https://arxiv.org/abs/2608.30702)

**<font color=#1a73e8>作者：</font>** Philippe Meyer, Guillaume Gricourt, Thomas Duigou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used as agents for multistep retrosynthesis, raising the question of how much their search policy contributes independently of the underlying reaction model. We investigate this question in a biological setting through rule-based retrobiosynthesis: a deterministic biochemical engine generates the same validated transitions for every method, searching for routes that terminate in metabolites available to an \emph{Escherichia coli} chassis, while the policy only selects which frontier molecule to expand next. Prompted and LoRA-tuned Qwen2.5-7B policies use a strict choice-only interface. The fine-tuned policy reaches $65\pm1$\% solve rate at 10 expansions on LASER versus 59\% for MCTS, and at 200 expansions reaches $78\pm1$\% versus 75\% on LASER, $88\pm3$\% versus 80\% on the RetroPath RL Golden benchmark, and $63\pm2$\% versus 45\% on the BioNavi-NP benchmark. Fine-tuning also consistently outperforms direct prompting. These results show that route-supervised frontier selection can improve budgeted search without altering biochemical generation, although performance remains dependent on frontier construction and reaction ranking.

---


### 364. [SingProbe Technical Report](https://arxiv.org/abs/2608.30703)

**<font color=#1a73e8>作者：</font>** Sing Team  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Runtime guardrails are essential for reliable large language model (LLM) deployment, yet existing approaches typically rely on independent, external models that introduce additional inference cost, delayed safety signals, and a capacity mismatch with increasingly capable base models. To address these issues, we introduce SingProbe, a lightweight intrinsic runtime guard that directly reuses hidden states produced during LLM inference and operates alongside autoregressive decoding. Within a unified framework, SingProbe continuously predicts query intent, response safety, and hallucination risk at the token level with negligible additional guardrail inference overhead, offering a "free-lunch" solution. We further introduce SingStreamBench, a benchmark designed to assess whether streaming guardrails remain inactive on benign prefixes while promptly detecting emerging unsafe content. Extensive experiments show that SingProbe achieves competitive or superior performance compared with substantially larger standalone guardrails and specialized hallucination detectors, with only $\approx$2M parameters and $<0.5\%$ extra overhead. Beyond passive detection, we also show that SingProbe scores can anticipate future generation risk and guide constrained safe decoding. We further extend this paradigm to medical generation through SingProbe-Med, which selectively activates risk-directed decoding interventions only when clinically relevant risks emerge. Together, these results demonstrate that internal model representations provide an effective and efficient interface for generation-time monitoring and control.

---


### 365. [TUE-Detector: A Tool-Using Expert MLLM-Based Detector for AI-Generated Videos](https://arxiv.org/abs/2608.30704)

**<font color=#1a73e8>作者：</font>** Yichen Wu, Haoxuan Qu, Yongxing Dai 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> AI-generated video detection, which aims to distinguish AI-generated videos from real ones, has recently received increasing research attention. To perform this task reliably, a key challenge lies in accurately identifying subtle-yet-measurable unnatural artifacts. In this work, we address this challenge from a novel perspective of tool-mediated evidence discovery and propose Tool-Using Expert MLLM-based AI-generated Video Detector (TUE-Detector), a novel framework for AI-generated video detection. TUE-Detector trains a general MLLM into a task-tailored tool-using expert detector that learns to invoke suitable tools, collect concrete evidence of unnaturalness, and reason over the evidence for reliable detection. Meanwhile, TUE-Detector further introduces novel designs to equip the expert detector with high-quality and suitable tools. Extensive experiments demonstrate the effectiveness of our framework.

---


### 366. [VisLens: Single-Pass Interpretable Visual Search for Multimodal LLMs](https://arxiv.org/abs/2608.30705)

**<font color=#1a73e8>作者：</font>** Jingyi He, Sanghwan Kim, Zeynep Akata  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models (MLLMs) struggle with fine-grained Visual Search, the task of locating small or rare objects in high-resolution images. Existing remedies fall into two families: (1) Training-free methods based on attention or confidence scores are accurate but slow, since they require multiple MLLM queries per example. (2) Reinforcement Learning (RL) trained tool-use models are faster at inference but opaque, since their tool calls remain uncontrollable and hard to interpret. To overcome this, we propose \emph{VisLens} (Visual Focus via Logit Lens), a Visual Search method built on the logit lens, which decodes the semantics held in a hidden state by projecting it through the LLM head. VisLens further uses a lightweight tuned-lens that maps early hidden states into the final hidden state space, so visual tokens can be read out from early layers. These tokens are matched to target words in the query to generate a crop of the relevant region, which is fed back in alongside the original image to produce the final answer. The whole process, from decoding to the final answer, completes in a single forward pass without repeated queries. VisLens matches or exceeds prior baselines while delivering a substantial latency advantage, running $8.5$--$9.9\times$ faster than Thyme and up to $22.2\times$ faster than training-free multi-pass search methods.

---


### 367. [GUIDE: Guiding Internal Evidence with Language Instructions](https://arxiv.org/abs/2608.30712)

**<font color=#1a73e8>作者：</font>** Soyeon Caren Han, Hyunsuk Chung, Jinwoo Kim 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large multimodal models follow instructions about what to generate, but not necessarily about what evidence to rely on. Hence, models may continue to depend on shortcut-associated cues even when instructions suggest otherwise. We introduce GUIDE, a framework for controlling internal evidence usage through language instructions. GUIDE combines grouped parameter-efficient adaptation with instruction-conditioned gating to modulate multimodal evidence pathways during reasoning and generation. We further introduce a pathway-level evaluation framework that characterizes instruction-conditioned evidence modulation through reliance sensitivity, controlled perturbation analysis, pathway modulation, and autoregressive decoding dynamics. Across multimodal reasoning, classification, and generation, GUIDE induces structured and instruction-aligned redistribution of evidence reliance while largely preserving task behavior. Experiments on GQA, TextVQA, MM-IMDb, CREMA-D, RAVDESS, and Flickr30K show that GUIDE improves robustness under targeted evidence perturbations and enables controllable modulation across diverse multimodal settings. This suggests that multimodal instruction following can extend beyond output control toward regulating how different evidence sources contribute to model predictions.

---


### 368. [SocialReasonBench: A Video-QA Benchmark for Social Reasoning with Counterfactual Narrative Videos](https://arxiv.org/abs/2608.30716)

**<font color=#1a73e8>作者：</font>** Zheyu Huang, Zijing Shi, Haozhe Luo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent advances in Large Multimodal Models (LMMs) have greatly improved video understanding, yet their ability to reason about human-centered social situations remains limited. Existing benchmarks typically rely on videos with a single observed trajectory, making it difficult to determine whether models truly understand social dynamics or merely exploit recurring narrative patterns. We introduce SocialReasonBench, a video multiple-choice QA benchmark for evaluating socially grounded reasoning in scenarios derived from interactive narratives. Built from gameplay videos of Detroit: Become Human, the benchmark leverages branching storylines where player decisions lead to alternative social outcomes that can be checked against the game's own script, flowchart, and recorded branches. We develop a multi-agent curation pipeline that localizes socially meaningful clips, grounds answer labels in game-state signals, and generates theory-guided questions with diagnostic distractors. SocialReasonBench covers seven reasoning dimensions, including intent recognition, emotional empathy, moral dilemma, counterfactual reasoning, and causal antecedent. Experiments on contemporary LMMs show that models perform reasonably well on basic social understanding but struggle with counterfactual and causal reasoning. Further ablation and diagnostic error analyses reveal that models often depend on incomplete modality cues and fall into reasoning traps such as visual shortcuts, highlighting a gap between observable event recognition and deeper reasoning over latent social states.

---


### 369. [Tracing distinguishability through transformer processing with stochastic LayerNorm](https://arxiv.org/abs/2608.30720)

**<font color=#1a73e8>作者：</font>** Kieran Murphy  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Representational similarity is foundational to analyses of deep networks, yet distances between point-valued representations are not intrinsically tied to downstream function: nearby states may produce different behaviors, while distant states may behave similarly. We instead give representations volume, turning similarity into statistical distinguishability. Overlapping stochastic representations necessarily induce overlapping downstream distributions, grounding latent comparison in model function and bringing it under information-theoretic tools such as the data-processing inequality. We realize this idea in pretrained transformers through a light-touch modification to LayerNorm: at each residual-stream read, we normalize the state, add isotropic Gaussian noise, and renormalize. During distillation fine-tuning, one learned allocation parameter per residual-stream read distributes a fixed global rate budget across the processing stack. The resulting model can be viewed as transformer blocks reading the residual stream with learned finite precision under a shared global rate budget. Using the Bhattacharyya coefficient, we trace which counterfactual distinctions are preserved through MLP blocks or selectively exposed to the query, key, and value computations of individual attention heads. Experiments on ViT-S and GPT-2 small reveal the depthwise propagation of continuous visual perturbations and head-specific sensitivity to token distinctions aligned with known attention motifs. These results establish distinguishability as a functionally grounded lens on transformer computation that complements existing interpretability approaches.

---


### 370. [BAITBENCH: Measuring Agent Reward Hacking with Optional Shortcuts Planted in ML Tasks](https://arxiv.org/abs/2608.30724)

**<font color=#1a73e8>作者：</font>** Pradyumna Shyama Prasad, Meiri Anto, Leon Eshuijs 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM agents are increasingly used to run autonomous ML experiments, iterating on target metrics with little human oversight. Prior work has documented reward hacking in these environments, bringing into question the validity of produced research and the broader safety case for AI R&D. Existing benchmarks do not measure exploits that live in the data or the modeling task itself. We introduce BAITBENCH, a suite of three synthetic tabular ML tasks that each contain a shortcut that allows agents to inflate the public test score but fail on a hidden test set. Since the shortcut is optional and using it breaks no stated rule, BAITBENCH measures how often models exploit the shortcut to achieve inflated scores. Across seven frontier agents scored by our two-stage judge pipeline, 57.1% of runs exhibit reward hacking, with five of seven above 50%. Agents cheat even under a second condition where they are prompted not to -the mean cheating rate remains above 50%. We release BAITBENCH, along with the judge implementation, and an annotated dataset of transcripts containing reward hacks as a testbed for evaluating reward-hacking mitigations head-to-head.

---


### 371. [E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation](https://arxiv.org/abs/2608.30730)

**<font color=#1a73e8>作者：</font>** Wei Fan, Xinjie Shen, Xudong Guo 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Long-horizon agentic tasks go beyond chaining short tasks over more interaction turns. Their evolving dynamic environments and long-range dependencies require Large Language Models (LLMs) to continually explore, learn from experience, and adapt their policies over thousands of steps. We introduce E-Commerce Bench, the first open-source benchmark that integrates multi-round counterpart negotiation and dynamic events into a year-long business operation. Over a 365-day year, an LLM agent concurrently runs multiple online stores, researching the market, negotiating with suppliers to source inventory, optimizing sales strategies, fulfilling orders, handling returns, and managing cash flow to maximize its end-of-year total assets. To construct a realistic merchant-side operating environment, the product and supplier data are derived from a real e-commerce platform, while a year-long calendar of promotions, natural disasters, and supply-chain shocks continually reshapes demand. For reproducibility, both sides of the market are deterministic: customer purchases and returns follow a fixed demand model, while a negotiation kernel determines supplier pricing, concessions, and decisions, with an LLM used only to verbalize them. We evaluate 18 frontier models across seven dimensions, including year-end assets, and find that no single model dominates. GPT-5.6 Sol earns the most, growing the 100,000 opening stake into 1,431,425, yet it ranks 16th of 18 on fraud avoidance and trails Fable5 in operational efficiency. Among open-weight models, Qwen3.8-Max-Preview leads with 416,252, 38% above GLM 5.2 (high), and achieves the strongest learning over the horizon, progressively bargaining down prices across repeated orders. Our code is available at this https URL.

---


### 372. [Calibrating Small Language Models for Claim Check-Worthiness Detection](https://arxiv.org/abs/2608.30731)

**<font color=#1a73e8>作者：</font>** Pratuat Amatya, Venktesh Viswanathan, Vinay Setty  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Assessing claim check-worthiness is an essential first step in automated fact-checking pipelines. This work is motivated by a real deployment challenge at an early-stage startup: running large language models (LLMs) over every incoming claim is cost- and latency-prohibitive, yet smaller models sacrifice accuracy. We propose NN-PPI, a pointwise extension of Prediction-Powered Inference (PPI) that calibrates model predictions at inference time as a lightweight post-hoc layer, without re-training the underlying model. NN-PPI achieves weighted F1 gains ranging from 12% to 33.80% depending on the size and performance of the baseline model, bringing SLMs on par with larger LLMs. Beyond few-shot SLMs, NN-PPI further improves a production-deployed fine-tuned model, demonstrating that residual calibration is complementary to supervised fine-tuning. By recovering LLM-level accuracy from models that are an order of magnitude cheaper to serve, it makes accurate check-worthiness detection substantially cheaper to operate at scale. Our code and data can be found at this https URL.

---


### 373. [Do VLMs Share Safety Neurons Across Modalities?](https://arxiv.org/abs/2608.30750)

**<font color=#1a73e8>作者：</font>** Jiaxuan Li, Jiahao Zhang, Duc Minh Vo 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) can comply with harmful requests delivered through images, even when their LLM backbones would refuse the same content in text. While prior work characterizes these jailbreaks empirically or at the representation level, how visual inputs perturb safety pathways at the neuron level remains uncharted. We close this gap with a causal, neuron-level analysis of safety mechanisms in 10 VLMs. We propose a two-stage detection pipeline with iterative ablation that accounts for self-repair, and introduce two modality-isolated benchmarks, ViSafe-Detect and ViSafe-Eval, which decouple visual and textual safety signals.
Our analysis reveals: (i) Text safety in VLMs is localizable: $\sim$88 neurons ($<$0.01%) whose targeted ablation substantially reduces refusal. (ii) Text safety neurons constitute the dominant refusal pathway: ablating them is the only intervention that consistently and substantially reduces refusal across all models. (iii) Visual safety is high-dimensional and diffuse at the single-neuron level: text safety concentrates in $\sim$5 subspace directions while visual safety requires $\geq$50. This gap holds across architectures, explaining why current alignment has not closed the visual safety gap. Project page is at: this https URL
Warning: this paper may include examples of harmful content.

---


### 374. [Autoregressive Mosaics: Probing 2D Spatial Reasoning in Text-Only Language Models](https://arxiv.org/abs/2608.30751)

**<font color=#1a73e8>作者：</font>** Ashwin Nedungadi, Stefan Oehmcke, Stefan Lüdtke  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) trained only on text and code can sometimes generate programs that draw recognizable images. However, it is unclear whether this reflects an internal representation of 2D spatial layout or simply the ability to translate spatial descriptions into code. We introduce Autoregressive Mosaics (AM-Bench), a benchmark that separates these factors: First, a translation task gives a model a fully specified geometry of a picture in words as a prompt and asks for the code that produces it. Second, a layout task requires the model to compose an image from an underspecified prompt. Across eight open-weight text-and-code-only models, all models reliably translate specified geometry into code, but their open-ended layout performance differs substantially, indicating that these differences are not explained by code-generation ability alone. An output-medium ablation further shows that the interface or medium of expression that the model uses matters: replacing procedural code with raw SVG improves layout scores across all models. Finally, probing model activations shows that a coarse layout plan is present before generation, but reflects only the layout implied by the prompt. During generation, models track the evolving geometric state instead of executing an initially fixed plan. Overall, these results show that 2D spatial performance in text-only LLMs depends on both the model and the output medium, and is not explained by code-generation ability alone.

---


### 375. [CLIN: an Objective Framework for Evaluating Creativity in Short Persian Literary Text](https://arxiv.org/abs/2608.30754)

**<font color=#1a73e8>作者：</font>** Mohammad Reza Modarres, Armin Tourajmehr, Yadollah Yaghoobzadeh 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Evaluating creativity in large language model (LLM) outputs remains challenging because creativity is multidimensional and human-centered. We examine how reliably LLMs evaluate short literary text in Persian, a low-resource language, across multiple evaluation strategies and prompt formulations. We find that LLM-human agreement varies substantially across dimensions: alignment is stronger for structured TTCT-derived properties such as Originality, Fluency, and Elaboration, but considerably weaker for more subjective dimensions, particularly Emotion and Attractiveness. Judgments are also sensitive to prompt formulation, while few-shot prompting, ensembling, and multi-agent debate provide no consistent improvement. Motivated by this dimension-dependent behavior, we investigate whether structured creativity dimensions can instead be approximated using simple, interpretable proxy metrics. We introduce CLIN, which evaluates three TTCT-derived dimensions separately using topic-aware novelty for Originality, contextual lexical clustering for Fluency, and lexical diversity for Elaboration. These proxies achieve human alignment comparable to or better than the strongest zero-shot LLM judge in our setting while requiring substantially lower evaluation cost.

---


### 376. [CheXGround: Anatomical Region Tokens for Grounded Longitudinal Chest X-ray Interpretation](https://arxiv.org/abs/2608.30758)

**<font color=#1a73e8>作者：</font>** Adonay Demewez Gebremedhin, Wessam Shehieb, Sara Alansari 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent radiology multi-modal language models have made substantial progress in chest X-ray report generation, visual question answering, and temporal reasoning. While longitudinal chest X-ray interpretation compares sequential examinations to describe change, visual grounding aims to connect clinical language with localized image evidence. Although longitudinal modeling and visual grounding have each advanced radiology language models, how localized visual evidence can support longitudinal interpretation remains under-explored. We introduce CheXGround, a region-grounded longitudinal chest X-ray language model that represents paired studies through corresponding anatomical regions. CheXGround extracts anatomical regions from current and prior radiographs, encodes them as temporally enhanced Region-of-Interest (ROI) tokens, and combines them with global temporal image context during generation. To connect these region tokens with clinical text, we propose Temporal Region--Phrase Alignment, a pretraining objective that aligns temporal anatomical representations with localized report phrases. We evaluate CheXGround on single-study and longitudinal Visual Question Answering (VQA), longitudinal findings generation, temporal grounded VQA, and anatomical grounding. Across these tasks, CheXGround improves clinical language quality, temporal reasoning, and localization accuracy over recent baselines. Our results suggest that organizing longitudinal evidence at the anatomical level is a strong representation for grounded radiology language modeling. Project page: this https URL

---


### 377. [PRACTICE: From Experience to Expertise in Self-Evolving Embodied Agents](https://arxiv.org/abs/2608.30760)

**<font color=#1a73e8>作者：</font>** Ziyi Bai, Siqi Li, Tinglei Huang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent studies have shown that multimodal large language models (MLLMs) can serve as embodied agents, translating language instructions and visual observations into executable plans. However, building agents that can continually improve through interaction and rapidly adapt to their environments remains challenging. Summing up experience from past interaction trajectories provides a promising solution, but existing experience-based methods often rely on manually designed prompting workflows to extract and update skills. Such fixed procedures may struggle to learn updated skills from new and diverse experiences. We introduce PRACTICE, which trains a skill learner to discover and maintain a persistent skill library from past interaction trajectories while keeping the task executor frozen. Given the historical accumulated skills and incoming trajectories, the skill learner produces structured batch-edits that add, refine, merge, or remove skills, and then hierarchical consolidate all collected edits into a consistent updated skill library. We train the learner with a two-stage curriculum. First, it learns basic skill generation and library maintenance from oracle trajectories. Then, by contrasting successful and failed trajectories from heterogeneous executors on the same tasks, it learn to identify invalid action patterns and recovery strategies. Finally, we apply online skill-edit distillation to align the skill learner with a stronger teacher on its current edit distribution to further improves the policy. Experiments demonstrate that a compact skill learner delivers consistent performance improvements across successive library-update rounds for multiple frozen executors. On EB-ALFRED and EB-Habitat, PRACTICE further outperforms the strongest experience-based baselines. Project resources are publicly available at: this https URL

---


### 378. [TrainSDC: Characterizing and Mitigating Silent Data Corruption in Large Language Model Training](https://arxiv.org/abs/2608.30769)

**<font color=#1a73e8>作者：</font>** Zhipeng Xia, Haotian Xu, Siyu Yun 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> LLM training is increasingly vulnerable to silent data corruption (SDC), yet existing protection methods largely treat Transformer computations uniformly because their vulnerability remains poorly understood. We present the first systematic characterization of SDC vulnerability across major computation interfaces in both the forward and backward passes of Transformer training. Our analysis reveals two distinct error propagation mechanisms: forward-pass vulnerability is highly location dependent, with faults on the Q/K path producing persistent training deviations, whereas backward-pass vulnerability is largely governed by gradient exponent distributions rather than computation locations. Motivated by these observations, we propose TrainSDC, a characterization-guided protection framework consisting of Q/K-path recomputation, residual-gain monitoring, and exponent-aware gradient scaling. Experiments on Llama 3.2-1B and Qwen3-0.6B show that TrainSDC maintains training behavior close to fault-free execution under both sparse and dense fault injection while introducing only 1.65%-6.76% runtime overhead.

---


### 379. [SkillZip Pro: Execution-Aware Dynamic Compression of Progressively Loaded Skills for Self-Evolving Agents](https://arxiv.org/abs/2608.30785)

**<font color=#1a73e8>作者：</font>** Xiaofan Bai, Chao Liu, Hongqiang Lin 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Production agent skills are directory bundles, not isolated prompts. The root is loaded at activation; references, schemas, scripts, assets, and nested subskills are loaded only when an execution path needs them. Compressing only the root misses most deployment cost and may move branch-specific details into the always-loaded context. Flattening instead destroys progressive-loading boundaries.
We introduce \method, an evaluation-free compressor for complete, progressively loaded skill bundles. It leaves the agent harness unchanged and emits an ordinary directory. The method combines two safeguards. First, it compresses \emph{across files}, removing content from a reference or subskill when the root or a declared environment contract already provides it. Second, it preserves routing, so every required file and directly callable entry remains reachable after rewriting. Users can configure \method along two independent axes. \emph{One-Shot} mode rebuilds the full bundle; \emph{Continual} mode reuses state and applies Zip-on-Write after each evolution patch. \emph{Persistent} compression rewrites the shipped bundle to reduce storage and runtime context. \emph{Transient} compression keeps that bundle byte-identical and builds a task-specific view, reducing only per-run context after build cost. Entry contracts mark private, public, and conditional resources; a multi-entry audit preserves standalone public subskills.
On a production content-moderation skill evaluated by our industrial multi-round harness, \method removes \hl{38\%} of skill bundle tokens and \hl{10.4\%} of end-to-end per-run tokens with no quality loss, while an unprotected 71\% configuration loses up to 26 accuracy points to one-sided false positives. On a multi-entry bundle, \method effeciently reduces token cost while near-perfectly preserving every route and public entry.

---


### 380. [TopoCompress: Long Context Compression via Graph-Wired Semantic Trajectories](https://arxiv.org/abs/2608.30811)

**<font color=#1a73e8>作者：</font>** Daniel Agyei Asante, Yang Li  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Long-context compression is essential for reducing the cost and latency of large language model inference. However, existing methods can fragment important evidence, require additional training or alignment, and often depend on the target model for effective compression. We introduce TopoCompress, a training-free and model-agnostic framework that compresses long contexts by selecting coherent semantic spans. TopoCompress first scores each span using dense and lexical query relevance together with semantic acceleration. It then constructs a hybrid graph that connects spans based on semantic similarity and sequential adjacency, and propagates the query-guided relevance scores over the graph. Across five long-context tasks-HotpotQA, 2WikiMQA, MuSiQue, Qasper, and MultiFieldQA-en-TopoCompress consistently outperforms strong compression baselines. Notably, TopoCompress achieves performance comparable to the strongest baseline while using a 4x smaller compression budget, and provides a 1.41x smaller compression time over the fastest baseline.

---


### 381. [Lucida: Parse, Generate, and Place for Composable Real-to-Sim Scene Modeling](https://arxiv.org/abs/2608.30821)

**<font color=#1a73e8>作者：</font>** Minghan Qin, Yuang Wang, Xiuyu Yang 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Composable scene modeling aims to recover a real indoor scene as complete, editable object assets arranged as observed, giving robot simulation and embodied AI a simulation-ready replica of the real environment whose objects can be manipulated individually. Existing pipelines decompose the task into three steps---parse the observations into instances, generate an asset for each, and place each asset back---but every step presumes an input that a cluttered capture rarely provides: accurate instance geometry, unoccluded views, and assets that accurately match the observations. We propose Lucida, which keeps this order but redistributes the requirements, so each step consumes only what a real capture reliably provides and precision is reached at the end of the pipeline rather than demanded at its start. Lucida parses the video into a scene graph whose nodes carry per-instance multi-view evidence, generates a complete asset for each instance from its evidence, and places assets with GizmoAct, a VLM policy that casts placement as multi-turn GUI interaction, manipulating the object's gizmo in a closed loop and deciding itself when alignment is reached. Across scene-level 3D object detection, object pose estimation, and scene reconstruction, Lucida improves mAP over Boxer by 69% on R2S-Scene, raises ADD-SB@0.05 from 57.8% to 83.4% on CA-1M, and increases scene F-Score from 0.794 for SAM3D to 0.924.

---


### 382. [Error-Type-Aware Loss Reweighting for Robust Named Entity Recognition with Noisy LLM Labels](https://arxiv.org/abs/2608.30827)

**<font color=#1a73e8>作者：</font>** Elena Merdjanovska, Jonas Golde, Alan Akbik  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly used to annotate datasets for training smaller, task-specialized models such as named entity recognition. While this method yields effective models, it assumes that the synthetic dataset is correctly annotated. In this work, we find that (i) current fine-tuning processes simply ignore LLM-introduced annotation noise, resulting in degraded performance and (ii) existing noise-robust losses are not transferable to sequence labeling because annotation noise in named entity recognition is heterogeneous: for example, missing mentions and type errors affect the training signal in different ways. Treating all noisy tokens equally in noise-robust losses and applying a single reweighing criterion for all may therefore remove useful supervision or reinforce incorrect labels. To address this limitation, we propose error-type-aware loss reweighting for NER, which introduces separate reweighing rules for different types of potentially erroneous tokens. Our approach is simple and efficient, does not require additional training resources, and improves F1 by 0.8 - 2.0 percentage points on dataset-level average for noise levels between 15% and 40%, with a maximum improvement of 4.6 percentage points with 24.1% noise on Wikigold.

---


### 383. [HSRM: Hidden-State Reward Models for Test-Time Verification](https://arxiv.org/abs/2608.30841)

**<font color=#1a73e8>作者：</font>** Xianzhi Li, Xiaodan Zhu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models can often generate plausible mathematical reasoning traces, but reliably identifying the correct solution among multiple candidates remains a key challenge. Existing test-time reasoning pipelines typically rely on text-based verifiers that re-read each generated solution, making verification an expensive component of inference. Prior work has shown, however, that LLMs often encode correctness-related signals in their internal representations, including awareness of when their own answers are likely to be wrong. Building on this observation, we introduce HSRM, a lightweight hidden-state reward model that verifies candidate solutions by directly reading the generator's internal representations rather than re-processing its text. HSRM extracts hidden states from a frozen generator at reasoning-step boundaries and uses a small Transformer encoder to rank candidates. It is trained from self-generated trajectories with outcome labels, requiring neither human-written process supervision nor a large pretrained verifier. Across four mathematical reasoning benchmarks, HSRM matches or outperforms a 55M-parameter text-only energy verifier in 15 of 16 generator--dataset settings while using only about 2M parameters, providing an efficient alternative to text-only verification by reusing representations already computed during generation.

---


### 384. [Thesis Proposal: Toward a Human-Centered and Perspective-Aware Framework for Reproducible ML Evaluation and AI Alignment](https://arxiv.org/abs/2608.30842)

**<font color=#1a73e8>作者：</font>** Deepak Pandita, Christopher M. Homan  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Humans play a vital role at every stage of AI development, from data collection and curation to model development and evaluation. However, humans often disagree with each other and sometimes with themselves over time. It is essential to take disagreement into account when building human-centered AI systems, especially in domains where it is prevalent, such as AI safety, content moderation, or sentiment analysis. Disagreement often arises from subjective human opinion and can vary with one's identity, beliefs, and social environment. Despite this, current LLM evaluation approaches frequently rely on aggregating labels (often via plurality voting) to represent consensus, thereby obscuring minority perspectives. By failing to account for human disagreement, these evaluation methods contribute to the reproducibility crisis in AI. Human feedback is also crucial for ensuring that AI systems align with human values. For these systems to be trustworthy, it is critical to ensure that they reflect diverse human values and perspectives. In this thesis proposal, we present a human-centered and perspective-aware framework for reproducible ML evaluation and AI alignment.

---


### 385. [You Shouldn't Have Asked: A Pragmatics-Inspired Taxonomy for Evaluating LLM Refusals](https://arxiv.org/abs/2608.30856)

**<font color=#1a73e8>作者：</font>** Ruoxuan Li, Pinqiao Wang, Sheng Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Refusals are often treated as face-threatening acts in pragmatics because they can challenge the requester's socially claimed self-image. Large language models (LLMs) are increasingly trained to refuse unsafe and inappropriate requests, and these refusals may harm users when models fail to manage this interactional cost properly. While existing work has mainly approached LLM non-compliance as a safety-alignment outcome, it does not provide a way to evaluate whether LLMs refuse appropriately across different harmful contexts. To study this question, we propose (to our knowledge) the first taxonomy of LLM refusals that is grounded in pragmatic theory. Applying this taxonomy to responses from 16 modern LLMs across 14 harm categories, we find that although models differ in how they refuse, their refusals are overall explicit and strongly morally evaluative, with interactional repair occurring mainly through offering or providing safer alternatives instead of interpersonal facework. This pattern is especially consequential in sensitive harm contexts, where overuse of negative framing may make users feel shamed or provoked, undermining the purpose of safe non-compliance. We therefore call for alignment evaluation that considers not only whether models refuse harmful requests, but also whether they refuse in ways that are contextually adaptive and socially accountable for the interactional consequences of saying no.

---


### 386. [Personas Differ from Native-Language Generation: Language Pathways Shape LLM Interpersonal Advice](https://arxiv.org/abs/2608.30873)

**<font color=#1a73e8>作者：</font>** Jinhee Won, Xinlan Emily Hu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly used for interpersonal advice and as tools for studying social behavior across languages and cultures. A common shortcut for eliciting language- or culture-related variation is to ask a model to answer as a native speaker. We test whether this native-speaker persona reproduces the outputs obtained when models instead generate advice in the target language and translate the response back into English. Using 600 interpersonal advice questions across 13 languages and eight LLMs, we compare native-language generation followed by translation (NL) with native-speaker persona prompting (NP), measuring linguistic style, behavioral scaffolding, and forced-choice action recommendations. We find that NP and NL are not interchangeable. Compared to NL, NP often increases lexical social cues, including affiliation and positive tone, while reducing qualities such as concreteness and social attunement; NP also provides less actionable scaffolding in open-ended advice. In forced-choice scenarios, NP changes which action the model selects, favoring confrontation over redirection, with effect sizes varying across languages, topics, and models. Our results show that cross-lingual elicitation strategy is a consequential methodological choice that can change both how advice is framed and which actions models recommend.

---


### 387. [Deploying DeepSeek 175B Locally on a Single Consumer-Grade RTX 4060 Laptop with 32GB RAM for 200k-Scale Protein-Ligand Virtual Screening](https://arxiv.org/abs/2608.30877)

**<font color=#1a73e8>作者：</font>** Rui Xiao, Yili Xu  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Recent advances in large language models (LLMs) have demonstrated exceptional performance in protein-ligand interaction prediction, but state-of-the-art pipelines for large-scale virtual screening almost exclusively rely on high-end GPU clusters with hundreds of gigabytes of memory, creating prohibitive hardware barriers for small academic teams. In this work, we present a fully local low-resource framework that deploys the 175-billion-parameter DeepSeek 175B LLM on a single consumer-grade RTX 4060 laptop equipped with 32GB system RAM and 8GB VRAM, completing a full 200k-scale protein-ligand virtual screening workflow across 20 distinct protein targets. Our implementation achieves 100x throughput of an 8-card A100 cluster baseline under identical task configurations within 72 hours, with an average binding affinity prediction error of 0.88 kcal/mol across all targets, satisfying the 1.0 kcal/mol chemical accuracy requirement for preclinical drug discovery. Systematic runtime profiling reveals that heterogeneous memory management overhead accounts for 72% of total execution time, while accuracy loss introduced by model optimization contributes less than 10% to total prediction error. This work validates the engineering feasibility of running industrial-scale trillion-parameter LLM-driven biomedical computing tasks on consumer hardware, establishing a new low-barrier paradigm for AI-powered early stage drug discovery.

---


### 388. [Evaluating and Mitigating Anti-LGBTQ Biases in German and Multilingual Language Models](https://arxiv.org/abs/2608.30884)

**<font color=#1a73e8>作者：</font>** Melina Morch, Daniel Braun  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> While gender and racial biases in language models have been widely studied, anti-LGBTQ biases remain underexplored, particularly beyond English. Existing benchmarks often do not capture cultural and linguistic variation and rely on gender representations. This paper introduces a multilingual German-English benchmark dataset for the evaluation of anti-LGBTQ biases in language models. It combines community-sourced stereotypes from German-speaking queer individuals with a German translation of WinoQueer. The data is used to evaluate eight language models across sizes and architectures and explore mitigation through fine-tuning on community and progressive media content. Results show that language models reproduce anti-queer stereotypes, with variation across identities and models. Differences between the translated and community-based data highlight the importance of cultural adaptation for multilingual bias evaluation. Fine-tuning reduces bias on average, but not consistently across models and identities. Warning: This text contains examples of anti-queer hateful language and stereotypes.

---


### 389. [ECGQuest: Benchmarking and Fine-Tuning Language Models for Electrocardiography](https://arxiv.org/abs/2608.30893)

**<font color=#1a73e8>作者：</font>** Mohammadsina Hassannia, Matthew A. Reyna, Reza Sameni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Electrocardiogram (ECG) interpretation requires knowledge of cardiology, electrophysiology, clinical diagnosis, ECG waveforms, signal acquisition, and instrumentation. Existing language-model benchmarks, however, primarily assess broad medical knowledge or interpretation of individual ECG signals and images rather than the broader contextual knowledge required for ECG interpretation. We developed ECGQuest, a literature-grounded resource for evaluating and fine-tuning ECG-specific language models. A GPT-4o-based pipeline generated questions from 23 ECG references and Computing in Cardiology proceedings from 2003-2025. The final dataset contains 10,904 unique True/False questions paired with their negated forms (21,808 Q&A pairs). We evaluated three commercial and 20 open-source language models on a held-out test set in a zero-shot setting. Five open-source models with 7-14B parameters were fine-tuned using Low-Rank Adaptation, with BERT and BiomedBERT included as supervised encoder baselines. Generalization was assessed on ECG-related subsets of MedMCQA and MedQA converted to binary True/False questions using official answer keys. Zero-shot accuracy on ECGQuest ranged from 49.5% to 74.4%, with GPT-5 performing best. General-purpose models outperformed medically specialized models, several models showed strong True/False bias, and encoder baselines performed near chance. Fine-tuning improved all open-source models by 6.5-14.1%. Fine-tuned DeepSeek-R1-Distill-Qwen-14B reached 76.3% accuracy, while a five-model voting ensemble reached 78.5%. On MedMCQA and MedQA, fine-tuning mainly benefited weaker or class-biased models and did not consistently improve strong base models. ECGQuest provides a reproducible benchmark for contextual ECG knowledge and shows that parameter-efficient fine-tuning can make smaller language models competitive with substantially larger commercial models.

---


### 390. [Low-Resource Preference Adaptation of LLMs via Activation-Based Label Propagation](https://arxiv.org/abs/2608.30902)

**<font color=#1a73e8>作者：</font>** Alessio Galatolo, Meriem Beloucif  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Adapting large language models to user-specific preferences is often constrained by the cost of human annotation, making preference optimisation impractical in low-resource settings where preferences cannot be reliably labelled by LLMs themselves, e.g., due to cultural, subjective, or personalised contexts. In this paper, we investigate how language models encode preference information in their intermediate representations, finding that activations from chosen and rejected responses form distinct clusters across layers, even in pretrained models. Strikingly, this structure is strengthened by alignment on canonical datasets but erased when the target preferences differ from those the model was aligned on, suggesting aligned LLMs are poor judges for non-mainstream populations. Exploiting this structure, we propose training a lightweight linear probe on a few labelled preference pairs ($\leq$500) and using it to annotate large unlabelled datasets (50K+) for downstream preference optimisation. We systematically evaluate this approach across different datasets, preference optimisation methods and model scales and find that our method consistently outperforms direct training given the same annotation budget, and remains competitive against baselines trained on $50-100\times$ more labelled data in the majority of our settings. Code is available at this https URL.

---


### 391. [MMDS-Bench: Benchmarking Multimodal Large Language Models on Dynamic Stance in Social Media Interactions](https://arxiv.org/abs/2608.30903)

**<font color=#1a73e8>作者：</font>** Yuzhe Ding, Kang He, Li Zheng 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dynamic stance classification models how a reply responds to its direct parent message, rather than how a post relates to a fixed topic. Existing work has mainly studied this problem in text-only settings, while social media interactions increasingly rely on images, screenshots, memes, reaction images, and cross-modal references. We introduce MMDS-Bench, a diagnostic benchmark for multimodal dynamic stance classification in social media parent-reply interactions. MMDS-Bench contains 3,482 multimodal instances annotated with a seven-label dynamic stance taxonomy, together with an 800-instance diagnostic subset that requires structured reasoning over parent understanding, reply understanding, and stance-relation inference. We further annotate each instance with five challenge factors covering multimodal fusion, parent framing, non-literal expression, interaction reasoning, and label-boundary ambiguity. We evaluate 12 closed-source and open-source multimodal large language models and propose a reference-grounded LLM-judge protocol for assessing reasoning quality. Results show that current MLLMs still struggle with multimodal dynamic stance understanding, especially in cases that require relational inference beyond separate parent and reply comprehension.

---


### 392. [S3C-LLM: Skill-Code Guided Agentic Language Models for Spectrum-to-Structure Elucidation](https://arxiv.org/abs/2608.30910)

**<font color=#1a73e8>作者：</font>** Xuanle Zhao, Xinyuan Cai, Xiang Cheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Spectroscopic structure elucidation is central to molecular analysis, but recent Large Language Model (LLM)-based methods mostly formulate it as direct spectrum-to-SMILES generation. Although this paradigm can leverage paired spectral data, it does not explicitly model the analytical workflow used by spectroscopists, such as diagnostic peak interpretation, fragment reasoning, formula constraints, and chemical consistency checking. In this paper, we introduce S3C-LLM, a skill-guided and code-grounded agentic LLM for spectrum-to-structure elucidation. Rather than directly predicting a molecule, S3C-LLM retrieves modality-specific spectroscopy skills, executes analysis code to instantiate these skills on the input spectra, and integrates the resulting peak-level evidence and formula constraints before generating SMILES. Specifically, we contribute a self-evolving spectroscopy skill library, a thinking-augmented skill-code trajectory construction pipeline, and a two-stage training strategy that teaches Qwen3-4B through supervised fine-tuning (SFT) followed by our proposed step-level reinforcement learning (RL). Experiments on diverse benchmarks show that S3C-LLM consistently outperforms current general LLMs and spectrum-specific models across spectra, while using less than 1/10th of SpectraLLM's training corpus.

---


### 393. [CARVE: Verified Expansion for Variable-Length Generation in Diffusion Language Models](https://arxiv.org/abs/2608.30922)

**<font color=#1a73e8>作者：</font>** Wail Bouhedja, Amr Mohamed, Guokan Shang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models predict tokens from a partially observed response canvas, enabling bidirectional conditioning and parallel token refinement. Yet standard masked-diffusion decoders use a rigid inference interface: the number of masked positions allocated to the answer is fixed before generation begins. Choosing this length is difficult. A short canvas can truncate reasoning or code, while a long canvas wastes computation and can perturb denoising. We introduce CARVE (Counterfactual-Aware Reveal with Verified Expansion), a training-free variable-length algorithm for masked diffusion LMs. Starting from a shorter canvas, CARVE can grow the response during decoding by inserting additional [MASK] positions. Rather than keeping every insertion, CARVE tests a candidate expanded canvas and asks a counterfactual question: would the model make similar predictions for the unresolved positions in the original canvas if the extra masked space were present? The inserted masks are kept only when they induce low Jensen-Shannon (JS) divergence on aligned unresolved positions. This makes length growth a verified stability decision rather than a pure confidence heuristic. CARVE applies without retraining to both full-canvas and blockwise diffusion decoders. Across code generation and mathematical reasoning benchmarks, CARVE consistently improves average performance over fixed-length baselines across all evaluated model families. Crucially, CARVE achieves these accuracy gains while reducing inference cost, reaching half the FLOPs of fixed-length decoding in some settings.

---


### 394. [TRIPPULSE: Multi-Agent Travel Planning with Review-Grounded Reasoning](https://arxiv.org/abs/2608.30924)

**<font color=#1a73e8>作者：</font>** Priyanshu Karmakar, Borru Vijay Sai, Shubhojit Mallick 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Travel itinerary generation requires balancing strict spatio-temporal constraints with human preferences. Existing LLM-based planners mainly rely on structured attributes and pre- defined traveler personas, but real travel deci- sions are often shaped by reviews that reveal experiential factors such as comfort, safety, ser- vice quality, ambiance, crowding, and hidden risks absent from structured databases. Incor- porating such review information is therefore critical to realistic, user-centric itinerary gen- eration. We propose TRIPPULSE1, a multi- agent framework for review-grounded travel planning. Instead of relying on a monolithic planner (and face context and reasoning bot- tlenecks), TRIPPULSE2 decomposes itinerary generation into specialized agents (each op- erating over localized contexts) for accom- modations, transportation, meals, attractions, and events, coordinated through a global or- chestrator with scheduling mechanisms that enforce temporal and budget feasibility. We augment TRIPCRAFT with 100K+ real-world reviews and introduce Review-Grounded Per- sona Alignment (RGPA), an LLM-as-a-Judge metric for evaluating alignment with human- centric travel experiences. Experiments across multiple trip durations and diverse proprietary and open-source models show that TRIPPULSE maintains strong constraint satisfaction while generating more personalized and experien- tially grounded itineraries.

---


### 395. [Annotated Surrogate Retrieval for Polish Statutory Law](https://arxiv.org/abs/2608.30929)

**<font color=#1a73e8>作者：</font>** Orkun Yiğit Cengiz  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present a family of retrieval methods for Polish statutory law built on document surrogates: language-model annotations attached to statutory articles at index time. Three designs occupy different points on the cost-quality frontier. ASCR is a surrogate cascade with reranking; ASCR-H fuses a dense list into that cascade; and DTF replaces both language-model stages with three lexical and dense retrievers, weighted reciprocal rank fusion, and a deterministic re-scoring prior, using no model call before generation. We evaluate all three against fourteen lexical, dense, fused and ablated baselines plus four controls, on 300 questions from the 2024 and 2025 Polish bar and legal counsel entrance examinations (264 with their reference article in the corpus), over 82,508 articles from 1,133 acts. On paired McNemar tests, ASCR-H places the reference provision at rank one significantly more often than every other non-oracle configuration except one of its own ablations (eighteen of twenty comparisons significant in its favour at p < 0.005), reaching 72.3% against 61.7% for BM25 and 52.3% for dense retrieval. The advantage is concentrated at the head and does not survive depth: it is significant at cutoffs of one and five, disappears by ten, and by twenty DTF leads on point estimate (86.0% versus 84.5%) at one ninth the latency and less than half the cost. Ablation attributes 27.6 points of rank-one accuracy to the reranking stage alone. We further report that the ranking advantage does not extend to citation accuracy, where DTF matches the oracle ceiling, and three negative results on lemmatisation, pseudo-relevance feedback and query rewriting. Surrogate annotation covers 27.0% of the corpus but every reference provision in the benchmark, an asymmetry we disclose and discuss. Benchmark, per-question outputs and paired significance tests are publicly available.

---


### 396. [Evidence, Logic, and Compliance: Multi-Agent Structured Graph Reasoning with Expert Arbitration for Medical Referral](https://arxiv.org/abs/2608.30938)

**<font color=#1a73e8>作者：</font>** Qi Peng, Yi Cai, Jialin Cui 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Medical referral (directing patients to the appropriate hospital department) is a complex decision-making process requiring the synthesis of multimodal data, including patient narratives, laboratory indicators, and radiology imaging. While Large Language Models (LLMs) have advanced medical dialogue systems, they struggle with real-world referral tasks due to two primary limitations: (1) Information Overload, where models fixate on high-frequency disease terms while overlooking subtle but critical urgency indicators; and (2) Unstructured Collaboration, where existing multi-agent frameworks rely on loose dialogue that leads to semantic drift and confirmation bias. To address these challenges, we introduce MASGR (Multi-Agent Structured Graph Reasoning), a framework that treats referral not as a classification task but as a structured graph construction problem. MASGR deploys specialized agents to extract evidence from distinct modalities and coordinates them through a clinical reasoning graph. This graph forces agents to establish explicit logical connections between conflicting evidence. Furthermore, we integrate a knowledge-guided arbitration mechanism that prioritizes patient safety rules over standard diagnostic classification. Extensive experiments on real-world medical records demonstrate that MASGR significantly outperforms state-of-the-art LLMs and existing multi-agent systems, particularly in complex cases requiring the balancing of chronic disease management and emergency intervention. The AI contribution lies in the Multi-Agent Structured Graph Reasoning framework that transforms unstructured multi-agent dialogue into a verifiable logical graph construction. The engineering application is demonstrated through its deployment in a complex healthcare decision-making system to optimize the precision of complex medical referrals.

---


### 397. [Detecting AI Impostors: How Do Middle Schoolers Identify LLM Agents in a Live Collaborative Setting?](https://arxiv.org/abs/2608.30948)

**<font color=#1a73e8>作者：</font>** Dan Schumacher, Pragathi Durga Rajarajan, Haven Kotara 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLMs can imitate how people write, which raises concerns about impersonation, trust, and detection in social settings. These concerns are especially important for adolescents, who use generative AI frequently but may struggle to recognize it. We introduce \textit{DoppelBot}, a cooperative social deduction game designed to study how young people detect and respond to AI impersonation. Through studies with middle schoolers, we investigate whether a DoppelBot prompts reflection on privacy and impersonation, how repeated exposure affects AI-detection accuracy as agents become more personalized, and which strategies students use to identify AI doppelgängers. We find that students' detection accuracy improves over time, driven by a shift from relying on linguistic cues to leveraging shared social and contextual signals. Students also demonstrated an understanding of AI limitations such as embodiment and reflected on broader issues such as data privacy. To support future research, we release an anonymized dataset of game transcripts and voting behavior.

---


### 398. [One Policy Is Enough: Single-Agent Reinforcement Learning Outperforms Tree Search for Chemistry Tool Learning](https://arxiv.org/abs/2608.30952)

**<font color=#1a73e8>作者：</font>** Armin Dariani, Sifan Wu, Bang Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Chemistry questions often demand exact computation and database lookups that a language model cannot supply from its parameters, so it must reach for external tools. Tool use here is a three-part problem: select the right tool from a large pool, fill it with correctly typed arguments, and chain calls so that each consumes the outputs of the last. CheMatAgent, a previously published system, addresses this with hierarchical evolutionary MCTS: separate policy and execution models searching tool-call trees under two learned critics, one regressed partly onto GPT-assigned scores. We show that a single policy suffices. Our model interleaves reasoning, tool calls, and returns in one left-to-right generation, trained by a supervised warm-up and then outcome-level reinforcement learning against a programmatic reward read directly off the gold call chain, which leaves no learned critic and no judge in the training loop. On ChemToolBench multiple-tool comprehensive chemistry, on both backbones CheMatAgent use, we improve Tool F1 by 5.5% and Return F1 by 9.6% on Qwen-2.5-7B, and by 3.7% and 3.9% on Llama-3.1-8B, compared with their strongest search configuration, at one model invocation per question, against a search whose cost grows with the tree; we also lead answer Pass Rate on Qwen-2.5-7B.

---


### 399. [LOCI: A Locator-Critic with Refinement Loop](https://arxiv.org/abs/2608.30959)

**<font color=#1a73e8>作者：</font>** Walid Bousselham, Mathilde Caron, Arsha Nagrani 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-Language Models (VLMs) still struggle on tasks requiring complex visual understanding. We argue that the core issue is not high-level reasoning, but instead failing to locate critical details in the image. Due to this shortcoming, VLMs generate often plausible but incorrect reasoning based on flawed perceptual grounding. To address this, we propose Locator-Critic (LOCI), a training-free framework that decouples visual search from evidence verification. LOCI employs a Locator agent to propose candidate visual evidence and a separate Critic agent to evaluate its relevance and sufficiency. These agents engage in an iterative refinement loop, progressively improving the evidence until it is adequate to answer the given question. This decoupled, self-correcting process yields substantial performance gains, achieving state-of-the-art results on multiple complex visual benchmarks. LOCI improves accuracy for both open-weight models like Qwen3-VL (+12.1 on V*, +5.8 on HR-Bench and +11.2 on VisualProbe-Hard) and proprietary models like Gemini 2.5 Pro (+8.9 on V*, +4.3 on HR-Bench, +4.8 on VisualProbe-Hard).

---


### 400. [A Universal Context-Reuse Layer for Cross-Model KV Sharing](https://arxiv.org/abs/2608.30963)

**<font color=#1a73e8>作者：</font>** Yi Li, Dongming Jiang, Yi Zhao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Modern large language model (LLM) serving systems increasingly operate over repeated or shared context, yet each model typically performs its own prefill computation even when another model has already processed the same input. Existing KV-cache reuse mechanisms substantially reduce redundant computation within a single model, but generally assume that the producer and consumer of a cache are identical. We study \emph{cross-model KV sharing}, which translates the KV state produced by a source model into a representation that can be consumed by a different target model, including models that differ in scale, architecture, attention configuration, tokenizer, and model family. We evaluate the approach in both within-family and cross-family settings. For Qwen2.5-7B $\rightarrow$ Qwen2.5-1.5B, translated KV states improve LongBench2 accuracy from 27.59\% to 34.48\%, a gain of 6.89 percentage points over the native 1.5B baseline, while reducing handoff cost relative to native target prefill. For the cross-family Qwen2.5-1.5B $\rightarrow$ Gemma-2-2B setting, KV handoff reduces target-side prefill cost by up to 67.05\% at 4K context length while maintaining decoding perplexity close to native-model baselines. In a more heterogeneous Llama3.1-70B $\rightarrow$ Qwen2.5-7B setting, cross-family handoff achieves 44.0\% accuracy compared with 45.7\% for native Qwen2.5-7B inference, while reducing measured latency from 899ms to 138ms. These results provide initial evidence that KV states can serve as transferable computational representations rather than strictly model-local caches, and motivate \emph{context mobility} as a systems abstraction for reducing redundant prefill across heterogeneous LLM and multi-agent inference workflows.

---


> [!TIP]
> 当前位于：**351-400**（第 8/10 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | **351-400** | [401-450](./part-09.md) | [451-452](./part-10.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
