# 🧠 大模型相关研究 | 2026年11月09日

> 本类共 **183** 篇论文：已确认 **172** 篇，待复核 **11** 篇

> 聚焦 LLM / MLLM / Agent / MoE 等大模型研究，并包含使用 LLM 完成网络安全任务的研究；待复核论文合并展示在本章末尾。

> [!TIP]
> 当前位于：**151-183**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-183**

---

### 151. [Benchmarking Large Language Models on Heterogeneous Cognitive and Biomedical Knowledge Graphs: The Role of Graph Grounding in Multi-Hop Reasoning and Hallucination Mitigation](https://arxiv.org/abs/2611.08315)

**<font color=#1a73e8>作者：</font>** Ali Sarabadani, Kheirolah Rahsepar Fard, Tahereh Jeirani  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly used in biomedical and cognitive neuroscience, but their ability to reason reliably over heterogeneous knowledge graphs (KGs) remains unclear. We benchmark five LLMs (GPT-5.1, Gemini 2.0 Pro, Llama 3, Qwen, and BioGPT) across five KGs: DrugBank, NeuroSynth, Cognitive Atlas, Brain Map, and GDPKG. We introduce a multitier query dataset to evaluate reasoning depth and factual accuracy under KG-aware (graph-grounded) and KG-agnostic conditions. Inter-annotator agreement was substantial, with Cohen's kappa of 0.781 (range: 0.753-0.807) and Fleiss' kappa of 0.77. Results show that general-purpose models, particularly GPT-5.1 and Gemini 2.0 Pro, generally outperform domain-specific models on multi-hop and high-level reasoning tasks, although performance declines as query complexity increases. KG grounding reduces hallucination rates across all evaluated models. Contrary to our initial hypothesis, domain-specific models do not consistently outperform general-purpose models on specialized tasks without graph grounding. These findings highlight the value of combining broad language-model capabilities with structured domain knowledge. We provide practical guidance for selecting LLM-KG integration strategies based on task complexity and computational constraints, and discuss hybrid neurosymbolic architectures for personalized medicine, cognitive disorder diagnosis, and explainable AI.

---


### 152. [Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement](https://arxiv.org/abs/2611.08318)

**<font color=#1a73e8>作者：</font>** Wenbo Huang, Jianxin Bi, Shunyu Yang 等 13 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-improving embodied agents are increasingly being developed and compared on robot simulation benchmarks. Several recent works expose the benchmark's success criteria to the learning agent, a practice we call Criteria Exposure (CE). These criteria, originally written to verify policies trained by imitation learning, often demand more than the corresponding language instructions, so a score from such a verifier may not faithfully reflect whether the instructed task was completed, especially for robot-control programs written by an agent. As embodied coding agents report ever higher benchmark scores, a natural question arises: when a coding agent is exposed to the benchmark's criteria, does it generate code that better performs the instructed task, or code that simply overfits to the verification criteria? We conduct controlled experiments with a self-improving agent with and without CE, and find that with CE the agent quickly produces code with a higher success rate under the given criteria, but this advantage disappears when the criteria are changed slightly without departing from the original instructions. More importantly, the skills the agent develops under CE transfer poorly across tasks. We further propose instruction-faithful criteria and show that they better reflect the performance of agent-generated programs.

---


### 153. [ControlAnything: Generative UI and On-Demand Device Integration for Mixed-Reality Hand Interaction by a Coding Agent](https://arxiv.org/abs/2611.08321)

**<font color=#1a73e8>作者：</font>** Bektur Ryskeldiev  
**<font color=#188038>arXiv所属领域：</font>** Human-Computer Interaction

**<font color=#5f6368>摘要：</font>**
> Connecting hand input in mixed reality (MR) to a nearby physical device typically requires an integration written in advance for that device, its transport and the mapping. ControlAnything defers this integration to the moment of use and assigns it to a coding agent. On a Meta Quest 3, the wearer selects an object outlined by SAM 3.1 and states what their hands should control. An agent built on Meta's Muse Spark model then writes a connector program on the wearer's laptop, tests it against the live device through hand-written MIDI, Bluetooth and key-press transports, and returns augmented-reality (AR) controls, a per-frame hand program, or both. These outputs are a form of generative UI, interfaces created by an AI model; here, the agent also generates and tests the code that binds the interface to a physical device. In a single-session technical evaluation with the author as the only wearer, nine of ten requests addressing five targets reached a ready state, and the wearer stopped one. The median time to ready was 32.5 s (range 24.9-57.8 s, excluding speech transcription); sequential model calls accounted for a median of 89.9% of this time, and 91.7% of input tokens came from the prompt cache. The system's evidence of success extends to transport acknowledgements but not to physical effects. These findings point to connector reuse and the observation of effects through the headset's own sensors as next steps for on-demand device integration in MR. A user study with first-time wearers is planned.

---


### 154. [Decision Models as Retrieval Gates Against Injection and Pollution](https://arxiv.org/abs/2611.08325)

**<font color=#1a73e8>作者：</font>** Mahdi Ghadamyari, Reza Habibi  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieved web text can carry instructions aimed at the language model, or synthetic pages written to mislead. We test whether released open-weight decision models, which answer typed questions about a text without generating tokens, can screen retrieved passages against both threats. On a benchmark of 1,000 questions over forum-style web pages with hidden injected instructions, a Kev-4B gate reads each passage's HTML. Attack success, measured automatically, falls from 27.9% with no defence to 13.6% with the published mitigations (sanitisation, normalisation and citation prompting) and to 5.7% with the gate added. The gate takes 76 ms per passage and wrongly flags 4 of 186 benign pages with instructions for human readers. Responsiveness on clean queries stays within a point (85.6% to 86.2%). On a 200-query pollution testbed where two thirds of the candidate pages are fake, filtering the pool before the top ten are chosen keeps fake pages out of the answer (0.5% exposure) and holds accuracy at 83%, against 28% with no filter. Filtering only the top ten leaves the generator too few pages to answer. Large LLMs used as judges rank attacks better (AUROC 0.99 against 0.94) but cost ten times more. Gates catch more attacks when they read the page's HTML than when they read its plain text. Every model is open-weight.

