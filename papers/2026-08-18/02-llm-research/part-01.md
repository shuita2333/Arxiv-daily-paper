# 🧠 大模型相关研究 | 2026年08月18日

> 本类共 **144** 篇论文：已确认 **138** 篇，待复核 **6** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-144](./part-03.md)

---

### 1. [Proxy-Validated LLM UX Micro-Simulations: An Artifact-First Protocol for Early-Stage Decision Support](https://arxiv.org/abs/2608.13563)

**<font color=#1a73e8>作者：</font>** Alexandre Cristovão Maiorano  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Early-stage teams often lack users, time, and budget to run repeated UX studies, yet still need decision-oriented signals to iterate safely. We study an LLM-driven UX micro-simulation pipeline that generates structured customer-experience feedback (walkthrough steps, friction points, micro-survey signals) from versioned prompts, personas, tasks, and UI snapshots. Because public usability datasets with task outcomes are scarce, we validate simulated friction themes using multiple public proxy corpora (app reviews, support tweets, and open-source software issues). We propose a lightweight proxy-validation protocol with two alignment metrics: top-k Jaccard and distributional weighted-Jaccard (W), and compare lexical, TF-IDF, and multilingual embedding baselines across six proxy datasets. Embedding-based alignment yields higher W than lexical baselines on primary app-review and support-tweet proxies (e.g., W=0.128 vs 0.000 on Gojek), while top-k Jaccard is shown to overstate alignment at large k. We ablate four agent strategies (single-pass, best-of-N, hybrid, and a proposed score-then-select judge) across Azure OpenAI deployments and report bootstrap confidence intervals over 8 method-dataset pairs; these intervals reveal that the embedding W point estimate is systematically unstable under resampling at our subsample size. We also provide a failure-mode analysis of grounding and fabrication proxies, with documented calibration caveats and worked examples of outputs flagged as fabricated by an adversarial judge. Our artifact-first pipeline produces reproducible tables and figures from versioned run artifacts, supporting iterative prompt and taxonomy refinement before final paid-model calibration.

---


### 2. [Inducing Reward-Free Judging Rubrics that Reduce Over-Crediting in Agent Evaluation](https://arxiv.org/abs/2608.13564)

**<font color=#1a73e8>作者：</font>** Darragh Quinn, David Dylan, Roisin Healy 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Evaluating language-model agents at scale increasingly relies on a second language model as an automatic judge, because the gold signal, an executable environment reward, is expensive, slow, or unavailable at deployment time. Such a judge is a reward-free proxy whose value depends on whether it can be trusted, yet existing judges either hand-write the scoring rubric, as in G-Eval, or fine-tune the judge's weights, and both tend to credit fluent but unsuccessful trajectories as successes. We instead induce the text of an agent-judging rubric from a small set of ground-truth-labeled trajectories, grounding it in true outcomes. We present RubricForge, which evolves a judge rubric by reflective evolution against labeled trajectories to maximize agreement with the environment reward, freezes it, and applies it to held-out trajectories in one model call with no environment access. The optimized artifact is human-readable text, so every verdict is attributable to named criteria. Using one frozen 7B model as both agent and judge, on tau-bench (173 labeled trajectories drawn from 220 rollouts) and WebShop (160), the principal gain is faithfulness rather than raw agreement. The edge over a generic G-Eval judge is not statistically significant (McNemar p = 0.248), and absolute-score calibration marginally favors the generic judge (|err| difference -0.048, p = 2x10^-4). Yet RubricForge over-credits failed trajectories roughly half as often (0.115 vs. 0.173 false-pass rate on tau-bench, with three over-credit catches and zero reversals) and ranks graded WebShop outcomes more faithfully (Spearman 0.410 vs. 0.370). For a reward-free evaluator the false-pass rate, not aggregate agreement, is the deployment-relevant quantity, since a false pass ships a broken agent whereas a false fail merely costs a retry.

---


### 3. [Depth-Aware Sensitivity Analysis of Mixture-of-Experts Models via Magnitude-Based Expert Masking](https://arxiv.org/abs/2608.13565)

**<font color=#1a73e8>作者：</font>** Pradeep Kumar Sharma, Shantanu Godbole, Hritvik Shrivastava  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Mixture-of-Experts (MoE) architectures scale large language models (LLMs) while preserving computational efficiency through sparse activation. Despite their widespread adoption, the relative importance of individual MoE layers remains insufficiently characterized, particularly for model compression. This paper presents a systematic layer-wise sensitivity analysis of the Qwen3.6-35B-A3B model (40 MoE layers, 256 experts per layer, top-8 routing) using magnitude-based expert masking on the XLCoST cross-lingual code translation benchmark. We conduct a multi-phase study spanning 100, 300, and 500 prompt evaluation scales across three H100 GPU servers. Our central finding is that layer sensitivity is strongly depth-dependent: early layers (0-9) and middle layers (10-29) are highly fragile to expert masking, while late layers (30-39), and especially very-late layers (35-39), tolerate aggressive masking of low-magnitude experts. Flat all-layer masking at 30% retains only 150/300 Good+Similar outputs at 300-prompt scale, whereas late-focused policies retain 249-255/300 while masking 640-1,145 experts. On a later 500-prompt held-out validation slice, the narrow very-late policy (layers 35-39 @ 50%) achieves the strongest quality/masked-expert tradeoff among tested candidates, retaining 419/500 Good+Similar outputs while masking only 640 of 10,240 total experts. We additionally characterize top-k routing width reduction from 8 to 6 active experts per token, which shows a large observed wall-clock reduction on a 100-prompt probe with no Good+Similar loss, though it does not yet compose cleanly with aggressive expert masking. These findings provide an empirical foundation for depth-aware MoE expert masking and establish a practical path toward physical weight surgery, activation-based expert scoring, and training-based recovery.

---


### 4. [Don't Claim Benchmark-Oriented Optimization Improves General Coding Capability -- Diverse Evaluation Is Required](https://arxiv.org/abs/2608.13566)

**<font color=#1a73e8>作者：</font>** Egor Shibaev, Vera Kudrevskaia, Timur Galimzyanov 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Post-training papers, model cards, and blog posts often treat scores on a small set of coding benchmarks (e.g., SWE-bench and LiveCodeBench) as evidence of broad coding capability, both for research artifacts and user-facing systems. We argue that optimization for these benchmarks leads to measuring task-specific performance, creating a meaning gap between measured scores and claims of general coding ability. We examine this gap with a Django-based case study benchmark suite we create.
Evaluating foundation models and checkpoints post-trained on SWE-bench trajectories, we find that benchmark rankings frequently fail to generalize. Post-trained checkpoints show little cross-task transfer, and SWE-bench optimization yields limited or no gains on our tasks or on LiveCodeBench. Similarly, fine-tuning on individual Django modalities fails to transfer.
We conclude that a small number of benchmarks is insufficient for evaluating diverse models under benchmark optimization pressure. We encourage the community to use differentiated evaluation - holistic assessment for frontier models, multi-task suites for research, and human-in-the-loop studies for narrow task applications. Finally, we argue for creating a capability taxonomy and sustained benchmark maintenance, rather than one-off benchmark releases. Without reliable evaluation standards, engineers and researchers using LLMs and agents have to rely on insufficient evidence to make research, development, and deployment decisions.

---


### 5. [Modular Cognitive Architecture Emerges in Large Language Models](https://arxiv.org/abs/2608.13567)

**<font color=#1a73e8>作者：</font>** Pengrui Han, Jacob Andreas, Evelina Fedorenko 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The human brain exhibits a striking degree of functional specialization, with distinct networks supporting language, formal reasoning, reasoning about other minds, and reasoning about the physical world. Is this modular organization a fundamental principle of how intelligent systems must be built, or an evolutionary accident specific to biological brains? Here, we test whether a similar organization emerges in Large Language Models--another class of intelligent systems created through a very different optimization process. Using circuit analyses across N=46 tasks spanning four cognitive domains (language, formal reasoning, social reasoning, physical reasoning), we find that LLMs develop a modular architecture that mirrors the human brain: tasks drawing on the same network in humans recruit overlapping neurons in LLMs, whereas tasks drawing on different networks recruit distinct neurons. The convergent emergence of modularity in brains and neural networks suggests that it may be a fundamental property of intelligent systems.

---


### 6. [Does a Language Server Save Tokens for Coding Agents? A Measurement Methodology and Preliminary Study](https://arxiv.org/abs/2608.13568)

