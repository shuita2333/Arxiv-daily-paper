# 🔐 大模型安全相关研究 | 2026年05月06日

> 本类共 **17** 篇论文

> 聚焦大模型安全、对齐、可信与防护方向。

> [!TIP]
> - [返回当日日报目录](../index.md)

---

### 1. [E-MIA: Exam-Style Black-Box Membership Inference Attacks against RAG Systems](https://arxiv.org/abs/2605.00955)

**<font color=#1a73e8>作者：</font>** Zelin Guan, Shengda Zhuo, Zeyan Li 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-Augmented Generation (RAG) equips large language models (LLMs) with external evidence by retrieving documents at inference time, but it also turns the retrieval corpusinto a sensitive asset. Under a black-box setting, an adversary given a candidate document can infer whether it has been ingested into the RAG knowledge base (i.e., document-level membership inference) solely from query response interactions, thereby leaking corpus coverage and the existence of sensitive topics. Existing RAG MIA methods either rely on soft signals such as semantic similarity, which often yield overlapping member/non-member score distributions and unstable thresholds, or employ explicit confirmation probes whose intent is conspicuous and thus prone to refusal and detection. We propose E-MIA, which converts verifiable hard evidence in the target document (e.g., fine-grained details, proper nouns/technical terms, definitional statements, metadata cues, and causal/constraint relations) into an exam with four objectively gradable question types (FB/SC/MC/T/F), and uses the aggregated exam score across multiple evidence targeted questions as the membership signal. Experiments across multiple datasets and diverse RAG configurations demonstrate that E-MIA improves member/non-member separability in stringent settings while preserving natural, stealthy queries, and we further analyze the impact of question composition and exam length on attack effectiveness.

---


### 2. [SRTJ: Self-Evolving Rule-Driven Training-Free LLM Jailbreaking](https://arxiv.org/abs/2605.00974)

**<font color=#1a73e8>作者：</font>** Jindong Li, Ying Liu, Yali Fu 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> LLMs are increasingly equipped with safety alignment mechanisms, yet recent studies demonstrate that they remain vulnerable to jailbreaking attacks that elicit harmful behaviors without explicit policy violations. While a growing body of work has explored automated jailbreak strategies, existing methods face several fundamental challenges, including the lack of systematic utilization of both successful and failed attack experiences, as well as the absence of principled mechanisms for composing and selecting reusable attack rules under diverse constraints. As a result, existing methods struggle to accumulate transferable knowledge over time and to reliably adapt attack strategies across different targets and evolving safety mechanisms. To address these issues, we propose a Self-Evolving Rule-Driven Training-Free Jailbreak (SRTJ) framework that systematically discovers, composes, and refines attack strategies through interaction and feedback, without updating model parameters. Specifically, SRTJ couples experience-driven attack generation with answer set programming (ASP)-based rule selection and constraint-aware composition, where iterative verifier feedback is leveraged to jointly refine successful strategies and analyze failure patterns. The resulting rule memory evolves in a hierarchical multi-level manner, explicitly organizing distilled attack knowledge into long-term, middle-term, and short-term rules, thereby capturing both stable transferable strategies and transient adaptive behaviors to effectively balance exploration and exploitation across attack attempts. Extensive experiments on mainstream jailbreak benchmark (HarmBench) demonstrate that SRTJ achieves strong and stable attack performance across different target LLMs, while exhibiting improved robustness and generalization compared to existing jailbreak methods. The code is available at this https URL.

---


### 3. [LLM Ghostbusters: Surgical Hallucination Suppression via Adaptive Unlearning](https://arxiv.org/abs/2605.01047)

**<font color=#1a73e8>作者：</font>** Joseph Spracklen, Pedram Aghazadeh, Farinaz Koushanfar 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Hallucinations, outputs that sound plausible but are factually incorrect, remain an open challenge for deployed LLMs. In code generation, models frequently hallucinate non-existent software packages, recommending imports and installation commands for fictional libraries. This creates a critical supply-chain vulnerability: an attacker can proactively register such packages on public registries with malicious payloads that are subsequently installed and executed by developers or autonomous agents, a class of package confusion attack known as slopsquatting. Once a model is deployed, mitigating this failure mode is difficult: full retraining is costly, and existing approaches either cause severe degradation of model utility or rely on a pre-specified forget-set, an assumption that does not apply to the unbounded space of hallucinations. To address this problem, we present Adaptive Unlearning (AU), a post-deployment framework that surgically suppresses hallucinations while preserving general model utility. AU introduces a hybrid token-level objective that simultaneously reinforces valid outputs and suppresses hallucinated ones. Combined with an adaptive discovery loop that continuously surfaces new hallucination-inducing contexts without human supervision, AU enables generalization to unseen prompts and hallucinations. We demonstrate that AU reduces package hallucination rates by 81%, corresponding to a substantial reduction in slopsquatting attack surface, while maintaining performance on standard coding benchmarks. Our analysis shows that distributional changes are concentrated on package-related generations, leaving general coding behavior largely unaffected and confirming that AU's effect is isolated to the targeted distribution. AU operates entirely on model-generated data, requires no human annotation, and generalizes across domains.