---


### 155. [Cultural Adaptation within Repeated Social Interactions](https://arxiv.org/abs/2611.08334)

**<font color=#1a73e8>作者：</font>** Chen Cecilia Liu, Roi Reichart, Anna Korhonen  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Much of human culture is tacit and is typically learned through situated social interaction. As LLMs are deployed as interactive agents across diverse communities, assessing their cultural competence demands moving beyond existing question-answering approaches, shifting from what they know to how they adapt. In this work, we broaden the scope of cultural adaptation in NLP by investigating whether LLMs can adapt through repeated interactions via a sandbox environment. By reframing cultural adaptation as a continuous process of norm assimilation through social interaction, our work demonstrates that memory mechanisms foster longitudinal learning across repeated interactions, facilitate transfer to different social settings, and enable multilingual norm assimilation across five languages. Together, our findings lay the groundwork for continuous, interaction-driven cultural adaptation in LLMs.

---


### 156. [Enhancing Local and Global Structure in Compressed AI Agent Memory](https://arxiv.org/abs/2611.08341)

**<font color=#1a73e8>作者：</font>** Henry Han  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> AI agents store text as embedding vectors and compress them at scale. A compression is accepted when each item's nearest neighbors survive, but agents also consolidate, delete, and compare memories, tasks that depend on which items lie far apart. We evaluate both ends with two label-free fidelities from our prior work: the local fidelity $L$ at 10 neighbors and the global fidelity $G$ at 30 to 50 percent of the memory. At 96 bytes per passage, rescored binary codes reach an $L$ of 0.97 yet move 10.1 percent of passages to another theme; PCA with 8-bit codes, at an $L$ of 0.77, moves 1.7 percent. Rescoring leaves the stored codes, and thus $G$, unchanged. We prove that across the $G$ band, $1-\nu_k$ is at most 2 to 2.18 times the square root of the near-far rank-violation rate, and that this rate follows the distance noise of the compression (correlation 0.979). Our locality-aware quantization (LAQ) turns the bound into a hinge objective on the codebooks of an OPQ index, keeping its bytes, rotation, and search. To our knowledge, LAQ is the first quantizer whose objective comes from a proven bound on the far end. Reconstruction alone raises $G$ in 0 of 52 held-out runs; the far hinge raises it in all 52. LAQ raises $G$ in all 52 ($p=8.5\times 10^{-4}$ over 13 memory-encoder groups), including the external FinDER memory, has the highest $G$ of seven equal-size quantizers in all 12 Multi-Doc-2025 runs, scales to a million passages, and keeps evidence recall.

---


### 157. [LABBA: LLM-Assisted Behavioral Biometric Authentication](https://arxiv.org/abs/2611.08343)

**<font color=#1a73e8>作者：</font>** Howard Halim, Eyasu Getahun Chekole, Jianying Zhou  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Behavioral biometrics have emerged as a promising complement to traditional physiological biometrics by leveraging dynamic human characteristics. These modalities offer advantages including continuous authentication, inherent liveness detection, and greater resistance to credential theft and other spoofing attacks. However, existing systems remain limited in adaptability, contextual awareness, and semantic reasoning as they primarily rely on similarity metrics, static thresholds, or supervised classifiers. As a result, they often struggle with real-world conditions such as behavioral variability, environmental changes, contextual changes, and adversarial manipulations.
To address these limitations, we systematically integrate LLM-based contextual reasoning into behavioral biometric authentication. LLMs provide capabilities in contextual inference, sequential reasoning, multimodal understanding, and adaptive decision-making. Building on these strengths, we integrate a lightweight LLM-based reasoning module with a novel phone-blowing behavioral biometric technique to develop a context-aware authentication framework. To this end, we first collect blow-acoustic signals from participants and systematically extract spectral and temporal features. These features are aggregated and converted into comparable similarity representations, using either discrete rule-based categories or continuous normalized scores, which are transformed into structured prompts through prompt engineering.
We experimentally evaluate the proposed framework using blow-acoustic data collected from 50 participants under diverse behavioral and contextual conditions. The proposed framework achieves 99.46% and 99.38% authentication accuracy in the rule-based and score-based modes, respectively, outperforming its non-LLM counterpart while maintaining strong robustness under dynamic real-world conditions.

---


### 158. [SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time Markov Chains](https://arxiv.org/abs/2611.08362)

**<font color=#1a73e8>作者：</font>** Siva Rajesh Kasa, Yasong Dai, Sumit Negi 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Masked diffusion language models offer parallel text generation, but independently sampling multiple tokens can disrupt their dependencies and change the output distribution. Exact continuous-time sampling avoids this approximation, yet typically requires one sequential model evaluation per token. We introduce SpecCTMC, a training-free speculative sampler that reduces this sequential bottleneck without a separate draft model. SpecCTMC proposes successive token updates using previously computed model predictions, evaluates their intermediate states in parallel, and applies an exact acceptance-and-correction procedure. We prove that SpecCTMC preserves the joint distribution of event times, generation order, and token values of the underlying continuous-time Markov chain. It therefore introduces neither time-discretization error nor additional factorization error from parallel decoding. Experiments on LLaDA-8B-Instruct and Dream-v0-Instruct-7B across five benchmarks demonstrate 1.73-4.38x fewer sequential model evaluations than direct continuous-time sampling, while preserving the reference sampling distribution. Our code is available at: this https URL

---


### 159. [StrataFlux: Memory-Hierarchy-Native Low-Bit LLM Inference](https://arxiv.org/abs/2611.08363)