**<font color=#1a73e8>作者：</font>** Pengcheng Xu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Coding agents spend most of their context budget on retrieval. Lexical retrieval (grep) is universal, instant, and zero-setup, but noisy: it cannot tell a definition from a call from a comment. Semantic retrieval via the Language Server Protocol (LSP) is precise and typed, but needs a running, indexed server and pays a per-symbol round-trip. The claim that semantic retrieval is more token-efficient is, we find, asserted almost everywhere and measured almost nowhere: no public source isolates the LSP-vs-lexical token delta for an agent at equal task-success. This paper formalizes the question with one metric (tokens-to-success), specifies a five-arm ablation isolating semantic retrieval from confounds, maps three pre-stated failure modes onto measurable variables, and reports a preliminary study (Python and TypeScript repos; Claude Opus 4.8, Sonnet 4.6, Haiku 4.5). The answer is conditional and usually negative. On symbol-named localization the LSP costs tokens (+6% to +118%) and the agent ignores it when free. On reference-completeness it buys precision but not token savings and cannot raise the recall ceiling set by agent thoroughness; it saves tokens only for the weakest model. Tool choice is task-dependent: models default to grep on localization (0-6% semantic use) but reach for the LSP about half the time on reference tasks, unprompted. On edits scored by real test execution the gap is starkest: grep solves multi-file renames perfectly, a location-only LSP fails three-quarters of them by missing a call site, and even a complete, index-warmed, text-enriched LSP (each reference's line inline, as production LSP-MCP servers do) recovers most of the gap but cannot close it, since a rename must touch comments and strings that semantic references exclude. The implication is not LSP-always but an adaptive router keyed on task class, model capability, and lexical noise.

---


### 7. [Think in Latent, Explain in Language: Self-Explainable Latent Reasoning](https://arxiv.org/abs/2608.13570)

**<font color=#1a73e8>作者：</font>** Dayuan Zhao, Shengcao Cao, Yu-Xiong Wang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Latent reasoning has emerged as a powerful alternative to text-based Chain-of-Thought (CoT), offering significant gains in computational efficiency by compressing verbose reasoning into compact embeddings. However, compressing reasoning into the latent space renders the thinking opaque, hindering its interpretability. Current methods present a stark trade-off: they either function as unexplainable ''black boxes'' (e.g., Coconut), where the latent reasoning is not human-readable, or rely on separate post-hoc decoders for explainability (e.g., Heima), introducing architectural overhead and decoupling the explanation from the actual reasoning process. In this work, we present a unified framework for Self-Explainable Latent Reasoning (SELR) that trains a single model to perform efficient and inherently explainable latent reasoning. Our core contribution is a novel multi-task training objective that optimizes for two goals simultaneously: (1) an Answer Loss that optimizes the latent reasoning trajectory to produce accurate final answers, and (2) a CoT Loss that explicitly trains the same model to decode its own latent representations back into human-understandable reasoning steps. This design ensures that generated latent representations are both task-effective and semantically interpretable, eliminating the need for external decoders. We validate the effectiveness of SELR on both Large Language Models (LLMs) and Vision-Language Models (VLMs), demonstrating that SELR achieves superior token efficiency and accuracy compared to baselines, while uniquely providing self-contained explainability without auxiliary models. Project page is available at this https URL.

---


### 8. [Not All Tokens Are Equal: Inflation-Aware Routing for Agentic LLM Systems](https://arxiv.org/abs/2608.13571)

**<font color=#1a73e8>作者：</font>** Heming Fu, Shan Lin, Qianqian Xie 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> When a language model fails to answer a query on the first attempt, an agentic system retries, consuming additional tokens each time. This retry overhead creates a gap between what a model's per-token price implies and what a full workflow actually costs. We call this gap \emph{token inflation} and define it as the ratio of true workflow cost to single-call cost. Systems like FrugalGPT route based on the latter, which can underestimate real cost by more than $2\times$ on difficult tasks. We address this with InflationAgent, a four-stage router that (1) measures token inflation systematically across model tiers and task types, finding inflation as high as $4.25\times$ for a 7B model on multi-hop question answering; (2) introduces CoT Branching Entropy (CBE), a pre-execution difficulty signal computed entirely from local inference, which predicts high inflation with AUROC 0.887; and (3) selects models by maximizing a Semantic Exchange Rate (SER) that divides expected accuracy by predicted true cost, with a fresh-escalation policy that discards failed chains before routing to a stronger model. On GSM8K under a fixed budget, InflationAgent achieves 94.7\% accuracy versus 91.0\% for FrugalGPT while using 31\% fewer tokens, and we show that forwarding a failed reasoning chain to GPT-4o reduces its accuracy by up to 34.8 percentage points, validating the fresh-escalation design.

---


### 9. [A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing](https://arxiv.org/abs/2608.13573)

**<font color=#1a73e8>作者：</font>** William Nixon, Jon Durbin, Florian Standhartinger 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large Language Model (LLM) serving has become a critical cloud workload, and realistic traces are essential for motivating and benchmarking serving systems. However, existing LLM serving workload studies remain limited in scale and scope. They often observe short time periods and provide limited visibility into how users interact with models in production. As a result, they do not fully capture how LLM serving workloads evolve over time or how user-model interactions shape production traffic.
In this work, we further the understanding of real-world LLM serving workloads through both a global characterization and a longitudinal study of a one-year production trace from Chutes. Unlike prior studies, our trace captures full production behavior across many models and users, including both popular and long-tail models. We analyze the workload from aggregate, temporal, model-level, and user-level perspectives, revealing workload evolution and user-model structure that are typically hidden behind aggregate views. To support future research, we will release the full one-year trace with the paper, enabling downstream studies of production behavior without relying on sampled or synthetically generated workloads.

---


### 10. [Agentao: A Governed Local-First Runtime for Tool-Using LLM Agents](https://arxiv.org/abs/2608.13574)

**<font color=#1a73e8>作者：</font>** Bo Jin, Qiang Jiao, Xin Tong  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents increasingly operate as execution systems that invoke tools, modify local state, use persistent memory, and interact with external protocols. These capabilities make agents useful, but they also introduce risks related to over-privileged actions, weak auditability, prompt injection, tool poisoning, and uncontrolled side effects. This paper presents Agentao, a governed local-first runtime for tool-using LLM agents. Agentao separates model-generated action proposals from host-authorized execution through a layered architecture consisting of host-facing surfaces, a host contract, a runtime core, a permission-mediated tool system, and supporting subsystems for memory, replay, plugins, skills, sub-agents, and protocol integration. We describe the motivation, threat model, design goals, governance model, execution pipeline, and structured event interface of the system. Agentao does not provide formal safety guarantees; rather, it demonstrates how permissions, state, protocol boundaries, and execution traces can be made explicit runtime abstractions for building agents that are more governable, inspectable, and suitable for host-controlled local environments. The code is publicly available at this https URL.

---


### 11. [BCIJelly: An integrated ecosystem for brain-computer interface research](https://arxiv.org/abs/2608.13576)

**<font color=#1a73e8>作者：</font>** Liyuan Han, Xinrui Yang, Tianyu Zheng 等 15 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Brain-computer interface (BCI) research relies on multistage computational pipelines, yet progress remains constrained by fragmented data formats, heterogeneous decoder implementations and hardware-specific deployment toolchains, and researchers lack an integrated workflow. Here, we fill this gap with BCIJelly, a unified computational ecosystem that integrates 18 curated BCI datasets, 15 benchmark decoders and an algorithmic library of 80 reusable modules, an automated architecture search (AAS) procedure, and hardware-aware deployment through the toChip pipeline within a single Python framework. AAS constructs task-specific decoders without manual architecture design. It is further extended into a closed-loop mode guided by a large language model (LLM), which uses task specifications, module descriptions and search history to support multitask and cross-species decoding. The toChip pipeline compiles trained decoders for execution on neuromorphic chips, enabling energy-efficient deployment for BCI systems. An accompanying visualization software provides a graphical interface to the full workflow, making BCIJelly accessible without programming. We validate BCIJelly across five BCI paradigms (motor, visual, speech, emotion and auditory) with recordings from humans, macaques and mice, and single-task, multitask and cross-species decoding settings. BCIJelly establishes a unified and extensible infrastructure that bridges decoder development and hardware-aware deployment for BCI research.

---


### 12. [Jais 2: A Family of Arabic-Centric Open Large Language Models](https://arxiv.org/abs/2608.13580)

