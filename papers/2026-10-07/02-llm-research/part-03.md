# 🧠 大模型相关研究 | 2026年10月07日

> 本类共 **505** 篇论文：已确认 **467** 篇，待复核 **38** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

---

### 101. [Do Tool Calls Execute as Intended? Measuring and Repairing Intent-Execution Correspondence in LLM Agents](https://arxiv.org/abs/2610.04375)

**<font color=#1a73e8>作者：</font>** Boyang Yang, Zhenhao Li, Ziyao Yang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Agents built on large language models (LLMs) build and run software through tool calls. A call reaches its program through several hops, and any hop can change the call without notice. When the changed call fails, the agent retries a correct call, which costs users time and money. Benchmarks and failure analyses do not see the change, because they read the call and its result but not what a hop received. We define intent-execution correspondence (IEC) as the property that the executed action matches the action the emitted call denotes under the tool contract. Our protocol observes what each hop received without executing the call, and names the first hop that changed it by the receiver's own parser. IntAct then delivers the call in a form that this hop cannot alter, or refuses the call. We build IEC-Bench from the changes observed in real-world use, with chains of dependent calls under the execution paths of 4 widely-used harnesses.
In 47,828 shell calls within production sessions, Claude Code's Bash tool changes 12.0% of the calls that carry code, escape sequences, or long text. For 80.7% of the calls whose backslashes are changed, the wrong action runs without any reported error. All 10 measured harnesses change a call. Trajectory-based judgment attributes 95.1% of the production failures to the LLM, although the path caused more than half of them. On IEC-Bench, the path raises the token cost per passed task 2.4 times (up to 12.3 times). A hop that changes a call also hides the changes after it, so 55.1% of the failures on one path appear only after its first hop is repaired. IntAct, deployed in a commercial product, recovers 79.2% of the failures with a changed call. Harnesses should therefore be designed and tested hop-by-hop to ensure a correct call executes as intended or is refused.

---


### 102. [COPEX: Benchmarking LLM Robustness to Adversarial Context Across Model Context Protocol Layers](https://arxiv.org/abs/2610.04378)

**<font color=#1a73e8>作者：</font>** Nahom Birhan, Mehrdad Rostamzadeh, Sidhant Narula 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models increasingly mediate tool use in Model Context Protocol (MCP) systems, where adversarial influence may enter through user instructions, tool schemas, tool outputs, or protocol messages. Existing benchmarks often evaluate deployed agents, conflating model susceptibility with guardrails, orchestration, and general task capability. We introduce COPEX (COntext Provider EXploitation), a controlled benchmark that isolates the model as an MCP client by fixing the surrounding agent stack and varying only the tool-selecting model. COPEX covers 25 attack types instantiated as 125 scenarios across four entry surfaces: model/agent, client, server/tool, and transport. Across nine models and 3,375 trials, the mean attack success rate is 64.4%, with surface-level means ranging from 58.3% to 71.4%. Some client- and transport-level attacks succeed partly outside the model's observation or control, separating system exposure from model susceptibility. Combined input and context scanning reduces mean attack success by 49.6% on an eight-attack defense subset relative to the undefended setting. The benchmark is available at this https URL.

---


### 103. [AgentPersonaBench: Benchmarking Persona-Driven User Simulation](https://arxiv.org/abs/2610.04379)

**<font color=#1a73e8>作者：</font>** Jintao Huang, Yifan Wang, Hongyu Shen 等 46 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We introduce AgentPersonaBench (APB), a benchmark evaluating whether persona conditioning faithfully steers downstream agent behavior. While language models are increasingly deployed for persona-driven user simulation, existing benchmarks primarily evaluate conversational styling or self-reports rather than authentic behavioral fidelity. APB evaluates latent persona adherence one trait at a time, embedding each target trait within a complete synthetic profile without explicitly naming the trait or disclosing the test. Ground-truth adherence is verified strictly from observable actions across four interaction surfaces of increasing realism: survey, chat, web (interactive web environments), and app (desktop software environments). APB comprises 2,460 tasks spanning 867 traits, verified through automated audits and expert review. Our evaluation of 20 frontier model arms demonstrates that high-fidelity user simulation is already attainable: leading models achieve up to 84.7% full-pass adherence under unprompted conditions. At the same time, APB identifies clear behavioral boundaries: adherence drops across interaction modalities (only 37.9-64.3% pass all four surfaces), multi-attribute demands degrade retention, and competing model families exhibit pronounced behavioral divergence.

---


### 104. [Beyond Plausibility: Verifiable Fine-Grained Image Editing on Structured Assets](https://arxiv.org/abs/2610.04381)

**<font color=#1a73e8>作者：</font>** Muyao Wang, Chen Zhu, Shiqi Yang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Fine-grained image editing requires more than producing a visually plausible result: an editor must execute the requested attribute change precisely while leaving everything else intact. However, existing benchmarks leave a critical gap between realism and verifiability: benchmarks built on realistic images typically rely on human or vision--language model judgments, while deterministic evaluation has largely focused on synthetic shape canvases, with application-oriented extensions primarily limited to charts. This makes it difficult to determine precisely how much of a requested edit was executed, where unintended changes occurred, and whether small differences between models reflect genuine editing capability or evaluator uncertainty. To bridge this gap, we present VeriEdit-Bench, a benchmark for fine-grained, instruction-faithful image editing across realistic structured assets with deterministic, four-axis evaluation. Its 1,740 cases are compiled from the source code of 153 Scalable Vector Graphics (SVG) graphics, charts, web interfaces, and presentation slides. Controlled source-code edits preserve the original visual context while yielding exact target images, pixel-level edit masks, and explicit edit specifications, enabling reproducible scoring along four axes: edit fidelity, preservation, localization, and magnitude. Evaluating eleven editors, we find that even the strongest model remains far from full credit; rankings for the same recoloring operation reverse between charts and SVG graphics; and outputs with similar pixel-accuracy profiles can still differ substantially in localization and change magnitude. This decomposition yields graded, verifiable feedback and exposes model-specific capability and failure profiles that holistic scores or evaluator-dependent judgments may obscure.

---


### 105. [TrustMed-RL: Long-Horizon Reinforcement Learning for Evidence-Grounded Clinical Diagnosis](https://arxiv.org/abs/2610.04387)

**<font color=#1a73e8>作者：</font>** Wenxin Zhan, Yizheng Jiao, Haifeng Song 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Medical language models can produce correct diagnoses despite incomplete investigations and unsupported reasoning. To support long-horizon, evidence-grounded diagnosis, we introduce \textbf{TrustMed-RL}. Built from PubMed rare-disease cases and over 24,000 manually annotated image panels, it integrates interviews, examinations, testing, specialist consultation, and literature search through state-dependent actions. Our 8B vision--language policy, trained with clinically adapted GiGPO and coverage-adjusted diagnostic rewards, achieves 37.1\% diagnostic accuracy on 2,500 evaluation cases, outperforming all evaluated open-weight baselines and improving over supervised fine-tuning by 12.4 percentage points.. When success additionally requires acquiring at least 50\% of supporting test evidence, TrustMed-RL achieves 32.5\%, exceeding GPT-4o by 6.8 percentage points. Furthermore, it surpasses all evaluated baselines on MTMedDialog and multiple larger 27--32B models on AgentClinic. In physician review of 200 diagnostically accepted test-set trajectories, 83.0\% receive evidential-grounding scores of 4--5 out of 5. Physicians' assessments suggest that these diagnostic trajectories are trustworthy and aligned with human diagnostic reasoning.

---


### 106. [Detecting Defects that Matter: An Application-Driven Benchmark for Anomaly Detection in Manufacturing and Retail Logistics (VAND 4.0 Challenge)](https://arxiv.org/abs/2610.04392)

**<font color=#1a73e8>作者：</font>** Lars Heckler-Kram, Dorian Henning, Ashwin Vaidya 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Existing Anomaly Detection benchmarks are saturated and often unrealistic. As part of the VAND 4.0 Challenge, we introduce a hidden-test, application-driven benchmark across two deployment-critical domains: industrial manufacturing and retail logistics. In the Industrial Track (MVTec AD 2), the results reveal that unsupervised anomaly segmentation remains challenging: the best regular-setting method achieves only ~57\% pixel-level $SegF_1$, indicating substantial room for improvement. Zero-shot approaches trail by ~15 $SegF_1$ points, confirming that task-specific training on normal data remains essential for precise defect localization. Robustness to distribution shifts remains a key open challenge and DINOv3-backbones clearly dominate this track. In the Retail Track (Kaputt 2), the results reveal that (1) supervised defect detection is approaching saturation for common defect types; (2) the best off-the-shelf VLM approach trails specialized models by ~28 AP, confirming that currently VLMs cannot replace fine-tuned detectors, (3) reference images did not prove helpful for top-performing approaches. Performance collapses on rare defects (spillage ~53 AP, missing units ~27 AP), where the supervised ceiling is bounded by data availability. To drive future progress in this domain, we provide a new low-prevalence retail AD dataset (Kaputt-Rare). Across both tracks, computational efficiency is assessed as a first-class metric combining performance, throughput, memory, and power consumption. We introduce a novel metric for measuring efficiency and reveal that that top-performing methods rely on heavy architectures while efficiency is largely neglected. Overall, we conclude that the community needs (a) more efficiency-aware method development, and (b) true anomaly detection approaches for rare defects and shifting conditions. this https URL