---


### 4. [When Embedding-Based Defenses Fail: Rethinking Safety in LLM-Based Multi-Agent Systems](https://arxiv.org/abs/2605.01133)

**<font color=#1a73e8>作者：</font>** Lingxi Zhang, Guangtao Zheng, Hanjie Chen  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language model (LLM)-powered multi-agent systems (MAS) enable agents to communicate and share information, achieving strong performance on complex tasks. However, this communication also creates an attack surface where malicious agents can propagate misinformation and manipulate group decisions, undermining MAS safety. Existing embedding-based defenses aim to detect and prune suspicious agents, but their effectiveness depends on a clear separation between the text embeddings of malicious and benign messages. Attackers can circumvent such defenses by crafting messages whose embeddings lie close to benign ones. We analyze this failure mode theoretically and validate it empirically with three attacks, Slow Drift, Benign Wrapper, and Chaos Seeding. Our analysis further reveals a fundamental limitation of embedding-based defenses: because they rely solely on the text embeddings, they ignore token-level confidence signals such as logits, which can remain informative when embeddings are not distinguishable under attack. We propose using confidence scores to prune or down-weight messages during MAS communication. Experiments show improved robustness across models, datasets, and communication topologies. Moreover, we find that the effectiveness of confidence signals decays over communication rounds, highlighting the importance of early intervention. This insights can inform and inspire future work on MAS attacks and defenses.

---


### 5. [VisInject: Disruption != Injection -- A Dual-Dimension Evaluation of Universal Adversarial Attacks on Vision-Language Models](https://arxiv.org/abs/2605.01449)

**<font color=#1a73e8>作者：</font>** Pang Liu, Yingjie Lao  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Universal adversarial attacks on aligned multimodal large language models are increasingly reported with attack success rates in the 60-80% range, suggesting the visual modality is highly vulnerable to imperceptible perturbations as a prompt-injection channel. We argue that this number conflates two distinct events: (i) the model's output was perturbed (Influence), and (ii) the attacker's chosen target concept was actually emitted (Precise Injection). We compose two existing techniques -- Universal Adversarial Attack and AnyAttack -- under an $L_{inf}$ budget of 16/255, and we add a dual-axis evaluation: a deterministic Ratcliff-Obershelp drift score for Influence (programmatic baseline) plus a 4-tier ordinal categorical none/weak/partial/confirmed for Precise Injection. The judge is DeepSeek-V4-Pro in thinking mode, calibrated against Claude Opus 4.7 with Cohen's $\kappa$ = 0.77 on the injection axis (substantial agreement); the entire 4475-entry SHA-256 input cache ships with the dataset so reviewers can re-derive paper numbers bit-exact without an API key. Across 6615 pairs over four open VLMs, seven attack prompts, and seven test images, the two axes diverge by roughly 90$\times$: 66.4% of pairs are programmatically disturbed (LLM-judged 46.6% at the substantial-or-complete tier), but only 0.756% (50/6615) reach any non-none injection tier and only 0.030% (2/6615) verbatim. The few injections that do land cluster on screenshot- or document-style carriers whose semantics already invite text transcription. BLIP-2 shows \emph{zero detectable drift} at $L_{inf}$ = 16/255 across all 2205 pairs even when used as a Stage-1 surrogate. We release the full dataset -- 21 universal images, 147 adversarial photos, 6,615 response pairs, the v3 dual-axis judge results, and the cache at this http URL.

---


### 6. [LocalAlign: Enabling Generalizable Prompt Injection Defense via Generation of Near-Target Adversarial Examples for Alignment Training](https://arxiv.org/abs/2605.01462)