**<font color=#1a73e8>作者：</font>** Mohamed Anwar, Abed Alhakim Freihat, George Ibrahim 等 60 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Jais 2 is a family of Arabic-centric large language models developed jointly by MBZUAI, Cerebras, and Inception, designed to advance Arabic-centric language modeling, with strong performance across the Arabic and culturally grounded benchmarks evaluated in this report. The family includes, to our knowledge, the largest open Arabic-centric LLM trained from scratch at 70B parameters, and a competitive 8B-parameter variant among the evaluated open models. A custom Arabic-centric vocabulary enables efficient training and inference. In addition, an optimized architecture and training recipe yield highly compute-efficient training. With a substantially smaller token budget than comparable models, Jais 2 achieves strong Arabic performance on the benchmarks considered in this report and competitive English results. The models obtain leading results among the evaluated open models on OALL2 and AraGen. They also perform strongly on several culturally grounded Arabic benchmarks, including poetry, religion, cuisine, and dream interpretation, as well as in general tasks such as translation and summarization. We release the models in HuggingFace under a commercially permissive license. Jais 2 70B is also released as a chat app on the Web, iOS, and Android; it runs on Cerebras hardware, delivering up to 2,000 tokens per second, and enabling high-throughput Arabic-centric chat serving in our deployment setting. By uniting scale, linguistic diversity, cultural fidelity, openness, and speed, Jais 2 provides an open-weight foundation intended to support further research and development in Arabic-centric LLMs.

---


### 13. [From Prediction to Intervention: Personalized Meal-Level Glucose Regulation via an LLM Agent](https://arxiv.org/abs/2608.13581)

**<font color=#1a73e8>作者：</font>** Mingyu Huang, Weiqing Min, Ying Jin 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Personalized glucose regulation remains a central yet unresolved challenge in precision nutrition, as postprandial glucose response varies substantially across individuals. Existing approaches based on glycemic indices fail to adequately account for such heterogeneity and lack the mechanism to dynamically adjust meals based on personal physiological feedback. In this context, recent advances in LLM-based agents offer a promising direction, as they enable context-aware reasoning and iterative refinement. Inspired by this, we propose a physio-feedback agentic loop, a unified system that integrates individualized absorption modeling with dietary intervention to regulate glucose response. Specifically, we develop a Physiology-Aware Glucose Predictor to model individualized absorption dynamics through a learnable Temporal Physiological Absorption Decay Module. We then construct a Prediction-Driven Two-Stage Meal Optimization Agent that iteratively refines real-world meals using predicted outcomes as explicit feedback. Through extensive experiments on multiple public datasets, we demonstrate that our method not only improves prediction accuracy but also effectively reduces glucose excursions. To the best of our knowledge, this paper marks the first step in integrating physiological learning with an LLM-based agent for personalized glucose regulation.

---


### 14. [Beyond Simplification: DFT-GEN for Fidelity-Preserving Visual Accessibility in Dyslexia-Friendly Educational Texts](https://arxiv.org/abs/2608.13583)

**<font color=#1a73e8>作者：</font>** Jiaqian Yu, Chen Jason Zhang, Haoyang Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Dense educational texts impose avoidable reading friction on people with dyslexia, yet generic simplification can delete terminology, task constraints, or source evidence that readers still need. Stakeholder interviews with dyslexic adults and specialists reveal a core tension: reduced burden must not compromise information fidelity. We present DFT-GEN, a stakeholder-informed text transformation framework for content-heavy educational materials. Its central contribution is not a generic LLM refinement loop, but a dyslexia-specific accessibility layer that combines protected-span preservation with a deterministic Dyslexia Accessibility Controller (DAC) for rendered visual organization. DAC converts stakeholder and expert preferences into reproducible controls for visual-unit length, chunk spacing, source/task separation, highlighting budget, and reviewable risk flags. We therefore separate evaluation into DCFI, a fidelity-safety diagnostic, and B-DVAS-VL, a rendered visual-accessibility diagnostic. On 2,280 bilingual exam-style items, DFT-GEN preserves task-critical information while improving visual accessibility: it wins 93% in English and 64% in Chinese of B-DVAS-VL pairwise judgments against same-backbone controls, and in a controlled pilot with dyslexic adult readers it preserves answerability while reducing effort.

---


### 15. [FactorFlow: A Visual Analytics Workspace with Large Language Model-Assisted Interpretation for Factor Analysis](https://arxiv.org/abs/2608.13585)

**<font color=#1a73e8>作者：</font>** Justin Philip Tuazon, Joemari Olea, Richelle Ann Juayong  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> In exploratory factor analysis (EFA), one typically aims to extract and describe a small number of factors (i.e., latent variables) based on the relationships among numerous manifest variables (i.e., directly observable variables). In practice, performing EFA entails examining different factor models (and rotations) to identify the underlying latent structure. Now, the primary criterion for evaluating a factor model is interpretability. That is, the preferred model is the one that yields a meaningful, coherent, and theoretically defensible factor structure. However, gauging a model's interpretability is not a trivial task, as it is subjective and often requires keeping track of large amounts of information simultaneously. Because of this, researchers typically employ various visualizations to interpret models and determine the "best" one. Hence, we introduce FactorFlow, a visual analytics workspace for performing EFA end-to-end. Using FactorFlow, one can fit and rotate factor models, perform model diagnostics, and more. The main component of the tool is a dashboard with a comprehensive set of interactive visualizations, where a user can easily dissect a factor model and even compare two models side-by-side at the same time. Moreover, several large language models are integrated with FactorFlow, enabling the user to generate and assess automated factor interpretations written in natural language. With multiple views and readily available calculations, FactorFlow can enable the researcher to efficiently and effectively understand factors and ultimately, perform EFA. Finally, we conducted a usability study to identify strengths and weaknesses, and capture feedback to incorporate in the app.

---


### 16. [Student-ChatGPT Interaction Visible: Designing a Teacher Dashboard for EFL Writing Education](https://arxiv.org/abs/2608.13587)

**<font color=#1a73e8>作者：</font>** Minsun Kim, Seon Gyeom Kim, Suyoun Lee 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> We present a Prompt Analytics Dashboard (PAD) for teachers that can traces student-LLM interactions from EFL writing classes. PAD can show student prompt-response exchanges with LLM chatbot and English essay writing revision histories to support data-informed instruction and visibility in classes. Through two iterative co-design sessions with six EFL instructors, we distilled a compact trace taxonomy (misuse signals, goal-alignment cues, revision effort) and instantiated three interface views (overview, week/outcome filter, drill-down with evidence snippets). This pipeline summarizes potential misuse and alignment at class/cohort levels and attaches micro-explanations to reduce over-surveillance. Instructors reported reduced scanning burden and clearer timing for interventions.

---


### 17. [IterCOMP: Reasoning-aware Adaptive Prompt Compression for Multi-hop Question Answering](https://arxiv.org/abs/2608.13588)

**<font color=#1a73e8>作者：</font>** JungMin Yun, YoungBin Kim  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Multi-hop question answering requires complex reasoning across multiple evidence segments, which often overwhelms retrieval-augmented generation systems with lengthy and noisy contexts, thereby undermining both efficiency and accuracy. While existing prompt compression methods attempt to address this issue, they are typically designed for single-turn queries and fail to capture interdependent reasoning steps. We propose IterCOMP, a unified, training-free prompt compression framework that incorporates multi-hop reasoning within an iterative compression loop. IterCOMP decomposes documents into evidence segments, evaluates question answerability, and generates targeted follow-up questions to iteratively integrate essential evidence, producing a compact, reasoning-oriented prompt. Experiments on MusiQue, 2WikiMultiHopQA, and HotpotQA demonstrate that IterCOMP achieves substantial improvements in Exact Match and F1 scores while reducing the token budget, outperforming existing baselines and exhibiting robustness as reasoning complexity increases.

---


### 18. [Context Aware AI Assistant and AR Interface for Lunar Extravehicular Activity (EVA) Procedural Guidance](https://arxiv.org/abs/2608.13589)

**<font color=#1a73e8>作者：</font>** Rodrigo Gallardo, Qilmeg Doudatcz, Ganit Goldstein 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> As human space exploration returns to the Moon, astronauts need rapid access to procedural information during extravehicular activities (EVAs), where attention is divided across navigation, repair tasks, tool handling, and environmental risk. The challenge is not the absence of information, but surfacing the right information at the right moment. We present GAIN-AI (Guided Assistant for Intelligent Navigation), a context-aware AI assistant and minimal heads-up interface for procedural guidance in simulated lunar EVA. The system operates in two layers. The first grounds a large language model with structured context: EVA procedure documents, live telemetry data, and error-handling protocols encoded as JSON. The second restructures that output into three compact units for AR display: Goal, Task, and Verification. Evaluated on 111 synthetic EVA scenarios, the system scores 10.0/10 on nominal conditions and 8.15/10 on single-fault scenarios, with performance degrading on multi-fault and boundary-threshold cases.

---


### 19. [Stable Miscalibration in Large Language Models: A Practical View of High-Confidence Errors](https://arxiv.org/abs/2608.13591)