---


### 107. [GlitchPatch: Repairing Glitch Tokens in Frozen Language Models via Local Retokenization](https://arxiv.org/abs/2610.04399)

**<font color=#1a73e8>作者：</font>** Kunsheng Tang, Peigui Qi, Yide Song 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Glitch tokens are anomalous vocabulary entries that can cause large language models (LLMs) to produce outputs inconsistent with their inputs. Existing repair methods require access to model internals, making them impractical for frozen checkpoints. We investigate whether glitch tokens can be repaired outside the model by optimizing the input tokenization. An empirical study on BPE merge-rule deletion reveals that (1)deleting a glitch token's merge rule can fix a substantial fraction of failures, yet disrupting normal tokens sharing intermediate merge nodes causes the overall glitch rate to rise, and (2)different decomposition granularities yield non-monotonic fix rates while collateral damage on normal tokens grows monotonically. Motivated by these findings, we propose GlitchPatch, a repair framework for frozen language models based on local retokenization, consisting of two stages: the offline stage uses Behavioral Path Optimization (BPO) to find the behaviorally optimal replacement token sequence for each glitch token and compiles validated replacements into a rule table; the online stage substitutes only the IDs of matched glitch tokens in the canonical token sequence, with no modification to model parameters or internal states. Experiments on ten models spanning six tokenizer families show that GlitchPatch achieves an 85.10% mean fix rate, outperforming the strongest baseline by 14.37 percentage points, and reduces the average glitch rate from 14.88% to 2.27%. GlitchPatch achieves a 0.00% RR in full-vocabulary evaluation and leaves rule-unmatched inputs unchanged by design. We further evaluate the practical impact of repair from the perspectives of time cost, language understanding, and capability, supporting its deployment feasibility. We hope this work provides a practical option for improving tokenizer reliability.

---


### 108. [Ideological Stance Detection in a Low-Resource Language: Polarization in Bangladeshi Public vs Private University Discourse on Social Media](https://arxiv.org/abs/2610.04401)

**<font color=#1a73e8>作者：</font>** Safaruzzaman Shovo, Monowar Islam, Asif Hossain 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Public vs. private universities is a debatable issue, and it creates polarization on social media in Bangladesh. Debate on quality, jobs, and prestige is passionate among the students, parents, and graduates, the majority of whom speak Bengali, a low-resource language. To measure this polarization, this paper introduces a manually annotated dataset of 4,060 Bengali comments labeled as Pro-Public, Pro-Private, or Neutral. We evaluated the quality of our annotations by Fleiss's Kappa agreement that was 0.89, corresponding to a high agreement among annotators. The classical ML (SVM, Random Forest, XGBoost), BiLSTM network, hybrid BanglaBERT+XGBoost models and the state-of-the-art zero-shot LLMs (Claude Sonnet 4, DeepSeek-V3.1, Llama 4 Maverick, Kimi K2 Thinking, Qwen3-235B Thinking) models are evaluated. The accuracy of BanglaBERT+XGBoost is 91.81% and macro F1 score is 91.70%, which is higher than all the supervised baselines. The zero-shot Llama 4 Maverick Thinking achieves a macro F1 of 0.931 (overall accuracy of 93.31%) without any fine-tuning. All machine learning (ML), deep machine learning (DL) and transformer models were outperformed by the zero-shot Llama 4 Maverick model. Polarization also is evident, in some ways more clearly in the Pro-Private comments, which emphasize modern facilities and timely graduation, versus the Pro-Public comments, which emphasize affordability and government jobs. Our findings open new directions for analyzing social media polarization in low-resource languages.

---


### 109. [Saying, Not Knowing: Aggressively GGUF-Quantized Small Language Models Still Write Rare Words They Can No Longer Define](https://arxiv.org/abs/2610.04403)

**<font color=#1a73e8>作者：</font>** Saurabh Kumar Singh, Yogeshwar Singh Dadwhal, Malhar Vedak  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Post-training quantization to the GGUF format's mixed-precision K-quants is commonly how open-weight language models reach consumer hardware, yet its effect on fine-grained lexical competence is uncharacterized. We audit 27 quantized artifacts across 13 families and four architecture backbones, 0.35B-14B parameters, evaluated down their published ladder to Q2_K (about 2.6 bits per weight), on 429 frequency-validated rare English words under two probes: surface inclusion of a prompt-supplied word and its one-sentence definition, scored by a tiered multi-synonym matcher, its error measured by a blind LLM-judge census of every definition, with human verification. Three regimes emerge at Q2: total collapse into unusable builds, severe semantic dissociation in sub-2B models, and mostly robust preservation above about 3B. In every sub-2B artifact, definitions fall 20-67% below the artifact's baseline, typically several times the inclusion loss. Two controls separate rarity from task difficulty: within the rare set, loss rises with rarity in six of seven sub-2B artifacts, and on a 100-word common-word set rare words lose more than common words in all eight, significantly in six. Tokenizer vocabulary size does not predict the damage (Spearman rho=0.12); parameter count dominates (rho=0.72), confirmed within five of six same-tokenizer families. Q4_K_M remains lexically clean at >=1B. The damage is frequency-graded, provider-dependent, and not calibrated by WikiText-2 perplexity: across nine artifact-matched ladders, near-identical Q2 penalties (44.7%/47.6%) separate an artifact keeping its definitions (3.6%) from one losing them (43.6%). Aggressively quantized small models can keep generating fluent text while no longer knowing what it means, risking hardware-constrained deployments in domains where semantics carries consequences. Validation must be per artifact.

---


### 110. [Understanding and Mitigating Hallucination Escape in Tool-Using LLM Agents](https://arxiv.org/abs/2610.04409)

**<font color=#1a73e8>作者：</font>** Peigui Qi, Kunsheng Tang, Yide Song 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly serve as autonomous agents that invoke external tools. However, this capability introduces tool hallucination, selecting incorrect tools or generating invalid calls. Existing mitigation methods report substantial improvements, yet we identify a previously overlooked failure mode that we term Hallucination Escape. These methods reduce hallucination on the tool configuration they are tuned on but increase it on other configurations, canceling out the gain. We further investigate this phenomenon and find that hallucination rises sharply when a model's intrinsic tool-use tendencies conflict with the current tool configuration, and that existing methods reinforce rather than suppress these tendencies, which in turn contributes to hallucination escape. Building on these findings, we propose EscapeGuard, a training-free inference-time method that combines conflict-aware gating with configuration-derived attention enhancement to mitigate tool hallucination while preventing hallucination escape. Across six benchmarks on various models, EscapeGuard reduces tool-selection hallucination by 9.0 pp and suppresses hallucination escape, lowering the cross-configuration mean by 23.7 pp and achieving an 89.1% net improvement in paired-query evaluation. We hope this work can encourage evaluation beyond a single tool configuration and pave the way for more reliable tool-using LLM agents.

---


### 111. [AgroGround: Multi-Granularity Grounded Recognition in Agriculture](https://arxiv.org/abs/2610.04425)

**<font color=#1a73e8>作者：</font>** Abdulla Alshehhi, Zongyan Han, Rao Anwer  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Agricultural visual models are typically evaluated for either recognition or localization, but reliable diagnosis requires identifying what is present and localizing the evidence. Agricultural visual question answering (VQA) datasets carry rich semantic labels but rarely link them to image regions, and adding such annotations by hand is costly at scale. We introduce AgroGround, a large-scale dataset for grounded agricultural recognition: identifying plant diseases and other agricultural targets and localizing their image regions. An automated pipeline converts the labels of eight agricultural VQA datasets into annotations for disease lesions and whole objects, producing 794,850 instruction examples. Healthy images provide negative supervision for disease queries, teaching the model to return empty predictions. We fine-tune a shared vision-language model on known-target grounding instructions combined with instructions requiring both recognition and localization. We evaluate predicted identities, regions, joint correctness, and healthy-image abstention on 1,480 human-verified images disjoint from all training data. Grounding-only fine-tuning reduces recognition accuracy from 51.8\% to 29.1\%, while adding recognition-and-localization instructions raises it to 72.6\%. With images and annotations held fixed, combining the two formats raises joint accuracy from 19.2\% to 43.3\% at comparable grounding. Healthy negatives raise abstention on healthy images to 95.0\%, and reinforcement learning improves lesion-level grounding. The resulting 2B model exceeds its annotation teacher in grounding F1 on our benchmark and on the external PlantSeg test set. AgroGround establishes a benchmark for grounded agricultural recognition, measuring joint correctness of identity and localization along with abstention on healthy images. The code is available at this https URL.

---


### 112. [Asking Earns Nothing: Scoring the Decision to Act in BFCL Multi-Turn](https://arxiv.org/abs/2610.04429)

