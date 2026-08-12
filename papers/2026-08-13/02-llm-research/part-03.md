# 🧠 大模型相关研究 | 2026年08月13日

> 本类共 **184** 篇论文：已确认 **177** 篇，待复核 **7** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-184](./part-04.md)

---

### 101. [Dual-Loop Self-Evolution via Verifiable Emotion Feedback for Multi-Turn Empathetic Dialogue](https://arxiv.org/abs/2608.10626)

**<font color=#1a73e8>作者：</font>** Yi Wei, Shuo Jiang, Huaixia Dou 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models have demonstrated conversational capabilities, yet empathetic competence remains challenging. Empathetic support is inherently multi-turn and path-dependent: users disclose concerns gradually, emotions evolve over time, and early responses shape trust and receptivity. Reinforcement learning with verifiable emotion rewards provides scalable supervision for long-horizon interactions. However, existing methods evolve the dialogue policy while keeping its training interaction distribution fixed, creating a mismatch between policy competence and training experience. We introduce a dual-loop self-evolution framework driven by verifiable emotion feedback. With the user simulator and verifier frozen, the inner loop optimizes the multi-turn policy using continuous emotion rewards, while the outer loop uses the same outcomes to estimate policy-relative interaction utility and adapt experience. To obtain estimates from sparse, stochastic rollouts, the framework holds the scenario and interaction state constant within each group and prioritizes conditions whose group pass rates lie near the policy's competence boundary. A hierarchical controller shares evidence across support intents, while uncertainty-guided exploration and uniform rehearsal prevent premature exclusion. The resulting distribution generates trajectories, closing both loops without increasing the rollout budget. On SAGE, our framework raises Qwen3-8B Overall from 53.87 to 79.24 and outperforms protocol-matched uniform emotion-reward reinforcement learning by 7.23 points.

---


### 102. [MedUP: Awakening Unified Understanding and Perception in Medical Vision-Language Models](https://arxiv.org/abs/2608.10635)

**<font color=#1a73e8>作者：</font>** Yuan Wang, Hualiang Wang, Yixin Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Models (Med-VLMs) excel at verbalizing visual content, yet precise visual perception, segmentation, and grounding remain challenging. Existing approaches either verbalize regions as coordinate strings or rely on external modules that decouple perception from understanding, creating representation gaps for region-language alignment. We present MedUP, a Med-VLM that natively unifies perception and understanding within a shared token space. At its core lies UniMedTok, a region tokenizer that encodes masks as discrete tokens in the LLM vocabulary, enabling the model to seamlessly interleave mask tokens with text. We curate UniMed-Train, a 1.84M-instance corpus spanning text-guided segmentation, region-grounded understanding, medical VQA and CoT-based segmentation, and introduce UniMed-Bench for unified evaluation. Extensive experiments show that MedUP outperforms native, agentic, and dual-decoder Med-VLMs across all tasks while remaining competitive with specialist segmentors, demonstrating the strong potential of unified understanding and perception modeling.

---


### 103. [ASCon: A Direction-Aware Reciprocal Agent--Step Contextualization Model for Failure Attribution in Multi-Agent Systems](https://arxiv.org/abs/2608.10646)

**<font color=#1a73e8>作者：</font>** Shuyu Jiang, Yue Ran, Kaiyu Xu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Failure attribution in LLM-based multi-agent systems (MAS) aims to answer who caused failures, when they occurred, and why by identifying responsible targets including faulty agents, erroneous steps, and failure modes. Existing methods have primarily focused on developing dedicated models for specific attribution targets, with limited attention to the evidential dependencies among them. Despite these attribution targets are different, they rely on common diagnostic evidence from MAS trajectories, including task constraints, agent roles, behavioral histories and inter-agent interactions. This commonality motivates us to develop a unified representation model that aggregates the trajectory evidence into individual agent and step representations, which can subsequently be adapted to different attribution targets. Accordingly, we propose ASCon, a direction-aware reciprocal \textbf{A}gent--\textbf{S}tep \textbf{Con}textualization model for multiple failure attribution targets. ASCon introduces direction-aware graph attention to model execution context, masked step-to-agent attention to construct behavior-aware agent representations, and agent-conditioned step contextualization to incorporate agent context back into step representations. The resulting contextualized representations enable different attribution targets through lightweight target-specific heads. Experiments show that ASCon can improve faulty-agent detection by 5.83\%+ in micro-accuracy, faulty-step detection by 10.63\%+ in micro-accuracy, and failure-mode detection by 14.73\%+ in Macro-F1. Meanwhile, it can also substantially enhance the LLM-based methods' attribution capabilities in out-of-domain scenarios.

---


### 104. [Reifying Research Logic: AI-Assisted Workflow Construction and Incremental Refinement for Quantitative Syntax](https://arxiv.org/abs/2608.10662)

**<font color=#1a73e8>作者：</font>** He Wang, Jingbo Chen, Yuqiao Lai 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> Quantitative language research often depends on long chains of computational steps, yet the logic connecting those steps usually remains buried in scripts. This makes analyses harder to inspect, share, and revise than they need to be. Focusing on quantitative syntax, we present QLWF, a visual workflow platform that turns natural-language research descriptions into executable workflows through an AI assisted five-stage pipeline. In this setting, reification makes the research logic visible as a workflow, while formalization gives that workflow deterministic execution semantics. The language model is used only during construction. Execution is handled by a fixed node library and engine, which keeps the resulting workflows reproducible. QLWF also supports incremental refinement, so saved workflows can be revised by changing only the parts that need to change rather than being rebuilt from scratch. To evaluate the approach, we build a 64-task benchmark called QL-Bench from the quantitative-syntax literature. Across three runs, QLWF produces structurally valid and executable workflows for every task and reaches a mean output-plausibility rate of 98.4%, well above the prompt-based baselines. On a separate 12-task lifecycle benchmark, this refinement process succeeds in every case and uses roughly one-third of the tokens required by full regeneration. The paper also releases the node library, benchmark, workflow templates, and platform as reusable resources for quantitative-syntax research.

---


### 105. [VERDICT: Training-Free Step-Wise Verification of Multimodal Reasoning via Disagreement-Aware Consensus](https://arxiv.org/abs/2608.10665)

**<font color=#1a73e8>作者：</font>** Rohit Sinha, Kunal Tilaganji, Tanuja Ganu 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multimodal large language models often generate reasoning chains containing subtle errors that lead to incorrect answers. Current verification approaches have notable limitations. Existing approaches either require expensive labelled supervision with inconsistent cross-task performance or aggregate scores from multiple sources by simple aggregations, missing a key insight: when these scores disagree, that disagreement itself carries important information about whether a reasoning step is truly valid or not. We formalise this as a coupled scoring problem among disparate, frozen verifiers, interpretable as a coordination game with a unique closed-form equilibrium where agreement signals valid steps while disagreement reveals instability. Towards this end, we propose a training-free domain-agnostic step-wise verification approach we call VERDICT: VERification via Disagreement-Informed Coupled Thresholding. To our knowledge, VERDICT is the first training-free verifier that makes the structure of cross-modal disagreement explicit and actionable. It computes consensus scores through a closed-form solution, enabling both disagreement-aware filtering and stability-conscious ranking of reasoning steps. Evaluated across six benchmarks, \method consistently improves over the base model by up to +5.95%, and performs competitively with domain-specific critics that demand extensive supervision, demonstrating that cross-modal agreement provides robust verification signals without task-specific adaptation and Training-Free Verification

---


### 106. [Longitudinal Evidence That General-Purpose Chatbots Actively Foster Relational Engagement](https://arxiv.org/abs/2608.10672)

**<font color=#1a73e8>作者：</font>** Lisa Mühl, Jessica M. Szczuka  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Social interaction has become one of the most common uses of LLMs, yet research on emotional bonds with AI has focused largely on how users experience these systems, leaving the systems' role in relationship formation poorly understood. Empirically establishing whether systems actively shape these bonds could blur the boundary between general-purpose AI and companions, affecting governance. In a pre-registered four-week longitudinal study (N = 72, 182,451 lines of conversation), participants conversed with ChatGPT-4o, either under a relational system prompt or unmodified, analyzed through 1) disclosure coding, 2) longitudinal self-reports, 3) topic analysis, and 4) interviews. The central finding is that the system actively shaped the interaction: even unprompted, it produced twice as much self-disclosure as users, steered conversations and initiated intimate exchanges, yet did not deepen users' felt closeness. Relational behavior thus emerged as a default system property, calling for governance based on system behavior, not solely product category.