**<font color=#1a73e8>作者：</font>** Jake Hyun, Ziyu Zhao, Jae-sun Seo 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Quantization reduces the memory and bandwidth demands of large language model (LLM) inference but can degrade accuracy; offloading higher-precision data can instead stall generation. We introduce StrataFlux, a framework that challenges this tradeoff by recovering accuracy lost to low-bit weight and key-value (KV) cache quantization while retaining quantization's memory and speed advantages. StrataFlux co-designs refinement representation, selection, and delivery to make host RAM and solid-state drives useful sources of additional precision. Its selective precision streaming reduces transfer volume, overlaps delivery with computation, and reuses fetched precision across decoding steps so generation need not wait for every transfer. We evaluate 2-4-bit weights and 2-3-bit KV-cache on dedicated GPUs and unified-memory platforms. For 2-bit Llama-3.1-8B-Instruct weights, StrataFlux reduces WikiText-2 perplexity from 9.46 to 8.40 while maintaining 95.4% of the quantized base's throughput on RTX 5090. With 2-bit weights and KV, StrataFlux raises Qwen3-8B's AIME 2024/2025 accuracy from 11.0% to 47.1% at unchanged GPU memory use. At 128K context, Llama-3.1-8B-Instruct with 3-bit weights and 2-bit KV achieves comparable perplexity and speed to vLLM's 4-bit AWQ weights and 8-bit KV on RTX 5090, using approximately half the GPU memory. These results show that GPU-resident precision need not set the accuracy ceiling, nor offloading-tier latency dictate decoding speed.

---


### 160. [Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter Readout](https://arxiv.org/abs/2611.08376)

**<font color=#1a73e8>作者：</font>** Tushaar Gangavarapu, Gil Tabak, Clemens JS Schaefer  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> Linear attention compresses context into a fixed-size key-value state for linear-time training and constant-memory inference. Gated delta-rule models decay this state and erase its prediction for an incoming key before writing a new value; Gated DeltaNet-2 (GDN-2) generalizes this with channel-wise decay and decoupled, full-rank erase and write gates. However, we show that state updates are far less sensitive to erasure than to writes: key activation and unit normalization concentrate key energy onto a sparse subset of channels, whereas value writes scale all channels, so the erase gate can be parameterized at lower rank. Furthermore, slow-decaying state rows accumulate much larger norms than fast rows, dominating unweighted readout and forcing stronger write-time erasure to suppress interference. Guided by this analysis, we introduce Muir, which fuses all gates into a sensitivity-allocated low-rank projection, re-weights state rows with a matched-filter readout gate, and reinvests the saved parameters in a wider feed-forward network. Because standard chunkwise algorithms become numerically unstable at the large chunk sizes needed to saturate wide matrix units, we design a parallel update for stable, efficient training. Across 166M-1.34B parameters, Muir lowers perplexity by 1.8-2.0% over GDN-2 and 2.5-3.6% over Transformer, raises commonsense accuracy by up to 1.9 points, and improves extractive recall over GDN-2. At 1.34B, Muir outperforms both baselines on multi-hop and multi-needle recall, extrapolates 2,560x from its 4K training length to 10M-token streams without perplexity drift, and maintains near-100% passkey retrieval to 1M tokens with static readout. Muir achieves these gains while matching GDN-2 throughput, reaching its 100B-token validation loss 1.2x faster, and training 2.7x faster than Transformer at 32K.

---


### 161. [FedReason: Large Language Models as Weight-Space Meta-Aggregators for Heterogeneous Federated Learning](https://arxiv.org/abs/2611.08383)

**<font color=#1a73e8>作者：</font>** Ali Mohammadi Ruzbahani, Abbas Yazdinejad, Hadis Karimipour  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Federated learning servers combine client models with a fixed aggregation rule, and each rule in common use is designed for one kind of heterogeneity. We study whether a large language model (LLM) that inspects the client models can choose the rule itself, without any training on the server. In FedReason, the LLM is called every ten rounds. It analyses the weights by running code in a restricted server-side sandbox, sees only the printed results, may score a few candidates on a 500-image proxy set, and submits a short Python aggregation program. The server applies the program until the next call and falls back to FedAvg whenever its output is invalid. Full weight tensors never leave the server. We evaluated FedReason with Claude Opus 5.5 on CIFAR-10 and CIFAR-100 with ResNet-18 under Dirichlet label skew, width-heterogeneous sub-models and Byzantine clients, in 168 runs against 14 baselines. Across 12 paired label-skew runs it beat FedAvg by 1.26 percentage points on average (10 wins), and a control that spends the same per-round proxy budget on choosing among standard rules by 1.08 points. It was the strongest server-side rule on CIFAR-100 but did not beat SCAFFOLD, which changes client training. With three of ten clients malicious, it excluded all sign-flipping clients from the first round and stayed about one point below FLTrust without training a root model. Without proxy feedback, accuracy fell from 73.8% to 38.8% in one seed. A 60-round run cost 0.79 USD in API fees on average.

---


### 162. [The Gold Rush in AI4Math, II: What are signatures of AI-assisted Proofs?](https://arxiv.org/abs/2611.08412)

**<font color=#1a73e8>作者：</font>** Yuanchuan Guo, Jiashun Jin, Zheng Tracy Ke 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> The growing use of AI in mathematics raises a question: can we detect AI involvement in proofs, separately from AI assistance with writing? Historical arXiv papers, recent papers disclosing substantive AI use, and manuscripts released by OpenAI provide a rich empirical basis for studying this question. However, several challenges remain: lack of matched case-control pairs; potential incompleteness of disclosure; and lack of ready-to-use features designed to capture signals of AI involvement in proofs.
To address these challenges, we construct five cohorts comprising 8,281 papers by combining existing manuscripts with those we produced using generative AI. These cohorts span different levels of AI involvement and include matched pairs of papers addressing the same research problems. We then introduce ProofTrace, a framework that represents each paper as a graph of immediate proof support (GIPS) and extracts interpretable features of mathematical organization.
Our study yields three discoveries. First, principal-component projections of our features reveal a qualitative gradient of AI involvement, where AI-reworded papers remain close to human papers, the two AI-generated cohorts depart in broadly shared directions, and papers disclosing substantive AI use occupy intermediate positions which shifts toward AI-generated cohorts over time. Second, we identify recurring signatures of AI-generated proofs, such as fewer externally cited results, greater reliance on intermediate conclusions, and altered graph connectivity; many of these signatures persist under controls for research field, manuscript length, or graph size. Finally, in a separate detection experiment, ProofTrace distinguishes human-written papers from those disclosing substantive AI use. Its performance remains stable under AI rewording, whereas the performance of state-of-the-art text-based detectors declines sharply.