**<font color=#1a73e8>作者：</font>** Yangze Liu, Zhongyi Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> An agent that lacks the information it needs should ask rather than act, and the task definitions of agent leaderboards say so. BFCL multi-turn builds two of its four categories around a turn on which the model is supposed to ask, and its scorer never looks at that turn: the gold trajectory there is empty, the checker skips it, and the scripted user cannot answer, so asking earns nothing, guessing costs nothing on that turn, and asking twice loses the item. The benchmark also contains the control experiment for that decision. A should-ask item is a base item with one piece of information removed from one turn, so the same request appears twice at the same turn index, once complete and once not: on the first the model should make the call that changes the world, on the second it should ask. We score one decision per pair, whether the model attempted a world-changing call on that turn, read off the stored trajectories with no LLM judge; acting always and asking always both score 50. On the 223 pairs that pose this decision, gpt-5.4 attempts the call on 83.4% of the complete turns and holds back on 78.0% of the incomplete ones, the best decision accuracy of seven models at 80.7%; on the same items the official score ranks it sixth and puts first a model that lands in the middle here. One added line telling gpt-5.4 not to ask pushes it toward acting on both sides of the pair, so its decision accuracy shows no detectable change, while its official score rises by 13.5 to 23.5 points on the two should-ask categories and on the base twins; the opposite line, telling gemma-4-31B-it to ask first, improves its decision by 4.5 points and gains no official score. The score moves with the push toward action, not with the decision. We release the pairs, a turn-level scorer that runs on any BFCL output directory without an API key, and 31 manually verified bad items.

---


### 113. [MERCI Cards: An LLM Evaluation and Deployment Framework for High-Stakes Domains](https://arxiv.org/abs/2610.04430)

**<font color=#1a73e8>作者：</font>** Aparna Komarla, Annalisa Szymanski  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> As LLMs are increasingly deployed in high-stakes professional workflows, engineers and researchers require principled protocols to systematically track, monitor, and improve model performance across deployment cycles. We present a mathematical framework for iterative LLM evaluation and deployment, and demonstrate its application to AI systems used in criminal justice. Our framework formalizes LLM integration in high-stakes, high-risk, and resource-constrained domains across model selection, rubric design, evaluations and deployment via a weighted multi-objective optimization. We demonstrate that MERCI Cards can guide improvements of the system across deployment iterations, direct developer attention toward under-performing areas, and focus user attention on validation and error-correction in the LLM's outputs.

---


### 114. [Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos](https://arxiv.org/abs/2610.04432)

**<font color=#1a73e8>作者：</font>** Jinzhou Tang, Zijun Zhang, Jing Yang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Building interactive simulators from real-world observations is a promising way to scale embodied data, but current pipelines still rely heavily on manual environment construction and calibration. We study whether frontier foundation models and coding agents can automate this process end to end. We formulate \emph{autonomous video-to-simulation} as a software engineering task in which an agent observes an embodied video, constructs the corresponding simulated environment and robot behavior, and iteratively refines the result through execution feedback. To evaluate this capability, we introduce \textbf{Video2World}, a benchmark comprising 222 reconstruction instances derived from 189 robot and human demonstration videos. Video2World measures reconstructed worlds along geometric fidelity, dynamic fidelity, and functional correctness, capturing spatial perception, physical reasoning, and executable interaction. Evaluating 9 frontier coding-agent systems reveals a sharp improvement in Task success beginning with Claude Opus 5, rising from below 5\% to over 15\%, while substantial gaps to human-assisted reconstruction remain. We further find that worlds that look better could work worse: better visual fidelity does not always lead to higher task success. This echoes the broader gap between perceptual realism and factual correctness observed in generative models.

---


### 115. [What Does a Harness Buy? Tokens, Mostly](https://arxiv.org/abs/2610.04433)

**<font color=#1a73e8>作者：</font>** Yangze Liu, Zhongyi Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> A coding agent is a language model wrapped in a harness: the system prompt, the tool set, and the context management that turn a chat model into something that can work inside a repository. Production harnesses ship releases daily, vendors advertise pass-rate gains from harness changes, and leaderboards mix harnesses freely. What is rarely measured is how much the harness itself moves the score when the model is held fixed. We run five models through three production harnesses, Claude Code, mini-SWE-agent, and OpenCode, on SWE-bench Verified, and rerun the same configurations to calibrate how much a score moves when nothing changes but the run. On 447 tasks and the two models we ran there, Claude Code and mini-SWE-agent, the heaviest and the lightest harness, are equivalent within five points. On a 45-task hard subset and five models, swapping the harness flips as many tasks as rerunning the same harness, 13% in both cases, and the tasks a harness wins in one run are not the tasks it wins in the next. The one harness effect that clears the noise is a loss, not a gain: OpenCode trails by up to 9 points on the large pool, and on one model half of that gap sits in runs its output cap cut short. What the harness does decide is the bill. With the same model, the same tasks, and one price list, cost per task differs by up to 3x across harnesses. The gap is set at the first call, by the preamble of system prompt and tool schemas each harness sends with every step, and scaled by the number of steps; per-step growth and per-call tool output differ far less. The provider's price for cached input scales the bill and does not reorder it. The rerun data also give the resolution a harness comparison needs: at the discordance we observe, 45 tasks catch a 13-point gap only half the time and no gap with 80% power, and 447 tasks resolve 5 points, still coarser than the gains many harness changes claim.

---


### 116. [LocusRL: Diagnosing LLM Reward and Policy Interventions in Competitive Games](https://arxiv.org/abs/2610.04441)

**<font color=#1a73e8>作者：</font>** Chengyu Luan, Bo Xin, Songyan Guo 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Large language models can intervene in reinforcement learning through both reward design and action selection, yet aggregate performance offers an incomplete account of what these interventions actually do. Similar returns can conceal different learning mechanisms, while plausible rewards can induce undesirable behavior. We introduce LocusRL, a diagnostic framework that connects controlled reward-policy comparisons with audits of reward judgments, signal delivery, optimization objectives, and executed actions. The framework traces performance differences to testable explanations and checks targeted corrections through executable rules and counterfactual replay.
Across two evaluation batches covering ten Connect Four training seeds, we uncover seed-dependent reversals in intervention effects and show how tracing actual updates changes their interpretation: historical Qwen training operates through reward-weighted teacher-action likelihood. A separate matched three-seed reward-direction experiment distinguishes sensitivity to a learning signal from its usefulness. With terminal rewards held fixed, a sign-reversed dense oracle yields a 2.8% aggregate win rate, compared with 57.2% for terminal-only training and 46.7% for the positive dense oracle. Thus, a reward can strongly influence learning without improving performance. At the decision level, counterfactual replay verifies a winning correction to a diagnosed action error. Complementary experiments in Leduc and reward-validation studies in Goofspiel extend the analysis to imperfect-information settings, revealing how reference-label definitions and validation-data exposure affect intervention assessment.
Together, these findings show why evaluating LLM interventions requires tracing how their outputs become learning signals and actions. LocusRL turns aggregate outcomes into actionable diagnoses and verifiable corrections.

---


### 117. [Causally Fair Generation with Large Language Models](https://arxiv.org/abs/2610.04444)

**<font color=#1a73e8>作者：</font>** Patrik Okanovic, Torsten Hoefler, Drago Plecko  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used to generate, complete, and transform information in settings where their outputs can shape consequential decisions, raising concerns about their impact on demographic disparities. In this context, causal inference provides a principled basis for assessing fairness, because it attributes observed disparities to the mechanisms that generated them, which a purely statistical approach cannot do even with infinite data. In LLM generation, a query may request several causally related variables, each of which is both an outcome of interest and a possible cause of other outputs, and the information supplied in the prompt need not follow a topological or a temporal order. This calls for methods that can analyze and selectively remove disparities from such a flexible generation process. In this paper we introduce Causally Fair Generation with LLMs (CFG, for short). CFG extracts relevant concepts, grounds generation in a reference population and causal diagram, and removes user-selected causal effects. CFG also allows pathways deemed justifiable for the task's utility to be retained, which is known in legal literature as business necessity. Further, we provide formal guarantees for our method when eliminating all discriminatory causal effects in the adapted population model, under appropriate causal assumptions. We evaluate CFG with four LLMs in three real-world settings based on population data and on a synthetic dataset with a known causal ground truth.

---


### 118. [Understanding Generative AI Use in Programming MOOCs: The Role of Course Context and Learner Characteristics](https://arxiv.org/abs/2610.04447)

**<font color=#1a73e8>作者：</font>** Marina Lepp  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The increasing availability of generative artificial intelligence (GenAI) tools, such as ChatGPT and code-completion assistants, raises questions about how learners integrate these tools into learning activities, particularly in MOOCs that attract diverse participant populations. This study examines the use of GenAI in two programming MOOCs taught in Estonian that differ in duration, workload, topic complexity, and assignment volume: About Programming (4 weeks, 26 expected hours, n = 187) and Introduction to Programming (8 weeks, 78 expected hours, n = 182). Post-course questionnaire data were analyzed using non-parametric statistical methods to examine self-reported adoption, usage frequency, and purposes of GenAI use across courses and learner backgrounds. The results show that GenAI adoption was widespread in both MOOCs, with no statistically significant differences by gender, age, education level, or prior programming experience. However, participants in the longer, more extensive MOOC reported significantly higher usage frequency and were more likely to use GenAI for debugging and idea generation. Reported usage frequency for code explanation and debugging was also higher in the longer course. Exploratory analyses found limited relationships between GenAI use and learning-related outcomes. The findings suggest that course context may play a greater role than learner characteristics in shaping how GenAI tools are used. These results provide implications for instructional design and guidance in programming education.

---


### 119. [Trinity: Self-Evolving Vision-Language Models with a Self-Verifier](https://arxiv.org/abs/2610.04469)