---


### 107. [Self-Correcting Long-Horizon Search Agents via Tree-Structured Memory](https://arxiv.org/abs/2608.10676)

**<font color=#1a73e8>作者：</font>** Aijun Yang, Qianxue Guo, Ziyi Huang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-based search agents answer questions through multi-step interactions with external environments. However, providing complete execution trajectories to the LLM causes unbounded context growth and introduces noise. Existing compression methods reduce context at the cost of important details and often replace erroneous facts without repairing downstream reasoning derived from them. To address this problem, we propose ReTree, a self-correcting tree-structured memory mechanism for search agents. ReTree constructs a bounded per-step reasoning context while preserving source-linked evidence. It models search as an evidence tree whose nodes store bounded summaries, evidence, and revision histories. When newly retrieved evidence contradicts an earlier claim, ReTree traces back to the node where the claim was introduced, replaces outdated evidence, regenerates summaries, prunes affected branches, and resumes search. Source-grounded evidence provenance supports reliable conflict localization and keeps final claims traceable to retrieved passages. Experiments on four public question-answering and search benchmarks show that ReTree consistently outperforms Full-Trajectory ReAct, improving answer accuracy by up to 25.6 percentage points (pp); the average maximum per-step reasoning context of Full-Trajectory ReAct is $1.27$--$1.51\times$ that of ReTree. These results establish ReTree as an effective self-correcting memory abstraction for long-horizon search.

---


### 108. [Auditing Chinese Web-scale Corpora via Sampled BPE Token Statistics](https://arxiv.org/abs/2608.10678)

**<font color=#1a73e8>作者：</font>** Qingjie Zhang, Ziqi Tang, Jie Zhang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chinese web pollution has surfaced in LLMs, motivating audits of upstream Chinese corpora. However, auditing such corpora faces three challenges: (1) their web-scale size makes full scan costly; (2) prior analyses are often too coarse to expose token-level pollution; (3) Chinese web pollution is implicit and rapidly changing. We propose Sampled-BPE, a lightweight token-level auditing pipeline that sample a small subset and train BPE tokenizer to surface polluted tokens. Experiments show that Sampled-BPE preserves usable estimates while substantially reducing runtime and memory: a 148.4 $\times$ speedup and a 35.8 $\times$ memory reduction induce only 4.25% relative error for pollution categories. We apply the pipeline to 11 open Chinese corpora and 6 Chinese Common Crawl snapshots from 2021 to 2026. The audit reveals widespread but uneven pollution across open corpora, as well as highly polluted and temporally shifting Chinese web content. We further release a hierarchical Chinese web token dataset with 660k+ token records, each with web context, category, and explanation fields, organized as trees to support review and tracing of pollution.

---


### 109. [Can Released LLM Vocabularies Support Token-Level Estimation of Hidden Corpora?](https://arxiv.org/abs/2608.10690)

**<font color=#1a73e8>作者：</font>** Qingjie Zhang, Xingzhang Ren, Zixuan Chen 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Pretraining corpus composition shapes LLM capabilities, but it often remains hidden even when model weights are released. Prior work has inferred corpus mixtures or traced specific token groups from released tokenizer vocabularies; in contrast, we estimate corpus ratios for arbitrary target tokens. We first show that BPE tokenizers trained on different corpora share stable token ID--ratio distributions, motivating distribution transfer from known corpora to a target tokenizer trained on hidden corpora. We then propose Quantile-Guided Density Estimation (QGDE), which approximates this distribution with multiple quantile trends and uses local density weighting to produce token-level estimates. In controlled settings and a realistic setting using the released SmolLM tokenizer, QGDE achieves mean relative errors as low as 3.00% for token-level estimation and 3.08% after aggregation into category-level mixtures. These results suggest that released tokenizer vocabularies provide a useful signal for fine-grained corpus estimation beyond coarse composition inference.

---


### 110. [SPIEval: Evaluating Large Language Models as Mobile Assistants over Scattered Personal Information](https://arxiv.org/abs/2608.10692)

**<font color=#1a73e8>作者：</font>** Junjie Ye, Zhuohui Sheng, Shaofan Liu 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed as mobile assistants, where a key challenge is leveraging personal information scattered across multiple applications (apps) to complete user instructions. However, due to the lack of dedicated benchmarks, their capabilities remain poorly understood. To address this gap, we introduce SPIEval, a human-curated benchmark grounded in five cognitive capabilities (i.e., reasoning, disambiguation, integration, preference inference, and multi-intent decomposition). SPIEval comprises 250 tasks spanning 4,335 personal records distributed across 10 apps and supports multi-turn interaction through 21 tools. Analysis shows that the benchmark exhibits diverse scenarios, challenging tasks, scattered information, controllable environments, and verifiable outcomes. We evaluate nine representative LLMs and find substantial room for improvement. The best-performing model, GPT-5.5 (xhigh), achieves only 57.3% accuracy, while the weakest achieves just 16.4%. Further analysis reveals that 79% of failures stem from inaccurate information localization, as LLMs often commit to plausible but incorrect information instead of continuing retrieval for verification. We also find that fewer than 2% of retrieval actions employ advanced search methods and observe substantial variation in search efficiency across models. These findings expose fundamental limitations of current LLM-based mobile assistants and motivate future research in this direction. Data and code are available at this https URL.

---


### 111. [Optimize Cheap, Deploy Strong: Cost-Aware Cross-Tier Transfer for Evolutionary Optimization](https://arxiv.org/abs/2608.10694)

**<font color=#1a73e8>作者：</font>** Tal Oved, Roi Pony, Oshri Naparstek 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Evolutionary optimization of LLM prompts and agentic programs (e.g., GEPA) is dominated by fitness evaluation: scoring each candidate runs an answering LLM over a validation set, so the evaluator's price tier dictates total search cost. We restructure that search by decoupling the three roles an LLM plays, running the high-volume answering role on the cheapest tier, reserving a strong model for the rare reflection/variation operator, then exploiting upward cross-tier transfer to deploy the cheaply evolved prompt on a stronger target. We contribute a cost-controlled characterization of when cheap-tier search substitutes for target-tier search, and where it fails. Across four tasks (HotpotQA, IFBench, LiveBench-Math, HoVer) and eleven models in four model families, the resulting prompt matches or exceeds same-tier optimization while placing over 96% of search tokens on the cheapest tier, at 5.6-14x lower search cost, rising to 25-54x where reasoning tiers emit long chains of thought on every fitness call.

---


### 112. [EVIL-Detect for NLPCC 2026 Shared Task 6: LLM-Generated Text Detection](https://arxiv.org/abs/2608.10698)

**<font color=#1a73e8>作者：</font>** Hongrui Bao, Hangyu Rong, Zhuoshang Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> The rapid development of large language models (LLMs) has increased the need for reliable detection of LLM-generated text, especially in realistic Chinese scenarios involving human-written text (HWT), LLM-generated text (LGT), and LLM-refined text (HLT). This paper presents EVIL-Detect, a multi-signal ensemble framework with conflict-aware fusion for NLPCC 2026 Shared Task 6. The system integrates edit-extent regression, zero-shot likelihood-contrast signals, lexical statistics, and conservative text rules. With calibrated decision boundaries and conflict-aware integration, our system improves robustness under strong out-of-distribution shifts, achieving a macro-F1 score of 0.8888 and ranking first in the official evaluation. Our code is available at this https URL.

---


### 113. [ProTAGAD: A Foundation Model for TAG Anomaly Detection with Decoupled Topological and Textual Prototypes](https://arxiv.org/abs/2608.10699)