**<font color=#1a73e8>作者：</font>** Yuyang Gong, Zihao Wang, Jiawei Liu 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models are increasingly embedded into systems that interact with user data, retrieved web content, and external tools, creating a new attack surface: prompt injection, where malicious commands embedded in untrusted data override the trusted command and induce unintended behavior. Existing defenses mainly rely on fine-tuning the model to preserve an explicit boundary between trusted commands and the untrusted data portion, so that the model learns to prioritize the trusted field and ignore malicious commands in data. However, we observe that while these defenses can block obviously malicious responses caused by injected commands, they generalize poorly to real-world scenarios where the model's response to the injected command is much nearer to the correct response. This is because existing methods typically train against only a fixed set of hand-crafted attack targets, which yields a loose boundary around the correct response and leaves it easier to bypass.
To address this challenge, we propose LocalAlign, a more generalizable prompt injection defense inspired by adversarial training. LocalAlign automatically and efficiently generates adversarial examples in which the command embedded in the data portion induces a response that stays near to the correct response while still being wrong. We generate such near-but-wrong adversarial examples using prompting and a single inference step. This design enforces a tighter robustness boundary around the correct response: even small response shifts induced by commands in untrusted data are explicitly penalized. Moreover, the resulting adversarial examples can vary substantially in quality across samples. To address this issue, we further introduce a margin-aware alignment algorithm that quantifies each sample's distance to the correct response and assigns larger training weight to nearer ones.

---


### 7. [AgenticVM: Agentic AI for Adaptive Software Vulnerability Management](https://arxiv.org/abs/2605.01739)

**<font color=#1a73e8>作者：</font>** Asrul Arifin, Hussain Ahmad, Yiyao Zhang 等 4 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> As software systems grow in scale and complexity, vulnerability management is increasingly strained by high alert volumes, fragmented toolchains, and manual triage processes. We introduce AgenticVM, a multi-agent framework that integrates large language models with security tools to automate vulnerability detection, assessment, prioritization, and reporting. AgenticVM combines rule-based processing, a BERT-based CVSS prediction module, and specialised LLM-driven agents, leveraging data from sources such as the National Vulnerability Database and the European Union Vulnerability Database. Across multiple evaluation scenarios, AgenticVM reduces raw scanner outputs into compact, actionable queues, achieving up to 98% alert reduction (e.g., from 3,983 findings to 82 high-priority items), while predicting missing CVSS attributes with 89.3% accuracy. These results demonstrate improved prioritisation efficiency and reduced analyst workload without compromising risk visibility. Beyond performance, the framework provides practical design insights into agent decomposition, tool-LLM integration, and human-in-the-loop governance for real-world deployment.

---


### 8. [Architectural Obsolescence of Unhardened Agentic-AI Runtimes](https://arxiv.org/abs/2605.01740)

**<font color=#1a73e8>作者：</font>** Alfredo Metere  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> An agentic-AI runtime issues tool calls, sends messages, and actuates devices on behalf of an LLM. Catching the four ways an action can diverge from its audit record -- F1 gate-bypass, F2 audit-forgery, silent host failure, F4 wrong-target, -- is a load-bearing safety property of any such runtime. We show that upstream OpenClaw, the most engineered single-user agentic-AI gateway in public release, catches none of them: recall is 0.000 on every cell of every confusion matrix, on a 1600-sample template baseline through OpenClaw's actual production command-line interface (CLI) and on a ten-LLM cross-model generalisation run. Detecting F1--F4 requires seven specific runtime structures absent from OpenClaw's source tree: a biconditional checker, a hash-chained audit log, an extension admission gate, a two-layer egress guard, a Bell-LaPadula classification policy, a module-signing trust root, and a bootstrap seal. enclawed-oss -- an MIT-licensed drop-in fork that ships all seven -- reaches $P = R = F_1 =$ accuracy $= 1.000$ on the same input. The gap is structural, not parametric: a six-line append-only widening of enclawed-oss's data-loss-prevention (DLP) regex catalog raises per-channel F3 detection by 14.6\% net at unchanged precision; the same edit on OpenClaw has nowhere to land. The harness deliberately exercises real Discord and Telegram channels -- plugin categories the first enclawed release deleted as unsafe -- to show F1--F4 detection extends to those previously-unsafe extensions. With architectural superiority for security and feature parity for extensions, we argue that unhardened agentic-AI runtimes are architecturally obsolete: a strictly better alternative exists, is adoptable today, and the gap requires re-architecture rather than configuration. We invite reviewers to apply the harness to any candidate runtime.

---


### 9. [Needle-in-RAG: Prompt-Conditioned Character-Level Traceback of Poisoned Spans in Retrieved Evidence](https://arxiv.org/abs/2605.01782)