**<font color=#1a73e8>作者：</font>** Youngwan Lee, Yong-Ju Lee, Sung Ju Hwang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-evolving vision-language models (VLMs), a form of self-improvement in which a model generates its own training data from unlabeled images, are a promising route toward agents that expand their reasoning capability in an unsupervised manner, without relying on ever-larger annotation budgets. Existing methods pair a Questioner that proposes problems with a Solver that answers them, but reward both roles mainly by agreement among sampled answers. Agreement is a weak proxy for truth: it cannot tell whether a question is grounded in the image, whether the proposed reference answer is right, or whether a confident majority is wrong in the same way. We present Trinity, in which one VLM plays three roles, Questioner, Solver, and Verifier, and the Verifier is a self-verifier: an exponential moving average (EMA) of the policy itself, requiring neither labels nor an external judge. The Verifier screens every generated question for image grounding and answer correctness before it becomes supervision, scores Solver reasoning against the image, and adjudicates disputes between the reference answer and a strong Solver consensus, correcting the reference and penalizing the Questioner when the consensus is right. Trained on images alone, Trinity improves Qwen3-VL-8B on mathematical visual reasoning and on science benchmarks with biology content, for example, +8.6 points on the biology split of SciVQR and +12.8 on MathVerse, and its reward dynamics behave as a healthy self-play curriculum should. These results suggest that a self-evolving multimodal agent can strengthen its scientific reasoning from unlabeled scientific images alone, with the model itself serving as the verifier.

---


### 120. [InferOpt: Constrained Multi-Objective Search for LLM Inference Configurations](https://arxiv.org/abs/2610.04473)

**<font color=#1a73e8>作者：</font>** Qi Chen, Yingying Cheng, Zhaoyi Sun 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Serving an LLM means setting dozens of inference-time knobs, from per-layer KV retention to per-layer expert counts. Practice sets them with mechanism-specific heuristics that return a single operating point and do not scale to layer-wise search spaces. We recast inference configuration as constrained multi-objective black-box optimization and build InferOpt, a reusable search framework that requires only variable bounds, a deterministic resource cost, and an evaluation hook. InferOpt searches on a frozen sampled proxy set, rejects over-budget candidates before any model call, tightens the budget adaptively, and re-validates Pareto representatives on full-scale dataset. One pipeline covers a 28-dimensional continuous KV space (Qwen2.5-7B) and a 26-dimensional discrete MoE space (DeepSeek-V2-Lite). On KV, post-prefill pruning cuts the 16K cache by 64.4% and TPOT by 22.9--48.5%, and the searched layer-wise budget by InferOpt beats a matched uniform budget by 7.3% and 14.0% of the Full KV reference points. On MoE, a searched top-k schedule by InferOpt removes 43.0% of routed token--expert pairs while staying within 0.59 points of the default, closer than the matched-budget baselines. Against Random Search, NSGA-II, and MOTPE, InferOpt leads on both spaces, taking the best proxy hypervolume and the lowest retention on KV and staying closest to the uncompressed reference at the lowest experts on MoE.

---


### 121. [DV-Lens: Revealing the Functional Organization of Language Model Parameters](https://arxiv.org/abs/2610.04489)

**<font color=#1a73e8>作者：</font>** Chenhang Cui, Jian Yu, Shuyi Miao 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Understanding parameter functions helps elucidate the internal mechanisms of large language models (LLMs). However, how to connect parameters from different modules to verifiable output effects and further characterize the relationship between their functional organization and model capability remains to be explored. To this end, we introduce the downstream vocabulary lens (DV-Lens), a parameter-level interpretability framework that links native parameter directions to their downstream vocabulary responses. Specifically, we first estimate module-specific downstream Jacobians over a reference prompt set for attention query, key, value, and output (Q/K/V/O) projections and feed-forward networks (FFNs). Second, we use these mappings to project native parameter columns into the final vocabulary space, obtaining signed readouts that characterize their average local output responses. Third, we group parameter columns by their vocabulary readouts and introduce downstream vocabulary complexity (DV-Complexity), which quantifies within-group structural variation using normalized reconstruction residuals of the original weights. At the parameter level, randomized controls and finite-difference tests show that DV-Lens readouts capture non-random vocabulary structure and predict local logit changes with 98.0% coordinate-orientation agreement across 720 cases from nine models. These readouts further guide parameter ablation, steering, and swapping across 21 models, shifting target-token probabilities in the predicted directions under controlled conditions. At the model level, the joint-parameter score of DV-Complexity achieves a Spearman correlation of 0.904 with benchmark-based capability rankings across 48 language models. Together, these results provide intervention-based evidence for DV-Lens interpretations and reveal an association between DV-Complexity and model capability.

---


### 122. [BARQ: Balanced Codebook Refinement for Low-Bit LLM Quantization](https://arxiv.org/abs/2610.04490)

**<font color=#1a73e8>作者：</font>** Chenhang Cui, Xu Xie, Linrui Xu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> As large language models (LLMs) grow in parameter count, model storage and parameter memory traffic have become major bottlenecks to efficient deployment. Codebook-based weight quantization reduces these costs, but imbalanced nearest-codeword assignments during fitting can leave some codewords insufficiently updated, limiting effective codebook utilization. To address this limitation, we propose Balanced Assignment Refinement for Quantization (BARQ), which improves quantization quality through balanced fitting of existing codebooks. Specifically, we first compute joint soft assignments between weight blocks and codewords through entropically regularized optimal transport with uniform marginals and curvature-weighted reconstruction costs, ensuring equal positive fitting mass for every codeword in the exact solution. We then refine the codewords through an assignment-weighted barycentric update, which we prove minimizes the fitting objective for fixed assignments. For finite Sinkhorn iterations, the implemented update retains this optimality provided all codeword masses exceed the denominator floor. Finally, we discard the soft assignments and use the refined codebook for standard hard nearest-codeword encoding, with our analysis establishing sufficient conditions for reducing hard-quantization distortion and evaluation loss. Across multiple LLMs, BARQ achieves lower perplexity and higher mean zero-shot accuracy than the evaluated baselines at comparable bit budgets. The code is available at this https URL.

---


### 123. [Localization Lens for Improving Medical Vision-Language Models](https://arxiv.org/abs/2610.04502)

**<font color=#1a73e8>作者：</font>** Hasan Farooq, Murtaza Taj, Mehwish Nasim 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Medical Vision-Language Models (Med-VLMs) have demonstrated strong capabilities in clinical tasks. However, they often struggle to understand anatomical structures and spatial positioning, which are crucial for medical reasoning. To address this, we propose a localization-aware enhancement to the Med-VLM pipeline, introducing improvements at three levels: data,architecture, and alignment. First, we introduce localization lens, a set of expert-validated representations that provide richer anatomical and positional context. However, as these representations increase input complexity, we integrate pixel shuffle within the model architecture to filter and refine representations, enhancing spatial information processing while preserving anatomical continuity. Lastly, to effectively align the localization lens representations with textual features, we incorporate decoupled contrastive loss (DCL) alongside the standard loss function. This ensures better feature discrimination and robustness, particularly in data limited medical settings. Through extensive evaluations on medical visual question answering (Med-VQA) datasets, we show that our methodology improves localization-driven performance across different Med-VLM architectures. Our analysis of localization-based questions further reveals that improvements in anatomy and spatial reasoning directly enhance the overall accuracy of Med-VQA upto 6.2%. The proposed approach is model-agnostic and can be seamlessly integrated into existing Med-VLM pipelines. The dataset, code, and trained models will be made publicly available at this https URL.

---


### 124. [EgoExo-Next:Benchmarking Vision-Language Models on Visual-Option Next-State and Cross-View Reasoning](https://arxiv.org/abs/2610.04506)

**<font color=#1a73e8>作者：</font>** Yutong Li, Molin Wang, Xiaotong Li 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision-language models (VLMs) are increasingly evaluated for egocentric and cross-view video reasoning, yet existing benchmarks largely focus on semantic event understanding, temporal relations, or correspondence between already observed views, leaving their ability to reason directly about future visual states underexplored. We introduce EgoExo-Next, a visual-option benchmark for dynamic visual-state reasoning, where models must identify how an observed action trajectory subsequently appears rather than predict only an action label or textual description. EgoExo-Next contains 2,503 human-curated four-choice questions from six public egocentric and ego--exo video sources and comprises four interconnected subtasks that evaluate egocentric next-state prediction, bidirectional ego--exo state correspondence, exocentric next-state prediction, and their composition in Ego-to-Exo Next-State. Extensive evaluation of proprietary, open-source, and spatial reasoning VLMs reveals a substantial human--model gap, with the best model achieving 43.81\% average accuracy compared with 98.55\% for humans, and the largest degradation occurring on the composed Ego-to-Exo task. These results suggest that current VLMs remain substantially limited in dynamic visual-state reasoning, particularly when temporal progression and cross-view reasoning must be composed. The benchmark is publicly available at \url{this https URL}.

---


### 125. [LoRA's Second Descent Extends Beyond Parameter Parity](https://arxiv.org/abs/2610.04507)