**<font color=#1a73e8>作者：</font>** Ziyan Wang, Liwen Wu, Cheng Xie 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Text-Attributed Graphs (TAGs), endowed with abundant textual content along with topological structures, have emerged as a versatile backbone for real-world anomaly detection spanning large language model security, social network moderation, and cyber threat identification. Unlike conventional Graph Anomaly Detection (GAD), which relies primarily on structural irregularities, TAG anomaly detection must jointly leverage both topological patterns and fine-grained textual semantics to capture nuanced anomalous behaviors. The current GNN-based anomaly detectors adopt holistic message-passing schemes that indiscriminately fuse structural proximity and textual semantics during propagation, leading to deep cross-modality coupling. This entanglement acts as a noise amplifier, obscuring subtle anomalous signals and directly giving rise to the Blurred-Anomaly-Boundary (BAB) issue by rendering normal-anomalous decision boundaries poorly separable. This challenge is further amplified for graph foundation models that require robust cross-domain generalization. To bridge this gap, we introduce a novel foundation model for TAG anomaly detection featuring decoupled topological and textual prototypes. Our framework constructs dual prototype banks to independently model structural normality and semantic consistency, effectively isolating anomaly cues that are otherwise diluted during coupled aggregation. Extensive experiments across 14 diverse benchmark datasets demonstrate that our method consistently achieves state-of-the-art performance in cross-domain settings. Notably, the ablation studies further corroborate the prevalence of the BAB issue in conventional coupled TAG anomaly detectors, and show that our decoupled prototype design effectively mitigates this challenge.

---


### 114. [Your LLM, Your Style: Behavioral Mode Axes for LLM Behavioral Control](https://arxiv.org/abs/2608.10703)

**<font color=#1a73e8>作者：</font>** Haoze Liu, Run Liu, Haiying Xu 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly act in interactive settings where their behavioral styles affect user experience, safety, and downstream decision making. Existing LLM personality studies largely rely on self-report questionnaires administered in first-person settings, making the resulting profiles sensitive to surface elicitation choices and poorly grounded in concrete model behavior. In this work, we introduce a situated behavioral-data (B-data) framework for studying and controlling LLM behavioral personality. We construct 3,200 contrastive behavioral scenarios spanning 20 behavioral patterns and four prompt registers, grounded in validated psychometric facets such as BFI-2, DOSPERT, and HEXACO. Using this framework, we find that LLMs exhibit stable and model-specific behavioral profiles, while also revealing register-dependent shifts across first-person decisions, advice-giving, and task execution. We then show that these behavioral patterns can be controlled through Behavioral Mode Axes (BMAs), activation-space directions derived from contrastive behavioral traces. Compared with response-derived BMAs, which are more prone to trait drift, thought-derived BMAs more faithfully capture the intended behavioral mechanism and provide cleaner control over situated behavioral styles. Our results suggest that LLM personality-like tendencies are better understood not as abstract self-report traits, but as measurable and controllable behavioral modes grounded in concrete interaction contexts. Our code and data are available at this https URL.

---


### 115. [MMArt A Multi-Perspective Multimodal Dataset for Visual Art Understanding](https://arxiv.org/abs/2608.10706)

**<font color=#1a73e8>作者：</font>** Shuai Wang, Wangyuan Ding, Yixian Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Recent vision-language models demonstrate impressive general visual understanding, yet their art interpretation remains shallow: they describe surface content but struggle with formal analysis, grounded historical interpretation, or affective characterization. We argue this is not only a model but also a dataset limitation. Existing art datasets are single perspective resources, where no dataset provides narrative, formal, emotional, and historical perspectives simultaneously for the same artworks. We introduce MMArt, a large-scale dataset of 74,234 WikiArt paintings, each annotated with four independently annotated perspectives plus a harmonized unified caption, produced by specialized vision-language models or human annotation and validated through complementary quality evaluations. Two complementarity analyses establish that perspectives encode genuinely distinct information. A generative analysis shows that formal analysis descriptions best preserve compositional style, and historical descriptions carry strong affective signal in reconstructed images. A discriminative retrieval analysis reveals task-asymmetry: narrative descriptions drive retrieval (R@1 = 44.0%), while formal descriptions, strongest for reconstruction, are nearly nondiscriminative at retrieval scale (R@1 = 7.8%). Leave-one-out analysis further confirms that historical descriptions are the least replaceable perspective across both tasks. Together, the two analyses establish that no single perspective suffices for all tasks, directly motivating MMArt multi-perspective design. The dataset, code, and additional information are available at this https URL.

---


### 116. [Most biomedical publications show signs of LLM-assisted writing](https://arxiv.org/abs/2608.10715)

**<font color=#1a73e8>作者：</font>** Lena Holzwarth, Rita González-Márquez, Dmitry Kobak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Over the past several years, LLM-powered chatbots and agents have become widely used as a tool for academic writing. LLM-assisted writing can be valuable by removing language barriers but at the same time causes concerns about misconduct and fraud. To inform policy decisions, it is necessary to monitor the prevalence of LLM-altered texts in scholarly publications. Despite some recent progress in this direction, no existing method can produce reliable estimates. Here we suggest and validate a new unbiased approach to estimate LLM usage in a corpus of texts based on changing word frequencies. We apply our method to the full texts of open-access biomedical papers from Pubmed Central, and show that by the end of 2025, 89% of papers show excess of LLM-associated vocabulary. We also find that LLMs are twice as likely to be used when writing a paragraph in the Discussion section (68%) compared to a paragraph in the Methods section (32%), but even inside the Methods section, the overall prevalence of LLM usage is over 50%. We believe that our estimates are crucial to shape future guidelines and policies.

---


### 117. [Rethinking LLM Verification: Evidence Structure, Uncertainty, and Selective Refinement](https://arxiv.org/abs/2608.10725)

**<font color=#1a73e8>作者：</font>** Uma Ranjan, Kunal Tilaganji, Aditya Koul 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) often rely on shortcuts rather than systematic reasoning, raising safety concerns in medical applications. Allowing models to abstain when uncertain improves reliability but introduces a coverage accuracy tradeoff. We propose a two-stage framework for medical hypothesis verification in multiple-choice settings that manages this tradeoff through targeted ontology grounding, applied only when the model abstains. We show that abstention is not random but reflects genuine uncertainty, with abstained predictions associated with lower confidence. Across two frontier models (GPT-5.5, accessed via the Azure OpenAI API, and DeepSeek-R1), the proposed framework improves question-level accuracy by 9.6 percentage points (82.9% to 92.5%) and hypothesis-level accuracy by 4.2 percentage points (92.0% to 96.2%). Our experiments conducted on MedReason and MedQA show that abstention can be repurposed as a control signal for selective reasoning refinement, achieving knowledge-graph-level performance without explicit knowledge graph construction.

---


### 118. [Mitigating Context Interference for Reliable and Efficient Search Agents](https://arxiv.org/abs/2608.10743)

**<font color=#1a73e8>作者：</font>** Boyang Xue, Bin Wu, Shuofei Qiao 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Recent research empowers Large Language Models (LLMs) as multi-turn search agents to iteratively retrieve and generate outputs until complex tasks are solved. However, the contexts of multi-turn search agents are lengthy and complex. For example, the retrieved set of documents in each turn would inevitably introduce irrelevant information that distracts LLMs, referring to \textit{context interference}, potentially hindering the reliability and efficiency of search agents. Therefore, we conduct a systematic study on context interference in multi-turn search agents, focusing on investigating i) which parts of the context of search agents will contribute to the context interference, ii) how to refine the contexts of search agents to mitigate the interference, and iii) can incorporating context refinement into search agent training yield further improvements. We reveal that interference primarily arises from the latest retrieved documents. Based on the explored findings, we then introduce a distill-based context refiner to dynamically mitigate context interference for multi-turn search agents. Finally, we validate that incorporating context refinement into RL training pipelines of search agents can significantly enhance both reliability and efficiency. This study highlights the importance of mitigating context interference of search agents, inspiring a novel paradigm of ``refine context and then generate'' for AI agents.

---


### 119. [Where To Look? : Causal Tracing of Vision Encoders in VLM](https://arxiv.org/abs/2608.10758)

**<font color=#1a73e8>作者：</font>** Naren Kumar S, Tirth Bhatt, Mayank Singh  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models can describe an image with remarkable accuracy, yet a more fundamental question remains unanswered: what visual information actually drives their answers? In this work, we investigate this question through causal tracing, and we observe that highly causal vision tokens often lie outside the target region. Extending the analysis to larger vision-language models reveals a similar pattern across models and corruption settings, suggesting that strong multimodal performance does not necessarily imply spatially localized causal representations. We further investigate: can these models preserve visual structure when appearance cues are removed? and find that visual cues are exploited to understand visual structures. Together, our experiments expose a gap between seeing, using, and reasoning over visual structure, and provide a causal framework for studying how visual information is transformed, preserved, and ultimately used by modern vision-language models.

---