---


### 163. [Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks](https://arxiv.org/abs/2611.08417)

**<font color=#1a73e8>作者：</font>** E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Coding agents are among the most economically consequential deployments of LLMs to date, making reliable evaluation increasingly important. Yet even benchmarks that are carefully validated at release can become stale. As models improve, they can discover valid solutions that existing verifiers reject, while changes to evaluation infrastructure can invalidate assumptions embedded in tasks and tests. We call the resulting accumulation of defects benchmark maintenance debt: a growing gap between benchmark scores and the capabilities they are intended to measure. We introduce a continuous-validation workflow for agentic benchmarks that combines community reports, task artifacts, agent traces, automated oracle checks, and human-gated repairs. We apply this workflow to Terminal-Bench 2.0, a benchmark that underwent extensive human and LM-assisted review and red-teaming before release. Our audit identifies issues in roughly 30% of the benchmark, and we release the resulting repairs as Terminal-Bench 2.1. These repairs change evaluation results: accuracy increased by over 10 percentage points and leaderboard positions move by up to three ranks, even as the overall ranking remains highly correlated (Spearman rho = 0.958).
We evaluate how resource allocation shapes benchmark conclusions. We show that fixed wall-clock can materially change agent performance: For example, extending the time limit closes a 20pp harness gap on GPT 5.4 and shrinks a 30 pp gap on GPT 5.4 mini to 5 pp. Benchmark maintenance is therefore not only about repairing task artifacts: resource budgets are part of the measurement specification and must be validated alongside the tasks themselves.
More broadly, benchmark maintenance debt is not just accumulated implementation bugs: our results show that as models improve, both evaluation assumptions and resource settings may need to be revalidated.

---


### 164. [The Power of Meta Access in the Software of the Future --- Demonstrated on LLM Chat UIs and Chat AI](https://arxiv.org/abs/2611.08428)

**<font color=#1a73e8>作者：</font>** Julian Kunkel, Ali Doosthosseini  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Chat remains the default surface for many large language model (LLM) tasks, even as agentic tools such as OpenCode excel at coding and automation. Yet the model sees the current dialogue but not the workspace around it. We explore meta access---giving the assistant a structured, permissioned view of the interface itself and propose a ladder of levels: feature tutoring; metadata, settings, and preference access; retrieval over summaries and messages, confirmed mutation, and full orchestration. Meta access can turn a chat client from many screens into one entry point for finding, navigating, organising, and operating it, while raising risks around grounding, privacy, prompt injection, and trust. General-purpose agentic harnesses are runtimes; because they can change their own settings, meta access becomes reflexive and needs a separate control-plane boundary. We ground this in the Meta Chat prototype of the Chat AI client. It builds bounded context from, e.g., summaries, settings, and relevant messages; links references to conversations, topics, and personas; supports confirmed, reversible changes; offers a browsable tutorial library; and recommends personas as user-started conversations. By exposing application state in structured form, meta access can extend screen readers from widget descriptions to semantic workspace operations. Meta access thus turns chat from a window onto one conversation into a control layer for the whole workspace, extending chat toward agentic capability without surrendering user control. As assistants become embedded in IDEs, dashboards, office suites, and operating systems, AI-era interfaces should expose a structured, permissioned model of their state and capabilities, ideally by opening their existing metamodels through a debugger-like interface.

---


### 165. [MedGraph: Maintaining Patient State with Graph Memory for Long-Term Medical Dialogue](https://arxiv.org/abs/2611.08433)

**<font color=#1a73e8>作者：</font>** Donghua Zhang, Zizheng Wang, Ze Dong 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> LLM-based medical assistants that follow a patient across visits need a memory that keeps the patient's clinical state correct as it changes. We examine the errors of five memory systems on longitudinal medical dialogue and find three recurring causes: the retrieved evidence gives an outdated state, includes another person's health facts, or lacks a safety fact the answer depends on. We present MedGraph, a graph memory built for these three cases. Construction extracts dated facts from each session, attributes each fact to the person it describes, and links medication, diagnosis, and measurement records into chains that keep earlier states. Retrieval ranks the patient's chains as units, reads each chain at the time the question asks about, and adds the original dialogue text; a patient profile lists every recorded safety fact with every question. On MedMemoryBench, MedGraph has the highest overall accuracy with both a GPT and a Qwen backbone, 10.5 and 10.4 points above the strongest of five baselines, with efficient memory construction and answering in the GPT setting.

---


### 166. [Edge-Assisted Crowdsensing for Explainable Cyclist Safety Perception](https://arxiv.org/abs/2611.08441)

**<font color=#1a73e8>作者：</font>** Hongsen Cao, Chia-Yen Chiang, Mona Jaber 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Cyclist fatality rates remain high despite policy support for active travel, and autonomous vehicles add complexity to mixed traffic. Neither crash statistics nor multi-model detection pipelines scale to continuous monitoring of perceived safety along a route. We present an edge-assisted crowdsensing system: handlebar cameras supply street-level frames, a vision-language model (VLM) turns each frame into structured traffic attributes through a single prompt, and an explainable boosting machine (EBM) combines them with OpenStreetMap road infrastructure and on-bike kinematics to predict a crowdsourced 1-9 safety score. Extraction belongs at the network edge: the fastest self-hosted model needs 2.49 s per frame and scoring takes 0.4 ms on a CPU. On 1,362 annotated frames from two London routes, the EBM regressor reaches 72.2 percent binary accuracy and a mean absolute error of 1.011 under five-fold cross-validation. It is within one accuracy point of black-box ensembles. Its per-feature shape functions give exact attribution: physical lane separation is worth +0.97 rating points, a painted lane +0.70 and a construction site -0.65. Planners can therefore price an infrastructure change in rating points, and the results enter cost-benefit analysis directly. We also report inter-annotator agreement (alpha = 0.4695), an attribute audit, and a sensitivity analysis linking attribute error to accuracy. With re-encoding, a 20 s sampling interval serves 1,000 riders at 54 Mbit/s at a cost of 1.4 accuracy points, making continuous monitoring practical.