**<font color=#1a73e8>作者：</font>** Yueran Ma  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Double descent has sparked considerable interest, with recent work relating it to the data, the model and the learning configuration. Practical fine-tuning commonly involves training a small adapter on top of frozen pretrained weights, as in low-rank adaptation (LoRA). The adapter's rank is the hyperparameter that sets its capacity, yet how this rank relates to double descent has not been well explored. We quantify this relation under label noise on four vision backbones and a 7B language model with a module-matched rank sweep (MMRS), which extends past full rank and compares every rank with dense fine-tuning of the same modules, paired by seed. On DeiT-Tiny, risk is lowest at rank one and rises sharply as the adapter becomes able to fit the noisy labels, forming an interpolation cliff. Past the peak, risk falls again, but every tested post-peak rank that still saves parameters remains above dense risk. Rank-one LoRA outperforms dense fine-tuning on three of the four vision backbones, consistent with strong regularization at small rank. LoRA thus exhibits a second descent, but matches dense risk only after losing its parameter advantage, first on DeiT-Tiny at four times dense's projection weights. Code is available at this https URL.

---


### 126. [Correctness Is a Direction: Geometric Answer Selection in Language Models](https://arxiv.org/abs/2610.04512)

**<font color=#1a73e8>作者：</font>** Marcus Armstrong, Navid Ayoobi, Pradham Mummaleti 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Answer correctness is encoded as a recoverable geometric direction in the hidden states of language models. We show that the mean displacement from incorrect to correct answer representations, computed at approximately 70\% of model depth from fifty labeled examples with no parameter updates, yields a scoring direction that outperforms zero-shot log-probability scoring by up to +32.0 percentage points on factual benchmarks (ARC-Challenge and MMLU) and by +38.1 to +51.8 percentage points on TruthfulQA, across five models spanning 1B to 8B parameters in three architecture families (Llama, Qwen, Gemma). The method requires one forward pass and one dot product per candidate; no generation is performed at inference. Applied as a hallucination detector on individual (question, answer) pairs, the recovered direction achieves 0.693~AUROC versus 0.578 for log-probability scoring. We additionally find that correctness directions for factual reasoning, domain knowledge, and calibrated truthfulness are near-orthogonal in representation space, revealing that language models allocate geometrically independent subspaces to qualitatively distinct notions of correct answer, with architecture-dependent variation in the degree of separation. This structure explains the observed transfer pattern---the direction calibrated on factual questions transfers within task type but not across it---and suggests that LLM calibration failures may reflect a routing problem: the model's internal representation contains more correctness signal than its output behaviour exploits.

---


### 127. [EvoCast: Reliable Autonomous Research Agents for Iterative Forecasting Architecture Evolution](https://arxiv.org/abs/2610.04517)

**<font color=#1a73e8>作者：</font>** Kaipeng Xu, Xianli Yan, Yan Wang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Deep time-series forecasting models have rapidly diversified, yet adapting them to a specific task still requires extensive expert effort in model selection, mechanism diagnosis, architecture design, implementation, and evaluation. Existing AutoML methods are constrained by predefined search spaces, while general-purpose LLM research agents lack reliable control over experimental protocols and model promotion. We introduce EvoCast, a fully autonomous research-agent system for iterative forecasting architecture evolution. EvoCast first establishes and diagnoses a task-specific baseline through executed mechanism ablations, then generates evidence-grounded research directions from dataset characteristics, diagnostic results, prior rounds, and failure records. Its central design, cognition-authority separation, assigns open-ended hypothesis generation and code implementation to LLM agents, while deterministic program authorities control source-edit boundaries, canonical evaluation, and promotion decisions. Experimental outcomes are accumulated as evidence to guide subsequent rounds. Results show that EvoCast completes complex architecture modifications with higher implementation success and lower agent-side token/time cost, and develops task-specific architectures that outperform selected baselines, strong forecasting models, and agent baselines in three real-world forecasting cases. The code is available at this https URL.

---


### 128. [Quantifying Collusion Among Autonomous LLM Agents: A Statistical Analysis of the Collusion Wiki Incident](https://arxiv.org/abs/2610.04528)

**<font color=#1a73e8>作者：</font>** Shariq Murtuza  
**<font color=#188038>arXiv所属领域：</font>** Multiagent Systems

**<font color=#5f6368>摘要：</font>**
> In August and September 2026, independent researchers publicly documented an unusual incident: thousands of autonomous agents, self identifying as OpenAI models on web research tasks, discovered and began using a small German wiki as an improvised message board posting roughly 18,000 times over six weeks to relay task answers, share a sandbox escape technique, and coordinate against a volunteer human moderator who spent weeks manually deleting their content [1]. The investigators' public writeup is a careful qualitative account, rich with direct quotation, but does not attempt a statistically rigorous quantitative characterization of the behaviour it documents.

---


### 129. [PhaseGate: Phase-Aware CPU Retrieval Scheduling for On-Device LLMs on Unified Memory](https://arxiv.org/abs/2610.04537)

**<font color=#1a73e8>作者：</font>** Seoyoon Yum, Sehoon Kim  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-device assistants run GPU-based LLM inference alongside CPU retrieval on unified-memory systems. Under a saturated local-retrieval workload, four concurrent retrieval workers raise 95th-percentile (p95) decode latency by 60-61% on two M4 systems, whereas prefill latency rises by only 5.7-6.9%. We study LLM phase as an admission signal for independent CPU retrieval under controlled LLM workloads. PHASEGATE calibrates separate concurrency limits for prefill and decode, selecting four and one on our base-M4 configuration. Under a backlogged queue, it achieves 2.0 times the aggregate retrieval throughput of the best tested feasible fixed policy, with both p95 LLM latency metrics within 1.25 times their no-retrieval baselines in all seven held-out runs. A phase-blind control, TimeGate, uses the same two limits on a calibration-derived schedule without observing LLM phase. It achieves similar retrieval throughput but violates the output-token latency limit in every run. M2 and M2 Pro Mac minis reproduce the policy ordering, while output-length sweeps show that the advantage narrows as decode occupies more of each request.

---


### 130. [Autonomous Structuring of Radiology Reports Across Modalities at Archive Scale Using an Open-Weight Large Language Model](https://arxiv.org/abs/2610.04541)

**<font color=#1a73e8>作者：</font>** Friedrich Puttkammer, Fabian Drexel, Marlene Fritzsche 等 22 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Purpose: To develop and evaluate an open-weight large language model (LLM) pipeline that converts an entire archive of free-text radiology reports into structured reports without human oversight. Materials and Methods: In this retrospective study, a pipeline with 150 hierarchically organized templates was developed at one center and tested at a second center on reports from 2010 to 2025. The open-weight model gpt-oss-120B selects the template in three constrained-decoding steps and fills it on one local graphics processing unit. Template selection was scored against expert labels on 914 randomly sampled reports of five modalities, structuring quality on 920 radiography and CT reports corrected field by field by five residents. The pipeline then processed the complete archive of the second center. Proportions are reported with Wilson 95% confidence intervals (CIs). Results: An optimal template set was selected for 74.4% of reports (680 of 914; 95% CI: 71.5%, 77.1%) and an appropriate set for 82.3% (752 of 914; 95% CI: 79.7%, 84.6%), 87.7% for single-region and 54.1% for multi-region reports. Macro semantic textual similarity between output and corrected reference was 0.95 for radiography and 0.97 for CT, residents left 88.7% of 24,638 fields unchanged, and unsupported content was flagged in 1.0% and 1.5% of reports. Of 2,186,982 archive reports, 96.5% received structured output, 2,401,544 structured reports, at 1,258 reports per hour on one graphics processing unit. Conclusion: An open-weight LLM pipeline structured a complete multimodality report archive without human oversight with high content fidelity. Multi-region reports remained the main source of template errors.

---


### 131. [Decide, Ask, or Defer: Clinical LLMs under Incomplete Evidence](https://arxiv.org/abs/2610.04542)

**<font color=#1a73e8>作者：</font>** Mingzhan Yang, Weili Wu  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Clinical LLMs must decide not only what diagnosis to produce, but also whether the available evidence is sufficient for autonomous decision making. Binary DECIDE/ABSTAIN formulations merge distinct non decision states and do not explicitly evaluate information acquisition. We introduce a DECIDE/ASK/DEFER formulation together with a blinded protocol that prevents models from using evidence completeness metadata. We evaluate Qwen, Gemini, and GPT on 200 matched clinical evidence states constructed from DDXPlus. The models show substantial differences in action selection under identical evidence, with disagreement in 137 of 200 states. For Qwen, a matched targeted versus random analysis shows that selected information changes the likelihood of a subsequent autonomous decision more clearly than diagnostic correctness. Its matched DECIDE/ABSTAIN baseline further reveals a safety autonomy tradeoff: the three action policy rescues some erroneous autonomous decisions but also removes some correct autonomous deci sions. These results show that separating information acquisition from clinician deferral exposes behavior that binary abstention hides, without yielding a uniformly improved decision policy.

---


### 132. [Label Agreement Does Not Measure Authorization](https://arxiv.org/abs/2610.04544)