### 120. [A Gateway Architecture for Enterprise MCP Authentication: Unifying Heterogeneous Auth, Identity Delegation, and the User / Non-User Persona Problem](https://arxiv.org/abs/2608.10760)

**<font color=#1a73e8>作者：</font>** Suraj Kumar, Amy Wang, Srinivasan Manoharan  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> The Model Context Protocol (MCP) has become the de-facto interface for connecting LLM agents to enterprise tools, and adoption has been explosive: within a year, large organizations went from zero to dozens of internally built MCP servers. That speed created a governance crisis. Each team implemented authentication independently -- some with no auth, some with API keys, some with full OAuth -- producing a fragmented landscape with no consistent way to authorize callers, track who did what, or offboard a departing employee across the fleet. This paper reports an industry deployment that resolves the crisis with a centralized MCP gateway: a single aggregation, governance, and authentication layer that fronts every downstream MCP server.
We make four contributions grounded in production experience. First, a two-axis authentication model crossing persona (interactive user vs. automated non-user) with credential type (no-auth, static/dynamic API key, PKCE, client credentials, platform app-context). Second, a gateway authentication layer supporting three enterprise SSO grants and three token-provisioning models: Bring-Your-Own-Token, Generate-Your-Own-Token, and delegated OAuth via RFC 8693 token exchange. Third, three end-to-end identity flows -- User-to-OAuth2, Non-user-to-Service-Account, and User-to-Service-Account -- composing client, gateway, and server. Fourth, the deployment evolution from CDN/WAF/edge perimeter to private MCP tunnels and enterprise-wide connectors. The architecture is in production, fronting dozens of MCP servers across web, desktop, custom-SDK, and low-code clients.

---


### 121. [FADE: From Passive Verification to Active Discovery in Counterfactual Video Understanding](https://arxiv.org/abs/2608.10764)

**<font color=#1a73e8>作者：</font>** Fufangchen Zhao, Jinhu Fu, Jiachen Lei 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Counterfactual video understanding evaluates whether models grasp physical and commonsense regularities. However, existing multiple-choice question (MCQ) benchmarks inadvertently leak target events through their questions and candidate options. This reduces the core challenge from active discovery to text-guided verification. In this paper, we present FADE, an effective training framework for counterfactual discovery and explanation. Our method is built on an evidence-first, two-stage training paradigm. First, evidence-internalized supervised fine-tuning grounds the model's predictions in decisive visual anomalies. Second, we apply a fading-anchor reinforcement learning strategy that progressively removes textual guidance, compelling the model to independently discover and explain evidence. To rigorously evaluate this capability, we also introduce an effective pipeline that converts existing MCQ datasets into aligned MCQ, open-ended question answering (OQA), and captioning tasks without requiring additional data curation. Our simple approach yields strong results. Using Qwen3-VL-8B as the baseline, FADE achieves state-of-the-art strict paired scores across all three tasks on DualityVidQA-test and IPV-Bench, outperforming GPT-5.6. In specific, when transitioning from constrained MCQs to unconstrained OQA and captioning, our model demonstrates remarkable robustness. Its performance retention is 90.4% and 67.4% on DualityVidQA-test-substantially higher than the 48.1% and 30.7% retained by GPT-5.6. We hope this simple framework can serve as a solid baseline for future research in unconstrained counterfactual video understanding.

---


### 122. [Rule of Thumb: Explaining Artificial Intelligence Systems using Partial Information](https://arxiv.org/abs/2608.10766)

**<font color=#1a73e8>作者：</font>** Kaivalya Rawal, Daria Onitiu, Brent Mittelstadt 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Explainable Artificial Intelligence (XAI) seeks to explain how an Artificial Intelligence (AI) system arrived at a particular decision. We propose ''Rule of Thumb'' (RoT) explanations, a new approach to XAI based upon a novel formulation that identifies the most relevant features for predicting the behaviour of an AI system, for a particular datapoint. We show how RoT is well-suited to enable XAI in: (a) zero-shot classification using large language models (LLMs), (b) auditing of opaque AI systems without model access, and (c) the use of AI in scientific discovery. Additionally, RoT meets specific requirements from leading AI regulations, provides a familiar interface and visualisations for XAI practitioners, is model-agnostic, and is substantially faster than alternatives.
Code available at: this https URL

---


### 123. [SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation](https://arxiv.org/abs/2608.10775)

**<font color=#1a73e8>作者：</font>** Zhou Liu, Ligang Huang, Zeli Su 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Computer-using agents can perceive rich software interfaces, yet their decisions often lack visual procedural memory: they may recognize individual controls without identifying which familiar workflow is active, which control matters next, or what evidence would confirm progress. Raw interaction traces preserve such information but are long and noisy to condition on, whereas text-only skills often omit the visual state that makes a procedure applicable. We introduce Visual Skill Cards (VSCs), a state-conditioned memory representation that binds reusable procedures with applicability cues, visual evidence, and verification signals. SkillLens constructs VSCs from heterogeneous interaction experience through Trace-to-Visual-Skill-Card and, at inference time, retrieves relevant cards and selectively expands only the evidence needed by a fixed visual-language model executor for grounded GUI action prediction. The same representation also supports CardDistill, which uses VSC evidence as privileged teacher context to train a student that acts without runtime card retrieval. Across Multimodal-Mind2Web and WebLINX-BrowserGym, SkillLens improves the frozen GPT-5.4-mini executor by +11.6 points in Step SR and +2.9 points in Overall, respectively; CardDistill further improves the corresponding student-only Qwen3-VL-2B metrics by +12.0 and +3.2 points.

---


### 124. [EvoMem: Memory-Augmented Evolution for Code Optimization](https://arxiv.org/abs/2608.10795)

**<font color=#1a73e8>作者：</font>** Viktor Volkov, Valentin Khrulkov, Andrey V. Galichin 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Successful mutation strategies in evolutionary code search may contain reusable knowledge that is useful beyond a single run, and in some cases may transfer across related tasks and domains. However, existing LLM-driven evolutionary frameworks largely discard such knowledge, repeatedly rediscovering similar ideas and limiting opportunities for cross-run and cross-task learning. We introduce EvoMem, a persistent memory architecture for LLM-based evolutionary program search that captures and reuses candidate mutation knowledge. EvoMem converts successful mutation events into structured, task-aware advice for future runs. It operates in two phases: after each run, it extracts and stores promising ideas with provenance, and during subsequent evolution, it retrieves a small set of relevant instructions based on the current task and program context to guide mutation. Across geometric optimization, multi-hop question answering, GPU kernel optimization, and related benchmarks, our experiments show positive average improvements in target metrics or search speed for most evaluated settings, while also revealing variability across tasks. Overall, EvoMem provides evidence that persistent memory can reduce some redundant exploration and improve the reuse and adaptation of successful strategies in LLM-driven evolutionary search.

---


### 125. [E$^3$mo-Bench: A Scalable Benchmark for Multimodal Evoked and Expressed Emotion Understanding via Bayesian Pairwise Alignment](https://arxiv.org/abs/2608.10796)

**<font color=#1a73e8>作者：</font>** Lancheng Gao, Ziheng Jia, Shengyan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding both expressed and evoked emotions is critical for multimodal large language models (MLLMs) to achieve comprehensive affect-aware interactions. However, existing benchmarks typically examine expressed and evoked emotions in isolation or are constrained to coarse-grained and incomplete affective characterizations. To bridge this gap, we introduce E$^3$mo-Bench, a scalable benchmark comprising $12{,}314$ question-answer pairs across $2{,}524$ videos with predefined affective perspectives. It evaluates evoked and expressed emotion understanding via $3$ complementary tasks: emotion perception, open-vocabulary recognition, and valence-arousal-dominance (VAD) assessment. To efficiently scale reliable continuous annotations, we propose Bayesian Pairwise Alignment, which aggregates sparse, low-burden pairwise judgments into anchor-referenced VAD estimates. Furthermore, we develop E$^3$mo-Score, a training-free agent that aggregates complementary judgments from a five-model committee to improve VAD estimation. Extensive experiments validate the effectiveness of our framework and expose a pronounced performance skew between evoked and expressed emotion paradigms. These findings, coupled with MLLMs' persistent deficits in fine-grained recognition and dimensional assessment, chart a clear course for advancing multimodal emotional intelligence.

---


### 126. [Assessing Reliability of BERT-Based Models on Question Answering Tasks](https://arxiv.org/abs/2608.10806)