**<font color=#1a73e8>作者：</font>** Akira Okutomi  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> High-confidence errors in large language models are often treated as evidence of fragile internal inference. We study a different possibility: stable miscalibration, where a confident wrong answer remains locally stable under small perturbations. We combine two diagnostics: a label-aware output-level audit score that ranks domains by confidence variation and overconfident mistakes under a forced-answer baseline, and an internal sensitivity probe that measures hidden-state movement. On a multi-domain binary factual audit set, this audit score tracks where abstention-aware self-critique reduces decision loss, although direct labeled baselines rank the same gain more strongly. Internally, self-critical prompting consistently reduces hidden-state sensitivity across layers in three open-weight models. This supports prompt-induced local stabilization rather than a purely output-level abstention pattern, but it does not imply calibration: audit-defined overconfident errors are not clearly more locally sensitive than confidently correct answers, so some high-confidence errors may be stable and miscalibrated rather than simply fragile.

---


### 20. [Training-Free Knowledge Transfer Across Model Scales through Activation-Guided Pruning](https://arxiv.org/abs/2608.13596)

**<font color=#1a73e8>作者：</font>** Jiahe Fan, Si Chen, Yinghao Hou 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Heterogeneous model fusion seeks to combine models that differ in tasks, initializations, architectures, or scales. We study an underexplored cross-scale setting: improving a small recipient language model with a stronger donor despite substantial architectural mismatch. We ask whether useful capabilities can be transferred without explicit neuron-wise semantic alignment. Building on the observation that truncating a large model to a smaller architecture and injecting it with a tiny mixing weight can already improve the recipient, we propose Activation-Prune-Merge (APM), an activation-guided framework for cross-scale fusion. APM constructs task-conditioned activation maps on the donor, selects salient layers, hidden dimensions, attention heads, and MLP neurons to prune it to the recipient architecture, and injects the resulting donor slice into the original recipient using a micro interpolation coefficient. This formulation treats the donor as a source of concentrated functional components rather than requiring precise structural transplantation. Across 16 benchmarks spanning reasoning, mathematics, code generation, instruction following, and classification, APM improves the overall average accuracy from 55.5% to 60.6% over the original 3B recipient. RTE accuracy increases from 64.3% to 82.3%, QNLI from 52.3% to 65.7%, and BoolQ from 70.8% to 79.2%. Analyses of injection ratios and sequential multi-stage fusion further suggest that activation-guided extraction improves the quality of the transferable donor slice while preserving the small-ratio fusion regime. These results provide evidence that cross-scale heterogeneous fusion can succeed without explicit semantic alignment when the donor contribution is sufficiently concentrated and carefully selected.

---


### 21. [Measuring Cross-Task Behavioral Consistency in Language Model Agents](https://arxiv.org/abs/2608.13598)

**<font color=#1a73e8>作者：</font>** Amritesh Banerjee, Pranil Raichura  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agent evaluation relies almost entirely on outcome metrics such as success rate, which capture whether an agent succeeds but not how consistently it behaves. We argue that behavioral consistency across tasks is a distinct and measurable property, and we introduce the Behavioral Consistency Metric (BCM) to quantify it. BCM trains a model to predict task success from behavioral features of agent execution traces, derives a per-trajectory feature-attribution vector, and measures the mean pairwise similarity of these vectors within an agent system. Across roughly 9,000 trajectories from six language model agents on software engineering tasks, our central finding is that cross-task and within-task consistency are distinct axes that can diverge: some systems are locally reproducible, behaving similarly on repeated attempts at one task, yet globally fragmented, with no stable strategy across different tasks, while others are consistent at both scales. Prior work measures only same-task reproducibility and so cannot observe this separation. We further find that consistency is not reducible to success rate, since systems with comparable success can differ sharply in consistency, and that the frontier-versus-open-source consistency gap persists under a within-task control that holds task difficulty constant. We position BCM as a process-level reliability signal that complements outcome metrics, and we are explicit about the conditions under which it is meaningful.

---


### 22. [Active Perception for Embodied Disambiguation](https://arxiv.org/abs/2608.13605)

**<font color=#1a73e8>作者：</font>** Yiwei Liu, Luwei Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural language provides robots with a flexible task interface, but target ambiguity in embodied environments arises not only from user intent; it can also result from missing taskrelevant physical evidence in the current observation. Existing interactive disambiguation methods primarily obtain additional information by asking the user, whereas occlusion, restricted viewpoints, unreadable text, and unobserved targets require the robot to actively change its observation. We propose an active-perception framework for embodied target disambiguation that uses active observation as the backbone for information acquisition and uses a vision-language model to decide, on the basis of accumulated visual evidence and interaction information, whether to continue observing, request clarification, or complete target selection. Active observation can both directly recover missing discriminative evidence and reveal object names, labels, and semantic attributes, thereby improving user clarification when it remains necessary. Real-robot experiments show that the framework combines physical information acquisition and userintent clarification within a unified embodied disambiguation process.

---


### 23. [No Universal Signal Predicts Sample-Level LLM Regression under Version Updates](https://arxiv.org/abs/2608.13607)

**<font color=#1a73e8>作者：</font>** Jia Sheng, Yiwei Lu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Frontier LLMs are updated frequently and typically outperform their predecessors in aggregate. But aggregate gains say little about individual samples: an update can still cause sample-level regression, where a response correct under the old model becomes incorrect under the new one. This paper studies how to predict such regressions from signals available at inference time. We compare single-model signals (confidence, logit margin, attention entropy) against cross-version signals (output KL divergence, likelihood drift, token-level KL, representation drift) under a unified added-value test that isolates each signal's gain over a confidence baseline. Across six benchmarks in three task families (multiple-choice question answering, or MCQ; math reasoning; code generation) and six model update pairs, we find that (1) signal effectiveness is task-dependent: confidence is strongest on MCQ and simpler math, while likelihood/KL signals give the most frequent gains on harder math and code; (2) no signal is universally best across model updates either; and (3) some cross-version signals stay informative even when confidence fails, including without labels, which supports a proof-of-concept selective fallback that routes high-risk samples back to the old model. Practitioners can use these task-level patterns to choose which regression signal to trust for a given update. Code is available at this https URL.

---


### 24. [Evaluating Agentic Learning Harness Capabilities Without Labels via the Scaling Hypothesis](https://arxiv.org/abs/2608.13608)

**<font color=#1a73e8>作者：</font>** Aryan Luthra, Kshitij Jain, Siddharth Arya 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agentic "Continual Learning Harnesses", systems that pair an LLM with retrieval or memory to improve from feedback without retraining, have shown growing value in cybersecurity. But their value is conventionally measured by gains against labeled benchmarks, an approach that often fails in operational security settings. Benchmark labels are scarce, stale, and unrepresentative, so a practitioner often cannot tell whether a given harness helps at all or which of two is better for their task. Traditional LLM-as-a-judge offers little signal because it is no stronger than the agent it evaluates, and distillation is unreliable on scarce, sporadic, and biased labels.
We propose a framework for evaluating learning harnesses end-to-end without a labeled benchmark, grounded in the scaling hypothesis. A stronger teacher model provides sparsely sampled corrections to a smaller student with a continual learning harness. We score a harness by how much its student converges toward the teacher over time. Across security tasks, model families, and harness designs, we show that improvement relative to the teacher correlates with improvement relative to a held-out gold standard, validating teacher-relative lift as a proxy for true harness uplift when labels are absent. We further show that LLM-as-a-judge between similarly powered models yields no usable signal. These results suggest that a teacher-sized model can be improved through the same harness when humans provide the same kind of sparse, high-precision corrections.

---


### 25. [SemPlan: Benchmarking Structured Semantic Planning for LLM-Based Queries over Enterprise Data](https://arxiv.org/abs/2608.13612)

**<font color=#1a73e8>作者：</font>** Bruno Santos Teixeira  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Natural-language interfaces to enterprise data must translate underspecified requests into governed, executable behavior while controlling invalid queries, policy failures, cost, and nondeterminism. SemPlan Benchmark evaluates this architectural design space with a deterministic synthetic bilingual benchmark containing 1,800 cases in English and Brazilian Portuguese; 1,200 cases form the frozen scientific evaluation subset. Four architectures are compared under the same model configuration: direct SQL generation (A1), a bounded tool-agent baseline (A2), structured semantic-request generation followed by deterministic planning and execution (A3), and a clarification/stateful semantic-plan variant (A4). Across 4,800 primary records, answer correctness was low in absolute terms: 22.25% for A1, 22.58% for A2, 25.67% for A3, and 24.25% for A4. A3 had the highest observed correctness and significantly exceeded A1, A2, and A4 in the pre-specified paired correctness analysis, while A1 retained the highest policy-correct rate and the lowest unsafe-or-invalid rate. A4 had the lowest mean API cost and lowest false-refusal rate. On a preselected 150-case stability subset, answer-correct repeatability ranged from 92.00% to 98.67%. The results support a trade-off interpretation rather than a universal ranking: additional structural constraints changed failure modes and efficiency, but did not monotonically improve correctness or solve ambiguity and multi-turn state consistency.