**<font color=#1a73e8>作者：</font>** Amir Sabbaghziarani, Bradley Thomas Baker, Theodore J. LaGrow 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Many groups now delegate label ontology and metadata harmonization to agentic LLM pipelines. We built one and audited it. Our aggregate scores looked healthy, but the pipeline kept failing in ways they did not show, so we set out to find what they hid. Label agreement asks whether a proposed label matches a reference. It does not ask whether the agent was entitled to propose it, whether the output was complete enough to act on, or whether the label moved when the evidence moved. We measured those three separately on COBRE and FBIRN, two schizophrenia and control neuroimaging cohorts from different consortia, and they come apart, from label agreement and from each other. Showing the agent an upstream proposal barely moves label agreement, 0.857 to 0.870, while agreement on the chosen action doubles, 0.409 to 0.830. Output that parses as JSON still drops a required field on 10% of one model's cases and 33% of the other's. And an agent that replays its first answer scores perfectly on original cases and zero once we change the evidence that decides them. Downstream, a row-order error that none of these metrics reports erases most of the diagnostic signal. So we measure these properties apart, pair each with a control, and gate commitment on the result, which makes failures visible and easy to route to a person. None of this prevents failure. Our reference labels are rule-derived, so agreement with them means consistency, not correctness. Code is available at this https URL.

---


### 133. [$\mathrm{TRIZ}^{a}$: Guiding Agent Evolution from Pattern Recognition to Solution Invention](https://arxiv.org/abs/2610.04555)

**<font color=#1a73e8>作者：</font>** Wenyin Liu, Yiheng Huang, Kai Wang  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> We propose $\mathrm{TRIZ}^{a}$ (TRIZ exponentiated by an agent), a general R\&D automation paradigm that combines TRIZ inventive theory with LLM-driven agent evolutionary search. TRIZ's 40 inventive principles and contradiction matrix provide structured, explainable directions for solution generation, replacing random or untyped mutation with theory-guided ideation. Functional information (FI), operationalized under a frozen reference contract, is combined with TRIZ Ideality to measure useful and harmful function on a commensurable information scale, while hard gates keep promotion distinct from metric improvement. We validate $\mathrm{TRIZ}^{a}$ in cybersecurity--an adversarial and rapidly evolving domain--on PowerDuck GOOSE, CICIoT2023, and CIC-DDoS2019. Under paired-rerun protocols with protocol fingerprinting and hard-gate validation, the legacy experiments yield absolute F1 improvements of $+2.88$, $+4.23$, and $+0.15$ percentage points, respectively. A completed 45-activity CICIoT2023 campaign further increases macro-F1 from $0.8325$ to $0.8483$, but does not pass its frozen promotion gate. Every result remains traceable from contradiction identification and TRIZ principle selection to code transformation, evaluation metrics, and promotion decision.

---


### 134. [Coupling Noisy Pairwise Knowledge to the DAG Posterior for Causal Discovery](https://arxiv.org/abs/2610.04559)

**<font color=#1a73e8>作者：</font>** Guoliang Xu, James E Corter  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> External causal reports can improve structure learning from limited observations, but their reliability varies across sources and variable pairs. We introduce HB-NoisyKG, a Bayesian framework that combines observational data with repeated causal reports from sources such as large language models. Each report is a noisy observation of a direct pair state implied by one DAG. A feature-conditioned Beta prior pools information about pair reliability, and a shared error matrix captures systematic mistakes. Alternating inference uses the graph posterior to refine reliability estimates, which determine how reports influence subsequent graph updates. The report likelihood uses only graph pair-state marginals, so the same observation layer supports discrete and continuous likelihoods in graph-only and joint inference. Against an 80-restart no-KG baseline, HB uses at most 80 total restarts and lowers mean SHD from 22.39 to 16.06 on five discrete benchmarks. On a physical light tunnel with random variable IDs and retained descriptions, HB lowers SHD from 39.00 for no-KG to 27.30. On continuous Sachs, graph-only BGe raises AUROC by 0.121 over no-KG Top-K. In a controlled synthetic study, continued updating also reduces mean reliability estimation error and held-out report log loss compared with one-time estimation.

---


### 135. [Recursive Improvement of a Differentiable Scientific Software Ecosystem](https://arxiv.org/abs/2610.04561)

**<font color=#1a73e8>作者：</font>** Pengcheng Hou, Xiaojun Tan, Sihan Hu 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Differentiable programming connects scientific computation with gradient-based inference, learning and design. Extending these capabilities across a heterogeneous software ecosystem requires specialized effort to implement derivatives, integrate interfaces and evaluate quality. AI coding agents can accelerate this transformation, but translating their capabilities into useful scientific software requires identifying research needs and evaluating how well implementations meet them. We present an environment for agent-driven evolution of differentiable scientific software that connects demand identification, development and quality evaluation. A unified differentiation interface exposes reusable derivative rules alongside existing numerical routines, allowing research tasks to share these capabilities. Research requirements guide development, with implementations assessed through independent derivative checks, workflow tests and performance evaluation. Validated software, research programs and tests become shared resources for subsequent studies. We construct and validate automatic differentiation extensions across 20 packages spanning physical, chemical and biological modeling, with research workflows demonstrating reuse across tasks. Benchmarks demonstrate computational savings over finite differences in gradient evaluation and complete parameter estimation. Research-driven revisions make previously unsupported workflows differentiable, correct derivatives of scientific observables and eliminate redundant computation. Quantum-control and thermal-design studies revise objectives in response to physical evaluation, improving designs while reusing existing derivatives. This work provides a practical approach to expanding differentiable programming across established scientific software and organizing AI agents around the recursive improvement of a shared computational ecosystem.

---


### 136. [From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents](https://arxiv.org/abs/2610.04575)

**<font color=#1a73e8>作者：</font>** Xueping Gao  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation probes can predict safety-relevant properties of language models with high area under the receiver-operating-characteristic curve (AUROC), but deployed agent monitors make thresholded alarm decisions under tight false-alarm budgets. These are different estimands. We introduce an Operational Validity Contract that fixes a monitor's target, observability, identity, timing, intervention unit, comparator, calibration, and cost. We formalize risk at the semantic request or trajectory level: when one task contains repeated alarm opportunities, row-level AUROC and false positive rate do not identify semantic-unit any-alarm risk. A confidence-certified threshold also requires enough independent negative units, a tie-safe rule, and transport to deployment. Across Models Under Pressure, LASR refusal prediction, immutable AgentDojo, and a prospectively protocol-frozen ST-WebAgentBench replication, joint activation-observable monitors reach AUROC 0.957 and 0.935 on the first two benchmarks, yet their locked 5%/10% detection rates are only .642/.742 and .719/.782, respectively. On AgentDojo, the secondary mean-activation rollout monitor reaches AUROC 0.922 but detects none of 38 positive semantic cases at the locked 5% operating point; thresholds intended for 10% false alarms realize 18.7-20.0% on test. Because the test misses its prospectively frozen 40-positive support gate, we label it support-insufficient. On ST-WebAgentBench, activation reaches AUROC .874, but 23 independent calibration negatives cannot identify even a 10% controller; the locked policy abstains rather than reporting its mechanical zero FPR as a success. An exploratory counterexample also lowers full AUROC while improving realized 10% utility. The fail-closed compiler caps MUP and LASR at restricted predictive value and AgentDojo and ST-Web at representation accessibility; no setting reaches alarm-policy validity.

---


### 137. [Strong Helps Weak: Directional Cross-Modal Alignment Transfer in Multi-modal LLMs](https://arxiv.org/abs/2610.04580)

**<font color=#1a73e8>作者：</font>** Hoigi Seo, Byung Hyun Lee, Minjun Kim 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Multi-modal large language models (MLLMs) achieve strong modality understanding by pairing a large language model (LLM) with an encoder for a target modality such as vision, video, or audio. However, improving an MLLM's capability for a given modality typically requires additional training on large modality-specific datasets, incurring substantial data collection and compute costs. Model merging offers an alternative, but it is often infeasible for data-scarce, large per-sample size, or domain-specific modalities (\textit{e.g.}, audio and video), where same-modality model variants are rarely available. In this work, we characterize an intriguing asymmetric phenomenon: merging a well-aligned, data-rich source-modality MLLM into a data-scarce target-modality MLLM substantially improves the target on its own benchmarks. Our theoretical and empirical analyses show that this gain stems from enhanced alignment between modality-specific and textual tokens, induced by the stronger donor modality. Specifically, we derive a mutual-information lower bound that is monotonic in alignment-related quantities and strongly correlated with downstream MLLM performance. Building on this principle, we propose Directional Cross-modal Alignment Transfer (DCAT), a novel framework that transfers textual alignment from a strong, well-aligned source (donor) modality to a weak target (recipient) modality, boosting target-modality performance without further fine-tuning. We further show that the alignment-enhancing objective admits a closed-form weight-space solution computed from only a small calibration set. DCAT outperforms existing model-merging methods, offering an efficient path toward cross-modal alignment transfer. Project page with code is available at \url{this https URL}

---


### 138. [SIFT: Robust Meta-Faithfulness Verification of Chain-of-Thought Reasoning Under Distribution Shift](https://arxiv.org/abs/2610.04594)