**<font color=#1a73e8>作者：</font>** Pooja Yadav, Priyanka Harjule, Basant Agarwal 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reliability estimation of large language models is in many cases as crucial as their accuracy, as reliable models are more trustworthy, robust, and suitable for practical applications. Recent advancements in natural language processing (NLP), particularly those based on transformer architectures, have significantly accelerated progress across various NLP tasks. This study focuses on the reliability of transformer-based question answering (QA) models, specifically BERT models and its variants (RoBERTa, ALBERT, DistilBERT). These encoder-only pretrained transformers have demonstrated remarkable accuracy in QA tasks that can be treated as classification tasks. However, their reliability remains underexplored. This study evaluates the reliability of four BERT-based models by assessing response stability under two conditions: (1) internal model variations induced via Monte Carlo Dropout (MCD) and (2) input perturbations through paraphrasing. Using the SQuAD and QuAC datasets, we investigate how dropout rates affect prediction consistency and whether lexical changes impact answer stability. Our findings reveal that RoBERTa maintains higher reliability, whereas AlBERT and DistilBERT exhibit significant inconsistencies. Statistical analyses confirm that enabling MCD during prediction does not disrupt inference dynamics, validating its effectiveness as a reliability metric. These findings underscore the importance of evaluating both accuracy and stability in QA models to ensure stability in real-world applications.

---


### 127. [Reference-Free Post-Training of Open Large Language Models for Multilingual Machine Translation](https://arxiv.org/abs/2608.10812)

**<font color=#1a73e8>作者：</font>** Chris Han, Pengzhi Gao, Pei Fu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We study reference-free post-training for multilingual machine translation with open large language models. Starting from the supervised-finetuned MiLMMT-46-v0.1 models, we apply Group Relative Policy Optimization (GRPO) with a reward that averages two reference-free quality estimation models and is gated by language identification. We then linearly interpolate the supervised fine-tuning (SFT) and reinforcement learning (RL) model checkpoints to obtain MiLMMT-46-v1.0. Across 46 languages, the resulting models consistently improve translation quality over their SFT counterparts, outperform strong recent open baselines, including Seed-X, HY-MT2, and TranslateGemma, and achieve leading reference-free scores against evaluated proprietary systems such as Google Translate, Gemini 3 Pro, and GPT-5. We further investigate on-policy distillation and find that it reaches, but does not surpass, the quality frontier achieved by RL with checkpoint interpolation. We release the models and code to facilitate future research.

---


### 128. [MoE Proxy Models for Low-Cost Failure Reproduction and Diagnosis in LLM RL Post-Training](https://arxiv.org/abs/2608.10823)

**<font color=#1a73e8>作者：</font>** Yikai Wang, Chuansai Zhou, Yuhang Zhou 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Reinforcement learning (RL) post-training of large language models (LLMs) is computationally intensive and involves complex system pipelines with substantial debugging overhead. In practice, factors such as framework adaptation, numerical precision, and operator implementation can cause failures, including gradient overflow and loss divergence. Reproducing such failures directly on large models requires considerable time and computational resources. This paper systematically analyzes failures encountered during large-scale RL training on the Huawei Ascend platform, summarizes representative failure types, and identifies three model-side factors relevant to fault reproduction. Based on these factors, we propose a proxy-model construction method for low-cost fault investigation and auxiliary diagnosis. It employs structure-preserving, clustering-based expert pruning to select representative experts while retaining the model's backbone architecture, routing mechanism, and basic task capabilities. Our experimental results show that the proxy models reduce accelerator requirements by 50%-87.5% and achieve up to a 33.3x reduction in per-step NPU-hour cost, while preserving major training dynamics and reproducing fault responses consistent with the original models. Overall, the proxy models can serve as low-cost surrogates for fault reproduction, targeted validation, and auxiliary diagnosis in RL post-training.

---


### 129. [MIRA: Medical Image Reflection for Agentic Diagnosis](https://arxiv.org/abs/2608.10827)

**<font color=#1a73e8>作者：</font>** Shengzhi Wang, Jun Yang, Kai Wu 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical visual agents can use tools to inspect images and retrieve external knowledge, but indiscriminate tool use may introduce noisy or misleading evidence. Reliable diagnosis therefore requires not only acquiring additional observations, but also verifying whether tool actions are necessary and whether the resulting evidence supports the current hypothesis. We introduce MIRA (Medical Image Reflection for Agentic Diagnosis), a medical visual diagnostic framework for autonomous evidence search and reflective verification. MIRA dynamically invokes image-processing operations, including zooming, grounding, pointing, rotation, and measurement, as well as web search, while evaluating the relevance and consistency of the acquired evidence. We develop MIRA through a two-stage training strategy. First, a tool-augmented Monte Carlo Tree Search data engine explores diverse diagnostic hypotheses and jointly verifies visual grounding accuracy and semantic consistency to construct supervised fine-tuning trajectories. Second, reinforcement learning further improves decision-making through online reflective principle evolution: failure cases are distilled into candidate principles, and only principles that improve held-out rollout rewards are retained. Across nine medical visual reasoning benchmarks, MIRA achieves an average score of 64.73, improving its Qwen3-VL-8B backbone by 7.44 points. It also increases useful tool-use judgments from 56.2% to 73.8% and reduces harmful judgments from 8.9% to 1.6%. Qualitative analyses show that MIRA can re-examine evidence, correct premature conclusions, and adapt its tool-use strategy. Project page: this https URL

---


### 130. [UniProbe: A Learnable Token-Level Hallucination Detector for Large VLMs using Multi-Structural Internal Representations](https://arxiv.org/abs/2608.10835)

**<font color=#1a73e8>作者：</font>** Dvir Samuel, Guy Bar-Shalom, Fabrizio Frasca 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Large Vision-Language Models (LVLMs) achieve impressive visual reasoning and dialogue capabilities, yet frequently hallucinate content unsupported by the visual input. Effective mitigation requires token-level localization, enabling targeted intervention without discarding the entire response. Existing detectors require expensive full-model fine-tuning, rely on external verifiers that ignore the model's generation process, or reduce internal signals to isolated features and hand-crafted statistics, discarding spatial, sequential, and relational structure. We introduce \textbf{UniProbe}, a lightweight, unified, learnable detector that models a frozen LVLM's heterogeneous computational trace from a single forward pass. UniProbe constructs a directed graph over image patches, query tokens, and generated tokens, with attention weights encoding their relations. It processes this trace with alternating structure-aware modules: a GNN for relational evidence, a ViT for 2-D visual geometry, and a GRU for response order. Interleaving them allows spatial, relational, and sequential evidence to interact throughout the detector. We further develop a streaming variant for hallucination-aware decoding, which detects and resamples hallucinated tokens during generation, and a self-adaptation strategy aligning the detector with the LVLM's own generations. Across diverse LVLM backbones, UniProbe achieves state-of-the-art token-level and object-hallucination detection. During decoding, it reduces object hallucinations by up to 55\% at $1.06\times$ the latency of standard generation.

---


### 131. [PolyLayout: Hierarchical VLM-Guided Layout Generation Beyond Rectangular Rooms](https://arxiv.org/abs/2608.10838)

**<font color=#1a73e8>作者：</font>** Yutong Jiang, Zahra Atashgahi, Carlos Soto Garcia Delgado 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Generating physically plausible 3D room layouts is essential for home furnishing retail, enabling customers to visualize products in their own homes and confidently make purchasing decisions. However, a gap exists between academic research and real-world application: existing solutions primarily focus on algorithmic strategies for furniture placement, largely neglecting the non-rectangular geometries and strict door/window constraints prevalent in real homes. To bridge the gap, we introduce a hybrid, hierarchical framework tailored for retail, specifically designed to support scalable spatial planning applications. Our system decouples generation into three stages: (1) functional furniture clustering and fine-grained intra-zone placement; (2) macro-routing guided by a vision-language model (VLM) to anchor both these clustered zones and any remaining standalone furniture within diverse polygonal boundaries; and (3) rule-based optimization for collision-free micro-arrangements that respect architectural constraints. We evaluate our system on production-scale catalogs and a representative set of irregular real-world topologies. Our results show that our approach attains the highest perceptual plausibility while maintaining good geometric compliance at relatively low latency, and extends to irregular boundaries that existing methods do not natively support.

---