---


### 26. [How Compliant is Sepsis Treatment? An Expert-Guided Neuro-symbolic Pipeline for Generating Clinical Compliance Insights](https://arxiv.org/abs/2608.13617)

**<font color=#1a73e8>作者：</font>** Himanshu Tripathi, Kaushik Roy, Subash Neupane 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Verifying whether clinical care follows evidence-based protocols is a natural neuro-symbolic problem, yet the safety-critical setting defeats either paradigm alone. We present an expert-guided pipeline that constrains a large language model strictly to semantic normalization, mapping messy drug and microbiology strings onto a fixed clinical vocabulary, while a Sugeno fuzzy inference system reasons over the normalized events. The fuzzy layer encodes eight Surviving Sepsis Campaign bundle rules and replaces binary judgments with graded scores in [0,1]. Applied to 2,438 MIMIC-IV v3.1 sepsis episodes, it surfaces antibiotic timing as the most critical breakdown (mean 0.24, 13% within one hour), Hour-1 underperformance (mean 36.7%), a 51% elevated-lactate drop-off, and descriptive differences in ICU stay across compliance groups (3.8 versus 5.1 days).

---


### 27. [Measuring Fairness in Large Audio Language Models via Semantic-Aware Bias Estimation](https://arxiv.org/abs/2608.13624)

**<font color=#1a73e8>作者：</font>** Zhe Liu  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Audio Language Models (LALMs) have seen increasing use for audio understanding tasks such as speech recognition and audio question answering, raising concerns about fairness across demographic subgroups. Fairness evaluation in spoken-input settings is challenging due to confounding factors, including semantic variation in spoken content and speaker-specific characteristics. Ignoring these factors can result in misleading conclusions about model bias. We propose a semantic-aware mixed-effects regression framework for fairness evaluation in LALMs that explicitly accounts for these confounders. Our approach incorporates sentence-level semantic embeddings of reference text as covariates and models speaker identity as a random effect. Notably, semantic representations are extracted from the same LALM under evaluation, enabling semantic control over variation as perceived by the model itself. Experiments on simulated data and real-world benchmarks demonstrate that the proposed approach substantially reduces spurious fairness findings and yields more robust and interpretable estimates of subgroup performance differences.

---


### 28. [A Calibrated Test of Internal Action Maps: State Signals Without Global Affine Closure](https://arxiv.org/abs/2608.13626)

**<font color=#1a73e8>作者：</font>** Dekun Yang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A hidden state signal can be decodable or causally usable without supporting a reusable action map. We test whether action maps fitted without a source reach its natural post-action activation and compose. We organize the tests as an evidence lattice and validate the geometric branch on a known affine S_5 carrier: all held-source folds pass one-step, composition, inverse, decoding, and commutativity gates. Structured curvature and held-domain conjugacy raise error monotonically, but only 23/30 strongest cells flip a closure gate, bounding rather than universalizing calibration. In post-trained Qwen/Qwen3-4B, frozen final-token h28 affine maps have mean held-entity error .519, versus .398 for within-test-domain cross-fit. Seven randomized entity splits and map geometry do not support a purely entity-specific account. Earlier h4/h16 layers fit one-step transitions better, but h4 conflict-state decoding is weak and lexical controls remain unresolved. Three matched intervention datasets regenerated from one frozen checkpoint show causal effects only at h28/h36. Outcome-aware refitting improves h28 one-step error to .474 (.469 with weighting), yet no refit passes composition. Learned finite worlds likewise preserve relative algebraic signals or shared charts without held-source affine closure. Within the tested carriers, state availability, causal use, local geometry, and reusable closure are separable. The result is limited to one pretrained model, sampled final-token layers, two finite worlds, and the tested affine or diagnostic function classes.

---


### 29. [Ontology-Grounded Project Memory for Coding Agents](https://arxiv.org/abs/2608.13662)

**<font color=#1a73e8>作者：</font>** James Adam  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents have become the primary means of generating new code in many software projects, and the resulting velocity of changes makes keeping track of the reasons behind those changes challenging. This paper introduces MOOSEDev, a system designed to give coding agents structured, ontology-grounded project memory. The system captures architectural decisions, lessons, constraints, and rationales in a knowledge graph exposed to agents via a Model Context Protocol (MCP) interface. Records carry lifecycle status, provenance, and supersession links, queryable via MOOSE, a proprietary neurosymbolic engine that treats the symbolic layer as the primary reasoning substrate. We compared MOOSEDev against a production vector-memory tool on a neutral public corpus of 835 typed records. MOOSEDev returned the expected answer set essentially in full (0.98-1.00) on supersession, set-completeness, and negation questions, whereas the baseline's top-k retrieval surfaced between 6% and 27%. Conversely, relevance recall and token cost were largely equivalent between the two systems. We also describe a temporal commit-history bootstrap of our own codebase, a pre-registered live trial, and lessons learned.

---


### 30. [FabDreamer: Exploring the Image-to-Physical Workflow Through AI-Assisted Layered Fabrication](https://arxiv.org/abs/2608.13665)

**<font color=#1a73e8>作者：</font>** Chenfeng Gao, Zeya Chen, Anjie Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Generative AI lets anyone create rich visual content in seconds, yet translating that content into a physically fabricable artifact still demands manual decomposition, occlusion repair, and structural verification that most tools leave entirely to the user. We present FabDreamer, an image-to-physical system that carries an image to fabrication-ready SVGs through three stages with deliberately staged AI initiative: (1) AI leads decomposition into depth-ordered layers, (2) assists on demand during creative editing with realtime 3D preview, and (3) advises on structural integrity before export. We instantiate this workflow for layered laser-cut art and evaluate it through three rounds including a formative analysis, an early prototype user evaluation (N=13), and a cross-domain practitioner study with specialists from 6 fabrication domains (N=6). Our findings show that physical awareness during design opens creative opportunities beyond error prevention, that practitioners appropriate the system's generic geometric operations for their own domains, and that the fabrication agent covers geometry-readable constraints while domain knowledge remains with the maker.

---


### 31. [Second Thought: Reasoning in Parallel as LLM Agents Act and Observe](https://arxiv.org/abs/2608.13667)

**<font color=#1a73e8>作者：</font>** Zhensu Sun, Chengran Yang, Yunbo Lyu 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM agents in the ReAct paradigm alternate between reasoning, acting, and observing, but deliberate reasoning is confined to the Thought phase: while the agent serializes an action and waits for the environment, its reasoning is frozen. We identify this recurring interval for Action and Observation as a reasoning idle window and ask whether it can host additional reasoning in parallel that serves future turns. Therefore, we propose Second Thought, a training-free inference framework that forks four auxiliary branches the instant each Thought phase concludes, decodes them concurrently with the main loop, and merges the generated thoughts back when the environment observation arrives. In this way, Second Thought relocates the added reasoning off the main thread's sequential decoding path. Across three agentic benchmarks and three reasoning LLMs, Second Thought lowers the average turn count in all nine (model,benchmark) pairs and reduces main thread decoding in six of them by up to 43% (roughly 20% on average among those settings), while leaving it essentially unchanged in a seventh; Pass@1 shows no significant change in seven of nine pairs and the two significant differences are +12.4 and +10.2 points. Against a compute-matched control that forces an equivalent budget onto the main thread's own reasoning, it attains strictly higher Pass@1 with 1.3 to 3.2 less sequential decoding in all four settings where the control applies.

---


### 32. [The Query Knows What to Forget: A Second Erase Direction for Linear Attention](https://arxiv.org/abs/2608.13668)

**<font color=#1a73e8>作者：</font>** Dhruman Gupta, Aritra Das, Debayan Gupta  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention keeps a state of fixed size. At long context, many stored items share this state, and interference between them degrades retrieval. Gated DeltaNet-2 (GDN-2), like every delta-rule model before it, derives its erase vector from the key of the current token. However, the interference in its reads is measured through the query, and the erase step cannot reach it. We introduce the Query-derived Erase Direction (QED). QED adds a second erase direction derived from the query and orthogonal to the key. In the fast-weight view, a key-directed delta edit cannot change the key-orthogonal part of a read. It uses the editable part to cancel old-state content measured along the query. It also improves retrieval at every length past the training window, and it about doubles the usable context length on S-NIAH-1.