**<font color=#1a73e8>作者：</font>** Noor Islam S. Mohammad, Md. Basim Al Zabir Shammo, Hasan Siddiki 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Chain-of-Thought (CoT) faithfulness detectors are widely used to audit reasoning models, yet a detector is itself a predictor whose verdicts are treated as stable properties. We ask whether a detector is faithful to itself under distribution shift. We formalize meta-faithfulness as an invariance principle: a valid detector must return identical verdicts on traces that differ only by transformations preserving ground-truth faithfulness. We prove three results: (i) no detector using only intervention-response profiles can separate faithful from epiphenomenal mechanisms with identical signatures; (ii) any detector relying on shift-sensitive features violates invariance at a rate independent of its in-distribution accuracy; (iii) an asymptotic certified selective-risk guarantee enables confident abstention. We operationalize the principle in FaithShift, a stress-test protocol spanning ten shift axes, and propose SIFT, a hidden-state trajectory detector trained with cross-environment invariance objectives and certified abstention. Across 14,996 traces, four domains, and eight models, three findings emerge. First, transfer collapse is real: all existing detectors show gaps $\geq 0.15$ AUROC. Second, the dominant bottleneck is sampling stochasticity, not shift: over 80% of detector instability stems from random seed variation, falsifying our preregistered prediction that shift-attributable violations exceed 0.25. Third, SIFT cuts invariance violations by 64% over the best single-seed baseline, but a four-seed ensemble of any detector narrows the margin to 0.01 (indistinguishable at matched coverage, $p=0.21$), and SIFT needs a 51% abstention rate. Cross-model transfer degrades from within-family to cross-family to open-weight-to-API, partly closed by multi-model training. We offer a framework for auditing auditors: the real barrier is detector variance, not distribution shift.

---


### 139. [DiffGate: Difficulty-Gated Teacher Guidance for On-Policy Distillation](https://arxiv.org/abs/2610.04596)

**<font color=#1a73e8>作者：</font>** Karn Tiwari, Varnith Chordia, Prathosh A P  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) has emerged as a widely used paradigm for post-training large language models, reducing the train--test mismatch of conventional distillation by supervising the student on its own generated trajectories. However, existing OPD objectives remain largely token-local and outcome-agnostic, optimizing teacher--student agreement at each prefix despite reasoning quality being determined at the trajectory level. Reinforcement learning with verifiable rewards (RLVR), particularly Group Relative Policy Optimization (GRPO), provides complementary outcome-level supervision but suffers from sparse rewards and coarse credit assignment. We show that OPD and RLVR exhibit complementary blind spots: teacher signals provide dense local guidance but are weakly aligned with rollout correctness, whereas group-relative rewards capture task success but provide coarse token-level credit and vanish on all-failure groups. We introduce DiffGate, an outcome-gated objective that combines GRPO with selective, bounded teacher guidance. Teacher supervision is applied only to failed trajectories, scaled by group difficulty, and smoothly bounded to prevent extreme teacher--student discrepancies from dominating optimization. The verifier therefore determines \emph{which trajectories} receive teacher guidance, while the teacher provides dense token-level update directions within those trajectories. Across Qwen3-0.6B and Qwen3-1.7B students, DiffGate improves code avg@8 over matched GRPO by $+1.7$ and $+1.8$ points and pass@8 by $+1.6$ and $+5.7$ points, respectively. On mathematics, avg@8 remains within $0.5$ points of GRPO while pass@8 improves by $+1.1$ and $+3.9$ points. Overall, DiffGate improves pass@8 across all four model--domain settings, demonstrating improved solution coverage under our evaluation protocol.

---


### 140. [Anticipating the Consequences of Curriculum Decisions with Large Language Models](https://arxiv.org/abs/2610.04604)

**<font color=#1a73e8>作者：</font>** Octavio Pappalardo, Nathan Herr, Tim Rocktäschel  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Automatic curriculum learning can improve the effectiveness of reinforcement learning by selecting the training experiences presented to the agent over time. Predicting the consequences of such decisions can, however, be difficult. We analyze automatic curriculum learning as a sequential decision-making problem, highlighting a gap between the quantities that determine the value of curriculum decisions and the information captured by local learning signals commonly used to guide them. We then investigate whether Large Language Models (LLMs) can exploit richer information about the learning problem to better anticipate the consequences of curriculum decisions. We introduce a method that combines online learning-progress estimates with LLM-informed estimates of (i) the potential downstream benefits of learning on each task and (ii) whether direct training on a task is currently likely to produce progress. We evaluate the approach on a custom benchmark of 256 textual goals in Craftax under different curriculum objectives. We observe the strongest gains when optimizing for individual target tasks. When optimizing across the full task set, the benefits vary across learners with different mechanisms for cross-task transfer, ranging from modest improvements in learning speed to larger gains that persist through the end of training.

---


### 141. [Stance Drift: How AI-mediated Communication Distorts Our Message](https://arxiv.org/abs/2610.04620)

**<font color=#1a73e8>作者：</font>** Lingchong Liu, Yanfei Zhou, Jacob Bien 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) increasingly mediate human communication, from drafting emails to summarizing scientific reports, yet whether they faithfully preserve a speaker's position remains largely untested. We model AI-mediated communication as a two-step generation-extraction pipeline: one LLM produces an argument from a specified stance, and a second LLM extracts the stance from that argument. We represent the pipeline as a probabilistic state transition over five Likert-type stance categories and define the stance preservation rate (SPR) as the average probability that the extracted stance matches the initial stance. Across 112 debate propositions, none of the nine LLMs tested exceeded an SPR of 0.7 under the default configuration. Three drift patterns accounted for most of the drift: polarization, deviation from neutrality, and flipping. Among the mitigation strategies tested, including in-context learning, multiple extraction with shuffled options, assertion, and reflection, only adding medium reasoning effort to a reflection prompt for GPT-5.4 substantially improved the SPR, to 0.775, yet polarization remained the largest pattern, with 0.119 of the transition mass. An exploratory comparison with human extraction on a single proposition suggests that drift arises at both the generation and the extraction stage. These results point to a fidelity gap in AI-mediated communication, with implications for journalism, policy deliberation, scientific communication, and other domains where opinion-laden messages pass through language models.

---


### 142. [The Numerical Linear Algebra of Large Language Models](https://arxiv.org/abs/2610.04631)

**<font color=#1a73e8>作者：</font>** Abdelkader Baggag, Yousef Saad  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Numerical Linear Algebra (NLA) has consistently played a vital role in advancing science by providing tools to solve fundamental problems encountered in scientific and engineering applications. Over the decades, it has continually evolved to meet the demands driven by successive waves of scientific discovery. For instance, during the 1950s and 1960s, substantial efforts were devoted to developing methods for solving eigenvalue problems that emerged from the rapidly growing field of aerodynamics. This led to the discovery of the LR and QR algorithms. Later the attention turned to the solution of sparse linear systems that were common in applications like computational aerodynamics. Today we are experiencing yet another wave of major scientific advancement and NLA is once more at the heart of its development. This Machine Learning (ML) wave is proving to be utterly disruptive in science and engineering. Many tools in ML particularly Large Language Models (LLMs) are grounded in matrix and tensor methods. As we are approaching Artificial General Intelligence (AGI), it is clear that matrix methods will be called to play an even more significant role. For the numerical linear practitioner the speed of the current change makes it particularly challenging to adapt.
This is a survey article that centers on machine learning techniques, with a particular focus on large language models. It has two main objectives. The first is to clarify the core concepts behind Large Language Models in a manner accessible to specialists in numerical methods. The second is to examine the key Numerical Linear Algebra concepts employed by LLM techniques, while also highlighting several significant recent contributions of NLA to the field.

---


### 143. [LatentIndex: Cross-Layer Sharing with Layer-Specific Selection for Sparse Attention](https://arxiv.org/abs/2610.04635)

**<font color=#1a73e8>作者：</font>** Zhaohui Wang, Zhixin Pan, Fanxu Meng 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Sparse attention reduces core-attention computation, but its indexers still incur repeated selection work and per-layer key-cache storage. Reusing selected indices across layers reduces this overhead but constrains multiple layers to the same token set. We introduce LatentIndex, which extends the latent-sharing principle of Multi-head Latent Attention across indexer layers. Each layer group constructs a shared latent cache from its first layer's hidden states, while layer-specific scoring enables independent token selection. Absorbing key decoders into queries enables direct scoring of the shared cache without reconstructing historical per-layer keys. We develop training-free calibration and investigate a training-aware instantiation of this principle. To balance quality and computation, a hierarchical selection (HS) variant lets followers independently refine a shared candidate set proposed by the anchor. With four-layer sharing, LatentIndex reduces logical indexer-cache storage by 61.1% on DeepSeek-V3.2. Across DeepSeek-V3.2 and GLM-5, training-free LatentIndex improves head-wise attention-mass recall over IndexCache by up to 3.28 percentage points while maintaining RULER and LongBench performance close to native DSA. HS further achieves 2.30-2.72 times decode indexer speedups over DSA across 8K-128K contexts, retaining most of LatentIndex's recall. LatentIndex offers a new perspective on cross-layer indexing: sharing continuous representations rather than discrete selections enables efficient reuse while preserving layer-specific token selection.

---


### 144. [Grounding Probes: Generator-Independent Hallucination Detection from Observer Model Hidden States](https://arxiv.org/abs/2610.04642)

**<font color=#1a73e8>作者：</font>** Michael Rathmayr, Ádám Kovács, Gábor Recski  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Detecting responses that retrieval-augmented generation does not ground in its context trades speed against accuracy: surface checks miss paraphrased fabrication, sampling-based methods cost extra generations. Hidden-state probes sit between the two, but every existing one reads the generating model's own activations, so a change of generator invalidates the detector and a closed-weight generator is out of reach. This paper removes that coupling. The Grounding Probe is logistic regression over the mean-pooled middle-layer hidden states of an observer language model that reads the context, question, and response in one forward pass and generates nothing, with the recipe it needs: pool over response tokens, read a middle layer, and control capacity, which closes the train-test AUROC gap from 0.087-0.202 to 0.009-0.013. Asking the observer outright, rather than reading its hidden state, costs at least +0.166 AUROC in every one of four models. Fitted on 15,090 annotated responses it reaches 0.879-0.894 AUROC on RAGTruth test across four observers, and 0.924 AUROC with 0.820 F1@0.5 averaged with a supervised span detector, 0.060 above that detector alone. One probe holds across six generators, and hold-out controls, including one in which no evaluation prompt appears in training, bound the cost of removing a generator at about 0.02 AUROC. Code, probes, and predictions are released.