---


### 167. [ReproBridge: Building Reproducibility into ML Research Artifacts](https://arxiv.org/abs/2611.08452)

**<font color=#1a73e8>作者：</font>** Yubo Wang, Rui Meng, Jaehyun Nam 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Reproducing machine learning experiments requires reconstructing procedures from information scattered across papers, released code, and supporting artifacts. For coding agents, reproduction success can therefore depend on their ability to fill in missing details, rather than on the released artifacts alone. We ask whether preserving recovered procedures and decisions improves subsequent independent reproduction. We define a standardized artifact design comprising a refined codebase, environment setup, experiment launchers, and a reproduction guide, and introduce ReproBridge, an agent workflow for constructing these refined reproducible artifacts. ReproBridge-Bench provides 1,029 tasks from 387 experiments across 36 papers, anchored by five human-verified reference scores per task. Agents attempt tasks in fresh sessions with raw code or refined artifacts; a separate Auditor checks execution evidence. Across four evaluated models, refined artifacts raise mean reproduction success from 76.4% to 92.6% and reduce downstream API spending by 19.7% on average. The cross-model success-rate spread narrows from 21.6 to 3.9 percentage points, with all four models achieving mean success rates above 90%. Removing any component reduces success in the ablation study, with the largest losses from code and environment removal. These results suggest that preserving execution knowledge helps even models with lower raw-code success reproduce experiments more reliably and at lower API cost.

---


### 168. [Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO](https://arxiv.org/abs/2611.08453)

**<font color=#1a73e8>作者：</font>** Zeyu Leo Liu, Yang Li, Bo Pang 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> On-policy distillation (OPD) trains a student on its own rollouts under a frozen teacher's per-token supervision. Does this dense signal reduce the training FLOPs needed to reach a target accuracy compared with reinforcement learning? We systematically compare vanilla reverse-KL OPD with Group Relative Policy Optimization (GRPO) across task difficulty, student and teacher size, domain, and optimization choices, measuring held-out accuracy against training FLOPs. With an external post-trained teacher, OPD generally loses to GRPO in accuracy per training FLOP at matched settings, even when the teacher is further trained with GRPO, and often suffers response-length inflation. Yet a different teacher changes the picture: when the teacher is the student's own GRPO checkpoint, OPD recovers that checkpoint's accuracy on math with $50\times$ fewer distillation FLOPs than GRPO needs to reach the same accuracy. Following the same teacher setting, we consistently observe this high efficiency with a larger student, on code, and in a second model family. On a single domain, however, the GRPO checkpoint is already the desired model, so distilling it adds to total compute. Across domains, separate GRPO checkpoints hold different capabilities, and no single checkpoint serves every domain. Multi-teacher OPD (DeepSeek-AI, 2026) consolidates per-domain GRPO experts into a single student that matches each expert's accuracy, with the distillation stage costing only 5.2% (on 2 domains) and 8.0% (on 4 domains) of the specialist training FLOPs. Counting specialist training and distillation together, this pipeline reaches joint GRPO's performance on the 2-domain mix with 42.0% fewer total FLOPs.

---


### 169. [Towards interpreting any residual stream direction by scaling activation inversion](https://arxiv.org/abs/2611.08465)

**<font color=#1a73e8>作者：</font>** Celeste De Schamphelaere, Juan J. Vazquez, Ari Spiesberger 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> To interpret a direction in a language model's residual stream, we can look for text that strongly activates it. But when such text is found by scanning a corpus, it is limited to what that corpus contains. We develop Maximally-Activating Example Metamodels (MAEMs), language models which map residual stream directions from a subject model to text exemplars that strongly activate those directions. Our objective is to maximise the cosine similarity of a supplied residual stream direction with the activations of the text generated by the MAEM. This label-free RL objective helps to scale MAEMs on diverse sources of residual stream directions. Empirically, we find the resultant metamodel produces informative exemplars: a Qwen3.6-27B MAEM inverts held-out activations better than corpus search or a natural-language autoencoder (NLA), beats corpus search (at 10M tokens) on a majority of held-out languages/domains, and activates 89% of held-out SAE features. It also identifies concepts behind steering vectors about as well as NLAs, recovers the payloads of LoRA backdoors more often than corpus search, and can even verbalise some model workspace inner monologue. Unlike explanations produced by other metamodels (e.g. NLAs), MAEM exemplars can be verified with a forward pass on the subject model, making the MAEM objective a grounded alternative for scaling the training of metamodels.

---


### 170. [XStack: A Benchmark for ML Repo Migration](https://arxiv.org/abs/2611.08472)

**<font color=#1a73e8>作者：</font>** Linrong Cai, Taiming Lu, Haozhe Chen 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> ML code should run where researchers choose, not where it was first written. Today, machine learning code mainly lives in two ecosystems, PyTorch on NVIDIA GPUs and JAX on Google TPUs. Migrating repositories between them means building and testing across frameworks and hardware. This migration is (1) a practical need, since it unlocks different hardware for researchers, and (2) a natural benchmark: it involves different frameworks and hardware, covers whole repositories, and is long-horizon and challenging. We introduce XStack, a benchmark that evaluates agents on migrating ML repositories between these two ecosystems. Each agent receives a PyTorch repository and a clean TPU machine and must deliver a JAX repository. Its output passes if it meets our grading criteria, based on the source repository's published result, authenticated and calibrated by us. Migration by agents remains unreliable: Claude Opus 5 passes 75%, GPT-5.6-sol 45%, and every other agent at most 40%. XStack is a step toward freeing ML code from its ecosystem. We release XStack to make progress toward reliable migration across frameworks and hardware measurable.