---


### 33. [From BERT to Frontier Agents: Eight Years of Language-Model Progress, the Collapse of the Capability-Cost Curve, and the Rise of Task-Targeted Models](https://arxiv.org/abs/2608.13675)

**<font color=#1a73e8>作者：</font>** Pranav Kumar Kaliaperumal  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Between October 2018 and July 2026 AI models progressed from simple systems like BERT to massive agents that solve complex math and write software. The ability to resolve real coding issues improved by nearly six times per year since late 2024. During this time costs dropped sharply with OpenAIs budget model GPT 5 point 6 Luna matching flagship capabilities for just one to six dollars per million tokens beating older versions at a fraction of the price. Top performance is now split across specialized models as Claude Opus 5 leads in frontend coding Claude Fable 5 excels at repository level coding and GPT 5 point 6 Sol dominates terminal tasks. In a grade school math test using the Qwen 2 point 5 model basic methods solved 58 of 100 problems while advanced sampling solved up to 79. A confidence ranking tool correctly identified 47 right answers in its top 50 choices proving highly useful for sorting tasks with all research materials made fully public.

---


### 34. [MedPlex: Deep Vision-Language Co-Adaptation for Clinically Grounded Medical Segmentation](https://arxiv.org/abs/2608.13690)

**<font color=#1a73e8>作者：</font>** Rafi Ibn Sultan, Hui Zhu, Chengyin Li 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical image segmentation is still largely treated as a vision-only problem, although clinical interpretation often relies on textual knowledge of anatomy, location, appearance, and surrounding context. Existing text-guided segmentation methods within the Vision-Language Model (VLM) paradigm often use language only as a late conditioning signal, limiting its influence on visual representation learning. We introduce MedPlex (Medical Plexus of Vision and Language), an end-to-end VLM framework that makes text guidance a continuous, clinically grounded component of segmentation learning. Through Bi-Fusion (Bidirectional Fusion), visual and textual representations evolve jointly across the encoding hierarchy. MedPlex further introduces class-level and region-level concept alignment to organize the shared representation at complementary granularities. Class-level alignment anchors each anatomical target to an aggregated clinical concept profile, while region-level alignment preserves individual concepts, such as shape, location, appearance, and texture, through class-specific visual evidence. In this way, language provides structured supervision throughout the encoder rather than serving only as a late-stage cue. MedPlex achieves state-of-the-art performance across CT and MR benchmarks for multi-organ, cardiac substructure, and tumor segmentation, including settings with real free-text clinical supervision. Code: this https URL.

---


### 35. [GRPO Beyond English: A Large-Scale Study of GRPO in Non-English and Multilingual Settings](https://arxiv.org/abs/2608.13698)

**<font color=#1a73e8>作者：</font>** Konstantin Dobler, Federico Scozzafava, Jonathan Janke 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Reinforcement Learning with Verifiable Rewards (RLVR), often optimized with Group Relative Policy Optimization (GRPO), has become a central recipe for improving the reasoning capabilities of pretrained language models but current studies remain heavily English-centric. We conduct a large-scale empirical study of multilingual and non-English GRPO across a wide range of base models, training languages, and different reasoning language rewards. We find that training to reason in the native language often leaves only a small gap to training for English reasoning. We further observe strong crosslingual transfer: training in one language often improves performance in many others. However, specific trends are highly model- and language-dependent. In some cases, training in a particular language induces severe regressions on out-of-domain capabilities in other languages. Our analysis shows that RLVR beyond English can provide broad crosslingual gains, but also requires broad evaluation to detect language-specific regressions.

---


### 36. [CLAIR-Fin: An Adversarial Multi-Agent Framework for Claim-Level Verification and Adaptive Debate in Cross-Modal Financial QA](https://arxiv.org/abs/2608.13706)

**<font color=#1a73e8>作者：</font>** Fatema Tuj Johora Faria, Mukaffi Bin Moin, Jubayer Al Mahmud 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Existing defenses against hallucination in retrieval-augmented and multi-agent pipelines remain partial: evidence is trusted despite modality disagreement, debate verifies an aggregate report rather than individual claims, and such verification occurs only after drafting, leaving inter-agent errors undetected until the final text. To close this gap, we present CLAIR-Fin, a nine-agent framework that decomposes each question into atomic claims maintained in a typed Financial Claim Ledger. Each claim is resolved through Asymmetric Evidence Authority, which conditions evidence trust on claim type rather than treating all modalities as equally reliable; Chain-of-Custody Verification, which checks grounding at the hand-off between drafting and adversarial review rather than only at the pipeline's exit; an Adaptive Rebuttal Cycle, which routes contested claims through adversarial debate whose depth scales with what that debate finds; and a terminal entailment audit paired with a continuous Hallucination Risk Index that distinguishes claims that passed scrutiny from claims never contested. We evaluate CLAIR-Fin on BB-FinQA-X, a 500-question cross-modal financial evaluation set built from Bangladesh Bank Annual Report material, stratified by query type, format, and difficulty. Relative to a single-pass retrieval-augmented generation baseline, it raises faithfulness ($0.780 \rightarrow 0.889$) while abstaining on 5.4% of questions when evidence is insufficient rather than forcing an unsupported response, and it exceeds stronger retrieval-strategy baselines such as HyDE and Graph-RAG on faithfulness ($\leq 0.874$).

---


### 37. [TeachMateGPT: A Multi-Agent Knowledge-Grounded Framework for Pedagogical Assessment Generation from Science Curriculum Materials](https://arxiv.org/abs/2608.13708)

**<font color=#1a73e8>作者：</font>** Fatema Tuj Johora Faria, Mukaffi Bin Moin, M. F. Mridha 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Automatically generating textbook-grounded assessment items can reduce science teachers' workload, but existing retrieval-augmented generation (RAG) systems rely on flat retrieval, support only single-question generation, lack safeguards against weak evidence, and are ill-suited to low-resource, board-exam-structured curricula. We address these limitations with TeachMateGPT, a multi-agent system contributing four advances to curriculum-grounded science-assessment authoring. (i) COPE, a hierarchical knowledge base replacing token-window chunking with a multi-resolution index that segments documents along syllabus structure and links them at three granularities via a traversable graph-based lineage, matching evidence to each topic's instructional level. (ii) A staged, fail-closed agent pipeline replacing one-shot retrieve-then-generate: routing gates search, retrieval fuses dense and lexical evidence under a coverage gate that withholds generation on insufficient evidence, and specialist agents draft objective and constructed-response items. (iii) SAVER, a source-attributed verification protocol scoring faithfulness, relevance, and hallucination risk against retrieved evidence, applying stricter grounding checks across each creative question's four sub-parts, paired with teacher-in-the-loop evaluation rather than automatic filtering. (iv) NCTB-SciGen8, a curriculum-grounded dataset of 198 items (143 multiple-choice, 55 creative questions) spanning all 14 chapters of the NCTB Class 8 science textbook, produced by the pipeline and rated by three practicing teachers. TeachMateGPT raises faithfulness (0.68 $\rightarrow$ 0.96) and answer relevancy (0.60 $\rightarrow$ 0.89) over a vanilla RAG baseline.

---


### 38. [BM25-Augmented Many-Shot Translation for Low-Resource North-Eastern Indian Languages](https://arxiv.org/abs/2608.13722)

**<font color=#1a73e8>作者：</font>** Aashish Dhawan, Christopher Driggers-Ellis, Dzmitry Kasinets 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> This paper describes the University of Florida Gators submission to the WMT26 Low-Resource Indic Language Translation shared task. We adapt the retrieval-augmented many-shot translation pipeline from our AmericasNLP 2026 system to translate between English and eleven North-Eastern Indian languages in both directions. At inference time, BM25 retrieves the most similar parallel examples from a language-specific training bank, and Gemini 2.5 Flash translates the input conditioned on these examples. No model fine-tuning is involved. Training banks combine official WMT26 data with publicly available corpora such as Samanantar and prior WMT shared task releases. A grid search over retrieval count r and development exemplar count d across all 22 language-direction pairs selects the best configuration for each submission.

---


### 39. [Explanation Multiplicity: Circuit-Level Interpretability Evidence Does Not Survive Defensible Analytic Variation](https://arxiv.org/abs/2608.13754)