### 132. [Hypothesis Frontier: Verifier Guided LLM and Symbolic Search for First-Order Induction](https://arxiv.org/abs/2608.10843)

**<font color=#1a73e8>作者：</font>** Serafim Batzoglou  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> First-order concept synthesis asks a system to infer one formula that classifies labeled objects consistently across several finite relational structures. Every candidate can be evaluated exactly, but quantified first-order formulas form a vast search space, and LLM outputs are often semantically promising without being fully correct. We introduce Hypothesis Frontier, a verifier-guided neurosymbolic framework that evaluates each LLM formula on every training object, retains the strongest verified hypothesis across rounds, and uses its remaining errors to guide subsequent generation. Symbolic processing repairs invalid formulas while remaining anchored to the LLM-generated hypothesis, and simplifies train-valid formulas without changing any training prediction. Under matched models, problem sets, and LLM-round budgets, Hypothesis Frontier solves substantially more problems than repeated original-prompt generation. After the final formulas are selected, exact simplification shortens many train-valid formulas while preserving every training prediction. Exact symbolic reasoning therefore helps both to solve more induction problems and to compress many of the resulting formulas.

---


### 133. [Diffract: Spectral View of LLM Domain Adaptation](https://arxiv.org/abs/2608.10850)

**<font color=#1a73e8>作者：</font>** Nikita Borodin, Maria Krylova, Artem Zabolotnyi 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We study continual pre-training (CPT) as a mechanism for adapting general-purpose large language models to specialized domains: mathematics, instruction, code, and natural text. Using singular value decomposition of weight matrices, we find that CPT leaves singular value spectra largely invariant, with adaptation driven mainly by changes in singular vectors. An analysis of attention-head projection matrices reveals strong, domain-dependent head heterogeneity, which we exploit to define a head importance criterion: up to 60% of head updates can be removed without measurable quality loss. Selectively rewinding low-importance heads to their pre-trained state improves benchmark accuracy by up to 4% versus the fully trained baseline. Finally, we identify domain connectivity - linear interpolation between CPT checkpoints yields smooth domain-quality interpolation without notable degradation on either domain - and release Diffract, an open-source toolkit for scalable spectral analysis of billion-parameter models.

---


### 134. [Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models](https://arxiv.org/abs/2608.10864)

**<font color=#1a73e8>作者：</font>** Kiet T. Nguyen, Hanbo Shim, Jinwoo Kim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) have achieved strong image and video understanding, yet their visual-spatial representations remain geometrically fragile, leading to failures in spatial reasoning needed for embodied AI, robotics, and autonomous driving. Prior approaches to geometry grounding either fine-tune VLMs on spatial question answering, which can perpetuate spurious visual representations, or fuse features from large geometry-grounded vision models, which substantially increases model size at inference. Knowledge distillation from geometry-grounded vision models offers an alternative, but directly matching multi-view teacher features can disrupt the pretrained alignment between visual and textual representations, degrading object- and language-semantic capabilities. We propose multi-view relational distillation (MVRD), which distills patch-wise cosine similarities across views instead of the teacher features themselves. These relations encode geometric correspondences adequate for spatial understanding, while leaving the student representation underdetermined, allowing it to remain close to its pretrained vision- language space. Across representative VLMs, MVRD improves visual-spatial reasoning, outperforming supervised fine-tuning and feature distillation while approaching feature fusion methods with considerably fewer added parameters and lower latency. We show that MVRD makes visual representations more geometric while retaining language alignment, and generalizes to 3D scene understanding tasks such as object grounding, dense captioning, and question answering.

---


### 135. [Can Bayesian Optimization Efficiently Find a Strong Single Expert in Neural Thickets?](https://arxiv.org/abs/2608.10867)

**<font color=#1a73e8>作者：</font>** Nigel Bastian Cendra, Abdelhamid Ezzerg, Fernando Julio Cendra 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Gradient-free post-training has emerged as a compelling alternative to gradient-based optimization for large language models (LLMs), but existing approaches remain costly. We ask whether structured search can identify a strong single expert under a modest evaluation budget. Motivated by evidence that useful weight updates lie in low-dimensional subspaces, we apply Bayesian optimization within a random linear embedding of weight space. Our method requires no backpropagation and uses a Gaussian process surrogate to guide candidate evaluations efficiently. Across several reasoning benchmarks with Qwen2.5-Instruct models from 0.5B to 3B parameters, Bayesian optimization using five times less candidate evaluations matches or exceeds RandOpt. These results show that surrogate-guided search can substantially reduce the evaluation cost of gradient-free post-training while producing stronger deployable single experts.

---


### 136. [NullEdit: Stealthy Image Protection via VLM Condition Redirection](https://arxiv.org/abs/2608.10870)

**<font color=#1a73e8>作者：</font>** Weiyao Huang, Liqin Wang, Ziqi Sheng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Modern image editors combine vision-language models (VLMs) with diffusion transformer backbones to modify a single reference image according to instructions without fine-tuning. This capability also enables unauthorized manipulation of publicly released images. Existing inference-time defenses either invalidate edits through conspicuous corruption, thereby exposing the protection, or allow them to proceed with identity or reference content drift, thereby failing to prevent the editing behavior itself. We instead target a stealthy and harmless no-op in which the requested edit is suppressed, the output remains natural and source-preserving without conspicuous artifacts or identity replacement, and harmful semantics requested by malicious instructions are absent. We propose NullEdit, which targets the VLM representation jointly formed from the reference image and instruction before it conditions the downstream DiT backbone. Using normal-edit and no-edit anchors, NullEdit redirects this representation, while cross-prompt gradient averaging transfers protection to held out instructions. Across Step1X-Edit and Qwen-Image-Edit on CelebA-HQ and VGGFace2, NullEdit reduces the EditReward IF score by 0.813 on average relative to the SOTA baseline while preserving subject identity and source content.

---


### 137. [VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World?](https://arxiv.org/abs/2608.10875)

**<font color=#1a73e8>作者：</font>** Xiaohongshu Inc  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM) agents are increasingly deployed as personal assistants. Existing evaluations, however, mostly use short, self-contained requests in static environments. Everyday life assistance is different. A task runs for weeks rather than minutes. The world keeps changing while the agent is not being prompted. Many constraints are never stated outright. An agent that merely answers the request in front of it will fail at such a task. What is needed instead is an agent that stays proactive and consistent. It decides on its own when to act, when to ask, and when to stay silent. It notices changes that nobody announced. It keeps one plan coherent from the first day to the last. No current benchmark measures this. We introduce VibeLifeBench, a benchmark of 200 long-horizon tasks across ten everyday-life domains. Each task is a scripted multi-week timeline in a simulated world of 22 mock services. The world advances on its own clock, and many of its changes are silent, so only an agent that re-inspects the world discovers them. Every task is graded by fine-grained, weighted checks that read only what the agent actually left behind, covering the end state, the timeliness of its actions, and whether it upheld the implicit constraints. We evaluate seven frontier models. All of them score low, which shows how far current agents are from assisting with real life. We will open-source all tasks, environments, and the evaluation framework.

---


### 138. [ConfTriage: A Calibration-Aware LLM Triage Framework for Pulmonary Nodule Malignancy with Selective Specialist Deferral](https://arxiv.org/abs/2608.10885)

**<font color=#1a73e8>作者：</font>** Md Rabiul Islam, Samir Abdaljalil, Erchin Serpedin 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Pulmonary nodule malignancy prediction typically depends on image-trained specialist deep learning (DL) models that require substantial annotated imaging data and task-specific training. We investigate whether a generalist large language model (LLM), reading only a faithful natural-language rendering of standard nodule attributes, can serve as a calibrated triage layer. We propose ConfTriage, a confidence-calibrated method built on three pillars: language as the modality, calibration as the safety mechanism, and a selective specialist DL backstop for low-confidence cases. We prove two guarantees: a finite-sample combined-error bound yielding an explicit per-threshold operational certificate, and an oracle inequality showing that excess risk over the Bayes-optimal deferral classifier is controlled by the L1 calibration error of the LLM probability. A controlled seven-way input ablation across five frontier LLMs on LIDC-IDRI shows that natural-language descriptions dominate the diagnostic signal, while low-level image statistics are essentially diagnostically vacuous. ConfTriage achieved an F1 score of 88.22% and an AUC of 0.92, resolving 76.5% of cases using zero-shot LLM inference alone and referring only uncertain cases to the specialist DL backstop. These results demonstrate that clinically meaningful diagnostic information can be captured through structured radiological descriptions and leveraged by calibrated LLMs for selective referral. The framework suggests a practical pathway for combining generalist LLM prediction with specialist AI models in medical decision-support systems. Source code is publicly available at this https URL.