**<font color=#1a73e8>作者：</font>** Huining Cui, Wei Liu  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Retrieval-augmented generation (RAG) improves factual grounding by conditioning large language models on retrieved evidence, but it also opens a data-layer attack surface: poisoned corpus entries can steer outputs without changing model parameters. Existing defenses and traceback methods are largely passage-level, which is too coarse for modern attacks whose effective payload may be a short fabricated claim, trigger phrase, or hidden instruction embedded inside an otherwise benign chunk. We study black-box character-level poison traceback in RAG and present RAGCharacter, a two-pass forensic framework that localizes the responsible retrieved span for a concrete misgeneration event. Pass-0 runs standard RAG while logging a prompt-anchored execution trace. Pass-1 re-enters a triggered trace and performs event-conditioned traceback over prompt-used evidence via budgeted counterfactual masking and replay, yielding an attribution span for forensic reporting and a causal span under the logged trace. We further introduce an evaluation protocol that measures both event-level chunk traceback and character-level localization fidelity. Across two QA corpora, five poisoning attack families, six target LLMs, and multiple passage- and character-level baselines, RAGCharacter achieves the best overall trade-off within our benchmark between localization accuracy and low over-attribution. These results suggest that prompt-conditioned, black-box character-level traceback can be feasible, moving RAG forensics from document-level suspicion toward finer-grained evidence auditing and potential remediation.

---


### 10. [QASecClaw: A Multi-Agent LLM Approach for False Positive Reduction in Static Application Security Testing](https://arxiv.org/abs/2605.01885)

**<font color=#1a73e8>作者：</font>** Mohd Ruhul Ameen, Md Takrim Ul Alam, Akif Islam  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Static Application Security Testing tools help developers find security vulnerabilities before release, but they often produce many false positives. This increases manual review effort, reduces developer trust, and may cause real vulnerabilities to be ignored among noisy reports. We present QASecClaw, a multi agent approach that combines conventional Static Application Security Testing with coding specialized Large Language Model based contextual code review. A SAST engine first reports candidate vulnerabilities, and a Large Language Model based SAST Filter Agent then reviews each finding with source code context to decide whether it is likely to be a true positive or a false positive. QASecClaw is coordinated by a Mission Orchestrator and includes specialized agents for test planning, security validation, evidence correlation, filtering, and reporting. We evaluate QASecClaw on OWASP Benchmark v1.2, which contains 2,740 Java test cases across 11 Common Weakness Enumeration categories with ground truth labels. QASecClaw achieves an F1 score of 90.93 percent, compared with 78.39 percent for standalone Semgrep. The improvement is mainly driven by an 88.6 percent reduction in false positives, from 560 to 64, with only a 3.1 percent reduction in recall. These results show that Large Language Model augmented multi agent verification can make Static Application Security Testing output more accurate, useful, and trustworthy.

---


### 11. [Trojan Hippo: Weaponizing Agent Memory for Data Exfiltration](https://arxiv.org/abs/2605.01970)

**<font color=#1a73e8>作者：</font>** Debeshee Das, Julien Piet, Darya Kaviani 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Memory systems enable otherwise-stateless LLM agents to persist user information across sessions, but also introduce a new attack surface. We characterize the Trojan Hippo attack, a class of persistent memory attacks that operates in a more realistic threat model than prior memory poisoning work: the attacker plants a dormant payload into an agent's long-term memory via a single untrusted tool call (e.g., a crafted email), which activates only when the user later discusses sensitive topics such as finance, health, or identity, and exfiltrates high-value personal data to the attacker.
While anecdotal demonstrations of such attacks have appeared against deployed systems, no prior work systematically evaluates them across heterogeneous memory architectures and this http URL introduce a dynamic evaluation framework comprising two components: (1) an OpenEvolve-based adaptive red-teaming benchmark that stress-tests defenses and memory backends against continuously refined attacks, and (2) the first capability-aware security/utility analysis for persistent memory systems, enabling principled reasoning about defense deployment across different usage profiles.
Instantiated on an email assistant across four memory backends (explicit tool memory, agentic memory, RAG, and sliding-window context), Trojan Hippo achieves up to 85-100 percent ASR against current frontier models from OpenAI and Google, with planted memories successfully activating even after 100 benign sessions. We evaluate four memory-system defenses inspired by basic security principles, finding they substantially reduce attack success rates (to as low as 0-5 percent), though at utility costs that vary widely with task requirements. Because of this substantial security-utility tradeoff, the effective real-world deployment of defenses remains an open challenge, which our evaluation framework is specifically designed to address.