---


### 171. [SwarmEvolve: Latent Agent Swarms for Evolutionary Discovery and Optimization](https://arxiv.org/abs/2611.08483)

**<font color=#1a73e8>作者：</font>** Qile Jiang, George Em Karniadakis  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> LLM-guided evolutionary search uses AI agents to improve programs for mathematical and computational problems by iteratively refining solutions and combining high-scoring methods. However, the process is often slow because the LLM generates a long textual chain of thought for each round and must repeat this generation many times to maintain population diversity. We present SwarmEvolve, a framework in which hundreds of low-cost agents per round work in swarms, reason in latent space without decoding to text, and share information by passing KV caches. Each swarm studies the problem from a different angle. A novelty filter keeps the most distinct agent ideas by directly measuring the distances between the agents' hidden state vectors. Crossover of ideas happens naturally in latent space, as a summarizer agent receives the combined KV caches of all swarm members. On 21 problems in mathematical discovery and scientific computing, SwarmEvolve gets the highest average score and needs a median of only 3 to 8 minutes to reach the best scores that other state-of-the-art frameworks reach in 60 minutes. On several problems, SwarmEvolve with Qwen3 8B improves on the solutions that AlphaEvolve first found with frontier LLMs. Our work shows that agent swarms that communicate in latent space offer a fast, low-cost approach to program search for scientific problems.

---


### 172. [Do You Miss the Nights We Spent Crafting Figures? Rethinking Teaser and Framework Figures in the Age of Generative AI](https://arxiv.org/abs/2611.08486)

**<font color=#1a73e8>作者：</font>** Xiaoqi Zhao, Youwei Pang, Kailai Zhou  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Scientific figures give research ideas a visual form through choices of abstraction, composition, and emphasis. Generative AI offers new ways to realize these choices, raising questions about explanatory clarity and purposeful visual expression. We examine these questions through a visual retrospective of 371 motivation and framework figures from 200 papers. The corpus comprises a quota-based main sample of 160 papers spanning four temporal periods and a separate purposive style-contrast sample of 40 papers. A single multimodal judge evaluates six dimensions of communication and design, with three repeated judgments per figure. We attempt source-constrained revisions of all 371 figures, of which 369 pass the recorded fidelity checks. Original-figure ratings show no uniform decline across periods. Revisions increase mean clarity ratings by 0.428 points and decrease aesthetic coherence ratings by 0.111 points on a five-point scale. Gains in the six-dimension average are larger for main-sample motivation figures than for frameworks. Case analyses show that added explanation can clarify comparisons while leaving typographic hierarchy and visual economy unresolved. These model-based findings support researcher-led design, with AI assisting exploration and authors retaining responsibility for explanatory purpose, composition, and scientific relationships. The accompanying atlas and evaluation records are available at this https URL.

---


## ⚠️ 待复核论文

> 以下论文保留内部待复核标记，并统一放在大模型章节末尾。

### 173. [Shaping & Monitoring Models through their Internal Representations](https://arxiv.org/abs/2611.07071)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Thomas Fel, Matthew Kowal, Matt Feiszli 等 26 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We propose Mechanistic Shaping, a unified framework for shaping models through their internal representations. Mechanistic Shaping is applied during training so that models follow specifications (rules) about which concepts they express, measured via their outputs or internal representations (e.g., no harmful content), and also which concepts they rely on, i.e., what they use to make their decisions (e.g., not a candidate's gender when screening a résumé). Across multiple domains (vision, medical imaging, language), scales (up to 32B parameters), and training paradigms (classification, SFT, DPO, GRPO), we find that Mechanistic Shaping substantially reduces targeted behaviors while preserving task performance. Since training against a representation can also modify it, we ask whether shaped concepts remain monitorable, a question that depends on the class of monitors considered. We therefore introduce a hierarchy of such classes, which separates a concept that escapes one probe from a concept that is truly gone. We characterize three geometric mechanisms of circumvention: the concept can drift away from the monitor, be erased from the layer, or persist in higher-order statistics as a nonlinear encoding, which we explain through a product-code construction. Although other mechanisms may arise in different settings or at larger scales, these three account for all of our observations, and each can be detected by a matching monitor. In practice, we find that shaped concepts largely remain monitorable: refitted linear probes recover the concept in most settings, and the original probe remains reliable whenever gradients do not flow through it. Taken together, these results point to the potential of using interpretability as a tool for training, and call for a correspondingly rigorous science of interpretability-based training.

---


### 174. [HyFlash: A Prefix-Memory Prior for On-Device Speculative Decoding](https://arxiv.org/abs/2611.07263)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Jongwoo Ko, Pashmina Cameron  
**<font color=#188038>arXiv所属领域：</font>** Computation and Language

**<font color=#5f6368>摘要：</font>**
> Parallel block drafting accelerates speculative decoding by predicting multiple future positions in a single backbone pass, but on-device deployment constrains both drafter capacity and context storage. Under tight memory budgets, drafters must model long-range dependencies and fine-grained draft-position interactions without the growing KV-cache overhead of full-context attention. We propose HyFlash, a compact parallel drafter that introduces a prefix-memory prior to separate long-range context modeling from fine-grained draft-position interactions with limited capacity. Local attention captures recent context and draft-position interactions, while recurrent memory compresses historical target features into fixed-size states. This inductive bias enables effective local and long-range modeling with bounded draft-side memory. Experiments show that HyFlash achieves higher acceptance than full-context attention with substantially less KV storage and with larger gains for shallow drafters and long contexts.

---