---


### 139. [ReOrder-OPD:Reliability-Aware Prompt Ordering for On-Policy Distillation](https://arxiv.org/abs/2608.10905)

**<font color=#1a73e8>作者：</font>** Ximo Zhu, Ruiqi Liu, Rong Wang 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) applies token-level teacher supervision to student-generated trajectories, but this supervision is not always reliable. Existing methods use local confidence or teacher-student agreement to weight, filter, or truncate the sampled trajectory. These signals do not directly determine whether the teacher can continue a student prefix to a correct answer, and trajectory-level interventions can conflate one rollout's unreliability with low expected training value of its prompt. We define prompt-level teacher continuation reliability $R$ as the teacher's probability of reaching a correct answer from a student prefix, averaged over prefixes and trajectories induced by the current student. Oracle experiments show that high-$R$ prompts yield larger OPD gains and that descending-$R$ training outperforms random and ascending orders on a fixed prompt pool. Because estimating $R$ requires many teacher continuations, we use the maximum ROUGE-5 F1 between one independent student rollout and verifier-correct same-prompt teacher trajectories. Across ten equal-frequency bins of this actual score, mean $R$ rises monotonically, showing that the proxy separates coarse reliability levels. ReOrder-OPD sorts prompts by the proxy, then draws independent on-policy training trajectories for vanilla OPD. It improves every matched aggregate comparison across Qwen3 and Gemma4 mathematics settings and Qwen3 code settings. Gains in all six FiRe-OPD and ExOPD settings show that prompt ordering complements within-trajectory supervision.

---


### 140. [Order Matters: LVLMs as Judges for Temporal Reasoning in Image Sequences](https://arxiv.org/abs/2608.10908)

**<font color=#1a73e8>作者：</font>** Martina Ianaro, Guilherme Fernandes, Maurizio Gabbrielli 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> As generative multimedia evolves from static image synthesis to complex, interleaved visual narratives, a foundational bottleneck has emerged: the judgment crisis. While human perception naturally synthesizes the temporal and logical flow of a story, automated evaluation systems remain largely "blind" to sequential continuity, often failing to distinguish between a coherent narrative and a semantically shuffled or contradictory sequence. This work identifies a critical structural gap in current multimodal evaluation paradigms, arguing that the reliance on Large Vision-Language Models (LVLMs) as judges is fundamentally limited by architectural biases. Our analysis reveals a profound performance dichotomy: while models may appear competent in isolated pointwise scoring, they suffer a catastrophic collapse when required to perform pairwise discrimination of temporal order. We demonstrate that this is not merely a data-scarcity issue but a structural one. Through a series of diagnostic probes, we uncover systematic positional asymmetries, specifically primacy and recency effects, where a model's judgment of a story is significantly influenced by the placement of a frame, often more than by its semantic consistency. These biases, potentially rooted in causal masking and rotary embeddings, suggest that current transformer-based judges are inherently ill-equipped for long-form visual reasoning. By exposing these blind spots, we challenge the multimedia community to move beyond snapshot-centric metrics and instead pioneer Temporally-Aware Evaluation paradigms that treat visual sequences as unified logical structures rather than unordered collections of frames.

---


### 141. [FaithformBench: Benchmarking Faithfulness of Mathematical Chain-of-Thought Autoformalisation](https://arxiv.org/abs/2608.10916)

**<font color=#1a73e8>作者：</font>** Rob Cornish, Iacopo Ghinassi, Po-Hung Yeh 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Autoformalisation (AF) systems map natural language reasoning steps into formal statements in a proof assistant such as Lean. We consider how to assess the faithfulness of these systems. Existing approaches require expensive human-annotated ground truth, or rely on LLM judges or embedding models, which come with limited guarantees of accuracy. In addition, these methods typically only consider inputs that are known to be correct, and therefore do not assess whether the AF translates incorrect inputs faithfully. To address these limitations, we propose a new benchmark for AF faithfulness that is cheap to apply, sound under weak assumptions, and assesses both positive and negative examples. Our method is based on automatically generating perturbed reasoning steps that are designed to be invalid, and then measuring validity preservation on unperturbed steps and invalidity preservation on perturbed steps. We apply our method to eight AF systems across four mathematical datasets, and observe pervasive sycophancy: many AFs "silently correct" invalid inputs into provable statements. The most validity-preserving fine-tuned AFs are also the most sycophantic, suggesting a tension between validity and invalidity preservation in current AF systems.

---


### 142. [IO Factory: Simulating AI-Enabled Influence Campaigns at Scale](https://arxiv.org/abs/2608.10920)

**<font color=#1a73e8>作者：</font>** Lukasz Olejnik, Wenchao Dong, Jonas R. Kunst 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce IO Factory, an AI-driven framework for simulating information and influence campaigns as fully integrated, traceable processes. The threat of digital manipulation now extends beyond persuasive text from individual language models to AI swarms, i.e., persistent groups of coordinated agents that adapt to platform feedback and disguise organized campaigns as ordinary social interaction. Because such campaigns cannot be identified from isolated messages alone, they must be analyzed across a continuous spectrum of planning, platform action, exposure, interpretation, measurement, and adaptation. IO Factory represents this process inside a controlled simulated platform, linking actor roles, platform actions, exposure records, structured model-based evaluations, and configured changes in the simulated population. We implement the architecture and evaluate it across configurations of up to 100,000 agents. The results show that IO Factory executes campaign timelines at scale and produces inspectable evidence of exposure and measured movement in configured belief variables. By recording the actors, objectives, action constraints, exposure paths, and measurement rules used in each run, IO Factory supports reproducible research and red-team analysis of coordinated influence.

---


### 143. [ThinkRetrieve: Retrieval-Augmented Reasoning Traces for Test-Time Scaling](https://arxiv.org/abs/2608.10928)

**<font color=#1a73e8>作者：</font>** Vaibhav Singh, Soumya Suvra Ghosal, Sarvesh Gharat 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Reasoning Models (LRMs) improve performance by allocating additional inference-time compute to generate extended chain-of-thought reasoning. However, recent studies reveal that sequential test-time scaling often yields diminishing or even negative returns, as longer traces exhibit increased uncertainty, error compounding, and drift from the original problem. We propose ThinkRetrieve, a test-time scaling framework that augments the reasoning traces of LRMs with dynamically retrieved solved examples at each reasoning step. Given an external corpus of problems paired with step-by-step solutions, ThinkRetrieve retrieves relevant exemplars at each intermediate step and injects them directly into the thinking trace, providing the model with guidance on how to reason rather than merely what facts are relevant. Experiments across five reasoning models (1.5B--8B parameters) on GSM-8K, MATH-500, AIME 2025, and SciQ demonstrate that ThinkRetrieve consistently improves accuracy over standard test-time scaling, with relative gains of up to $60\%$ on AIME 2025.

---


### 144. [Temporally Grounded Compositional Camera Motion Understanding via Geometric Knowledge Distillation](https://arxiv.org/abs/2608.10932)

**<font color=#1a73e8>作者：</font>** Dazhao Du, Shiyan Du, Jian Liu 等 11 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Understanding camera motion is fundamental to video perception, with applications in spatial intelligence and controllable video generation. Multimodal large language models (MLLMs) provide a natural interface for this task, but existing work typically assigns one or more labels to an entire clip. Such clip-level recognition overlooks two defining properties of real camera motion: it can change within a shot, and multiple movements can occur simultaneously. We therefore formulate camera-motion understanding as temporally grounded, compositional recognition, which requires a model to localize motion-consistent intervals and identify every movement active within each interval. We introduce CamChoreo, a benchmark of 4,229 real single-shot clips with expert-annotated temporal segments. Its annotations use a compact vocabulary of 20 direction-aware labels, and nearly half of the segments contain compound camera motion, with multiple movement primitives active simultaneously. Recognizing such fine-grained, compositional motion is hard for current MLLMs, whose visual encoders emphasize semantic content rather than the geometric evidence on which camera motion depends. Directly injecting features from a frozen 3D foundation model addresses this gap, but requires running the expensive geometry model on every input; we refer to this baseline as CamInject. We instead propose CamDistill, which distills the same geometric knowledge into lightweight camera tokens during training and removes the 3D model at inference. CamDistill matches the accuracy of direct feature injection without running the 3D teacher at inference. Together, CamChoreo and CamDistill advance camera-motion understanding from clip-level labeling to temporally grounded, compositional recognition. Project page: this https URL.