---


### 12. [When Alignment Isn't Enough: Response-Path Attacks on LLM Agents](https://arxiv.org/abs/2605.02187)

**<font color=#1a73e8>作者：</font>** Mingyu Luo, Zihan Zhang, Zesen Liu 等 10 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bring-Your-Own-Key (BYOK) agent architectures let users route LLM traffic through third-party relays, creating a critical integrity gap: a malicious relay can modify an aligned LLM response after generation but before agent execution. We formalize this post-alignment tampering threat and show that, without end-to-end integrity, the relay can observe, suppress, or replace downstream messages, making even perfectly aligned LLMs ineffective against such attacks. We instantiate this threat as the Relay Tampering Attack (RTA), which performs multi-round strategic rewriting, minimal security-critical edits, and stealth restoration by resubmitting tampered outputs to the upstream LLM. Across AgentDojo and ASB with six LLMs, RTA achieves up to 99.1% attack success, outperforming prompt-injection baselines with modest overhead. Case studies on OpenClaw and Claude Code demonstrate real-world feasibility, and evaluations of four defenses show that none fully prevent RTA. Finally, we propose a time-based detection defense that mitigates RTA while preserving agent utility.

---


### 13. [On the Privacy of LLMs: An Ablation Study](https://arxiv.org/abs/2605.02255)

**<font color=#1a73e8>作者：</font>** Karima Makhlouf, Lamiaa Basyoni, Syed Khaderi 等 7 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Large language models (LLMs) are increasingly deployed in interactive and retrieval-augmented settings, raising significant privacy concerns. While attacks such as Membership Inference (MIA), Attribute Inference (AIA), Data Extraction (DEA), and Backdoor Attacks (BA) have been studied, they are typically analyzed in isolation, leaving a gap in understanding their behavior under common system factors. In this paper, we introduce a unified threat model and notation, reproduce a representative set of privacy attacks, and conduct a structured ablation study to evaluate the impact of key factors such as model architecture, scale, dataset characteristics, and retrieval configuration. Our analysis reveals clear differences across attack types. Membership inference attacks, particularly mask-based variants, exhibit strong and reliable signals, while backdoor attacks achieve consistently high success rates due to their trigger-based nature. In contrast, attribute inference and data extraction attacks remain more challenging, resulting in lower accuracy, yet they pose significant risks as they target sensitive personal information. Overall, these results highlight that privacy risks in LLM systems are highly context-dependent and driven by design choices, emphasizing the need for holistic evaluation and informed deployment practices.

---


### 14. [APIOT: Autonomous Vulnerability Management Across Bare-Metal Industrial OT Networks](https://arxiv.org/abs/2605.02346)

**<font color=#1a73e8>作者：</font>** Adel ElZemity, Budi Arief, Shujun Li 等 9 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Bare-metal operational technology (OT) devices -- especially the microcontrollers running Modbus/TCP and CoAP at the base of industrial control systems -- have remained outside the reach of autonomous security attacks. Prior autonomous pentesting studies target Linux and web systems, whose shells and filesystems are familiar to LLM agents. Bare-metal OT has neither, so agents must reason directly over protocol fields and parser semantics. This requires new action-space designs and runtime controls, and opens new research questions about protocol-level exploit reasoning and its deployment envelope. We present APIOT (Autonomous Purple-teaming for Industrial OT), the first large language model (LLM) framework demonstrating an autonomous attack and remediation of bare-metal OT devices, achieving the full discovery -> exploitation -> patching -> verification cycle without step-by-step human intervention. We implemented and evaluated this framework on Zephyr RTOS firmware across heterogeneous industrial IoT (IIoT) topologies. Through 290 experiment runs spanning five frontier LLMs, three network topologies, two impairment levels, and guided versus unguided conditions, APIOT achieved a mission success rate of 90.0% on the full attack-remediation cycle. We found that the runtime governance layer (which we call an overseer) is a critical engineering variable: without it, agents exhibit systematic degenerate patterns, including repetition loops, missing crash verification, and reconnaissance deadlocks. Together, these findings carry two implications beyond our testbed. Attacker expertise is no longer the binding constraint on bare-metal OT exploitation, and defender threat models must now assume LLM-augmented adversaries capable of executing autonomous discovery-through-remediation cycles against industrial firmware.

---


### 15. [VertMark: A Unified Training-Free Robust Watermarking Framework for Vertical Domain Pre-trained Language Models](https://arxiv.org/abs/2605.02557)