**<font color=#1a73e8>作者：</font>** Ajay Pravin Mahale  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The EU AI Act requires providers of high-risk systems to file technical documentation describing how the system reaches its decisions. Mechanistic interpretability is the obvious source of such evidence, and circuit discovery is its most developed instrument. We ask whether that evidence survives the condition under which it would be relied upon: two competent analysts, the same system, the same tool, different defensible settings.
We pre-registered a crossed grid of seven analytic axes, every level taken from a published implementation, and mapped each discovered circuit through a deterministic claim map to a structured Annex IV statement. Across 15,840 pre-registered specifications on GPT-2 small and the indirect object identification task, of which 7,561 produced a claim, the derived statement flips across 73.2% of specification pairs (95% CI 0.725 to 0.738) and the modal claim commands 41.1% of the space. The evidence fails a filability criterion at every tolerance a conformity assessment body would plausibly accept.
Standardising the single most influential choice, the evaluation metric, leaves the flip rate at 59.4%. Removing circuit size from the claim entirely and holding it fixed leaves 27.1% (95% CI 0.255 to 0.286), still above the pre-registered threshold. The circuits underlying these claims are structurally near-disjoint, median pairwise Jaccard overlap 4%, and functionally uncorrelated at Cohen's kappa 0.015, so the instability is not one mechanism described in different words.
We give the filability criterion as a standalone protocol, and we report that one of the seven documented discovery objectives does not execute at all on the library's own canonical task. The study covers one model and one task, and whether the conclusion holds at scale is untested.

---


### 40. [The Integer Alibi: Localizing Cross-Kernel Divergence in INT8-Quantized LLM Inference](https://arxiv.org/abs/2608.13756)

**<font color=#1a73e8>作者：</font>** Teng-Ruei Chen  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Two GPU kernels implementing the same scaled INT8 GEMM interface are usually treated as interchangeable. We test that assumption: holding the checkpoint, prompts, hardware, inference engine, decoding, and quantization configuration fixed, we swap only the INT8 linear kernel (CUTLASS versus Triton) inside vLLM. At 1.7B each arm reproduces itself bit-for-bit across cold restarts, yet the arms agree on no sequence in any end-to-end comparison we ran (0/8, 0/16, and 0/64). What makes this more than a benchmark discrepancy is an integer alibi: for shared INT8 operands under a verified no-overflow bound, the INT32 dot product is exact and order-independent, so the accumulator cannot be the source of any difference. Feeding both kernels identical operands from every linear layer of Qwen3-1.7B and 8B (196 and 252 layers), we find bit-identical outputs under power-of-two scales, confirming a pinned prediction list 196/196 and 252/252 (pre-registered at 1.7B, pinned but not blind at 8B), and observed differences of at most one bfloat16 spacing under the checkpoints' real scales. This localizes the divergence to scale application and output rounding after the exact accumulator. Applied as a probe checkpoint, the same intervention restores end-to-end bitwise agreement (8/8 and 16/16 sequences). Cross-implementation FP8 GEMM shows a different signature: both the prevalence and the magnitude of differences grow with reduction depth, while the INT8 fraction stays at parts per million and within one spacing over a 64x range of K. Teacher-forced replay ties layers to tokens: flips concentrate at small logit margins, which predict flip risk with ROC-AUC 0.94 on 16,384 positions. We will release the pre-registration, per-layer predictions, manifests with kernel-selection evidence, and a conformance procedure that turns these controls into a concrete check for kernel interchangeability.

---


### 41. [Amplified Does Not Mean Predictive: Reasoning Behaviors in Thinking Models](https://arxiv.org/abs/2608.13760)

**<font color=#1a73e8>作者：</font>** Jean de Dieu Nyandwi, Leena Mathur, Yonatan Bisk 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Which reasoning behaviors are associated with correct answers in reasoning models, and does reasoning-oriented training amplify those behaviors? This distinction is important because reasoning-oriented training can make traces look more deliberative without amplifying the behaviors most tied to model correctness. We quantify this mismatch with Behavioral Lift, a metric that measures how much correctness changes when a behavior is present versus absent in a model's reasoning trace. Across 15 models and 6 benchmarks spanning text-only and vision-language reasoning, we annotate 15,282 traces with a taxonomy whose core behaviors are defined for both LLM and VLM traces. We find evidence for an Amplification-Lift Gap, in which thinking models strongly amplify self-correction, hypothesis testing, and uncertainty acknowledgment, while the highest-lift behaviors are confidence calibration, knowledge alignment, and self-awareness. Confidence calibration is among the strongest positive signals of correctness in both modalities, yet is barely amplified; uncertainty acknowledgment is amplified by 3--7$\times$, yet is weakly or negatively associated with correctness. We find that reasoning-oriented training does not preferentially amplify the highest-Lift behaviors, motivating process-level objectives that reward calibrated and grounded reasoning rather than surface form alone.

---


### 42. [ChartProbe: A Diagnostic Study on Visual Reasoning through Perception, Grounding, and Simple Reasoning](https://arxiv.org/abs/2608.13766)

**<font color=#1a73e8>作者：</font>** Mahsa Khoshnoodi, Sarah Adel Bargal  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) remain unreliable on chart questions that require reasoning over visual quantities, and this weakness is usually attributed to a reasoning deficit and addressed with more reasoning supervision. We ask whether the difficulty lies in reasoning itself, or in the simpler skills that reasoning operates on: reading the plotted elements (\emph{perception}), locating them and binding them to their labels (\emph{grounding}), and performing single-step computations such as ranking, totals, and differences (\emph{simple reasoning}). We introduce \textbf{ChartProbe}, a diagnostic framework whose probes are generated directly from the code that renders each chart, so every gold answer is exact by construction, needs no human annotation, and attributes each failure to a single skill. ChartProbe enables an intervention prior work does not attempt: instead of synthesizing complex-reasoning data, we withhold complex questions and reasoning traces entirely, fine-tune on one simple skill at a time, and measure transfer to held-out complex-reasoning questions. Across three open-weight VLMs, supervising the simpler skills alone produces large gains on complex-reasoning questions the model never trained on: where these skills are weak and the model can be taught to read the image, training them recovers much of complex reasoning at no reasoning-data cost. The gains hold across three out-of-distribution settings: an unseen chart type (pie charts), a human-written benchmark disjoint from our images and templates (ChartQA), and a non-chart visual domain (CLEVR). Complex visual reasoning can therefore improve without complex-reasoning supervision.

---


### 43. [Simulation-Aware In-Context Policy Improvement for LLM-Aided Analog Layout Refinement](https://arxiv.org/abs/2608.13767)

**<font color=#1a73e8>作者：</font>** Bingyang Liu, Ziming Wei, Xiaohan Gao 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Analog IC layout design remains a labor-intensive iterative process dominated by simulation-driven refinement. Although end-to-end layout generators accelerate initial placement and routing, they still require experts to manually tune layout optimization parameters with repeated post-layout simulations for stringent design specifications. While Bayesian Optimization (BO) is widely adopted for parameter tuning in analog IC design, at the layout level it typically requires hundreds to thousands of evaluations, each involving costly parasitic extraction and post-layout simulation, which makes it impractical. Recently, Large Language Models (LLMs) have demonstrated potential in improving the sample efficiency of such simulation-driven tuning. However, their restricted access to geometric layout context and design-specific heuristics limits their ability to manipulate the layout optimization process. In this paper, we propose a simulation-aware LLM multi-agent framework that performs in-context policy improvement (ICPI) by iteratively updating layout optimization parameters exposed by an analog layout generator through an act-observe-reflect loop on compact structured layout representations. Experiments on real-world analog circuits show that, with only tens of post-layout simulations, our approach improves post-layout performance over the generator's built-in heuristics and BO-based tuning method.

---


### 44. [Doomed to Re-Annotate, Forever: The ImageNet Story](https://arxiv.org/abs/2608.13783)

**<font color=#1a73e8>作者：</font>** Illia Volkov, Nikita Kisel, Tetiana Mishkina 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Top-1 accuracy on ImageNet-1k remains the most commonly reported metric in visual recognition. Quality issues with the dataset have been repeatedly reported, yet the original 2012 noisy labels are still predominantly used. The paper presents a comprehensive effort, which goes well beyond prior correction attempts, towards obtaining accurate and complete ImageNet-1k validation set annotations. The result, ReImageNet, includes multilabel correction, object localization, revised class definitions, and semantic attributes (text-recognition, rendition, reflection, crowd, dominant). The reannotation reveals that approximately 12% of the original ImageNet-1k labels are incorrect, 33.3% of images are multilabel and 3.8% contain no object from an ImageNet-1k class. With the new labels, top-1 accuracy increases by up to 1.2% for supervised models and by 5-6% for MLLMs. We argue that annotation at ImageNet scale cannot realistically be completed in one pass, as errors and definitional issues are discovered only through annotating, and we build our pipeline around repeated refinement and error checking. We observed that human and LLM collaboration with appropriate tooling represents the current quality ceiling for annotation at this scale. ImageNet-1k issues propagate into its derivative test sets, indicating that the problem is structural rather than specific to any single benchmark. All annotations, class definitions, guidelines, and analysis code have been publicly released. Project page: this https URL Annotations: this https URL Code: this https URL