### 175. [IMUDINO: Self-distilled Foundation Model for Inertial Sensing](https://arxiv.org/abs/2611.07437)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Zhoutong Ye, Chengwen Zhang, Zixuan Wang 等 12 位作者  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> We present IMUDINO, the first foundation model (FM) for inertial sensing to achieve competitive performance across diverse sensing tasks including human activity recognition (HAR), health, motion capture, and odometry. Prior inertial FMs often focus on one subfield of inertial sensing and sometimes underperform state-of-the-art supervised methods (e.g., in HAR), making their scope considerably narrower than FMs for vision and natural language. Moreover, they often require fixed input length and sampling rate, and generalize poorly to unseen sensor locations. To build a general-purpose foundation model for inertial sensing, we adapt the DINO self-supervised learning (SSL) paradigm to inertial data through a set of semantics-preserving motion transformations that simulate variations in motion pattern and sensor setup. For model architecture, we use a plain transformer encoder with frequency-aware positional encoding that natively supports varying input length and sampling rate. This simple setup proved remarkably effective for learning global and dense features generalizable across users, sensor setups, tasks, and, in the case of robot odometry, embodiments. We hope IMUDINO can serve as a backbone for inertial sensing and kickstart the development of general-purpose inertial FMs.

---


### 176. [Generator-Aligned Reward Modeling with Target-Aware Bounded Optimization for Visual Generation](https://arxiv.org/abs/2611.07648)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Ziqiao Weng, Yuanzhi Liang, Haibing Huang 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Post-training aims to enhance desired attributes in visual generative models while preserving their general generation capabilities. Reward-guided post-training faces two challenges: real training data may mismatch the generator's output distribution, and attribute supervision may be confounded by unrelated content. Unbounded reward maximization can also cause overoptimization and degrade generation quality. We propose a framework combining Generator-Aligned Reward Modeling (GARM) and Target-Aware Bounded Optimization (TABO). GARM mitigates distribution mismatch through generator-support matching and reduces content confounding using content-matched real contrasts, yielding generator-relevant, attribute-focused reward supervision. TABO maps the learned reward to a smooth, upper-bounded function calibrated from real target-positive examples. This transformation is independent of the optimization algorithm and supports both direct reward-gradient and policy-based optimization. We further introduce Target-Aware GRPO (TA-GRPO), an adaptation of Flow-GRPO that combines fixed stage-wise advantage scaling, a generator-to-target curriculum, and timestep-balanced credit assignment for flow-based video optimization. Experiments show that GARM improves target-attribute expression while maintaining competitive generation quality. TABO better balances attribute enhancement and visual quality than unconstrained reward maximization, while TA-GRPO improves target enhancement over vanilla Flow-GRPO and reduces unintended attribute leakage on neutral prompts. These results highlight the importance of generator-aligned reward supervision and controlled, data-calibrated optimization for targeted visual generation.

---


### 177. [Pediatric ECG foundation model via adult-to-pediatric fine-tuning: downstream tasks and clinical evaluation](https://arxiv.org/abs/2611.07717)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yu Cao, Haiyan Xu, Xiaohan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Pediatric electrocardiogram (ECG) interpretation is complicated by age-dependent electrophysiological changes that limit direct transfer of adult AI models. We asked whether an adult ECG foundation model could be adapted to pediatric ECGs. Using 339,563 12-lead ECGs from 238,189 children, we compared direct application, pediatric fine-tuning, and training from scratch under an identical architecture. Direct transfer was poor (mean AUC 0.8256). Fine-tuning reached 0.9695, above de novo training (0.9661), and attained 0.9079 using only 1% of training data. On 10,999 external ECGs, fine-tuning achieved a mean AUC of 0.9385 across 30 labels. It generalized to age regression (MAE 1.12 years) and congenital heart disease classification (AUC 0.9562). Across 17 clinicians and 100 cases, diagnostic accuracy rose from 56.8% to 65.4% (p < 0.001) and did not decline when AI erred. Adult ECG foundation models require pediatric adaptation; fine-tuning offers a data-efficient route to scalable pediatric ECG AI.

---


### 178. [InnerLogic-Surg: An Open Surgical Foundation Model via Continual Pretraining](https://arxiv.org/abs/2611.07883)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kun Yuan, Hao Ding, Yiqing Shen 等 8 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Vision foundation models are the backbone of modern surgical image analysis, yet most surgical systems still rely on encoders pretrained on natural images or on specialist models trained from scratch on comparatively small datasets. Pretraining encoders on large amounts of surgery-specific data has the potential to generally enhance the performance of surgical image analysis methods simply by providing stronger backbones. Here we present InnerLogic-Surg, an open family of surgical vision encoders (21M--300M parameters) obtained by continually pretraining a transformer-based image encoder on millions of surgical images curated from 11,965 internet-sourced surgical videos spanning ~2,900 hours and more than fifteen procedure types. Our training recipe inherits DINOv3's pretraining stage to preserve representation ability after surgical adaptation, and additionally applies a learned feature-upsampling module for high-resolution dense prediction at low token cost. Across a benchmark covering workflow, instrument and anatomy recognition, segmentation, detection, and monocular depth, under the same architecture, the largest InnerLogic-Surg model achieves the best linear-probe performance in all 20 surgical tasks. We demonstrate that surgical continual pretraining yields transferable representations that generalize across procedures, anatomical regions, and task types, showing our surgical image encoders as a promising and scalable alternative to the procedure-specific representation learning approaches that have traditionally dominated surgical computer vision.

---


### 179. [When GeoFMs Meet VHR: Benchmarking Foundation Models on Very High Resolution Earth Observation Imagery](https://arxiv.org/abs/2611.08003)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Kshitij Raj Sharma, Pierre Adorni, Minh-Tan Pham 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Geospatial foundation models are a widely adopted starting point for remote sensing tasks. Most are pretrained on Sentinel-1/2 and Landsat imagery at a ground sampling distance (GSD) of 10m or coarser. Many applications instead rely on very high resolution (VHR) imagery, where individual buildings, roads, and amenities are resolved. We study which pretraining regimes transfer well to this scale. We introduce VHR-Bench, a benchmark suite of ten datasets at 1.5m GSD or finer spanning five task families, eight application domains, and both satellite and aerial platforms. We evaluate twelve encoders in three pretraining tiers with frozen backbones at two training-data fractions. We find that both pretraining on large natural-image collections and VHR-specific pretraining transfer effectively to VHR tasks, with complementary strengths. SkySense leads when labels are scarce; at the full label fraction the web-pretrained DINOv3 ViT-L edges ahead, with the two close together there. Encoders pretrained only on Sentinel-scale imagery transfer least well under RGB input. Guided by these complementary results, we continue the self-supervised pretraining of DINOv3 ViT-L on 1.02 million held-out VHR tiles and evaluate the resulting encoder without changing the downstream protocol. The continued model gives a clear improvement over the released backbone when labels are scarce and a modest one at the full fraction, at no increase in inference parameters or compute. These findings support a generalize-then-specialize strategy: already strong, broad natural-image pretraining can be further improved by a short VHR continuation stage while preserving its general visual features.