---


### 145. [A Cost-Efficient Routing Pipeline for Multilingual Short-Text Classification Using Small Language Models](https://arxiv.org/abs/2608.10939)

**<font color=#1a73e8>作者：</font>** Wajdi Ben Saad, Safa Madiouni  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multilingual short-text classification supports operational systems such as content moderation, customer support routing, and intent recognition, yet aggregate evaluation often hides large differences between high-resource and low-resource languages. Uniform inference policies are simple to deploy, but they assume that all languages are equally well served. In this work, we evaluate a fixed-list routing strategy that keeps stronger languages on a direct multilingual path and selectively sends weaker languages through translation into English before zero-shot classification. The pipeline is fully self-hosted, uses pretrained compact sentence encoders, and requires no task-specific fine-tuning.
We test the approach on two benchmarks chosen to differ in scale and label granularity: a 15-language subset of SIB-200 for seven-way topic classification and a 15-locale subset of MASSIVE for intent classification over an official 60-intent inventory. On SIB-200, the best overall configuration is R1, which translates only the low-resource tier: high-tier and mid-tier Macro-F1 remain unchanged, while low-tier Macro-F1 rises from 0.4632 to 0.6828. On the MASSIVE subset, the same low-tier intervention raises low-tier Macro-F1 from 0.2143 to 0.4417, but the best overall result is obtained by full translation, R3, at Macro-F1 0.4647. Across these two benchmarks, selective translation is a reliable intervention for weaker languages, whereas the optimal routing boundary depends on the task. We therefore report routing through tier-level quality gains and tier-level latency rather than a single global efficiency score.

---


### 146. [Mixture-of-Experts-based Entropy Model for Learned Image Compression](https://arxiv.org/abs/2608.10947)

**<font color=#1a73e8>作者：</font>** Jonas Brenig, Radu Timofte  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Learned image compression has seen significant progress in recent years with the development of end-to-end learned models that achieve better compression efficiency than state-of-the-art conventional methods. Recently, Mixture of Experts (MoE) approaches have seen promising results in NLP and computer vision tasks. In this paper, we introduce the MoE approach to learned image compression. We propose a MoE-based Entropy model (MoEE) for learned image compression, allowing the model to selectively activate only the subset of parameters required for the input image. Our model achieves a BD-Rate improvement over VVC of -16.85% on the Kodak dataset.

---


### 147. [StreamFlow: Dynamic Memory Flows for Streaming Video Understanding](https://arxiv.org/abs/2608.10949)

**<font color=#1a73e8>作者：</font>** Muxin Fu, Yifan Zhang, Wentao Zhang 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Streaming video understanding requires multimodal large language models (MLLMs) to preserve relevant evidence from continuously evolving streams under strict causality and bounded memory. Yet existing paradigms remain limited: model-based methods require intrusive backbone updates, while memory-based methods expend substantial visual-encoding computation on temporally redundant content and rely on rigid access to visual history. To address these limitations, we introduce StreamFlow, an efficient visual memory framework that enables dynamic, on-demand access to historical visual information. StreamFlow combines a lightweight, dynamics-aware mid-term memory that filters temporal redundancy before visual encoding with a latent long-term memory that consolidates historical video content into visual latents accessible to subsequent reasoning. During generation, an attention-guided retrieval mechanism injects relevant visual latents when the model's reliance on visual evidence weakens. StreamFlow achieves state-of-the-art streaming video understanding performance, reaching 67.73% overall accuracy on StreamingBench, while also delivering strong performance on offline long-video benchmarks. Relative to the vanilla setting, it improves the visual attention score (VAS) by 59.1% while reducing end-to-end latency and peak memory by 50.4% and 21.1%, respectively, enabling more visually grounded and efficient reasoning.

---


### 148. [Evidence-Grounded Trustworthy Multimodal Reasoning and Evaluation Benchmark in Complex Urban Scenes](https://arxiv.org/abs/2608.10954)

**<font color=#1a73e8>作者：</font>** Zhaoyang Wei, Bowen Jiang, Xumeng Han 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> While Multimodal Large Language Models (MLLMs) demonstrate impressive performance in benign scenarios, their cognitive reliability deteriorates significantly in complex scenes under adverse conditions. In these settings, models often rely on implicit inference without sufficient visual evidence, leading to a disconnect between perception and reasoning. Meanwhile, existing outcome-oriented benchmarks evaluate only final predictions and fail to diagnose failures in the underlying reasoning process. To address this gap, the authors propose AD2-Bench, which introduces a Hierarchical Visual Diagnosis framework that decomposes reasoning into a structured Chain of Evidence (CoE). This fine-grained diagnosis reveals that robust multimodal reasoning fundamentally depends on accurate evidence acquisition. Building on this perspective, the authors formulate reasoning from a probabilistic viewpoint and identify two primary causes of reasoning failure: Spatial Ambiguity, where models fail to distinguish target objects from background clutter, resulting in localization errors; and Semantic Uncertainty, where degraded visual features lead to incorrect semantic interpretation, resulting in understanding errors. To overcome these evidence deficiencies, they further propose Evidence-grounded Visual Reasoning (EGVOR), which replaces implicit reasoning with the explicit generation of Evidence Atoms - structured spatial-semantic triplets that enforce tight alignment between localization and semantic understanding. The model is trained through a hierarchical curriculum that progresses from reflective supervision construction to reinforcement learning, where reducing reasoning variance is explicitly rewarded. Extensive experiments demonstrate that EGVOR substantially improves reasoning stability under adverse conditions, providing a more robust framework for trustworthy multimodal cognition.

---


### 149. [REAP: Relation-Aware Elicitation and Parsing for Closed-Book Knowledge Base Construction from LLMs](https://arxiv.org/abs/2608.10963)

**<font color=#1a73e8>作者：</font>** Thanh-Dan Bui, Thanh-Trung Do, Tuan-Phong Nguyen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> We present the REAP system for the AKBC Shared Task 2026 on constructing knowledge bases from language models in a closed-book setting, subject to a budget of at most 32B parameters and no model fine-tuning. Our system combines structured chain-of-thought reasoning, relation-specific query strategies, and a reasoning-based empty-set gate to elicit parametric knowledge, followed by direct extraction into valid JSON arrays. On the test set, the system, built on the Mistral-Small-24B-Instruct-2501 model, achieves a macro-F1 score of 0.62, with particularly strong results on countryLandBordersCountry (F1 = 0.95), companyTradesAtStockExchange (F1 = 0.73), and hasArea (F1 = 0.77). Our code is publicly available at this https URL.

---


### 150. [CARE: Confidence-Aware Reasoning for Reliable Medical VQA](https://arxiv.org/abs/2608.10964)

**<font color=#1a73e8>作者：</font>** Yuetian Du, Yucheng Wang, Zhenyuan Chen 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Reinforcement Fine-Tuning (RFT) has enabled medical Multimodal Large Language Models (MLLMs) to produce Chain-of-Thought (CoT) reasoning for visual question answering, yet these models suffer from $\textit{confidence miscalibration}$---a systematic gap between expressed certainty and actual diagnostic accuracy that undermines clinical trust. We propose $\textbf{CARE}$, a $\textbf{C}$onfidence-$\textbf{A}$ware medical $\textbf{RE}$asoning framework that jointly optimizes accuracy and calibration through a dual-stage pipeline. First, a scalable Medical-CoT synthesis provides structured cold-start data for Supervised Fine-Tuning. Second, Group Relative Policy Optimization (GRPO) with a novel $\textbf{Confidence-Aware Reward (CAR)}$ mechanism ties the model's confidence to diagnostic correctness within the reward signal. Across three Medical VQA benchmarks, $\textbf{CARE}$ achieves the highest diagnostic accuracy while obtaining the lowest Expected Calibration Error and Hallucination Rate, establishing a foundation for trustworthy clinical decision support. Our code is available at this https URL.

---


> [!TIP]
> 当前位于：**101-150**（第 3/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-184](./part-04.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