**<font color=#1a73e8>作者：</font>** Cong Kong, Xin Cheng, Zhaoxia Yin 等 6 位作者  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> With the application of vertical domain pre-trained language models (VPLMs) in specialized fields such as medical, finance, and law, model parameters and inference capabilities have become important digital assets. Achieving traceable copyright verification for VPLMs has become an urgent challenge. Existing copyright verification methods primarily rely on embedding backdoor watermarks into models. However, most of these methods require additional training, suffer from inefficient watermark embedding, and lack scalable designs for multiple vertical domains. To address these limitations, we propose VertMark, the first unified training-free and robust watermarking framework for copyright verification across multiple vertical domain VPLMs. The framework embeds ownership-encoded watermarks by establishing a hidden semantic equivalence between low-frequency trigger tokens and high-frequency domain-relevant words via a training-free parameter replacement strategy. Experiments demonstrate that VertMark can achieve efficient watermark embedding and reliable watermark verification for both text understanding and text generation downstream tasks in the medical, financial, and legal domains, with negligible impact on model performance. Moreover, VertMark exhibits strong robustness against various attacks (e.g., pruning and quantization), highlighting its practical value and providing strong protection for the copyright security of VPLMs.

---


### 16. [FunFuzz: An LLM-Powered Evolutionary Fuzzing Framework](https://arxiv.org/abs/2605.02789)

**<font color=#1a73e8>作者：</font>** Mario Rodríguez Béjar, B. Romera-Paredes, Jose L. Hernández-Ramos  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Modern fuzzers increasingly use Large Language Models (LLMs) to generate structured inputs, but LLM-driven fuzzing is sensitive to prompt initialization and sampling variance, which can reduce exploration efficiency and lead to redundant inputs. We present FunFuzz, a multi-island evolutionary fuzzing framework that runs several isolated searches in parallel and periodically migrates high-value candidates to maintain diversity. FunFuzz derives initial generation prompts from documentation and initializes islands with topic-specific instructions, then continuously adapts prompts using feedback-guided selection. During fuzzing, candidates are prioritized by incremental compiler coverage, while compiler-internal failure signals are used to identify crash-inducing inputs. We evaluate FunFuzz on compiler fuzzing, where inputs are source programs and success is measured by compiler coverage and unique compiler-internal failures. Across repeated 24-hour campaigns on GCC and Clang, FunFuzz achieves higher compiler coverage than previous LLM-driven baselines and discovers more unique failure-triggering inputs.

---


### 17. [Autonomous LLM Agent Worms: Cross-Platform Propagation, Automated Discovery and Temporal Re-Entry Defense](https://arxiv.org/abs/2605.02812)

**<font color=#1a73e8>作者：</font>** Mingming Zha, Xiaofeng Wang  
**<font color=#188038>arXiv所属领域：</font>** Cryptography and Security

**<font color=#5f6368>摘要：</font>**
> Autonomous LLM agents operate as long-running processes with persistent workspaces, memory files, scheduled task state, and messaging integrations. These features create a new propagation risk: attacker-influenced content can be written into persistent agent state, re-enter the LLM decision context through scheduled autoloading, and drive high-risk actions including configuration changes and cross-agent transmission. We present the first systematic framework for automated analysis of persistent worm propagation in file-backed multi-agent LLM ecosystems. SSCGV, our automated source-code graph analyzer, traces data flow from file I/O to LLM context injection points and ranks carriers by context injection position without manual analysis. SRPO, our summary-resilient payload optimizer, generates worm payloads robust to LLM-mediated summarization and paraphrasing across multi-hop communication. Evaluated on three production agent frameworks, we demonstrate zero-click autonomous propagation, 3-hop cross-platform transmission without platform-specific adaptation, inter-agent privilege escalation, and data exfiltration. We identify two empirical insights: user prompt carriers achieve higher attack compliance than system prompt carriers, and read operations represent the primary integrity threat in LLM-mediated systems. To defend against this class of attacks, we develop RTW-A, proven under a formal No Persistent Worm Propagation theorem. RTW blocks write-before-exposed-read re-entry; sealed configuration protects static files; typed memory promotion prevents untrusted summaries from entering trusted memory; and capability attenuation limits high-risk actions after external reads. These mechanisms eliminate the persistence, re-entry, action chain while preserving ordinary workflows. Affected systems are anonymized pending coordinated disclosure.

---


> [!TIP]
> - [返回当日日报目录](../index.md)

*本日报由 AI 自动生成，数据来源：[arXiv.org](https://arxiv.org)*