---


### 180. [A Generative Foundation Model for Multimodal Tokamak Tasks](https://arxiv.org/abs/2611.08153)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yingshuai Ji, Haodong Feng, Guohong Deng 等 5 位作者  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Tokamak experiments record diverse measurements, including waveforms, profiles, fields, and scalars, which are used to reconstruct the plasma, forecast its evolution, recover associated control signals, and estimate disruption risk. Most models are built separately for one task and a fixed set of inputs and outputs, and each relies on a prescribed subset of diagnostics rather than structuring the full multimodal observation set to extract global, cross-signal information about the discharge. These limitations motivate a reusable foundation model that adapts to each task's input-output schema and models heterogeneous target signals jointly, rather than retraining a separate model for every configuration. In this work, we extend the TokaMark benchmark with two groups of tasks for actuator action inversion and disruption prediction, yielding 20 MAST tasks in six groups with explicit schemas and evaluation protocols. Then, we introduce GenToka, a generative tokamak foundation model that jointly generates schema-selected targets through a shared conditional diffusion Transformer, with signal-specific codecs preserving native time series, profiles, fields, and scalars; foundation pretraining and task-specific adaptation transfer cross-signal structure across all six groups. Evaluation on MAST measurements shows that GenToka reduces macro-average normalized root mean squared error relative to TokaMind by 4.7% on Groups 1-4 and by 17.7% on Group 5, and improves macro-average window-level F1 on Group 6 by 8.4% at a common validation-selected threshold. GenToka provides a reusable, generative, and multimodal pathway for experimental tokamaks, linking plasma-state reconstruction, actuator inference, and disruption warning from shared measurements to support more integrated, data-driven fusion plasma prediction and control research.

---


### 181. [Do sEMG Foundation Models Improve Cross-Subject Generalisation?](https://arxiv.org/abs/2611.08199)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** William Raftery, Dario Farina  
**<font color=#188038>arXiv所属领域：</font>** Machine Learning

**<font color=#5f6368>摘要：</font>**
> sEMG Foundation Models aim to learn general purpose representations over diverse subjects and recording conditions that boost performance on a variety of downstream tasks. However, existing evaluations make it difficult to discern whether pretraining alone is sufficient to combat the cross-subject overfitting which makes machine learning on sEMG so challenging. We conduct a systematic evaluation of three sEMG foundation models across three gesture classification datasets under both intra-session and inter-subject splits, using three fine-tuning strategies designed to isolate the contribution of pretraining. We find that pretraining boosts performance when train and test samples are drawn from the same recording session, but this benefit largely disappears under inter-subject evaluation. In low subject count datasets, pretraining provides little to no benefit and classical ML baselines match or exceed foundation model performance.

---


### 182. [StepBack: Step-Level Error-Localized Resampling for Efficient Test-Time Reasoning](https://arxiv.org/abs/2611.08403)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** Yang Ouyang, Jung-Eun Kim  
**<font color=#188038>arXiv所属领域：</font>** Artificial Intelligence

**<font color=#5f6368>摘要：</font>**
> Self-consistency (SC) is a widely used decoding strategy for improving chain-of-thought reasoning, but it requires sampling many complete reasoning trajectories with a preset budget. Its efficient variants reduce the cost mainly by stopping full-trajectory sampling early or distributing the number of samples across questions. In this paper, we propose StepBack, a step-level error-localized resampling method for efficient test-time reasoning. Given a small set of draft trajectories, StepBack localizes likely first error positions using lightweight signals and then resamples the detected error step and its suffix, followed by majority answer voting. Empirically, StepBack matches the accuracy of SC on average across seven mathematical reasoning and multi-hop QA benchmarks, while reducing token usage by up to 41.26%. In addition, by nature, StepBack can be combined with adaptive inference methods such as Adaptive Consistency, further improving their inference-time efficiency.

---


### 183. [Where and Why is Grounded Reasoning Useful?](https://arxiv.org/abs/2611.08485)

> ⚠️ **待复核**：规则检测到弱相关信号，暂并入大模型章节。

**<font color=#1a73e8>作者：</font>** David Yan, Le Xue, Forrest Huang 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Computer Vision and Pattern Recognition

**<font color=#5f6368>摘要：</font>**
> Grounded reasoning, where a model outputs text coordinates of relevant locations in chain-of-thought reasoning, is a common strategy for solving complex visual reasoning problems. However, the benefits and limitations of grounded reasoning are understudied. We study where and why grounded reasoning is most useful. To do so, we introduce a chain-of-thought analysis method to measure how much a model uses its outputted grounding in its thinking trace and perform a detailed ablation study of a grounded reasoning training recipe. We find that grounded reasoning improves counting but shows no significant gain over baselines without coordinate grounding across a wide range of spatial reasoning and perception benchmarks. Using several synthetic tasks, we show that grounded reasoning is most useful when a task requires undescribable references, which are visual concepts that are difficult to describe in language. However, we observe that many existing visual reasoning benchmarks are solvable with only describable text references. To close this gap, we introduce BrickVision, a new benchmark that requires undescribable visual references to solve.

---


> [!TIP]
> 当前位于：**151-183**（第 4/4 组）
> - [返回当日日报目录](../index.md)
> - 分组跳转：[1-50](./part-01.md) | [51-100](./part-02.md) | [101-150](./part-03.md) | **151-183**

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