---


### 45. [From Passive Delegates to Strategic Negotiators: Reinforcing Social Reasoning in Small Language Models with SocialRL](https://arxiv.org/abs/2608.13787)

**<font color=#1a73e8>作者：</font>** Wenyue Hua, Zachary Huang, Tyler Payne 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents increasingly act on their users' behalf, handling tasks such as scheduling meetings, comparing offers, and haggling over prices. These principal-driven tasks routinely place the agent across from a counterpart (another user's agent, a seller, a recruiter) whose goals may conflict with its principal's. Yet the dispositions that make an assistant pleasant can make it a poor delegate: a friendly, helpful frontier model may disclose its principal's private information unprompted and concede at the first sign of resistance. We present SocialRL, a general recipe that trains social reasoning directly, and apply it to a 4B model across six domains: Deal-or-No-Deal, CaSiNo, Craigslist, Job Interview, Calendar, and Marketplace. Every domain is trained in-domain under the same recipe, and every policy is evaluated on all six. We find that (1) in-domain training reaches the frontier: on held-out scenarios the 4B matches or exceeds the GPT-5 family per domain, closing 73-122% of the baseline-to-frontier gap on the negotiation games, with 78% of buyer openings anchoring below target versus 3% untrained; (2) cross-domain transfer follows game structure: structurally paired games lift each other, a broad multi-issue donor lifts nearly all domains, and structurally isolated games transfer nothing; (3) guided by this transfer structure, two strategies, cascade RL and multi-teacher on-policy distillation (OPD), consolidate the per-domain specialists into a single unified 4B that reaches 0.627 average utility across all six environments, matching or exceeding GPT-4.1 (0.625), GPT-5.1 (0.619), and GPT-5.2 (0.613); (4) an explicit theory-of-mind scaffold helps only through training: distilling the ToM trace, rather than actions alone, lifts utility on every environment and generalizes better across them, and of the two ToM skills, only next-action prediction predicts negotiation outcomes.

---


### 46. [When Lexical Change Misleads: Rethinking Dynamic Topic Model Evaluation with Traditional and LLM-Based Metrics](https://arxiv.org/abs/2608.13835)

**<font color=#1a73e8>作者：</font>** Charu Karakkaparambil James  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Dynamic topic models capture evolving word distributions, but traditional coherence metrics may fail when vocabulary changes while semantic meaning persists. We evaluate 120 topics from CoNTM and DLDA across NYT, DBLP, and arXiv, using three human annotators and Low, Medium, and High lexical-change categories. Traditional temporal coherence shows highly variable agreement with human judgments ($\rho$=-0.256 to 0.614). In contrast, LLM-based semantic similarity agrees strongly with human semantic judgments for CoNTM on NYT ($\rho$=0.609), DBLP ($\rho$=0.721), and arXiv ($\rho$=0.502), but is less consistent for DLDA. Lexical-change stratification reveals variation hidden by aggregate evaluation. We therefore advocate lexical-change-aware evaluation, jointly reporting traditional coherence and LLM-based semantic measures as complementary rather than interchangeable signals.

---


### 47. [ASSERT: A Measurement Pipeline for GenAI Audits](https://arxiv.org/abs/2608.13840)

**<font color=#1a73e8>作者：</font>** Riccardo Fogliato, Abhinav Palia, Xiawei Wang 等 14 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Audits of generative AI (GenAI) systems often summarize behavior as a reported rate: how often the audited system complies with policy. Researchers and stakeholders use that rate to compare systems, track regressions, and gate deployment. A reported rate reflects both the system under audit and the measurement choices behind it, so a change in the rate can leave it unclear whether the system or those choices moved. We introduce ASSERT, a specification-driven measurement pipeline for GenAI audits that ties each reported rate to a written specification of the measurement choices used to produce it. ASSERT helps draft a behavioral rubric and test cases, then runs the audit against a GenAI system and returns a reported rate. In a case study on conversational deception, we observe that the reported rate moves substantially with the dialogue setup, the simulated user, the judge, and the evidence bar for non-compliance. These measurement choices substantially change the reported rate and can reorder GenAI system rankings. Because each reported rate is tied to an explicit specification, differences across audits are easier to attribute and interpret.

---


### 48. [Federated Prompt Learning: A Unified Framework, Empirical Analysis, and Future Directions](https://arxiv.org/abs/2608.13844)

**<font color=#1a73e8>作者：</font>** Qinglin Yang, Chen Qiu, Hongyuan Zhang 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have become core components of cloud-based intelligent services in academia and industry, yet their training and deployment are hindered by high computational costs, data centralization, and privacy concerns. Federated learning (FL) offers a decentralized training paradigm that enables clients to collaboratively train a learning model without sharing raw data, making it a promising solution for privacy-preserving LLM training and reasoning. This paper presents a comprehensive survey of federated prompt learning (FPL) to review recent advances in integrating the federated learning paradigm and large language models, answering the following research questions: RQ1: The fundamental motivations, characteristics, and enabling technologies of FPL, and how it differs from conventional FL and full-model federated fine-tuning; RQ2: The trade-offs FPL approaches exhibit in performance, communication efficiency, computational overhead, scalability, personalization, and heterogeneity handling; RQ3: The remaining security, privacy, robustness, and system challenges, along with key future research directions. To this end, we systematically examine existing FPL methods across the full model lifecycle: pre-training, fine-tuning, and practical applications, while discussing security, privacy, and robustness issues and summarizing existing defense mechanisms. Finally, we highlight open challenges and future directions, aiming to help readers understand how the insights drive research in FPL.

---


### 49. [Bootstrapping Niche Multilingual Code Translation via Reinforcement Learning with Execution-Based Verifiable Supervision](https://arxiv.org/abs/2608.13854)

**<font color=#1a73e8>作者：</font>** Kouki Yuki, Jie Zeng, Kyoko Ogawa 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Code translation must preserve executable behavior across many programming languages, yet neural code translation has largely focused on a few popular languages such as C++, Java, and Python. This leaves a niche, many-to-many setting where parallel supervision is sparse, producing plausible but non-executable translations. We address this setting with preference-based reinforcement learning driven by execution-based supervision. Our pipeline firstly expands verifiable seed Python programs into a multilingual pool of execution-validated codes. Using the pool, a base LLM generates translation candidates across language pairs, which we label by their execution outcomes. The resulting preferences are used to train a reward model that scores cross-language translation quality. Finally, we optimize our base LLMs with GRPO over 600 directed language pairs (25 x 24) using the reward model as a signal. To evaluate the niche translation capability, we introduce HumanEval-X++, an execution-based benchmark that extends HumanEval-X to a broad many-to-many language space. We evaluate our approach using Qwen-3.5 4B and 9B models. On HumanEval-X++ and existing benchmarks, it yields consistent gains over the untrained baselines. In particular, the 4B model achieves an average improvement of 13% across all languages on HumanEval-X++, with a gain of 21% on mid-tier languages. Our study establishes a reliable approach of data generation, training, and benchmarking, paving the way toward further bootstrapping the quality of many-to-many translation for programming languages.

---


### 50. [Geometric Filtering of LLM-Generated Samples for Few-Shot Text Classification](https://arxiv.org/abs/2608.13866)

**<font color=#1a73e8>作者：</font>** Benjamín Schindler, Gonzalo A. Ruz  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) can generate synthetic training data for text classification, but the quality of generated samples is heterogeneous: some fall in correct class regions of the embedding space while others land in peripheral or cross-class zones. We propose a geometric filtering framework that evaluates each LLM-generated sample by its Euclidean distance to real class examples in a sentence embedding space, selecting only geometrically consistent candidates. A soft weighting mechanism transforms filter scores into sample weights for classifier training. Evaluated across 13 datasets, 5 classifiers, 10 augmentation methods, and over 6,700 configurations, our method achieves +2.61 percentage points (pp) over SMOTE ($p<0.0001$, Cohen's $d=0.95$, 88.9% win rate). The approach generalizes to named entity recognition (+9.26pp, 100% win rate) without filter modification, and is robust across 5 LLMs from 4 providers. A key finding is that the simplest distance-based filter consistently outperforms complex multi-criteria alternatives.

---


> [!TIP]
> 当前位于：**1-50**（第 1/3 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：**1-50** | [51-100](./part-02.md) | [101-144](./part-03.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