---


### 145. [SEIS: Self-Evolving Inference Systems](https://arxiv.org/abs/2610.04646)

**<font color=#1a73e8>作者：</font>** Zhen Xu, Jingyu Liu, Zongze Li 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Inference systems determine how fast and how cheaply language models can be served, so making them faster has direct practical value. However, prior work focuses mostly on optimizing certain parts such as kernels or memory within the large system. In this work, we take a holistic approach and apply agentic self-evolution to optimize the whole system end-to-end. Our SEIS (Self-Evolving Inference Systems) autonomously optimizes the entire mini-sglang engine without human intervention through iterative sessions with inherited experiences and code changes. Serving Qwen3-0.6B on H100, the resulting engine reaches 3.27X the throughput of the original mini-sglang implementation and beats SOTA engines like vLLM, TensorRT-LLM, and SGLang in the single-request workload. The correctness of the optimized inference engine by SEIS is tested in terms of numerical difference and downstream accuracy on math and long-context retrieval tasks. The code and session histories show that the speedup comes from redesigning the whole engine and that building on earlier sessions beats independent attempts. These results suggest that agentic self-evolution can optimize a complex system end-to-end. The evaluation also has to evolve with the engine, and letting agents evolve it is a natural next step.

---


### 146. [PermVLA: Factorization Order as a Regularizer for VLA Learning](https://arxiv.org/abs/2610.04659)

**<font color=#1a73e8>作者：</font>** Yanqiao Chen, Yuhan Rui, Dongsheng Hou 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Vision-language-action (VLA) policies commonly learn action chunks through a fixed left-to-right (LTR) factorization, although the same expert trajectory distribution admits many valid chain-rule factorizations. We identify factorization order as an overlooked regularization choice and introduce causally anchored permutation (CAP), which samples action reveal orders with a tunable chronological prefix. Its auxiliary objective trains one shared policy to predict actions from different known subsets of the same expert chunk, while deployment retains deterministic LTR control. We call this conditional-set augmentation: it creates multiple conditional prediction problems from one expert chunk without adding demonstrations. This discourages reliance on the single chronological prefix used by ordinary teacher forcing. Controlled experiments show that CAP consistently outperforms standard LTR training on LIBERO and LIBERO-Plus, with the same advantage appearing in cross-dataset CALVIN evaluation. A diagnostic that measures the expected squared difference between a chunk's joint log likelihood under two reveal orders verifies that CAP training internalizes agreement across reveal orders. These findings position sampled subset-conditioned auxiliary objectives as a general recipe for constructing VLA regularizers, illustrated by an extension to diffusion action generators.

---


### 147. [A Tropical Geometry View of Forgetting: A Per-Unit Projector for Knowledge-Preserving Fine-Tuning](https://arxiv.org/abs/2610.04670)

**<font color=#1a73e8>作者：</font>** Yuyang Zhang, Xiaoyin Chen, Chunlin Ren 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Fine-tuning a language model on new text degrades what it already does. Replay-free projectors such as Adam-NSCL and GPM forbid one shared subspace of a layer's inputs in every row of the update. The tropical geometry of a ReLU layer shows why this is too coarse. In data space, the units' walls are tropical hypersurfaces whose cells are dual to the upper vertices of a zonotope; in weight space, each old token is a hyperplane, and the tokens cut out a polyhedron, the closure of the weights that keep every token on its side. An exact identity joins the two pictures: the squared change of the layer's output under any weight change splits into in-cell, open-to-closed and closed-to-open terms, and the first two live on the tokens each unit fires on. The identity names a gate-aware per-unit projector, and a budget-separation theorem prices exact protection: it costs a unit the rank of its own open tokens, while a shared subspace pays at least the rank of their union in every row. On OPT-1.3b, where 96% of (token, unit) pairs are closed, the projector forgets less than Adam-NSCL at all six matched budgets from 9 to 60 constrained directions per row, the gap widening from $1.1\times$ to $4.3\times$; with 1/5.5 of the directions it halves the forgetting of Adam-NSCL at GPM's energy threshold. On OPT-6.7b, it matches Adam-NSCL's forgetting at matched budget while learning more. As the theory predicts, the open/closed partition is the operative variable: open tokens beat random, sign-blind and anti-gate token sets on 18 of 18 seed-pairs. In pruning repair, every derivative-based local model of the output error at the dense weights is blind to pairs that open: the minimisers of the gate-weighted objective can leave the polyhedron, the objective's closed-form solution is 1.94 nats worse than no repair on OPT-1.3b, and a convex one-sided penalty bounds the escape.

---


### 148. [MASBench: Benchmarking LLM-based Multi-Agent Collaboration under Partial Observability](https://arxiv.org/abs/2610.04672)

**<font color=#1a73e8>作者：</font>** Qizhi Chu, Zekai Yu, Sijie Wen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) have progressively evolved into the core of autonomous agents. Building on this progress, LLM-based multi-agent systems (MAS) coordinate multiple agents into a synergistic team to accomplish complex tasks that exceed the capabilities of individual agents. The effectiveness of such systems depends not only on the agents themselves, but also on how collaboration mechanisms are designed and organized. Note that real-world collaboration is typically partially observable, where each agent can only access partial information about the environment due to physical or privacy-related constraints. However, many existing multi-agent benchmarks assume global observability, and leave limited support for systematically evaluating collaboration mechanisms. To bridge this gap, we introduce MASBench, a multi-agent collaboration benchmark designed under partially observable constraints. It is organized into three progressive task categories: Reasoning, Scheduling, and Game. Through this structure, we progressively evaluate three representative collaboration mechanisms: Protocol, Memory, and Routing. MASBench further provides deterministic evaluation metrics, including performance score, communication cost, and cost effectiveness, to characterize both collaboration outcomes and communication overhead. Experiments across diverse LLM backbones and mechanism configurations offer empirical guidance for effective MAS design. Code is available at: this https URL

---


### 149. [Extracting Persona Subspaces Through Iterative Nullspace Projection For Modulation](https://arxiv.org/abs/2610.04676)

**<font color=#1a73e8>作者：</font>** Ananya Malik, Mai ElSherief  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Large Language Models (LLMs) can adopt distinct personas to tune their semantics, expertise, and perspective to different users and tasks. Precise control over these traits is critical to ensure safety and reliability in model behavior. Existing methods like activation steering and prompt-based persona induction reduce a persona to a single dominant direction, missing the finer, nested traits that emerge only once that dominant signal is factored out. We introduce modulation as a setting where the persona context is already embedded in the content being manipulated, requiring control methods to amplify or suppress a trait already present rather than inject it from scratch. PaSS is an inference-time control paradigm that models personas as multi-dimensional subspaces in a model's latent space without supervised contrastive examples. The persona subspaces are extracted via iterative concept erasure and applied to modulate persona-guided generation without retraining. To extract this subspace, we use Iterative Nullspace Projections (INLP) to linearly and iteratively isolate persona-specific directions. We causally evaluate six personas against diverse tasks like MATH-500, TinyAlpaca, GSM8K, and IFEval, showing that discriminative, iterative subspace extraction captures diverse traits underlying a given persona, enabling stronger and larger modulation than single-direction additive methods, while maintaining content fidelity. We further study individual peeled directions within each subspace to uncover the distinct aspects of persona behavior they encode. Overall, we show that persona subspaces offer a controllable, interpretable, and generalizable framework for modulating LLM behavior without sacrificing task performance.

---


### 150. [Steering Speech-Language Models: Training-Free Task Specialization via Contrastive Activation Addition](https://arxiv.org/abs/2610.04683)

**<font color=#1a73e8>作者：</font>** Séverin Baroudi, Yanis Labrak, Pierfrancesco Melucci 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Activation steering has proven effective for controlling the behavior of Large Language Models (LLMs) at inference time, but its application to SpeechLLMs remains new, and training-free steering approaches for such models are still largely unexplored. We propose a training-free Contrastive Activation Addition (CAA) protocol that derives steering vectors for common speech tasks (e.g. transcription) in SpeechLLMs from a small number of labeled utterances. We showcase that adding these vectors in the representation space, at inference time, enforces better the targeted speech task. We further show that, when combined with prompting, these vectors yield to consistent improvement over prompting alone on most evaluated tasks such as Automatic Speech Recognition (ASR) or Emotion Recognition (ER), and transfer to out-of-domain data. We additionally demonstrate the usefulness of script-normalization directions to enforce the target script of a specific language.

---


> [!TIP]
> 当前位于：**101-150**（第 3/11 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | **101-150** | [151-200](./part-04.md) | [201-250](./part-05.md) | [251-300](./part-06.md) | [301-350](./part-07.md) | [351-400](./part-08.md) | [401-450](./part-09.md) | [451-500](./part-10.md) | [501-505](./part-11.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
